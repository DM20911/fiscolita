#!/usr/bin/env python3
"""Descarga jurisprudencia administrativa (oficios) 2019+ vía API pública del SII.
Uso: python3 -I oficios.py <dir_base>
Salida: raw/jurisprudencia_api/<KEY>/<year>/<archivo>.pdf + meta.json ; docs/... .md
"""
import json, os, sys, time, subprocess, re
import requests
from concurrent.futures import ThreadPoolExecutor

BASE = sys.argv[1]
OUT = os.path.join(BASE, "raw", "jurisprudencia_api")
DOCS = os.path.join(BASE, "docs", "jurisprudencia_api")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124 Safari/537.36"
s = requests.Session(); s.headers["User-Agent"] = UA
YEARS = range(2019, 2027)
KEYS = {"RENTA": "Ley de Impuesto a la Renta", "IVA": "Ley de Impuesto a las Ventas y Servicios", "OTROS": "Otras normas"}


def lista(key, y):
    r = s.post("https://www3.sii.cl/getPublicacionesCTByMateria", data=json.dumps({"key": key, "year": str(y)}),
               headers={"Content-Type": "application/json"}, timeout=60)
    r.raise_for_status()
    return r.json()


def bajar(item):
    key, y, it = item
    d = os.path.join(OUT, key, str(y)); os.makedirs(d, exist_ok=True)
    name = re.sub(r"[^\w.\-]", "_", it.get("nombreArchPublica") or f"{it['pubNumOficio']}.pdf")
    p = os.path.join(d, name)
    if not os.path.exists(p) or os.path.getsize(p) == 0:
        time.sleep(0.3)
        try:
            r = s.get("https://www4.sii.cl/gabineteAdmInternet/descargaArchivo", params={
                "nombreDocumento": f"{it['pubNumOficio']}-{it['pubFechaPubli']}.pdf", "extension": it.get("extensionArchPublica") or "pdf",
                "acc": "download", "id": it["idBlobArchPublica"], "mediaType": it.get("mTypeArchPublica") or "application/pdf"}, timeout=90)
            if r.status_code != 200 or len(r.content) < 200:
                return f"ERR {r.status_code} {name}"
            open(p, "wb").write(r.content)
        except Exception as e:
            return f"ERR {e} {name}"
    txt = ""
    if p.endswith(".pdf"):
        txt = subprocess.run(["pdftotext", "-enc", "UTF-8", p, "-"], capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
    else:
        txt = subprocess.run(["textutil", "-convert", "txt", "-stdout", p], capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
    txt = re.sub(r"\n\s*\n\s*\n+", "\n\n", txt.replace("\f", "\n\n")).strip()
    md = os.path.join(DOCS, key, str(y), name + ".md"); os.makedirs(os.path.dirname(md), exist_ok=True)
    titulo = f"{it.get('tipoArchPublica','Oficio')} N° {it['pubNumOficio']} de {it['pubFechaPubli']} – {it.get('pubResumen','')}".replace("\n", " ")
    with open(md, "w", encoding="utf-8") as f:
        f.write(f"---\nurl: https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/indice_jadm.htm\n"
                f"titulo: {titulo}\ncategoria: jurisprudencia\nmateria: {KEYS[key]}\nnumero: {it['pubNumOficio']}\n"
                f"fecha: {it['pubFechaPubli']}\nreferencia_legal: {it.get('pubLegal','')}\n---\n"
                f"# {titulo}\n\n**Materia:** {KEYS[key]}  \n**Referencia legal:** {it.get('pubLegal','')}  \n"
                f"**Resumen SII:** {it.get('pubResumen','')}\n\n{txt}\n")
    return "OK"


def main():
    todo, meta = [], []
    for k in KEYS:
        for y in YEARS:
            try:
                items = lista(k, y)
            except Exception as e:
                print("lista", k, y, e); continue
            print(k, y, len(items), flush=True)
            for it in items:
                it["_key"] = k; meta.append(it); todo.append((k, y, it))
    os.makedirs(OUT, exist_ok=True)
    json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), ensure_ascii=False, indent=1)
    errs = 0
    with ThreadPoolExecutor(4) as ex:
        for i, r in enumerate(ex.map(bajar, todo), 1):
            if r != "OK":
                errs += 1; print(r, flush=True)
            if i % 200 == 0:
                print("oficios", i, "/", len(todo), flush=True)
    print("FIN oficios", len(todo), "errores", errs)


if __name__ == "__main__":
    main()
