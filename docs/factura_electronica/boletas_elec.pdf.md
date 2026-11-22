---
url: https://www.sii.cl/factura_electronica/boletas_elec.pdf
titulo: FORMATO BOLETAS ELECTRÓNICAS
categoria: factura_electronica
---
FORMATO BOLETAS ELECTRÓNICAS

2010-07-12
Versión 2.0

Servicio Impuestos Internos
Formato Boletas Electrónicas

FORMATO BOLETAS ELECTRÓNICAS
FORMATO BOLETAS ELECTRÓNICAS ............................................................................................................................ 1
BITÁCORA DE CAMBIOS...................................................................................................................................................................... 3
1.- INTRODUCCIÓN ................................................................................................................................................................................ 5
2.- DETALLE DE CONTENIDO DE LAS BOLETAS .......................................................................................................................... 5
A.- Encabezado ........................................................................................................................................................................................ 7
B.- Detalle de Productos o Servicios ...................................................................................................................................................... 10
C.- Subtotales Informativos.................................................................................................................................................................... 13
D.- Información de Descuentos o Recargos ........................................................................................................................................... 14
E.- Datos de Referencia .......................................................................................................................................................................... 15
F.- Timbre Electrónico SII del Documento. ........................................................................................................................................... 15

Versión 2.0 2010-07-12

Pág. 2 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

BITÁCORA DE CAMBIOS.
Cambios 2010 07 12
1. Se modifica el formato para incorporar datos de los ticket de espectáculos, para la emisión de boletas electrónicas
por cuenta de terceros.
2. En la sección A. Encabezado en el campo “Indicador Servicio” se agrega un cuarto tipo “boleta de espectáculo
emitida por cuenta de terceros”.
3. En la sección B. Detalle de Productos o Servicios:
a. Se agrega el campo “Item Espectaculo”
b. Se agrega el campo “Rut Mandante”
c. Se agregan los campos del Área “INFO TICKET”:
i. Folio Ticket
ii. Fecha Generación Ticket
iii. Nombre Evento
iv. Tipo Ticket
v. Código del Evento
vi. Fecha y Hora del Evento
vii. Lugar del Evento
viii. Ubicación en el Evento
ix. Fila Ubicación
x. Asiento Ubicación
d. Se modifica la descripción del campo “Nombre del Item”, indicando en caso que el campo “Item
Espectaculo” no sea nulo, este debe tener relación al ticket o al valor por servicio (comisión).
e. Se agrega el campo “Porcentaje de Descuento”
f. Se agrega el campo “Monto Descuento”
g. Se agrega el campo “Porcentaje de Recargo”
h. Se agrega el campo “Monto Recargo”
i. Se modifica descripción de los campos “Cantidad” y “Precio Unitario” indicando que se debe indicar en el
caso de venta de mercaderías o productos.
j. Se modifica descripción del campo “Valor por línea detalle” incorporando a la fórmula el descuento y
recargo.
4. En la sección E. Datos de Referencia se agregan los campos “Código Vendedor” y “Código Caja”.

Versión 2.0 2010-07-12

Pág. 3 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

Cambios 2005 08 05
1. Se hacen correcciones varias de forma y redacción.
2. Se incorporan indicadores de exención por no facturable (códigos 2 y 6).
Cambios 2005 04 15
3. Se explica la obligación de los emisores de boletas electrónicas de emitir diariamente un Reporte de Consumo de
Folios. (Ver nuevo documento electrónico Reporte de Consumo de Folios).
4. En la sección de Encabezado Se aumenta el largo máximo de los campos: “Nombre o Razón Social Emisor”,
“Dirección Origen”, “Ciudad Origen”, “Nombre Receptor”, Dirección Receptor”, “Ciudad Receptor”, “Dirección
postal” y “Ciudad Postal”.
5. En la sección de Encabezado, se modifica la obligatoriedad de información de los campos: “Comuna Receptor”,
“Ciudad Receptor”, “Monto neto” e “IVA”. Adicionalmente se modifica la obligatoriedad de impresión de los campos:
“Dirección postal”, “Comuna Postal” y “Ciudad Postal”
6. En el Rut Receptor se permite el uso de RUT genérico en caso de Boletas de Ventas y Servicios (no periódicos ni
domiciliarios): valor: 66.666.666-6
7. En la sección de Detalle, se incrementa el número máximo de líneas de 60 a 1000, y se incrementa el largo
máximo del campo “Tipo código” de 5 a 10, así como el campo “Descripción Adicional” se aumenta el largo de 180
a 1000.
8. En la sección de Referencias se reduce de 50 a 40 el número de líneas posibles de informar.
9. En la sección de Referencias se incrementa el largo del campo “Código referencia” de 10 a 18, y también el campo
“Razón referencia” de 30 a 90.
10. Se agrega una nueva área opcional de INFORMACIÓN DE SUBTOTALES.

Cambios 2004 01 12
1. En el XML se dejan como opcionales algunos campos que tenían obligatoriedad 4 (sólo impresión).
2. En el XML se modifica la carátula para indicar número de boletas exentas.

Versión 2.0 2010-07-12

Pág. 4 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

1.- INTRODUCCIÓN
En este documento se especifica el formato de las boletas. La empresa que emita boletas electrónicas debe generar un Libro de
Boletas con el resumen de las boletas electrónicas emitidas, el cual se describe en el documento “Formato de Libro de Boletas”.
A diferencia de las facturas electrónicas, las boletas emitidas no se deben enviar una a una al SII.
Las boletas se deberán mantener en la empresa durante seis años, en el formato XML que se establece en este documento.
Deben estar disponibles para consulta en línea en la sucursal para el mes en curso y para los dos meses anteriores.
El SII podrá solicitar información en medios tecnológicos para períodos anteriores.
Los contribuyentes emisores electrónicos que emitan boletas electrónicas en una sucursal, deben emitir la totalidad de su
documentación de forma electrónica en dicha sucursal.
Adicionalmente, los emisores de Boletas Electrónicas o Boletas No Afectas o Exentas Electrónicas que no son prestadores de
servicios periódicos deberán:
DIARIAMENTE generar y enviar al SII un “Reporte de Consumo de Folios”.
El emisor autorizado deberá publicar en un sitio Web las boletas electrónicas y boletas no afectas o exentas electrónicas emitidas.
Los documentos antes mencionados deberán estar a disposición para consulta por parte de los clientes, durante un período de tres
meses contados desde la emisión del documento. El sitio web donde estará disponible la consulta de la boleta electrónica deberá
estar señalado en la representación impresa como una leyenda bajo el timbre electrónico, por ejemplo: “Verifique documento:
http://www.consultaboletaelectronica.empresa.cl”

2.- DETALLE DE CONTENIDO DE LAS BOLETAS
A.- Datos de encabezado: corresponden a la identificación del documento, información del emisor, información del receptor y
monto total de la transacción.
B. - Detalle por Ítem: En esta zona se debe detallar al menos una línea. Se debe detallar el ítem cobrado, cantidad y valor.
C.- Timbre Electrónico SII: Firma electrónica sobre la información representativa del documento para permitir la validación del
documento impreso.
Códigos de Obligatoriedad:
1: Dato obligatorio. El dato debe estar en el documento siempre, independiente de las características de la transacción.
2: Dato condicional. El dato no es obligatorio en todas las boletas, pero pasa a ser obligatorio en determinadas operaciones si se cumple una
cierta condición.
3: Opcional.
4: Es obligatorio sólo en el documento impreso, pero no es obligatorio que se guarde en forma electrónica.

Versión 2.0 2010-07-12

Pág. 5 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

A continuación se especifica el contenido de cada Zona, formato de cada dato de la zona, y códigos de obligatoriedad del dato. Los nombres y
características son similares a la Factura electrónica.
Zonas del Documento

OBLIGATORIEDAD DE LA ZONA

Encabezado

1

Detalle

1

Subtotales Informativos

3

Descuentos y Recargos

2

Datos de Referencia

4

Timbre

1

En la columna I, se indica si el dato debe estar en la representación impresa del documento.
N = No es obligatorio que esté impreso.
I = Debe estar impresa. La impresión que se haga debe ser en un formato editado.
P = Debe estar impresa traduciendo el código a palabras.(ejemplo: en el documento electrónico el tipo de documento está codificado,
sin embargo en la representación impresa debe ir en palabras)

Versión 2.0 2010-07-12

Pág. 6 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

A.- Encabezado
CAMPOS

Largo

DESCRIPCIÓN

Tipo

Validación

I

MAX
1

VERSIÓN

2

Obligatoriedad de campo
Boleta
Boleta
exenta

3

Alfa

1.0

N

1

1

Tipo de Documento

Versión del Formato utilizado
Indica que el documento es:
39: Boleta Electrónica
41: Boleta No Afecta o Exenta Electrónica

2

NUM

De acuerdo con la descripción del
Campo

P

1

1

3

FOLIO –Documento

Folio autorizado por el SII

10

NUM

Campo NUM

I

1

1

4

Emisión Contable

Fecha de emisión del docto (AAAA-MM-DD)

10

ALFA

Fecha válida entre

I

1

1

2002-08-01 y 2050-12-31
5

Indicador Servicio

El objetivo del indicador es identificar el tipo de
transacción

1

NUM

1 Boletas de servicios periódicos
2 Boletas de servicios periódicos
domiciliarios
3 Boletas de venta y servicios
4 Boleta de Espectáculo emitida
por cuenta de Terceros

N

1

1

6

Indicador Montos Netos

Este indicador se utiliza para expresar que el
precio unitario y el valor de todas las líneas de
detalles corresponden a Montos netos, es decir no
incluyen el IVA. Sólo se aplica para empresas que
tienen autorización para emitir las boletas
desglosando el IVA.

1

NUM

2: Líneas de detalle indican
montos netos

N

2

0

7

Periodo Desde

10

ALFA

I

2

2

I

2

2

No aplica en boleta exenta

8

Periodo Hasta

9

Fecha de vencimiento
(pago)

10

Rut Emisor

11

Nombre o Razón Social
Emisor

Se usa para servicios periódicos
Se usa para servicios periódicos

10

ALFA

Fecha de vencimiento (AAAA-MM-DD).
Obligatorio, en caso de servicios periódicos
domiciliarios.

10

ALFA

Fecha válida entre

I

2

2

Con guión y dígito verificador

10

ALFA

2002-08-01 y 2050-12-31
Cuerpo numérico entre 100.000
y 99 millones, guión y dígito
verificador alfanumérico entre 0 y
9 o K

I

1

1

I

4

4

Dato opcional

100

Versión 2.0 2010-07-12

ALFA

Pág. 7 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

12

Giro del negocio del
Emisor1

Dato opcional. Se debe indicar el giro del emisor.
No es preciso registrar todos los giros, sino que se
podrá registrar sólo el giro que corresponde a la
transacción.

80

ALFA

I

4

4

13

Código sucursal

Código numérico entregado por el SII, que
identifica a cada sucursal que está identificada en
el Servicio de Impuestos Internos. Si no hay
sucursales se puede omitir.

9

NUM

N

2

2

14

Dirección Origen2

Datos correspondientes a Dirección de sucursal
desde donde se despachan bienes o de sucursal
que emite el documento si no hay despacho de
bienes. Dato opcional

70

ALFA

I

4

4

15

Comuna Origen

Dato opcional

20

ALFA

I

4

4

16
17

Ciudad Origen

Dato opcional
Rut del Cliente Receptor de la Boleta. Con guión y
dígito verificador.
Es obligatorio que venga un Rut válido o el
Código Interno.
Se acepta que venga un 0 en los casos en que el
cliente se identifica con Código Interno.
Se imprime si es distinto de 0 y de 66.666.666-6

20

ALFA

N

4

4

I

1

1

Para identificación adicional interna del Receptor,
por ejemplo código del cliente, número de medidor,
etc.

20

ALFA

I

2

2

40

ALFA

Sin validación

I

3

3

80

ALFA

Sin Validacion

N

3

3

18

19
20

Rut Receptor

Código Interno del Cliente

Nombre Receptor
Contacto Receptor

Dato obligatorio si Indicador Servicio =3 y RUT =
0, Opcional en otros casos
Nombre adicional o código adicional para
identificar al cliente.

10

ALFA

Cuerpo numérico, guión y dígito
verificador alfanumérico entre 0 y
9 o K. Debe venir un 0, cuando
el cliente se identifica sólo con
código interno.
Sólo en caso de Boletas de
Ventas y Servicios no periódicos
ni Domiciliarios, en caso de no
contar con el RUT o código
interno del cliente, se debe
utilizar el RUT genérico
66.666.666-6
Sin Validación
Si Rut es 0, obligatoriamente
debe ir Código interno del
cliente

1

Este dato puede ir preimpreso, indicando todos los giros autorizados del emisor, al igual que en la generación de documentos manuales. Pero
puede también ser un dato variable, en que se imprime sólo el giro que corresponde a la transacción.
2
La inclusión en el documento impreso puede ser hecho en forma similar a la generación de documentos manuales, en que en el anverso está
preimpresa la casa matriz y en el reverso o anverso están impresas todas las sucursales; se puede optar también por imprimir en forma variable
sólo la sucursal.

Versión 2.0 2010-07-12

Pág. 8 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

21

Dirección Receptor

22

Comuna Receptor

23
24
25

Dirección en que se otorga el Servicio en el caso
de Servicios otorgados en un domicilio o dirección
a la cual se envían bienes. Si es un servicio móvil,
se debe indicar la dirección de residencia del
cliente.
Es obligatorio si Indicador Servicio =1 o 2
Es opcional si Indicador Servicio =3

70

ALFA

Sin validación

I

2

2

Idem

20

ALFA

I

2

2

Ciudad Receptor

Ídem

20

ALFA

Sin Validación
Sin Validación

I

3

3

Dirección postal

Otra dirección registrada.

N

3

3

N

3

3

N

3

3

I

2

0

I

2

2

I

2

0

I

1

1

Comuna Postal

70

Ídem

20

ALFA
ALFA

Sin Validación
Sin Validación
Sin Validación

26

Ciudad Postal

Ídem

20

ALFA

27

Monto neto

Sólo es válido si el campo Indicador Montos
Netos tiene el valor 2.

18

NUM

18

NUM

18

NUM

18

NUM

18

NUM

Sin validación Puede ser negativo

N

2

2

18

NUM

N

2

2

18

NUM

N

3

3

18

NUM

Sin validación
Valor Numérico
(Puede ser negativo
de acuerdo a descripción)
Sin validación (Puede ser
negativo o cero
(de acuerdo a descripción)

N

3

3

28

Monto exento

29

IVA

30 Monto Total

31

Monto no Facturable

32 Total período
33

Saldo anterior

34

Valor a pagar

Se calcula como: Suma de Valor por línea de
detalle – Descuentos+ Recargos (de los items que
no tienen Indicador exención =2 )
Suma de Valor por línea de detalle para
Indicador Exención=1
Sólo es válido si Indicador Montos Netos tiene el
valor 2 y la boleta no es exenta.
Igual a la tasa (%) de IVA aplicada al Monto neto
a) Si no está presente el Indicador Montos
Netos se calcula como: Suma de Valor por
línea de detalle – Descuentos+ Recargos (de
los items que no tienen Indicador exención
=2 )
b) Si el si Indicador Montos Netos = 2, se calcula
como Monto neto + IVA + Monto Exento
Corresponde a la suma de montos de bienes o
servicios con Indicador exención = 2
Monto Total + Monto no Facturable
Saldo Anterior. Se incluye sólo con fines de
ilustrar con claridad el cobro.
Valor Cobrado
Valor total + Saldo anterior

Versión 2.0 2010-07-12

Valor Numérico > 0

Valor Numérico de acuerdo a
descripción.
Valor Numérico de acuerdo a
descripción.

Pág. 9 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

B.- Detalle de Productos o Servicios
Corresponde a la información de un ítem. Debe ir al menos una línea de detalle. El máximo de ítemes es de 1000.

CAMPOS

Largo

DESCRIPCIÓN

Tipo

I

Validación

MAX

Obligatoriedad
de campo
Boleta Boleta
exenta

1

N° de Línea o N° Secuencial

2

Tipo código

3

Código del ítem

4

Indicador exención

5

Item Espectáculo

Número del ítem. Desde 1 a 1000
Tipo de codificación utilizada
Standard: EAN, PLU, DUN o Interna
(Hasta 5 tipos de códigos)
Código del producto de acuerdo a tipo de
codificación indicada en campo anterior
Indica si el servicio es exento o no afecto a
impuesto o de monto no debe ser facturado.
En el caso que sea 2, no se debe considerar
para el cálculo del IVA del período.
No se usa para saldo anterior.

4
10

35
1

Indica si el ítem corresponde a:
01: TICKET
02: VALOR SERVICIO4

2

NUM

Número secuencial de la línea.
Valores : EAN13, PLU, DUN14,
ALFA
INT1, INT2, EAN128, etc.
Sin validación
Sin Validación
ALFA
(Máximo 35 Bytes)
1: Producto o servicio es exento
NUM
o no afecto
2: 2: Producto o servicio no es
facturable3
6: Producto o servicio no es
facturable (negativo)
Sin Validación
NUM

6

Rut Mandante

Rut de la Empresa Mandante de la Boleta.
Con guión y dígito verificador.

10

ALFA

Obligatorio si el “Indicador
Servicio” es 4
Cuerpo numérico entre
100.000 y 99 millones, guión y
dígito verificador alfanumérico
entre 0 y 9 o K

7

Nombre del ítem

Nombre del producto o servicio.

80

ALFA

Sin Validación

N

1

1

N

3

3

N

3

3

N

2

2

N

2

2

N

3

3

I

1

1

2

2

1

1

Si el campo Item Espectáculo no es nulo se
debe indicar un nombre de producto o servicio
que tenga relación con “TICKET” o “VALOR
SERVICIO - COMISIÓN”

8

Obligatorio si el “Item
Espectáculo” es 01

AREA

INFO TICKET

Folio Ticket

Corresponde a la numeración única para el
evento.

6

NUM

Sin Validación

I

3

Ejemplos de estos items son: Cobro de ventas o servicios de otras empresas que ya pagaron el IVA, por ejemplo compras en expendedoras
automáticas pagando con Celular.
4
Este puede ser un valor por acercamiento o comisión por venta de ticket.

Versión 2.0 2010-07-12

Pág. 10 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

9

Fecha Generación Ticket

Corresponde a la fecha y hora de generación
del ticket
(AAAA-MM-DDThh:mm:ss)

16

ALFA

Fecha válida entre
2010-03-10T00:00:00 y 2050-1231T23:59:59

N

1

1

10

Nombre Evento

Nombre del Espectáculo

80

ALFA

Sin Validación

I

1

1

10

ALFA

Sin Validación

I

1

1

5

ALFA

Sin Validación

I

1

1

16

ALFA

Fecha válida entre

I

1

1

11
12
13

Tipo Ticket
Código del Evento
Fecha y Hora del Evento

Tipo de ticket, Por ejemplo: Adulto, Niño, etc
Código asociado al Evento
Fecha y hora de realización del evento
(AAAA-MM-DDThh:mm:ss)

2010-03-10T00:00:00 y 205012-31T23:59:59
14

Lugar del Evento

15

Ubicación en el Evento

Dirección o identificación del recinto donde se
realizará el evento
Sector/Sección de la ubicación en el evento

16

Fila Ubicación

17

Asiento Ubicación

Fila correspondiente a la Ubicación en el
evento
N° de Asiento correspondiente a la Ubicación
en el evento

FIN AREA

INFO TICKET

18

Descripción Adicional

Descripción adicional del producto o servicio.
Se utiliza para pack, servicios con detalle

19

Cantidad

Cantidad del ítem en 12 enteros y 6
decimales.

80

ALFA

Sin Validación

I

1

1

20

ALFA

Sin Validación

I

1

1

3

ALFA

Sin Validación

I

3

3

3

NUM

Sin Validación

I

3

3

1000

ALFA

Sin Validación

I

3

3

18

NUM

Valor numérico

I

2

2

Se debe indicar en el caso de venta de
mercaderías o productos
20

Unidad de Medida

Glosa con unidad de medida

4

ALFA

Sin Validación

I

3

3

21

Precio Unitario

Precio con 16 enteros y 2 decimales. Este
precio es bruto con IVA, excepto cuando el
Indicador Montos Netos tiene el valor 2.

18

NUM

Valor numérico

I

2

2

5

NUM

Valor Numérico, entre los
valores 0 y 100 incluidos

N

3

3

18

NUM

Valor Numérico. Si hay
descuento en porcentaje, debe
ir el monto del descuento.

I

2

2

5

NUM

Valor Numérico, entre los
valores 0 y 100 incluidos

N

3

3

22

Porcentaje de Descuento

23

Monto Descuento

24

Porcentaje de Recargo

Se debe indicar en el caso de venta de
mercaderías o productos
Porcentaje (%) de Descuento, de 3 enteros y
2 decimales.
Correspondiente al anterior. Totaliza el
descuento aplicado al item. Este monto es
bruto con IVA, excepto cuando el Indicador
Montos Netos tiene el valor 2
Porcentaje (%) de Recargo, de 3 enteros y 2
decimales.

Versión 2.0 2010-07-12

Pág. 11 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

25

Monto Recargo

26

Valor por línea de detalle

Correspondiente al anterior. Totaliza el
Recargo aplicado al item. Este monto es bruto
con IVA, excepto cuando el Indicador
Montos Netos tiene el valor 2
(Precio Unitario * Cantidad) - Monto
Descuento + Monto Recargo
Este valor es bruto (con IVA), excepto cuando
el campo Indicador Montos Netos tiene el
valor 2.

18

NUM

Valor Numérico. Si hay Recargo
en porcentaje, debe ir el Monto
del Recargo.

I

2

2

18

NUM

Valor numérico, de acuerdo con
descripción

I

1

1

Versión 2.0 2010-07-12

Pág. 12 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

C.- Subtotales Informativos
Pueden ser de 0 hasta 20 líneas. Estos subtotales no aumentan ni disminuyen la base del impuesto, no modifican los campos totalizadores, sólo
son campos informativos para agrupar ítemes que desee el contribuyente.
Estos subtotales tienen una glosa que especifica el concepto. Por ejemplo un subtotal aplicado a un determinado grupo de productos, servicios o
elementos.
En la representación impresa, estos sub-totalizadores pueden intercalarse entre las líneas de detalle, o indicarse en forma agrupada en una
sección aparte.

CAMPOS

Largo

DESCRIPCIÓN

Tipo

I

Validación

MAX

Obligatoriedad de
campo
Boleta

Boleta
exenta

1

N° de Línea o N°
Secuencial

Número de Subtotal. De 1 a 20.

2

NUM

Número secuencial de la línea.
La obligatoriedad se refiere a
que si se incluye esta zona
debe haber al menos una línea
y este caso debe ir el dato de
número de línea.

N

1

1

2

Glosa

Especificación del Subtotal

80

ALFA

Sin Validación

I

3

3

3

Orden de impresión

Número de referencia para definir el orden, o lugar en
que se imprimirá este subtotal en la representación
gráfica e impresa del DTE

2

NUM

Sin validación

N

3

3

Para uso y definición del emisor
electrónico

4

Valor Sub Total Neto

Valor Neto del Subtotal

18

NUM

16 enteros 2 decimales

I

3

3

5

Valor Sub Total IVA

Valor del IVA del Subtotal

18

NUM

16 enteros 2 decimales

I

3

3

6

Valor Sub Total
Impuesto Adicional

Valor de los Impuestos adicionales o específicos del
Subtotal

18

NUM

16 enteros 2 decimales

I

3

3

7

Valor Sub Total
Exento

Valor no Afecto o Exento del Subtotal

18

NUM

16 enteros 2 decimales

I

3

3

8

Valor del Subtotal

Valor de la línea de subtotal

18

NUM

Sin validación. 16 Enteros y 2
decimales. Aplica en subtotales
en $ u otra moneda.

I

3

3

9

Línea de Detalle

TABLA de Líneas de Detalle que se agrupan en el
Subtotal. Hasta 60 repeticiones.

18

NUM

Sin validación. 16 Enteros y 2
decimales. Aplica en subtotales
en $ u otra moneda.

N

3

3

Versión 2.0 2010-07-12

Pág. 13 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

D.- Información de Descuentos o Recargos
Pueden ser de 0 hasta 20 líneas.
Estos aumentan o disminuyen la base del impuesto.
Estos descuentos o recargos tienen una glosa que especifica a qué items se aplica. Por ejemplo un descuento
global aplicado a un determinado tipo de producto o un descuento por pago contado que afecta a todos los items.
N°

CAMPOS

Largo

DESCRIPCIÓN

Tipo

Validación

I

Max

Obligatoriedad
de campo
Boleta Boleta
exenta

4

1

N° de Línea o N°
Secuencial

Número del ítem. Desde 1 a 20

3

NUM

Número secuencial de la línea. La
obligatoriedad se refiere a que si se incluye
esta zona debe haber al menos una línea y
este caso debe ir el dato de número de línea.

N

1

1

2

Tipo de movimiento

D(descuento) o R(recargo)

1

ALFA

DoR

N

1

1

3

Glosa

Especificación de descuento o
recargo

45

ALFA

Sin Validación

I

3

3

4

Tipo de valor

%o$

1

ALFA

%o$

I

1

1

5

Valor

18

NUM

Sin validación

I

1

1

6

Indicador exención

Valor del descuento o recargo en 16
enteros y 2 decimales
Indica si el descuento o recargo
afecta a ítems exentos o no
afectos a IVA

1

NUM

N

2

2

1: Producto o servicio es exento o no afecto
2: Producto o servicio no es facturable4

Ejemplos de estos items son: Cobro de ventas o servicios de otras empresas que ya pagaron el IVA. Por ejemplo compras en expendedoras
automáticas pagando con Celular.

Versión 2.0 2010-07-12

Pág. 14 de 15

Servicio Impuestos Internos
Formato Boletas Electrónicas

E.- Datos de Referencia
Datos opcionales para indicar otros datos referenciales del documento. Pueden ir hasta 40 posibles repeticiones.
N°

CAMPOS

1

DESCRIPCIÓN

2

N° de Línea o N°
Secuencial
Código referencia

Número de Dato de referencia. De 1
a 40
Código alfanumérico establecido por
la Empresa para informar el dato al
cliente.

3

Razón referencia

Detalle del dato

Largo
Max

Tipo

Validación

I

2

NUM

Número secuencial de la línea.

N

1

1

ALFA

De acuerdo con la Descripción

I

3

3

90

ALFA

Sin validación

I

3

3

8

ALFA

Sin Validación

I

3

3

8

ALFA

Sin Validación

I

3

3

18

Código alfanumérico establecido por
la Empresa, a su Vendedor.
4

Código Vendedor

Obligatoriedad
de campo

Este código puede estar asociado a
“INTERNET”
5

Código Caja

Código alfanumérico establecido por
la Empresa, a la Caja

F.- Timbre Electrónico SII del Documento.
Largo

N°

CAMPOS

DESCRIPCIÓN

1

Timbre Electrónico del
Documento. Corresponde a una
firma electrónica sobre los datos
principales. Es el mismo formato
de la Factura.

Contiene la firma Electrónica sobre
campos representativos del DTE y el
Código de Autorización de Folios (CAF)
entregado por el SII. Corresponde a la
información del Código de Barras
Bidimensional PDF417

Versión 2.0 2010-07-12

Tipo
ALFA

Validación
Para una descripción detallada véanse
Anexos de Instructivo de Generación de
documentos.

Pág. 15 de 15
