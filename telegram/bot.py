#!/usr/bin/env python3
"""Bot de Telegram para FiscolItA.

Requiere un bot creado con @BotFather y UN motor de IA (ver telegram/README.md):
  API (pago por uso):   anthropic · openai · gemini · openrouter
  Local (gratis):       ollama · lmstudio · llamacpp · jan · localai · vllm · gpt4all · koboldcpp · local
  Suscripción (CLI):    claude (Claude Pro/Max + Claude Code) · codex (ChatGPT Plus/Pro + Codex CLI)
  CLI con API key:      gemini-cli (Gemini CLI + GEMINI_API_KEY)

Variables en .env (en la raíz del repo, nunca se sube a GitHub). Plantilla: .env.example
Ejecutar:  python3 telegram/bot.py      (o con uv, ver README)
"""
import json, os, re, subprocess, sys, time, traceback

import requests

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)


# ---------------- configuración (.env) ----------------
def cargar_env(path=os.path.join(BASE, ".env")):
    if not os.path.exists(path):
        return
    for linea in open(path, encoding="utf-8"):
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        k, v = linea.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


cargar_env()
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
PERMITIDOS = {x.strip() for x in os.environ.get("TELEGRAM_ALLOWED_USERS", "").split(",") if x.strip()}
BACKEND = {"api": "anthropic"}.get(os.environ.get("FISCOLITA_BACKEND", "anthropic").lower(), os.environ.get("FISCOLITA_BACKEND", "anthropic").lower())
MODELO = os.environ.get("FISCOLITA_MODEL", "")
ESFUERZO = os.environ.get("FISCOLITA_EFFORT", "medium")
MAX_MENSAJES = int(os.environ.get("FISCOLITA_MAX_MENSAJES", "60"))  # al superar, conversación nueva
TG = f"https://api.telegram.org/bot{TOKEN}"


def identidad():
    try:
        return json.load(open(os.path.join(BASE, "config", "identidad.json"), encoding="utf-8")).get("nombre", "FiscolItA")
    except Exception:
        return "FiscolItA"


NOMBRE = identidad()


# ---------------- Telegram ----------------
def tg(metodo, **datos):
    r = requests.post(f"{TG}/{metodo}", json=datos, timeout=70)
    return r.json()


def enviar(chat_id, texto):
    texto = texto.strip() or "(sin respuesta)"
    for i in range(0, len(texto), 4000):
        trozo = texto[i:i + 4000]
        r = tg("sendMessage", chat_id=chat_id, text=trozo, parse_mode="Markdown", disable_web_page_preview=True)
        if not r.get("ok"):  # Markdown inválido → texto plano
            tg("sendMessage", chat_id=chat_id, text=trozo, disable_web_page_preview=True)


# ---------------- herramientas locales (backend api) ----------------
def _py(*args, timeout=180):
    r = subprocess.run([sys.executable, *args], cwd=BASE, capture_output=True, text=True, timeout=timeout)
    return (r.stdout or r.stderr or "").strip()[:30000] or "Sin resultados."


def h_buscar(consulta, categoria="", n=10):
    a = ["buscar.py", consulta, "-n", str(max(1, min(int(n), 40)))]
    return _py(*a, *(["-c", categoria] if categoria else []))


def h_leer_documento(archivo, desde=0, max_chars=20000):
    p = os.path.realpath(os.path.join(BASE, archivo))
    if not p.startswith(os.path.join(BASE, "docs") + os.sep) or not os.path.exists(p):
        return "Archivo no válido (debe estar dentro de docs/)."
    t = open(p, encoding="utf-8").read()
    desde = int(desde); chunk = t[desde:desde + min(int(max_chars), 40000)]
    resto = len(t) - desde - len(chunk)
    return chunk + (f"\n\n[… quedan {resto} caracteres; usar desde={desde + len(chunk)}]" if resto > 0 else "")


def h_ultimas_normas(tipo, n=5, materia=""):
    if tipo not in ("circulares", "resoluciones", "oficios"):
        return "tipo: circulares | resoluciones | oficios"
    return _py("en_vivo.py", tipo, "-n", str(n), *(["--materia", materia] if materia and tipo == "oficios" else []))


def h_valor_indicador(indicador):
    return _py("en_vivo.py", "valor", indicador if indicador in ("utm", "uf", "dolar") else "utm")


def h_pagina_sii(url):
    if not re.match(r"^https?://(www\.)?sii\.cl/", url):
        return "Solo páginas públicas de www.sii.cl."
    return _py("en_vivo.py", "pagina", url)


def h_calculadora(monto=""):
    return _py("calculadora.py", *([monto] if monto else []))


def h_simulador(tipo, monto, monto2="", meses=0):
    a = {"bhe": [monto], "bhe_liquido": [monto, "--liquido"], "ppm": [monto, monto2 or "0,25"], "iva": [monto, monto2 or "0"],
         "multa": [monto, str(meses or 1)], "sueldo": [monto]}.get(tipo)
    if a is None:
        return "tipo: bhe | bhe_liquido | ppm | iva | multa | sueldo"
    return _py("simuladores.py", tipo.replace("_liquido", ""), *a)


def h_calendario(dias=45):
    return _py("calendario.py", "--dias", str(max(1, min(int(dias), 400))))


def _tool(name, desc, props, req):
    return {"name": name, "description": desc, "strict": True,
            "input_schema": {"type": "object", "properties": props, "required": req, "additionalProperties": False}}


TOOLS = [
    _tool("buscar", "Busca en la base local del SII (~29.700 docs: leyes, circulares, resoluciones, oficios, FAQ, ayudas, valores). "
          "Sintaxis FTS5: palabras = AND, \"frase exacta\", OR, prefijo*. Devuelve título, url, archivo y extracto.",
          {"consulta": {"type": "string"},
           "categoria": {"type": "string", "description": "vacío o: ley, faq, circular, resolucion, jurisprudencia, normativa, valores, "
                         "servicios_online, ayuda, formulario, factura_electronica, declaraciones_juradas, noticia, otros"},
           "n": {"type": "integer", "description": "resultados (1-40)"}}, ["consulta", "categoria", "n"]),
    _tool("leer_documento", "Lee un documento de la base local usando la ruta 'archivo' que devuelve buscar (docs/...md). Paginar con desde.",
          {"archivo": {"type": "string"}, "desde": {"type": "integer"}, "max_chars": {"type": "integer"}}, ["archivo", "desde", "max_chars"]),
    _tool("ultimas_normas", "Últimas circulares, resoluciones u oficios publicados hoy en www.sii.cl (en vivo).",
          {"tipo": {"type": "string", "enum": ["circulares", "resoluciones", "oficios"]}, "n": {"type": "integer"},
           "materia": {"type": "string", "description": "solo oficios: RENTA | IVA | OTROS, o vacío"}}, ["tipo", "n", "materia"]),
    _tool("valor_indicador", "Tabla oficial del año de UTM, UF o dólar desde www.sii.cl (en vivo).",
          {"indicador": {"type": "string", "enum": ["utm", "uf", "dolar"]}}, ["indicador"]),
    _tool("pagina_sii", "Descarga una página o PDF público de www.sii.cl como texto.", {"url": {"type": "string"}}, ["url"]),
    _tool("calculadora", "Convierte un monto en UF, USD, EUR y UTM a pesos chilenos con valores del día. Vacío = valor de 1 unidad. "
          "Acepta formato chileno (\"1.500,5\").", {"monto": {"type": "string"}}, ["monto"]),
    _tool("simulador", "Simuladores en pesos: bhe (retención boleta de honorarios desde el bruto), bhe_liquido (bruto necesario para un líquido), "
          "ppm (monto=ingresos netos del mes, monto2=tasa %), iva (monto=ventas netas, monto2=compras netas), "
          "multa (monto=impuesto adeudado, meses=meses de atraso; art. 97 N°2 + interés penal vigente), "
          "sueldo (monto=renta líquida imponible → impuesto único 2ª categoría).",
          {"tipo": {"type": "string", "enum": ["bhe", "bhe_liquido", "ppm", "iva", "multa", "sueldo"]}, "monto": {"type": "string"},
           "monto2": {"type": "string"}, "meses": {"type": "integer"}}, ["tipo", "monto", "monto2", "meses"]),
    _tool("calendario", "Próximos vencimientos tributarios (F29/F50, F22, contribuciones, DJ, cambio UF) en los próximos N días.",
          {"dias": {"type": "integer"}}, ["dias"]),
]
HANDLERS = {"buscar": h_buscar, "leer_documento": h_leer_documento, "ultimas_normas": h_ultimas_normas,
            "valor_indicador": h_valor_indicador, "pagina_sii": h_pagina_sii, "calculadora": h_calculadora,
            "simulador": h_simulador, "calendario": h_calendario}


def system_prompt():
    partes = [f"Eres {NOMBRE}, asesora tributaria de IA experta en el SII de Chile. Respondes por Telegram: "
              "mensajes breves, sin tablas anchas, Markdown simple de Telegram (*negrita*, listas con guiones).",
              "Usa las herramientas: buscar → leer_documento → (en vivo si depende de la fecha) → calculadora para todo monto en UF/USD/EUR/UTM. "
              "Cita siempre título + URL oficial. Si no lo encuentras, dilo. "
              "Nunca pidas claves tributarias, Clave Única ni certificados; si el usuario envía una, dile que no la comparta y no la repitas. "
              "No haces trámites por el contribuyente.",
              "Para cálculos (retención de boletas, PPM, IVA, multas por atraso, impuesto de un sueldo) usa la herramienta simulador; "
              "para fechas de vencimiento, calendario.",
              "Si el usuario envía una foto o documento (factura, notificación, carta, formulario del SII), explica qué es, qué le piden, "
              "el plazo y qué hacer, citando la norma o la ayuda del SII que corresponda.",
              "Termina cada respuesta normativa con una línea de sello: "
              "'✅ Fuente oficial SII · <fecha del documento>' y, si la norma fue modificada o dejada sin efecto, '⚠️ Modificada por <norma>'."]
    for f in ("agente/IDENTIDAD.md", "agente/CONTEXTO.md", "agente/REGLAS.md"):
        try:
            partes.append(open(os.path.join(BASE, f), encoding="utf-8").read())
        except Exception:
            pass
    return "\n\n".join(partes)


# ---------------- backend: API de Anthropic ----------------
class BackendAPI:
    def __init__(self):
        import anthropic
        self.anthropic = anthropic
        self.client = anthropic.Anthropic()  # lee ANTHROPIC_API_KEY
        self.chats = {}  # chat_id -> {"system": [...], "messages": [...]} (solo se agrega, nunca se edita)

    def nueva(self, chat_id):
        # system fijo por conversación (cacheado); se reconstruye solo al iniciar una conversación nueva
        self.chats[chat_id] = {"system": [{"type": "text", "text": system_prompt(), "cache_control": {"type": "ephemeral"}}],
                               "messages": []}

    def responder(self, chat_id, texto, imagenes=()):
        if chat_id not in self.chats or len(self.chats[chat_id]["messages"]) > MAX_MENSAJES:
            self.nueva(chat_id)
        c = self.chats[chat_id]
        contenido = [{"type": "image", "source": {"type": "base64", "media_type": mime, "data": b64}} for mime, b64, _ in imagenes]
        c["messages"].append({"role": "user", "content": contenido + [{"type": "text", "text": texto}] if contenido else texto})
        for _ in range(25):
            r = self.client.beta.messages.create(
                model=MODELO or "claude-opus-5-5", max_tokens=16000, system=c["system"], tools=TOOLS, messages=c["messages"],
                thinking={"type": "adaptive"}, output_config={"effort": ESFUERZO},
                cache_control={"type": "ephemeral"},
                betas=["server-side-fallback-2026-07-01"], fallbacks="default",
            )
            c["messages"].append({"role": "assistant", "content": r.content})
            if r.stop_reason == "refusal":
                self.nueva(chat_id)
                return "No puedo responder esa consulta. Prueba reformulándola (conversación reiniciada)."
            if r.stop_reason == "pause_turn":
                continue
            usos = [b for b in r.content if b.type == "tool_use"]
            if r.stop_reason != "tool_use" or not usos:
                txt = "\n".join(b.text for b in r.content if b.type == "text")
                return txt + ("\n\n_(respuesta cortada por largo)_" if r.stop_reason == "max_tokens" else "")
            resultados = []
            for b in usos:
                try:
                    out, err = HANDLERS[b.name](**b.input), False
                except Exception as e:
                    out, err = f"Error en {b.name}: {e}", True
                resultados.append({"type": "tool_result", "tool_use_id": b.id, "content": out, "is_error": err})
            c["messages"].append({"role": "user", "content": resultados})
        return "La consulta requirió demasiados pasos. Intenta acotarla."


# ---------------- backend: suscripción Claude (Claude Code) ----------------
class BackendClaude:
    PERMISOS = ["Bash(python3 buscar.py:*)", "Bash(python3 en_vivo.py:*)", "Bash(python3 calculadora.py:*)",
                "Bash(python3 simuladores.py:*)", "Bash(python3 calendario.py:*)",
                "Read", "Grep", "Glob", "WebFetch(domain:www.sii.cl)"]

    def __init__(self):
        self.sesiones = {}

    def nueva(self, chat_id):
        self.sesiones.pop(chat_id, None)

    def responder(self, chat_id, texto, imagenes=()):
        if imagenes:  # Claude Code lee la imagen desde el archivo temporal
            texto += "\n\nImagen(es) adjunta(s), léelas con Read: " + ", ".join(p for _, _, p in imagenes)
        cmd = [os.environ.get("CLAUDE_BIN", "claude"), "-p", "--output-format", "json", *(["--model", MODELO] if MODELO else []),
               "--allowedTools", *self.PERMISOS,
               "--append-system-prompt", "Respondes por Telegram: mensajes breves, Markdown simple, sin tablas anchas."]
        if chat_id in self.sesiones:
            cmd += ["--resume", self.sesiones[chat_id]]
        r = subprocess.run(cmd, input=texto, cwd=BASE, capture_output=True, text=True, timeout=900)  # pregunta por stdin
        try:
            d = json.loads(r.stdout)
        except Exception:
            return "Error ejecutando Claude Code: " + (r.stderr or r.stdout)[-500:]
        if d.get("session_id"):
            self.sesiones[chat_id] = d["session_id"]
        return d.get("result") or "(sin respuesta)"


# ---------------- backend: APIs compatibles con OpenAI (OpenAI, Gemini, OpenRouter, Ollama) ----------------
COMPAT = {  # base_url por defecto, variable con la clave
    "openai": ("https://api.openai.com/v1", "OPENAI_API_KEY"),
    "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
    "ollama": ("http://localhost:11434/v1", None),
    "lmstudio": ("http://localhost:1234/v1", None),
    "llamacpp": ("http://localhost:8080/v1", None),     # llama-server
    "jan": ("http://localhost:1337/v1", None),
    "localai": ("http://localhost:8080/v1", None),
    "vllm": ("http://localhost:8000/v1", None),
    "gpt4all": ("http://localhost:4891/v1", None),
    "koboldcpp": ("http://localhost:5001/v1", None),
    "local": ("http://localhost:8080/v1", None),        # cualquier servidor compatible con OpenAI (usar FISCOLITA_BASE_URL)
}
OAI_TOOLS = [{"type": "function", "function": {"name": x["name"], "description": x["description"], "parameters": x["input_schema"]}}
             for x in TOOLS]


class BackendCompat:
    def __init__(self, proveedor):
        base, var = COMPAT[proveedor]
        self.url = os.environ.get("FISCOLITA_BASE_URL", base).rstrip("/") + "/chat/completions"
        self.key = os.environ.get(var, "") if var else ""
        self.chats = {}

    def nueva(self, chat_id):
        self.chats[chat_id] = [{"role": "system", "content": system_prompt()}]

    def responder(self, chat_id, texto, imagenes=()):
        if chat_id not in self.chats or len(self.chats[chat_id]) > MAX_MENSAJES:
            self.nueva(chat_id)
        msgs = self.chats[chat_id]
        partes = [{"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}} for mime, b64, _ in imagenes]
        msgs.append({"role": "user", "content": partes + [{"type": "text", "text": texto}] if partes else texto})
        h = {"Content-Type": "application/json", **({"Authorization": f"Bearer {self.key}"} if self.key else {})}
        for _ in range(25):
            r = requests.post(self.url, headers=h, json={"model": MODELO or "local-model", "messages": msgs, "tools": OAI_TOOLS}, timeout=600)
            if r.status_code != 200:
                msgs.pop()
                return f"Error del proveedor ({r.status_code}): {r.text[:300]}"
            m = r.json()["choices"][0]["message"]
            msgs.append({k: v for k, v in m.items() if k in ("role", "content", "tool_calls") and v is not None})
            if not m.get("tool_calls"):
                return m.get("content") or "(sin respuesta)"
            for tc in m["tool_calls"]:
                try:
                    out = HANDLERS[tc["function"]["name"]](**json.loads(tc["function"]["arguments"] or "{}"))
                except Exception as e:
                    out = f"Error: {e}"
                msgs.append({"role": "tool", "tool_call_id": tc["id"], "content": out})
        return "La consulta requirió demasiados pasos. Intenta acotarla."


# ---------------- backend: CLIs de suscripción sin herramientas propias (Codex, Gemini CLI) ----------------
def contexto_local(texto):
    """Busca en la base local y arma el contexto que se entrega al modelo (para CLIs sin herramientas)."""
    res = h_buscar(texto, "", 6) if len(texto) > 3 else ""
    if res == "Sin resultados.":
        res = _py("buscar.py", texto, "-n", "6", "--or")
    archivos = re.findall(r"^\s+(docs/\S+\.md)$", res, re.M)[:3]
    docs = "\n\n".join(f"### {a}\n{h_leer_documento(a, 0, 4000)}" for a in archivos)
    calc = h_calculadora(re.search(r"\d[\d.,]*", texto).group()) if re.search(r"\b(uf|utm|usd|d[oó]lar|euro|eur)\b", texto, re.I) and re.search(r"\d", texto) else ""
    return f"## Resultados de búsqueda\n{res}\n\n## Documentos\n{docs}\n\n" + (f"## Calculadora (valores del día)\n{calc}\n" if calc else "")


class BackendCLI:
    def __init__(self, tipo):
        self.tipo, self.hist = tipo, {}

    def nueva(self, chat_id):
        self.hist.pop(chat_id, None)

    def responder(self, chat_id, texto, imagenes=()):
        if imagenes:
            return f"El motor {self.tipo} no lee imágenes desde el bot. Envía el documento como PDF o usa un motor con visión (anthropic, openai, gemini, claude)."
        h = self.hist.setdefault(chat_id, [])
        previo = "\n".join(f"{q}: {a}" for q, a in h[-6:])
        prompt = (f"{system_prompt()}\n\nResponde SOLO con la información de contexto (documentos oficiales del SII) y cita la URL. "
                  f"Si no está, dilo.\n\n{contexto_local(texto)}\n## Conversación previa\n{previo}\n\n## Pregunta\n{texto}\n")
        if self.tipo == "codex":
            cmd = [os.environ.get("CODEX_BIN", "codex"), "exec", "--skip-git-repo-check", "-"]
        else:
            cmd = [os.environ.get("GEMINI_BIN", "gemini"), "-p", "Responde la pregunta del final usando el contexto entregado."]
        if MODELO:
            cmd[1:1] = ["-m", MODELO] if self.tipo == "gemini-cli" else []
        r = subprocess.run(cmd, input=prompt, cwd=BASE, capture_output=True, text=True, timeout=900)
        out = (r.stdout or "").strip() or f"Error ejecutando {self.tipo}: {(r.stderr or '')[-400:]}"
        h += [("Usuario", texto), ("Asistente", out[:1500])]
        return out


def crear_backend():
    if BACKEND == "anthropic":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            sys.exit("FISCOLITA_BACKEND=anthropic requiere ANTHROPIC_API_KEY en .env.")
        return BackendAPI()
    if BACKEND == "claude":
        return BackendClaude()
    if BACKEND in COMPAT:
        var = COMPAT[BACKEND][1]
        if var and not os.environ.get(var):
            sys.exit(f"FISCOLITA_BACKEND={BACKEND} requiere {var} en .env.")
        if not MODELO and BACKEND not in ("lmstudio", "llamacpp", "koboldcpp", "local"):
            sys.exit(f"FISCOLITA_BACKEND={BACKEND} requiere FISCOLITA_MODEL en .env (ver telegram/README.md).")
        return BackendCompat(BACKEND)
    if BACKEND in ("codex", "gemini-cli"):
        return BackendCLI(BACKEND)
    sys.exit("FISCOLITA_BACKEND no válido: " + " | ".join(["anthropic", "claude", "codex", "gemini-cli", *COMPAT]))


# ---------------- archivos, voz, avisos ----------------
import base64, datetime, tempfile
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/Santiago")
ESTADO = os.path.join(BASE, "config", "telegram.json")
HORA_AVISOS = os.environ.get("FISCOLITA_HORA_AVISOS", "08:30")
TMP = os.path.join(BASE, "config", "tmp")


def estado():
    try:
        return json.load(open(ESTADO, encoding="utf-8"))
    except Exception:
        return {"suscritos": [], "ultimo_envio": ""}


def guardar_estado(e):
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    json.dump(e, open(ESTADO, "w", encoding="utf-8"), indent=1)


def bajar_archivo(file_id):
    info = tg("getFile", file_id=file_id)["result"]
    data = requests.get(f"https://api.telegram.org/file/bot{TOKEN}/{info['file_path']}", timeout=120).content
    return data, info["file_path"]


def pdf_a_texto(data):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(data); f.flush()
        return subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", f.name, "-"], capture_output=True, timeout=120).stdout.decode("utf-8", "replace")


def guardar_tmp(data, ext):
    os.makedirs(TMP, exist_ok=True)
    p = os.path.join(TMP, f"{int(time.time() * 1000)}{ext}")
    open(p, "wb").write(data)
    return p


def transcribir(data):
    """Nota de voz → texto. Usa OPENAI_API_KEY (Whisper) o GROQ_API_KEY, o el comando local `whisper` si está instalado."""
    for var, url, modelo in (("OPENAI_API_KEY", "https://api.openai.com/v1/audio/transcriptions", os.environ.get("FISCOLITA_STT_MODEL", "whisper-1")),
                             ("GROQ_API_KEY", "https://api.groq.com/openai/v1/audio/transcriptions", "whisper-large-v3")):
        if os.environ.get(var):
            r = requests.post(url, headers={"Authorization": f"Bearer {os.environ[var]}"},
                              files={"file": ("voz.ogg", data, "audio/ogg")}, data={"model": modelo, "language": "es"}, timeout=300)
            if r.status_code == 200:
                return r.json().get("text", "")
    import shutil
    if shutil.which("whisper"):
        p = guardar_tmp(data, ".ogg")
        subprocess.run(["whisper", p, "--language", "es", "--model", "base", "--output_format", "txt", "--output_dir", TMP],
                       capture_output=True, timeout=900)
        txt = p[:-4] + ".txt"
        if os.path.exists(txt):
            return open(txt, encoding="utf-8").read()
    return None


def novedades_de(fecha):
    try:
        reg = json.load(open(os.path.join(BASE, "config", "actualizacion.json"), encoding="utf-8"))
        return [x["titulo"] for x in reg.get("agregados", []) if x.get("fecha") == fecha]
    except Exception:
        return []


def resumen_diario():
    from actualizar_novedades import asegurar_al_dia
    import calendario
    asegurar_al_dia()
    hoy = datetime.datetime.now(TZ).date()
    partes = []
    av = calendario.avisos(hoy)
    if av:
        partes.append("*📅 Vencimientos*\n" + "\n".join(
            f"- {'HOY' if n == 0 else 'Mañana' if n == 1 else f'En {n} días'} ({d:%d-%m}): {t}" for d, t, _, n in av))
    nov = novedades_de(hoy.isoformat())
    if nov:
        partes.append("*📰 Novedades del SII*\n" + "\n".join(f"- {x[:300]}" for x in nov[:15]))
    return f"Buenos días ☀️ — {NOMBRE}\n\n" + "\n\n".join(partes) if partes else ""


def revisar_avisos():
    ahora = datetime.datetime.now(TZ)
    e = estado()
    if not e.get("suscritos") or e.get("ultimo_envio") == ahora.date().isoformat() or ahora.strftime("%H:%M") < HORA_AVISOS:
        return
    e["ultimo_envio"] = ahora.date().isoformat(); guardar_estado(e)
    msg = resumen_diario()
    if msg:
        for c in e["suscritos"]:
            enviar(c, msg)


def simular_cmd(cmd, args):
    tipo = {"bhe": "bhe", "liquido": "bhe_liquido", "ppm": "ppm", "iva": "iva", "multa": "multa", "sueldo": "sueldo"}[cmd]
    a = args + ["", ""]
    return h_simulador(tipo, a[0], a[1] if tipo in ("ppm", "iva") else "", int(a[1]) if tipo == "multa" and a[1].isdigit() else 0)


# ---------------- bucle principal ----------------
AYUDA = (f"Hola, soy *{NOMBRE}*, asesora tributaria (SII Chile) 🇨🇱\n\n"
         "Pregúntame lo que quieras: F29, IVA, boletas, PPM, plazos, circulares… También puedes:\n"
         "📷 enviar una *foto o PDF* (factura, notificación, carta del SII) y te explico qué es\n"
         "🎙️ mandar una *nota de voz*\n"
         "💱 enviar solo un monto (`15`) → UF/USD/EUR/UTM en pesos\n\n"
         "*Simuladores*\n/bhe 1000000 — retención boleta de honorarios\n/liquido 850000 — cuánto boletear para recibir ese líquido\n"
         "/ppm 10000000 1,1 — PPM (ingresos netos, tasa %)\n/iva 5000000 2000000 — IVA (ventas netas, compras netas)\n"
         "/multa 500000 7 — multa e interés por atraso (impuesto, meses)\n/sueldo 2500000 — impuesto único de un sueldo\n\n"
         "*Avisos*\n/calendario — próximos vencimientos\n/novedades — normas nuevas del SII de hoy\n"
         "/alertas — recibir cada mañana vencimientos y novedades (/alertas off para dejar)\n\n"
         "/contador — resumen de tu caso listo para reenviar a tu contador\n/nuevo — conversación nueva · /id — tu ID")


def procesar(backend, chat_id, m):
    texto = (m.get("text") or m.get("caption") or "").strip()
    imagenes = []
    if m.get("voice") or m.get("audio"):
        tg("sendChatAction", chat_id=chat_id, action="typing")
        data, _ = bajar_archivo((m.get("voice") or m.get("audio"))["file_id"])
        txt = transcribir(data)
        if not txt:
            return enviar(chat_id, "No puedo transcribir notas de voz: agrega OPENAI_API_KEY o GROQ_API_KEY al .env, o instala `whisper`.")
        enviar(chat_id, f"🎙️ _{txt.strip()}_")
        texto = txt.strip()
    elif m.get("photo"):
        data, ruta = bajar_archivo(m["photo"][-1]["file_id"])
        imagenes.append(("image/jpeg", base64.b64encode(data).decode(), guardar_tmp(data, ".jpg")))
        texto = texto or "¿Qué es este documento, qué me piden y qué debo hacer?"
    elif m.get("document"):
        doc = m["document"]; mime = doc.get("mime_type", "")
        if doc.get("file_size", 0) > 20_000_000:
            return enviar(chat_id, "El archivo supera 20 MB.")
        data, ruta = bajar_archivo(doc["file_id"])
        if "pdf" in mime:
            contenido = pdf_a_texto(data)[:60000]
            texto = (texto or "¿Qué es este documento, qué me piden y qué debo hacer?") + f"\n\n--- Documento adjunto ({doc.get('file_name', 'pdf')}) ---\n{contenido}"
        elif mime.startswith("image/"):
            imagenes.append((mime, base64.b64encode(data).decode(), guardar_tmp(data, os.path.splitext(ruta)[1] or ".jpg")))
            texto = texto or "¿Qué es este documento, qué me piden y qué debo hacer?"
        else:
            return enviar(chat_id, "Por ahora leo PDF e imágenes.")
    if not texto:
        return
    cmd, *args = texto.split()
    cmd = cmd.lstrip("/").split("@")[0].lower() if texto.startswith("/") else ""
    if cmd in ("start", "ayuda", "help"):
        return enviar(chat_id, AYUDA)
    if cmd == "nuevo":
        backend.nueva(chat_id); return enviar(chat_id, "Conversación nueva.")
    if cmd in ("bhe", "liquido", "ppm", "iva", "multa", "sueldo"):
        return enviar(chat_id, simular_cmd(cmd, args) if args else AYUDA)
    if cmd == "calendario":
        return enviar(chat_id, "*📅 Próximos vencimientos*\n" + h_calendario(int(args[0]) if args and args[0].isdigit() else 45))
    if cmd == "novedades":
        from actualizar_novedades import asegurar_al_dia
        asegurar_al_dia()
        nov = novedades_de(datetime.datetime.now(TZ).date().isoformat())
        return enviar(chat_id, "*📰 Novedades de hoy*\n" + "\n".join(f"- {x}" for x in nov) if nov else
                      "Hoy no hay normas nuevas. Últimas circulares:\n" + h_ultimas_normas("circulares", 3))
    if cmd == "alertas":
        e = estado(); s = set(e.get("suscritos", []))
        if args and args[0].lower() in ("off", "no", "salir"):
            s.discard(chat_id); msg = "Alertas desactivadas."
        else:
            s.add(chat_id); msg = f"Listo ✅ Cada día a las {HORA_AVISOS} te aviso vencimientos (3 días antes, el día anterior y el mismo día) y normas nuevas del SII."
        e["suscritos"] = sorted(s); guardar_estado(e)
        return enviar(chat_id, msg)
    if cmd == "contador":
        texto = ("Redacta un resumen de mi caso tributario de esta conversación para reenviarlo a mi contador: contexto, pregunta concreta, "
                 "lo que encontraste (con normas y URLs), montos calculados y qué debe validar él. Formato breve, listo para copiar.")
    elif re.fullmatch(r"\$?\s*[\d.,]+", texto):
        texto = f"Calcula {texto} en UF, USD, EUR y UTM a pesos (tabla completa)."
    tg("sendChatAction", chat_id=chat_id, action="typing")
    try:
        enviar(chat_id, backend.responder(chat_id, texto, imagenes))
    except Exception as e:
        traceback.print_exc()
        backend.nueva(chat_id)
        enviar(chat_id, f"Ocurrió un error ({type(e).__name__}). Conversación reiniciada; intenta de nuevo.")


def main():
    if not TOKEN:
        sys.exit("Falta TELEGRAM_BOT_TOKEN en .env (ver telegram/README.md).")
    backend = crear_backend()
    yo = tg("getMe")
    if not yo.get("ok"):
        sys.exit(f"Token de Telegram inválido: {yo}")
    tg("setMyCommands", commands=[{"command": c, "description": d} for c, d in (
        ("ayuda", "qué puedo hacer"), ("calendario", "próximos vencimientos"), ("novedades", "normas nuevas del SII hoy"),
        ("alertas", "avisos diarios (off para dejar)"), ("bhe", "retención boleta de honorarios"), ("liquido", "bruto para un líquido"),
        ("ppm", "simular PPM"), ("iva", "simular IVA"), ("multa", "multa e interés por atraso"), ("sueldo", "impuesto único de un sueldo"),
        ("contador", "resumen para tu contador"), ("nuevo", "conversación nueva"), ("id", "ver tu ID"))])
    print(f"@{yo['result']['username']} en línea · backend={BACKEND}" + (f" · modelo={MODELO}" if MODELO else "")
          + f" · usuarios permitidos={len(PERMITIDOS)} · avisos {HORA_AVISOS}", flush=True)
    if not PERMITIDOS:
        print("AVISO: TELEGRAM_ALLOWED_USERS está vacío → nadie puede usar el bot. Escríbele /id y agrega tu ID al .env.", flush=True)
    offset = None
    while True:
        try:
            revisar_avisos()
        except Exception:
            traceback.print_exc()
        try:
            ups = tg("getUpdates", offset=offset, timeout=50, allowed_updates=["message"])
        except Exception as e:
            print("red:", e, flush=True); time.sleep(5); continue
        for u in ups.get("result", []):
            offset = u["update_id"] + 1
            m = u.get("message") or {}
            chat_id, uid = m.get("chat", {}).get("id"), str(m.get("from", {}).get("id", ""))
            if chat_id is None:
                continue
            if (m.get("text") or "").startswith("/id"):
                enviar(chat_id, f"Tu ID de Telegram es `{uid}`"); continue
            if uid not in PERMITIDOS:
                enviar(chat_id, f"No autorizado. Pide al administrador que agregue tu ID `{uid}` a TELEGRAM_ALLOWED_USERS.")
                print(f"rechazado: usuario {uid}", flush=True); continue
            procesar(backend, chat_id, m)


if __name__ == "__main__":
    main()
