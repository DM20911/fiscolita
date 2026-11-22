# Herramientas

| Herramienta | Para qué | Ejemplo |
|---|---|---|
| `buscar.py` | búsqueda de texto completo en ~29.700 documentos | `python3 buscar.py "postergación IVA" -c faq` |
| `en_vivo.py` | datos del día en sii.cl | `python3 en_vivo.py circulares -n 3` |
| `calculadora.py` | UF / USD / EUR / UTM → pesos del día | `python3 calculadora.py "1.500,5"` |
| `actualizar_novedades.py` | 1 vez al día, automático: agrega circulares, resoluciones y oficios nuevos del SII | `python3 actualizar_novedades.py --forzar` |
| `simuladores.py` | BHE, bruto para un líquido, PPM, IVA, multa + interés por atraso, impuesto único de un sueldo | `python3 simuladores.py multa 500000 7` |
| `calendario.py` | próximos vencimientos (F29/F50, F22, contribuciones, DJ, UF) | `python3 calendario.py --dias 60` |
| `telegram/bot.py` | bot de Telegram (suscripción Claude/ChatGPT/Gemini, API o Ollama local) con alertas, fotos, PDF y voz | ver `telegram/README.md` |
| `construir_indice.py` | crea `busqueda.sqlite` desde `docs/` (automático la primera vez) | `python3 construir_indice.py` |
| `instalar.py` | registra el agente (ver `ARRANQUE.md`) | `python3 instalar.py --modo agente --nombre FiscolItA` |
| `mcp_sii/server.py` | servidor MCP con todo lo anterior | ver abajo |
| `_tools/` | regenerar la base desde sii.cl | ver `README.md` |

Categorías de `buscar.py -c`: `ley`, `faq`, `circular`, `resolucion`, `jurisprudencia`, `normativa`, `valores`, `servicios_online`, `ayuda`, `destacado`, `noticia`, `factura_electronica`, `declaraciones_juradas`, `sobre_el_sii`, `portal`, `formulario`, `resolucion_regional`, `otros`.

## MCP `asesor-tributario-sii`

| Tool | Descripción |
|---|---|
| `buscar` | búsqueda en la base local |
| `leer_documento` | lee un `.md` de `docs/` por partes |
| `ultimas_normas` | últimas circulares, resoluciones u oficios (en vivo) |
| `valor_indicador` | tabla anual de UTM, UF o dólar (en vivo) |
| `pagina_sii` | cualquier página o PDF público de www.sii.cl |
| `calculadora` | UF / USD / EUR / UTM → pesos |
| `simulador` | BHE, PPM, IVA, multas, impuesto de un sueldo |
| `calendario` | próximos vencimientos |
| `sii_login` | inicia sesión en la cuenta SII del usuario |
| `sii_consultar` | lee páginas de la cuenta (solo GET) |

El SII **no tiene MCP oficial**: la conexión a la cuenta es scraping con las credenciales del propio usuario, **solo lectura**. Bloquea URLs de declarar, rectificar, anular, pagar, firmar o timbrar.

### Credenciales (opcional)

- macOS: el usuario ejecuta en su terminal `security add-generic-password -s asesor-sii -a 12345678-9 -w` (la clave se pide oculta).
- Linux / Windows / contenedores: variables `ASESOR_SII_RUT` y `ASESOR_SII_CLAVE` en el entorno del servidor MCP.
- Nunca por chat. Usar solo con cuenta propia o autorización del titular.
