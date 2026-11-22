---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_iecv.pdf
titulo: FORMATO DE INFORMACIÓN ELECTRÓNICA DE COMPRAS Y VENTAS
categoria: factura_electronica
---
FORMATO DE INFORMACIÓN ELECTRÓNICA DE COMPRAS Y VENTAS

DOCUMENTO VÁLIDO PARA:
Facturadores Electrónicos y Obligados a DJ 3327 y 3328

Versión 3.0
Marzo de 2016

Información Electrónica de Compras y Ventas

ÍNDICE DE CONTENIDO
Cambios registrados en este documento: .................................................................................................................................................................................. 3
1.- INSTRUCCIONES GENERALES ................................................................................................................................................................................................................. 6

1.1 Referente a los Archivos ................................................................................................................................................................................... 6
1.2 Zonas de la Información Electrónica De Compras y Ventas ............................................................................................................................ 8
1.3 Estructura de un envío ...................................................................................................................................................................................... 9
1.4 Instrucciones generales de formato para las Zonas ...................................................................................................................................... 10
1.5 Validaciones de envíos ................................................................................................................................................................................... 11
1.6 Obligatoriedad por Zonas ............................................................................................................................................................................... 12
2.- INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328 ........................................................................................................................................... 13
2.1. Carátula para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328 ................................................................................................... 13
CARÁTULA PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328 ............................................................................................. 13
2.2. Resumen segmento para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328 ................................................................................. 15
2.3. Resumen período para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328: ................................................................................... 18
2.4.
Detalle para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328 ............................................................................................... 21
2.5. Certificado de Autorización de Libros (CAL) – Libros Contables Electrónicos (NO APLICA PARA DJ3327 Y3328) ............................ 26
2.6. Comprobante de Certificación (COCERTIF) – Libros Contables Electrónicos (NO APLICA PARA DJ3327 Y3328) ............................. 26
3.- INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327 ....................................................................................................................................... 27
3.1.Carátula para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327 ................................................................................................ 27
3.2. Resumen segmento para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327 .............................................................................. 29
3.3. Resumen período INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3328 ......................................................................................... 32
3.4.
Detalle para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3328 ........................................................................................... 35
4.- CÓDIGOS DE DOCUMENTOS ........................................................................................................................................................................................ 39
4.1 De Ventas ........................................................................................................................................................................................................ 39
4.2 De Compras .................................................................................................................................................................................................... 40
5.- CÓDIGOS DE DOCUMENTOS ZONA FRANCA Y MERCADERÍAS NO NACIONALES ................................................................................... 41
5.1. Información electrónica de Ventas ................................................................................................................................................................ 41
5.2. Información electrónica de Compras ........................................................................................................................................................... 41
6.- CÓDIGOS DE AJUSTE DE TIPO DE CAMBIO ............................................................................................................................................................ 41
7.- CÓDIGOS DE IMPUESTOS Y RECARGOS. ................................................................................................................................................................. 42
Versión 3.0 - Marzo 2016

Pág. 2 de 45

Información Electrónica de Compras y Ventas

Cambios registrados en este documento:
Cambios 2016
1. Se corrige información respecto a la descripción de la forma de registro del factor de proporcionalidad del IVA y factor de proporcionalidad ILA en el libro de compras,
señalando que debe ser el mismo para todos los documentos informados. No se cambia schema ni validaciones, sólo es cambio de información. Para cada libro
mensual de compras debe utilizarse sólo un valor de factor de proporcionalidad, aplicado sobre los documentos que acceden al cálculo de cada uno de ellos.

Cambios 2015
1. Modificaciones a las tasas de ILA. Agregándose el código 271 para bebidas con alto contenido de azúcares. En general las tasas de impuestos pueden variar con el
tiempo por lo cual se ha intentado mantener los códigos asociados a los tipos de bebidas. Capitulo N° 7, registros 24-271.
2. Otras actualizaciones de tasas. Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda > Aprenda sobre.>. Aprenda sobre los Impuestos >

Cambios 2011
1.
2.
3.
4.
5.
6.

Se modifica formato incorporando DJ3327 y 3328
Se actualiza definición de Impuestos Específicos a los Combustibles según Ley N° 20.493 (SIPCO), su Reglamento y Res. Ex SII N° 51 de 2011.
Se actualiza definición del registro de documentos anulados.
En puntos 4.1 y 4.2 se agrega documento 29, Factura de Inicio
En punto 7 se agrega el Código de Impuesto N°60: Impuesto Retenido Factura de Inicio
En punto 7 se modifican tasas de retención de legumbres (13% a 10%) y trigo (de 11% a 4%), Res.Ex N° 189 y 192, de 2010.

Cambios 2010
1. Se aumenta capacidad de caracteres de código Número Identificador del Receptor Extranjero <NumId>.

Cambios 2009
1. Se agrega en el punto 7 el Código de de Impuesto N°53: Retención Suplementeros
2. Se agrega Código de Autorización de Reemplazo (Rectificación de Libro). Etiqueta <CodAutRec> de la Carátula, y se agrega el valor “RECTIFICA” a la etiqueta
<TipoLibro> de la Carátula. Este nuevo valor se debe utilizar en conjunto con al etiqueta <CodAutRec>

Cambios 2006
1. Se agregan dos secciones que son exclusivas para envió de Libros Contables Electrónicos.
2. Para los campos <MntImp> y <TotMntImp> ahora se aceptan montos negativos.
3. El tipo de documento “Declaración de Ingreso de Zona Franca” se corrigió el código porque habían 2 valores diferentes en la documentación. Ahora se elimina el
código “918” y se reemplazó por “911”.

Versión 3.0 - Marzo 2016

Pág. 3 de 45

Información Electrónica de Compras y Ventas

Cambios 2005
1. Actualización punto 7. Códigos de Impuestos y Recargos, se agregan los Códigos de Impuesto 51 y 52.
2. Debajo de cada campo se incluye el nombre del tag xml que tiene asociado dentro del schema. Por ejemplo <TpoDoc>.
3. Se agregan nuevos códigos de documentos: Boleta No Afecta o Exenta Electrónica: (Cód. 41), Liquidación-Factura Electrónica (Cód 43), Factura de Exportación
Electrónica (110), Nota de Débito de Exportación Electrónica (Cód 111) y Nota de Crédito de Exportación Electrónica (Cód 112)
4. Se agregan códigos de ajuste de tipo de cambio, sólo para la Información Electrónica de Ventas de contribuyentes que emitan documentos de exportación
electrónicos, o estén autorizados a registrar documentos internos que incluyan valores en otra moneda: Ajuste aumento Tipo de Cambio (código 500): a utilizar
cuando la paridad (moneda extranjera)/(moneda nacional) aumente entre la fecha de emisión del documento y la fecha de cierre del periodo y ajuste disminución
Tipo de Cambio (código 501): a utilizar cuando la paridad (moneda extranjera)/(moneda nacional) disminuya entre la fecha de emisión del documento y la fecha de
cierre del periodo
5. Se corrige información de códigos: se elimina el código 103 (Liquidación) de la Información Electrónica de Compras; Se eliminan los códigos 900 y 921
(Liquidación recibida por el mandante y Liquidación recibida por mandatario) de la Información Electrónica de Ventas; Se redefine el código 919, sólo para ventas
nacionales de pasajes sin Factura; Se agrega el código 924, sólo para ventas internacionales de pasajes sin Factura
6. Se admiten valores negativos en Liquidaciones Factura (tipos 40 y 43) para los siguientes campos: “Monto Neto”, “Valor Neto Comisiones y Otros Cargos”,
“Monto exento o no gravado”, “Valor Comisiones y Otros Cargos No Afectos o Exentos”, “Monto IVA”, “IVA Propio”, “IVA Terceros”, “IVA Comisiones y Otros Cargos”
y “Monto Total”.
7. Se admiten valores negativos en Liquidaciones (cód 103) para los siguientes campos: “Monto Neto”, “Monto exento o no gravado”, “IVA”, “IVA Propio”, “IVA
Terceros”, y “Monto Total”.
8. Se agregan nuevos campos:
a) En Información Electrónica de Ventas: Campo “Excepción EMISOR/RECEPTOR”, para ser utilizado cuando el contribuyente anota en su libro de venta una nota
(crédito o débito) que referencia factura de compra recibida.
b) En Información Electrónica de Ventas: Campo “Rut Emisor”, para ser utilizado en forma obligatoria en Liquidaciones, Liquidaciones-Factura y LiquidacionesFactura Electrónicas recibidas.
c) En Información Electrónica de Ventas; “Valor Neto Comisiones y Otros Cargos”, “Valor Comisiones y Otros Cargos no Afectos o Exentos” e “IVA Comisiones y
Otros Cargos”, que serán utilizados solamente por Liquidaciones-Factura y Liquidaciones-Factura Electrónicas.
d) En la Información Electrónica de Ventas: Campos “Número identificador del Receptor extranjero” y “Nacionalidad del Receptor Extranjero” para complementar la
información de documentos emitidos a extranjeros.
9. Se Corrige o Aclara Información.
a) En Información Electrónica de Compra: Se cambia nombre de Campo “EMISOR” por “Excepción EMISOR/RECEPTOR”, para ser utilizado cuando el
contribuyente anota en su libro de compra una nota (crédito o débito) que referencia factura de compra emitida.
b) Se deja obligatorio el PERÍODO TRIBUTARIO en todos los libros. En libros tipo “ESPECIAL”, se debe poner el primer período tributario que incluye dicho libro.
c) Se agregan Códigos de impuesto (47,48, 49 y 50) en Tabla N° 7 y se incorporan Notas de Crédito y Débito como tipos de documentos en que se aplican
impuestos (14, 15, 30 al 39 y 41).
d) Se indica que tampoco se registran en el detalle (Tipo de Documento) los documentos tipo resumen Código 41, correspondientes a “Total operaciones del mes,
con boleta electrónica no afecta o exenta”, y que sí se debe indicar en Resumen del Período como Tipo y Cantidad de documentos.
e) Se admite en el detalle del libro de Venta indicar: IVA Retenido Total, IVA retenido Parcial e IVA no retenido también para las Notas de Crédito y de Débito
asociadas a Facturas de Compra.
f) Se admite en el detalle del libro de Compra indicar IVA no Retenido también para las Notas de Crédito y de Débito asociadas a Facturas de Compra.
g) Se modifica fórmula del Monto Total del Detalle de Ventas en consideración al punto anterior y a la incorporación de los campos de Comisiones y Otros Cargos.

Versión 3.0 - Marzo 2016

Pág. 4 de 45

Información Electrónica de Compras y Ventas

Cambios 2004:
1.- Se agregan campos opcionales
a) Folios anulados: para informar la cantidad de folios anulados por tipo de documento
b) IVA terceros e IVA propio: Ambos se crean como opcionales para quienes venden por cuenta de un mandante.
c) Monto IVA Activo Fijo
d) Emisor: Se usa en libro Compra. Destinado a diferenciar las Notas de Crédito emitidas por el comprador que afectan a una Factura de Compra, de las Notas de
Crédito emitidas por el vendedor.
2.- Se crean códigos:
a) De Retención de Impuestos: Se crea código 41 para registrar la retención para cambio sujeto de la construcción en libro Compra y de Tipo de documento: Se
crea código 921 para registrar Liquidación Factura emitida por mandatario en libro Venta y 922 para registrar disminuciones de débito por diferencias.
b) Se agrega códigos 9 para “otros” en la Tabla de No Recuperable del libro de Compra
3.- Se corrige información de tasas de retención
a) IVA Anticipado Harina y carne: Se corrige error en tasas
4.- Se cambia obligatoriedad de contadores de “cantidad de operaciones”: Campos pasan a ser opcionales.
5.- Se corrige o aclara información:
a) IVA Anticipado Harina y Carne: Se corrige error en tasas
b) Uso de códigos de retenciones: Las retenciones de IVA por cambio de sujeto se usan sólo en el Libro de Compras. El contribuyente que recibe Facturas de
Compra, no tiene que codificar según el tipo de producto que originó la retención.
c) En los archivos electrónicos del Tipo Especial, el campo Periodo Tributario de la carátula debe venir con el primer período.
d) Los montos de los documentos que han sido anulados, no se deben considerar en las sumas de totales. Esto es para los folios anulados. Distinto es el caso de
los documentos anulados vía otro DTE, en que tanto el documento primitivo como aquel que lo anula, SI DEBE SER CONSIDERADO EN LOS TOTALES.
e) Los totales de Cantidad de documentos sí deben incluir a los anulados.

Versión 3.0 - Marzo 2016

Pág. 5 de 45

Información Electrónica de Compras y Ventas

1.- INSTRUCCIONES GENERALES
Este documento describe el contenido que debe tener la Información electrónica de Compra y de Venta, así como también, el contenido necesario
para presentar la Declaración juradas 3327 y 3328. La información aquí contenida puede ser utilizada por ambos grupos de contribuyentes y solo
en los casos debidamente indicados existe diferenciación.
El envío a hacer al SII debe contener toda la información de los documentos de Venta y de Compras tanto electrónicas como no electrónicas.
La información debe ser remitida mensualmente en el formato XML definido por el SII.
El archivo a entregar deberá cumplir con las especificaciones que se detallan a continuación:
1.1 Referente a los Archivos
1. Formato XML definido por el SII.
2. La Información Electrónica de Compra (IEC) debe mantenerse y entregarse separada de la Información Electrónica de Ventas (IEV).
3. Se distinguen:
a) (No aplica las DJ 3327 y 3328)
Archivos MENSUALES: libros regulares por período tributario, los cuales se debe enviar mensualmente al SII.
 De Venta: En el Sector Detalle, se deberá incluir sólo la información de los Documentos No Electrónicos emitidos y de las Facturas de
Compra Electrónicas y manuales recibidas; en consecuencia no se necesitará incluir el detalle de los documentos electrónicos emitidos, y si
se incluyen no serán considerados. En el RESUMEN del PERÍODO (ver 1.2) se deberá incluir los totales de todos los documentos tanto
electrónicos como no electrónicos. Si en el período no ha habido ventas que se devenguen en ese mes, se debe enviar sólo la carátula.


De Compra: Se debe incluir detalle y Resumen Período para todos los documentos electrónicos y no electrónicos. Si en el período no ha
habido compras, se debe enviar sólo la carátula.

b) (No aplica las DJ 3327 y 3328)
Archivos ESPECIALES: corresponden a archivos requeridos por el SII vía una notificación. Un libro especial podrá contener sólo cierto
tipo de documentos, ciertos períodos o alguna selección de la información. Un archivo especial se distingue de los libros regulares, en
que indica el folio de la notificación en la carátula.


Se debe mantener la separación entre archivos de Venta y archivos de Compra.



Podrán enviarse en uno o varios envíos, tal como se establece en el punto 4 siguiente.

Versión 3.0 - Marzo 2016

Pág. 6 de 45

Información Electrónica de Compras y Ventas



Se considera que todos los envíos de la notificación corresponden a un sólo libro, cuya identificación es el folio de la notificación. En caso que
los datos incluidos abarquen más de un período tributario, se deberá indicar el período tributario que corresponda a la fecha más temprana de
un documento en el campo “Período tributario”.



Deberán contener siempre la Zona Resumen Período.



En caso de contener detalle, podrán incluir documentos electrónicos y no electrónicos de acuerdo a lo que se haya solicitado en la notificación.
Si se solicita información de los documentos electrónicos, se deberá entregar también el detalle de éstos, excepto que se diga expresamente
en la notificación que esta información se omita.

c) (Aplica solo a las DJ 3327 y 3328)


DJ 3328, de Venta: En el Sector Detalle, se deberá incluir la información de los Documentos Electrónicos y No Electrónicos emitidos y de las
Facturas de Compra, Liquidaciones y Liquidaciones Factura, electrónicas y manuales recibidas. En el RESUMEN del PERÍODO (ver 1.2) se
deberá incluir los totales de todos los documentos tanto electrónicos como no electrónicos. Si en el período no ha habido ventas que se
devenguen en ese mes, se debe enviar sólo la carátula.



DJ 3327, de Compra: Se debe incluir detalle y Resumen Período para todos los documentos electrónicos y no electrónicos. Si en el período no
ha habido compras, se debe enviar sólo la carátula.



Cuando se requiere enviar un año, se deben enviar 24 libros en total (12 de compras, 12 de ventas) cada uno de los cuales debe ser identificado
por un folio de notificación y el período tributario.



Podrán enviarse en uno o varios envíos, tal como se establece en el punto 8 siguiente.



Deberán contener siempre la Zona Resumen Período, excepto aquellos períodos en que no han habido compras o ventas.



Cada libro enviado deberá indicar que es ESPECIAL.

4. Independiente del tipo de archivo (mensual o especial) éste se puede enviar de una sola vez, o en varios envíos. Cada tipo de envío puede ser
identificado a través de la carátula que lo define, que indica si es:


Total: Se hace un solo envío para el período tributario o para la notificación. “Se debe anotar TOTAL” en el identificador de la Carátula.



Parcial: Envíos parciales. Pueden ser de 1 a 999 envíos. Se debe anotar “PARCIAL” seguida por el número del envío parcial, por ejemplo P1, P2,
etc. Esto es para todos los envíos parciales, excepto para el último.



Final: Corresponde al último envío parcial. Se debe anotar “FINAL” en el identificador de la Carátula.



Ajuste: Corresponde a un envío que permite agregar o eliminar documentos informados anteriormente. Se debe anotar “AJUSTE” en el identificador
de la Carátula.

Versión 3.0 - Marzo 2016

Pág. 7 de 45

Información Electrónica de Compras y Ventas

1.2 Zonas de la Información Electrónica De Compras y Ventas
En los Archivos se distinguen las siguientes zonas:
a) Carátula
Contiene datos generales de la información del envío los cuales corresponden al Rut del contribuyente emisor, período tributario, tipo de segmento,
y número de Segmento en el caso de envíos parciales.
b) Resumen Segmento
Contiene los totales por tipo de documento. Esta Zona es obligatoria si viene la Zona de Detalle, excepto si el envío es TOTAL.
Las boletas u otros que se incluyen sólo totalizados, no se incluyen en este resumen y deben ir sólo en el Resumen Período.
c) Resumen Período
En cuanto a contenido
El resumen del período se debe construir en base a todos los Resúmenes de Segmento del período enviados.
 En consecuencia, no se debe enviar hasta que exista la seguridad que no hay rechazos a los segmentos.
 Aparte de totalizar lo que se informó en los segmentos, se debe agregar la información de los documentos que sólo se registran como
totales (boletas u otros), incorporando una línea por tipo de documento.
 En el IEC se deben agregar los campos para determinar el crédito en base a proporcionalidad.
En cuanto al tipo de envío
 El Resumen Periodo se debe incluir en un envío de tipo TOTAL, FINAL o AJUSTE.
 Si el envío es FINAL este debe incluir sólo el Resumen Período.
 Si el envío es TOTAL, el Resumen Período puede venir acompañado de Detalle (si hay documentos que informar).
 Si el envío es AJUSTE, el Resumen Período puede venir acompañado de Detalle y de Resumen Segmento (si hay documentos que
informar).
d) Detalle
En esta Zona se debe detallar una línea por cada documento. No se incluyen documentos del tipo totales, tales como Boletas o Resumen de
pasajes.
El detalle se incluye en un envío sólo si hay documentos, informados uno a uno.

Versión 3.0 - Marzo 2016

Pág. 8 de 45

Información Electrónica de Compras y Ventas

1.3 Estructura de un envío
A continuación se explican los distintos tipos de envío y se detalla que debe contener cada uno
a) Envío Total: Un envío es del tipo Total, cuando se envía el IEV, el IEC del período tributario o de la notificación en un único envío. Este tipo de
envío, que se identifica como “TOTAL” en el campo tipo de la carátula, puede contener:




Sólo el Resumen Período: Esto se aplica si no corresponde enviar detalle. Un ejemplo de este caso, es una empresa que, durante
el período sólo emitió Boletas, dato que sólo debe ser consignado en el RESUMEN PERÍODO.
Zona de Detalle y Resumen Período: Cuando hay documentos unitarios que informar

b) Envío Parcial: Un envío parcial significa que el IEV o el IEC del período tributario o de una notificación se mandan en más de un envío. Un envío
PARCIAL debe indicar “PARCIAL” en el campo “Tipo” de la CARÁTULA. En este tipo de envío no se puede incluir el RESUMEN PERÍODO, ya
que este último debe ser enviado en forma independiente. Todo envío parcial debe incluir una Zona DETALLE.
c) Envío Final: El envío final se realiza una vez que se han recibido y aceptado por parte del SII, todos los envíos parciales. Este tipo de envío debe
contener sólo la Zona RESUMEN PERÍODO. Se debe indicar “FINAL” en el campo tipo de la CARÁTULA.
d) Envío de Ajuste: Este tipo de envío sólo se puede realizar una vez hecho un envío FINAL o TOTAL y tiene como objetivo agregar registros
faltantes, eliminar registros o modificar la información de un registro.
Se indica como AJUSTE en la CARÁTULA y puede contener



1.

Sólo el Resumen Período: Si la modificación es de algún documento del tipo Totales. En este caso, el Resumen Período anterior
es reemplazado por el nuevo.
Las tres Zonas de datos que deben contener:
Zona Detalle: Con el detalle del ajuste. Se puede eliminar y/o agregar uno o más registros del IEV o IEC; el tipo de operación se debe
anotar en el campo “Operación” del detalle de Ajuste. Si la modificación consiste en cambiar algún dato de un documento, se debe
eliminar el registro anterior y agregar el documento con los valores correctos.

Versión 3.0 - Marzo 2016

Pág. 9 de 45

Información Electrónica de Compras y Ventas

Por ejemplo si se ha registrado:
TIPO DOCUMENTO

FOLIO

NETO

IVA

TOTAL

33

1234

10.000

1800

11.800

y había un error en el tipo de documento de forma que los valores correctos son:
TIPO DOCUMENTO

FOLIO

NETO

IVA

TOTAL

61

1234

10.000

1800

11.800

en la Zona DETALLE se debe registrar:

2.

OPERACIÓN

TIPO DOCUMENTO

FOLIO

NETO

IVA

TOTAL

2
1

33
61

1234
1234

10.000
10.000

1800
1800

11.800
11.800

Zona Resumen Segmento: Para construir el total por documento, se suman los ajustes con signo, restando los campos que se
eliminan y sumando los que se agregan. En el ejemplo anterior en el RESUMEN SEGMENTO debe indicarse:
TIPO DOCUMENTO

CANTIDAD DE DOCUMENTOS FOLIO

NETO

33
61

-1
1

-10.000 -1.800 -11.800
10.000 1.800 11.800

IVA

TOTAL

Dado lo anterior, todos los campos numéricos del Resumen Segmento pueden ser negativos.
3.

Zona Resumen Período: El Resumen período debe totalizar todos los segmentos enviados más el de ajuste (considerando el signo).

1.4 Instrucciones generales de formato para las Zonas
-

Los largos indicados se refieren a tamaño máximo.
En la información de tipo numérica, los decimales se separan con punto y se deben indicar sólo cuando el valor que se desea incluir contiene
decimales significativos.
No deben separarse los miles con carácter alguno.
Todos los valores de montos deben venir en pesos.
En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben ser reemplazados por la
secuencia de escape que el estándar define para dichos caracteres.
La columna (*), indica que si la información recibida por el SII no contiene este campo, la información se considera incompleta y será rechazada.
En general, los datos deberán ser positivos, excepto que se indique lo contrario en forma expresa.

Versión 3.0 - Marzo 2016

Pág. 10 de 45

Información Electrónica de Compras y Ventas

1.5 Validaciones de envíos
Al recibir un envío el SII validará:
a)

Si el envío es tipo Parcial
 Campo “Tipo de Envío” de CARÁTULA debe indicar “PARCIAL”
 Existe sólo Resumen Segmento y Detalle
 Suma por documento del RESUMEN SEGMENTO corresponda con DETALLE

b)

Si el envío es Total
 Campo “Tipo de Envío” de CARÁTULA debe indicar “TOTAL”
 Es obligatorio el Resumen Periodo
 Si se informan documentos del tipo Facturas, Notas etc. que requieren detalle por documento, debe venir DETALLE.

c)

Si el envío es Final
 Campo “Tipo de Envío” de CARÁTULA debe indicar “FINAL”
 Sólo debe venir Resumen Período
 Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período

d)

Si el envío es Ajuste
 Campo “Tipo de Envío” de CARÁTULA debe indicar “AJUSTE”
 Es obligatorio el Resumen Periodo
 Si se informan documentos del tipo Facturas, Notas etc. que requieren detalle por documento, debe venir DETALLE, informando el tipo de
“operación” y RESUMEN SEGMENTO
 Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período, incluyendo el ajuste.

e)

Sólo si el envío es por notificación (especial), en el campo período tributario de la carátula se debe poner el primer período tributario que incluye
EN CASO DE DISCORDANCIA CON LO ANTERIOR SE RECHAZARÁ EL ENVÍO.

CASO ESPECIAL: EN EL CASO DE LAS FACTURAS Y BOLETAS DE SERVICIOS PERIÓDICOS DOMICILIARIOS, LOS DOCUMENTOS SE DEBEN
INFORMAR EN EL PERÍODO TRIBUTARIO EN QUE SE DEVENGA EL IMPUESTO Y NO CUANDO SE EMITE EL DOCUMENTO.

Versión 3.0 - Marzo 2016

Pág. 11 de 45

Información Electrónica de Compras y Ventas

1.6 Obligatoriedad por Zonas
La obligatoriedad de cada una de las zonas por tipo de documento se especifica en la siguiente Tabla:
ZONA

CÓDIGO
OBLIGATORIEDAD

OBSERVACIONES

Carátula

1

Siempre obligatoria

Resumen Segmento

2

Resumen Período

2

Es obligatorio en envíos Parcial y Ajuste cuando
existe Detalle
Obligatoria en envío Total, Final o Ajuste

Detalle

2

Certificado Autorización
Libros (CAL)

2

Comprobante de
Certificación (COCERTIF)

2

No debe venir en envío Final
Exclusivo para Libro Contable Electrónico
Exclusivo para Libro Contable Electrónico

Códigos de Obligatoriedad:
1:
2:
3:

Dato obligatorio. El dato debe estar en el documento siempre.
Dato condicional. El dato se registra sólo si corresponde.
Opcional.

En referencia al formato de los datos:
-

El tipo de información puede ser alfanumérica (ALFA) o numérica (NUM), en ambos tipos de información el largo indicado es el largo máximo.
En la información de tipo numérica, los decimales se separan con punto y se indican sólo cuando el valor que se desea incluir contiene decimales
significativos. No debe separarse las miles con carácter alguno.
En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben ser reemplazados por la
secuencia de escape que el estándar define para dichos caracteres.

La columna (*), indica que si el archivo recibido por el SII no contiene este campo, el DTE se rechazará por esquema XML.

Versión 3.0 - Marzo 2016

Pág. 12 de 45

Información Electrónica de Compras y Ventas

2.- INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328
2.1. Carátula para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328

CARÁTULA PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

1

RUT Contribuyente
<RutEmisorLibro>

ALFA

10

Corresponde al Rut del contribuyente emisor con guión y dígito verificador

*

1

2

RUT Enviador

ALFA

10

Corresponde al Rut del usuario autorizado que hace el envío al SII

*

1

ALFA

7

Periodo Tributario , en formato AAAA-MM (Año (4),Mes (2)).

<RutEnvia>
3

PERÍODO TRIBUTARIO

1

Si “tipo de Libro” es ESPECIAL y abarca más de un período se debe indicar la fecha del
primer período tributario.

<PeriodoTributario>

Para la DJ 3328:
Periodo Tributario, en formato AAAA-MM (Año (4),Mes (2)).
Debe indicarse el período del libro enviado. Se debe enviar un libro por cada período.

4

Fecha Resolución

ALFA

10

<FchResol>
5

Número Resolución

Tipo de Operación

*

1

*

1

Para la DJ 3328: Debe ser de valor fijo: 2006-01-20
NUM

6

<NroResol>
6

AAAA-MM-DD

Número de Resolución que autoriza al contribuyente como emisor electrónico.
Para la DJ3328: Debe ser de valor fijo 102006

ALFA

6

=VENTA

*

1

ALFA

8

MENSUAL (Corresponde a los libros Regulares)

*

1

<TipoOperacion>
7

Tipo de Libro
<TipoLibro>

ESPECIAL (Corresponde a un libro solicitado vía una notificación)
RECTIFICA (Corresponde a un libro que reemplaza a uno ya recibido por el SII, requiere un
Código de Autorización de Reemplazo de Libro Electrónico en la etiqueta <CodAutRec> )
Para la DJ3328: ESPECIAL

8

Tipo de Envío
<TipoEnvio>

ALFA

7

TOTAL: información total del mes. Si no se incluye, se asume que es total.

2

PARCIAL: Se está enviando un segmento que tiene parte de la información del
período
FINAL: Corresponde al último segmento

Versión 3.0 - Marzo 2016

Pág. 13 de 45

Información Electrónica de Compras y Ventas

CARÁTULA PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

AJUSTE : Movimientos ingresados con posterioridad a un envío FINAL o TOTAL
9

Numero de Segmento

NUM

3

Número del segmento. Sólo si el TIPO DE ENVIO es PARCIAL

2

NUM

10

Folio de notificación. Obligatorio si es un tipo de envío ESPECIAL

2

<NroSegmento>
10

Folio de Notificación
<FolioNotificacion>

11

Código de Autorización de Reemplazo de
Libro Electrónico.
<CodAutRec>

Para la DJ3328: Debe ser de valor fijo: 102006
ALFA

10

Código de Autorización de Reemplazo de Libro Electrónico, obtenido por un Representante
Legal de la empresa, para permitir el reemplazo de un libro recibido OK por SII para un
período y tipo de libro específico.

2

Para la DJ3328: No aplica

Versión 3.0 - Marzo 2016

Pág. 14 de 45

Información Electrónica de Compras y Ventas

2.2. Resumen segmento para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328
En este resumen se deben entregar totalizados los montos por campo de cada tipo de documento, para los documentos incluidos en el detalle.
Todos los montos pueden ser negativos así como también el campo “cantidad de documentos” que puede ser negativo en un envío de ajuste.
RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°
1

NOMBRE DEL CAMPO
TIPO DE DOCUMENTO

TIP
O

LARGO
MÁX.

NUM

3

NUM

10

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

Para todos los tipos de documentos que se han informado en el archivo de detalle

*

1

Cantidad de documentos del tipo especificado en el campo Tipo de Documento. Incluye
anulados.

*

1

<TpoDoc>
2

CANTIDAD DE DOCUMENTOS
<TotDoc>

Cantidad de documentos cuyos folios han sido anulados, previo al envío al SII. Estos
documentos no se totalizan en los campos siguientes.

TOTAL ANULADOS
3

4

NUM

10

<TotAnulado>

TOTAL OPERACIONES
EXENTO O NO GRAVADO

CON

CAMPO PRÓXIMO A ELIMINARSE. Se mantiene para contribuyentes que
están informándolo

MONTO
NUM

10

TOTAL MONTO EXENTO O NO GRAVADO

3
Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
3. En el caso de facturas exentas, este monto es igual al del campo 2.

<TotOpExe>
5

2

No se contabiliza aquí si un documento electrónico ha sido anulado posterior al envío al SII,
con Una Nota de Crédito o Débito. Esos documentos deben ser informados como emitidos,
con todos los datos que correspondan.

NUM

18

Si no hay montos de este tipo, se debe registrar un cero.

*

1

NUM

18

Si no hay montos de este tipo, se debe registrar un cero.

*

1

NUM

18

Si no hay montos de este tipo, se debe registrar un cero.

*

1

18

Sólo aplica para Notas de Crédito.

3

NUM

18

Sólo cuando hay venta o servicio por cuenta de terceros

3

NUM

18

Sólo cuando hay venta o servicio por cuenta de terceros

3

NUM

18

<TotMntExe>
6

TOTAL MONTO NETO
<TotMntNeto>

7

TOTAL MONTO IVA
<TotMntIVA>

8

IVA fuera plazo
<TotIVAFueraPlazo>

9

TOTAL IVA propio
<TotIVAPropio>

10

TOTAL IVA terceros
<TotIVATerceros>

11

TOTAL Ley 18.211

2

<TotLey18211>

Versión 3.0 - Marzo 2016

Pág. 15 de 45

Información Electrónica de Compras y Ventas

RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIP
O

LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.
Totaliza por código para cada tipo de documento

Tabla Tipos de Impuesto o recargo
<TotOtrosImp>
12

Código del Impuesto o Recargo

NUM

18

Incluye Combustibles y margen Comercialización

2

NUM

18

IVA NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente.

3

NUM

18

Totales por documento

2

IVA NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente.

3

NUM

18

Totales por documento

2

65% NUM

18

2

NUM

18

2

<CodImp>
13

Valor del Impuesto o Recargo

2

<TotMntImp>
14

TOTAL
OPERACIONES
RETENIDO TOTAL

CON

<TotOpIVARetTotal>
15

IVA Retenido Total
<TotIVARetTotal>

16

TOTAL
OPERACIONES
RETENIDO PARCIAL

CON

<TotOpIVARetParcial>
17

IVA Retenido Parcial
<TotIVARetParcial>

18

TOTAL
CREDITO
ESPECIAL
EMPRESAS CONSTRUCTORAS
<TotCredEC>

19

TOTAL Depósito envases
<TotDepEnvase>

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.
Totaliza por código para cada tipo de documento

Tabla Liquidaciones
<TotLiquidaciones>
20

TOTAL Valor Neto Comisiones y Otros Cargos

Puede ser negativo.
NUM

18

TOTAL Valor Comisiones y Otros Cargos no
Afectos o Exentos
NUM

18

2

<TotValComNeto>
21

Puede ser negativo.
2

<TotValComExe>

Versión 3.0 - Marzo 2016

Pág. 16 de 45

Información Electrónica de Compras y Ventas

RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°
22

NOMBRE DEL CAMPO

TIP
O

LARGO
MÁX.

NUM

18

NUM

18

Suma para el tipo de documento

OPERACIONES CON IVA NO RETENIDO NUM
PARCIAL

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente. Sólo aplica para Factura de Compra recibidas

TOTAL IVA Comisiones y Otros Cargos

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

Puede ser negativo.
2

<TotValComIVA>
23

TOTAL MONTO TOTAL

*

1

<TotMntTotal>
24

3

<TotOpIVANoRetenido>
25

TOTAL IVA no retenido

NUM

18

2

NUM

18

Valor puede ser negativo

3

NUM

18

Valor puede ser negativo

3

TOTAL EXENTO Venta de pasajes Transporte NUM
nacional

18

Sólo ventas con Factura Exenta

2

18

Sólo ventas con Factura Exenta

2

<TotIVANoRetenido>
26

Total Monto no facturable
<TotMntNoFact>

27

Total Monto Período
<TotMntPeriodo>

28

<TotPsjNac>
29

TOTAL EXENTO Venta de pasajes
Transporte internacional

NUM

<TotPsjInt>

Versión 3.0 - Marzo 2016

Pág. 17 de 45

Información Electrónica de Compras y Ventas

2.3. Resumen período para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328:
Obligatorio si Envío es TOTAL, FINAL O AJUSTE
En este resumen se deben entregar totalizados los montos por campo de cada tipo de documento de todo el período. También es obligatorio en el caso
de efectuar ajustes posteriores al cierre del período.
RESUMEN PERÍODO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO
MÁX.

1

TIPO DE DOCUMENTO

NUM

3

<TpoDoc>

2

CANTIDAD DE DOCUMENTOS

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

Para todos los tipos de documentos que se han informado en el mes.

*

1

*

1

Se debe agregar el resumen para los documentos correspondientes a Boletas y Resumen
pasajes Códigos (35, 38, 39, 41, 105, 500, 501, 919, 920, 922 y 924)
NUM

10

<TotDoc>

Cantidad de documentos del tipo especificado en el campo 1. Incluye anulados
Si tipo de documento es 35, 38, 39 y 41 se indica la cantidad de boletas emitidas en el mes.
En el caso del documento 919 y 924 (Resumen Pasajes) se anota la cantidad de pasajes que
se han vendido SIN FACTURA EXENTA
Cantidad de documentos cuyos folios han sido anulados, previo al envío al SII. Estos
documentos no se totalizan en los campos siguientes.

TOTAL ANULADOS
3

NUM

10

En el caso de los documentos manuales y de las Boletas Electrónicas , se registran todos los
folios anulados.

2

<TotAnulado>
No se contabiliza aquí si un documento electrónico ha sido anulado, posterior al envío al SII,
con Una Nota de Crédito o Debito. Esos documentos deben ser informados como emitidos,
con todos los datos que correspondan.

4

OPERACIONES CON MONTO EXENTO O
NO GRAVADO

NUM

10

<TotOpExe>

5

CAMPO PRÓXIMO A ELIMINARSE. Se mantiene para contribuyentes que están
informándolo.

3

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
3. En el caso de facturas exentas, este monto es igual al del campo 2. No se usa si tipo de
documento es 35, 38, 39, 41, 105, 500, 501, 919, 920, 922 y 924.

TOTAL MONTO EXENTO O NO GRAVADO NUM

18

Si no hay montos de este tipo, se debe registrar un 0

*

1

18

Si no hay montos de este tipo, se debe registrar un 0

*

1

18

Si no hay montos de este tipo, se debe registrar un 0

*

1

18

Sólo en Notas de Crédito.

<TotMntExe>
6

TOTAL MONTO NETO

NUM

<TotMntNeto>
7

TOTAL MONTO IVA

NUM

<TotMntIVA>
8

IVA fuera plazo

3

<TotIVAFueraPlazo>

Versión 3.0 - Marzo 2016

Pág. 18 de 45

Información Electrónica de Compras y Ventas

RESUMEN PERÍODO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

9

TOTAL IVA propio

NUM

18

Sólo cuando hay venta o servicio por cuenta de terceros

3

NUM

18

Sólo cuando hay venta o servicio por cuenta de terceros

3

NUM

18

Impuesto Zona Franca

2

<TotIVAPropio>
10

TOTAL IVA terceros
<TotIVATerceros>

11

TOTAL Ley 18211
<TotLey18211>
Tabla Tipos de Impuesto o recargo

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.

<TotOtrosImp>
12

Código del Impuesto o Recargo

18

Según lo informado en detalle

2

18

Totaliza los valores correspondiente al código por tipo de documento del detalle

2

10

CAMPO PRÓXIMO A ELIMINARSE. Se mantiene para contribuyentes que están
informándolo.

3

<CodImp>
13

Valor del Impuesto o Recargo
<TotMntImp>

14

OPERACIONES
TOTAL

CON

IVA

RETENIDO

NUM

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente. Sólo aplica para Factura de Compra recibidas

<TotOpIVARetTotal>

15

IVA Retenido Total

NUM

18

NUM

10

2

<TotIVARetTotal>
16

OPERACIONES
PARCIAL

CON

IVA

RETENIDO

<TotOpIVARetParcial>

17

CAMPO PRÓXIMO A ELIMINARSE. Se mantiene para contribuyentes que están
informándolo.

3

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente. Sólo aplica para Factura de Compra recibidas

IVA Retenido Parcial

NUM

18

2

NUM

18

2

NUM

18

2

<TotIVARetParcial>
18

TOTAL
CREDITO
ESPECIAL
EMPRESAS CONSTRUCTORAS

65%

<TotCredEC>
19

TOTAL Depósito envases
<TotDepEnvase>

Versión 3.0 - Marzo 2016

Pág. 19 de 45

Información Electrónica de Compras y Ventas

RESUMEN PERÍODO PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.
Totaliza por código para cada tipo de documento

Tabla Liquidaciones
<TotLiquidaciones>
20

TOTAL Valor Neto Comisiones y Otros Cargos

Puede ser negativo.
NUM

18

2

<TotValComNeto>
21

TOTAL Valor Comisiones y Otros Cargos no
Afectos o Exentos
NUM

Puede ser negativo.
18

2

<TotValComExe>
22

TOTAL IVA Comisiones y Otros Cargos

Puede ser negativo.
NUM

18

2

NUM

18

Totales de los documentos

NUM

10

CAMPO PRÓXIMO A ELIMINARSE. Se mantiene para contribuyentes que están
informándolo.

<TotValComIVA>
23

TOTAL MONTO TOTAL

*

1

<TotMntTotal>
24

OPERACIONES CON IVA NO RETENIDO
<TotOpIVANoRetenido>

3

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente. Sólo aplica para Factura de Compra recibidas
25

TOTAL IVA no retenido

NUM

18

2

NUM

18

Valor puede ser negativo

3

NUM

18

Valor puede ser negativo

3

NUM

18

Sólo ventas con Factura Exenta

2

NUM

18

Sólo ventas con Factura Exenta

2

<TotIVANoRetenido>
26

Total Monto no facturable
<TotMntNoFact>

27

Total Monto Período
<TotMntPeriodo>

28

TOTAL EXENTO Venta
Transporte nacional

de

pasajes

<TotPsjNac>
29

TOTAL EXENTO Venta de pasajes
Transporte internacional
<TotPsjInt>

Versión 3.0 - Marzo 2016

Pág. 20 de 45

Información Electrónica de Compras y Ventas

2.4.

Detalle para INFORMACIÓN ELECTRÓNICA DE VENTAS y F3328

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE

TIPO

1

TIPO DE DOCUMENTO

NUM

LARGO OBSERVACIONES
MÁX.
3

<TpoDoc>
2

EXCEPCION EMISOR/RECEPTOR

FOLIO (NUMERO DE DOCUMENTO)

OBLIGATORIEDAD

*

1

Todos los documentos, incluso los anulados.
NUM

1

<Emisor>
3

Ver codificación en el punto 4 de este documento. No se registran en el detalle los documentos
tipo resumen Códigos (35, 38, 39, 41, 105, 500, 501, 919, 920, 922 y 924).

(*)

Sólo aplica para Nota de Débito o de Crédito recibida por el contribuyente que genera el libro.

2

Se debe anotar un 1 si la Nota de Débito o Crédito afecta a Factura de Compra.
NUM

10

FOLIO.

A

1

= A (Anulado). Se registra en los documentos electrónicos cuando se ha anulado un folio que
no se ha enviado al SII. Aplica para todos los documentos no electrónicos que se anulen.

*

1

<NroDoc>
Folio Anulado
<Anulado>

2

Los documentos anulados sólo deben informar el “Tipo de Documento”, el “Folio (Numero de
Documento)” y este campo.

4

No se contabiliza aquí si un documento electrónico ha sido anulado, posterior al envío al SII,
con Una Nota de Crédito o Débito Electrónica. Esos documentos deben ser informados como
emitidos, con todos los datos que correspondan.
5

OPERACIÓN

NUM

1

<Operación>

Sólo en envíos de Ajuste

2

1= Agrega
2= Elimina
Si no se indica, se supone que es 1, folio a agregar.

6

Tasa Impuesto

NUM

5

3 enteros, 2 decimales. Se debe registrar la tasa del IVA o del DL 18.211

1

ALFA

10

Referencia del comprobante

3

NUM

1

<TasaImp>
7

NUMERO INTERNO
<NumInt>

8

9

10

<IndServicio>

1: Facturación de servicios periódicos domiciliarios
2: Facturación de otros servicios periódicos
3: Facturación de servicios no periódicos
Obligatorio en caso de servicios periódicos domiciliarios. Si es 1, el documento se debe
registrar en el mes en que se devenga el impuesto (según fecha de vencimiento).

Indicador Venta sin costo

Sólo Facturas

<IndSinCosto>

1: Entrega gratuita

Indicador Servicio periódico

FECHA DE DOCUMENTO

ALFA

8

AAAA-MM-DD (año, mes, día , separado por guiones)

2

2

1

<FchDoc>

Versión 3.0 - Marzo 2016

Pág. 21 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE

TIPO

LARGO OBSERVACIONES
MÁX.

11

CÓDIGO SUCURSAL

NUM

8

Sucursal donde se emitió el documento. Código numérico entregado por el SII, que identifica a
cada sucursal que está identificada en el Servicio de Impuestos Internos. Si no hay sucursales
se puede omitir. (Código registrado en el SII)

2

ALFA

10

Corresponde al Rut del receptor excepto en facturas de compra y Liquidaciones Facturas
recibidas como mandante, que corresponde al Rut del emisor. Con guión y dígito verificador.

1

ALFA

50

Es obligatorio en los documentos no electrónicos. En el resto es opcional.

2

ALFA

20

Para factura de exportación: Corresponde al número o código de identificación del receptor
extranjero. Se deben incluir guiones y dígitos verificadores

3

ALFA

3

Para factura de exportación: Corresponde a la nacionalidad del extranjero, de acuerdo al código
de País indicado en Tabla de Países de Aduana.

3

NUM

3

2

<TpoDocRef>

Este campo sólo se utiliza para Notas de Crédito que anulan una Factura o una Nota de Débito
en forma completa. Se debe indicar el tipo de documento anulado. Sólo es obligatorio si se ha
emitido en forma excepcional una Nota de Crédito no electrónica que anula una Factura
Electrónica. En otros casos es opcional.

Folio documento referencia

Folio anulado que ya se ha enviado al SII. Sólo válido si viene campo anterior

2

<CdgSIISucur>
12

RUT ASOCIADO (CLIENTE)
<RUTDoc>

13

NOMBRE O RAZON SOCIAL

(*)

OBLIGATORIEDAD

<RznSoc>
14

Número
identificador
extranjero

del

Receptor

<NumId>
15

Nacionalidad del Receptor Extranjero
<Nacionalidad>

16

17

Tipo de documento referencia

<FolioDocRef>
18

MONTO EXENTO O NO GRAVADO

NUM

18

2

NUM

18

2

<MntExe>
19

MONTO NETO
<MntNeto>

Versión 3.0 - Marzo 2016

Pág. 22 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE

TIPO

20

MONTO IVA

NUM

LARGO OBSERVACIONES
MÁX.
18

<MntIVA>

Es un dato obligatorio y debe corresponder al total de IVA del documento.

(*)

OBLIGATORIEDAD
1

Casos especiales
a) En los documentos exentos, el campo debe ir con un cero.
b) En Notas de Crédito fuera de plazo para rebajar el débito; se debe registrar el IVA registrado
en el documento. Este mismo dato se debe registrar en el campo siguiente, para considerar
que ese IVA no se debe descontar.
c) En casos de Venta por cuenta de terceros, se debe registrar el IVA expresado en el
documento en este campo, en forma obligatoria. Opcionalmente, el dato también se puede
registrar en los campos IVA Terceros y/o IVA propio.
d) Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación-Factura

21

IVA fuera plazo

18

IVA Propio

NUM

18

<IVAPropio>
23

IVA Terceros

2

En las Notas de Crédito que están fuera de plazo para rebajar el débito, se debe anotar el valor
completo del IVA en el campo anterior, pero el valor se debe registrar en este campo con el fin
de indicar el IVA que el emisor no debe descontar del débito.

<IVAFueraPlazo>

22

Sólo en Notas de Crédito que no deben descontar el débito por estar fuera de plazo.

Cuando se efectúan ventas por cuenta de terceros, se registra la parte del IVA que es propia.

3

Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación-Factura
NUM

18

<IVATerceros>

Cuando se efectúan ventas por cuenta de terceros, se registra la parte del IVA que es
responsabilidad de terceros y que se traspasará por una Liquidación.

3

Monto IVA = IVA propio + IVA Terceros
Puede ser negativo sólo si el tipo de documento es Liquidación-Factura
24

Ley 18211

NUM

18

Impuesto Zona Franca

2

<Ley18211>
Tabla Tipos de Impuesto o recargo

Según tabla número 7. Los siguientes 3 campos. Hasta 20 posibles ocurrencias.

<OtrosImp>

No se debe usar códigos de IVA Retenido (según tipo de producto códigos 30 al 41 ) en
Facturas de Compra recibidas. Estos datos van sólo en los Campos IVA Retenido Total e IVA
Retenido parcial.
Se debe usar códigos por Retención anticipo por Cambio de sujeto en facturas de venta
emitidas (códigos 15, 17)

25

Código del Impuesto o Recargo

3

Según tabla número 7.

2

5

Según tabla número 7.

2

<CodImp>
26

Tasa del Impuesto o Recargo
<TasaImp>

Versión 3.0 - Marzo 2016

3 enteros, 2 decimales.

Pág. 23 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE

TIPO

LARGO OBSERVACIONES
MÁX.

27

Valor del Impuesto o Recargo

NUM

18

NUM

18

(*)

OBLIGATORIEDAD
2

<MntImp>
28

IVA Retenido Total
<IVARetTotal>

Sólo Facturas de compra recibidas cod (45, 46) y Notas de Crédito y Débito asociadas.
Se genera según la tasa del IVA Retenido.

2

- Si la tasa de retención es por el Total del IVA, el valor de la retención debe estar en este
campo.
29

IVA Retenido Parcial

NUM

18

<IVARetParcial>

Sólo Facturas de compra recibidas cod. (45, 46) y Notas de Crédito y Débito asociadas.
Se genera según la tasa del IVA Retenido.

2

- Si la tasa de retención es menor al Total del IVA, el valor de la retención debe ir en este
campo.
30

Crédito 65% Empresas Constructoras

NUM

18

Según Artículo 21 del Decreto Ley N° 910/75

2

NUM

18

Depósito por envases

3

<CredEC>
31

Garantía Dep.Envases
<DepEnvase>
Tabla Liquidaciones

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.
Totaliza por código para cada tipo de documento

<Liquidaciones>
32

RUT EMISOR

ALFA

10

<RutEmisor>

Con guion y dígito verificador. Sólo para registrar el Rut del emisor de Liquidaciones y
Liquidaciones-Factura, tanto electrónicas como manuales.

2

Su registro es obligatorio para Liquidaciones y Liquidaciones-Factura, tanto electrónica
como manuales, recibidas (códigos 40, 43 y 103).
Para Liquidaciones y Liquidaciones-Factura, tanto electrónicas como manuales, emitidas el
registro es opcional.
33

TOTAL Valor Neto Comisiones y Otros
Cargos

Puede ser negativo.
NUM

18

2

<ValComNeto>
34

TOTAL Valor Comisiones y Otros Cargos no
Afectos o Exentos

Puede ser negativo.
NUM

18

NUM

18

2

<ValComExe>
35

TOTAL IVA Comisiones y Otros Cargos

Puede ser negativo.
2

<ValComIVA>

Versión 3.0 - Marzo 2016

Pág. 24 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE VENTAS Y F3328
N°

NOMBRE

TIPO

36

MONTO TOTAL

NUM

LARGO OBSERVACIONES
MÁX.
18

<MntTotal>

(*)

Monto neto + Monto no afecto o exento + IVA + Impuestos Adicionales + Retención anticipo+
IVA anticipado + Garantía por depósito de envases o embalajes - Crédito empresas
constructoras - IVA Retenido, parcial y total (en caso de facturas de compra, Notas de Crédito
y Débito asociadas) – Impuesto Retenido Factura de Inicio – Valor Comisiones y Otros Cargos
no Afectos o Exentos – Valor Neto Comisiones y Otros Cargos – Valor IVA Comisiones y Otros
Cargos

OBLIGATORIEDAD
1

Se obtiene del monto total del documento, excluidos los no facturables y el saldo anterior.
Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación-Factura
37

IVA no retenido

NUM

18

<IVANoRetenido>
38

Total Monto no facturable

IVA no retenido= Monto IVA -IVA retenido parcial- IVA Retenido Total

2

Sólo Facturas de compra recibidas cód. (45, 46) y Notas de Crédito y Débito asociadas.
NUM

18

Valor puede ser negativo

3

NUM

18

Valor puede ser negativo

3

NUM

18

Sólo ventas con Factura Exenta

2

NUM

18

Sólo ventas con Factura Exenta

2

<MntNoFact>
39

Total Monto Período
<MntPeriodo>

40

Venta de pasajes Transporte nacional
<PsjNac>

41

Venta de pasajes Transporte internacional
<PsjInt>

Versión 3.0 - Marzo 2016

Pág. 25 de 45

Información Electrónica de Compras y Ventas

2.5. Certificado de Autorización de Libros (CAL) – Libros Contables Electrónicos (NO APLICA PARA DJ3327 Y3328)
El Certificado de Autorización de Libros (CAL) es otorgado por el SII al Rut que ha efectuado las pruebas.
A través de la entrega del CAL, el SII confirma que ese contribuyente es capaz de generar el respectivo Libro Contable Electrónico.
N°

CAMPO

OBLIG

TIPO

LARGO
MAX

DESCRIPCIÓN

1

Rut Distribuidor

1

R

10

Rut de quien ha efectuado las pruebas de formato de los Libros en el SII. Este rut puede
pertenecer a un contribuyente de primera o segunda categoría.

2

Tipo certificado

C: Certificación. Se utiliza para efectuar las pruebas de archivos
P: Producción. Lo entrega el SII, una vez que se hayan efectuado las pruebas respectivas.

3

Clase

1: Contribuyente. Sólo para su propio uso. Este CAL no se puede endosar
2: Holding. Para uso de quien lo obtuvo y para empresas del holding. Este CAL es endosable.
3: Empresa Software: Este CAL es endosable y vence anualmente.

4

Tipo del Libro Contable

1

N

4

1: Contable. Incluye, Diario, Mayor, Balance
Compra
6: Compra y Venta
Según Tabla 2 de Anexos

5

Fecha Emisión

1

A

10

Fecha en que el SII emite el CAL. En forma AAAA-MM-DD

6

Período Vigencia

1

N

4

Año en que es válido hacer envíos con este CAL.
Si es de Clase 1 y 2, indica que a partir de ese año puede hacer envíos obligatorios.
Si es de Clase 3, se debe renovar el CAL cada año ya que sólo puede hacer envíos obligatorios
el año del período de vigencia.

7

Fecha Firma

1

A

19

Fecha y Hora de la Firma de este documento. En formato AAAA-MM-DDTHH:MI:SS

8

Firma Electrónica

1

XML

Firma Electrónica sobre este documento.

2.6. Comprobante de Certificación (COCERTIF) – Libros Contables Electrónicos (NO APLICA PARA DJ3327 Y3328)
El COCERTIF es utilizado por contribuyentes que no han efectuado las pruebas de archivos, directamente en el SII.
Corresponde a un CAL tipo 2 o 3, el cual es endosado.
N°

CAMPO

OBLIG

TIPO

1

Rut Contribuyente

1

R

2

Fecha Emisión

1

A

3

CAL

1

XML

4

Rut Firmante del Endosante 1

A

10

Rut de firmante autorizado por el Distribuidor a firmar este tipo de documentos.

5

Fecha Firma

1

A

19

Fecha y Hora de la Firma de este documento. En formato AAAA-MM-DDTHH:MI:SS.

6

Firma Electrónica

1

XML

Versión 3.0 - Marzo 2016

LARGO MAX
DESCRIPCIÓN
Rut del contribuyente al que se le endosa el CAL.
10

Fecha de Emisión del COCERTIF.Formato AAAA-MM-DD
Certificado de Autorización del Libro (CAL)

Firma Electrónica sobre este documento.

Pág. 26 de 45

Información Electrónica de Compras y Ventas

3.- INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327
3.1.Carátula para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327
CARÁTULA PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3327
N°

NOMBRE DEL CAMPO

TIPO LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

1

RUT Contribuyente

ALFA

10

Corresponde al Rut del contribuyente emisor con guión y dígito verificador

*

1

ALFA

10

Corresponde al Rut del usuario autorizado que hace el envío al SII

*

1

ALFA

7

Periodo Tributario, en formato AAAA-MM (Año (4),Mes (2))

<RutEmisorLibro>
2

RUT Enviador
<RutEnvia>

3

PERIODO TRIBUTARIO

1

Si “tipo de Libro” es ESPECIAL y abarca más de un período se debe indicar la fecha del primer
período tributario.

<PeriodoTributario>

Para la DJ3327:
Periodo Tributario, en formato AAAA-MM (Año (4),Mes (2)).
Debe indicarse el período del libro enviado. Se debe enviar un libro por cada período.
4

Fecha Resolución

ALFA

10

AAAA-MM-DD

*

1

*

1

<FchResol>
Para la DJ3327: Debe ser de valor fijo: 2006-01-20
5

Número Resolución

NUM

6

Para la DJ3327: Debe ser de valor fijo 102006

<NroResol>
6

Tipo de Operación

Número de Resolución que autoriza al contribuyente como emisor electrónico.

ALFA

6

=COMPRA

*

1

ALFA

8

MENSUAL (Corresponde a los libros Regulares)

*

1

<TipoOperacion>
7

Tipo de Libro
<TipoLibro>

ESPECIAL (Corresponde a un libro solicitado vía una notificación)
Para la DJ3327: ESPECIAL

8

Tipo de Envío
<TipoEnvio>

ALFA

7

TOTAL: información total del mes. Si no se incluye, se asume que es total.
PARCIAL: Segmento parcial: tiene
FINAL: Corresponde al último segmento

parte

de

la

información

2
del

período

AJUSTE : Movimientos ingresados con posterioridad al envío final

Versión 3.0 - Marzo 2016

Pág. 27 de 45

Información Electrónica de Compras y Ventas

CARÁTULA PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3327
N°

NOMBRE DEL CAMPO

TIPO LARGO
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

9

Número de Segmento

NUM

3

Número del segmento. Sólo si el TIPO DE ENVÍO es PARCIAL

2

NUM

10

Folio de notificación. Obligatorio si es un tipo de envío ESPECIAL

2

<NroSegmento>
10

Folio de Notificación
<FolioNotificacion>

11

Código de Autorización de Reemplazo de
Libro Electrónico.
<CodAutRec>

Para la DJ3327: Debe ser de valor fijo: 102006
ALFA

10

Código de Autorización de Reemplazo de Libro Electrónico, obtenido por el Representante
Legal para permitir el reemplazo de un libro recibido OK por SII para un período y tipo de
libro específico.

2

Para la DJ3327: No Aplica

Versión 3.0 - Marzo 2016

Pág. 28 de 45

Información Electrónica de Compras y Ventas

3.2. Resumen segmento para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3327
En este resumen se deben entregar totalizados los montos por campo de cada tipo de documento, para los documentos incluidos en el detalle.
Todos los montos pueden ser negativos así como también el campo “cantidad de documentos” que puede ser negativo en un envío de ajuste.

RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3327
N°

NOMBRE DEL CAMPO

TIPO

LARG
O
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

1

TIPO DE DOCUMENTO

NUM

3

Para todos los tipos de documentos que se informan en el detalle

*

1

NUM

1

1: IVA

<TpoDoc>
2

TIPO DE IMPUESTO
<TpoImp>

2

2: Ley 18.211. Se usa para documentos de Zona Franca. Tipo de Documento 108 (SRF)
Si se omite se asume 1.

3

CANTIDAD DE DOCUMENTOS

NUM

10

<TotDoc>

Cantidad de documentos del tipo especificado en el campo 1 con el tipo de Impuesto indicado en el
campo 2. Incluye anulados.

*

1

Sólo Facturas de Compra emitidas, Notas de Crédito y Débito relacionadas a Factura de Compra
emitidas
Cantidad de Documentos Electrónicos señalados cuyos folios han sido anulados, previo al envío al SII.
Estos documentos no se totalizan en los campos siguientes.

TOTAL ANULADOS
4

NUM

10

<TotAnulado>

2
En el caso de los documentos manuales se registran todos los folios anulados.
No se contabiliza aquí si una Factura de Compra electrónica ha sido anulada, posterior al envío al SII,
con una Nota de Crédito. Esos documentos deben ser informados como emitidos, con todos los datos
que correspondan.

5

OPERACIONES CON MONTO EXENTO O
NO GRAVADO

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo siguiente

3

NUM

18

Suma de monto exento de todos los documentos registrados en el detalle

*

1

NUM

18

Suma del monto neto de todos los documentos registrados en el detalle. Incluye el Monto Neto de
Activo Fijo.

*

1

<TotOpExe>
6

TOTAL MONTO EXENTO O NO
GRAVADO
<TotMntExe>

7

TOTAL MONTO NETO
<TotMntNeto>

Versión 3.0 - Marzo 2016

Pág. 29 de 45

Información Electrónica de Compras y Ventas

RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3327
N°

NOMBRE DEL CAMPO

TIPO

LARG
O
MÁX.

OBSERVACIONES GENERALES

(*)

OBLIGATORIEDAD

8

OPERACIONES CON IVA RECUPERABLE

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo siguiente

NUM

18

Suma del monto IVA recuperable de todos los documentos registrados en el detalle. Si el tipo de
impuesto es 2, significa crédito por Ley 18.211

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo siguiente

3

NUM

18

Si la compra es de Activo Fijo, se debe indicar la parte del Monto Neto que corresponde a Activo Fijo.

3

NUM

18

Suma del monto IVA de todos los documentos registrados en el detalle.

3

3

<TotOpIVARec>
9

TOTAL MONTO IVA (recuperable)
<TotMntIVA>

10

OPERACIONES ACTIVO FIJO

*

1

<TotOpActivoFijo>
11

MONTO NETO ACTIVO FIJO
<TotMntActivoFijo>

12

TOTAL MONTO IVA ACTIVO FIJO
<TotMntIVAActivoFijo>
Tabla IVA no recuperable

Contiene los dos campos siguientes. Se totaliza por código

<TotIVANoRec>
1: Compras destinadas a IVA a generar operaciones no gravadas o exentas.

13 Código No recuperable

2

2: Facturas de proveedores registradas fuera de plazo.

<CodIVANoRec>

3: Gastos rechazados
4: Entregas gratuitas (premios, bonificaciones, etc.) recibidas.
9: Otros

14

OPERACIONES
RECUPERABLE

CON

IVA

NO

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo siguiente

3

NUM

18

Suma de Montos de IVA correspondiente a la operación codificada en campo anterior. Si el tipo de
impuesto es 2, significa crédito por Ley 18.211.

2

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en la tabla siguiente.

3

NUM

18

Suma. Si el tipo de impuesto es 2, significa crédito por Ley 18.211.

2

<TotOpIVANoRec>
15

Monto IVA No Recuperable
<TotMntIVANoRec>

16

OPERACIONES CON IVA USO COMUN
<TotOpIVAUsoComun>

17

IVA USO COMUN
<TotIVAUsoComun>

Versión 3.0 - Marzo 2016

Pág. 30 de 45

Información Electrónica de Compras y Ventas

RESUMEN SEGMENTO PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3327
N°

NOMBRE DEL CAMPO

TIPO

LARG
O
MÁX.

<TotOtrosImp>
Código del Impuesto o Recargo

(*)

OBLIGATORIEDAD

Contiene los dos campos siguientes. Hasta 20 posibles ocurrencias.
Según Tabla de códigos de Impuesto, utilizada en los DTE. Ver N ° 7 del Índice.
Incluye también código para retenciones de IVA por tipo de producto.

Tabla Tipos de Impuesto o recargo

18

OBSERVACIONES GENERALES

NUM

10

2

NUM

18

Totaliza los valores correspondiente al código por tipo de documento del detalle

2

NUM

18

Totaliza los valores del detalle

3

NUM

18

Suma de los montos totales de las operaciones registradas en el detalle

<CodImp>
19

Valor del Impuesto o Recargo
<TotMntImp>

20

Impuesto sin Derecho a crédito
<TotImpSinCredito>

21

TOTAL MONTO TOTAL

*

1

<TotMntTotal>
22

IVA no retenido
<TotIVANoRetenido>

NUM

18

Sólo para Facturas de Compra

2

23

TABACOS MANUFACTURADOS (Cigarros
puros)

NUM

18

Valor neto. Sólo para el importador

2

NUM

18

Valor neto. Sólo para el importador

2

NUM

18

Valor neto. Sólo para el importador

2

<TotTabPuros>
24

TABACOS MANUFACTURADOS
(Cigarrillos)
<TotTabCigarrillos>

25

TABACOS MANUFACTURADOS (Tabaco
elaborado)
<TotTabElaborado>

Versión 3.0 - Marzo 2016

Pág. 31 de 45

Información Electrónica de Compras y Ventas

3.3. Resumen período INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3328
Obligatorio si Tipo Envío es TOTAL, FINAL O AJUSTE
En el resumen se deben entregar totalizados los montos por campo de cada tipo de documentos de todo el período. También es obligatorio en el caso de
efectuar ajustes posteriores al cierre del período.
RESUMEN PERÍODO INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO

OBSERVACIONES

(*)

OBLIGATORIEDAD

1

TIPO DE DOCUMENTO

NUM

3

Para todos los tipos de documentos que se han informado en el periodo

*

3

NUM

1

1: IVA
2: Ley 18.211. Se usa para documentos de Zona Franca. Tipo de Documento 108 (SRF)
Si se omite se asume 1.

NUM

10

Cantidad de documentos del tipo especificado en el campo anterior. Incluye anulados

<TpoDoc>
2

TIPO DE IMPUESTO
<TpoImp>

3

CANTIDAD DE DOCUMENTOS

2

*

1

<TotDoc>
Sólo Facturas de Compra emitidas, Notas de Crédito y Débito relacionadas a Factura de
Compra emitidas
Cantidad de Documentos Electrónicos señalados cuyos folios han sido anulados, previo al
envío al SII. Estos documentos no se totalizan en los campos siguientes.

TOTAL ANULADOS
4

NUM

10

<TotAnulado>

2
En el caso de los documentos manuales se registran todos los folios anulados.
No se contabiliza aquí si una Factura de Compra electrónica ha sido anulada, posterior al
envío al SII, con una Nota de Crédito. Esos documentos deben ser informados como emitidos,
con todos los datos que correspondan.

5

OPERACIONES CON MONTO EXENTO O
NO GRAVADO

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente

3

NUM

18

NUM

18

Suma del Monto Neto del período. Incluye el Monto de Activo Fijo.

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente

3

NUM

18

Totales del período

1

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente

3

<TotOpExe>
6

MONTO EXENTO O NO GRAVADO

*

2

*

2

<TotMntExe>
7

MONTO NETO
<TotMntNeto>

8

OPERACIONES IVA RECUPERABLE
<TotOpIVARec>

9

MONTO IVA (RECUPERABLE)
<TotMntIVA>

10

OPERACIONES ACTIVO FIJO
<TotOpActivoFijo>

Versión 3.0 - Marzo 2016

Pág. 32 de 45

Información Electrónica de Compras y Ventas

RESUMEN PERÍODO INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO

11

MONTO NETO ACTIVO FIJO

NUM

18

<TotMntActivoFijo>

OBSERVACIONES
Se calcula de dos formas posibles

(*)

OBLIGATORIEDAD
3

a) Si viene información en detalle, es igual a la suma de los valores.
b) Puede venir información en este campo aun cuando no se haya informado en el Detalle

12

TOTAL MONTO IVA ACTIVO FIJO

NUM

18

Se calcula de dos formas posibles

3

a) Si viene información en detalle, es igual a la suma de los valores.

<TotMntIVAActivoFijo>

b) Monto Neto* Tasa IVA

Contiene los dos campos siguientes. Hasta 5 posibles ocurrencias.

Tabla IVA no recuperable
<TotIVANoRec>
13

Código No recuperable

1

<CodIVANoRec>

1: Compras destinadas a IVA a generar operaciones no gravados o exentas.

2

2: Facturas de proveedores registradas fuera de plazo.
3: Gastos rechazados
4: Entregas gratuitas (premios, bonificaciones, etc ) recibidas
9: Otros

14

OPERACIONES IVA NO RECUPERABLE

NUM

10

Cantidad de documentos en que se ha registrado Montos del tipo especificado en el campo
siguiente

3

NUM

18

Suma de Montos de IVA correspondiente a la operación codificada en tabla anterior.

2

NUM

10

Cantidad de documentos en que se han registrado Montos del tipo especificado en siguiente
campo

3

NUM

18

Totales del período

2

NUM

6

Informa sobre el factor que se aplica al IVA Uso Común. Se calcula como total para el
período, pero se aplica por tipo de documento.

2

NUM

18

Factor proporcionalidad IVA * Total IVA Uso común

2

<CodIVANoRec>
15

Monto IVA No Recuperable
<TotOpIVANoRec>

16

OPERACIONES CON IVA USO COMUN
<TotOpIVAUsoComun>

17

IVA USO COMUN
<TotIVAUsoComun>

18

Factor proporcionalidad IVA
<FctProp>

19

TOTAL CREDITO IVA COMUN
<TotCredIVAUsoComun>

Contiene los cuatro campos siguientes. Hasta 20 posibles ocurrencias.
Según Tabla de códigos de Impuesto, utilizada en los DTE. Ver N°7 del Índice
Incluye también código para retenciones de IVA por tipo de producto.

Tabla Tipos de Impuesto o recargo
<TotOtrosImp>
20

Código del Impuesto o Recargo

NUM

18

2

<CodImp>
Versión 3.0 - Marzo 2016

Pág. 33 de 45

Información Electrónica de Compras y Ventas

RESUMEN PERÍODO INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL CAMPO

TIPO

LARGO

21

Valor del Impuesto o Recargo

NUM

18

OBSERVACIONES

(*)

OBLIGATORIEDAD

Totaliza los valores correspondiente al código por tipo de documento del detalle

2

Factor de proporcionalidad para ILA. Valor mayor que 0 y menor que 1. Sólo si el
contribuyente es minorista y ocasionalmente vende a otros vendedores. Indica la proporción
entre venta mayorista y minorista. Se calcula como total para el período, pero se aplica por
tipo de documento.
Cuando existe valor en Factor Impuesto adicional, se calcula como:
Factor impuesto adicional* IMPUESTO ART. 42 (Según código)
En otros casos es igual a Valor del Impuesto o Recargo

2

3

<TotMntImp>
22

Factor impuesto adicional
<FctImpAdic>

23

CREDITO IMPUESTO

18

NUM

18

Totaliza los valores del detalle

NUM

18

Totales del período

NUM

18

Totales del período

2

NUM

18

ART. 3 DL 828

2

NUM

18

ART. 4 DL 828

2

NUM

18

ART. 5 DL 828

2

NUM

18

Art 64 (46) D.L.824/74. Conjuntos de partes o Piezas para desarmaduría o Ensamblaje y de
automóviles semiterminados

2

<TotCredImp>
24

Impuesto sin Derecho a crédito

2

NUM

<TotImpSinCredito>
25

MONTO TOTAL

*

1

<TotMntTotal>
26

IVA no retenido
<TotIVANoRetenido>

27

TABACOS (Cigarros puros)
<TotTabPuros>

28

TABACOS (Cigarrillos)
<TotTabCigarrillos>

29

TABACOS (Tabaco elaborado)
<TotTabElaborado>

30

Impuesto a Los Vehículos Automóviles
<TotImpVehiculo>

Versión 3.0 - Marzo 2016

Pág. 34 de 45

Información Electrónica de Compras y Ventas

3.4.

Detalle para INFORMACIÓN ELECTRÓNICA DE COMPRAS y F3328

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL
CAMPO

TIPO

LARG
O

1

TIPO
DOCUMENTO

OBSERVACIONES

(*)

OBLIGATORIEDAD

DE

NUM

3

De acuerdo a codificación que se incluye en el punto 4 de este documento

*

1

EXCEPCION
EMISOR/RECEPTOR

NUM

1

Sólo aplica para Nota de Débito o de Crédito emitida por el contribuyente que genera el libro.

<TpoDoc>
2

2

Se debe anotar un 1 si la Nota de Débito o Crédito afecta a una Factura de Compra.

<Emisor>
3

FOLIO (NUMERO DE
DOCUMENTO)

NUM

10

Folio del documento

ALFA

1

= A (Sólo en Facturas de Compra anuladas y Notas de Crédito y Débito relacionadas a Factura de Compra, y aplica
para Factura de Compra Electrónica y Notas de Crédito y Débito Electrónicas relacionadas a Factura de Compra cuyos
folios han sido anulados, previo al envío al SII).

*

1

<NroDoc>
4

ANULADO
<Anulado>

2

Los documentos anulados sólo deben informar el “Tipo de Documento”, el “Folio (Numero de Documento)” y este
campo.
No se contabiliza aquí si un documento electrónico ha sido anulado, posterior al envío al SII, con Una Nota de
Crédito o Debito Electrónica. Esos documentos deben ser informados como emitidos, con todos los datos que
correspondan.
5

OPERACIÓN

NUM

1

<Operacion>

2

1 = Agrega
2 = Elimina
Si no se indica, se supone que es 1 (folio a agregar). Sólo en envíos tipo Ajuste

6

TIPO DE IMPUESTO

NUM

1

<TpoImp>

1: IVA

2

2: Ley 18.211. Se usa para documentos de Zona Franca. Tipo de Documento 108 (SRF)
Si se omite se asume 1.

7

Tasa Impuesto

NUM

5

3 enteros, 2 decimales. Se debe registrar la tasa ya sea del IVA o de Impuesto Ley 18.211 según corresponda
a la operación

1

NUM

10

Número del comprobante contable

3

ALFA

8

AAAA-MM-DD (año , mes , día, separados por guiones)

1

<TasaImp>
8

NUMERO INTERNO
<NumInt>

9

FECHA
DOCUMENTO

DE

<FchDoc>

Versión 3.0 - Marzo 2016

Pág. 35 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL
CAMPO

TIPO

LARG
O

10

CÓDIGO SUCURSAL

NUM

8

Sucursal donde se emitió el documento. Código numérico entregado por el SII, que identifica a cada sucursal que está
identificada en el Servicio de Impuestos Internos. Si no hay sucursales se puede omitir. (Código registrado en el SII)

2

ALFA

10

Rut del proveedor. Con guión y dígito.

1

ALFA

50

Obligatorio sólo en los documentos NO ELECTRÓNICOS

2

NUM

18

Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación Factura

2

NUM

18

Todos los documentos. Incluye el Monto ACTIVOFIJO.

2

<CdgSIISucur>
11

RUT
ASOCIADO
PROVEEDOR

OBSERVACIONES

(*)

OBLIGATORIEDAD

<RUTDoc>
12

NOMBRE O RAZON
SOCIAL
<RznSoc>

13

MONTO EXENTO O
NO GRAVADO
<MntExe>

14

MONTO NETO
<MntNeto>

15

Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación Factura

MONTO
IVA
(RECUPERABLE)

NUM

18

1

IVA con derecho a crédito
En el caso de una compra con crédito Empresa constructora, se debe registrar el 100% del IVA.

<MntIVA>

El IVA total de la operación se descompone en:
Tasa IVA * Monto neto = Monto IVA Recuperable + IVA no recuperable + IVA uso común
Si en un documento no hay IVA recuperable debe venir con cero.
Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación Factura

16

MONTO
ACTIVO FIJO

NETO

NUM

18

Monto NETO activo fijo. Este monto está incluido en el Campo Monto Neto. Se registra adicionalmente en este campo.

3

NUM

18

Monto IVA activo fijo.

3

<MntActivoFijo>
17

IVA ACTIVO FIJO

Cuando hay compra de Activo Fijo, el valor del IVA, se registra en el campo “IVA Recuperable y también
opcionalmente en este campo.

<MntIVAActivoFijo>

Tabla
IVA
recuperable

no

Contiene los dos campos siguientes. Hasta 5 posibles ocurrencias.

<IVANoRec>

Versión 3.0 - Marzo 2016

Pág. 36 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL
CAMPO

TIPO

18

Código No recuperable

LARG
O
1

<CodIVANoRec>

OBSERVACIONES

(*)

OBLIGATORIEDAD

1: Compras destinadas a IVA a generar operaciones no gravados o exentas.

2

2: Facturas de proveedores registradas fuera de plazo.
3: Gastos rechazados
4: Entregas gratuitas (premios, bonificaciones etc.) recibidas.
9: Otros

19

Monto
IVA
Recuperable

No

NUM

18

Monto de IVA correspondiente a la operación codificada en campo anterior.

2

NUM

18

Compras que, a diferencia de los dos casos anteriores, están destinadas en parte a a ventas afectas y en parte a
ventas exentas. Se indica en este campo porque la determinación de la parte exenta y afecta solo se puede
hacer al finalizar el período tributario.

2

<MntIVANoRec>
20

IVA USO COMUN
<IVAUsoComun>
Tabla
Tipos
de
Impuesto o recargo

Contiene los tres campos siguientes. Hasta 20 posibles ocurrencias.
Según Tabla de códigos de Impuesto, utilizada en los DTE. Ver N°7 del Índice.
Incluye también código para retenciones de IVA por tipo de producto.

<OtrosImp>
21

Código del Impuesto o
Recargo

18



<CodImp>

22

Según tabla número 7.



Tasa del Impuesto

5

<TasaImp>

2

En el caso de Facturas de Compra se deben utilizar los códigos (30 al 41) asociados a retenciones y códigos de
retención total asociados (301, 321, 331, etc.)
Si la factura de Compra emitida es de retención total y no corresponde a ningún cambio de sujeto, se debe usar
el código 15 Retención Total.

Según tabla número 7. En el caso de Facturas de compra emitidas se debe indicar la tasa de retención. Si se retuvo
el total del impuesto se debe indicar el mismo valor de la tasa del impuesto.

2

3 enteros, 2 decimales
23

Valor del Impuesto o
Recargo con derecho a
crédito

18



<MntImp>
24

Impuestos sin derecho
a crédito

NUM

18

<MntSinCred>
25

MONTO TOTAL



2

En el caso de Impuesto adicional, registrar sólo si el contribuyente tiene derecho a crédito. Artículos 37 y 40 del
Decreto Ley N° 825/74. Si no tiene derecho al crédito, los impuestos adicionales pagados deben ir en el campo
siguiente, fuera de la tabla.
En el caso de Impuestos retenidos, se debe indicar la parte retenida

Totalizar el impuesto registrado en documentos que no da derecho a crédito para ese contribuyente

2

Art 37 Letras a, b y c + Art 37 letras e, h, I, l+ Art 37 Letras j+ Art 42.+ Impuestos diesel (si no hay derecho al crédito)
+ Impuesto gasolina(siempre)
Este dato se incluye para asegurar la cuadratura con el Monto Total

NUM

18

<MntTotal>

Monto Neto + Monto Exento + IVA recuperable + IVA Uso común + IVA no recuperable + IVA adicional + IVA anticipado
+ Garantía envases - IVA retenido parcial y total – Impuesto Retenido Factura de Inicio + Impuestos adicionales + IVA
Margen comercialización + Impuestos sin derecho a crédito.

1

Puede ser negativo sólo si el tipo de documento es Liquidación o Liquidación Factura
26

IVA no retenido
<IVANoRetenido>

Versión 3.0 - Marzo 2016

NUM

18

2

Corresponde a la diferencia entre el IVA total y el IVA Retenido parcial.
Se usa sólo en Facturas de Compra emitidas y Notas de Crédito y Débito asociadas
Pág. 37 de 45

Información Electrónica de Compras y Ventas

DETALLE PARA INFORMACIÓN ELECTRÓNICA DE COMPRAS Y F3328
N°

NOMBRE DEL
CAMPO

TIPO

LARG
O

OBSERVACIONES

(*)

OBLIGATORIEDAD

27

TABACOS
puros)

(Cigarros

NUM

18

ART. 3 DL 828

2

TABACOS (Cigarrillos)

NUM

18

ART. 4 DL 828

2

NUM

18

ART. 5 DL 828

2

NUM

18

Art 64 (46) D.L.824/74. Conjuntos de partes o Piezas para desarmaduría o Ensamblaje y de automóviles
semiterminados

2

<TabPuros>
28

<TabCigarrillos>
29

TABACOS
elaborado)

(Tabaco

<TabElaborado>
30

Impuesto
a
Los
Vehículos Automóviles
<ImpVehiculo>

Versión 3.0 - Marzo 2016

Pág. 38 de 45

Información Electrónica de Compras y Ventas

4.- CÓDIGOS DE DOCUMENTOS
4.1 De Ventas
Los documentos marcados con una X en la columna SOLO EN RESUMEN, solo se informan en el resumen del libro
totalizadas para el período.
ARCHIVO
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV
IEV

CÓDIGO
29
30
32
33
34
35
38
39
40
41
43
45
46
47
48
55
56
60
61
101
102
103
104
105
106
108
109
110
111
112
901
902
903
919
920
922
924

Versión 3.0 - Marzo 2016

NOMBRE DEL DOCUMENTO
Factura de Inicio
Factura
Factura de ventas y servicios no afectos o exentos de IVA
Factura Electrónica
Factura no Afecta o Exenta Electrónica
Boleta de Ventas y Servicios (afecta)
Boleta de Ventas y Servicios no afectos o exentos de IVA
Boleta electrónica (de Ventas y Servicios - afecta)
Liquidación factura
Boleta no afecta o exenta electrónica (de Ventas y Servicios)
Liquidación-Factura Electrónica
Factura de Compra
Factura de Compra electrónica.
Vale Electrónico
Comprobante de Pago Electrónico
Nota de débito
Nota de débito electrónica
Nota de Crédito
Nota de crédito electrónica
Factura de exportación
Factura de venta exenta a zona franca primaria (Res.Ex. N° 601, del 07.05.82)
Liquidación
Nota de débito de exportación
Boleta liquidación (Res. Ex. N° 1423 del 23.12.76)
Nota de Crédito de exportación
SRF Solicitud Registro de Factura
Factura a turista (Res. Ex. N° 6428 de 06.12.93)
Factura de Exportación Electrónica
Nota de Débito de Exportación Electrónica
Nota de Crédito de Exportación Electrónica
Factura de ventas a empresas del territorio preferencial ( Res. Ex. N°1057, del 25.04.85)
Conocimiento de Embarque (Marítimo o aéreo)
Documento único de Salida (DUS)
Resumen ventas de nacionales pasajes sin Factura
Otros registros no documentados Aumenta débito
Otros registros. Disminuye débito.
Resumen ventas de internacionales pasajes sin Factura.

SOLO EN RESUMEN

X
X
X
X

X
X

X

X
X
X
X

Pág. 39 de 45

Información Electrónica de Compras y Ventas

4.2 De Compras

ARCHIVO CÓDIGO

NOMBRE DEL DOCUMENTO

IEC

29

Factura de Inicio

IEC

30

Factura

IEC

32

IEC

33

Factura de ventas y servicios no afectos o exentos de IVA
Factura Electrónica

IEC
IEC

34
40

IEC

43

IEC

45

IEC

46

IEC

55

IEC

56

IEC

60

IEC

61

Nota de Crédito
Nota de Crédito Electrónica

IEC

108

SRF Solicitud de Registro de Factura

IEC

901

Factura de ventas a empresas del territorio preferencial ( Res. Ex. N° 1057, del 25.04.85)

IEC

914

Declaración de Ingreso (DIN)

IEC

911

Declaración de Ingreso a Zona Franca Primaria.

Versión 3.0 - Marzo 2016

Factura No Afecta o Exenta Electrónica
Liquidación Factura
Liquidación Factura Electrónica
Factura de Compra
Factura de Compra electrónica
Nota de Débito
Nota de Débito Electrónica

Pág. 40 de 45

Información Electrónica de Compras y Ventas

5.- CÓDIGOS DE DOCUMENTOS ZONA FRANCA Y MERCADERÍAS NO NACIONALES
5.1. Información electrónica de Ventas
USUARIOS DE ZONA FRANCA
IEV

904

Factura de Traspaso

IEV

905

Factura de Reexpedición

IEV

906

Boletas Venta Módulos ZF (todas)

IEV

907

Facturas Venta Módulo ZF (todas)

5.2. Información electrónica de Compras
USUARIOS DE ZONA FRANCA
IEC

904

Factura de Traspaso

IEC

909

Facturas Venta Módulo ZF

IEC

910

Solicitud Traslado Zona Franca (Z)

IEC

911

Declaración de Ingreso a Zona Franca Primaria

6.- CÓDIGOS DE AJUSTE DE TIPO DE CAMBIO
CONTRIBUYENTES QUE EMITAN DOCUMENTOS DE EXPORTACIÓN ELECTRÓNICOS, O ESTÉN AUTORIZADOS A REGISTRAR DOCUMENTOS
INTERNOS QUE INCLUYAN VALORES EN OTRA MONEDA.
IEV

500

Ajuste aumento Tipo de Cambio (código 500): a utilizar cuando la paridad (moneda extranjera)/(moneda nacional) aumente entre
la fecha de emisión del documento y la fecha de cierre del periodo, debe indicarse sólo en el Resumen

IEV

501

Ajuste disminución Tipo de Cambio (código 501): a utilizar cuando la paridad (moneda extranjera)/(moneda nacional) disminuya
entre la fecha de emisión del documento y la fecha de cierre del periodo, debe indicarse sólo en el Resumen

Versión 3.0 - Marzo 2016

Pág. 41 de 45

Información Electrónica de Compras y Ventas

7.- CÓDIGOS DE IMPUESTOS Y RECARGOS.
CÓDIGOS DE IMPUESTOS Y RECARGOS
CÓD.

CÓD. CAMBIO
DE SUJETO SI
ES RETENCIÓN
TOTAL

NOMBRE

DESCRIPCIÓN GENERAL

DOCUMENTOS EN QUE SE APLICA

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

14

IVA de margen de comercialización

Para Facturas de venta del contribuyente

15

IVA retenido total

Corresponde al IVA retenido en Facturas de compra del contribuyente Factura de Compra emitida (cod 45, 46)
Notas de Crédito (cod 60, 61)
que genera el libro. Suma de retenciones con tasa toral del IVA

17

IVA ANTICIPADO FAENAMIENTO Tasa de 5% sobre Monto base faenamiento. Se registra el monto de
IVA anticipado cobrado al cliente.
CARNE

18

IVA ANTICIPADO CARNE

19

IVA ANTICIPADO HARINA

30

301

IVA RETENIDO LEGUMBRES

Notas de Débito (cod 55, 56)
Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Tasa de 5%. Se registra el monto de IVA anticipado cobrado al cliente. Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Facturas (cod 30, 33)
Tasa de 12%. Se registra el monto de IVA anticipado cobrado al cliente. Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Normalmente 10% retención.



31

32

321

IVA RETENIDO SILVESTRES



IVA RETENIDO GANADO

Normalmente 8% retención.



33

331

IVA RETENIDO MADERA


34

341

IVA RETENIDO TRIGO



Factura de Compra emitida (cod 45, 46)

Si se retuvo el 8%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA, por ser NDF, se registra en el IEC en
Retención Total.
Factura de Compra emitida (cod 45, 46)

Si se retuvo el 8%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA, por ser NDF, se registra en el IEC en
Retención Total.

Normalmente 4% retención.


Versión 3.0 - Marzo 2016

total del IVA retención. El monto retenido se registra en el IEC en Factura de Compra emitida (cod 45, 46)
Retención total.
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

Normalmente 8% retención.


Factura de Compra emitida (cod 45, 46)

Si se retuvo el 10%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA, por ser NDF se registra también en
Retención Total.

Factura de Compra emitida (cod 45, 46)

Si se retuvo el 4%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA por ser NDF se registra en el IEC en
Retención Total.

Pág. 42 de 45

Información Electrónica de Compras y Ventas

CÓDIGOS DE IMPUESTOS Y RECARGOS
CÓD.

CÓD. CAMBIO
DE SUJETO SI
ES RETENCIÓN
TOTAL

36

361

NOMBRE

IVA RETENIDO ARROZ

DESCRIPCIÓN GENERAL

Normalmente 10% retención.



37

371

Normalmente 10% retención.

HIDROBIOLO




Factura de Compra emitida (cod 45, 46)

Si se retuvo el 10%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA por ser NDF se registra en el IEC en
Retención Total.

IVA RETENIDO
GICAS

DOCUMENTOS EN QUE SE APLICA

Factura de Compra emitida (cod 45, 46)

Si se retuvo el 10%, el monto retenido se registra en el IEC en Notas de Crédito (cod 60, 61)
Retención parcial
Notas de Débito (cod 55, 56)
Si se retuvo el total del IVA por ser NDF se registra en el IEC en
Retención Total.

38

IVA RETENIDO CHATARRA

total del IVA retención. El monto retenido se registra en el IEC en Factura de Compra emitida (cod 45, 46)
Retención total.
Notas de Crédito (cod 60, 61)

39

IVA RETENIDO PPA

total del IVA retención. El monto retenido se registra en el IEC en Factura de Compra emitida (cod 45, 46)
Retención total.
Notas de Crédito (cod 60, 61)

41

IVA RETENIDO CONSTRUCCION

Se retiene el total del IVA.

Notas de Débito (cod 55, 56)

Notas de Débito (cod 55, 56)

23

44

45

IMPUESTO ADICIONAL
ART 37 LETRAS A, B, C

IMPUESTO ADICIONAL
ART 37 LETRAS E, H, I, L

IMPUESTO ADICIONAL
ART 37 LETRAS J

Tasa del 15%
a)
artículos oro, platino, marfil
b)
Joyas, piedras preciosas
c)
Pieles finas

Factura de Compra emitida (cod 45, 46)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

Tasa del 15% en 1era venta
e)
Alfombras, tapices
f)
Casa rodantes
g)
Caviar
h)
Armas de aire o gas

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)

Tasa del 50% en 1era venta
Pirotecnia

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)

Notas de Débito (cod 55, 56)

Notas de Débito (cod 55, 56)

24

25

IMPUESTO ART. 42, LEY DE IVA
LETRA B)

Tasa del 31,5% (DEBE VERIFICAR LA TASA VIGENTE)
whisky, aguardientes y destilados

Y documentos exentos en casos especiales
Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)

Notas de Débito (cod 55, 56)
Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda >
y documentos exentos en casos especiales
Aprenda sobre.>. Aprenda sobre los Impuestos >
Facturas (cod 30, 33)
Tasa del 20,5% (DEBE VERIFICAR LA TASA VIGENTE)
IMPUESTO ART. 42, LEY DE IVA Vinos destinados al consumo, comprendidos los vinos gasificados, los Notas de Crédito (cod 60, 61)
LETRA C)
espumosos o champaña, los generosos o asoleados, chichas y sidras. Notas de Débito (cod 55, 56)
Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda > y documentos exentos en casos especiales
Aprenda sobre.>. Aprenda sobre los Impuestos >
Versión 3.0 - Marzo 2016

Pág. 43 de 45

Información Electrónica de Compras y Ventas

CÓDIGOS DE IMPUESTOS Y RECARGOS
CÓD.

26

27

CÓD. CAMBIO
DE SUJETO SI
ES RETENCIÓN
TOTAL

NOMBRE

DESCRIPCIÓN GENERAL

DOCUMENTOS EN QUE SE APLICA

Facturas (cod 30, 33)
IMPUESTO ART. 42, LEY DE IVA Tasa del 20,5% (DEBE VERIFICAR LA TASA VIGENTE)
Notas de Crédito (cod 60, 61)
cervezas
y
otras
bebidas
alcohólicas,
cualquiera
que
sea
su
tipo,
LETRA C)
calidad o denominación.
Notas de Débito (cod 55, 56)y documentos exentos en
Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda > casos especiales
Aprenda sobre.>. Aprenda sobre los Impuestos >
Facturas (cod 30, 33)
IMPUESTO ART. 42, LEY DE IVA Tasas del 10% utilizar código 27 (DEBE VERIFICAR TASA VGTE)
Notas de Crédito (cod 60, 61)
Bebidas
analcohólicas
naturales
o
artificiales,
energizantes
o
LETRA A)
hipertónicas, jarabes y en general cualquier otro producto que las Notas de Débito (cod 55, 56)
y documentos exentos en casos especiales
sustituya o que sirva para preparar bebidas similares
Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda >
Aprenda sobre.>. Aprenda sobre los Impuestos >

271

Facturas (cod 30, 33)
IMPUESTO ART. 42, LEY DE IVA Tasas del 18% utilizar código 271 (DEBE VERIFICAR TASA VGTE)
Notas de Crédito (cod 60, 61)
En
el
caso
que
las
especies
señaladas
en
esta
letra
presenten
la
LETRA A) PÁRRAFO 2°
composición nutricional de elevado contenido de azúcares a que se Notas de Débito (cod 55, 56)
refiere el artículo 5° de la ley N° 20.606, la que para estos efectos se y documentos exentos en casos especiales
considerará existente cuando tengan más de 15 gramos (g) por cada
240 mililitros (ml) o porción equivalente.
Las tasas actualizadas las puede encontrar en www.sii.cl > ayuda >
Aprenda sobre.>. Aprenda sobre los Impuestos >

28

IMPUESTO ESPECÍFICO DIÉSEL

Impuesto Específico a los Combustibles traspasado al comprador por Se usa en las Facturas que emite el vendedor.
compra de diesel según Ley N° 18.502, Decreto Supremo N° 311/86. Se registra en el IEV.
Impuesto Específico Resultante a los Combustibles = Componente Fija En el IEC se registra bajo este código el Impuesto
+ Componente Variable, según Ley N° 20.493, su Reglamento y Res. Específico Resultante = Componente Fija + Componente
Ex SII N° 51 de 2011.
Variable si el comprador tiene derecho al crédito y no está
Tasas publicadas en sitio web www.sii.cl > Valores y Fechas > contemplado en el código 29.
Si el comprador no tiene derecho a recuperar este
Impuesto al petróleo (Componentes base y variable)
impuesto, el monto de este impuesto va en el campo
“Impuesto sin derecho a crédito”

29

RECUPERACIÓN IMPUESTO
ESPECÍFICO RESULTANTE AL
DIÉSEL TRANSPORTISTAS.

Para transportistas de carga Art 2° Ley N°19.764/2001 Impuesto En el IEC se registra separado con este código el monto
Específico Resultante a los Combustibles = Componente Fija + que corresponde al % del Impuesto específico resultante
Componente Variable, según Ley N° 20.493, su Reglamento y Res. Ex que se recupera; el % no recuperado en este caso, va en
SII N° 51 de 2011.
el campo “Impuesto sin derecho a crédito”.
Tasas publicadas en sitio web www.sii.cl > Valores y Fechas >
Impuesto al petróleo (Componentes base y variable)

35

IMPUESTO
GASOLINA

ESPECÍFICO Impuesto Específico a los Combustibles traspasado al comprador por Se usa en las Facturas que emite el vendedor, en el IEV.
compra de Gasolina según Ley N° 18.502, Decreto Supremo N° 311/86. No se registra separado en el IEC.
En el IEC se debe incorporar este monto en el campo
No da derecho a crédito.
“Impuesto sin derecho a crédito”
Impuesto Específico Resultante a los Combustibles = Componente Fija
+ Componente Variable, según Ley N° 20.493, su Reglamento y Res.
Ex SII N° 51 de 2011.
Tasas publicadas en sitio web www.sii.cl > Valores y Fechas >
Impuesto al petróleo (Componentes base y variable)

Versión 3.0 - Marzo 2016

Pág. 44 de 45

Información Electrónica de Compras y Ventas

CÓDIGOS DE IMPUESTOS Y RECARGOS
CÓD.

CÓD. CAMBIO
DE SUJETO SI
ES RETENCIÓN
TOTAL

47

NOMBRE

DESCRIPCIÓN GENERAL

IVA RETENIDO CARTONES

Retención Total

DOCUMENTOS EN QUE SE APLICA

Factura de Compra emitida (cod 45, 46)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

48

481

IVA RETENIDO BERRIES

Retención del 14 %

Factura de Compra emitida (cod 45, 46)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Factura de Compra emitida (cod 45, 46)

49

FACTURA DE COMPRA SIN
RETENCIÓN (SÓLO BOLSA DE
PRODUCTOS DE CHILE)

0% de retención

50

IVA DE MARGEN DE
COMERCIALIZACIÓN DE
INSTRUMENTOS DE PREPAGO

Para Facturas de venta del contribuyente

Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

Art. 1°,Ley N° 20.052; Ley N° 20.493, su Reglamento y Res. Ex SII N°
51 de 2011.
Tasas publicadas en sitio web:
51

IMPUESTO GAS NATURAL
COMPRIMIDO

http://www.sii.cl/pagina/valores/impuesto.htm
Se usa en Facturas que emite el vendedor, se registra en la IEV, no
se registra separado en la IEC.

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

Para Facturas de venta del contribuyente
Art. 1°, Ley N° 20.052, Ley N° 20.493, su Reglamento y Res. Ex SII N°
51 de 2011.

52

IMPUESTO GAS
PETRÓLEO

LICUADO

DE

Tasas publicadas en sitio web:
http://www.sii.cl/pagina/valores/impuesto.htm

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

Se usa en Facturas que emite el vendedor, se registra en la IEV, no se
registra separado en la IEC.
Para Facturas de venta del contribuyente

53

IMPUESTO RETENIDO
SUPLEMENTEROS ART 74 N°5
LEY DE LA RENTA

Facturas (cod 30, 33)
Para Facturas de venta del contribuyente, retención del 0,5% sobre el Notas de Crédito (cod 60, 61)
precio de venta al público.
Notas de Débito (cod 55, 56)

IMPUESTO RETENIDO FACTURA
DE INICIO

Retención Total de Impuestos Factura de Inicio.

60

Versión 3.0 - Marzo 2016

Factura de Inicio (cod 29)

Solo una retención por documento

Pág. 45 de 45
