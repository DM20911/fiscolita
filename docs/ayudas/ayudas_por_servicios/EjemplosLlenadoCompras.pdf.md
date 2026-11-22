---
url: https://www.sii.cl/ayudas/ayudas_por_servicios/EjemplosLlenadoCompras.pdf
titulo: Registro de Compras.
categoria: ayuda
---
Registro de Compras.

Ejemplos de Ingreso de Documentos
Tributarios no Electrónicos en el Registro
de Compras
01-07-2017 Versión 1.0

SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

Ejemplos de Ingreso de Documentos Tributarios no
Electrónicos en el Registro de Compras
1. REGISTRO DE FACTURAS DE PROVEEDORES.
Las facturas de proveedores corresponden a un código de documento 30.

1.1

Factura recibida de Proveedores con IVA Recuperable.

El campo destinado a IVA recuperable se utiliza cuando se tiene derecho al 100% del crédito fiscal asociado al documento. La
información que se registra en este campo debe ser consistente con lo registrado en el Formulario 29 de Declaración Mensual y Pago
Simultáneo de Impuestos (Facturas recibidas del giro, código 520).
En estos casos no se deben completar los campos Monto IVA No Recuperable ni Monto IVA Uso Común.
Ejemplo:
Monto Neto
IVA
Total
Tipo de Transacción de Compra

100.000
19.000
119.000
Del Giro

Las facturas de proveedores (código de documento 30) con IVA Recuperable, se deben registrar en los siguientes campos:
Tipo de
Folio del
RUT del
Tasa de
Documento Documento Proveedor Impuesto

30

10

123-1

19

Nombre o Tipo de
Impuesto
Razón
Social

AAAA

1

Fecha de
emisión del
Documento

01-07-2017

Monto Neto Monto IVA
Recuperable

100000

19000

Monto
Total

Tipo de
Transacción
de Compra

119000

1

2
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

1.2

Factura recibida de Proveedores con IVA No Recuperable.

El campo destinado a IVA No recuperable se utiliza cuando se sabe, al momento de registrar el documento, que el IVA de dicho
documento no tendrá derecho a ser recuperado por ser una compra destinada a operaciones exentas o no gravadas, estar
registrado fuera de plazo, corresponder a entregas gratuitas o corresponder a gastos rechazados.
En estos casos no se debe completar el campo Monto IVA Uso Común y en el campo Monto IVA Recuperable se debe indicar “0”.
Ejemplo:
Monto Neto
IVA
Total
Tipo de Transacción de Compra

100.000
19.000
119.000
Compra sin Derecho a Crédito

Las facturas de proveedores (código de documentos 30) con IVA No Recuperable, se deben registrar en los siguientes campos:

Tipo de
Documento

Folio del
Documento

30

10

RUT del Tasa de
Proveedor Impuesto

123-1

19

Tipo de
Nombre o
Fecha de
emisión del
Razón
Impuesto
Documento
Social

Monto
Neto

AAAA

100000

1

01-07-2017

Monto IVA
Recuperable

0

Código IVA
Monto IVA
No
No
Recuperable Recuperable

9

19000

Monto
Total

Tipo de
Transacción
de Compra

119000

6

3
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

1.3

Factura recibida de Proveedores con IVA Uso Común.

El campo IVA de uso común es utilizado cuando el crédito fiscal de una factura está asociado tanto a operaciones afectas como
exentas o no gravadas y, el monto de IVA a recuperar se debe determinar de acuerdo a lo establecido en el artículo 43 del Decreto
Supremo N° 55, de 1977 (Reglamento de la Ley sobre Impuesto a las Ventas y Servicios), relacionado con la proporcionalidad del
Crédito Fiscal.
Se debe registrar la totalidad del IVA en el campo Monto IVA Uso Común, y luego se deberá ingresar el porcentaje de proporcionalidad
correspondiente para cada tipo de documento. El sistema identifica aquellos Registros de Compra en los cuales se utilizan campos de
proporcionalidad del IVA, como por ejemplo [IVA Uso Común]. En tales casos, en la pantalla de Visualización de resúmenes se
presenta un recuadro en el cual el usuario debe completar dicho Factor de Proporcionalidad para finalmente completar este proceso.
(en el futuro dicho campo se calculará sólo y en forma automática considerando la información ingresada a los Registros de Compras)
En estos casos no se debe completar el campo Monto IVA No Recuperable y en el campo Monto IVA Recuperable se debe indicar
“0”.
Ejemplo:
Monto Neto
IVA
Total
Tipo de Transacción de Compra

100.000
19.000
119.000
Del Giro

Las facturas de proveedores (código de documento 30) con IVA Uso Común, se deben registrar en los siguientes campos:

Tipo de
Documento

Folio del
Documento

RUT del
Proveedor

Tasa de
Impuesto

Nombre o
Razón
Social

Tipo de
Impuesto

Fecha de
emisión del
Documento

Monto
Neto

33

10

123-1

19

AAAA

1

01-07-2017

100000

Monto IVA
Monto IVA
Recuperable Uso Común

0

19000

Monto
Total

Tipo de
Transacción
de Compra

119000

1

4
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

2. REGISTRO DE FACTURAS DE COMPRAS EMITIDAS.
Las facturas de compras tiene el código de documento 45.

2.1

Factura de Compra emitida con Retención Total.

En estos casos el que emite el documento es el Comprador, quien debe retener y declarar en el Formulario 29 de Declaración Mensual
y Pago Simultáneo de Impuestos, el total del IVA asociado a la operación.
Ejemplo:
Monto Neto
19% de IVA a retener
Subtotal
Menos IVA Retenido
Total
Tipo de Transacción de Compra

100.000
19.000
119.000
(19.000)
100.000
Del Giro

Las facturas de compras emitidas (código de documentos 45), se deben registrar en los siguientes campos:

Tipo de
Folio del
RUT del Tasa de
Documento Documento Proveedor Impuesto

45

10

123-1

19

Tipo de
Nombre
Impuesto
o
Razón
Social

AAAA

1

Fecha de
emisión del
Documento

01-07-2017

Código
Tasa Otro Monto Otro
Otro
Impuesto o Impuesto o
Impuesto o Retención
Retención
Monto
Monto IVA Retención
(Con
(Con
Neto
Recuperable
Crédito)
(Con
Crédito)
Crédito)
100000

19000

38

19

19000

Monto
Total

100000

Tipo de
Transacción
de Compra

1

Para registrar el IVA de estos documentos se debe tener en considerar si corresponde a IVA Recuperable, No Recuperable o IVA Uso
Común (de acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

5
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

2.2

Factura de Compra emitida con Retención Parcial.

En estos casos el que emite el documento es el Comprador, quien debe retener y declarar en el Formulario 29 de Declaración Mensual
y Pago Simultáneo de Impuestos, el IVA retenido parcial asociado a la operación.
Ejemplo:
Monto Neto
100.000
10% de IVA a retener
10.000
9% de IVA No Retenido
9.000
Subtotal
119.000
Menos 10% IVA Retenido
(10.000)
Total
109.000
Tipo de Compra
Del Giro
Nota: el porcentaje de IVA a retener y el no retenido dependerá del fijado por el SII para un determinado producto.
Las facturas de compras emitidas (código de documento 45), se deben registrar en los siguientes campos:
Tipo de
Nombre Impuesto
o
Fecha de
Tipo de
Folio del
RUT del Tasa de
emisión del
Documento Documento Proveedor Impuesto Razón
Social
Documento

45

10

123-1

19

AAAA

1

01-07-2017

Código
Otro
Impuesto
o
Monto Monto IVA
Neto Recuperable Retención
(Con
Crédito)
100000

19000

36

Tasa Otro
Impuesto o
Retención
(Con
Crédito)

Monto Otro
Impuesto o
Retención
(Con
Crédito)

Monto
IVA No
Retenido

10

10000

9000

Monto
Total

109000

En este caso no se registró el campo “Tipo de Transacción de Compra”, lo cual es asumido por el sistema como una compra “Del
Giro”.
Se debe tener en consideración para registrar el IVA, si corresponde a IVA Recuperable, No Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

6
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

2.3

Registro de Facturas de Compra anuladas.

Las facturas de compra no electrónicas que se hayan anulado, como también aquellas facturas de compra electrónicas anuladas, que
NO se hayan enviado al SII, y cuyo folio se encuentre anulado en la aplicación de timbraje electrónico, no deben informarse al Registro
de Compras.
Las facturas de compra electrónicas que se hayan enviado al SII, se anulan con una nota de crédito, por lo que no debe indicarse
información algún en el Registro de Compras que se encuentra anulada, debido a que es suficiente con el registro de la nota de crédito
electrónica que se emita, para informar que se ha anulado el documento.
Entonces, las facturas de compras no electrónicas (código de documento 45) y las facturas de compra electrónicas (código de
documento 46) NO enviadas al SII y que hayan sido anuladas no se debe realizar indicación alguna en el Registro de Compras.

7
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

2.4

Registro de Notas de Débito o Notas de Crédito por Facturas de Compra.

Las notas de débito (código 55), y las notas de crédito (código de documento 60), emitidas por facturas de compras (código
45) emitidas, se consignan de la siguiente forma en el Registro de Compras
Ejemplo de nota de crédito relacionada a una factura de compra con retención total:
Monto Neto Nota de Débito
19% de IVA a retener
Subtotal
Menos IVA Retenido
Total

10.000
1.900
11.900
(1.900)
10.000

Las notas de crédito o de las notas de débito emitidas por facturas de compras, se deben registrar en los siguientes campos:
Tipo de
Tipo de
Folio del
RUT del Tasa de Nombre Impuesto
o
Documento Documento Proveedor Impuesto
Razón
Social

55

10

123-1

19

AAAA

1

Fecha de
emisión del
Documento

01-07-2017

Código Tasa Otro Monto Otro Notas de
Otro
Impuesto Impuesto o Débito o
Impuesto
o
Retención
Crédito
Monto
o
Retención
(Con
por
Neto Monto IVA Retención
Crédito) Facturas
(Con
Recuperable
(Con
Crédito)
de
Crédito)
Compra
10000

1900

38

19

1900

1

Monto
Total

10000

Es importante indicar que en caso que no se informe el campo “Notas de Débito o Crédito por Facturas de Compra”, la Nota de
Débito o Crédito emitida, se entenderá consignada en el Registro de Compras como recibida y no como emitida.
Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).
8
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

3. REGISTRO DE FACTURAS DE PROVEEDORES POR COMPRAS DE ACTIVO FIJO.
Ejemplo:

Monto Neto
IVA
Total
Tipo de Compra

100.000
19.000
119.000
Activo Fijo

Las facturas de proveedores por adquisiciones de Activo Fijo (código de documento 30), se deben registrar en los siguientes campos:

Tipo de
Folio del
RUT del Tasa de
Documento Documento Proveedor Impuesto

30

10

123-1

19

Nombre o Tipo de
Impuesto
Razón
Social

AAAA

1

Fecha de
emisión del
Documento

Monto
Neto

01-07-2017 100000

Monto IVA
Recuperable

Monto
Neto
Activo Fijo

Monto
IVA
Activo
Fijo

Monto
Total

Tipo de
Transacción
de Compra

19000

100000

19000

119000

4

Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

9
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

4. REGISTRO DE FACTURAS DE PROVEEDORES CON IMPUESTOS ADICIONALES O
ESPECÍFICOS.
En estos casos se debe registrar lo siguiente: Impuestos adicionales Art. 37 o 42, del D.L. N° 825, de 1974 (alcoholes y bebidas
analcohólicas); el Impuesto Específico al Petróleo Diesel soportado por transportistas de carga (Ley 19.764), Impuesto al Gas Natural
Comprimido y Gas Licuado de Petróleo (Ley 20.052); y el Impuesto Específico al Petróleo Diesel y a las Gasolinas (Ley 18.502).

4.1

Factura recibida de Proveedores con Impuestos Adicionales o Específicos Sin Derecho a
Crédito.

Ejemplo Impuesto Adicional Art. 42:
Monto Neto
100.000
19% IVA
19.000
20,5% ILA (Vinos)
20.500
Total
139.500
Tipo de Compra
Con Derecho a Crédito IVA, pero sin Derecho a Crédito Impuesto Adicional (Se consigna
como “2”, tipo compra en “Supermercado o comercios similares”)
Las facturas de proveedores recibidas con Impuestos Adicionales o Específicos Sin Derecho a Crédito, se deben registrar en los
siguientes campos:
Nombre o
Tipo de
Folio del
RUT del Tasa de
Razón
Documento Documento Proveedor Impuesto
Social

30

10

123-1

19

AAAA

Tipo de
Impuesto

1

Fecha de
emisión del
Documento

Monto
Neto

01-07-2017

100000

Monto Otro
Monto IVA
Impuesto (Sin
Recuperable
Crédito)

19000

20500

Monto
Total

Tipo de
Transacción
de Compra

139500

2

Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).
En caso de tratarse de más de un tipo de Impuesto Adicional sin derecho a Crédito, estos deben sumarse y registrarse de la misma
forma como si fuera uno solo.
El tipo de compra es valor = “2” en función que se trataría de una compra en establecimiento de venta al público final tipo
“Supermercado o similar”, y la compra en su totalidad se trataría como un gasto aceptado y el IVA sí podría utilizarse como crédito
10
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras
fiscal, aunque el o los Impuestos Adicionales no tendrían derecho a crédito, en razón que la compra no se destinaría directamente a
ser vendida luego con documentos con derecho a crédito fiscal. (En caso de dudas consultar el ejemplo siguiente del 4.2)

4.2

Factura recibida de Proveedores con Impuestos Adicionales o Específicos Con Derecho a
Crédito.

Ejemplo Impuesto Adicional Art. 42:

Monto Neto
19% IVA
20,5% ILA (Vinos)
Total
Tipo de Compra

100.000
19.000
20.500
139.500
Con Derecho a Crédito IVA y con Derecho a Crédito Impuesto Adicional, por lo que correspondería
a una Compra del Giro.

Las facturas de proveedores recibidas (código de documento 30) con Impuestos Adicionales o Específicos Con Derecho a Crédito,
se deben registrar en los siguientes campos:

Tipo de
Folio del
RUT del Tasa de
Documento Documento Proveedor Impuesto

30

10

123-1

19

Tipo de
Nombre Impuesto
Fecha de
o
emisión del
Razón
Documento
Social

AAA

1

01-072017

Código
Tasa Otro Monto Otro
Otro
Impuesto
Impuesto
Impuesto o
o
(Con
Monto Monto IVA
Retención Retención
Crédito)
Neto Recuperable
(Con
(Con
Crédito)
Crédito)

100000

19000

251

20.5

20500

Monto
Total

Tipo de
Transacción
de Compra

139500

1

1

Los códigos de Otros Impuestos y Retenciones se encuentran disponibles en Ayudas de Códigos de Impuesto. El Código N° 25 corresponde al Impuesto
Adicional a los vinos Art. 42, letra c).

11
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable, No Recuperable o IVA
Uso Común (de acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

4.3

Factura recibida de Proveedores con Impuestos Adicionales con más de un impuesto con
Derecho a Crédito.

Ejemplo Impuesto Adicional Art. 42:
Monto Neto
19% IVA
31,5% ILA (Licores, Piscos, destilados, etc.) ($ 30.000 * 31,5%)
20,5% ILA (Vinos) ($ 30.000 * 20,5%)
20,5% (Cervezas y bebidas alcohólicas) ($ 40.000 * 20,5%)
Total
Tipo de Compra

100.000
19.000
9.450
6.150
8.200
142.800
Con Derecho a Crédito IVA y con Derecho a Crédito Impuesto
Adicional, por lo que correspondería a una Compra del Giro.
Las facturas de proveedores recibidas (código de documento 30) con Impuestos Adicionales Con Derecho a Crédito, se deben
registrar en los siguientes campos:
Tipo de
Nombre Impuesto
Fecha de
Tipo de
Folio del
RUT del Tasa de
o
emisión del
Documento Documento Proveedor Impuesto Razón
Documento
Social

30

10

123-1

19

AAAA

1

30

10

123-1

19

AAAA

1

30

10

123-1

19

AAAA

1

01-072017
01-072017
01-072017

Código Tasa Otro
Otro
Impuesto
Impuesto
o
Monto Monto IVA
o
Retención
Neto Recuperable Retención
(Con
(Con
Créd)
Crédito)

Monto
Otro
Impuesto
(Con
Crédito)

Monto
Total
Tipo de
Transacción
de Compra

100000

19000

24

31.5

9450

142800

1

100000

19000

25

20.5

6150

142800

1

100000

19000

26

20.5

8200

142800

1

Los datos del documento que se deben repetir en todas las filas son:
12
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras
“Código Otro Impuesto o Retención”.
“Tasa Otro Impuesto o Retención”.
“Monto Otro Impuesto (Con Crédito)”.
Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

4.4 Factura recibida de Proveedores con Impuestos Específicos Con y Sin Derecho a Crédito.
Ejemplo Impuesto Específico a los Combustibles:
Supuesto: Transportista de Carga que por ingresos anuales propios del giro todo el IVA asociado al ejemplo es recuperable.
El monto a recuperar se determina aplicando el porcentaje establecido en la Ley 19.764, sobre el componente base facturado. Para el
ejemplo, se aplica el 80% considerando que los ingresos anuales propios del año calendario 2010 son 2.000 UF.
Monto Neto
19% IVA
Impuesto Específico Petróleo Componente Base (1,5 UTM/m3)
Impuesto Específico Bencina (6 UTM/m3 * 2m3)
Total

3.400.668
646.127
292.658
468.252
4.807.705

Tipo de Compra

Con Derecho a Crédito IVA y con Derecho a Crédito Impuesto
Adicional, por lo que correspondería a una Compra del Giro.
(salvo Bencina)

Las facturas de proveedores recibidas (código de documento 30) con Impuestos Adicionales Con Derecho a Crédito y Sin Derecho
a Crédito, se deben registrar en los siguientes campos:

13
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

Nombre
Tipo de Fecha de
Tipo de
Folio del
RUT del Tasa de
o
Impuesto emisión del
Documento Documento Proveedor Impuesto Razón
Documento
Social
30

10

123-1

19

AAAA

1

30

10

123-1

19

AAAA

1

01-072017
01-072017

Código Tasa Otro Monto
Otro
Impuesto
Otro
Monto Monto IVA
Impuesto
o
Impuesto
Neto Recuperable
o
Retención
(Con
Retención
Crédito)

Monto
Total

Tipo de
Transacción
de Compra

3400668

646127

28

1.5

292658

4807705

1

3400668

646127

35

6

468252

4807705

1

Impuesto adicional de Diesel debe registrarse completo como con derecho a crédito, la diferencia entre valor con derecho o sin
derecho a crédito deberá declararse correctamente luego en el F29.
Impuesto adicional de Bencina nunca tiene derecho a crédito, por lo cual al indicarse que es código 35, luego para cualquier efecto
se asumirá como sin crédito.

5. REGISTRO DE LIQUIDACIONES FACTURA.
Las Liquidaciones Factura (código de documento 40).
Registro de la Comisión de Liquidaciones Factura recibidas
En estos casos el receptor de la Liquidación Factura (Mandante), debe registrar la comisión de la operación.
Ejemplo:
Monto Neto Liquidación
19% IVA
Subtotal
Monto Neto Comisiones
19% IVA Comisión
Total

100.000
19.000
119.000
10.000
1.900
107.100

14
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras
El detalle de la comisión indicado en las liquidaciones factura recibidas se debe registrar en los siguientes campos:
Tipo de
Documento

Folio del
Documento

RUT del
Proveedor

Tasa de
Impuesto

40

10

123-1

19

Nombre o
Tipo de
Razón
Social
Impuesto

Fecha de
emisión del
Documento

Monto
Exento o No
Gravado

Monto
Neto

Monto IVA
Recuperable

Monto
Total

AAAA

01-04-2017

0

10000

1900

11900

1

Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).
En caso que no se informe el Tipo de Transacción de Compra se asume como “Del Giro”

6. REGISTRO DE FACTURAS DE VENTAS Y SERVICIOS NO AFECTOS O EXENTOS DE IVA.
Las Facturas de Ventas y Servicios no afectos o exentos de IVA (código de documento 32).
Ejemplo:

Monto Exento
Monto Total

100.000
100.000

Las facturas de ventas y servicios no afectos o exentos de IVA manuales y las facturas afectas o exentas electrónicas se deben
registrar en los siguientes campos:

15
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras

Tipo de
Folio del
RUT del
Documento Documento Proveedor

32

10

123-1

Nombre o
Razón Social

Fecha de
emisión del
Documento

Monto
Exento o No
Gravado

Monto
Total

AAAA

01-07-2017

100000

100000

REGISTRO DE LAS DECLARACIONES DE INGRESO (DIN).
Las Declaraciones de Ingreso (código de documento 914) deben ser registradas en el Libro de Compras en el periodo que
se efectúe el pago de los impuestos.
Ejemplo:
Antecedentes de la DIN:
Valor CIF en dólares
: US$ 10.000
Derecho Ad Valorem (Código 223 DIN)
: 0%
IVA en dólares (Código 178 DIN)
: US$ 1.900 (19% sobre la base valor CIF + Derecho Ad Valorem) Tipo
de Cambio (Cód. 61 DIN)
: $ 700
Antecedentes de la DIN que se deben calcular para su registro en la Información de Compras:
Valor CIF en pesos (US$ 10.000 x $ 500) : $ 7.000.000 (Base Imponible del IVA)
IVA en pesos (US$ 1.900 x $ 500)
: $1.330.000
Monto Total
: $ 8.330.000

16
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras
Las Declaraciones de Ingreso se deben registrar en los siguientes campos:
Tipo de
Folio del
RUT del
Documento Documento Proveedor2

914

10

Tasa
de
Nombre
Fecha de
Tipo de
Impues
o
emisión del
to
Razón Impuesto
Documento
Social

55555555-5

19

AAAA

1

Monto
Neto

01-07-2017 7000000

Monto Neto
Activo Fijo

Monto IVA
Recuperable

1330000

7000000

Monto IVA
Activo Fijo

Monto
Total

1330000 8330000

Tipo de
Transacción
de Compra

4

Si la importación corresponde a una adquisición de activo fijo, se deberá agregar dicha información al campo Monto Neto Activo Fijo y
al campo Monto IVA Activo Fijo, e indicar como Tipo de Transacción de Compra un valor = 4.
Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable o IVA Uso Común (de
acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

8. REGISTRO DE LAS FACTURAS DE INICIO RECIBIDAS.
La factura de inicio (código de documentos 29).
El comprador, al hacer uso de la Factura de Inicio está obligado a realizar la retención de los impuestos generados por la operación y
debe declararlos en su Formulario 29 de Declaración Mensual y Pago Simultáneo de Impuestos.
Ejemplo:
Monto Neto
19% de IVA a retener
Subtotal
Menos IVA Retenido
Total

100.000
19.000
119.000
(19.000)
100.000

Las facturas de inicio recibidas (código de documentos 29), se deben registrar en los siguientes campos:
2

Para el caso de las importaciones en el campo RUT del Proveedor, se debe ingresar el RUT: 55.555.555-5

17
SDAC– Versión 1.0

Ejemplos ingreso Registro de Compras
Nombre
o
Fecha de
Tipo de
Folio del
RUT del Tasa de
Monto
Tipo de
emisión del Neto
Razón
Documento Documento Proveedor Impuesto
Social Impuesto Documento

29

10

123-1

19

AAAA

1

01-07-2017

100000

Código
Tasa Otro
Otro
Impuesto o
Monto IVA
Impuesto o
Retención
Recuperable Retención (Con (Con Créd)
Crédito)
19000

60

19

Monto Otro
Impuesto o
Retención
(Con
Crédito)

Monto
Total

19000

100000

Tipo de
Transacción
de Compra

1

Para registrar el IVA de estos documentos se debe tener en consideración si corresponde a IVA Recuperable, No Recuperable o IVA
Uso Común (de acuerdo a lo indicado en los ejemplos para las facturas de proveedores).

18
SDAC– Versión 1.0
