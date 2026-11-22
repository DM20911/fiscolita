#!/usr/bin/env python3
"""Calendario tributario: próximos vencimientos del SII.

  python3 calendario.py            # próximos 45 días
  python3 calendario.py --dias 90
  python3 calendario.py --avisos   # solo lo que vence en 3 días o mañana (lo usa el bot para avisar)

Reglas (fuentes oficiales en la base local):
- F29 y F50: hasta el día 20 de cada mes si se declara por internet (día 12 en papel); si cae sábado,
  domingo o feriado, pasa al día hábil siguiente (Res. Ex. SII N° 127/2023; DS 1.001/2006).
- F22 Operación Renta: abril de cada año.
- Contribuciones: cuotas con vencimiento en abril, junio, septiembre y noviembre (último día hábil del mes).
- Declaraciones juradas anuales: marzo (fechas exactas por DJ en el suplemento anual del SII).
- UF: el valor del período del 10 de un mes al 9 del siguiente se publica cada mes (Banco Central / SII).
Los feriados se leen de config/feriados.json si existe (lista "AAAA-MM-DD"); si no, se usan los fijos de Chile.
"""
import calendar, datetime, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FERIADOS_FIJOS = ["01-01", "05-01", "05-21", "06-29", "07-16", "08-15", "09-18", "09-19", "10-12", "10-31", "11-01", "12-08", "12-25"]


def feriados(anio):
    p = os.path.join(HERE, "config", "feriados.json")
    try:
        return {datetime.date.fromisoformat(d) for d in json.load(open(p))}
    except Exception:
        return {datetime.date(anio, int(m), int(d)) for m, d in (x.split("-") for x in FERIADOS_FIJOS)}


def habil(d, atras=False):
    fer = feriados(d.year)
    while d.weekday() >= 5 or d in fer:
        d += datetime.timedelta(days=-1 if atras else 1)
    return d


def ultimo_habil(anio, mes):
    return habil(datetime.date(anio, mes, calendar.monthrange(anio, mes)[1]), atras=True)


def eventos(desde, hasta):
    ev = []
    for anio in range(desde.year, hasta.year + 1):
        for mes in range(1, 13):
            ev.append((habil(datetime.date(anio, mes, 20)), "F29 / F50 por internet",
                       "Declaración y pago de IVA, PPM, retenciones e impuesto único del mes anterior (con pago o sin movimiento)."))
            ev.append((habil(datetime.date(anio, mes, 12)), "F29 en papel", "Plazo para quienes no declaran por internet."))
            ev.append((datetime.date(anio, mes, 10), "Cambia el período de la UF", "Nuevo tramo de valores UF del 10 al 9 del mes siguiente."))
            if mes in (4, 6, 9, 11):
                ev.append((ultimo_habil(anio, mes), "Contribuciones: vence la cuota", "Pago de la cuota de impuesto territorial (bienes raíces)."))
        ev.append((datetime.date(anio, 4, 1), "Inicio Operación Renta (F22)", "Declaración anual de impuestos a la renta: todo abril."))
        ev.append((ultimo_habil(anio, 4), "Último día Operación Renta (F22)", "Plazo final para presentar el F22 del año tributario."))
        ev.append((datetime.date(anio, 3, 1), "Declaraciones juradas anuales", "Marzo: vencen la mayoría de las DJ (ver suplemento del SII)."))
    return sorted(e for e in ev if desde <= e[0] <= hasta)


def proximos(dias=45, hoy=None):
    hoy = hoy or datetime.date.today()
    return eventos(hoy, hoy + datetime.timedelta(days=dias))


def avisos(hoy=None):
    """Eventos que vencen exactamente en 3 días o mañana (para alertas)."""
    hoy = hoy or datetime.date.today()
    return [(d, t, x, (d - hoy).days) for d, t, x in eventos(hoy, hoy + datetime.timedelta(days=3)) if (d - hoy).days in (0, 1, 3)]


DIAS = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]


def texto(lista):
    return "\n".join(f"- {DIAS[d.weekday()]} {d:%d-%m-%Y} · {t}: {x}" for d, t, x in lista) or "Sin vencimientos en el período."


if __name__ == "__main__":
    if "--avisos" in sys.argv:
        for d, t, x, n in avisos():
            print(f"{'HOY' if n == 0 else 'MAÑANA' if n == 1 else f'en {n} días'} ({d:%d-%m}): {t} — {x}")
    else:
        n = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 45
        print(texto(proximos(n)))
