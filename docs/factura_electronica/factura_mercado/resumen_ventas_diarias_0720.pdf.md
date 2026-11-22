---
url: https://www.sii.cl/factura_electronica/factura_mercado/resumen_ventas_diarias_0720.pdf
titulo: Página 1 de 8
categoria: factura_electronica
---
Página 1 de 8

FORMATO ARCHIVO ELECTRÓNICO RESUMEN DE VENTAS DIARIAS (EX
REPORTE CONSUMO DE FOLIOS)

2020-08-03
Versión 2.0

Página 2 de 8

FORMATO RESUMEN DE VENTAS DIARIAS
FORMATO ARCHIVO ELECTRÓNICA RESUMEN DE VENTAS DIARIAS………………………………………………….....1
BITÁCORA DE CAMBIOS…………………………………………………………………………………………………………….2
1.- INTRODUCCIÒN…………………………………………………………………………………………………………………….2
2.- CONTENIDO DE ARCHIVO DE RESUMEN DE VENTAS DIARIAS………………………………………………………….3
3. EJEMPLOS…………………..……………………..……………………..……………………..…………………………………...5

BITÁCORA DE CAMBIOS
Cambios 03/08/2020
1) Se modifica el nombre del archivo de “Reporte de Consumo de Folios” a “Resumen de Ventas Diarias”.
2) Se modifica introducción y contenido de archivo.
3) Se modifican los documentos a informar.
Cambios 05/02/2009
1) Se actualiza ejemplos de rangos de folios emitidos y anulados.
1.- INTRODUCCIÓN
Los contribuyentes habilitados a la emisión de boletas electrónicas y/p boletas no afectas o exentas electrónicas deben enviar al SII en forma
DIARIA, este archivo electrónico para reportar las ventas que ha realizado cada día. En caso de no reportar ventas, debe enviar este reporte con
valores en cero.

Página 3 de 8

2.- CONTENIDO DE ARCHIVO DE RESUMEN DE VENTAS DIARIAS.
2.1- Carátula: Área donde se informa datos del emisor, fecha del Resumen.
2.2- Resumen: Área donde se informa la cantidad de documentos emitidos, y montos asociados a los totales emitidos, para cada documento
requerido.
2.3- Firma: Firma electrónica sobre el archivo.
Códigos de Obligatoriedad:
1: Dato obligatorio: El dato debe estar en el documento siempre.
2: Dato condicional: El dato no es obligatorio en todos los resúmenes, pero pasa a ser obligatorio en determinados casos si se cumple una cierta
condición.
3: Opcional.
A continuación, se especifica el contenido de cada Zona, formato de cada dato de la zona, y códigos de obligatoriedad del dato. Los nombres y
características son similares a la Factura Electrónica.
Zonas del Documento
Carátula
Resumen
Firma

OBLIGATORIEDAD DE LA ZONA

1
1
1

Página 4 de 8

2.1 Carátula
N°

Campo

Tipo

Largo
Máximo

Observaciones Generales

Obligatoriedad

1

RUT Contribuyente

ALFA

10

Corresponde al Rut del contribuyente emisor con guion y dígito
verificador

1

2

RUT Envía

ALFA

10

Corresponde al Rut del usuario autorizado por el contribuyente
que hace el envío al SII

1

3

Fecha Resolución

ALFA

10

4

Número Resolución

NUM

6

ALFA

10

Fecha del primer día a que corresponde el Resumen, en
formato AAAA-MM-DD (Año (4),
Mes (2), Día (2)).

1

ALFA

10

Fecha del último día a que corresponde el Resumen, en
formato AAAA-MM-DD (Año (4),
Mes (2), Día (2)).

1

1

1

5

6

Fecha de Inicio del Resumen
En caso de servicios periódicos,
considerar la fecha de vencimiento de los
documentos1
Fecha Final del Resumen
En caso de servicios periódicos,
considerar la fecha de vencimiento de los
documentos1

AAAA-MM-DD, Fecha de Resolución que autoriza al
contribuyente a emitir DTE.
Número de Resolución que autoriza al contribuyente como emisor
de DTE.

7

Secuencia de Envío

NUM

3

Secuencia de Envío. La primera vez que se envía debe traer
el número 1. Si se desea
corregir información se debe enviar el archivo completo, pero
"SecEnvio", debe aumentar en
1, es decir la segunda vez debe traer el valor 2, la tercera vez
debe traer el valor 3, etc.

8

Fecha y hora de la firma digital del envío

ALFA

19

AAAA-MM-DDTHH:MI:SS Fecha-Hora de Firma

1
1

NOTA: Para los documentos que se exija este resumen en forma diaria la fecha de Inicio del Resumen debe ser igual a la fecha de Final del
Resumen.

1

Los servicios periódicos domiciliarios son aquellos identificados en DL 825, Art. 9° en que el impuesto se devenga en la fecha de vencimiento

Página 5 de 8

2.2 Resumen

N°

Campo

Tipo

Largo
Máximo

Observaciones Generales
Indica que el documento informado es:
39: Boleta Electrónica.
41: Boleta No Afecta Exenta Electrónica.
Total Monto Neto (Afecto) de documentos emitidos informados.
En caso de Boletas Electrónicas en que la cantidad de
documentos emitidos sea mayor que 0, debe contener valor
mayor o igual a 0. En el caso de Boletas No Afectas o Exentas
Electrónicas debe ser cero.
Total IVA de documentos emitidos informados. En caso de
Boletas Electrónicas en que la cantidad de documentos emitidos
sea mayor que 0, debe contener valor mayor o igual a 0 e igual a
Monto Neto * Tasa IVA. En el caso de Boletas No Afectas o
Exentas Electrónicas debería ser cero.

Obligatoriedad

1

Tipo de Documento

NUM

2

2

TOTAL MONTO NETO

NUM

18

3

TOTAL MONTO IVA

NUM

18

4

TASA IVA

NUM

5

3 enteros, 2 decimales En Porcentaje (Ej: 19,50)

3

2

1

2

2

5

TOTAL MONTO NO AFECTO O EXENTO

NUM

18

Total Monto No Afecto o Exento de documentos emitidos
informados. En el caso de Boletas No Afectas
Exentas
Electrónicas en que la cantidad de documentos emitidos en el día
sea mayor que 0, debe contener valor mayor o igual a 0.

6

TOTAL MONTO TOTAL

NUM

18

Suma de totales (neto, IVA y no afecto) para cada tipo de
documento.

1

7

Cantidad de documentos emitidos en el
periodo

10

Cantidad de Documentos del tipo correspondiente a emitidos. Se
debe indicar la cantidad total de documentos emitidos en el
período. Si no hay documentos emitidos del tipo especificado, en
el período indicado en la carátula, se debe registrar 0.

1

10

En este campo indicar Cantidad de Folios de documentos del tipo
correspondiente anulados. se refiere a los folios anulados en el
sistema que no corresponden a documentos enviados al SII
(Opción anulación de folios) y no a Documentos anulados
mediante Notas de Crédito Electrónicas.

1

8

Cantidad de folios anulados en el periodo

NUM

NUM

Página 6 de 8

9

Cantidad de documentos utilizados en el
periodo

NUM

Cantidad de Documentos del tipo correspondiente a emitidos y
anulados. Si no informa folios anulados, se repite cantidad de
documentos emitidos.
Tabla que contiene un rango de folios CONSECUTIVOS utilizados
(Hasta 5.000 posibles repeticiones). La suma total de los folios
utilizados debe ser igual a “Cantidad de documentos utilizados en
el periodo”.
Número de folio inicial del rango de folios utilizados en el período.
Debe ser mayor que el “folio utilizado final” del rango precedente.
Número de folio final del rango de folios utilizados en el período.
Debe ser mayor que “Folio Utilizado Inicial”
Tabla que contiene los folios CONSECUTIVOS anulados (Hasta
5.000 posibles repeticiones). La suma total de los folios anulados
debe ser igual a la “Cantidad de Folios anulados en el período”.
Número de folio inicial de rango de folios anulados. O folio
individual anulado si no se trata de un rango (Inicial – Final).
Número de folio final de rango de folios anulados.(puede omitirse
cuando se reporta folio individual.

10

Tabla de rangos utilizados (emitidos y
anulados)
10

Folio Utilizado Inicial (Desde)

NUM

10

11

Folio Utilizado Final (Hasta)

NUM

10

Tabla de folios anulados
12

Folio Anulado (O folio anulado Inicial)

NUM

10

13

Folio Anulado Final

NUM

10

3.- EJEMPLOS.
3.1 A continuación ejemplo:

N°

Nombre del Campo

Valor

1

Tipo de Documento

2

TOTAL MONTO NETO

1000000

3

TOTAL MONTO IVA

190000

4

TASA IVA

19,00

5

TOTAL MONTO NO AFECTO O EXENTO

39

0

2

2

1
1
2
1
3

Página 7 de 8

6

TOTAL MONTO TOTAL

7

Cantidad de documentos emitidos en el
periodo

134

8

Cantidad de folios anulados en el periodo

16

9

Cantidad de documentos utilizados en el
periodo

150

1190000

Tabla de rangos de folios emitidos
10

Folio Utilizado Inicial (Desde)

1

11

Folio Utilizado Final (Hasta)

20

10

Folio Utilizado Inicial (Desde)

29

11

Folio Utilizado Final (Hasta)

50

10

Folio Utilizado Inicial (Desde)

103

11

Folio Utilizado Final (Hasta)

150

10

Folio Utilizado Inicial (Desde)

201

11

Folio Utilizado Final (Hasta)

234

10

Folio Utilizado Inicial (Desde)

240

11

Folio Utilizado Final (Hasta)

244

10

Folio Utilizado Inicial (Desde)

246

11

Folio Utilizado Final (Hasta)

250

Tabla de rangos de folios anulados
12

Folio Anulado Inicial

21

13

Folio Anulado Final

28

12

Folio Anulado

101

12

Folio Anulado

102

Página 8 de 8

12

Folio Anulado Inicial

235

13

Folio Anulado Final

239

3.2 A continuación ejemplos de errores:
Tabla de rangos de folios emitidos
10

Folio Utilizado Inicial (Desde)

1

11

Folio Utilizado Final (Hasta)

50

10

Folio Utilizado Inicial (Desde)

25

11

Folio Utilizado Final (Hasta)

30

10

Folio Utilizado Inicial (Desde)

250

11

Folio Utilizado Final (Hasta)

200

Este valor debe ser mayor de 50

El valor inicial debe ser menor al valor final

Tabla de rangos de folios anulados
12

Folio Anulado Inicial

120

13

Folio Anulado Final

115

El valor inicial debe ser menor al valor final
