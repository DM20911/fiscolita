#!/usr/bin/env python3
"""Simuladores tributarios (montos en pesos, valores del día cuando aplica).

  python3 simuladores.py bhe 1000000            # retención boleta de honorarios (bruto → líquido)
  python3 simuladores.py bhe 850000 --liquido   # cuánto boletear para recibir un líquido
  python3 simuladores.py ppm 10000000 1,1       # PPM = ingresos netos del mes × tasa %
  python3 simuladores.py iva 5000000 2000000    # ventas netas, compras netas → IVA a pagar
  python3 simuladores.py multa 500000 7         # impuesto adeudado, meses de atraso → multa + interés
  python3 simuladores.py sueldo 2500000         # impuesto único de 2ª categoría (renta líquida imponible)

Fuentes: tasa BHE (sii.cl/destacados/boletas_honorarios), art. 97 N° 2 y art. 53 del Código Tributario,
resolución SII vigente de tasas de interés por mora, art. 43 N° 1 de la Ley sobre Impuesto a la Renta,
art. 14 del DL 825 (IVA 19%). Resultados referenciales: validar con el SII o un contador.
"""
import datetime, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

IVA = 0.19
BHE = {2025: 14.5, 2026: 15.25}  # % retención por año de emisión (fuente: sii.cl/destacados/boletas_honorarios/ejemplos_bh.html)
INTERES_RESPALDO = (7.70, "Res. Ex. SII N° 88 de 26-06-2026 (2° semestre 2026)")
TRAMOS_IUSC = [(13.5, 0.0), (30, 0.04), (50, 0.08), (70, 0.135), (90, 0.23), (120, 0.304), (310, 0.35), (float("inf"), 0.40)]


def pesos(x):
    return "$" + f"{round(x):,}".replace(",", ".")


def num(s):
    s = str(s).replace("$", "").replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(".") > 1 or re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        s = s.replace(".", "")
    return float(s)


def utm_mes():
    try:
        import calculadora
        for f in calculadora.calcular(None):
            if f.get("moneda") == "UTM" and f.get("tasa"):
                return float(f["tasa"]), f.get("fecha")
    except Exception:
        pass
    return None, None


def tasa_interes():
    """Tasa anual de interés penal vigente según la última resolución SII descargada (art. 53 CT)."""
    mejor = None
    for p in glob.glob(os.path.join(HERE, "docs/normativa_legislacion/resoluciones/20*/reso*.pdf.md")):
        t = open(p, encoding="utf-8", errors="replace").read(4000)
        if "TASAS DE INTER" not in t.upper() or "MORA" not in t.upper():
            continue
        cuerpo = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"B = A \+ 3,5%(.*?)Tasa de inter", cuerpo, re.S)
        if not m:
            continue
        pct = re.findall(r"(\d+,\d+)%", m.group(1))
        tit = re.search(r"^titulo: (.*)$", t, re.M)
        fecha = re.search(r"(\d{4})/reso(\d+)", p)
        if len(pct) >= 2 and fecha:
            clave = (int(fecha.group(1)), int(fecha.group(2)))
            if not mejor or clave > mejor[0]:
                mejor = (clave, float(pct[-1].replace(",", ".")), (tit.group(1)[:90] if tit else p))
    return (mejor[1], mejor[2]) if mejor else INTERES_RESPALDO


def bhe(monto, liquido=False, anio=None):
    anio = anio or datetime.date.today().year
    tasa = BHE.get(anio)
    nota = ""
    if tasa is None:
        tasa = BHE[max(BHE)]; nota = f"\n(Tasa {anio} no cargada: se usó {tasa}%. Verificar en sii.cl/destacados/boletas_honorarios.)"
    t = tasa / 100
    bruto = monto / (1 - t) if liquido else monto
    ret = round(bruto * t)
    return (f"Boleta de honorarios {anio} · retención {tasa}%\n"
            f"- Bruto (total honorarios): {pesos(bruto)}\n- Retención: {pesos(ret)}\n- Líquido a recibir: {pesos(bruto - ret)}\n"
            f"Fuente: https://www.sii.cl/destacados/boletas_honorarios/{nota}")


def ppm(base, tasa):
    v = base * tasa / 100
    return (f"PPM del mes\n- Base imponible (ingresos brutos sin IVA, F29 cód. 563): {pesos(base)}\n- Tasa (cód. 115): {tasa}%\n"
            f"- PPM a pagar (cód. 62): {pesos(v)}\nFuente: art. 84 LIR; F29 línea 69.")


def iva(ventas, compras):
    deb, cred = ventas * IVA, compras * IVA
    neto = deb - cred
    return (f"IVA del mes (tasa 19%)\n- Débito fiscal (ventas netas {pesos(ventas)}): {pesos(deb)}\n"
            f"- Crédito fiscal (compras netas {pesos(compras)}): {pesos(cred)}\n"
            + (f"- IVA a pagar: {pesos(neto)}" if neto >= 0 else f"- Remanente de crédito para el mes siguiente: {pesos(-neto)}")
            + "\nFuente: arts. 14, 20 y 23 DL 825.")


def multa(impuesto, meses, dias=None):
    meses = int(meses)
    pct = 10 if meses <= 5 else min(10 + 2 * (meses - 5), 30)
    tasa, fuente = tasa_interes()
    dias = dias if dias is not None else meses * 30
    interes = impuesto * tasa / 100 / 360 * dias
    return (f"Atraso de {meses} mes(es) en declarar un impuesto de {pesos(impuesto)}\n"
            f"- Multa art. 97 N° 2 CT: {pct}% → {pesos(impuesto * pct / 100)}\n"
            f"- Interés penal aprox. ({tasa}% anual / 360 × {dias} días): {pesos(interes)}\n"
            f"- Total aprox. (sin reajuste IPC): {pesos(impuesto * (1 + pct / 100) + interes)}\n"
            f"Notas: además se reajusta por IPC (art. 53); el interés usa la tasa de cada semestre ({fuente}); "
            "si el impuesto es de retención o recargo (ej. IVA) y no se pagó, aplica el art. 97 N° 11. "
            "El SII suele condonar parte si se regulariza antes de una fiscalización (Circular 50/2016 y sus modificaciones).")


def sueldo(renta):
    utm, _ = utm_mes()
    if not utm:
        return "No pude obtener la UTM del mes (sin conexión). Probar más tarde."
    imp, ant, det = 0.0, 0.0, []
    for lim, tasa in TRAMOS_IUSC:
        tope = lim * utm
        if renta > ant and tasa:
            parte = min(renta, tope) - ant
            imp += parte * tasa
            det.append(f"  {pesos(ant)}–{pesos(min(renta, tope))} × {tasa * 100:g}% = {pesos(parte * tasa)}")
        ant = tope
        if renta <= tope:
            break
    return (f"Impuesto único de 2ª categoría (UTM {pesos(utm)})\n- Renta líquida imponible: {pesos(renta)}\n"
            + ("\n".join(det) + "\n" if det else "- Exento (hasta 13,5 UTM)\n")
            + f"- Impuesto del mes: {pesos(imp)} ({imp / renta * 100 if renta else 0:.2f}% efectivo)\n"
            "Renta líquida imponible = sueldo imponible − AFP − salud − seguro de cesantía. Fuente: art. 43 N° 1 LIR.")


def main(argv):
    if not argv:
        print(__doc__); return
    c, a = argv[0].lower(), [x for x in argv[1:] if not x.startswith("--")]
    try:
        if c == "bhe":
            print(bhe(num(a[0]), "--liquido" in argv))
        elif c == "ppm":
            print(ppm(num(a[0]), num(a[1]) if len(a) > 1 else 0.25))
        elif c == "iva":
            print(iva(num(a[0]), num(a[1]) if len(a) > 1 else 0))
        elif c == "multa":
            print(multa(num(a[0]), num(a[1]) if len(a) > 1 else 1))
        elif c == "sueldo":
            print(sueldo(num(a[0])))
        else:
            print(__doc__)
    except (IndexError, ValueError):
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
