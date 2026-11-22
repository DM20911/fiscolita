#!/usr/bin/env python3
"""Actualización diaria automática de FiscolItA.

La primera vez que se usa en el día (buscar.py, servidor MCP o bot de Telegram lo llaman solos),
revisa en www.sii.cl las circulares, resoluciones y oficios del año en curso, descarga los que
no estén en docs/, los convierte a .md y los agrega al índice de búsqueda.

  python3 actualizar_novedades.py            # corre solo si hoy no se ha revisado
  python3 actualizar_novedades.py --forzar   # revisa igual
  FISCOLITA_SIN_ACTUALIZAR=1                 # desactiva la revisión automática

Si no hay internet o el SII no responde, no hace nada y no interrumpe la consulta.
"""
import datetime, json, os, re, sqlite3, subprocess, sys, tempfile, time
from urllib.parse import urljoin

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "busqueda.sqlite")
ESTADO = os.path.join(HERE, "config", "actualizacion.json")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
MATERIAS = {"RENTA": "Ley de Impuesto a la Renta", "IVA": "Ley de Impuesto a las Ventas y Servicios", "OTROS": "Otras normas"}


def _log(*a):
    print("[actualización]", *a, file=sys.stderr, flush=True)


def _pdf2txt(data):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(data); f.flush()
        t = subprocess.run(["pdftotext", "-enc", "UTF-8", f.name, "-"], capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", t.replace("\f", "\n\n")).strip()


def _guardar(rel, url, titulo, categoria, cuerpo, extra=""):
    p = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    titulo = re.sub(r"\s+", " ", titulo).strip()
    with open(p, "w", encoding="utf-8") as f:
        f.write(f"---\nurl: {url}\ntitulo: {titulo}\ncategoria: {categoria}\n{extra}---\n{cuerpo}\n")
    if os.path.exists(DB):
        con = sqlite3.connect(DB)
        con.execute("DELETE FROM docs WHERE archivo = ?", (rel,))
        con.execute("INSERT INTO docs VALUES(?,?,?,?,?)", (titulo, url, rel, categoria, cuerpo))
        con.commit(); con.close()
    return titulo


def _indice_normas(s, tipo, anio):
    """Circulares o resoluciones del año: lista (titulo, url_pdf, descripcion)."""
    from bs4 import BeautifulSoup
    url = {"circulares": f"https://www.sii.cl/normativa_legislacion/circulares/{anio}/indcir{anio}.htm",
           "resoluciones": f"https://www.sii.cl/normativa_legislacion/resoluciones/{anio}/res_ind{anio}.htm"}[tipo]
    r = s.get(url, timeout=60)
    if r.status_code != 200:
        return []
    r.encoding = r.apparent_encoding
    out = []
    for h5 in BeautifulSoup(r.text, "lxml").find_all("h5"):
        a = h5.find("a", href=True)
        if a and a["href"].strip().lower().endswith(".pdf"):
            p = h5.find_next_sibling("p")
            out.append((a.get_text(" ", strip=True), urljoin(url, a["href"].strip()), p.get_text(" ", strip=True) if p else ""))
    return out


def _normas(s, tipo, anio, nuevos):
    cat = "circular" if tipo == "circulares" else "resolucion"
    for t, u, d in _indice_normas(s, tipo, anio):
        rel = f"docs/normativa_legislacion/{tipo}/{anio}/{u.rsplit('/', 1)[1]}.md"
        if os.path.exists(os.path.join(HERE, rel)):
            continue
        r = s.get(u, timeout=90); time.sleep(0.3)
        if r.status_code != 200 or len(r.content) < 200:
            continue
        nuevos.append(_guardar(rel, u, f"{t} – {d}" if d else t, cat, _pdf2txt(r.content)))


def _oficios(s, anio, nuevos):
    for k, nombre in MATERIAS.items():
        r = s.post("https://www3.sii.cl/getPublicacionesCTByMateria", data=json.dumps({"key": k, "year": str(anio)}),
                   headers={"Content-Type": "application/json"}, timeout=60)
        if r.status_code != 200:
            continue
        for it in r.json():
            name = re.sub(r"[^\w.\-]", "_", it.get("nombreArchPublica") or f"{it['pubNumOficio']}.pdf")
            rel = f"docs/jurisprudencia_api/{k}/{anio}/{name}.md"
            if os.path.exists(os.path.join(HERE, rel)):
                continue
            d = s.get("https://www4.sii.cl/gabineteAdmInternet/descargaArchivo", params={
                "nombreDocumento": f"{it['pubNumOficio']}-{it['pubFechaPubli']}.pdf", "extension": it.get("extensionArchPublica") or "pdf",
                "acc": "download", "id": it["idBlobArchPublica"], "mediaType": it.get("mTypeArchPublica") or "application/pdf"}, timeout=90)
            time.sleep(0.3)
            if d.status_code != 200 or len(d.content) < 200 or not d.content.startswith(b"%PDF"):
                continue
            titulo = f"{it.get('tipoArchPublica', 'Oficio')} N° {it['pubNumOficio']} de {it['pubFechaPubli']} – {it.get('pubResumen', '')}"
            cuerpo = (f"# {titulo}\n\n**Materia:** {nombre}  \n**Referencia legal:** {it.get('pubLegal', '')}  \n"
                      f"**Resumen SII:** {it.get('pubResumen', '')}\n\n{_pdf2txt(d.content)}")
            extra = (f"materia: {nombre}\nnumero: {it['pubNumOficio']}\nfecha: {it['pubFechaPubli']}\n"
                     f"referencia_legal: {re.sub(chr(10), ' ', it.get('pubLegal', ''))}\n")
            nuevos.append(_guardar(rel, "https://www.sii.cl/normativa_legislacion/jurisprudencia_administrativa/indice_jadm.htm",
                                   titulo, "jurisprudencia", cuerpo, extra))


def _leer_estado():
    try:
        return json.load(open(ESTADO, encoding="utf-8"))
    except Exception:
        return {}


def actualizar(forzar=False):
    """Devuelve la lista de títulos agregados (vacía si no había nada o ya se revisó hoy)."""
    hoy = datetime.date.today().isoformat()
    est = _leer_estado()
    if not forzar and (est.get("ultima_revision") == hoy or os.environ.get("FISCOLITA_SIN_ACTUALIZAR")):
        return []
    try:
        import requests
        s = requests.Session(); s.headers.update(UA)
        s.get("https://www.sii.cl/", timeout=15)
    except Exception:
        return []  # sin conexión: se reintenta en la próxima consulta
    _log("primera consulta del día: revisando circulares, resoluciones y oficios nuevos en www.sii.cl…")
    nuevos, anio = [], datetime.date.today().year
    for paso in (lambda: _normas(s, "circulares", anio, nuevos), lambda: _normas(s, "resoluciones", anio, nuevos),
                 lambda: _oficios(s, anio, nuevos)):
        try:
            paso()
        except Exception as e:
            _log("aviso:", type(e).__name__, e)
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    hist = (est.get("agregados") or [])[-200:] + [{"fecha": hoy, "titulo": t} for t in nuevos]
    json.dump({"ultima_revision": hoy, "agregados": hist}, open(ESTADO, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    _log(f"{len(nuevos)} documento(s) nuevo(s) agregado(s)." if nuevos else "sin novedades.")
    for t in nuevos:
        _log("  +", t[:140])
    return nuevos


def asegurar_al_dia():
    """Uso interno: nunca lanza excepción."""
    try:
        return actualizar()
    except Exception as e:
        _log("omitida:", e)
        return []


if __name__ == "__main__":
    actualizar(forzar="--forzar" in sys.argv)
