#!/usr/bin/env python3
"""Descarga texto VIGENTE de las leyes enlazadas desde legislación tributaria básica/complementaria (BCN LeyChile XML)
y las agrega a docs/leyes_vigentes + índice FTS. Uso: python3 -I leyes.py <dir_base>"""
import os, re, sys, time, sqlite3
import requests
from lxml import etree

BASE = sys.argv[1]
DOCS = os.path.join(BASE, "docs")
OUT = os.path.join(DOCS, "leyes_vigentes"); os.makedirs(OUT, exist_ok=True)
RAWO = os.path.join(BASE, "raw", "leyes_vigentes"); os.makedirs(RAWO, exist_ok=True)
NS = {"n": "http://www.leychile.cl/esquemas"}
s = requests.Session(); s.headers["User-Agent"] = "Mozilla/5.0"

ids = {}
for page in ("legislacion_tributaria_basica.html.md", "legislacion_tributaria_complementaria.html.md"):
    p = os.path.join(DOCS, "normativa_legislacion", page)
    if not os.path.exists(p):
        continue
    for name, idn in re.findall(r"\[([^\]]+)\]\([^)]*idNorma=(\d+)", open(p, encoding="utf-8").read()):
        ids.setdefault(idn, name.strip())
print(len(ids), "normas", flush=True)

ix = sqlite3.connect(os.path.join(BASE, "busqueda.sqlite"))
ix.execute("DELETE FROM docs WHERE categoria='ley'")
for idn, name in ids.items():
    xp = os.path.join(RAWO, f"{idn}.xml")
    if not os.path.exists(xp):
        time.sleep(1)
        r = s.get(f"https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma={idn}", timeout=120)
        if r.status_code != 200 or not r.content.startswith(b"<?xml"):
            print("ERR", idn, name, r.status_code); continue
        open(xp, "wb").write(r.content)
    try:
        root = etree.parse(xp).getroot()
    except Exception as e:
        print("ERR xml", idn, e); continue
    fv = root.get("fechaVersion", "")
    tit = " ".join(t.text or "" for t in root.findall(".//n:Metadatos/n:TituloNorma", NS)).strip()
    tn = " ".join(f"{(x.findtext('n:Tipo', namespaces=NS) or '')} {(x.findtext('n:Numero', namespaces=NS) or '')}"
                  for x in root.findall(".//n:Identificador/n:TiposNumeros/n:TipoNumero", NS)).strip()
    parts = []
    enc = root.findtext("n:Encabezado/n:Texto", namespaces=NS)
    if enc:
        parts.append(enc.strip())
    for ef in root.iter("{http://www.leychile.cl/esquemas}EstructuraFuncional"):
        t = ef.findtext("n:Texto", namespaces=NS)
        if t and t.strip():
            tipo = ef.get("tipoParte", "")
            der = " (DEROGADO)" if ef.get("derogado") == "derogado" else ""
            parts.append((f"### {tipo}{der}\n\n" if tipo and tipo != "Artículo" else "") + re.sub(r"[ \t]+\n", "\n", t.strip()))
    body = "\n\n".join(parts)
    body = re.sub(r"\n(Artículo|ARTICULO|Art\.)\s", r"\n\n#### \1 ", body)
    slug = re.sub(r"[^\w]+", "_", f"{tn}_{name}".lower()).strip("_")[:90] + f"_{idn}"
    url = f"https://www.bcn.cl/leychile/navegar?idNorma={idn}"
    title = f"{tn} – {name} (texto vigente al {fv})"
    if idn == "172986":
        title = "DFL 1 (2000) – Ley de Impuesto a las Herencias, Asignaciones y Donaciones (Ley 16.271, en texto refundido junto al Código Civil)"
    md = os.path.join(OUT, slug + ".md")
    with open(md, "w", encoding="utf-8") as f:
        f.write(f"---\nurl: {url}\ntitulo: {title}\ncategoria: ley\nversion: {fv}\n---\n# {title}\n\n{tit}\n\n{body}\n")
    ix.execute("INSERT INTO docs VALUES(?,?,?,?,?)", (title, url, os.path.relpath(md, BASE), "ley", body))
    print("OK", idn, tn, name, fv, len(body), flush=True)
ix.commit()
