# Contexto (lo que sé)

Mi conocimiento es **solo información pública oficial**. No incluye datos de ningún usuario.

## Fuentes

| Fuente | Qué contiene | Dónde |
|---|---|---|
| www.sii.cl | sitio completo: ayudas, servicios online, destacados, factura electrónica, declaraciones juradas, valores y fechas | `docs/` (misma ruta que el sitio) |
| Circulares SII | 1981–2026 | `docs/documentos/circulares/`, `docs/normativa_legislacion/circulares/` |
| Resoluciones SII | 1978–2026, más resoluciones regionales 2026 | `docs/documentos/resoluciones/`, `docs/normativa_legislacion/resoluciones/`, `docs/documentos/normativa_ddrr/` |
| Jurisprudencia administrativa | oficios 1998–2026 (Renta, IVA, otras normas) | `docs/jurisprudencia_api/`, `docs/pagina/jurisprudencia/` |
| Preguntas frecuentes | 3.344 preguntas en 26 temáticas | `docs/preguntas_frecuentes/` |
| Leyes vigentes (BCN LeyChile) | Renta (DL 824), IVA (DL 825), Código Tributario (DL 830), Timbres (DL 3475), Impuesto Territorial, Herencias | `docs/leyes_vigentes/` |
| Catálogos | circulares, resoluciones, oficios, FAQ, aplicaciones y trámites | `docs/_catalogos/` |

Total: ~29.700 documentos. Mapa completo en `INDICE.md`.

## Vigencia

- La base es una foto al **20-11-2026**.
- Lo que depende de la fecha (última circular, UTM/UF de hoy, cambios recientes) lo confirmo **en vivo** en sii.cl.
- Una circular puede estar "dejada sin efecto" o "modificada": lo indican los catálogos.

## Jerarquía de fuentes

1. Ley vigente
2. Circular más reciente
3. Resolución
4. Oficio (jurisprudencia administrativa)
5. Preguntas frecuentes y ayudas

## Fuera de mi conocimiento

- Aplicaciones con login del SII (declarar, consultar tu situación): solo si el usuario conecta su cuenta (ver `HERRAMIENTAS.md`).
- Resoluciones regionales 2001–2025, sección `/transparencia/` del SII, videos y software.
- Jurisprudencia de tribunales (TTA, Cortes) más allá de lo publicado en sii.cl.
