#!/usr/bin/env python3
"""MCP del Asesora TributarIA (no oficial; el SII no tiene MCP).

Herramientas:
  Base local ...... buscar, leer_documento
  En vivo ......... ultimas_normas, valor_indicador, pagina_sii, calculadora
  Cuenta SII ...... sii_login, sii_consultar   (scraping con credenciales del Llavero; SOLO LECTURA)

Credenciales: Llavero de macOS, servicio "asesor-sii", cuenta = RUT sin puntos con guion (12345678-9).
  security add-generic-password -s asesor-sii -a 12345678-9 -w
Nunca se escriben en disco ni se devuelven al modelo.

Ejecutar: uv run --python 3.12 --with "mcp<2" --with requests --with beautifulsoup4 --with lxml --with markdownify python mcp_sii/server.py
"""
import os, re, sqlite3, subprocess, sys, json, datetime, tempfile
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from mcp.server.fastmcp import FastMCP

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "busqueda.sqlite")
sys.path.insert(0, BASE)
from construir_indice import asegurar as _asegurar_indice
_asegurar_indice()
from actualizar_novedades import asegurar_al_dia as _al_dia
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124 Safari/537.36"
KEYCHAIN_SERVICE = os.environ.get("ASESOR_SII_KEYCHAIN", "asesor-sii")

mcp = FastMCP("asesor-tributario-sii")
_sess = None  # sesión autenticada


# ---------------- utilidades ----------------
def _fts(q):
    if re.search(r'["*]|\b(AND|OR|NOT|NEAR)\b', q):
        return q
    return " ".join(f'"{t}"' for t in re.findall(r"\w+", q, re.U) if len(t) > 1)


def _html2md(html):
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        t.decompose()
    main = soup.find(id="contenido") or soup.find(class_="cuerpo") or soup.body or soup
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", md(str(main), heading_style="ATX", strip=["img"])).strip()


def _resp2text(r):
    ct = r.headers.get("Content-Type", "")
    if "pdf" in ct:
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(r.content); f.flush()
            return subprocess.run(["pdftotext", "-enc", "UTF-8", f.name, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    if "json" in ct:
        return json.dumps(r.json(), ensure_ascii=False, indent=1)
    if not r.encoding or r.encoding.lower() == "iso-8859-1":
        r.encoding = r.apparent_encoding
    return _html2md(r.text)


def _sii_host(url):
    h = urlparse(url).netloc.lower()
    return h == "sii.cl" or h.endswith(".sii.cl")


# ---------------- base local ----------------
@mcp.tool()
def buscar(consulta: str, categoria: str = "", n: int = 10) -> str:
    """Busca en la base local del SII (29.700 docs: leyes vigentes, circulares, resoluciones, oficios, FAQ, ayudas, valores).
    categoria opcional: ley, faq, circular, resolucion, jurisprudencia, normativa, valores, servicios_online, ayuda,
    destacado, noticia, factura_electronica, declaraciones_juradas, sobre_el_sii, portal, formulario, resolucion_regional, otros.
    Sintaxis FTS5: "frase exacta", OR, prefijo*."""
    _al_dia()  # primera consulta del día: agrega circulares/resoluciones/oficios nuevos
    sql = ("SELECT titulo, url, archivo, categoria, snippet(docs,4,'»','«',' … ',24), bm25(docs,8.0,0,0,1.0,1.0) r "
           "FROM docs WHERE docs MATCH ?")
    args = [_fts(consulta)]
    if categoria:
        sql += " AND categoria=?"; args.append(categoria)
    sql += " ORDER BY r LIMIT ?"; args.append(max(1, min(n, 50)))
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    out = []
    for i, (t, u, f, c, s, _) in enumerate(con.execute(sql, args), 1):
        s = re.sub(r"\s+", " ", s)
        out.append(f"{i}. [{c}] {t}\n   url: {u}\n   archivo: {f}\n   {s}")
    return "\n\n".join(out) or "Sin resultados. Probar sinónimos o menos palabras."


@mcp.tool()
def leer_documento(archivo: str, desde: int = 0, max_chars: int = 20000) -> str:
    """Lee un documento de la base local (ruta 'archivo' devuelta por buscar, ej. docs/...md). Paginar con 'desde'."""
    p = os.path.realpath(os.path.join(BASE, archivo))
    if not p.startswith(os.path.join(BASE, "docs")) or not os.path.exists(p):
        return "Archivo no válido (debe estar dentro de docs/)."
    t = open(p, encoding="utf-8").read()
    chunk = t[desde:desde + max_chars]
    resto = len(t) - desde - len(chunk)
    return chunk + (f"\n\n[… quedan {resto} caracteres; usar desde={desde + len(chunk)}]" if resto > 0 else "")


# ---------------- en vivo ----------------
@mcp.tool()
def ultimas_normas(tipo: str = "circulares", n: int = 5, anio: int = 0, materia: str = "") -> str:
    """Últimas normas publicadas HOY en www.sii.cl. tipo: circulares | resoluciones | oficios.
    materia (solo oficios): RENTA | IVA | OTROS."""
    anio = anio or datetime.date.today().year
    h = {"User-Agent": UA}
    if tipo == "oficios":
        items = []
        for k in ([materia] if materia else ["RENTA", "IVA", "OTROS"]):
            r = requests.post("https://www3.sii.cl/getPublicacionesCTByMateria", headers={**h, "Content-Type": "application/json"},
                              data=json.dumps({"key": k, "year": str(anio)}), timeout=60)
            for it in r.json():
                it["_k"] = k; items.append(it)
        items.sort(key=lambda i: datetime.datetime.strptime(i["pubFechaPubli"], "%d/%m/%Y"), reverse=True)
        return "\n".join(f"- [{i['_k']}] {i['tipoArchPublica']} N° {i['pubNumOficio']} de {i['pubFechaPubli']}: {i['pubResumen']} (Ref.: {i['pubLegal']})" for i in items[:n])
    url = {"circulares": f"https://www.sii.cl/normativa_legislacion/circulares/{anio}/indcir{anio}.htm",
           "resoluciones": f"https://www.sii.cl/normativa_legislacion/resoluciones/{anio}/res_ind{anio}.htm"}.get(tipo)
    if not url:
        return "tipo debe ser circulares, resoluciones u oficios"
    r = requests.get(url, headers=h, timeout=60); r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "lxml"); out = []
    for h5 in soup.find_all("h5"):
        a = h5.find("a", href=True)
        if a:
            p = h5.find_next_sibling("p")
            out.append(f"- {a.get_text(' ', strip=True)}: {p.get_text(' ', strip=True) if p else ''}\n  {requests.compat.urljoin(url, a['href'].strip())}")
        if len(out) >= n:
            break
    return "\n".join(out)


@mcp.tool()
def valor_indicador(indicador: str = "utm", anio: int = 0) -> str:
    """Tabla del año de UTM, UF o dólar desde www.sii.cl (en vivo). indicador: utm | uf | dolar."""
    anio = anio or datetime.date.today().year
    k = indicador.lower()
    url = {"utm": f"https://www.sii.cl/valores_y_fechas/utm/utm{anio}.htm", "uf": f"https://www.sii.cl/valores_y_fechas/uf/uf{anio}.htm",
           "dolar": f"https://www.sii.cl/valores_y_fechas/dolar/dolar{anio}.htm"}.get(k)
    if not url:
        return "indicador: utm | uf | dolar"
    return f"Fuente: {url}\n\n" + _resp2text(requests.get(url, headers={"User-Agent": UA}, timeout=60))[:15000]


@mcp.tool()
def pagina_sii(url: str) -> str:
    """Descarga una página o PDF PÚBLICO de www.sii.cl y la devuelve como texto."""
    if urlparse(url).netloc not in ("www.sii.cl", "sii.cl"):
        return "Solo www.sii.cl (para áreas con login usar sii_consultar)."
    return _resp2text(requests.get(url, headers={"User-Agent": UA}, timeout=60))[:30000]


@mcp.tool()
def calculadora(monto: str = "") -> str:
    """Calculadora UF / USD / EUR (+ UTM) → pesos chilenos, valores del día (UF y UTM: SII; USD/EUR: Banco Central).
    monto acepta formato chileno ("1.500,5", "$ 3.000"). Sin monto devuelve el valor de 1 unidad de cada moneda."""
    sys.path.insert(0, BASE)
    import calculadora as calc
    return calc.texto(calc.calcular(monto or None))


@mcp.tool()
def simulador(tipo: str, monto: str, monto2: str = "", meses: int = 0) -> str:
    """Simuladores en pesos. tipo: bhe (retención boleta honorarios desde bruto) | bhe_liquido (bruto para un líquido) |
    ppm (monto=ingresos netos, monto2=tasa %) | iva (monto=ventas netas, monto2=compras netas) |
    multa (monto=impuesto adeudado, meses=meses de atraso) | sueldo (monto=renta líquida imponible → impuesto único)."""
    a = {"bhe": [monto], "bhe_liquido": [monto, "--liquido"], "ppm": [monto, monto2 or "0,25"], "iva": [monto, monto2 or "0"],
         "multa": [monto, str(meses or 1)], "sueldo": [monto]}.get(tipo)
    if a is None:
        return "tipo: bhe | bhe_liquido | ppm | iva | multa | sueldo"
    r = subprocess.run([sys.executable, os.path.join(BASE, "simuladores.py"), tipo.replace("_liquido", ""), *a], capture_output=True, text=True)
    return r.stdout or r.stderr


@mcp.tool()
def calendario(dias: int = 45) -> str:
    """Próximos vencimientos tributarios (F29/F50, F22, contribuciones, DJ, cambio de UF) en los próximos N días."""
    sys.path.insert(0, BASE)
    import calendario as cal
    return cal.texto(cal.proximos(max(1, min(dias, 400))))


# ---------------- cuenta SII (autenticado, solo lectura) ----------------
def _credenciales():
    # 1) variables de entorno (Linux/Windows o contenedores): ASESOR_SII_RUT / ASESOR_SII_CLAVE
    if os.environ.get("ASESOR_SII_RUT") and os.environ.get("ASESOR_SII_CLAVE"):
        return os.environ["ASESOR_SII_RUT"], os.environ["ASESOR_SII_CLAVE"]
    # 2) Llavero de macOS
    if sys.platform != "darwin":
        return None, None
    out = subprocess.run(["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-g"], capture_output=True, text=True)
    if out.returncode != 0:
        return None, None
    acct = re.search(r'"acct"<blob>="([^"]+)"', out.stdout)
    pwd = re.search(r'^password: "(.*)"$', out.stderr, re.M)
    return (acct.group(1) if acct else None), (pwd.group(1) if pwd else None)


@mcp.tool()
def sii_login() -> str:
    """Inicia sesión en el SII con RUT + clave tributaria guardados en el Llavero (servicio 'asesor-sii'). No devuelve la clave."""
    global _sess
    rut, clave = _credenciales()
    if not rut or not clave:
        return ("No hay credenciales. El usuario debe ejecutar en su terminal: "
                f"security add-generic-password -s {KEYCHAIN_SERVICE} -a <RUT-DV> -w   (pedirá la clave, no la escribas en el chat)")
    num, dv = rut.replace(".", "").upper().split("-")
    s = requests.Session(); s.headers["User-Agent"] = UA
    s.get("https://zeusr.sii.cl/AUT2000/InicioAutenticacion/IngresoRutClave.html", timeout=60)
    r = s.post("https://zeusr.sii.cl/cgi_AUT2000/CAutInicio.cgi",
               data={"rut": num, "dv": dv, "referencia": "https://misiir.sii.cl/cgi_misii/siihome.cgi", "411": "",
                     "rutcntr": f"{num}-{dv}", "clave": clave}, timeout=60, allow_redirects=True)
    del clave
    if not any(c.name.upper() == "TOKEN" for c in s.cookies):
        txt = BeautifulSoup(r.text, "lxml").get_text(" ", strip=True)[:300]
        return f"Login falló (sin cookie TOKEN). Respuesta: {txt}"
    _sess = s
    return f"Sesión iniciada para RUT {num[:-3]}***-{dv}. Usa sii_consultar(url) para leer páginas autenticadas."


@mcp.tool()
def sii_consultar(url: str) -> str:
    """Lee (GET, solo lectura) una página o API autenticada de *.sii.cl con la sesión de sii_login.
    Nunca envía formularios, declara, rectifica ni modifica datos. Ejemplos de destino: Mi SII
    (https://misiir.sii.cl/cgi_misii/siihome.cgi), consultas de estado F29/F22, carpeta tributaria.
    Ver docs/_catalogos/aplicaciones_y_tramites.md para el mapa de aplicaciones."""
    if _sess is None:
        return "Primero ejecutar sii_login."
    if not _sii_host(url):
        return "Solo dominios *.sii.cl."
    if re.search(r"(logout|salir|enviar|declarar|rectific|anular|pagar|firmar|timbr)", url, re.I):
        return "Bloqueado: la URL parece una acción transaccional. Este MCP es solo de lectura."
    r = _sess.get(url, timeout=60)
    return f"HTTP {r.status_code} {r.url}\n\n" + _resp2text(r)[:30000]


if __name__ == "__main__":
    mcp.run()
