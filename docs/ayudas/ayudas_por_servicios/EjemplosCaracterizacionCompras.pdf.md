---
url: https://www.sii.cl/ayudas/ayudas_por_servicios/EjemplosCaracterizacionCompras.pdf
titulo: Registro de Compras.
categoria: ayuda
---
Registro de Compras.

Ejemplos de Caracterización de Tipo de
Compra de Documentos Tributarios
Electrónicos en Registro de Compras
01-07-2017 Versión 1.0

SDAC– Versión 1.0

Ejemplos Caracterización Tipo de Compra

Ejemplos de Caracterización de Tipo de Compra de
Documentos Tributarios Electrónicos en Registro de
Compras.
1. Facturas recibidas con Tipo de compra “Del Giro”, que deben cambiar a Tipo de compra
“Supermercados”
Contribuyente ha recibido factura por compras en Supermercado por artículos que corresponden al desarrollo de la actividad
económica y no son del giro, pero que por norma pueden ser aceptados como gasto, sin embargo al emitirse la Factura Electrónica
no fue caracterizada de esta forma, por lo cual se registró en forma automática como “Del Giro”, por lo cual el contribuyente receptor
debe cambiar el tipo de Compra a “Supermercados”.
Indicador Tipo de Compra en Supermercados o Comercios Similares = 2
(Se adjunta tabla con información de tipos de compra al final de este archivo)

La modificación sería la siguiente:
RUT del
Proveedor

Tipo de Documento

Folio del
Documento

Tipo de Transacción de
Compra

Código IVA no Recuperable

Concepto
Nombre Campo en
CSV
Valor del Campo

Rut-DV

Codigo_Tipo_Doc

Folio_Doc

TpoTranCompra

Codigo_IVA_E_Imptos

123-4

33

8455

2

2
SDAC– Versión 1.0

Ejemplos Caracterización Tipo de Compra

2. Facturas recibidas con Tipo de compra “Del Giro”, que deben cambiar a Tipo de compra
“Activo Fijo” con IVA Recuperable
Contribuyente ha recibido factura por compras por bienes destinados al Activo Fijo, pero al emitirse la Factura Electrónica no fue
caracterizada como Activo Fijo, de esta forma se registró en forma automática como “Del Giro”, por lo cual el contribuyente receptor
debe cambiar el tipo de Compra a Activo Fijo, con IVA Recuperable en su totalidad.
Indicador Tipo de Compra adquisiciones destinadas a Activo Fijo = 4
La modificación podría ser de alguna de las dos siguientes formas (el efecto es el mismo):
A)
Concepto

RUT del
Proveedor

Tipo de Documento

Folio del
Documento

Tipo de Transacción de
Compra

Código IVA e Impuestos

Nombre Campo en
CSV
Valor del Campo

Rut-DV

Codigo_Tipo_Doc

Folio_Doc

TpoTranCompra

123-4

33

7855

4

Concepto

RUT del
Proveedor

Tipo de Documento

Folio del
Documento

Tipo de Transacción de
Compra

Código IVA e Impuestos

Nombre Campo en
CSV
Valor del Campo

Rut-DV

Codigo_Tipo_Doc

Folio_Doc

TpoTranCompra

Codigo_IVA_E_Imptos

123-4

33

7855

4

1

Codigo_IVA_E_Imptos

B)

3
SDAC– Versión 1.0

Ejemplos Caracterización Tipo de Compra

3. Facturas recibidas con Tipo de compra “Del Giro”, que deben cambiar a Tipo de compra
“Activo Fijo” con IVA Uso Común
Contribuyente ha recibido factura por compras por bienes destinados al Activo Fijo, pero al emitirse la Factura Electrónica no fue
caracterizada como Activo Fijo, de esta forma se registró en forma automática como “Del Giro”, por lo cual el contribuyente receptor
debe cambiar el tipo de Compra a Activo Fijo, con IVA Uso Común.
Indicador Tipo de Compra adquisiciones destinadas a Activo Fijo = 4
Indicador Código IVA Uso Común = 2
La modificación debe ser de la siguiente forma:
RUT del
Proveedor

Tipo de Documento

Folio del
Documento

Tipo de Transacción de
Compra

Código IVA e Impuestos

Concepto
Nombre Campo en
CSV
Valor del Campo

Rut-DV

Codigo_Tipo_Doc

Folio_Doc

TpoTranCompra

Codigo_IVA_E_Imptos

123-4

33

7855

4

2

4
SDAC– Versión 1.0

Ejemplos Caracterización Tipo de Compra

4. Facturas recibidas con Tipo de compra “Del Giro”, pero que deben ser consideradas como
IVA Uso Común.
Contribuyente ha recibido factura por compras Del Giro, pero corresponde registrarla con IVA Uso Común.
Indicador Tipo de Compra adquisiciones IVA Uso Común = 5
La modificación debe ser de la siguiente forma:
RUT del
Proveedor

Tipo de Documento

Folio del
Documento

Tipo de Transacción de
Compra

Código IVA e Impuestos

Concepto
Nombre Campo en
CSV
Valor del Campo

Rut-DV

Codigo_Tipo_Doc

Folio_Doc

TpoTranCompra

Codigo_IVA_E_Imptos

123-4

33

7855

5

5
SDAC– Versión 1.0
