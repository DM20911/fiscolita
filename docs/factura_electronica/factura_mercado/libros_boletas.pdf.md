---
url: https://www.sii.cl/factura_electronica/factura_mercado/libros_boletas.pdf
titulo: FORMATO LIBRO DE BOLETAS
categoria: factura_electronica
---
FORMATO LIBRO DE BOLETAS
2010-07-12
Versión 2.0

Servicio de Impuestos Internos
Libro de Boletas

FORMATO LIBRO DE BOLETAS
ÍNDICE DE CONTENIDO
FORMATO LIBRO DE BOLETAS .................................................................................................................................................... 2
BITÁCORA DE CAMBIOS. ................................................................................................................................................................................... 3
1.- INSTRUCCIONES GENERALES .................................................................................................................................................................... 4
1.1 Referente a los Archivos.................................................................................................................................................................................... 4
1.2 Zonas del Libro de Boletas ................................................................................................................................................................................ 5
1.3 Estructura de un envío ....................................................................................................................................................................................... 6
1.4 Instrucciones generales de formato para las Zonas ........................................................................................................................................... 6
1.5 Validaciones de envíos ...................................................................................................................................................................................... 7
1.6 Obligatoriedad por Zonas .................................................................................................................................................................................. 8
2.- LIBRO DE BOLETAS........................................................................................................................................................................................ 9
2.1. Carátula LIBRO DE BOLETAS ..................................................................................................................................................................... 9
2.2. Resumen segmento LIBRO DE BOLETAS .................................................................................................................................................. 10
2.3. Resumen período LIBRO BOLETAS: .......................................................................................................................................................... 11
2.4. Detalle LIBRO DE BOLETAS ..................................................................................................................................................................... 12

Versión 2.0 2010-07-12

Pág. 2 de 12

Servicio de Impuestos Internos
Libro de Boletas

BITÁCORA DE CAMBIOS.
Cambios 2010 07 12
1. En la sección 2.2 Resumen Segmento Libro de Boletas en el campo “Tipo de Servicio” se agrega un cuarto tipo “Boleta de Espectáculo emitida por
cuenta de terceros”.
2. En la sección 2.2 Resumen Segmento Libro de Boletas:
a. Se agrega el campo “Total Ticket Periodo”
3. En la sección 2.3 Resumen Periodo Libro de Boletas en el campo “Tipo de Servicio” se agrega un cuarto tipo “Boleta de Espectáculo emitida por
cuenta de terceros”.
4. En la sección 2.3 Resumen Periodo Libro de Boletas:
a. Se agrega el campo “Total Ticket Periodo”
5. En la sección 2.4 Detalle Libro de Boletas en el campo “Tipo de Servicio” se agrega un cuarto tipo “Boleta de Espectáculo emitida por cuenta de
terceros”.
6. En la sección 2.4 Detalle Libro de Boletas:
a. Se agrega el campo “Total Ticket Boleta”
Cambios 2005 08 05.
Correcciones de forma y redacción. No afectan esquema.

Cambios 2005 04 15.
Se cambia obligatoriedad de campos “Fecha de vencimiento”, “Periodo desde” y “Periodo hasta”, a condicionales. Son obligatorios sólo en caso de tratarse
de Boletas de Servicios Periódicos y Boletas de Servicios Periódicos Domiciliarios.

Cambios 2004 01 30.
1. Se agregó carátula
2. Se incorporó contador de folios anulados
3. Campos IVA y Monto Neto van sólo en Resumen Período.
4. En carátula de Libro se debe indicar el período mas antiguo que se haya incluido.

Versión 2.0 2010-07-12

Pág. 3 de 12

Servicio de Impuestos Internos
Libro de Boletas

1.- INSTRUCCIONES GENERALES
La empresa que emita boletas electrónicas debe generar un Libro de Boletas con el resumen de las boletas emitidas; al cierre del período
deberá totalizar la información de este libro y traspasar la información de aquellas ventas que se devenguen en el mes, a un registro del IECV
codificándolo como documento 39 Boletas electrónicas del mes o documento 41 Boletas No Afecta o Exenta Electrónicas del Mes. Si hay
ventas que se devengan el mes siguiente, éstas se deberán incluir en el IECV del siguiente período tributario.
En este documento se describe el contenido que debe tener el Libro de Boletas. Este documento contiene un listado de las boletas
emitidas en cada mes, con información de tipo general. Se actualiza en forma permanente con la información de los documentos
emitidos en el día.
No se envía al SII
Debe estar disponible para consulta inmediata para los últimos tres meses.
Se podrá solicitar información para períodos anteriores, la cual deberá ser enviada en el medio electrónico que se defina, dando
un plazo de 10 días hábiles para contestar la consulta.
Al finalizar el mes, se debe generar Resumen
En el Resumen, debe haber un registro separado para cada período tributario en que se devenga el impuesto1, con el fin de que
sea consistente con la información que se incluye en el IECV.
Una vez generados todos los registros resumen del mes, se deberá firmar en forma electrónica.
El Libro de Boletas firmado, se debe guardar por un período de 6 años.

1.1 Referente a los Archivos
1. Formato XML definido por el SII.
2. Este archivo se envía a requerimiento del SII.
3. Un envío puede ser:
de un período tributario 2
de varios períodos tributarios
documentos generados para un determinado Rut receptor
documentos superiores a cierto monto
y en general por cualquier selección o clasificación que solicite Fiscalización asociados a los conceptos anteriores

1
2

Esto se aplica para los Servicios Periódicos Domiciliarios, en que el impuesto se devenga en la fecha de vencimiento.
Por fecha de emisión.
Versión 2.0 2010-07-12

Pág. 4 de 12

Servicio de Impuestos Internos
Libro de Boletas

4. El archivo solicitado se puede enviar de una sola vez, o en varios envíos. Cada tipo de envío puede ser identificado a través de la
carátula que lo define, que indica si es:
Total: Se hace un solo envío que contiene toda la información solicitada. “Se debe anotar TOTAL” en el identificador de la
Carátula.
Parcial: Envíos parciales. Pueden ser de 1 a 999 envíos. Se debe anotar “PARCIAL” seguida por el número del envío parcial,
por ejemplo P1, P2, etc. Esto es para todos los envíos parciales, excepto para el último.
Final: Corresponde al último envío parcial. Se debe anotar “FINAL” en el identificador de la Carátula.
Ajuste: Corresponde a un envío que permite agregar o eliminar documentos informados anteriormente. Se debe anotar
“AJUSTE” en el identificador de la Carátula.

1.2 Zonas del Libro de Boletas
Se distinguen las siguientes zonas:

a) Carátula
Contiene datos generales del envío: Rut del contribuyente emisor, período tributario (opcionalmente), tipo de segmento, número de
notificación y número de Segmento en el caso de envíos parciales.

b) Resumen Segmento
Contiene los totales por tipo de documento. Esta Zona es obligatoria si viene la Zona de Detalle, excepto si el envío es TOTAL.
● Las boletas que se incluyen totalizadas, no se incluyen en este resumen y deben ir sólo en el Resumen Período.

c)

Resumen Período
a) Si hay varios envíos: El resumen del período se construye en base a todos los Resúmenes de Segmento del período enviados.
b) Se debe incluir en un envío de tipo TOTAL, FINAL o AJUSTE.
Si el envío es FINAL: debe incluir sólo Resumen Período (no debe traer detalle).
Si el envío es TOTAL: Viene Resumen Período y Detalle (excepto que no haya Boletas que informar).
Si el envío es AJUSTE: Viene Resumen Período, Detalle y Resumen Segmento (Excepto que la corrección sea sólo en el
Resumen período).

d) Detalle
En esta Zona se debe detallar una línea por cada documento.

Versión 2.0 2010-07-12

Pág. 5 de 12

Servicio de Impuestos Internos
Libro de Boletas

1.3 Estructura de un envío
A continuación se resume que debe contener cada tipo de envío
a) Envío Total: Un envío es del tipo Total, cuando se envía de una vez, toda la información solicitada en una notificación. Este tipo de
envío, que se identifica como “TOTAL” en el campo tipo de la carátula, puede contener:
Sólo el Resumen Período: Si la empresa no emitió Boletas Electrónicas en el período notificado.
Zona de Detalle y Resumen Período: Cuando hay documentos unitarios que informar
b) Envío Parcial: Un envío es de tipo Parcial si la información se envía por partes. Un envío PARCIAL debe indicar “PARCIAL” en el
campo “Tipo” de la CARÁTULA. En este tipo de envío no se puede incluir el RESUMEN PERÍODO, ya que este último debe ser
enviado en forma independiente. Todo envío parcial debe incluir una Zona DETALLE.
c) Envío Final: Un envío final se realiza una vez que se han recibido y aceptado por parte del SII, todos los envíos parciales. Este tipo
de envío debe contener sólo la Zona RESUMEN PERÍODO. Se debe indicar “FINAL” en el campo tipo de la CARÁTULA.
d) Envío de Ajuste: Este tipo de envío sólo se puede realizar una vez hecho un envío FINAL o TOTAL y tiene como objetivo agregar
registros faltantes, eliminar registros, modificar la información de un registro o corregir el Resumen Período.

1.4 Instrucciones generales de formato para las Zonas
-

Los largos indicados se refieren a tamaño máximo.
En la información de tipo numérica, los decimales se separan con punto y se deben indicar sólo cuando el valor que se desea incluir
contiene decimales significativos.
No deben separarse los miles con carácter alguno.
Todos los valores de montos deben venir en pesos.
En la información alfanumérica, algunos caracteres como „&‟ y „<‟ tienen un significado especial para XML y deben ser reemplazados por
la secuencia de escape que el estándar define para dichos caracteres.
La columna (*), indica que si la información recibida por el SII no contiene este campo, la información se considera incompleta y será
rechazada.
En general, los datos deberán ser positivos, excepto que se indique lo contrario en forma expresa.

Versión 2.0 2010-07-12

Pág. 6 de 12

Servicio de Impuestos Internos
Libro de Boletas

1.5 Validaciones de envíos
Al recibir un envío el SII validará
a)

Si el envío es tipo Parcial
Campo “Tipo” de CARÁTULA debe indicar “Parcial”
Existe sólo Resumen Segmento y Detalle
Suma por documento del RESUMEN SEGMENTO corresponda con DETALLE

b)

Si el envío es Total
Campo “Tipo” de CARÁTULA debe indicar “Total”
Es obligatorio el Resumen Periodo

c)

Si el envío es Final
Campo “Tipo” de CARÁTULA debe indicar “Final”
Sólo debe venir Resumen Período
Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período

d)

Si el envío es Ajuste
Campo “Tipo” de CARÁTULA debe indicar “Ajuste”
Es obligatorio el Resumen Periodo
Los datos del Resumen Periodo deben corresponder a los totales de todos los segmentos recibidos del período, incluyendo el ajuste.

e)

El campo período tributario de la carátula puede venir con un cero.

En caso de discordancia se rechazará el envío.

Versión 2.0 2010-07-12

Pág. 7 de 12

Servicio de Impuestos Internos
Libro de Boletas

1.6 Obligatoriedad por Zonas
La obligatoriedad de cada una de las zonas por tipo de documento se especifica en la siguiente Tabla.
ZONA

Código
Obligatoriedad

Observaciones

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

No debe venir en envío Final

Códigos de Obligatoriedad:
1: Dato obligatorio. El dato debe estar en el documento siempre.
2: Dato condicional. El dato se registra sólo si está.
3: Opcional.

Versión 2.0 2010-07-12

Pág. 8 de 12

Servicio de Impuestos Internos
Libro de Boletas

2.- LIBRO DE BOLETAS
2.1. Carátula LIBRO DE BOLETAS
OBSERVACIONES GENERALES

(*)3

Obligatoriedad

10

Corresponde al Rut del contribuyente emisor con guión y dígito verificador

*

1

ALFA

10

Corresponde al Rut del usuario autorizado que hace el envío al SII

*

1

PERÍODO TRIBUTARIO

ALFA

7

Periodo Tributario , en formato AAAA-MM (Año (4),Mes (2)). En el caso de una notificación
que abarque varios períodos tributarios se debe colocar el de la fecha inicial solicitada

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

Número de Resolución que autoriza al contribuyente como emisor electrónico

*

1

6

Tipo de Libro

ALFA

8

ESPECIAL (Corresponde a un libro solicitado vía una notificación)

*

1

7

Tipo de Envío

ALFA

7

TOTAL: información total del mes. Si no se incluye, se asume que es total.

N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

1

RUT Emisor Libro

ALFA

2

RUT Enviador

3

1

1

PARCIAL: Segmento parcial : tiene parte de la información del período
FINAL: Corresponde al último segmento
AJUSTE : Movimientos ingresados con posterioridad al envío fina

3

8

Numero de Segmento

NUM

6

Número del segmento. Sólo si el TIPO DE ENVIO es PARCIAL

9

Folio de Notificación

NUM

18

Número de notificación. Obligatorio.

2
*

1

La columna (*), indica que si el archivo recibido por el SII no contiene este campo, el archivo se rechazará por esquema XML.

Versión 2.0 2010-07-12

Pág. 9 de 12

Servicio de Impuestos Internos
Libro de Boletas

2.2. Resumen segmento LIBRO DE BOLETAS
Todos los montos pueden ser negativos así como también el campo “cantidad de documentos” que puede ser negativo en un envío de ajuste.
N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

1

TIPO DE DOCUMENTO

NUM

2

OBSERVACIONES GENERALES

(*)

Obligatoriedad

Para todos los tipos de documentos que se han informado en el archivo de detalle

*

1

39: Boleta Electrónica
41: Boleta No Afecta o Exenta Electrónica
2

CANTIDAD DE FOLIOS ANULADOS

NUM

10

TABLA INFORMATIVA POR TIPO DE
SERVICIO Y PERÍODO DE DEVENGO

Registrar el total de folios anulados. Estos casos no se totalizan en ninguno de los campos
siguientes.

2

PRÓXIMOS 9 CAMPOS
1 Boleta Servicios periódicos
2 Boleta de Servicios Periódicos Domiciliarios
3 Boleta de Ventas y Servicios
4 Boleta de Espectáculo emitida por cuenta de Terceros

3

TIPO DE SERVICIO

NUM

1

4

Período devengo

NUM

7

AAAA-MM

5

TOTAL DE DOCUMENTOS

NUM

10

Cantidad de documentos del tipo especificado en el campo Tipo de Documento, por tipo de
servicio y Periodo de devengo. No incluye nulos.

*

Valido si Tipo de Servicio es 2

1

2
*

1

Ejemplo: Si una Empresa emite Boletas por Servicios Periódicos y otros por Ventas y
Servicios y algunas son Boletas exentas y el resto son afectas, debe incluir:
o
Un registro por las Boletas Electrónicas de Servicios Periódicos
o
Un registro por las Boletas Electrónicas de Ventas y Servicios
o
Un registro por las Boletas No Afecta o Exenta Electrónicas de Servicios
Periódicos
o
Un registro por las Boletas No Afecta o Exenta Electrónicas de Ventas y Servicios
6

TOTAL
MONTO
GRAVADO

7

EXENTO

O

NO

NUM

18

Este campo sólo se incluye si hay Montos exentos en detalle. No incluye nulos.

TOTAL MONTO TOTAL

NUM

18

Totales de los documentos. No considerar folios anulados.

8

Total Monto no facturable

NUM

18

No considerar folios anulados. Valor puede ser negativo

3

9

Total Monto Período

NUM

18

No considerar folios anulados . Valor puede ser negativo

3

10

Total Saldo Anterior

NUM

18

No considerar folios anulados

3

11

Total Valor a Pagar

NUM

18

No considerar folios anulados

3

12

Total Ticket Periodo

NUM

7

En caso de parcializar el envío, corresponde a la sumatoria de los Total Ticket Boleta, del
Detalle

2

Versión 2.0 2010-07-12

2

*

1

Pág. 10 de 12

Servicio de Impuestos Internos
Libro de Boletas

2.3. Resumen período LIBRO BOLETAS:
Obligatorio si Envío es TOTAL, FINAL O AJUSTE
En este resumen se deben entregar totalizados los montos por campo de cada tipo de documento de todo el período. También es obligatorio en el
caso de efectuar ajustes posteriores al cierre del período.
N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

1

TIPO DE DOCUMENTO

NUM

2

2

CANTIDAD DE FOLIOS ANULADOS

NUM

10

TABLA INFORMATIVA POR TIPO DE
SERVICIO Y PERÍODO DE DEVENGO

OBSERVACIONES GENERALES

(*)

Obligatoriedad

Para todos los tipos de documentos que se han informado en el archivo de detalle
39: Boleta Electrónica
41: Boleta No Afecta o Exenta Electrónica

*

1

Registrar el total de folios anulados. Estos casos no se totalizan en ninguno de los campos
siguientes.

2

PRÓXIMOS 11 CAMPOS
1 Boleta Servicios periódicos
2 Boleta de Servicios Periódicos Domiciliarios
3 Boleta de Ventas y Servicios
4 Boleta de Espectáculo emitida por cuenta de Terceros

3

TIPO DE SERVICIO

NUM

1

4

Período devengo

NUM

7

Año-mes en formato AAAA-MM Valido si Tipo de Servicio es 2

5

TOTAL DE DOCUMENTOS

NUM

10

Cantidad de documentos del tipo especificado en el campo Tipo de Documento, por tipo de
servicio y Periodo de devengo. No incluye nulos

6

TOTAL
MONTO
GRAVADO

NUM

18

Suma de Montos exentos de Detalle. No incluye nulos.

2

7

TOTAL MONTO NETO

NUM

18

a) Sólo se incluye si en el envío, toda la información es del mismo período.
b) En Boleta Electrónica afecta (codigo 39) se calcula a través de Formula = (Monto TotalMonto Exento)/(1+ tasa de IVA). En Boleta Exenta no se incluye o se incluye un 0.

2

8

Tasa IVA

NUM

18

Sólo se incluye si toda la información es del mismo período y el documento es tipo 39

2

EXENTO

O

NO

*

1

2
*

a) Se calcula como Total Monto Neto * tasa de IVA
b) Sólo se incluye si toda la información es del mismo período.

1

9

TOTAL MONTO IVA

NUM

18

10

TOTAL MONTO TOTAL

NUM

18

11

Total Monto no facturable

NUM

18

Valor puede ser negativo

3

12

Total Monto Período

NUM

18

Valor puede ser negativo

3

13

Total Saldo Anterior

NUM

18

14

Total Valor a Pagar

NUM

18

15

Total Ticket Periodo

NUM

7

Totales de los documentos

2
*

1

3
3
Corresponde a la sumatoria de los Total Ticket Boleta, del Detalle. En caso de parcializar el
envío, corresponde a la sumatoria de los Total Ticket Periodo de los Resúmenes Segmento,
en el Envío Final.

Versión 2.0 2010-07-12

2

Pág. 11 de 12

Servicio de Impuestos Internos
Libro de Boletas

2.4. Detalle LIBRO DE BOLETAS
CAMPO

Información del campo

N°

NOMBRE

Tipo

LAR
GO
Máx.

Observaciones

(*)

Obligatoriedad

1

TIPO DE DOCUMENTO

NUM

2

39: Boleta Electrónica

*

1

2

FOLIO (NUMERO DE DOCUMENTO)

NUM

10

FOLIO.

*

1

3

Folio Anulado

A

1

= A (Anulado): No debe tener Montos y si estos vienen, no se consideran luego en los montos
de los resúmenes

4

TIPO DE SERVICIO

NUM

1

5

FECHA DE EMISION

ALFA

10

AAAA-MM-DD (año, mes, día , separado por guiones)

1

6

FECHA DE VENCIMIENTO

ALFA

10

AAAA-MM-DD (año, mes, día , separado por guiones)

3

7

PERIODO DESDE

ALFA

10

AAAA-MM-DD (año, mes, día , separado por guiones)

3

8

PERIODO HASTA

ALFA

10

AAAA-MM-DD (año, mes, día , separado por guiones)

3

9

CÓDIGO SUCURSAL

NUM

8

Sucursal donde se emitió el documento. Código numérico entregado por el SII, que identifica a
cada sucursal que está identificada en el Servicio de Impuestos Internos. Si no hay sucursales o
se emite centralizadamente se puede omitir. (Código registrado en el SII)

2

10

RUT CLIENTE

ALFA

10

Corresponde al rut del receptor. Con guión y dígito verificador o código interno del cliente.

2

11

CODIGO INTERNO CLIENTE

ALFA

80

Para identificación interna del Receptor, por ejemplo Código de Cliente, Numero de Medidor,
etc. Sin Validación.

2

12

MONTO EXENTO O NO GRAVADO

NUM

18

Se debe incluir en Boletas exentas o en Boletas Afectas que tienen una parte exenta

2

13

MONTO TOTAL

NUM

18

Valor obligatorio

1

14

Total Monto no facturable

NUM

18

Valor puede ser negativo

3

15

Total Monto Período

NUM

18

Valor puede ser negativo

3

16

Total Saldo Anterior

NUM

18

Valor puede ser negativo

3

17

Total Valor a Pagar

NUM

18

Sin Validación

3

18

Total Ticket Boleta

NUM

3

Si tipo de servicio es 4, se debe totalizar la cantidad de ticket del documento “boleta electrónica”
de acuerdo al campo Item Espectaculo y Cantidad. Valor Entero Positivo.

2

41: Boleta No Afecta o Exenta Electrónica

1 Boleta Servicios periódicos
2 Boleta de Servicios Periódicos Domiciliarios
3 Boleta de Ventas y Servicios
4 Boleta de Espectáculo emitida por cuenta de Terceros

Versión 2.0 2010-07-12

2

1

Pág. 12 de 12
