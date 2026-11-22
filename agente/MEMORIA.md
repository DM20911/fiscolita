# Memoria (lo que recuerdo del usuario)

El **contexto** (`CONTEXTO.md`) es conocimiento público y es igual para todos. La **memoria** es de cada instalación: vive en `memoria/` y en `config/`, que **no se suben al repositorio** (`.gitignore`).

## Archivos

| Archivo | Qué guarda | Quién lo escribe |
|---|---|---|
| `config/identidad.json` | nombre, modo (agente/subagente), agente principal, fecha de instalación | `instalar.py` |
| `config/indicadores.json` | caché de UF/USD/EUR/UTM (1 hora) | `calculadora.py` |
| `memoria/contribuyente.md` | perfil tributario: tipo de contribuyente, régimen (14 D Pro Pyme, general…), giro, si emite BHE/facturas, periodicidad de F29 | el agente, con permiso del usuario |
| `memoria/preferencias.md` | cómo quiere las respuestas (largo, formato, nivel técnico) | el agente |
| `memoria/aprendizajes.md` | respuestas validadas por el usuario o su contador, aclaraciones de casos propios | el agente |

## Reglas de memoria

1. **Leer** `memoria/` al inicio de cada conversación para contextualizar (ej. si es Pro Pyme, responder para ese régimen).
2. **Preguntar antes de guardar** datos del contribuyente. Nunca guardar: claves, RUT completos de terceros, números de cuenta, certificados digitales.
3. **Un dato por línea**, con fecha: `- 2026-11-20: Régimen 14 D N°3 (Pro Pyme General).`
4. Si un dato cambia, actualizar la línea (no duplicar). Si el usuario pide olvidar, borrar.
5. La memoria **no reemplaza** la fuente oficial: si un aprendizaje choca con una norma más reciente, manda la norma y se avisa.
6. En modo **subagente**, el agente principal puede tener su propia memoria; esta es solo la tributaria.
