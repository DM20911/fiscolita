#!/usr/bin/env python3
"""Genera catálogos (circulares, resoluciones, oficios, FAQ, apps) e INDICE.md; mejora títulos en FTS.
Uso: python3 -I gen_indice.py <dir_base>
"""
import os, re, sys, json, sqlite3, glob
from collections import defaultdict
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

BASE = sys.argv[1]
RAW, DOCS = os.path.join(BASE, "raw"), os.path.join(BASE, "docs")
CAT = os.path.join(DOCS, "_catalogos"); os.makedirs(CAT, exist_ok=True)
crawl = sqlite3.connect(os.path.join(BASE, "_tools", "crawl.sqlite"))
ix = sqlite3.connect(os.path.join(BASE, "busqueda.sqlite"))
url2path = dict(crawl.execute("SELECT url, path FROM urls WHERE status=200 AND path IS NOT NULL"))
path2url = {v: k for k, v in url2path.items()}


def decode(b):
    m = re.search(rb'charset=["\']?([A-Za-z0-9_\-]+)', b[:3000])
    for enc in ([m.group(1).decode()] if m else []) + ["utf-8", "cp1252", "latin-1"]:
        try:
            return b.decode(enc)
        except Exception:
            pass
    return b.decode("latin-1", "replace")


def mdlink(url):
    p = url2path.get(url)
    if not p:
        return ""
    md = os.path.join("docs", os.path.relpath(os.path.join(BASE, p), RAW)) + ".md"
    return md if os.path.exists(os.path.join(BASE, md)) else ""


def clean(t):
    return re.sub(r"\s+", " ", t or "").strip()


# ---------- circulares y resoluciones: anclas en páginas índice ----------
DOC_RE = re.compile(r"/(circulares|resoluciones)/(\d{4})/[^/]+\.(pdf|htm|html|doc|docx)$", re.I)
items = {}
for path, url in path2url.items():
    if not re.search(r"\.(htm|html)$", path, re.I) or not re.search(r"(circular|resoluc|normativa)", path, re.I):
        continue
    try:
        soup = BeautifulSoup(decode(open(os.path.join(BASE, path), "rb").read()), "lxml")
    except Exception:
        continue
    for a in soup.find_all("a", href=True):
        u = urljoin(url, a["href"].strip()).split("#")[0].replace("http://", "https://")
        m = DOC_RE.search(urlparse(u).path)
        if not m or "normativa_ddrr" in u:
            continue
        txt = clean(a.get_text(" "))
        desc = ""
        blk = a.find_parent(["h5", "h4", "h3", "td", "li", "p"]) or a
        sib = blk.find_next_sibling()
        if blk.name in ("h5", "h4", "h3") and sib is not None and sib.name == "p":
            desc = clean(sib.get_text(" "))
        elif blk.name in ("td", "li", "p"):
            desc = clean(blk.get_text(" ").replace(a.get_text(" "), "", 1))
            if not desc and blk.name == "td":
                tr = blk.find_parent("tr")
                desc = clean(tr.get_text(" ").replace(a.get_text(" "), "", 1)) if tr else ""
        tipo = m.group(1).lower()
        key = u
        old = items.get(key)
        if not old or len(txt) + len(desc) > len(old["t"]) + len(old["d"]):
            items[key] = {"tipo": tipo, "anio": int(m.group(2)), "t": txt, "d": desc[:400], "u": u}

newtitle = {}
for tipo, nombre in (("circulares", "Circulares"), ("resoluciones", "Resoluciones")):
    rows = sorted([x for x in items.values() if x["tipo"] == tipo],
                  key=lambda x: (-x["anio"], -int((re.findall(r"\d+", x["u"].rsplit("/", 1)[1]) or ["0"])[0])))
    with open(os.path.join(CAT, f"{tipo}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Catálogo de {nombre} del SII\n\nFuente: índices anuales en www.sii.cl. {len(rows)} documentos. "
                f"Columna *Local* = texto convertido en este repositorio.\n\n")
        anio = None
        for x in rows:
            if x["anio"] != anio:
                anio = x["anio"]; f.write(f"\n## {anio}\n\n| Documento | Materia | Local |\n|---|---|---|\n")
            loc = mdlink(x["u"])
            f.write(f"| [{x['t'] or x['u'].rsplit('/',1)[1]}]({x['u']}) | {x['d'].replace('|','/')} | {('[md](../../'+loc+')') if loc else '—'} |\n")
            title = clean(f"{x['t']} – {x['d']}")[:300]
            if title and x["t"]:
                newtitle[x["u"]] = title
    print(tipo, len(rows))

rowids = [(r, newtitle[u]) for r, u in ix.execute("SELECT rowid, url FROM docs") if u in newtitle]
ix.executemany("UPDATE docs SET titulo=? WHERE rowid=?", [(t, r) for r, t in rowids]); ix.commit()
print("titulos actualizados", len(rowids), flush=True)

# ---------- oficios (API) ----------
meta_p = os.path.join(RAW, "jurisprudencia_api", "meta.json")
n_of = 0
if os.path.exists(meta_p):
    meta = json.load(open(meta_p))
    n_of = len(meta)
    nom = {"RENTA": "Ley de la Renta", "IVA": "IVA (DL 825)", "OTROS": "Otras normas"}
    with open(os.path.join(CAT, "jurisprudencia_oficios.md"), "w", encoding="utf-8") as f:
        f.write(f"# Jurisprudencia administrativa del SII (oficios) 2019–2026\n\n{n_of} pronunciamientos. "
                "Fuente: API pública `getPublicacionesCTByMateria` usada por www.sii.cl. Años previos: ver "
                "`docs/pagina/jurisprudencia/adminis/` y `docs/normativa_legislacion/jurisprudencia_administrativa/`.\n")
        by = defaultdict(list)
        for it in meta:
            by[(it["_key"], it["pubYear"])].append(it)
        for (k, y) in sorted(by, key=lambda t: (t[0], -t[1])):
            f.write(f"\n## {nom[k]} – {y}\n\n| Oficio | Fecha | Resumen | Referencia legal | Local |\n|---|---|---|---|---|\n")
            for it in sorted(by[(k, y)], key=lambda i: -int(re.sub(r"\D", "", i["pubNumOficio"]) or 0)):
                name = re.sub(r"[^\w.\-]", "_", it.get("nombreArchPublica") or f"{it['pubNumOficio']}.pdf")
                loc = f"docs/jurisprudencia_api/{k}/{y}/{name}.md"
                ok = os.path.exists(os.path.join(BASE, loc))
                f.write(f"| {it['pubNumOficio']} | {it['pubFechaPubli']} | {clean(it.get('pubResumen','')).replace('|','/')} | "
                        f"{clean(it.get('pubLegal','')).replace('|','/')[:200]} | {('[md](../../'+loc+')') if ok else '—'} |\n")

# ---------- FAQ ----------
faq = defaultdict(list)
for t, u, a in ix.execute("SELECT titulo, url, archivo FROM docs WHERE categoria='faq'"):
    m = re.search(r"/preguntas_frecuentes/([^/]+)/(\d{3}_\d{3}_\d{4})\.htm", u)
    if m:
        faq[m.group(1)].append((t, u, a))
with open(os.path.join(CAT, "preguntas_frecuentes.md"), "w", encoding="utf-8") as f:
    tot = sum(len(v) for v in faq.values())
    f.write(f"# Preguntas frecuentes del SII\n\n{tot} preguntas en {len(faq)} temáticas. Fuente: "
            "https://www.sii.cl/preguntas_frecuentes/preguntasfrecuentes.htm\n\n## Temáticas\n\n")
    for k in sorted(faq):
        f.write(f"- [{k.replace('_',' ')}](#{k.replace('_','-')}) ({len(faq[k])})\n")
    for k in sorted(faq):
        f.write(f"\n## {k.replace('_','-')}\n\n")
        for t, u, a in sorted(faq[k]):
            f.write(f"- [{t}](../../{a}) — {u}\n")

# ---------- aplicaciones / servicios en línea (subdominios) ----------
ext = crawl.execute("SELECT url, max(text), count(DISTINCT parent) FROM external GROUP BY url").fetchall()
byhost = defaultdict(list)
for u, t, n in ext:
    byhost[urlparse(u).netloc].append((u, t, n))
with open(os.path.join(CAT, "aplicaciones_y_tramites.md"), "w", encoding="utf-8") as f:
    f.write("# Aplicaciones y trámites en línea a los que lleva www.sii.cl\n\n"
            "Destinos fuera del sitio estático (requieren en general RUT + clave tributaria / Clave Única). "
            "No se descargaron: son aplicaciones transaccionales. *Refs* = cuántas páginas del sitio enlazan ahí.\n")
    for h in sorted(byhost, key=lambda h: -len(byhost[h])):
        f.write(f"\n## {h} ({len(byhost[h])})\n\n| URL | Texto del enlace | Refs |\n|---|---|---|\n")
        for u, t, n in sorted(byhost[h], key=lambda x: -x[2]):
            f.write(f"| {u} | {clean(t).replace('|','/')} | {n} |\n")

ix.commit()

# ---------- estadísticas ----------
stats = dict(ix.execute("SELECT categoria, count(*) FROM docs GROUP BY categoria"))
json.dump({"categorias": stats, "oficios": n_of, "circulares": sum(1 for x in items.values() if x["tipo"] == "circulares"),
           "resoluciones": sum(1 for x in items.values() if x["tipo"] == "resoluciones"),
           "faq": sum(len(v) for v in faq.values()), "apps": len(ext)},
          open(os.path.join(BASE, "_tools", "stats.json"), "w"), indent=1, ensure_ascii=False)
print(json.load(open(os.path.join(BASE, "_tools", "stats.json"))))
