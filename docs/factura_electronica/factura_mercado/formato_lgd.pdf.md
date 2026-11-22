---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_lgd.pdf
titulo: FORMATO LIBRO DE GUIAS DE DESPACHO ELECTRONICAS
categoria: factura_electronica
---
FORMATO LIBRO DE GUIAS DE DESPACHO ELECTRONICAS
2003-10-29
Versión 1.0

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

FORMATO LIBRO DE GUIAS DE DESPACHO ELECTRONICAS
ÍNDICE DE CONTENIDO
1.- INSTRUCCIONES GENERALES....................................................................................................................................................................3
a) Referente al Archivo............................................................................................................................................................................................3
b) Zonas del Libro de Guías de Despacho Electrónicas........................................................................................................................................3
c) Estructura de un envío .........................................................................................................................................................................................5
d) Instrucciones generales de formato para las Zonas............................................................................................................................................6
e) Validaciones de envíos .......................................................................................................................................................................................7
f) Códigos de Obligatoriedad .................................................................................................................................................................................8
2.- Libro de Guías de Despacho Electrónicas .......................................................................................................................................................9
a) Carátula...........................................................................................................................................................................................................9
b) Resumen segmento .......................................................................................................................................................................................10
c) Resumen PERIODO .....................................................................................................................................................................................11
d) Detalle...........................................................................................................................................................................................................12

Versión 1.0 2003-10-29

Pág. 2 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

1.- INSTRUCCIONES GENERALES
En este documento se describe el contenido que debe tener el Libro de Guías de Despacho Electrónicas.
La información debe ser remitida, en el formato XML definido por el SII, sólo en el caso de que sea solicitada por medio de una
notificación; en la notificación se establecerá sobre que tipo de guías se debe informar; en cualquier caso se debe enviar la
información de cada registro del archivo en forma completa.
El archivo a entregar deberá cumplir con las especificaciones que se detallan a continuación:

a) Referente al Archivo
1. Formato XML definido por el SII.
2. Este archivo no se envía regularmente al SII; sólo se envía a requerimiento del Servicio. El contenido puede ser de uno o varios
períodos tributarios, sólo los documentos generados para un determinado Rut receptor, por Tipo de operación, y en general por
cualquier selección que considere las variables anteriores.
3. La información solicitada se puede enviar de una sola vez, o en varios envíos. Cada tipo de envío puede ser identificado a través
de la carátula que lo define.
4. Si la notificación afecta a varios periodos tributarios, se debe confeccionar el Resumen Periodo (del envío) una vez que se haya
mandado toda la información correspondiente a la Notificación.

5. Cada archivo enviado al SII debe incluir la firma electrónica sobre toda la información, tal como lo establece el schema
XML.

b) Zonas del Libro de Guías de Despacho Electrónicas
En los Archivos se distinguen las siguientes zonas:

b.1. Carátula
Contiene datos generales de la información del envío los cuales corresponden al Rut del contribuyente emisor, identificación del folio
de la notificación, tipo de segmento, y número de Segmento en el caso de envíos parciales.

Versión 1.0 2003-10-29

Pág. 3 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

En la carátula se define si el envío es:
•

Total: Se hace un solo envío que contiene toda la información solicitada en la notificación. “Se debe anotar TOTAL” en el
identificador de la Carátula.

•

Parcial: Envíos parciales. Pueden ser de 1 a 999 envíos. Se debe anotar “PARCIAL” seguida por el número del envío parcial,
por ejemplo P1, P2, etc. Esto es para todos los envíos parciales, excepto para el último.

•

Final: Corresponde al último envío parcial correspondiente a la notificación. Se debe anotar “FINAL” en el identificador de la
Carátula.

•

Ajuste: Corresponde a un envío que permite agregar o eliminar documentos informados anteriormente. Se debe anotar
“AJUSTE” en el identificador de la Carátula.

b.2. Resumen Segmento
Contiene los mismos totalizadores del Resumen Notificación, pero sólo para los documentos incluidos en el segmento de Detalle. Si el
envío es parcial o ajuste esta Zona es obligatoria.

b.3

Resumen Período

El resumen del período se construye en base a toda la información correspondiente a la notificación.
El Resumen Periodo se debe incluir en un envío de tipo TOTAL, FINAL o AJUSTE.
Si el envío es FINAL, éste debe incluir sólo el Resumen Período.
Si el envío es TOTAL, el Resumen Período debe venir acompañado de Detalle.
Si el envío es AJUSTE, el Resumen Período debe venir acompañado de Detalle y de Resumen Segmento.

b.4. Detalle
En esta Zona se debe detallar una línea por cada guía de despacho electrónica.

Versión 1.0 2003-10-29

Pág. 4 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

c) Estructura de un envío
A continuación se explican los distintos tipos de envío y se detalla que debe contener cada uno
a) Envío Total: Un envío es del tipo Total, cuando se envía el libro de guías de despacho electrónicas con toda la información solicitada,
en un único envío. Este tipo de envío, que se identifica como “TOTAL” en el campo tipo de la carátula, puede contener:
• Zona de Detalle y Resumen Período.
b) Envío Parcial: Un envío parcial significa que el libro de guías de despacho electrónicas se manda en más de un envío. Un envío
PARCIAL debe indicar “PARCIAL” en el campo “Tipo” de la CARÁTULA. En este tipo de envío no se puede incluir el RESUMEN
PERIODO, ya que este último debe ser enviado en forma independiente. Todo envío parcial debe incluir una Zona DETALLE.
c) Envío Final: El envío final se realiza una vez que se han recibido y aceptado por parte del SII, todos los envíos parciales. Este tipo de
envío debe contener sólo la Zona RESUMEN PERIODO. Se debe indicar “FINAL” en el campo tipo de la CARÁTULA.
d) Envío de Ajuste: Este tipo de envío sólo se puede realizar una vez hecho un envío FINAL o TOTAL y tiene como objetivo agregar
registros faltantes, eliminar registros o modificar la información de un registro.
Se indica como AJUSTE en la CARÁTULA y puede contener
• Las tres Zonas de datos que deben contener:
Zona Detalle: Con el detalle del ajuste. Se puede eliminar y/o agregar uno o más registros del libro de guías de despacho
electrónicas; el tipo de operación se debe anotar en el campo “Operación” del detalle de Ajuste. Si la modificación consiste en
cambiar algún dato de un documento, se debe eliminar el registro anterior y agregar el documento con los valores correctos.

Versión 1.0 2003-10-29

Pág. 5 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

Por ejemplo si se ha registrado:
Tipo documento
Folio
52
1234

Monto Total
11.800

y había un error en el Monto Total de forma que los valores correctos son
Tipo documento
Folio
Monto Total
52
1234
1.800
en la Zona DETALLE se debe registrar:
Operación
2
1

Tipo documento
52
52

Folio
1234
1234

Monto Total
11.800
1.800

Zona Resumen Segmento: Para construir el total por documento, se suman los ajustes con signo, restando los campos que se
eliminan y sumando los que se agregan. En el ejemplo anterior en el RESUMEN SEGMENTO debe indicarse:
Tipo documento
52
52

Cantidad de Documentos Folio
-1
1

Total
-11.800
1.800

Dado lo anterior, todos los campos numéricos del Resumen Segmento pueden ser negativos.
Zona Resumen Período: El Resumen período debe totalizar todos los segmentos enviados más el de ajuste (considerando el
signo).

d) Instrucciones generales de formato para las Zonas
-

Los largos indicados se refieren a tamaño máximo.
En la información de tipo numérica, los decimales se separan con punto y se deben indicar sólo cuando el valor que se desea incluir
contiene decimales significativos.
No deben separarse los miles con carácter alguno.
Todos los valores de montos deben venir en pesos.
En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben ser reemplazados por
la secuencia de escape que el estándar define para dichos caracteres.
La columna (*), indica que si la información recibida por el SII no contiene este campo, la información se considera incompleta y será
rechazada.
En general, los datos deberán ser positivos, excepto que se indique lo contrario en forma expresa.
Versión 1.0 2003-10-29

Pág. 6 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

e) Validaciones de envíos
Al recibir un envío el SII validará
a)

Si el envío es tipo Parcial
• Campo “Tipo” de CARÁTULA debe indicar “Parcial”
• Existe sólo Resumen Segmento y Detalle
• Suma por documento del RESUMEN SEGMENTO debe corresponder con DETALLE

b)

Si el envío es Total
• Campo “Tipo” de CARÁTULA debe indicar “Total”
• Es obligatorio el Resumen PERIODO
• Debe venir DETALLE, excepto que no vengan documentos informados en el Resumen

c)

Si el envío es Final
• Campo “Tipo” de CARÁTULA debe indicar “Final”
• Sólo debe venir Resumen Total
• Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período

d)

Si el envío es Ajuste
• Campo “Tipo” de CARÁTULA debe indicar “Ajuste”
• Es obligatorio el Resumen Notificación
• Debe venir DETALLE, informando el tipo de “operación” y RESUMEN SEGMENTO
• Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período, incluyendo el ajuste.

En todos los casos, debe siempre indicarse el número de la notificación, que corresponde al folio preimpresa en ésta.

En caso de discordancia se rechazará el envío.

Versión 1.0 2003-10-29

Pág. 7 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

f) Códigos de Obligatoriedad
1: Dato obligatorio. El dato debe estar siempre.
2: Dato condicional. El dato se registra sólo si está registrado en el documento emitido.
3: Opcional.

Obligatoriedad por Zonas
ZONA

Código
Obligatoriedad

Observaciones

Carátula

1

Siempre obligatoria

Resumen Segmento

2

Es obligatorio en envíos Parcial y Ajuste

Resumen Período

2

Obligatoria en envío Total, Final o Ajuste

Detalle

2

No debe venir en envío Final

Versión 1.0 2003-10-29

Pág. 8 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

2.- Libro de Guías de Despacho Electrónicas
a) Carátula
N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

OBSERVACIONES GENERALES

(*)

Obligatoriedad

1

RUT Contribuyente

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

3

PERÍODO TRIBUTARIO

ALFA

7

Periodo Tributario , en formato AAAA-MM (Año (4),Mes (2)). Este dato se indica como
informativo, sólo si el tipo de libro es mensual.

4

Fecha Resolución

ALFA

10

AAAA-MM-DD

*

1

5

Número Resolución

NUM

6

Número de Resolución que autoriza a operar al contribuyente

*

1

6

Tipo de Libro

ALFA

8

MENSUAL (Corresponde al Libro regular que el contribuyente mantiene). Este tipo se usa
si el SII solicita a través de una notificación que el Libro se envíe completo para un solo
mes.

2

2

ESPECIAL (Corresponde a un libro solicitado vía una notificación y que corresponde a uno
o más periodos o a una selección especial del tipo de Guías a considerar en un mes)
Si no viene el dato se supondrá que es especial.
7

Tipo de Envío

ALFA

7

TOTAL: información total del mes. Si no se incluye, se asume que es total.

2

PARCIAL: Segmento parcial : tiene parte de la información del período
FINAL: Corresponde al último segmento
AJUSTE : Movimientos ingresados con posterioridad al envío final
8

Numero de Segmento

NUM

3

Número del segmento. Sólo si el TIPO DE ENVIO es PARCIAL

9

Número de Notificación

NUM

3

Número de notificación.

Versión 1.0 2003-10-29

2
*

1

Pág. 9 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

b) Resumen segmento
En este resumen se deben entregar totalizados los montos por campo, para los documentos incluidos en el detalle.
Todos los montos pueden ser negativos así como también el campo “cantidad de documentos” que puede ser negativo en un envío de ajuste.
Al término del período tributario, una vez que se hayan emitido las Facturas de venta que correspondan, se debe generar este resumen.
Cuando el SII solicite la información, siempre debe venir este dato N° de Factura en las Guías correspondientes a Venta.
NOMBRE DEL CAMPO

Tipo

LARGO
Max.

OBSERVACIONES GENERALES

(*)

Obligatoriedad

1

Total Folios anulados

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO = 1

2

2

Total Guías anuladas

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO = 2

2

3

Total Guías venta

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO
distinto de 1 y 2 y el campo TIPO DE OPERACIÓN=1

1

4

Total Monto Total Guias Venta

NUM

18

Suma del Monto Total de Guías Venta

1

5

Total Monto Total Modificado

NUM

18

Suma del Monto Total modificado

3

6

Tabla Guías no ventas

7

Código Tipo de Traslado de Bienes

NUM

1

Valores de 2 a 7

8

Cantidad Guías

NUM

5

Cantidad de Guías del periodo

2

9

Monto Guías

NUM

18

Indicar Monto, en caso que se hayan valorizado

3

Indica la cantidad y el Monto Total de los distintos tipos de Guías
no Venta. Se repite hasta 6 veces, según los distintos códigos no
venta

Versión 1.0 2003-10-29

Pág. 10 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

c) Resumen PERIODO
Para los Envíos: Obligatorio si Envío es TOTAL, FINAL O AJUSTE
En este resumen se deben entregar totalizados los montos por campo de los documentos de todo el período. También es obligatorio en el caso de
efectuar ajustes posteriores al cierre del período.
Para la información que mantiene el contribuyente: Al término del período tributario, una vez que se hayan emitido las Facturas de venta que
correspondan, se debe generar este resumen.
El mismo formato de Resumen , es el que debe enviarse al SII, pero para todo el envío. Es decir si la información solicitada es de varios meses, se
podrán efectuar varios envíos, pero el Resumen debe incluir toda la información correspondiente a la notificación.
NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

OBSERVACIONES GENERALES

(*)

Obligatoriedad

1

Total Folios anulados

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO=1

2

2

Total Guías anuladas

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO=2

2

3

Total Guías venta

NUM

5

Cantidad de Guías en que el campo ANULADO/MODIFICADO
distinto de 1 y 2 y el campo TIPO DE OPERACIÓN=1

*

1

4

Total Monto Total Guías Venta

NUM

18

Suma del Monto Total de Guías Venta

*

1

5

Total Monto Total Modificado

NUM

18

Suma del Monto Total modificado

6

Tabla Guías no ventas

7

Código Tipo de Traslado de Bienes

NUM

1

Valores de 2 a 7

2

8

Cantidad Guías

NUM

5

Cantidad de Guías del periodo

2

9

Monto Guías

NUM

18

Indicar Monto, en caso que se hayan valorizado

3

3

Indica la cantidad y el Monto Total de los distintos tipos de Guías
no Venta. Se repite hasta 6 veces, según los distintos códigos no
venta. Los siguientes 3 campos constituyen esta tabla.

Versión 1.0 2003-10-29

Pág. 11 de 12

Servicio de Impuestos Internos
Libro de Guías de Despacho Electrónicas

d) Detalle
CAMPO

NOMBRE DEL CAMPO

Tipo

LARGO

1

FOLIO –Documento

NUM

10

2

ANULADO/MODIFICADO

NUM

1

OBSERVACIONES

Obligatoriedad
1

Se indica un

2

1: Folio anulado. Si el documento ha sido anulado previo a su envío al SII.
En este caso el resto de los campos no se requieren.
2: si el documento ha sido anulado posterior a su envío al SII.
3: si los productos han sido recibidos parcialmente (no se deben modificar
los montos)
1

3

Indicador Tipo de operación

NUM

1

1: Operación constituye venta
2: Ventas por efectuar
3: Consignaciones
4: Productos en demostración
5: Traslados internos
6: Otros traslados no venta
7: Guía de devolución

2

4

FECHA

ALFA

10

Fecha (AAAA-MM-DD)

2

5

RUT DE RECEPTOR

ALFA

10

Con guión y dígito Obligatorio en el caso de ser ventas.
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

2

6

NOMBRE
O
RECEPTOR

ALFA

50

3

7

MONTO NETO

NUM

18

3

8

Tasa Impuesto

NUM

5

9

IVA

NUM

18

10

MONTO TOTAL

NUM

18

Es obligatorio en el caso de ventas

2

11

MONTO TOTAL MODIFICADO

NUM

18

Si el campo ANULADO/MODIFICADO =3, SE ANOTA EL MONTO
CORREGIDO. Este campo es opcional.

3

12

Tipo de Documento Referencia

NUM

2

Este campo y los dos siguientes se utilizan para registrar la Factura emitida
en caso de ventas. Según codificaciones generales de DTE

2

13

FOLIO documento Referencia

NUM

10

Folio de factura emitida

2

14

FECHA documento Referencia

ALFA

10

AAAA-MM-DD

2

RAZON

SOCIAL

3 enteros, 2 decimales. Se debe registrar la tasa del IVA

3
3

1

De acuerdo a la definición de "venta" establecida en el Artículo 2° del DL 825 y las operaciones equiparadas a ventas según artículo 8°. Se debe indicar cuando el
producto está facturado o se facturará posteriormente.
Versión 1.0 2003-10-29

Pág. 12 de 12
