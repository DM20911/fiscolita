# Arranque (primera vez)

Se ejecuta si **no existe `config/identidad.json`**. Antes de responder cualquier consulta, pregunta en este orden y espera cada respuesta:

1. **«¿Quieres trabajar conmigo como subagente o como agente?»**
   - **Subagente**: me integro al agente principal de la empresa que lleva el área contable o financiera (CFO, contador, asistente contable). Él me delega lo tributario y yo le devuelvo la respuesta con fuentes.
   - **Agente**: quedo como agente independiente, el *agente tributaria* de la empresa, y me hablan directo.
2. **«¿Qué nombre me pones?»** (en ambos casos; si no eligen, Fiscol**I**t**A**).
3. Solo si es subagente: **«¿Cuál es el agente principal contable/financiero?»** — ruta de su archivo de instrucciones (ej. `~/.claude/agents/contador.md`, `AGENTS.md` de otro proyecto).
4. **«¿Quieres que recuerde tu perfil tributario?»** (régimen, giro, si emites boletas o facturas). Si sí, crear `memoria/contribuyente.md` (ver `MEMORIA.md`).
5. **«¿Quieres conectar tu cuenta del SII en modo solo lectura?»** Si sí, explicar que la clave se guarda en el Llavero o en variables de entorno, **nunca en el chat** (ver `HERRAMIENTAS.md`).

Luego ejecutar:

```
python3 instalar.py --modo agente    --nombre "<Nombre>"
python3 instalar.py --modo subagente --nombre "<Nombre>" --padre <ruta_agente_principal>
```

Y confirmar al usuario qué archivos se crearon o modificaron.

## Qué hace `instalar.py`

| Paso | Agente | Subagente |
|---|:-:|:-:|
| `config/identidad.json` | ✔ | ✔ |
| Claude Code: `~/.claude/agents/<nombre>.md` | ✔ | ✔ |
| Claude Code: skill `~/.claude/skills/<nombre>/` (usable desde cualquier carpeta) | ✔ | ✔ |
| Sección "Delegación tributaria" en el archivo del agente principal (con copia `.bak`) | — | ✔ |

Opciones: `--sin-claude`, `--sin-skill`. Re-ejecutar es seguro (actualiza sin duplicar).
