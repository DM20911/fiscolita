#!/usr/bin/env python3
"""Genera las páginas SEO del sitio (web/): una página por calculadora, 404, sitemap, robots, llms.txt y security.txt.

    python3 _tools/gen_web.py

Toma de web/index.html el estilo, el menú y el pie (fuente única). Ejecutar después de cambiar index.html
o el contenido de PAGINAS, y luego publicar con `cd web && vercel deploy --prod`.
"""
import datetime, html, json, os, re

BASE = "https://fiscolita.optimizaria.com"
GH = "https://github.com/OptimizarIA-Consulting/fiscolita"
AQUI = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(AQUI, "..", "web")
HOY = datetime.date.today().isoformat()

idx = open(os.path.join(WEB, "index.html"), encoding="utf-8").read()
ESTILO = re.search(r"<style>.*?</style>", idx, re.S).group(0)
MENU = re.search(r"<nav>.*?</nav>", idx, re.S).group(0).replace('href="#', 'href="/#')
PIE = re.search(r"<footer>.*?</footer>", idx, re.S).group(0)

EXTRA = """<style>
header.interior{padding:40px 0 84px}
header.interior h1{font-size:clamp(32px,5vw,52px);letter-spacing:-1.5px;line-height:1.05;margin:10px 0 12px}
.migas{display:flex;flex-wrap:wrap;gap:6px;list-style:none;padding:0;margin:0;font-size:14px;color:#A9C1E0}
.migas li+li:before{content:"›";margin-right:6px;opacity:.7}
.migas a{text-decoration:none}.migas a:hover{text-decoration:underline}
.texto{max-width:780px}
.texto h2{font-size:clamp(24px,3vw,30px);margin:44px 0 10px}
.texto p,.texto li{font-size:17px}
.texto table{width:100%;border-collapse:collapse;margin:14px 0;background:var(--tarjeta);border:1px solid var(--borde);border-radius:14px;overflow:hidden}
.texto th,.texto td{padding:10px 14px;border-bottom:1px solid var(--borde);text-align:left;font-size:15px}
.texto th{background:var(--campo)}
.faq details{background:var(--tarjeta);border:1px solid var(--borde);border-radius:14px;padding:14px 18px;margin-bottom:10px}
.faq summary{font-weight:700;cursor:pointer;font-size:17px}
.faq details p{margin:10px 0 0;color:var(--suave)}
.otras{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:14px}
.otras a{display:block;background:var(--tarjeta);border:1px solid var(--borde);border-radius:14px;padding:16px;text-decoration:none;font-weight:700}
.otras a span{display:block;font-weight:400;color:var(--suave);font-size:14px;margin-top:4px}
.otras a:hover{border-color:var(--acento)}
</style>"""

# ---------------------------------------------------------------- contenido
PAGINAS = [
  {
    "slug": "calculadora-boleta-honorarios", "sim": "bhe", "corto": "Boleta de honorarios",
    "title": "Calculadora boleta de honorarios 2026 (15,25%) · FiscolItA",
    "desc": "Calcula la retención de tu boleta de honorarios 2026 (15,25%): de bruto a líquido o cuánto boletear para recibir un monto líquido. Gratis y con fuente SII.",
    "h1": "Calculadora de boleta de honorarios 2026",
    "lead": "Ingresa el monto bruto o el líquido que quieres recibir y obtén la retención del 15,25% vigente en 2026.",
    "cuerpo": """
<h2>¿Cuánto me retienen en una boleta de honorarios en 2026?</h2>
<p>Durante 2026 la retención de las boletas de honorarios es de <b>15,25%</b> del monto bruto. Si emites una boleta por $1.000.000, el pagador retiene $152.500 y recibes $847.500. Esa retención la entera al SII a tu nombre y se descuenta de tu impuesto anual en la Operación Renta.</p>
<h2>Aumento gradual de la retención</h2>
<p>La Ley 21.133 sube la tasa año a año para financiar la cotización previsional de los trabajadores a honorarios:</p>
<table><tr><th>Año</th><th>Retención</th></tr><tr><td>2025</td><td>14,5%</td></tr><tr><td><b>2026</b></td><td><b>15,25%</b></td></tr><tr><td>2027</td><td>16%</td></tr><tr><td>2028</td><td>17%</td></tr></table>
<h2>Cómo calcular el bruto si sé cuánto quiero recibir</h2>
<p>Divide el líquido por (1 − 0,1525). Para recibir $850.000 líquidos debes boletear $1.002.950 brutos. Elige "Líquido que quiero recibir" en la calculadora y lo hace por ti.</p>
""",
    "faq": [
      ("¿Cuál es el porcentaje de retención de boleta de honorarios en 2026?", "15,25% del monto bruto, vigente desde el 1 de enero de 2026 según el aumento gradual de la Ley 21.133."),
      ("¿Quién paga la retención de la boleta de honorarios?", "Si la boleta se emite a una empresa o persona que lleva contabilidad, el pagador retiene y entera el impuesto. Si se emite a una persona natural sin obligación de retener, el emisor puede pagar la retención él mismo."),
      ("¿Recupero la retención de mi boleta de honorarios?", "Se imputa en tu declaración anual de Renta (F22) a tus impuestos y a tus cotizaciones previsionales. Si sobra, se devuelve."),
    ],
    "fuente": ("Boletas de honorarios · SII", "https://www.sii.cl/destacados/boletas_honorarios/"),
  },
  {
    "slug": "calculadora-ppm", "sim": "ppm", "corto": "PPM",
    "title": "Calculadora de PPM para el F29 · FiscolItA",
    "desc": "Calcula tu PPM del mes: ingresos brutos (código 563) por la tasa (código 115) = PPM a pagar (código 62) del Formulario 29. Gratis y con fuente SII.",
    "h1": "Calculadora de PPM para el Formulario 29",
    "lead": "El pago provisional mensual es un anticipo del impuesto a la renta que se declara cada mes en el F29.",
    "cuerpo": """
<h2>¿Qué es el PPM?</h2>
<p>Los pagos provisionales mensuales (PPM) son abonos que las empresas y algunos trabajadores independientes hacen cada mes a cuenta del impuesto anual a la renta. En abril, en la Operación Renta, se reajustan y se descuentan del impuesto que corresponde pagar.</p>
<h2>Cómo se calcula</h2>
<table><tr><th>Concepto</th><th>Código F29</th></tr><tr><td>Ingresos brutos del mes, sin IVA</td><td>563</td></tr><tr><td>Tasa de PPM</td><td>115</td></tr><tr><td>PPM a pagar</td><td>62</td></tr></table>
<p>La tasa depende de tu régimen tributario y de tus resultados anteriores. La encuentras en tu último F29 o te la informa tu contador.</p>
""",
    "faq": [
      ("¿Dónde va el PPM en el F29?", "En la línea de PPM: la base imponible en el código 563, la tasa en el código 115 y el monto a pagar en el código 62."),
      ("¿El PPM se recupera?", "Sí: en la declaración anual de Renta los PPM reajustados se imputan al impuesto del año; si exceden el impuesto, el saldo se devuelve."),
    ],
    "fuente": ("PPM en el F29 · Preguntas frecuentes SII", "https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1908.htm"),
  },
  {
    "slug": "calculadora-iva", "sim": "iva", "corto": "IVA del mes",
    "title": "Calculadora de IVA mensual (19%) · FiscolItA",
    "desc": "Calcula el IVA a pagar del mes en Chile (19%): débito fiscal de tus ventas menos crédito fiscal de tus compras, o el remanente para el mes siguiente.",
    "h1": "Calculadora de IVA mensual",
    "lead": "Ingresa tus ventas y compras netas del mes y obtén el IVA a pagar en el F29 o el remanente de crédito.",
    "cuerpo": """
<h2>Cómo se calcula el IVA a pagar</h2>
<p>El IVA en Chile es de <b>19%</b>. Cada mes declaras en el Formulario 29:</p>
<ul><li><b>Débito fiscal</b>: 19% de tus ventas netas.</li><li><b>Crédito fiscal</b>: 19% de tus compras netas respaldadas con factura.</li><li><b>IVA a pagar</b> = débito − crédito. Si el crédito es mayor, queda un <b>remanente</b> para el mes siguiente.</li></ul>
<h2>Plazo de declaración</h2>
<p>El F29 se declara y paga hasta el día 20 del mes siguiente si lo haces por internet, o hasta el día 12 en papel. Si cae en fin de semana o feriado, pasa al día hábil siguiente. Revisa el <a href="/calendario-tributario">calendario tributario</a>.</p>
""",
    "faq": [
      ("¿Cuál es la tasa de IVA en Chile?", "19% sobre el valor neto de la venta o servicio (artículo 14 del DL 825)."),
      ("¿Qué pasa si tengo más crédito que débito?", "La diferencia queda como remanente de crédito fiscal y se usa en los meses siguientes, reajustado."),
      ("¿Hasta cuándo puedo declarar el IVA?", "Hasta el día 20 del mes siguiente por internet, o hasta el 12 en papel; si es inhábil, el día hábil siguiente."),
    ],
    "fuente": ("Ley sobre Impuesto a las Ventas y Servicios (DL 825) · LeyChile", "https://www.bcn.cl/leychile/navegar?idNorma=6369"),
  },
  {
    "slug": "calculadora-multa-sii", "sim": "multa", "corto": "Multa por atraso",
    "title": "Calculadora de multa del SII por atraso · FiscolItA",
    "desc": "Estima la multa del artículo 97 N° 2 del Código Tributario y el interés penal por declarar fuera de plazo un impuesto en Chile. Gratis, con fuente oficial.",
    "h1": "Calculadora de multa por declarar atrasado",
    "lead": "Si declaraste fuera de plazo un impuesto que tenías que pagar, estima la multa y el interés penal.",
    "cuerpo": """
<h2>Multa del artículo 97 N° 2</h2>
<p>Declarar fuera de plazo un impuesto que se debía pagar tiene una multa de <b>10%</b> del impuesto adeudado. Si el atraso supera los 5 meses, sube <b>2% por cada mes o fracción adicional</b>, con un tope de <b>30%</b>.</p>
<h2>Interés penal</h2>
<p>Además se cobra interés por mora sobre el impuesto reajustado (artículo 53 del Código Tributario), con la tasa que el SII fija cada semestre. La calculadora usa la tasa vigente informada en la resolución del semestre.</p>
<h2>Antes de pagar</h2>
<p>Si regularizas antes de una fiscalización, el SII suele condonar parte de la multa y los intereses. Si el impuesto era de retención o recargo (como el IVA) y no se pagó, aplica otra norma (art. 97 N° 11). Valida tu caso con tu contador.</p>
""",
    "faq": [
      ("¿Cuánto es la multa por declarar el F29 atrasado?", "Si hay impuesto a pagar: 10% del impuesto, más 2% por cada mes adicional después de 5 meses, con tope de 30% (art. 97 N° 2 del Código Tributario), más intereses."),
      ("¿El SII condona multas?", "Sí, el SII aplica una política de condonación de multas e intereses que depende de cuándo regularizas y de tu comportamiento tributario."),
    ],
    "fuente": ("Código Tributario, art. 97 y art. 53 · LeyChile", "https://www.bcn.cl/leychile/navegar?idNorma=6374"),
  },
  {
    "slug": "calculadora-impuesto-unico", "sim": "sueldo", "corto": "Impuesto de un sueldo",
    "title": "Calculadora impuesto único al sueldo 2026 · FiscolItA",
    "desc": "Calcula el impuesto único de segunda categoría de tu sueldo con la tabla de tramos en UTM del mes y la UTM del día. Gratis y con fuente SII.",
    "h1": "Calculadora de impuesto único al sueldo",
    "lead": "Calcula cuánto impuesto único de segunda categoría se descuenta de tu sueldo este mes, con la UTM vigente.",
    "cuerpo": """
<h2>Tramos del impuesto único (mensual)</h2>
<p>El impuesto único de segunda categoría lo retiene tu empleador cada mes. Se calcula sobre la renta líquida imponible (sueldo imponible menos AFP, salud y seguro de cesantía) con tramos en UTM:</p>
<table><tr><th>Renta mensual en UTM</th><th>Tasa del tramo</th></tr>
<tr><td>Hasta 13,5</td><td>Exento</td></tr><tr><td>13,5 a 30</td><td>4%</td></tr><tr><td>30 a 50</td><td>8%</td></tr><tr><td>50 a 70</td><td>13,5%</td></tr><tr><td>70 a 90</td><td>23%</td></tr><tr><td>90 a 120</td><td>30,4%</td></tr><tr><td>120 a 310</td><td>35%</td></tr><tr><td>Más de 310</td><td>40%</td></tr></table>
<p>Cada tasa se aplica solo a la parte de la renta que cae en ese tramo. La calculadora usa la UTM del mes.</p>
""",
    "faq": [
      ("¿Desde qué sueldo se paga impuesto en Chile?", "Desde una renta líquida imponible mensual superior a 13,5 UTM. Bajo ese monto el sueldo está exento."),
      ("¿Qué es la renta líquida imponible?", "El sueldo imponible menos las cotizaciones obligatorias de AFP, salud y seguro de cesantía."),
    ],
    "fuente": ("Impuesto Único de Segunda Categoría 2026 · SII", "https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm"),
  },
  {
    "slug": "conversor-uf-utm-dolar", "sim": "conv", "corto": "UF, UTM, dólar y euro",
    "title": "Valor UF, UTM, dólar y euro hoy en pesos · FiscolItA",
    "desc": "Convierte UF, UTM, dólares y euros a pesos chilenos con los valores del día publicados por el SII y el Banco Central.",
    "h1": "Conversor UF, UTM, dólar y euro a pesos",
    "lead": "Valores del día de la UF, UTM, dólar observado y euro, y su equivalencia en pesos chilenos.",
    "cuerpo": """
<h2>¿Qué son la UF y la UTM?</h2>
<ul><li><b>UF (Unidad de Fomento)</b>: unidad reajustable según la inflación. Tiene un valor distinto cada día; cada mes se publica el período del 10 al 9 del mes siguiente.</li>
<li><b>UTM (Unidad Tributaria Mensual)</b>: unidad que usa el SII para multas, tramos de impuestos y montos tributarios. Cambia cada mes.</li>
<li><b>Dólar y euro</b>: tipos de cambio observados que publica el Banco Central.</li></ul>
""",
    "faq": [
      ("¿Dónde se publica el valor oficial de la UF y la UTM?", "En la sección Valores y fechas del sitio del SII."),
      ("¿Cada cuánto cambia la UTM?", "Una vez al mes, según la variación del IPC."),
    ],
    "fuente": ("Valores y fechas · SII", "https://www.sii.cl/valores_y_fechas/"),
  },
  {
    "slug": "calendario-tributario", "sim": None, "corto": "Calendario tributario",
    "title": "Calendario tributario: vencimientos F29 y Renta · FiscolItA",
    "desc": "Próximos vencimientos tributarios en Chile calculados con días hábiles: F29 y F50, Operación Renta F22, contribuciones y declaraciones juradas.",
    "h1": "Calendario tributario: próximos vencimientos",
    "lead": "Las fechas que vienen, calculadas con días hábiles y feriados de Chile.",
    "bloque": '<div class="cal" id="cal"></div>',
    "attrs": ' data-dias="120" data-eventos="20"',
    "cuerpo": """
<h2>Fechas que se repiten cada año</h2>
<table><tr><th>Obligación</th><th>Plazo</th></tr>
<tr><td>F29 y F50 por internet</td><td>Hasta el día 20 de cada mes</td></tr>
<tr><td>F29 en papel</td><td>Hasta el día 12 de cada mes</td></tr>
<tr><td>Declaraciones juradas anuales</td><td>Marzo, según el suplemento del SII</td></tr>
<tr><td>Operación Renta (F22)</td><td>Todo abril</td></tr>
<tr><td>Contribuciones</td><td>Cuotas en abril, junio, septiembre y noviembre</td></tr></table>
<p>Si un plazo cae sábado, domingo o feriado, pasa al día hábil siguiente.</p>
<p>Con el bot de Telegram de Fiscol<span class="ia">I</span>t<span class="ia">A</span>, el comando <code>/alertas</code> te avisa 3 días antes, el día anterior y el mismo día.</p>
""",
    "faq": [
      ("¿Hasta qué día se declara el F29?", "Hasta el día 20 de cada mes por internet y hasta el día 12 en papel; si cae en día inhábil, se corre al hábil siguiente."),
      ("¿Cuándo es la Operación Renta?", "En abril de cada año se presenta el Formulario 22 de la declaración anual de impuestos a la renta."),
    ],
    "fuente": ("Valores y fechas · SII", "https://www.sii.cl/valores_y_fechas/"),
  },
  {
    "slug": "novedades-sii", "sim": None, "corto": "Novedades del SII",
    "title": "Últimas circulares y resoluciones del SII · FiscolItA",
    "desc": "Las circulares, resoluciones y oficios más recientes publicados por el Servicio de Impuestos Internos de Chile, consultados en vivo.",
    "h1": "Últimas circulares, resoluciones y oficios del SII",
    "lead": "Lo último que ha publicado el SII, consultado en vivo en www.sii.cl.",
    "bloque": '<p class="fuente" id="nov-act"></p><div class="nov" id="nov"><div><div class="esqueleto"></div><div class="esqueleto"></div></div><div><div class="esqueleto"></div><div class="esqueleto"></div></div><div><div class="esqueleto"></div><div class="esqueleto"></div></div></div>',
    "attrs": ' data-n="8"',
    "cuerpo": """
<h2>Qué es cada documento</h2>
<ul><li><b>Circulares</b>: instrucciones generales del SII sobre cómo aplicar las leyes tributarias.</li>
<li><b>Resoluciones</b>: decisiones administrativas, como plazos, formularios y procedimientos.</li>
<li><b>Oficios</b>: respuestas del SII a consultas de contribuyentes, que muestran su interpretación en casos concretos.</li></ul>
<p>Fiscol<span class="ia">I</span>t<span class="ia">A</span> agrega cada día estas publicaciones a su base para responder siempre al día.</p>
""",
    "faq": [
      ("¿Dónde publica el SII sus circulares?", "En la sección Normativa y legislación de www.sii.cl, ordenadas por año."),
    ],
    "fuente": ("Normativa y legislación · SII", "https://www.sii.cl/normativa_legislacion/"),
  },
]

e = html.escape
INDICADORES = re.search(r'<div class="wrap ind".*?\n</div>', idx, re.S).group(0)


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def cabeza(title, desc, url, extra=""):
    return f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta name="theme-color" content="#0B2545">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CL">
<meta property="og:site_name" content="FiscolItA">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/mascota.svg">
<link rel="apple-touch-icon" href="/assets/mascota.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{ESTILO}
{EXTRA}
{extra}
</head>"""


def otras(actual):
    return "".join(f'<a href="/{p["slug"]}">{e(p["corto"])}<span>{e(p["desc"][:70].rsplit(" ", 1)[0])}…</span></a>'
                   for p in PAGINAS if p["slug"] != actual)


for p in PAGINAS:
    url = f'{BASE}/{p["slug"]}'
    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "FiscolItA", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["corto"], "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    if p["sim"]:
        ld.append({"@context": "https://schema.org", "@type": "WebApplication", "name": p["h1"], "url": url,
                   "applicationCategory": "FinanceApplication", "operatingSystem": "Web", "inLanguage": "es-CL",
                   "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CLP"},
                   "publisher": {"@type": "Organization", "name": "OptimizarIA Consulting", "url": "https://optimizaria.com"}})
    bloque = p.get("bloque") or '<div class="panel" id="panel"></div>'
    pagina = f"""{cabeza(p["title"], p["desc"], url, "".join(jsonld(x) for x in ld))}
<body{f' data-sim="{p["sim"]}"' if p["sim"] else ""}{p.get("attrs", "")}>
{MENU}
<header class="interior">
  <div class="wrap">
    <ol class="migas"><li><a href="/">Fiscol<span class="ia">I</span>t<span class="ia">A</span></a></li><li>{e(p["corto"])}</li></ol>
    <h1>{e(p["h1"])}</h1>
    <p class="lead">{e(p["lead"])}</p>
  </div>
</header>
{INDICADORES}
<main>
<section style="padding-top:40px"><div class="wrap">{bloque}</div></section>
<section style="padding-top:0"><div class="wrap texto">
{p["cuerpo"]}
<p class="fuente">✅ Fuente oficial: <a href="{p["fuente"][1]}" target="_blank" rel="noopener">{e(p["fuente"][0])}</a> · Cálculos referenciales: valida los casos importantes con tu contador.</p>
<h2>Preguntas frecuentes</h2>
<div class="faq">{"".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p["faq"])}</div>
<h2>Pregúntale a Fiscol<span class="ia">I</span>t<span class="ia">A</span></h2>
<p>Una agente de IA que conoce los ~29.700 documentos públicos del SII y responde con la fuente oficial. Úsala en tu computador o en Telegram, como agente o como subagente de tus agentes contables. Es gratis y de código abierto.</p>
<div class="btns"><a class="btn p" href="/#usala">Cómo usarla</a><a class="btn s" style="background:var(--navy);color:#fff" href="{GH}/blob/main/TUTORIAL.md" target="_blank" rel="noopener">Tutorial paso a paso</a></div>
<h2>Otras calculadoras</h2>
<div class="otras">{otras(p["slug"])}</div>
</div></section>
</main>
{PIE}
<script src="/app.js" defer></script>
</body>
</html>
"""
    os.makedirs(os.path.join(WEB), exist_ok=True)
    open(os.path.join(WEB, f'{p["slug"]}.html'), "w", encoding="utf-8").write(pagina)

# 404
open(os.path.join(WEB, "404.html"), "w", encoding="utf-8").write(f"""{cabeza("Página no encontrada · FiscolItA", "Esta página no existe.", BASE + "/404", '<meta name="robots" content="noindex">')}
<body>
{MENU}
<header class="interior"><div class="wrap"><h1>Esta página no existe</h1><p class="lead">Puede que el enlace esté mal escrito o que la página se haya movido.</p>
<div class="btns"><a class="btn p" href="/">Ir al inicio</a></div></div></header>
<main><section><div class="wrap texto"><h2>Quizás buscabas</h2><div class="otras">{otras("")}</div></div></section></main>
{PIE}
</body>
</html>
""")

# sitemap
urls = [("/", "1.0", "daily")] + [(f'/{p["slug"]}', "0.8", "daily" if p["slug"] in ("novedades-sii", "conversor-uf-utm-dolar", "calendario-tributario") else "monthly") for p in PAGINAS]
open(os.path.join(WEB, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + "\n".join(f'  <url><loc>{BASE}{u}</loc><lastmod>{HOY}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority>'
                + (f'<image:image><image:loc>{BASE}/assets/og.png</image:loc><image:title>FiscolItA, asesora tributaria de IA del SII</image:title></image:image>'
                   f'<image:image><image:loc>{BASE}/assets/mascota.png</image:loc><image:title>Mascota de FiscolItA</image:title></image:image>' if u == "/" else "")
                + "</url>" for u, pr, c in urls)
    + "\n</urlset>\n")

open(os.path.join(WEB, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {BASE}/sitemap.xml\n")

os.makedirs(os.path.join(WEB, ".well-known"), exist_ok=True)
vence = (datetime.date.today() + datetime.timedelta(days=365)).isoformat()
sec = f"Contact: mailto:contacto@optimizaria.com\nExpires: {vence}T00:00:00.000Z\nPreferred-Languages: es, en\nCanonical: {BASE}/.well-known/security.txt\n"
open(os.path.join(WEB, ".well-known", "security.txt"), "w").write(sec)

open(os.path.join(WEB, "llms.txt"), "w", encoding="utf-8").write(f"""# FiscolItA · Asesora TributarIA del SII de Chile

> Agente de IA de código abierto experta en el Servicio de Impuestos Internos (SII) de Chile. Responde con la fuente oficial a partir de ~29.700 documentos públicos (leyes, circulares, resoluciones, oficios y preguntas frecuentes), se actualiza cada día y funciona como agente independiente o como subagente de otros agentes de IA (Claude Code, Codex, Cursor, Gemini CLI, MCP). Proyecto de OptimizarIA Consulting.

- Sitio: {BASE}/
- Código y tutorial: {GH}
- Tutorial para personas no técnicas: {GH}/blob/main/TUTORIAL.md
- Empresa: https://optimizaria.com/

## Calculadoras y herramientas

""" + "\n".join(f'- [{p["h1"]}]({BASE}/{p["slug"]}): {p["desc"]}' for p in PAGINAS) + "\n")

print(f"{len(PAGINAS)} páginas + 404, sitemap ({len(urls)} URLs), robots, security.txt y llms.txt en web/")
