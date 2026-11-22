# Índice — Fiscol**I**t**A** (base de conocimiento SII)

Extracción completa del sitio público **www.sii.cl** + jurisprudencia administrativa (API pública del SII) + texto vigente de las leyes tributarias (BCN LeyChile).
Fecha de extracción: **20-11-2026**. 29.699 documentos indexados · 3,6 GB originales · 377 MB en Markdown.

## Cómo consultar

```
python3 buscar.py "boleta honorarios retención"          # búsqueda general
python3 buscar.py "crédito IVA exportador" -c jurisprudencia
python3 buscar.py '"impuesto único" tabla' -c circular -n 30
```

O abrir tu agente de IA en esta carpeta y preguntar directamente; `AGENTS.md` le indica cómo responder usando esta base.

## Contenido por tipo

| Tipo | Docs | Dónde | Catálogo |
|---|---:|---|---|
| Leyes vigentes (LIR DL 824, IVA DL 825, Código Tributario DL 830, Timbres DL 3475, Impuesto Territorial, Herencias) | 6 | `docs/leyes_vigentes/` | — |
| Circulares (1981–2026) | 3.727 | `docs/documentos/circulares/`, `docs/normativa_legislacion/circulares/` | [circulares.md](docs/_catalogos/circulares.md) |
| Resoluciones SII (1978–2026) | 6.850 | `docs/documentos/resoluciones/`, `docs/normativa_legislacion/resoluciones/` | [resoluciones.md](docs/_catalogos/resoluciones.md) |
| Resoluciones de Direcciones Regionales (solo 2026) | 2.776 | `docs/documentos/normativa_ddrr/` | — |
| Jurisprudencia administrativa: oficios 2019–2026 (Renta, IVA, Otras) | 3.068 | `docs/jurisprudencia_api/` | [jurisprudencia_oficios.md](docs/_catalogos/jurisprudencia_oficios.md) |
| Jurisprudencia administrativa anterior (1998–2018) | ~6.600 | `docs/pagina/jurisprudencia/`, `docs/normativa_legislacion/jurisprudencia_administrativa/` | — |
| Preguntas frecuentes (26 temáticas) | 3.344 | `docs/preguntas_frecuentes/` | [preguntas_frecuentes.md](docs/_catalogos/preguntas_frecuentes.md) |
| Declaraciones juradas (instrucciones, formatos, suplementos) | 839 | `docs/declaraciones_juradas/` | — |
| Destacados / portales temáticos (Renta, BHE, IVA, Bienes Raíces, Pymes…) | 534 | `docs/destacados/`, `docs/portales/`, `docs/renta/` | — |
| Servicios online (menús: qué trámite está dónde) | 213 | `docs/servicios_online/` | [aplicaciones_y_tramites.md](docs/_catalogos/aplicaciones_y_tramites.md) |
| Ayudas y guías paso a paso | 158 | `docs/ayudas/` | — |
| Factura electrónica (manuales técnicos, formatos XML, webservices) | 155 | `docs/factura_electronica/` | — |
| Valores y fechas (UF, UTM, dólar, IPC, impuesto 2ª categoría, corrección monetaria, vida útil, petróleo, MEPCO) | 74 | `docs/valores_y_fechas/` | — |
| Sobre el SII, estadísticas, cuenta pública, aprenda sobre impuestos | ~500 | `docs/sobre_el_sii/`, `docs/estadisticas/`, `docs/aprenda_sobre_impuestos/` | — |
| Normativa general (índices, convenios doble tributación, tribunales) | 80 | `docs/normativa_legislacion/` | — |

## Puntos de entrada útiles

- Preguntas frecuentes: `docs/preguntas_frecuentes/preguntasfrecuentes.htm.md` y `otros.html.md` (todas las temáticas).
  Temáticas: acuerdos/pagos (acuerdos_ant_pt), avalúos y contribuciones, beneficios tributarios, boleta electrónica de ventas, boletas de honorarios electrónicas, catastro, clave tributaria, criptomonedas, declaraciones juradas, declaración de renta, factura electrónica, herencias, impuestos mensuales (F29), infracciones/giros/condonaciones, IVA servicios profesionales, libros contables electrónicos, otros impuestos, peticiones administrativas, preguntas generales, RUT e inicio de actividades, situación tributaria, actualización de información, tasación fiscal de vehículos.
- Legislación: `docs/normativa_legislacion/legislacion_tributaria_basica.html.md`, `..._complementaria.html.md`, `convenios_internacionales.html.md`.
- Valores del año: `docs/valores_y_fechas/utm/utm2026.htm.md`, `uf/uf2026.htm.md`, `dolar/dolar2026.htm.md`, `impuesto_2da_categoria/`.
- Calendario/vencimientos y reajustes: `docs/valores_y_fechas/porcentaje_de_reajuste.html.md`, `reajuste_declaracion_renta.html.md`.
- Boletas de honorarios 2026 (retención 15,25%): `docs/destacados/boletas_honorarios/`.

## Cómo funciona el SII (mapa del sitio)

- **www.sii.cl** — sitio informativo estático (todo lo descargado aquí).
- **Aplicaciones con autenticación** (RUT + clave tributaria o Clave Única), no descargadas, listadas en [aplicaciones_y_tramites.md](docs/_catalogos/aplicaciones_y_tramites.md) con 510 destinos:
  - `www4.sii.cl` — consultas y declaraciones (F29/F50 `rfiInternet`, propuesta y estado F22, BHE directores, certificados, impuesto a vehículos, aseo, DDJJ consulta…).
  - `www2.sii.cl` — apps nuevas (carpeta tributaria, inicio de actividades, mi reavalúo, asistentes de renta/arriendo/bienes raíces, calculadoras, obtener/recuperar clave).
  - `palena.sii.cl` / `maullin.sii.cl` — facturación electrónica (producción / certificación).
  - `zeus.sii.cl` / `zeusr.sii.cl` / `misiir.sii.cl` — autenticación y Mi SII.
  - `loa.sii.cl`, `alerce.sii.cl` — BHE, declaraciones juradas (upload, software).
  - `www3.sii.cl` — devoluciones, pagos a proveedores, normativa (`normaInternet`).
  - `eboleta.sii.cl`, `homer.sii.cl`, `capacita.sii.cl`, `api.sii.cl`, `apicert.sii.cl`.

## Exclusiones

- ~71 mil PDFs de resoluciones de Direcciones Regionales 2001–2025 (casos individuales) — descargables a pedido.
- Sección `/transparencia/` (personal, remuneraciones) — excluida.
- Videos, imágenes, ZIP/EXE de software, 8 archivos > 40 MB, 96 Excel binarios con macros (.xlsb, no convertidos).
- Área autenticada — solo vía MCP con credenciales del usuario (ver `agente/HERRAMIENTAS.md`).

## Estructura

Ver [README.md](README.md#cómo-está-organizado). Identidad, contexto, memoria y reglas del agente en [`agente/`](agente/).
