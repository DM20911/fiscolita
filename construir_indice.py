#!/usr/bin/env python3
"""Construye busqueda.sqlite (índice de texto completo FTS5) a partir de docs/**/*.md.
Se ejecuta solo la primera vez (buscar.py y el MCP lo llaman si falta). ~1-2 minutos.
  python3 construir_indice.py
"""
import os, re, sqlite3, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "busqueda.sqlite")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def campo(fm, k):
    m = re.search(rf"^{k}: (.*)$", fm, re.M)
    return m.group(1).strip() if m else ""


def construir(verbose=True):
    t0 = time.time(); tmp = DB + ".tmp"
    if os.path.exists(tmp):
        os.remove(tmp)
    con = sqlite3.connect(tmp)
    con.execute("CREATE VIRTUAL TABLE docs USING fts5(titulo, url UNINDEXED, archivo UNINDEXED, categoria, cuerpo, tokenize='unicode61 remove_diacritics 2')")
    n = 0
    for root, _, files in os.walk(os.path.join(HERE, "docs")):
        for f in files:
            if not f.endswith(".md") or "_catalogos" in root:
                continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf-8", errors="replace").read()
            m = FM.match(t)
            fm, body = (m.group(1), t[m.end():]) if m else ("", t)
            con.execute("INSERT INTO docs VALUES(?,?,?,?,?)", (campo(fm, "titulo") or f, campo(fm, "url"),
                        os.path.relpath(p, HERE), campo(fm, "categoria") or "otros", body))
            n += 1
            if verbose and n % 5000 == 0:
                print(f"  {n} documentos…", file=sys.stderr, flush=True)
    con.commit()
    con.execute("INSERT INTO docs(docs) VALUES('optimize')"); con.commit(); con.close()
    os.replace(tmp, DB)
    if verbose:
        print(f"Índice listo: {n} documentos en {time.time() - t0:.0f}s → {DB}", file=sys.stderr)
    return n


def asegurar():
    if not os.path.exists(DB):
        print("Primera ejecución: construyendo índice de búsqueda (1-2 min)…", file=sys.stderr)
        construir()


if __name__ == "__main__":
    construir()
