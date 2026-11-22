# Fiscol**I**t**A** en Telegram

Conversa con tu asesora tributaria desde el celular. El bot corre en tu computador o servidor y usa la misma base local, las consultas en vivo al SII y la calculadora.

**⚠️ Requisito: el equipo donde corre el bot (computador o VPS) debe estar encendido, sin suspenderse y con internet todo el tiempo.** El bot no queda alojado en Telegram: si el equipo se apaga, se suspende o se cierra la terminal, deja de responder y las alertas diarias no se envían. Para uso de un equipo o de clientes, usa un servidor/VPS o un computador dedicado (ver [Dejarlo siempre encendido](#dejarlo-siempre-encendido)).

## Requisitos

Necesitas **un motor de IA**: una suscripción, una API key o un modelo local. Sin ninguno, el bot no puede responder.

| Tipo | `FISCOLITA_BACKEND` | Qué necesitas | Costo |
|---|---|---|---|
| Suscripción | `claude` | Claude Pro o Max + [Claude Code](https://claude.com/claude-code) instalado y con sesión iniciada (`claude`) en el equipo del bot | incluido en tu plan |
| Suscripción | `codex` | ChatGPT Plus o Pro + [Codex CLI](https://github.com/openai/codex) instalado y con sesión iniciada (`codex login`) | incluido en tu plan |
| CLI | `gemini-cli` | [Gemini CLI](https://github.com/google-gemini/gemini-cli) instalado, con `GEMINI_API_KEY` en el `.env` o cuenta Google Workspace / Vertex AI. Google ya no permite iniciar sesión con cuenta personal (pide migrar a Antigravity) | cuota gratuita de la API o tu plan |
| API | `anthropic` | API key de [console.anthropic.com](https://console.anthropic.com) | pago por uso |
| API | `openai` | API key de [platform.openai.com](https://platform.openai.com) + nombre del modelo | pago por uso |
| API | `gemini` | API key de [Google AI Studio](https://aistudio.google.com) + nombre del modelo | cuota gratuita y pago por uso |
| API | `openrouter` | API key de [openrouter.ai](https://openrouter.ai) + modelo (acceso a cientos de modelos) | pago por uso |
| Local | `ollama` | [Ollama](https://ollama.com) instalado y un modelo descargado (`ollama pull <modelo>`) | gratis, usa tu equipo |
| Local | `lmstudio` | [LM Studio](https://lmstudio.ai) con un modelo cargado y el servidor local encendido (pestaña *Developer*, puerto 1234) | gratis |
| Local | `llamacpp` | `llama-server` de [llama.cpp](https://github.com/ggml-org/llama.cpp) (puerto 8080) | gratis |
| Local | `jan` | [Jan](https://jan.ai) con el *Local API Server* encendido (puerto 1337) | gratis |
| Local | `localai` | [LocalAI](https://localai.io) (puerto 8080) | gratis |
| Local | `vllm` | [vLLM](https://docs.vllm.ai) (`vllm serve`, puerto 8000) | gratis, requiere GPU |
| Local | `gpt4all` | [GPT4All](https://gpt4all.io) con el *API Server* activado (puerto 4891) | gratis |
| Local | `koboldcpp` | [KoboldCpp](https://github.com/LostRuins/koboldcpp) (puerto 5001) | gratis |
| Local | `local` | cualquier otro servidor compatible con OpenAI: indica `FISCOLITA_BASE_URL` | gratis |

Con los motores de API, los locales y `claude`, la agente usa sus herramientas (búsqueda, lectura de documentos, simuladores, calendario, consultas en vivo). Con `codex` y `gemini-cli`, el bot busca primero en la base local y le pasa los documentos al modelo. En los motores locales conviene un modelo que soporte herramientas (*tool calling*), como las familias Qwen, Llama 3.1+ o Mistral recientes. Si el servidor usa otro puerto o está en otro equipo, cámbialo con `FISCOLITA_BASE_URL`.

Además: Python 3.10+, una cuenta de Telegram y **un equipo encendido 24/7** (computador dedicado o VPS).

## Paso 1 · Crear el bot con BotFather

1. En Telegram, busca **@BotFather** (tiene el check azul de verificado) y ábrelo.
2. Envía `/newbot`.
3. Escribe el **nombre visible** del bot, por ejemplo `FiscolItA`.
4. Escribe el **usuario** del bot. Debe terminar en `bot`, por ejemplo `mi_fiscolita_bot`.
5. BotFather responde con el **token**, algo como `7123456789:AAH...`. Cópialo: es la clave del bot, no la compartas.
6. Opcional, con el mismo BotFather:
   - `/setdescription` → "Asesora tributaria de IA experta en el SII de Chile".
   - `/setuserpic` → sube `assets/mascota.png` (la mascota de la agente).
   - Los comandos (`/bhe`, `/calendario`, `/alertas`…) los registra el bot solo al arrancar.

Si el token se filtra: en BotFather `/revoke`, elige el bot y reemplaza el token en `.env`.

## Paso 2 · Variables en `.env`

En la raíz del repositorio:

```bash
cp .env.example .env
```

Abre `.env` y completa:

| Variable | Valor |
|---|---|
| `TELEGRAM_BOT_TOKEN` | el token del paso 1 |
| `TELEGRAM_ALLOWED_USERS` | tu ID de Telegram (ver paso 4); varios separados por coma |
| `FISCOLITA_BACKEND` | suscripción: `claude`, `codex` · CLI: `gemini-cli` · API: `anthropic`, `openai`, `gemini`, `openrouter` · local: `ollama`, `lmstudio`, `llamacpp`, `jan`, `localai`, `vllm`, `gpt4all`, `koboldcpp`, `local` |
| `FISCOLITA_BASE_URL` | opcional: otra dirección para el servidor local o compatible con OpenAI |
| `FISCOLITA_MODEL` | modelo del proveedor; obligatorio en `openai`, `gemini`, `openrouter`, `ollama`, `jan`, `localai`, `vllm` y `gpt4all` (con `anthropic` el defecto es `claude-opus-5-5`) |
| `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GEMINI_API_KEY` / `OPENROUTER_API_KEY` | solo la del motor que uses |
| `FISCOLITA_EFFORT` | solo `anthropic`: `low`, `medium` (defecto) o `high` |
| `FISCOLITA_HORA_AVISOS` | hora de las alertas diarias, defecto `08:30` (hora de Chile) |
| `OPENAI_API_KEY` o `GROQ_API_KEY` | opcional, para transcribir notas de voz (o instala `whisper` local) |

`.env` está en `.gitignore`: nunca se sube a GitHub. No pegues el token ni la API key en el chat ni en otros archivos.

## Paso 3 · Instalar dependencias y ejecutar

Con `uv` (recomendado, no ensucia tu Python):

```bash
uv run --python 3.12 --with-requirements telegram/requirements.txt python telegram/bot.py
```

Con `pip` y un entorno virtual:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r telegram/requirements.txt
python telegram/bot.py
```

Si todo está bien verás: `@mi_fiscolita_bot en línea · backend=api · …`

## Paso 4 · Autorizarte y conversar

1. Abre tu bot en Telegram (`t.me/mi_fiscolita_bot`) y envía `/id`.
2. Copia el número que responde en `TELEGRAM_ALLOWED_USERS` del `.env` y reinicia el bot (Ctrl+C y ejecutar de nuevo).
3. Envía `/start` y pregunta, por ejemplo:
   - *¿Qué código del F29 es la base imponible del PPM?*
   - *¿Cuál fue la última circular?*
   - `15` → convierte 15 UF, USD, EUR y UTM a pesos.

Sin tu ID en la lista, el bot rechaza a cualquiera: así nadie más gasta tu API ni tu suscripción.

## Qué puedes hacer en el chat

| Acción | Ejemplo |
|---|---|
| Preguntar | *¿Cómo postergo el IVA?* |
| Enviar foto o PDF | factura, notificación o carta del SII → qué es, qué te piden, plazo y qué hacer |
| Nota de voz | pregunta hablando; responde por escrito |
| Monto solo | `15` → UF, USD, EUR y UTM en pesos |

## Comandos

| Comando | Acción |
|---|---|
| `/bhe 1000000` | retención de boleta de honorarios desde el bruto |
| `/liquido 850000` | cuánto boletear para recibir ese líquido |
| `/ppm 10000000 1,1` | PPM: ingresos netos del mes y tasa % |
| `/iva 5000000 2000000` | IVA: ventas netas y compras netas |
| `/multa 500000 7` | multa (art. 97 N° 2) e interés penal por meses de atraso |
| `/sueldo 2500000` | impuesto único de 2ª categoría |
| `/calendario` | próximos vencimientos (`/calendario 90` para 90 días) |
| `/novedades` | normas nuevas del SII de hoy |
| `/alertas` | cada mañana: vencimientos (3 días antes, el día anterior y el mismo día) y normas nuevas · `/alertas off` para dejar |
| `/contador` | resumen de tu caso listo para reenviar a tu contador |
| `/nuevo` | olvida la conversación y empieza otra |
| `/id` · `/ayuda` | tu ID de Telegram · ayuda |

Los simuladores son referenciales: la multa no incluye el reajuste IPC y el interés usa la tasa del semestre vigente (resolución SII de tasas de interés por mora).

## Dejarlo siempre encendido

- **macOS**: `launchd` con un `.plist` que ejecute el comando del paso 3, o simplemente `caffeinate -i` + la terminal abierta.
- **Linux/servidor**: un servicio `systemd` con `WorkingDirectory=` en la carpeta del repo.
- Los motores de suscripción (`claude`, `codex`) necesitan la sesión iniciada en ese mismo equipo; `gemini-cli`, su `GEMINI_API_KEY`.
- Las alertas salen a la hora configurada solo si el bot está encendido.

## Cómo funciona

- **Motores con herramientas** (API y locales): el bot llama al modelo con herramientas locales (`buscar`, `leer_documento`, `ultimas_normas`, `valor_indicador`, `pagina_sii`, `calculadora`, `simulador`, `calendario`). El modelo decide qué buscar, lee los documentos y responde citando la fuente. Las conversaciones se guardan solo en memoria (se pierden al reiniciar el bot).
- **`claude`**: el bot ejecuta `claude -p` dentro del repo, que carga `CLAUDE.md`/`AGENTS.md`. Solo se permiten los scripts de la agente, lectura de archivos y WebFetch a `www.sii.cl`.
- **`codex` y `gemini-cli`**: el bot busca en la base local, arma el contexto (resultados, documentos y calculadora) y se lo pasa al CLI. Las fotos no se leen en este modo; los PDF sí (se convierten a texto).
- La primera consulta del día revisa las normas nuevas del SII y las agrega a la base. Las alertas usan ese mismo registro (`config/actualizacion.json`) y el calendario (`calendario.py`). Los suscritos quedan en `config/telegram.json` (no se versiona).
- Fotos y audios se guardan temporalmente en `config/tmp/` (no se versiona).
- El bot **no** usa las herramientas con credenciales del SII (`sii_login`, `sii_consultar`): por Telegram nunca se manejan claves.
