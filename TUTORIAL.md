# Tutorial paso a paso · Fiscol**I**t**A** para personas no técnicas

Esta guía es para ti si nunca has usado una "terminal" ni instalado programas desde internet más allá de lo habitual. Vamos lento y en orden. Calcula entre **30 y 45 minutos** la primera vez; después, abrirla toma segundos.

Si en algún paso algo no te sale igual, revisa la sección [Problemas frecuentes](#problemas-frecuentes) al final.

**Aviso antes de empezar:** si vas a usar Fiscol**I**t**A** por Telegram, el computador o servidor donde la instales **tiene que estar encendido y conectado a internet todo el tiempo** que quieras que responda. Lee el detalle en el [Paso 7](#paso-7--opcional-tenerla-en-telegram-celular).

---

## Antes de empezar: qué vas a necesitar

| Necesitas | Por qué |
|---|---|
| Un computador **Mac** o **Windows** | Fiscol**I**t**A** vive en tu computador |
| Conexión a internet | Para descargar y para consultar el SII en vivo |
| **Una inteligencia artificial** (ver [Paso 5](#paso-5--elige-tu-inteligencia-artificial)) | Fiscol**I**t**A** es el "conocimiento"; la IA es el "cerebro" que conversa. Sin una, no puede responder |
| Opcional: Telegram en el celular | Si quieres hablarle desde el teléfono |

**Palabras que vas a leer** (no te asustes):

- **Terminal**: una ventana donde escribes instrucciones en vez de hacer clic. Solo vas a copiar y pegar.
- **Comando**: cada línea que copias y pegas en la terminal, y luego presionas **Enter**.
- **Carpeta del proyecto**: la carpeta `fiscolita` que vas a descargar.

---

## Paso 1 · Descargar Fiscol**I**t**A**

1. Entra a la página del proyecto en GitHub: **https://github.com/DM20911/fiscolita**
   (si te pide iniciar sesión, es porque necesitas una invitación; pídela a OptimizarIA).
2. Haz clic en el botón verde **`<> Code`**.
3. Elige **Download ZIP**. La descarga pesa varios cientos de MB porque trae los ~29.700 documentos del SII: ten paciencia.
4. Cuando termine, ve a tu carpeta **Descargas** y haz doble clic en el archivo `.zip` para descomprimirlo.
5. Te quedará una carpeta llamada `fiscolita-main`. **Cámbiale el nombre a `fiscolita`** y muévela a un lugar fácil, por ejemplo tu carpeta de usuario o **Documentos**.

✅ Listo cuando: tienes una carpeta `fiscolita` y dentro ves archivos como `README.md`, `buscar.py` y una carpeta `docs`.

---

## Paso 2 · Instalar Python

Python es el programa que hace funcionar las herramientas de Fiscol**I**t**A** (buscador, calculadora, simuladores). Es gratis y seguro.

### En Mac

1. Entra a **https://www.python.org/downloads/** y presiona el botón amarillo **Download Python 3.x**.
2. Abre el archivo descargado (`.pkg`) y sigue el instalador: **Continuar → Continuar → Aceptar → Instalar**. Te pedirá la clave de tu Mac.
3. Al terminar se abre una carpeta de Python: haz doble clic en **Install Certificates.command** (deja que termine y cierra esa ventana).

### En Windows

1. Entra a **https://www.python.org/downloads/** y presiona **Download Python 3.x**.
2. Abre el instalador. **MUY IMPORTANTE: antes de nada, marca la casilla de abajo que dice _"Add python.exe to PATH"_.**
3. Presiona **Install Now** y espera. Al final, si aparece **"Disable path length limit"**, presiónalo también.

✅ Listo cuando: el instalador dice *"Setup was successful"* / *"La instalación se completó correctamente"*.

---

## Paso 3 · Abrir la terminal dentro de la carpeta

Todos los comandos de este tutorial se escriben **en una terminal abierta dentro de la carpeta `fiscolita`**.

### En Mac

1. Presiona **⌘ Cmd + Espacio**, escribe **Terminal** y presiona **Enter**.
2. En la ventana que aparece escribe `cd` seguido de **un espacio** (no presiones Enter todavía).
3. Arrastra la carpeta `fiscolita` desde el Finder y suéltala sobre la ventana de la terminal: se escribirá su ubicación sola.
4. Ahora sí, presiona **Enter**.

### En Windows

1. Abre la carpeta `fiscolita` en el Explorador de archivos.
2. Haz clic en la **barra de dirección** de arriba (donde aparece la ruta de la carpeta), borra lo que dice, escribe **`cmd`** y presiona **Enter**.
3. Se abre una ventana negra ya ubicada en la carpeta.

✅ Para comprobarlo, escribe este comando y presiona Enter:

| Mac | Windows |
|---|---|
| `python3 --version` | `py --version` |

Debe responder algo como `Python 3.13.1`. Si dice que no lo encuentra, vuelve al Paso 2 (en Windows, reinstala marcando *"Add python.exe to PATH"*).

**Desde aquí, cuando veas dos comandos, usa la columna de tu sistema.** En Mac se escribe `python3`; en Windows, `py`.

---

## Paso 4 · Instalar las piezas que usa Fiscol**I**t**A**

Copia y pega este comando en la terminal y presiona **Enter**:

| Mac | Windows |
|---|---|
| `python3 -m pip install -r telegram/requirements.txt` | `py -m pip install -r telegram\requirements.txt` |

Verás muchas líneas pasar. Espera hasta que vuelva a aparecer el cursor y diga algo como *"Successfully installed…"*.

Ahora prueba que el buscador funciona (la primera vez demora **1 a 2 minutos** porque arma su índice):

| Mac | Windows |
|---|---|
| `python3 buscar.py "boleta de honorarios"` | `py buscar.py "boleta de honorarios"` |

✅ Listo cuando: aparece una lista de documentos del SII sobre boletas de honorarios.

---

## Paso 5 · Elige tu inteligencia artificial

Fiscol**I**t**A** necesita **una** de estas opciones. Elige la que te acomode:

| Opción | Qué es | Costo | Recomendada si… |
|---|---|---|---|
| **A. Claude Pro o Max** | Suscripción de Anthropic (claude.ai) | la que ya pagas (desde US$20/mes) | quieres lo más simple y completo ⭐ |
| **B. ChatGPT Plus o Pro** | Suscripción de OpenAI | la que ya pagas | ya pagas ChatGPT |
| **C. LM Studio (local)** | Un programa que corre una IA dentro de tu computador | **gratis** | no quieres pagar y tu computador es reciente (16 GB de RAM ideal) |
| **D. Una "API key"** | Clave de pago por uso (Anthropic, OpenAI, Google, OpenRouter) | pagas solo lo que usas | sabes o alguien te ayudó a crear una |

Si no sabes cuál, elige **A** si tienes Claude pagado, o **C** si quieres probar gratis.

---

## Paso 6 · Conversar con Fiscol**I**t**A** en tu computador

### Con la opción A (Claude Pro o Max) — la más fácil

1. Instala **Claude Code** copiando este comando en la terminal:

   | Mac | Windows (usa **PowerShell**: menú Inicio → escribe *PowerShell* → Enter) |
   |---|---|
   | `curl -fsSL https://claude.ai/install.sh \| bash` | `irm https://claude.ai/install.ps1 \| iex` |

2. **Cierra la terminal y ábrela de nuevo dentro de la carpeta** `fiscolita` (repite el [Paso 3](#paso-3--abrir-la-terminal-dentro-de-la-carpeta)).
3. Escribe `claude` y presiona **Enter**.
4. La primera vez te pedirá iniciar sesión: elige **"Claude account with subscription"**, se abrirá el navegador, entra con tu cuenta de Claude y autoriza. Vuelve a la terminal.
5. Si te pregunta si confías en la carpeta, responde que **sí** (*"Yes, proceed"*).
6. Escribe tu primera pregunta, por ejemplo: **`hola`**.

La primera vez Fiscol**I**t**A** te hará unas preguntas para configurarse. Si no sabes qué responder:

| Te pregunta | Responde |
|---|---|
| ¿Agente o subagente? | **agente** (subagente es solo si tu empresa ya tiene otro agente de IA contable) |
| ¿Qué nombre me pones? | **Fiscolita** o el que quieras |
| ¿Recuerdo tu perfil tributario? | **sí**, y cuéntale por ejemplo "emito boletas de honorarios" o "soy Pro Pyme" |
| ¿Conectar tu cuenta del SII? | **no** por ahora |

Después pregunta lo que quieras, con tus palabras:

- *¿Cuánto me retienen en una boleta de honorarios de 800 mil?*
- *¿Cuándo vence el F29 este mes?*
- *Me llegó una notificación del SII, ¿qué hago?*
- *¿Cuánto son 15 UF en pesos?*

Para salir escribe `/exit`. Para volver otro día: abre la terminal en la carpeta (Paso 3) y escribe `claude`.

### Con la opción B (ChatGPT Plus o Pro)

1. Instala **Node.js** desde **https://nodejs.org** (botón *LTS*, instalador normal: siguiente, siguiente…).
2. Cierra y abre la terminal en la carpeta `fiscolita` y escribe:
   `npm install -g @openai/codex`
3. Escribe `codex`, elige **Sign in with ChatGPT** e inicia sesión en el navegador.
4. Pregunta igual que en la opción A.

### Con la opción C (gratis, LM Studio) o D (API key)

Estas opciones funcionan a través del **bot de Telegram** (Paso 7), que es además la forma más cómoda de usar Fiscol**I**t**A** desde el celular.

---

## Paso 7 · Opcional: tenerla en Telegram (celular)

Así le escribes desde el teléfono como a cualquier contacto.

### ⚠️ Importante: el computador debe estar encendido todo el tiempo

El bot **no vive en Telegram ni en internet: vive en tu computador** (o en un servidor/VPS). Telegram solo le lleva los mensajes. Por eso:

- **Si el computador se apaga, se suspende, se le cierra la tapa o pierde internet, el bot deja de responder.** Los mensajes que le envíes en ese rato no se contestan.
- **Si cierras la ventana de la terminal donde corre el bot, también se apaga.**
- **Las alertas de la mañana (`/alertas`) solo llegan si el bot está encendido a esa hora.**
- Si lo usará más de una persona (por ejemplo, tu equipo o tu contador), avísales de esto. Lo recomendable es dejarlo en un **computador que no se apague** o en un **servidor (VPS)**, que es un computador en internet encendido las 24 horas.

En Mac, para que no se suspenda mientras el bot corre: **Configuración del Sistema → Batería (o Pantalla de bloqueo) → evitar que el Mac entre en reposo**, o escribe `caffeinate -i python3 telegram/bot.py` en vez del comando del paso 7.4. En Windows: **Configuración → Sistema → Inicio/apagado y suspensión → Suspender: Nunca**.


### 7.1 Crear tu bot (5 minutos, desde el celular)

1. En Telegram, busca **@BotFather** (tiene un check azul ✔️) y ábrelo.
2. Presiona **Iniciar** y luego escribe `/newbot`.
3. Te pide un **nombre**: escribe por ejemplo `Mi FiscolItA`.
4. Te pide un **usuario**: debe terminar en `bot`, por ejemplo `fiscolita_de_ana_bot` (si está ocupado, prueba otro).
5. BotFather te entrega un **token**: una línea larga tipo `7123456789:AAH-xxxxxxxx`. **Es como la llave de tu bot: no la compartas con nadie.** Cópiala (mantén presionado → copiar) y mándatela a ti mismo por un medio privado para tenerla en el computador.

### 7.2 Si elegiste la opción C: preparar LM Studio

1. Descarga **LM Studio** desde **https://lmstudio.ai** e instálalo como cualquier programa.
2. Ábrelo y en la lupa (**Discover**) busca **Qwen3** (o *Llama 3.1*). Descarga uno que diga que es compatible con herramientas (*Tool use*) y que quepa en tu computador (LM Studio te avisa si es muy grande).
3. Ve a la pestaña **Developer** (o *Server*), carga el modelo y activa **Start Server**. Debe decir que está corriendo en el puerto **1234**.
4. Deja LM Studio abierto.

### 7.3 Escribir tu configuración (archivo `.env`)

1. En la terminal, dentro de la carpeta `fiscolita`, escribe:

   | Mac | Windows |
   |---|---|
   | `cp .env.example .env` y luego `open -e .env` | `copy .env.example .env` y luego `notepad .env` |

2. Se abre un archivo de texto. Completa **solo** estas líneas (lo que va después del `=`, sin espacios ni comillas):

   ```
   TELEGRAM_BOT_TOKEN=pega-aquí-el-token-de-BotFather
   FISCOLITA_BACKEND=claude
   ```

   En `FISCOLITA_BACKEND` pon según tu opción:

   | Tu opción | Escribe |
   |---|---|
   | A. Claude Pro o Max | `claude` |
   | B. ChatGPT Plus o Pro | `codex` |
   | C. LM Studio | `lmstudio` |
   | D. API key de Anthropic | `anthropic` y pega tu clave en `ANTHROPIC_API_KEY=` |
   | D. API key de OpenAI | `openai`, tu clave en `OPENAI_API_KEY=` y el modelo en `FISCOLITA_MODEL=` |

3. **Guarda** (⌘ Cmd + S en Mac, Ctrl + G o Ctrl + S en Windows) y cierra.

**Ojo:** este archivo guarda tus claves **solo en tu computador**. Nunca lo envíes por correo ni lo subas a internet.

### 7.4 Encender el bot

En la terminal, dentro de la carpeta:

| Mac | Windows |
|---|---|
| `python3 telegram/bot.py` | `py telegram\bot.py` |

Si todo está bien verás algo como: **`@fiscolita_de_ana_bot en línea`**. **No cierres esa ventana**: mientras esté abierta, el bot funciona.

### 7.5 Autorizarte (para que nadie más use tu bot)

1. En Telegram busca tu bot por su usuario (ej. `@fiscolita_de_ana_bot`), ábrelo y escribe `/id`.
2. Te responde con un **número**. Cópialo.
3. En la terminal presiona **Ctrl + C** para apagar el bot.
4. Abre de nuevo el `.env` (como en 7.3) y pega ese número en: `TELEGRAM_ALLOWED_USERS=123456789`. Guarda.
5. Enciende el bot otra vez (7.4).
6. En Telegram escribe `/start` y pregúntale lo que quieras. 🎉

**Cosas útiles en Telegram:**

| Escribe | Qué hace |
|---|---|
| Cualquier pregunta | te responde con la fuente oficial |
| Una **foto** o **PDF** de una carta del SII | te explica qué es, qué te piden y el plazo |
| Una **nota de voz** | la transcribe y responde (requiere configuración extra, ver `telegram/README.md`) |
| `15` | convierte 15 UF, dólares, euros y UTM a pesos |
| `/bhe 1000000` | calcula la retención de una boleta de honorarios |
| `/calendario` | próximos vencimientos |
| `/alertas` | te avisa cada mañana lo que vence pronto |
| `/contador` | arma un resumen de tu caso para enviárselo a tu contador |
| `/ayuda` | lista de todo |

### 7.6 Para usarlo otro día

1. Abre la terminal en la carpeta (Paso 3).
2. Si usas LM Studio, ábrelo y enciende el servidor (7.2, punto 3).
3. Enciende el bot (7.4).

Si quieres que quede encendido siempre, en `telegram/README.md` (sección *Dejarlo siempre encendido*) está cómo hacerlo; es un paso para alguien con algo de experiencia.

---

## Problemas frecuentes

| Lo que ves | Qué hacer |
|---|---|
| `command not found: python3` / *"py no se reconoce"* | Python no quedó instalado. Repite el Paso 2 (en Windows, marca *"Add python.exe to PATH"*) y abre una terminal nueva |
| `No such file or directory` al usar un comando | La terminal no está en la carpeta `fiscolita`. Repite el Paso 3 |
| `No module named …` | Falta el Paso 4. Ejecútalo de nuevo |
| `command not found: claude` | Cierra y abre la terminal después de instalar Claude Code. Si sigue, repite el paso de instalación |
| El bot dice *"No autorizado"* | Falta tu número en `TELEGRAM_ALLOWED_USERS` (Paso 7.5) o no reiniciaste el bot |
| El bot no contesta nada | El computador está apagado, suspendido o sin internet, o se cerró la ventana del bot. Enciéndelo y repite el Paso 7.4 |
| No llegaron las alertas de la mañana | El bot estaba apagado a esa hora. Debe quedar encendido toda la noche |
| Con LM Studio responde mal o no usa las herramientas | Usa un modelo compatible con herramientas (Qwen3, Llama 3.1+) y verifica que el servidor esté encendido en el puerto 1234 |
| `Unauthorized` o `401` | El token o la API key están mal copiados en `.env` (sin espacios ni comillas) |
| En Mac: `SSL: CERTIFICATE_VERIFY_FAILED` | Haz doble clic en **Install Certificates.command** (Paso 2, Mac, punto 3) |

¿Sigues con problemas? Escríbenos en **https://optimizaria.com**.

---

## Lo importante

- Fiscol**I**t**A** **orienta**: no es el SII, no hace trámites por ti y no reemplaza a tu contador. En casos importantes, valida con un profesional.
- Por Telegram, **el computador o servidor tiene que estar encendido todo el tiempo**; si se apaga, el bot no responde ni envía alertas.
- **Nunca** le escribas tu Clave Tributaria, tu Clave Única ni datos de tarjetas. No los necesita.
- Tus claves de Telegram y de la IA quedan solo en tu computador, en el archivo `.env`.

<p align="center"><sub>Proyecto potenciado por <a href="https://optimizaria.com"><b>optimizarIA</b></a> · simple, pero funcional.</sub></p>
