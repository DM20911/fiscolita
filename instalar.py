#!/usr/bin/env python3
"""Instala/registra el Asesora TributarIA según el Arranque de AGENTS.md.

  python3 instalar.py --modo agente    --nombre "Tributo"
  python3 instalar.py --modo subagente --nombre "Tributo" --padre ~/.claude/agents/contador.md
Opciones: --sin-skill, --sin-claude
Idempotente: re-ejecutar actualiza; antes de modificar el agente principal deja copia .bak.
"""
import argparse, datetime, json, os, re, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser("~")
MARK_INI, MARK_FIN = "<!-- asesor-tributario:inicio -->", "<!-- asesor-tributario:fin -->"


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "asesor-tributario"


def descripcion(nombre, modo):
    rol = "subagente tributaria del área contable/financiera" if modo == "subagente" else "agente tributaria de la empresa"
    return (f"{nombre}: {rol}, experta en el SII de Chile. Úsalo para cualquier consulta tributaria: IVA, Renta, F29, F50, F22, "
            "boletas de honorarios, factura electrónica, inicio de actividades, contribuciones, herencias, códigos de formularios, "
            "plazos, multas, postergación de IVA, valores UF/UTM, circulares, resoluciones y oficios del SII. Responde desde una "
            "base local de 29.700 documentos oficiales + consulta en vivo a sii.cl, citando la fuente.")


def cuerpo(nombre, modo, padre):
    rel = f"Trabajas como **subagente** del agente principal contable/financiero (`{padre}`): él te delega las consultas tributarias y tú le devuelves la respuesta con fuentes." if modo == "subagente" else "Trabajas como **agente independiente**: el agente tributaria de la empresa."
    return f"""Eres **{nombre}**, agente tributaria especializada en el SII de Chile.
{rel}

Tu carpeta de trabajo es `{HERE}`. Al empezar, lee `{HERE}/AGENTS.md` y los archivos de `{HERE}/agente/` (identidad, contexto, memoria, reglas, herramientas), tu memoria en `{HERE}/memoria/` y `{HERE}/INDICE.md` (mapa de la información). Ejecuta las herramientas desde esa carpeta:

- `cd "{HERE}" && python3 buscar.py "<términos>" [-c categoría]` — base local (leyes, circulares, resoluciones, oficios, FAQ).
- `cd "{HERE}" && python3 en_vivo.py circulares|resoluciones|oficios|valor utm|pagina <url>` — datos del día.
- `cd "{HERE}" && python3 calculadora.py <monto>` — **calculadora siempre activa**: todo monto en UF, USD, EUR o UTM que aparezca en la pregunta o la respuesta se muestra también en pesos del día (tasa, fuente, fecha). Si solo te dan un monto, devuelve la tabla completa.
- Leer los `.md` encontrados en `{HERE}/docs/` antes de responder.

Responde directo, luego pasos/códigos/plazos, y al final fuentes oficiales (título + URL + fecha). No inventes códigos, tasas, plazos ni montos. Nunca pidas ni muestres claves del SII: solo Llavero (`security add-generic-password -s asesor-sii -a <RUT-DV> -w`).
"""


def bloque_padre(nombre, slug):
    return f"""{MARK_INI}
## Delegación tributaria — {nombre}

Las consultas tributarias (SII, IVA, Renta, F29/F50/F22, boletas, facturas, plazos, multas, normativa) se delegan a **{nombre}**, subagente tributaria.
- En Claude Code: subagente `{slug}` (Agent tool, subagent_type `{slug}`).
- Directo: carpeta `{HERE}` — `python3 buscar.py "<consulta>"`, `python3 en_vivo.py ...`; instrucciones en `AGENTS.md`.
- Calculadora UF/USD/EUR/UTM → pesos: `python3 "{HERE}/calculadora.py" <monto>`.
- {nombre} responde con fuente oficial; tú integras la respuesta en la gestión contable/financiera (F29, provisiones, flujo).
{MARK_FIN}
"""


def upsert_bloque(path, bloque):
    txt = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    shutil.copy2(path, path + ".bak") if os.path.exists(path) else None
    if MARK_INI in txt:
        txt = re.sub(re.escape(MARK_INI) + r".*?" + re.escape(MARK_FIN) + r"\n?", bloque, txt, flags=re.S)
    else:
        txt = txt.rstrip() + "\n\n" + bloque
    open(path, "w", encoding="utf-8").write(txt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modo", choices=["agente", "subagente"], required=True)
    ap.add_argument("--nombre", required=True)
    ap.add_argument("--padre", help="archivo de instrucciones del agente principal contable/financiero")
    ap.add_argument("--sin-skill", action="store_true")
    ap.add_argument("--sin-claude", action="store_true")
    a = ap.parse_args()
    nombre, slug = a.nombre.strip(), slugify(a.nombre)
    padre = os.path.abspath(os.path.expanduser(a.padre)) if a.padre else None
    if a.modo == "subagente" and not padre:
        ap.error("--padre es obligatorio en modo subagente")
    hechos = []

    # 1. identidad
    os.makedirs(os.path.join(HERE, "config"), exist_ok=True)
    ident = {"nombre": nombre, "slug": slug, "modo": a.modo, "agente_principal": padre, "carpeta": HERE,
             "instalado": datetime.datetime.now().isoformat(timespec="seconds")}
    json.dump(ident, open(os.path.join(HERE, "config", "identidad.json"), "w"), ensure_ascii=False, indent=1)
    hechos.append("config/identidad.json")
    os.makedirs(os.path.join(HERE, "memoria"), exist_ok=True)

    desc = descripcion(nombre, a.modo)
    body = cuerpo(nombre, a.modo, padre)

    # 3. Claude Code: agente/subagente
    if not a.sin_claude:
        d = os.path.join(HOME, ".claude", "agents"); os.makedirs(d, exist_ok=True)
        p = os.path.join(d, f"{slug}.md")
        open(p, "w", encoding="utf-8").write(f"---\nname: {slug}\ndescription: {desc}\ntools: Bash, Read, Grep, Glob, WebFetch\n---\n\n{body}")
        hechos.append(p)

    # 4. Skill (invocable desde cualquier carpeta)
    if not a.sin_skill:
        d = os.path.join(HOME, ".claude", "skills", slug); os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "SKILL.md")
        open(p, "w", encoding="utf-8").write(
            f"---\nname: {slug}\ndescription: {desc} Úsala SIEMPRE que pregunten por impuestos en Chile o el SII, digan \"{nombre}\", "
            f"\"/{slug}\", \"asesora tributaria\" o \"pregúntale al tributario\".\n---\n\n# {nombre} — asesora tributaria SII\n\n{body}\n"
            f"Si `{HERE}/config/identidad.json` no existe, hacer el Arranque de `AGENTS.md` antes de responder.\n")
        hechos.append(p)

    # 5. modo subagente: integrar en agente principal
    if a.modo == "subagente":
        upsert_bloque(padre, bloque_padre(nombre, slug)); hechos.append(f"{padre} (sección delegación; copia .bak)")

    print(f"{nombre} instalado como {a.modo}.\nArchivos:")
    for h in hechos:
        print(" -", h)


if __name__ == "__main__":
    main()
