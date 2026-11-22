#!/usr/bin/env python3
"""Convierte raw/ -> docs/ (markdown) y construye índice FTS5 (busqueda.sqlite).
Incremental: solo reconvierte si raw es más nuevo que el .md.
Uso: python3 -I convertir.py <dir_base>
"""
import os, re, sys, sqlite3, subprocess
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = sys.argv[1]
RAW, DOCS = os.path.join(BASE, "raw"), os.path.join(BASE, "docs")
CRAWL = os.path.join(BASE, "_tools", "crawl.sqlite")
IDX = os.path.join(BASE, "busqueda.sqlite")


def decode(b):
    m = re.search(rb'charset=["\']?([A-Za-z0-9_\-]+)', b[:3000])
    for enc in ([m.group(1).decode()] if m else []) + ["utf-8", "cp1252", "latin-1"]:
        try:
            return b.decode(enc)
        except Exception:
            continue
    return b.decode("latin-1", "replace")


def html2md(path):
    soup = BeautifulSoup(decode(open(path, "rb").read()), "lxml")
    title = (soup.title.get_text(" ", strip=True) if soup.title else "")
    for t in soup(["script", "style", "noscript", "header", "footer", "nav", "form", "iframe", "svg"]):
        t.decompose()
    cands = [x for x in [soup.find(id="contenido"), soup.find(class_="contenido"), soup.find(class_="cuerpo"),
                         soup.find("main"), soup.find(id="my-wrapper")] if x is not None]
    body = soup.body or soup
    good = [x for x in cands if len(x.get_text(strip=True)) > 0.3 * len(body.get_text(strip=True))]
    main = good[0] if good else body
    q = soup.find(id="div-pregunta")
    if q and q.get_text(strip=True):
        title = q.get_text(" ", strip=True)
    else:
        h1 = main.find(["h1", "h2"])
        if h1 and h1.get_text(strip=True) and (len(title) < 5 or "SII |" in title or "Servicio de Impuestos" in title or title == "Preguntas Frecuentes"):
            title = h1.get_text(" ", strip=True)
    text = md(str(main), heading_style="ATX", strip=["img"])
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text).strip()
    return title, text


def pdf2md(path):
    try:
        out = subprocess.run(["pdftotext", "-enc", "UTF-8", path, "-"], capture_output=True, timeout=180).stdout.decode("utf-8", "replace")
    except Exception as e:
        out = f"[error pdftotext: {e}]"
    out = re.sub(r"\f", "\n\n", out)
    out = re.sub(r"\n\s*\n\s*\n+", "\n\n", out).strip()
    first = next((l.strip() for l in out.splitlines() if len(l.strip()) > 8), "")
    return first[:150], out


def xls2md(path):
    import pandas as pd
    parts = []
    try:
        for name, df in pd.read_excel(path, sheet_name=None, header=None).items():
            df = df.dropna(how="all").dropna(axis=1, how="all").fillna("")
            parts.append(f"## Hoja: {name}\n\n" + df.to_csv(sep="|", index=False, header=False))
    except Exception as e:
        parts.append(f"[error excel: {e}]")
    return os.path.basename(path), "\n\n".join(parts)


def doc2md(path):
    try:
        out = subprocess.run(["textutil", "-convert", "txt", "-stdout", path], capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
    except Exception as e:
        out = f"[error textutil: {e}]"
    return os.path.basename(path), out


def categoria(rel):
    r = rel.lower()
    for k, v in [("normativa_legislacion/circulares", "circular"), ("normativa_legislacion/resoluciones", "resolucion"),
                 ("documentos/circulares", "circular"), ("documentos/resoluciones", "resolucion"),
                 ("normativa_ddrr", "resolucion_regional"), ("jurisprudencia", "jurisprudencia"),
                 ("normativa_legislacion", "normativa"), ("preguntas_frecuentes", "faq"), ("valores_y_fechas", "valores"),
                 ("servicios_online", "servicios_online"), ("ayudas", "ayuda"), ("destacados", "destacado"),
                 ("noticias", "noticia"), ("factura_electronica", "factura_electronica"), ("declaraciones_juradas", "declaraciones_juradas"),
                 ("sobre_el_sii", "sobre_el_sii"), ("portales", "portal"), ("formularios", "formulario")]:
        if k in r:
            return v
    return "otros"


def job(args):
    url, rel, ctype = args
    src = os.path.join(BASE, rel)
    out = os.path.join(DOCS, os.path.relpath(src, RAW)) + ".md"
    ext = os.path.splitext(src)[1].lower()
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
        try:
            t = open(out, encoding="utf-8").read()
            title = re.search(r"^titulo: (.*)$", t, re.M).group(1)
            return url, os.path.relpath(out, BASE), title, t.split("---\n", 2)[-1]
        except Exception:
            pass
    try:
        if "pdf" in (ctype or "") or ext == ".pdf":
            title, body = pdf2md(src)
        elif ext in (".xls", ".xlsx") or "excel" in (ctype or "") or "spreadsheet" in (ctype or ""):
            title, body = xls2md(src)
        elif ext in (".doc", ".docx", ".rtf") or "msword" in (ctype or "") or "wordprocessing" in (ctype or ""):
            title, body = doc2md(src)
        elif "html" in (ctype or "") or ext in (".htm", ".html", ".shtml", ""):
            title, body = html2md(src)
        elif ext in (".txt", ".csv", ".xml"):
            title, body = os.path.basename(src), decode(open(src, "rb").read())
        else:
            return None
    except Exception as e:
        title, body = os.path.basename(src), f"[error conversión: {e}]"
    title = re.sub(r"\s+", " ", title or "").strip() or os.path.basename(src)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"---\nurl: {url}\ntitulo: {title}\ncategoria: {categoria(rel)}\n---\n{body}\n")
    return url, os.path.relpath(out, BASE), title, body


def main():
    c = sqlite3.connect(CRAWL)
    rows = c.execute("SELECT url, path, ctype FROM urls WHERE status=200 AND path IS NOT NULL").fetchall()
    seen, uniq = set(), []
    for r in rows:
        if r[1] not in seen:
            seen.add(r[1]); uniq.append(r)
    ix = sqlite3.connect(IDX)
    ix.execute("DROP TABLE IF EXISTS docs")
    ix.execute("CREATE VIRTUAL TABLE docs USING fts5(titulo, url UNINDEXED, archivo UNINDEXED, categoria, cuerpo, tokenize='unicode61 remove_diacritics 2')")
    n = 0
    with ProcessPoolExecutor(8) as ex:
        for res in ex.map(job, uniq, chunksize=20):
            if not res:
                continue
            url, f, title, body = res
            ix.execute("INSERT INTO docs VALUES(?,?,?,?,?)", (title, url, f, categoria(f), body))
            n += 1
            if n % 1000 == 0:
                ix.commit(); print("convertidos", n, flush=True)
    ix.commit()
    # oficios descargados por oficios.py (ya en markdown)
    for root, _, files in os.walk(os.path.join(DOCS, "jurisprudencia_api")):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(root, fn)
            t = open(p, encoding="utf-8").read()
            title = (re.search(r"^titulo: (.*)$", t, re.M) or [None, fn])[1]
            ix.execute("INSERT INTO docs VALUES(?,?,?,?,?)", (title, "https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/indice_jadm.htm",
                                                              os.path.relpath(p, BASE), "jurisprudencia", t.split("---\n", 2)[-1]))
            n += 1
    ix.commit()
    ix.execute("INSERT INTO docs(docs) VALUES('optimize')"); ix.commit()
    print("TOTAL", n)


if __name__ == "__main__":
    main()
