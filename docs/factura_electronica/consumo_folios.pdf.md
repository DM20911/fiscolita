---
url: https://www.sii.cl/factura_electronica/consumo_folios.pdf
titulo: FORMATO ARCHIVO ELECTRÓNICO REPORTE CONSUMO DE FOLIOS
categoria: factura_electronica
---
FORMATO ARCHIVO ELECTRÓNICO REPORTE CONSUMO DE FOLIOS

5 Febrero 2009
Versión 1.0

Servicio Impuestos Internos
Formato Consumo de Folios

BITÁCORA DE CAMBIOS
Cambios 05/02/2009
1)

Se actualiza ejemplos de rangos de folios emitidos y anulados.

Versión 1.0 2009-02-05

Pág. 2 de 9

Servicio Impuestos Internos
Formato Consumo de Folios

FORMATO REPORTE CONSUMO DE FOLIOS
FORMATO ARCHIVO ELECTRÓNICO REPORTE CONSUMO DE FOLIOS................................................................... 1
BITÁCORA DE CAMBIOS.................................................................................................................................................... 2
1.- INTRODUCCIÓN ................................................................................................................................................................................4
2.- CONTENIDO DE ARCHIVO DE REPORTE DE CONSUMO DE FOLIOS. ..............................................................................4
2.1 Carátula Reporte Consumo de Folios.................................................................................................................................................5
2.2 Resumen .............................................................................................................................................................................................6
3.- EJEMPLOS. ..........................................................................................................................................................................................7

Versión 1.0 2009-02-05

Pág. 3 de 9

Servicio Impuestos Internos
Formato Consumo de Folios

1.- INTRODUCCIÓN

Al contribuyente autorizado a operar como emisor electrónico de algún tipo de Documento Tributario Electrónico (DTE) específico se
le podría requerir que entregue un reporte periódico de cómo ha utilizado los folios autorizados en sus documentos. Específicamente,
esto es un requerimiento para los contribuyentes autorizados a la emisión de boletas electrónicas y boletas electrónicas exentas o no
afectas. Los contribuyentes autorizados a la emisión electrónica de este tipo de documentos deben enviar al SII en forma DIARIA,
este archivo electrónico para reportar los folios que han utilizado cada día.

2.- CONTENIDO DE ARCHIVO DE REPORTE DE CONSUMO DE FOLIOS.
2.1- Carátula Consumo de folios: Área donde se informa datos del emisor, fecha del Reporte.
2.2- Resumen de Consumo de folios: Área donde se informa el consumo total de folios, y montos asociados a los totales emitidos,
para cada documento requerido.
2.3- Firma Electrónica SII: Firma electrónica sobre el archivo.
Códigos de Obligatoriedad:
1: Dato obligatorio: El dato debe estar en el documento siempre.
2: Dato condicional: El dato no es obligatorio en todos los resúmenes, pero pasa a ser obligatorio en determinados casos si se
cumple una cierta condición.
A continuación se especifica el contenido de cada Zona, formato de cada dato de la zona, y códigos de obligatoriedad del dato. Los
nombres y características son similares a la Factura Electrónica.
Zonas del Documento

OBLIGATORIEDAD DE LA ZONA

Carátula

1

Resumen

1

Firma

1

Versión 1.0 2009-02-05

Pág. 4 de 9

Servicio Impuestos Internos
Formato Consumo de Folios

2.1 Carátula Reporte Consumo de Folios
N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

1

RUT Contribuyente

ALFA

10

Corresponde al Rut del contribuyente emisor con guión y dígito verificador

1

2

RUT Enviador

ALFA

10

Corresponde al Rut del usuario autorizado por el contribuyente que hace el envío al SII

1

3

Fecha Resolución

ALFA

10

AAAA-MM-DD, Fecha de Resolución que autoriza al contribuyente a emitir DTE.

1

4

Número Resolución

NUM

6

Número de Resolución que autoriza al contribuyente como emisor de DTE.

1

5

Fecha de Inicio del Resumen

ALFA

10

Fecha del primer día a que corresponde el Resumen, en formato AAAA-MM-DD (Año (4),
Mes (2), Día (2)).

1

6

Fecha Final del Resumen

ALFA

10

Fecha del último día a que corresponde el Resumen, en formato AAAA-MM-DD (Año (4),
Mes (2), Día (2)).

1

Secuencia de Envío

NUM

3

Secuencia de Envío. La primera vez que se envía debe traer el numero 1. Si se desea
corregir información se debe enviar el archivo completo, pero "SecEnvio", debe aumentar en
1, es decir la segunda vez debe traer el valor 2, la tercera vez debe traer el valor 3, etc.

1

ALFA

19

AAAA-MM-DDTHH:MI:SS Fecha-Hora de Firma

1

7

8

Fecha y hora de la firma digital del envío

OBSERVACIONES GENERALES

Obligatoriedad

NOTA: Para los documentos que se exija este resumen en forma diaria la fecha de Inicio del Resumen debe ser
igual a la fecha de Final del Resumen.

Versión 1.0 2009-02-05

Pág. 5 de 9

Servicio Impuestos Internos
Formato Consumo de Folios

2.2 Resumen
N° NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

1

NUM

2

Tipo de Documento

Obligatoriedad

OBSERVACIONES GENERALES
Indica que el documento informado es:

1

39: Boleta Electrónica.
41: Boleta Exenta Electrónica.
61: Nota de Crédito
2

TOTAL MONTO NETO

NUM

18

Total Monto Neto (Afecto) de documentos emitidos informados.
En caso de Boletas Electrónicas en que la cantidad de documentos emitidos sea mayor que 0,
debe contener valor mayor o igual a 0.
En el caso de Boletas Exentas Electrónicas debería ser cero.

2

3

TOTAL MONTO IVA

NUM

18

Total IVA de documentos emitidos informados.
En caso de Boletas Electrónicas en que la cantidad de documentos emitidos sea mayor que 0,
debe contener valor mayor o igual a 0 e igual a Monto Neto * Tasa Iva.
En el caso de Boletas Exentas Electrónicas debería ser cero.

2

4

TASA IVA

NUM

5

3 enteros, 2 decimales En Porcentaje (Ej: 19,50)

3

5

TOTAL MONTO NO AFECTO O EXENTO

NUM

18

Total Monto No Afecto o Exento de documentos emitidos informados.
En el caso de Boletas Exentas Electrónicas en que la cantidad de documentos emitidos en el día
sea mayor que 0, debe contener valor mayor o igual a 0.

2

6

TOTAL MONTO TOTAL

NUM

18

Suma de totales (neto, IVA y no afecto) para el tipo de documento.

1

7

Cantidad de documentos emitidos en el período.

NUM

10

8

Cantidad de Folios anulados en el período.

NUM

10

9

Cantidad de documentos utilizados en el periodo.

NUM

10

Tabla rango de folios utilizados ( emitidos +
anulados)
10 Folio Utilizado Inicial (Desde)

NUM

10

11 Folio Utilizado Final (Hasta)

NUM

10

Tabla de folios anulados
12 Folio Anulado (O folio anulado Inicial)

NUM

10

13 Folio Anulado Final

NUM

10

Cantidad de Documentos del tipo correspondiente a emitidos. Se debe indicar la cantidad total de
documentos emitidos en el período. Si no hay documentos emitidos del tipo especificado, en el
período indicado en la carátula, se debe registrar 0.
En este campo indicar Cantidad de Folios de documentos del tipo correspondiente anulados. se
refiere a los folios anulados en el sistema que no corresponden a documentos enviados al SII
(Opción anulación de folios) y no a Documentos anulados mediante Notas de Crédito.

1

1

Cantidad de Documentos del tipo correspondiente a emitidos y anulados.
Tabla que contiene un rango de folios CONSECUTIVOS utilizados (Hasta 5.000 posibles
repeticiones) . La suma total de los folios utilizados debe ser igual a “Cantidad de documentos
utilizados en el periodo”.
Número del folio inicial del rango de folios utilizados en el período. Debe ser mayor que el “folio
utilizado final” del rango precedente.
Número del folio final del rango de folios utilizados en el período. Debe ser mayor que “Folio
Utilizado Inicial”
Tabla que contiene los folios CONSECUTIVOS anulados (Hasta 5.000 posibles repeticiones). La
suma total de los folios anulados debe ser igual a la “Cantidad de Folios anulados en el período”.
Número del folio inicial de rango de folios anulados. O folio individual anulado si no se trata de
un rango (Inicial – Final).
Número del folio final de rango de folios anulados.(puede omitirse cuando se reporta folio
individual.

Versión 1.0 2009-02-05

Pág. 6 de 9

2

1
1
2
1
3

Servicio Impuestos Internos
Formato Consumo de Folios

3.- EJEMPLOS.

3.1 A continuación se muestra un ejemplo:
N°

NOMBRE DEL CAMPO

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

5

TOTAL MONTO NO AFECTO O EXENTO

6

TOTAL MONTO TOTAL

7

Cantidad de documentos emitidos en el período.

134

8

Cantidad de Folios anulados en el período.

16

9

Cantidad de documentos utilizados en el periodo

150

39

19,00
0
1190000

Tabla rango de folios emitidos
10 Folio Utilizado Inicial (Desde)

1

11 Folio Utilizado Final (Hasta)

20

10 Folio Utilizado Inicial (Desde)

29

11 Folio Utilizado Final (Hasta)

50

10 Folio Utilizado Inicial (Desde)

103

11 Folio Utilizado Final (Hasta)

150

10 Folio Utilizado Inicial (Desde)

201

11 Folio Utilizado Final (Hasta)

234

10 Folio Utilizado Inicial (Desde)

240

11 Folio Utilizado Final (Hasta)

244

10 Folio Utilizado Inicial (Desde)

246

11 Folio Utilizado Final (Hasta)

250

Versión 1.0 2009-02-05

Pág. 7 de 9

Servicio Impuestos Internos
Formato Consumo de Folios
Tabla de folios anulados
12 Folio Anulado Inicial

21

13 Folio Anulado Final

28

12 Folio Anulado

101

12 Folio Anulado

102

12 Folio Anulado Inicial

235

13 Folio Anulado Final

239

12 Folio Anulado

245

Versión 1.0 2009-02-05

Pág. 8 de 9

Servicio Impuestos Internos
Formato Consumo de Folios

3.2 A continuación se muestra un ejemplo tabla de Rangos de Folios Emitidos ERRONEO:
Tabla rango de folios emitidos
10 Folio Utilizado Inicial (Desde)

1

11 Folio Utilizado Final (Hasta)

50

10 Folio Utilizado Inicial (Desde)

25

11 Folio Utilizado Final (Hasta)

30

10 Folio Utilizado Inicial (Desde)

250

11 Folio Utilizado Final (Hasta)

200

Este valor debe ser mayor que 50.

El valor inicial debe ser menor el valor final

3.2 B continuación se muestra un ejemplo tabla de Rangos de Folios Anulados ERRONEO.
Asumiendo que la tabla de Rangos de Folios utilizados es la del ejemplo 3.1, entonces:
Tabla rango de folios anulados
12 Folio Utilizado Inicial (Desde)

120

13 Folio Utilizado Final (Hasta)

115

Versión 1.0 2009-02-05

El valor inicial debe ser menor el valor final.

Pág. 9 de 9
