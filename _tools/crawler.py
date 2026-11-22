#!/usr/bin/env python3
"""Crawler cortés y reanudable de www.sii.cl (contenido público).
Uso: python3 -I crawler.py <dir_base>   (dir_base = carpeta asesor_tributario)
"""
import re, sys, time, sqlite3, threading, hashlib, os
from urllib.parse import urljoin, urlparse, urldefrag, unquote
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

BASE = sys.argv[1]
RAW = os.path.join(BASE, "raw")
DB = os.path.join(BASE, "_tools", "crawl.sqlite")
HOSTS = {"www.sii.cl", "sii.cl"}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
WORKERS = 6
DELAY = 0.25
MAX_BYTES = 40 * 1024 * 1024
MAX_DEPTH = 12
KEEP_EXT = {".htm", ".html", ".shtml", ".pdf", ".xls", ".xlsx", ".doc", ".docx", ".txt", ".csv", ".xml", ".ppt", ".pptx", ""}
SKIP_EXT = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".ico", ".css", ".js", ".woff", ".woff2", ".ttf", ".eot",
            ".mp4", ".mp3", ".avi", ".wmv", ".flv", ".swf", ".zip", ".rar", ".exe", ".msi", ".jar", ".dmg", ".7z",
            ".gz", ".tar", ".bmp", ".webp", ".mov", ".m4v", ".wav", ".iso", ".cab"}
SKIP_PATH = re.compile(r"(/transparencia/|/documentos/normativa_ddrr/.*\.pdf$|/cgi_|/cgi-bin/|/cvc_cgi/|\?.*(logout|login)|/pagina/actualizada/noticias/tv_)", re.I)

LINK_RE = re.compile(r"""(?:location(?:\.href)?|window\.open)\s*(?:=|\()\s*['"]([^'"]+)['"]""", re.I)
URL_RE = re.compile(r"""['"]((?:https?:)?//(?:www\.)?sii\.cl/[^'"\s]+|/[A-Za-z0-9_\-./]+\.(?:html?|pdf|xlsx?|docx?))['"]""")

lock = threading.Lock()
con = sqlite3.connect(DB, check_same_thread=False)
con.execute("""CREATE TABLE IF NOT EXISTS urls(url TEXT PRIMARY KEY, depth INT, parent TEXT, status INT DEFAULT 0,
  ctype TEXT, path TEXT, size INT, fetched TEXT)""")
con.execute("CREATE TABLE IF NOT EXISTS external(url TEXT, parent TEXT, text TEXT, PRIMARY KEY(url,parent))")
con.execute("CREATE INDEX IF NOT EXISTS ix_status ON urls(status)")
con.commit()

sess = requests.Session()
sess.headers.update({"User-Agent": UA, "Accept-Language": "es-CL,es;q=0.9"})
adapter = requests.adapters.HTTPAdapter(pool_connections=WORKERS, pool_maxsize=WORKERS * 2, max_retries=2)
sess.mount("https://", adapter); sess.mount("http://", adapter)


def norm(u):
    u, _ = urldefrag(u.strip())
    p = urlparse(u)
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower().split(":")[0]
    path = re.sub(r"/{2,}", "/", p.path or "/")
    return f"https://{host}{path}" + (f"?{p.query}" if p.query else "")


def in_scope(u):
    p = urlparse(u)
    if p.netloc not in HOSTS:
        return False
    ext = os.path.splitext(p.path.lower())[1]
    if ext in SKIP_EXT:
        return False
    if SKIP_PATH.search(u):
        return False
    return True


def local_path(u, ctype):
    p = urlparse(u)
    path = unquote(p.path)
    if path.endswith("/"):
        path += "index.html"
    ext = os.path.splitext(path)[1].lower()
    if not ext:
        path += "/index.html" if "html" in (ctype or "") else ""
    if p.query:
        h = hashlib.md5(p.query.encode()).hexdigest()[:8]
        root, e = os.path.splitext(path)
        path = f"{root}__{h}{e}"
    path = path.lstrip("/").replace("..", "_")
    return os.path.join(RAW, path)


def add(urls, depth, parent):
    with lock:
        for u in urls:
            con.execute("INSERT OR IGNORE INTO urls(url,depth,parent) VALUES(?,?,?)", (u, depth, parent))
        con.commit()


def extract(u, body, ctype):
    found, ext_links = set(), set()
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        text = body.decode("latin-1", "replace")
    raw = []
    if "html" in ctype:
        soup = BeautifulSoup(text, "lxml")
        for tag, attr in (("a", "href"), ("area", "href"), ("frame", "src"), ("iframe", "src"), ("link", "href"), ("option", "value"), ("form", "action")):
            for t in soup.find_all(tag):
                v = t.get(attr)
                if v:
                    raw.append((v, t.get_text(" ", strip=True)[:120] if tag == "a" else ""))
    for m in LINK_RE.finditer(text):
        raw.append((m.group(1), ""))
    for m in URL_RE.finditer(text):
        raw.append((m.group(1), ""))
    for v, txt in raw:
        v = v.strip()
        if not v or v.startswith(("javascript:", "mailto:", "tel:", "#")):
            continue
        if v.startswith("//"):
            v = "https:" + v
        n = norm(urljoin(u, v))
        if not n:
            continue
        host = urlparse(n).netloc
        if in_scope(n):
            found.add(n)
        elif host.endswith("sii.cl") and host not in HOSTS:
            ext_links.add((n, txt))
    return found, ext_links


def fetch(row):
    url, depth = row
    time.sleep(DELAY)
    try:
        r = sess.get(url, timeout=40, stream=True, allow_redirects=True)
        ctype = r.headers.get("Content-Type", "").lower()
        final = norm(r.url) or url
        if r.status_code != 200:
            with lock:
                con.execute("UPDATE urls SET status=?, fetched=datetime('now') WHERE url=?", (r.status_code, url)); con.commit()
            return
        if final != url and not in_scope(final):
            with lock:
                con.execute("UPDATE urls SET status=?, ctype=?, fetched=datetime('now') WHERE url=?", (399, "redirect:" + final, url)); con.commit()
            return
        cl = int(r.headers.get("Content-Length") or 0)
        if cl > MAX_BYTES:
            with lock:
                con.execute("UPDATE urls SET status=413, size=? WHERE url=?", (cl, url)); con.commit()
            return
        body = b""
        for chunk in r.iter_content(65536):
            body += chunk
            if len(body) > MAX_BYTES:
                break
        if len(body) > MAX_BYTES:
            with lock:
                con.execute("UPDATE urls SET status=413 WHERE url=?", (url,)); con.commit()
            return
        # páginas 404 "blandas" del SII
        if "html" in ctype and b"NO SE ENCONTR" in body[:6000] and b"404.css" in body[:3000]:
            with lock:
                con.execute("UPDATE urls SET status=404, fetched=datetime('now') WHERE url=?", (url,)); con.commit()
            return
        path = local_path(final, ctype)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(body)
        links, exts = set(), set()
        if ("html" in ctype or "javascript" in ctype or "xml" in ctype) and depth < MAX_DEPTH:
            links, exts = extract(final, body, ctype)
        with lock:
            con.execute("UPDATE urls SET status=200, ctype=?, path=?, size=?, fetched=datetime('now') WHERE url=?",
                        (ctype, os.path.relpath(path, BASE), len(body), url))
            for e, t in exts:
                con.execute("INSERT OR IGNORE INTO external VALUES(?,?,?)", (e, url, t))
            con.commit()
        if final != url:
            add([final], depth, url)
        add(links, depth + 1, url)
    except Exception as e:
        with lock:
            con.execute("UPDATE urls SET status=-1, ctype=? WHERE url=?", (str(e)[:200], url)); con.commit()


def seeds():
    s = ["https://www.sii.cl/", "https://www.sii.cl/preguntas_frecuentes/preguntasfrecuentes.htm",
         "https://www.sii.cl/preguntas_frecuentes/otros.html",
         "https://www.sii.cl/normativa_legislacion/legislacion_tributaria.html",
         "https://www.sii.cl/normativa_legislacion/jurisprudencia_y_tribunales.html",
         "https://www.sii.cl/valores_y_fechas/index_valores_y_fechas.html",
         "https://www.sii.cl/ayudas/ayudas.html", "https://www.sii.cl/servicios_online/index.html",
         "https://www.sii.cl/destacados/index.html", "https://www.sii.cl/noticias/index.html",
         "https://www.sii.cl/sobre_el_sii/nuestro_servicio.htm"]
    for y in range(1990, 2027):
        s += [f"https://www.sii.cl/normativa_legislacion/circulares/{y}/indcir{y}.htm",
              f"https://www.sii.cl/normativa_legislacion/resoluciones/{y}/res_ind{y}.htm",
              f"https://www.sii.cl/valores_y_fechas/utm/utm{y}.htm",
              f"https://www.sii.cl/valores_y_fechas/uf/uf{y}.htm",
              f"https://www.sii.cl/valores_y_fechas/dolar/dolar{y}.htm"]
    # enlaces del menú (JS)
    try:
        js = sess.get("https://www.sii.cl/js/responsive_barranav.js", timeout=30).text
        for m in re.finditer(r"(?:https?:)?//www\.sii\.cl(/[^\s'\"]+)|['\"](/[A-Za-z0-9_\-./]+\.html?)['\"]", js):
            p = m.group(1) or m.group(2)
            s.append("https://www.sii.cl" + p)
            n = norm("https://www.sii.cl" + p)
        for m in re.finditer(r"['\"]((?:https?:)?//[a-z0-9.\-]+\.sii\.cl/[^'\"\s]*)['\"]", js):
            u = norm(("https:" + m.group(1)) if m.group(1).startswith("//") else m.group(1))
            if u and urlparse(u).netloc not in HOSTS:
                con.execute("INSERT OR IGNORE INTO external VALUES(?,?,?)", (u, "menu_js", ""))
        con.commit()
    except Exception as e:
        print("nav.js", e)
    return [n for n in (norm(x) for x in s) if n and in_scope(n)]


def main():
    add(seeds(), 0, "seed")
    # reintentar errores de red
    with lock:
        con.execute("UPDATE urls SET status=0 WHERE status=-1"); con.commit()
    t0 = time.time()
    with ThreadPoolExecutor(WORKERS) as ex:
        while True:
            with lock:
                rows = con.execute("SELECT url, depth FROM urls WHERE status=0 ORDER BY depth LIMIT 300").fetchall()
                if rows:
                    con.executemany("UPDATE urls SET status=1 WHERE url=?", [(r[0],) for r in rows]); con.commit()
            if not rows:
                break
            list(ex.map(fetch, rows))
            with lock:
                done = con.execute("SELECT count(*) FROM urls WHERE status>1").fetchone()[0]
                pend = con.execute("SELECT count(*) FROM urls WHERE status IN (0,1)").fetchone()[0]
                mb = (con.execute("SELECT sum(size) FROM urls WHERE status=200").fetchone()[0] or 0) / 1e6
            print(f"[{time.strftime('%H:%M:%S')}] hechos={done} pendientes={pend} MB={mb:.0f} t={int(time.time()-t0)}s", flush=True)
    print("FIN", flush=True)


if __name__ == "__main__":
    # status=1 huérfanos de una corrida previa -> volver a cola
    con.execute("UPDATE urls SET status=0 WHERE status=1"); con.commit()
    main()
