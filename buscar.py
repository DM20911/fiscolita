#!/usr/bin/env python3
"""Búsqueda de texto completo sobre la documentación del SII.
Uso:
  python3 buscar.py "boleta honorarios retencion"            # top 15
  python3 buscar.py "contribuciones" -c faq -n 30           # filtra categoría
  python3 buscar.py '"impuesto unico" AND tabla' -c circular
Categorías: ley faq circular jurisprudencia resolucion_regional resolucion normativa valores servicios_online ayuda destacado
            noticia factura_electronica declaraciones_juradas sobre_el_sii portal formulario otros
Sintaxis FTS5: palabras sueltas = AND implícito; OR; "frase exacta"; prefijo*
"""
import argparse, os, re, sqlite3, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "busqueda.sqlite")
import sys
sys.path.insert(0, HERE)
from construir_indice import asegurar
asegurar()
from actualizar_novedades import asegurar_al_dia
asegurar_al_dia()  # regla general: 1 revisión de novedades del SII por día


def fts_query(q):
    if re.search(r'["*]|\b(AND|OR|NOT|NEAR)\b', q):
        return q
    toks = [t for t in re.findall(r"\w+", q, re.U) if len(t) > 1]
    return " ".join(f'"{t}"' for t in toks)


ap = argparse.ArgumentParser()
ap.add_argument("q")
ap.add_argument("-c", "--categoria")
ap.add_argument("-n", type=int, default=15)
ap.add_argument("--or", dest="o", action="store_true", help="unir palabras con OR")
a = ap.parse_args()
q = fts_query(a.q)
if a.o and '"' in q and " AND " not in q:
    q = " OR ".join(q.split(" "))
sql = ("SELECT titulo, url, archivo, categoria, snippet(docs, 4, '»', '«', ' … ', 24), bm25(docs, 8.0, 0, 0, 1.0, 1.0) AS r "
       "FROM docs WHERE docs MATCH ?")
args = [q]
if a.categoria:
    sql += " AND categoria = ?"; args.append(a.categoria)
sql += " ORDER BY r LIMIT ?"; args.append(a.n)
con = sqlite3.connect(DB)
for i, (t, u, f, c, s, r) in enumerate(con.execute(sql, args), 1):
    s = re.sub(r"\s+", " ", s)
    print(f"{i}. [{c}] {t}\n   {u}\n   {f}\n   {s}\n")
