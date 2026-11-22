---
url: https://www.sii.cl/ayudas/ayudas_por_servicios/FormatoyValidacionesCaracterizacionII.pdf
titulo: INSTRUCCIONES CARGA MASIVA DE CAMBIO DE
categoria: ayuda
---
INSTRUCCIONES CARGA MASIVA DE CAMBIO DE
CARACTERIZACIÓN TIPO DE COMPRA DE DOCUMENTOS
TRIBUTARIOS ELECTRÓNICOS (DTE’s) RECIBIDOS EN EL SII.
Modificador masivo de tipo de compra de DTE a través de Carga de archivo de Complemento.
El presente documento describe la operatoria requerida para caracterizar en forma masiva, y a través de un
archivo en formato CSV, los Documentos Tributarios Electrónicos que se encuentran incluidos en un Registro
de Compras de un periodo determinado.
Finalidad de la Caracterización.
Considerando que un contribuyente puede recibir una cantidad importante de Documentos Tributarios
Electrónicos (DTE’s) por distintas adquisiciones y transacciones realizadas para el desarrollo de su actividad
económica, de los cuales algunos de ellos deban ser reclasificados en su caracterización de compras, en
función que han sido recibidos o consignados previamente con un indicador de Tipo de Compra que no
corresponde a la transacción; es que el Registro de Compras y Ventas cuenta con una funcionalidad que
permite la carga masiva de un archivo de cambio de caracterización de tipo de compras para Documentos
Tributarios Electrónicos existentes en el SII.
Para realizar lo anteriormente indicado, es necesario caracterizar dichos documentos informando a qué “Tipo
de Compra” corresponde cada uno, lo cual se puede realizar en las siguientes circunstancias:
1) Al momento de la emisión de cada documento (el emisor del DTE puede agregar la información
de Tipo de Compra a petición del receptor)
2) En forma individual en el detalle, luego de haber sido recibido el documento y que se encuentre
en calidad de Registro.
3) Por un medio de la carga de un archivo de caracterización masiva de complemento, tal como se
describe en el presente documento (lo cual es el fin de este instructivo).
Para cualquiera de las tres vías anteriormente indicadas, la caracterización de cada documento se encuentra
definida en la siguiente tabla (sólo una por documento):
Valores Tipo de Transacción de Compra
Compras del Giro
Compras en Supermercados o comercios similares
Adquisición de bienes raíces
Compra de Activo Fijo
Compras con IVA Uso Común
Compras sin Derecho a Crédito (IVA no recuperable)
Compras que no corresponde incluir

Código
1
2
3
4
5
6
7

Consideraciones respecto de la Caracterización:
El cambio indicado puede ser parcial o total, en cuanto a que sólo basta informar los Documentos Tributarios
Electrónicos a los cuales se les haya realizado un cambio de tipo de compra, sin ser necesario informar la
totalidad de los documentos. Si en algunos casos se mantienen el indicador de tipo de compra sin
modificación, sólo se realizará la modificación solo de los documentos en los que efectivamente se cambió
el tipo de compra.

En caso que no se realice un cambio a todos los documentos, o el cambio se realice a una cantidad limitada
de documentos, también se recuerda que es posible hacerlo en forma individual uno a uno en el mismo
detalle del Registro de Compras. Incluso es posible realizar cambio de tipo de compra de un DTE en forma
indistinta y consecutiva utilizando la opción de caracterización a través de archivo o en forma individual en
pantalla en la opción de cambio del detalle del Registro de Compras.
Para cargar masivamente esta información se debe realizar el envío de un archivo en formato tipo “csv”, el
cual debe contener la información relacionada a DTE’s del periodo tributario que se ha seleccionado al
ingresar.
Mediante el envío del archivo en formato csv, que contiene la información en campos delimitados por el
signo de puntación (;) punto y coma, es posible ingresar un número ilimitado de registros de una sola vez; sin
embargo, considerando que un archivo sólo modificará el tipo de compra de DTE’s que se incluyan en él y
que no elimina ni cambia el tipo de compra de DTE’s que no sean informados en un archivo en particular,
esto permite que puedan realizarse múltiples envíos de un mismo periodo, en que se informen distintos
DTE’s
Se recomienda descargar previamente la información de los DTE’s para confirmar que se encuentren
recibidos en el SII, que correspondan al periodo y que es necesario un cambio de tipo de Compra.
La información cargada por esta vía podrá ser visualizada en forma inmediata en el área de Registro del
Registro de Compras. En caso de realizar esta operación, no generará cambios inmediatos en la propuesta
de F29, sino que estos se verán reflejados al día siguiente en dicha aplicación.
Para generar correctamente el archivo se solicita revisar el Instructivo de llenado y los ejemplos relacionados.
No es necesario informar todos los documentos tributarios electrónicos de un periodo, puesto que en caso
que no hayan sido caracterizados con anterioridad, por defecto son registrados como “Compras del Giro”.
Asimismo, en cada archivo no se podrá informar documentos tributarios electrónicos que no se encuentren
informados en el periodo tributario mensual de compras que se ha seleccionado, lo cual será alertado
mediante un mensaje.
Procedimiento para efectuar la caracterización:
Un usuario autorizado o el mismo contribuyente, debe ingresar a Servicios online – Factura electrónica Registro de Compras y Ventas, autenticándose con RUT-Clave, en caso de que el usuario pueda ingresar
información a más de un RUT, deberá seleccionar el N° de RUT del contribuyente sobre el cual se operará.
Posteriormente se debe seleccionar el periodo (mes y año) y hacer “click” en Consultar; desplegándose la
vista de Registro de Compras y Ventas, en donde se debe seleccionar el área de “Registro” de la opción de
Registro de Compras. A continuación se debe presionar el botón “Carga Masiva de Complementos”,
permitiendo seleccionar un archivo (previamente construido) y cargarlo en bases de datos. Lo anterior
realizará un cambio masivo del “Tipo de compra”, de los documentos consignados en el periodo y que
efectivamente se les esté realizando una modificación en el tipo de compra, luego se debe presionar el botón:
“Cargar Modificaciones Tipo de Compra de DTE”
Observaciones:
Considerando que en los registros de compras pueden existir documentos consignados en diferentes
periodos, o se encuentren en distintos estados de recepción (registro o pendientes), es que se recomienda
que antes de realizar una caracterización, se descarguen los registros de documentos tributarios electrónicos
de compra, con el fin de construir un archivo correcto de carga masiva de modificación de tipos de compra.´

Los DTE’s deberán estar previamente registrados en el detalle del Registro de Compra y sólo pueden
corresponder a los siguientes tipos de documentos:
Nombre Documento
Factura Electrónica
Factura Exenta Electrónica
Liquidación Factura Electrónica
Factura de Compra Electrónica
Nota de Débito Electrónica
Nota de Crédito Electrónica

Código Documento
33
34
43
46
56
61

Formato del Archivo:
Carga masiva de complementos para documentos tributarios electrónicos de compra recibidos en el SII. En
este caso sólo se solicitará que se informen los campos relacionados a la identificación del documento y los
campos de asignación de la compra, es así que el archivo de subida deberá contar con la siguiente estructura
en formato CSV:
|RUT-DV| Codigo_Tipo_Doc | Folio_Doc | TpoTranCompra |Codigo_IVA_e_Impuestos
Donde:
Tipo
Transacción
Compra
1
2
3
4
5
6
7

Descripción

Código de IVA e
Impuesto Asociado

Clasificación

Compras del Giro
Compras en Supermercados o comercios
similares
Adquisición de bienes raíces
Compra de Activo Fijo
Compras con IVA Uso Común
Compras sin Derecho a Crédito
Compras que no corresponde incluir

1
1y2

DEL GIRO O IVA
USO COMUN (*)

(*) DEL GIRO O IVA USO COMUN

(**) CODIGO IVA NO RECUPERABLE

1y2
1y2
2
1, 2, 3, 4 y 9
9

CODIGO IVA NO
RECUPERABLE
(**)

1

Del giro

2

Uso Común

1

Compras
destinadas a IVA a
generar
operaciones no
gravados
o
exentas
Facturas
de
proveedores
registradas fuera
de plazo.

2

3

Gastos
rechazados

4

Entregas gratuitas
(premios,
bonificaciones,
etc.) recibidas

9

Otros
