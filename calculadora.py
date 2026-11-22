#!/usr/bin/env python3
"""Calculadora UF / USD / EUR → pesos + UTM del mes.
  python3 calculadora.py            # valores del día
  python3 calculadora.py 15         # 15 UF, 15 USD, 15 EUR y 15 UTM en pesos
  python3 calculadora.py "1.500,5"  # formato chileno
  python3 calculadora.py 15 --json
Fuentes: UF y UTM tabla oficial SII; USD/EUR observado Banco Central (mindicador.cl); respaldo dólar SII y open.er-api.com.
Caché 1 h en config/indicadores.json (último valor bueno sirve sin red).
"""
import datetime, json, os, re, sys, time
from zoneinfo import ZoneInfo
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "config", "indicadores.json")
TTL = 3600
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def hoy():
    return datetime.datetime.now(ZoneInfo("America/Santiago")).date()


def _get(url, t=12):
    r = requests.get(url, timeout=t)  # sin user-agent propio: mindicador se cuelga con uno
    r.raise_for_status()
    return r.text


def parse_sii(html, d, decimal_comma):
    """Valor del día d (o último publicado antes) en una tabla anual del SII."""
    for back in range(40):
        x = d - datetime.timedelta(days=back)
        if x.year != d.year:
            return None
        i = html.find(f"id='mes_{MESES[x.month - 1]}'")
        if i < 0:
            continue
        end = html.find("class='meses'", i + 20)
        seg = html[i:end if end > 0 else None]
        m = re.search(rf"<strong>{x.day}</strong></th>\s*<td[^>]*>([^<]+)</td>", seg)
        if not m:
            continue
        raw = m.group(1).strip()
        try:
            n = float(raw.replace(".", "").replace(",", ".") if decimal_comma else raw.replace(",", ""))
        except ValueError:
            continue
        if n > 0:
            return {"valor": n, "fecha": x.isoformat()}
    return None


def utm_mes(d):
    try:
        html = _get(f"https://www.sii.cl/valores_y_fechas/utm/utm{d.year}.htm")
    except Exception:
        return None
    for back in range(12):
        m = (d.month - 1 - back) % 12
        if back and m == 11 and d.month - 1 - back < 0:
            return None
        row = re.search(rf"<th[^>]*>\s*{MESES[m].capitalize()}\s*</th>\s*<td[^>]*>([\d.]+)</td>", html, re.I)
        if row:
            v = float(row.group(1).replace(".", ""))
            if v > 0:
                return {"valor": v, "fecha": f"{d.year}-{m + 1:02d}", "fuente": "SII"}
    return None


def fetch_all():
    d = hoy(); out = {"at": time.time()}
    try:
        uf = parse_sii(_get(f"https://www.sii.cl/valores_y_fechas/uf/uf{d.year}.htm"), d, True)
        if uf:
            out["uf"] = {**uf, "fuente": "SII"}
    except Exception:
        pass
    mi = None
    try:
        mi = json.loads(_get("https://mindicador.cl/api", 25))
    except Exception:
        pass

    def from_mi(k):
        try:
            v = float(mi[k]["valor"])
            return {"valor": v, "fecha": str(mi[k]["fecha"])[:10], "fuente": "Banco Central"} if v > 0 else None
        except Exception:
            return None

    out["usd"], out["eur"] = from_mi("dolar"), from_mi("euro")
    if not out["usd"]:
        try:
            u = parse_sii(_get(f"https://www.sii.cl/valores_y_fechas/dolar/dolar{d.year}.htm"), d, False)
            if u:
                out["usd"] = {**u, "fuente": "SII"}
        except Exception:
            pass
    if not out.get("uf"):
        out["uf"] = from_mi("uf")
    for k, cur in (("eur", "EUR"), ("usd", "USD")):
        if not out.get(k):
            try:
                j = json.loads(_get(f"https://open.er-api.com/v6/latest/{cur}"))
                v = float(j["rates"]["CLP"])
                out[k] = {"valor": v, "fecha": datetime.datetime.fromtimestamp(j["time_last_update_unix"]).date().isoformat(), "fuente": "mercado (open.er-api.com)"}
            except Exception:
                pass
    out["utm"] = utm_mes(d) or from_mi("utm")
    return out


def indicadores(force=False):
    mem = None
    try:
        mem = json.load(open(CACHE))
    except Exception:
        pass
    if mem and not force and time.time() - mem.get("at", 0) < TTL and all(mem.get(k) for k in ("uf", "usd", "eur")):
        return mem
    n = fetch_all()
    merged = {"at": n["at"], **{k: n.get(k) or (mem or {}).get(k) for k in ("uf", "usd", "eur", "utm")}}
    if any(n.get(k) for k in ("uf", "usd", "eur")):
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        json.dump(merged, open(CACHE, "w"), ensure_ascii=False)
    elif not mem:
        raise RuntimeError("sin conexión a SII ni Banco Central")
    return merged


def num(s):
    """'1.500', '1500,5', '2.5', '$ 3.000' -> float (estilo chileno primero)."""
    t = re.sub(r"[$\s]", "", str(s or ""))
    if not t:
        return None
    if "," in t:
        t = t.replace(".", "").replace(",", ".")
    elif t.count(".") > 1 or re.fullmatch(r"\d{1,3}\.\d{3}", t):
        t = t.replace(".", "")
    try:
        return float(t)
    except ValueError:
        return None


def clp(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def tasa(n):
    return "$" + f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular(monto=None):
    r = indicadores(); n = num(monto) if monto not in (None, "") else None
    filas = []
    for k, lb in (("uf", "UF"), ("usd", "USD"), ("eur", "EUR"), ("utm", "UTM")):
        x = r.get(k)
        if not x:
            filas.append({"moneda": lb, "error": "sin dato"}); continue
        f = {"moneda": lb, "tasa": x["valor"], "fecha": x["fecha"], "fuente": x["fuente"]}
        if n and n > 0:
            f["monto"] = n; f["clp"] = round(n * x["valor"])
        filas.append(f)
    return filas


def texto(filas):
    out = []
    for f in filas:
        if "error" in f:
            out.append(f"{f['moneda']:<4} sin dato"); continue
        ref = f"1 {f['moneda']} = {tasa(f['tasa'])} · {f['fuente']} · {f['fecha']}"
        out.append(f"{f['moneda']:<4} {clp(f['clp']):>16}   ({ref})" if "clp" in f else f"{f['moneda']:<4} {tasa(f['tasa']):>16}   ({f['fuente']} · {f['fecha']})")
    return "\n".join(out)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--json"]
    filas = calcular(args[0] if args else None)
    print(json.dumps(filas, ensure_ascii=False, indent=1) if "--json" in sys.argv else texto(filas))
