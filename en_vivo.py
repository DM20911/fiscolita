#!/usr/bin/env python3
"""Consultas EN VIVO a www.sii.cl (complemento de la base local, para datos que dependen de la fecha).
Uso:
  python3 en_vivo.py circulares [-n 5] [--anio 2026]
  python3 en_vivo.py resoluciones [-n 5] [--anio 2026]
  python3 en_vivo.py oficios [-n 5] [--materia RENTA|IVA|OTROS] [--anio 2026]
  python3 en_vivo.py valor utm|uf|dolar [--anio 2026]     # tabla del año en markdown
  python3 en_vivo.py pagina <url www.sii.cl>              # cualquier página o PDF del SII como texto
"""
import argparse, datetime, json, re, subprocess, sys, tempfile
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
HOY = datetime.date.today()


def get(url):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    return r


def html_text(r):
    r.encoding = r.apparent_encoding if not r.encoding or r.encoding.lower() == "iso-8859-1" else r.encoding
    return r.text


def indice(url, n):
    soup = BeautifulSoup(html_text(get(url)), "lxml")
    out = []
    for h in soup.find_all("h5"):
        a = h.find("a", href=True)
        if not a:
            continue
        p = h.find_next_sibling("p")
        out.append((a.get_text(" ", strip=True), urljoin(url, a["href"].strip()), p.get_text(" ", strip=True) if p else ""))
        if len(out) >= n:
            break
    return out


def pagina(url):
    if urlparse(url).netloc not in ("www.sii.cl", "sii.cl"):
        sys.exit("Solo www.sii.cl")
    r = get(url)
    if "pdf" in r.headers.get("Content-Type", "") or url.lower().endswith(".pdf"):
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(r.content); f.flush()
            return subprocess.run(["pdftotext", "-enc", "UTF-8", f.name, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    soup = BeautifulSoup(html_text(r), "lxml")
    for t in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        t.decompose()
    main = soup.find(id="contenido") or soup.find(class_="cuerpo") or soup.body or soup
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", md(str(main), heading_style="ATX", strip=["img"])).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tipo", choices=["circulares", "resoluciones", "oficios", "valor", "pagina"])
    ap.add_argument("arg", nargs="?")
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--anio", type=int, default=HOY.year)
    ap.add_argument("--materia", default=None)
    a = ap.parse_args()
    if a.tipo == "circulares":
        url = f"https://www.sii.cl/normativa_legislacion/circulares/{a.anio}/indcir{a.anio}.htm"
        for t, u, d in indice(url, a.n):
            print(f"- {t}\n  {d}\n  {u}")
    elif a.tipo == "resoluciones":
        url = f"https://www.sii.cl/normativa_legislacion/resoluciones/{a.anio}/res_ind{a.anio}.htm"
        for t, u, d in indice(url, a.n):
            print(f"- {t}\n  {d}\n  {u}")
    elif a.tipo == "oficios":
        items = []
        for k in ([a.materia] if a.materia else ["RENTA", "IVA", "OTROS"]):
            r = requests.post("https://www3.sii.cl/getPublicacionesCTByMateria", headers={**UA, "Content-Type": "application/json"},
                              data=json.dumps({"key": k, "year": str(a.anio)}), timeout=60)
            for it in r.json():
                it["_k"] = k; items.append(it)
        items.sort(key=lambda i: datetime.datetime.strptime(i["pubFechaPubli"], "%d/%m/%Y"), reverse=True)
        for it in items[:a.n]:
            print(f"- [{it['_k']}] {it['tipoArchPublica']} N° {it['pubNumOficio']} de {it['pubFechaPubli']}: {it['pubResumen']}\n  Ref. legal: {it['pubLegal']}")
    elif a.tipo == "valor":
        k = (a.arg or "utm").lower()
        url = {"utm": f"https://www.sii.cl/valores_y_fechas/utm/utm{a.anio}.htm",
               "uf": f"https://www.sii.cl/valores_y_fechas/uf/uf{a.anio}.htm",
               "dolar": f"https://www.sii.cl/valores_y_fechas/dolar/dolar{a.anio}.htm"}[k]
        print(f"Fuente: {url}\n"); print(pagina(url)[:15000])
    elif a.tipo == "pagina":
        print(pagina(a.arg))


if __name__ == "__main__":
    main()
