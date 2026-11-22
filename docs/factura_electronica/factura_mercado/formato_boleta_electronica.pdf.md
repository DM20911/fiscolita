---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_boleta_electronica.pdf
titulo: FORMATO BOLETAS ELECTRÓNICAS DE VENTAS Y SERVICIOS
categoria: factura_electronica
---
FORMATO BOLETAS ELECTRÓNICAS DE VENTAS Y SERVICIOS

2025-09-08
Versión 4.2

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

FORMATO BOLETAS ELECTRÓNICAS
BITÁCORA DE CAMBIOS. ................................................................................................................................................................................................................ 3
1.- INTRODUCCIÓN ........................................................................................................................................................................................................................... 7
2.- TAMAÑO DE ENVÍO DE INFORMACIÓN AL SII ..................................................................................................................................................................... 7
3.- DETALLE DE CONTENIDO DE LAS BOLETAS ...................................................................................................................................................................... 8
A.- Encabezado .............................................................................................................................................................................................................................. 9
B.- Detalle de Productos o Servicios ..................................................................................................................................................................................... 13
C.- Subtotales Informativos ...................................................................................................................................................................................................... 15
D.- Información de Descuentos o Recargos ........................................................................................................................................................................ 17
E.- Datos de Referencia ............................................................................................................................................................................................................. 18
F.- Datos de Georreferenciación ............................................................................................................................................................................................. 19
G.- Timbre Electrónico SII del Documento ........................................................................................................................................................................... 19

Versión 4.2 2025-09-08

Página 2 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

BITÁCORA DE CAMBIOS.
Cambios 2025 09 08
1. Se modifica descripción y obligatoriedad de los campos <CorreoRecep> y <TelefonoRecep>.
2. Se modifica la descripción de los campos <MedioPago> y <NmbItem>.
3. Longitud de los campos <RznSocRecep> y <RznSocProvSW> pasa a 100 caracteres.
Cambios 2024 12 31
1. Se agregan los campos <MedioPago>, <CorreoRecep> y <TelefonoRecep> en la sección Encabezado.
2. Se modifica la descripción y obligatoriedad de los campos <RutRecep> y < RznSocEmisor>.
Cambios 2024 06 01
1. Se elimina código de obligatoriedad 4, reemplazándolo por 3 en los campos: <RznSocEmisor>; <GiroEmisor>;
<CdgSIISucur>; <DirOrigen>; <CmnaOrigen>; <CiudadOrigen>.
2. Se reemplaza en la columna I sobre obligatoriedad del dato en el pdf o el impreso la sigla “I” por “N”, en el campo
<RznSocEmisor>.
Cambios 2023 06 01
1. Se agregan campos para informar Rut y Nombre de Proveedor de Software de Boleta Electrónica.
2. Se agrega apartado F. Datos de Georreferenciación, pasando el Timbre Electrónico a ser la letra G.
Cambios 2022 12 28
1. En la sección A, fila se cambia nombre de tag <MntoNF> por <MontoNF>
2. En la sección A, fila se complementa descripción del campo Monto no Facturable.
Cambios 2020 07 20
1. Se modifica introducción:
a. Se elimina obligación de generar el Libro de Boletas Electrónicas.
b. Se elimina frase que indica que boletas electrónicas no se deben enviar al SII.
c. Se elimina excepción de envío de Reporte de Consumo de Folios a prestadores de servicios periódicos.
2. Se modifica obligatoriedad de zona Subtotales Informativos
3. Se modifica obligatoriedad y descripción de campo Indicador Montos Netos
4. Se modifica obligatoriedad y descripción de campo Monto Neto
5. Se modifica obligatoriedad y descripción de campo IVA
Versión 4.2 2025-09-08

Página 3 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

6. Se modifica descripción de campo Monto Total
7. Se modifica obligatoriedad y descripción de campo Valor Subtotal Impuesto Adicional
8. Se agregan campos <TpoDocRef> y <FolioRef> en zona Datos de Referencia.
9. Se agregan tags del schema XML
10. Se actualizan obligaciones de informar campos en representación digital o impresa
11. Se agrega información sobre tamaño de envío de información al SII.
Cambios 2019 03 11
1. Se modifica la obligatoriedad de la zona “Detalle” del documento, pasando de obligatoria a condicional.
Cambios 2010 07 12
1. Se modifica el formato para incorporar datos del ticket de espectáculos, para la emisión de boletas electrónicas por
cuenta de terceros.
2. En la sección A. Encabezado en el campo “Indicador Servicio” se agrega un cuarto tipo “boleta de espectáculo
emitida por cuenta de terceros”.
3. En la sección B. Detalle de Productos o Servicios:
a. Se agrega el campo “Ítem Espectáculo”
b. Se agrega el campo “Rut Mandante”
c. Se agregan los campos del Área “INFO TICKET”:
i.
Folio Ticket
ii.
Fecha Generación Ticket
iii. Nombre Evento
iv. Tipo Ticket
v. Código del Evento
vi. Fecha y Hora del Evento
vii. Lugar del Evento
viii. Ubicación en el Evento
ix. Fila Ubicación
d. Asiento Ubicación
e. Se modifica la descripción del campo “Nombre del Ítem”, indicando en caso de que el campo “Ítem
Espectáculo” no sea nulo, este debe tener relación al ticket o al valor por servicio (comisión).
f. Se agrega el campo “Porcentaje de Descuento”
Versión 4.2 2025-09-08

Página 4 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

g. Se agrega el campo “Monto Descuento”
h. Se agrega el campo “Porcentaje de Recargo”
i. Se agrega el campo “Monto Recargo”
j. Se modifica descripción de los campos “Cantidad” y “Precio Unitario” indicando que se debe indicar en
el caso de venta de mercaderías o productos.
k. Se modifica descripción del campo “Valor por línea detalle” incorporando a la fórmula el descuento
y recargo.
4. En la sección E. Datos de Referencia se agregan los campos “Código Vendedor” y “Código Caja”.
Cambios 2005 08 05
1. Se hacen correcciones varias de forma y redacción.
2. Se incorporan indicadores de exención por no facturable (códigos 2 y 6).
Cambios 2005 04 15
1. Se explica la obligación de los emisores de boletas electrónicas de emitir diariamente un Reporte de Consumo
de Folios. (Ver nuevo documento electrónico Reporte de Consumo de Folios).
2 En la sección de Encabezado Se aumenta el largo máximo de los campos: “Nombre o Razón Social Emisor”,
“Dirección Origen”, “Ciudad Origen”, “Nombre Receptor”, Dirección Receptor”, “Ciudad Receptor”, “Dirección
postal” y “Ciudad Postal”.
3 En la sección de Encabezado, se modifica la obligatoriedad de información de los campos: “Comuna Receptor”,
“Ciudad Receptor”, “Monto neto” e “IVA”. Adicionalmente se modifica la obligatoriedad de impresión de los
campos: “Dirección postal”, “Comuna Postal” y “Ciudad Postal”
4 En el Rut Receptor se permite el uso de RUT genérico en caso de Boletas de Ventas y Servicios (no periódicos
ni domiciliarios): valor: 66.666.666-6
5 En la sección de Detalle, se incrementa el número máximo de líneas de 60 a 1000, y se incrementa el largo
máximo del campo “Tipo código” de 5 a 10, así como el campo “Descripción Adicional” se aumenta el largo de
180 a 1000.
6. En la sección de Referencias se reduce de 50 a 40 el número de líneas posibles de informar.
7. En la sección de Referencias se incrementa el largo del campo “Código referencia” de 10 a 18, y también el
campo “Razón referencia” de 30 a 90.
8. Se agrega una nueva área opcional de INFORMACIÓN DE SUBTOTALES.

Versión 4.2 2025-09-08

Página 5 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

Cambios 2004 01 12
1. En el XML se dejan como opcionales algunos campos que tenían obligatoriedad 4 (sólo impresión).
2. En el XML se modifica la carátula para indicar número de boletas exentas.

Versión 4.2 2025-09-08

Página 6 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

1.- INTRODUCCIÓN
En este documento se especifica el formato de las boletas.
•
•
•
•
•
•

Las boletas se deberán mantener en la empresa durante seis años, en el formato XML que se establece en
este documento.
Deben estar disponibles para consulta en línea en la sucursal para el mes en curso y para los dos meses
anteriores.
El SII podrá solicitar información en medios tecnológicos para períodos anteriores.
Los contribuyentes emisores electrónicos que emitan boletas electrónicas en una sucursal, deben emitir la
totalidad de su documentación de forma electrónica en dicha sucursal.
Generar y enviar diariamente al SII un “Reporte de Consumo de Folios”.
El emisor autorizado deberá publicar en un sitio Web las boletas electrónicas y boletas no afectas o exentas
electrónicas emitidas. Los documentos antes mencionados deberán estar a disposición para consulta por
parte de los clientes, durante un período de tres meses contados desde la emisión del documento. El sitio
web donde estará disponible la consulta de la boleta electrónica deberá estar señalado en la representación
digital o impresa como una leyenda bajo el timbre electrónico, por ejemplo: “Verifique documento:
http://www.consultaboletaelectronica.empresa.cl”. Una vez entrada en vigencia la obligatoriedad del
documento en formato electrónico deberá indicar la leyenda “verifique en www.sii.cl”, pudiendo agregar
opcionalmente la dirección web de consulta para el receptor

2.- TAMAÑO DE ENVÍO DE INFORMACIÓN AL SII
Debido a que al momento de recibir la información de las boletas electrónicas el SII debe validar tanto el formato
XML del envío, así como la firma electrónica sobre el mismo, se ha establecido como límite para el envío de
información 500 boletas por envío, lo que permite asegurar un óptimo procesamiento de la información tanto a
los emisores como al SII

Versión 4.2 2025-09-08

Página 7 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

3.- DETALLE DE CONTENIDO DE LAS BOLETAS
A. Datos de encabezado: corresponden a la identificación del documento, información del emisor,
información del receptor y monto total de la transacción.
B. Detalle por Ítem: En esta zona se debe detallar al menos una línea. Se debe detallar el ítem cobrado,
cantidad y valor.
C. Timbre Electrónico SII: Firma electrónica sobre la información representativa del documento para permitir la
validación del documento impreso.
Códigos de Obligatoriedad:
1: Dato obligatorio. El dato debe estar en el documento siempre, independiente de las características de la transacción.
2: Dato condicional. El dato no es obligatorio en todas las boletas, pero pasa a ser obligatorio en determinadas
operaciones si se cumple una cierta condición.
3: Opcional.
A continuación, se especifica el contenido de cada Zona, formato de cada dato de la zona, y códigos de obligatoriedad
del dato. Los nombres y características son similares a la Factura electrónica.

Versión 4.2 2025-09-08

Zonas del Documento

Obligatoriedad de la Zona

Encabezado
Detalle
Subtotales Informativos
Descuentos y Recargos
Datos de Referencia
Datos de Georreferenciación
Timbre
Firma

1
2
2
2
3
2
1
1

Página 8 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

En la columna I, se indica si el dato debe estar en la representación digital o impresa del documento.
N = No es obligatorio que esté impreso.
I = Debe estar impresa. La impresión que se haga debe ser en un formato editado.
P = Debe estar impresa traduciendo el código a palabras. (ejemplo: en el documento electrónico el tipo de
documento está codificado, sin embargo, en la representación digital o impresa debe ir en palabras)

A.- Encabezado
CAMPOS

DESCRIPCIÓN

1

VERSIÓN

Versión del Formato utilizado

2

Tipo de Documento

Indica que el documento es:
39: Boleta Electrónica
41: Boleta No Afecta o Exenta Electrónica
Folio autorizado por el SII

<TipoDTE>
3

Folio Documento

<Folio>
4

Emisión Contable

Fecha de emisión del docto (AAAA-MM-DD)

<FchEmis>
5

Indicador Servicio

<IndServicio>

6

Indicador Montos Netos

<IndMntNeto>

7

Periodo Desde
Periodo Hasta

Este indicador se utiliza para expresar que el
precio unitario y el valor de todas las líneas de
detalles corresponden a Montos netos, es decir no
incluyen el IVA. No aplica en boleta exenta

Se usa para servicios periódicos
Se usa para servicios periódicos

<PeriodoHasta>
9

10

Fecha de vencimiento
(pago)

<FchVenc>

Fecha de vencimiento (AAAA-MM-DD).
Obligatorio, en caso de servicios periódicos
domiciliarios.

Medio de pago
<MedioPago>

Indica el Medio de Pago utilizado.
Obligatorio cuando Monto total > 135 UF (Ley
21.713) y obligatorio imprimir.

Versión 4.2 2025-09-08

MAX

Obligatoriedad de campo

Tipo

Validación

I

Boleta

Boleta
exenta

ALFA

1.0

N

1

1

2

NUM

De acuerdo con la descripción del
Campo

P

1

1

10

NUM

I

1

1

I

1

1

N

1

1

3

10

ALFA

1

NUM

El objetivo del indicador es identificar el tipo de
transacción

<PeriodoDesde>
8

Largo

Campo NUM
Fecha válida entre 2002-08-01 y
2050-12-31
1 Boletas de servicios periódicos
2 Boletas de servicios periódicos
domiciliarios
3 Boletas de venta y servicios
4 Boleta de Espectáculo emitida
por cuenta de Terceros
2: Líneas de detalle indican
montos netos

1

NUM

N

3

0

10

ALFA

I

2

2

10

ALFA

I

2

2

10

ALFA

I

2

2

N

2

2

1

NUM

Fecha válida entre 2002-08-01 y
2050-12-31
1: Efectivo
2: Pago electrónico
3: Transferencia electrónica
4: Cheque
5: Otro

Página 9 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

11 Rut Emisor

Con guion y dígito verificador

<RUTEmisor>

12 Nombre o
Emisor

10

ALFA

100

Cuerpo numérico entre 100.000 y
99 millones, guion y dígito
verificador alfanumérico entre 0 y
9oK

I

1

1

ALFA

N

3

3

80

ALFA

N

3

3

9

NUM

N

2

2

70

ALFA

N

3

3

20

ALFA

N

3

3

20

ALFA

N

3

3

N

1

1

Razón Social Dato opcional

<RznSocEmisor>
13 Giro del
Emisor1

negocio

<GiroEmisor>
14 Código sucursal

<CdgSIISucur>

15 Dirección Origen2

<DirOrigen>

16 Comuna Origen

del Dato opcional. Se debe indicar el giro del emisor.
No es preciso registrar todos los giros, sino que se
podrá registrar sólo el giro que corresponde a la
transacción.
Código numérico entregado por el SII, que identifica
a cada sucursal que está identificada en el Servicio
de Impuestos Internos.
Si no hay sucursales se
puede omitir.
Datos correspondientes a Dirección de sucursal
desde donde se despachan bienes o de sucursal
que emite el documento si no hay despacho de
bienes. Dato opcional
Dato opcional

<CmnaOrigen>
17 Ciudad Origen

Dato opcional

<CiudadOrigen>
18

Rut Receptor

<RUTRecep>

Rut del Cliente Receptor de la Boleta. Con guion y
dígito verificador.
Es obligatorio que venga un Rut válido o el
Código Interno.
Debe corresponder al RUT del cliente receptor
cuando Monto Total > 135 UF (Ley 21.713)
Se acepta que venga un 0 en los casos en
que el cliente se identifica con Código
Interno.
Se imprime si es distinto de 0 y de
66.666.666-6

10

ALFA

Cuerpo numérico, guion y dígito
verificador alfanumérico entre 0 y 9
o K. Debe venir un 0, cuando el
cliente se identifica sólo con código
interno.
Sólo en caso de Boletas de
Ventas y Servicios no periódicos
ni Domiciliarios, en caso de no
contar con el RUT o código interno
del cliente, se debe utilizar el RUT
genérico 66.666.666-6

1

Este dato puede ir pre impreso, indicando todos los giros autorizados del emisor, al igual que en la generación de documentos manuales. Pero
puede también ser un dato variable, en que se imprime sólo el giro que corresponde a la transacción.
2
La inclusión en el documento impreso puede ser hecho en forma similar a la generación de documentos manuales, en que en el anverso está pre
impresa la casa matriz y en el reverso o anverso están impresas todas las sucursales; se puede optar también por imprimir en forma variable sólo
la sucursal.

Versión 4.2 2025-09-08

Página 10 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

19 Código Interno del Cliente

<CdgIntRecep>

20 Nombre Receptor

<RznSocRecep>
21 Contacto Receptor

<Contacto>
Correo Receptor
<CorreoRecep>
Número de contacto receptor
23
<TelefonoRecep>
24 Dirección Receptor
22

<DirRecep>

Para identificación adicional interna del Receptor,
por ejemplo, código del cliente, número de medidor,
etc.

Sin Validación
Si Rut es 0, obligatoriamente debe
ir Código interno del
cliente

20

ALFA

Dato obligatorio si Indicador Servicio = 3 y RUT = 0,
o Monto Total > 135 UF (Ley 21.713)
Se debe imprimir cuando Monto total > 135 UF.
Opcional en otros casos
Nombre adicional o código adicional para identificar
al cliente.

100

ALFA

80

ALFA

N

3

3

Correo electrónico del cliente receptor.

80

ALFA

Sin Validación

N

3

3

Teléfono de contacto del cliente receptor

20

ALFA

Sin Validación

N

3

3

I

2

2

N

2

2

N

3

3

N

3

3

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

3

3

N

1

0

Sin validación

N

2

2

N

2

2

Sin Validación

Dirección en que se otorga el Servicio en el caso de
Servicios otorgados en un domicilio o dirección a la
cual se envían bienes. Si es un servicio móvil, se
debe indicar la dirección de residencia del cliente.

Sin validación

70

ALFA

20

ALFA

Es obligatorio si Indicador Servicio =1 o 2
Es opcional si Indicador Servicio =3
25 Comuna Receptor

Ídem

<CmnaRecep>
26 Ciudad Receptor

Ídem

20

<CiudadRecep>
27 Dirección postal

Otra dirección registrada.

70

<DirPostal>
28 Comuna Postal

Ídem

20

<CmnaPostal>
29 Ciudad Postal

Ídem

20

<CiudadPostal>
Rut Proveedor de
software
<RutProvSW>

ALFA
ALFA
ALFA
ALFA

Nombre o Razón
Social Proveedor
31

Sin Validación
Sin Validación
Sin Validación
Sin Validación

RUT de la empresa proveedora del sistema de
emisión de boletas electrónicas utilizado. Con guion
y dígito verificador
En caso de corresponder a un desarrollo propio,
debe informar el RUT del emisor.

30

Sin Validación

Corresponde al Nombre o Razón social del Rut
Proveedor de software. Si corresponde a un
desarrollo propio no informar.

10

ALFA

100

ALFA

Cuerpo numérico entre 100.000 y
99 millones, guion y dígito
verificador alfanumérico entre 0 y
9oK

<RznSocProvSW>
32 Monto neto

<MntNeto>

Versión 4.2 2025-09-08

Solo es válido si la boleta no es exenta. Suma de
valores totales de ítems afectos - descuentos +
recargos (Asignados a ítems afectos). Si no está
presente el Indicador de Montos Netos, el resultado
anterior se debe dividir por (1 + tasa IVA)

Valor Numérico
18

NUM

>0

Página 11 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

<IVA>

Suma de Valor por la línea de detalle para
Indicador
Exención=1
Sólo es válido si la boleta no es exenta.
Igual a la tasa (%) de IVA aplicada al Monto neto

35 Monto Total

Se calcula como Monto neto + IVA + Monto Exento.

33 Monto exento

<MntExe>
34 IVA

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

Saldo Anterior. Se incluye sólo con fines de ilustrar
con claridad el cobro.

18

NUM

Valor Cobrado
Valor total + Saldo anterior

18

NUM

Valor Numérico
de acuerdo a
descripción.
Valor Numérico de acuerdo a
descripción.

N

2

2

I

1

0

I

1

1

N

2

2

N

2

2

N

3

3

N

3

3

<MntTotal>

36 Monto no Facturable

<MontoNF>
37 Total período

Corresponde a la suma de montos de bienes o
servicios con Indicador exención = 2 y 6
Monto Total + Monto no Facturable

<TotalPeriodo>
38 Saldo anterior

<SaldoAnterior>
39 Valor a pagar

<VlrPagar>

Versión 4.2 2025-09-08

Sin validación Puede ser negativo
Sin validación
(de acuerdo a descripción)
(Puede ser negativo de
acuerdo a descripción)
Sin validación (Puede ser
negativo o cero
(de acuerdo a descripción)

Página 12 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

B.- Detalle de Productos o Servicios
Corresponde a la información de un ítem. El máximo de ítems es de 1000.

CAMPOS

DESCRIPCIÓN

Largo

Tipo

Validación

MAX

I

Obligatoriedad
de campo

Boleta Boleta
exenta
1

N° de Línea o N° Secuencial

Número del ítem. Desde 1 a 1000

<NroLinDet>
4

2

Tipo código

<TpoCodigo>
3

Código del ítem

<VlrCodigo>
4

Indicador exención

<IndExe>

5

Ítem Espectáculo

<ItemEspectaculo>

Tipo de codificación utilizada
Standard: EAN, PLU, DUN o Interna (Hasta
5 tipos de códigos)
Código del producto de acuerdo a tipo de
codificación indicada en campo anterior
Indica si el servicio es exento o no afecto a
impuesto o de monto no debe ser facturado. En
el caso que sea 2, no se debe considerar para
el cálculo del IVA del período.
No se usa para saldo anterior.
Indica si el ítem corresponde a:
01: TICKET
02: VALOR SERVICIO4

10
35

1

2

Número secuencial de la línea. La
obligatoriedad se refiere a que si se
NUM incluye esta zona debe
haber al
menos una línea y este caso debe
ir el dato de número de línea.
Valores: EAN13, PLU, DUN14,
ALFA INT1, INT2, EAN128, etc.
Sin validación
Sin Validación (Máximo
35
ALFA
Bytes)
1: Producto o servicio es exento o
no afecto
2: Producto o servicio no es
NUM facturable3
6: Producto o servicio no es
facturable (negativo)
Sin Validación
NUM Obligatorio si el “Indicador Servicio”
es 4

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

3

Ejemplos de estos ítems son: Cobro de ventas o servicios de otras empresas que ya pagaron el IVA, por ejemplo, compras en expendedoras
automáticas pagando con Celular.
4
Este puede ser un valor por acercamiento o comisión por venta de ticket.

Versión 4.2 2025-09-08

Página 13 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

6

Rut Mandante

<RUTMandante>

Rut de la Empresa Mandante de la Boleta. Con
guion y dígito verificador.

10

ALFA

Cuerpo numérico entre 100.000 y
99 millones, guion y
dígito
verificador alfanumérico entre 0 y
9 oK

N

3

3

I

1

1

2

2

I

1

1

N

1

1

I

1

1

I

1

1

I

1

1

I

1

1

I

1

1

I

1

1

Nombre del producto o servicio.
Se debe informar de forma clara su descripción
cuando Monto Total > 135 UF (Ley 21.713)
7

Nombre del ítem

<NmbItem>

8

AREA

INFO TICKET

Folio Ticket

Corresponde a la numeración única para el
evento.

<FolioTicket>
9

10

Sin Validación
Si el campo Ítem Espectáculo no es nulo se
debe indicar un nombre de producto o servicio
que tenga relación con “TICKET” o “VALOR
SERVICIO - COMISIÓN”

Fecha Generación Ticket

<FchGenera>

Corresponde a la fecha y hora de generación
del ticket
(AAAA-MM-DDThh:mm:ss)

Nombre Evento

Nombre del Espectáculo

80

6

<NmbEvento>
11

Tipo Ticket

Tipo de ticket, Por ejemplo: Adulto, Niño, etc

<TpoTicket>
12

Código del Evento

Código asociado al Evento

<CdgEvento>
13

Fecha y Hora del Evento

<FchEvento>

Fecha y hora de realización del evento (AAAAMM-DDThh:mm:ss)

ALFA

NUM

16

ALFA

80

ALFA

10

ALFA

5

ALFA

16

ALFA

Obligatorio si el “Ítem Espectáculo”
es 01
Sin Validación

Fecha válida entre 2010-0310T00:00:00 y 2050-1231T23:59:59
Sin Validación
Sin Validación
Sin Validación
Fecha válida entre 2010-0310T00:00:00 y 205012-31T23:59:59

14

Lugar del Evento

<LugarEvento>
15

Ubicación en el Evento

Dirección o identificación del recinto donde se
realizará el evento
Sector/Sección de la ubicación en el evento

80

ALFA

20

ALFA

Fila correspondiente a la Ubicación en el evento

3

ALFA

Sin Validación

I

3

3

N° de Asiento correspondiente a la Ubicación
en el evento
INFO TICKET

3

NUM

Sin Validación

I

3

3

Descripción adicional del producto o servicio.
Se utiliza para pack, servicios con detalle

1000

<UbicEvento>
16

Fila Ubicación

<FilaUbicEvento>
17

Asiento Ubicación

<AsntoUbicEvento>
FIN AREA
18

Descripción Adicional

<DscItem>

Versión 4.2 2025-09-08

Sin Validación
Sin Validación

ALFA Sin Validación

I

3

3

Página 14 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

19

Cantidad

<QtyItem>

20

Unidad de Medida

Cantidad del ítem en 12 enteros y 6 decimales.

Precio Unitario

<PrcItem>

NUM Valor numérico

4
18

Sin Validación
ALFA
NUM Valor numérico

I

2

2

Se debe indicar en el caso de venta de
mercaderías o productos
Glosa con unidad de medida

<UnmdItem>
21

18

Precio con 12 enteros y 6 decimales. Este
precio es bruto con IVA, excepto cuando el
Indicador Montos Netos tiene el valor 2.

I

3

3

I

2

2

N

3

3

I

2

2

N

3

3

I

2

2

I

1

1

Se debe indicar en el caso de venta de
mercaderías o productos
22

Porcentaje de Descuento

<DescuentoPct>
23

Monto Descuento

<DescuentoMonto>

24

Porcentaje de Recargo

<RecargoPct>
25

Monto Recargo

<RecargoMonto>

26

Valor por línea de detalle

<MontoItem>

Porcentaje (%) de Descuento, de 3 enteros y 2
decimales.

5

Valor Numérico, entre los valores 0
NUM y 100 incluidos

Correspondiente al anterior. Totaliza el
descuento aplicado al ítem. Este monto es bruto
con IVA, excepto cuando el Indicador Montos
Netos tiene el valor 2
Porcentaje (%) de Recargo, de 3 enteros y 2
decimales.

18

5

Valor Numérico, entre los valores 0
NUM y 100 incluidos

Correspondiente al anterior. Totaliza el Recargo
aplicado al item. Este monto es bruto con IVA,
excepto cuando el Indicador Montos Netos
tiene el valor 2
(Precio Unitario * Cantidad) - Monto
Descuento + Monto Recargo
Este valor es bruto (con IVA), excepto cuando el
campo Indicador Montos Netos tiene el valor
2.

18

NUM

18

NUM Valor Numérico. Si hay descuento
en porcentaje, debe ir el monto del
descuento.

NUM

Valor Numérico. Si hay Recargo en
porcentaje, debe ir el Monto del
Recargo.
Valor numérico, de acuerdo con
descripción

C.- Subtotales Informativos
Pueden ser de 0 hasta 20 líneas. Estos subtotales no aumentan ni disminuyen la base del impuesto, no modifican los
campos totalizadores, sólo son campos informativos para agrupar ítems que desee el contribuyente.
Estos subtotales tienen una glosa que especifica el concepto. Por ejemplo, un subtotal aplicado a un determinado grupo
de productos, servicios o elementos.
En la representación digital o impresa, estos sub-totalizadores pueden intercalarse entre las líneas de detalle, o indicarse
en forma agrupada en una sección aparte.
Versión 4.2 2025-09-08

Página 15 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

CAMPOS

1

N° de Línea o N°
Secuencial

DESCRIPCIÓN

Largo
MAX

Tipo

Número de Subtotal. De 1 a 20.

<NroSTI>

2

Glosa

Especificación del Subtotal

<GlosaSTI>
3

4

Orden de impresión

<OrdenSTI>

Número de referencia para definir el orden, o lugar en que
se imprimirá este subtotal en la representación digital e
impresa del DTE

Valor Sub Total Neto

Valor Neto del Subtotal

<SubTotNetoSTI>
5

Valor Sub Total IVA

Valor del IVA del Subtotal

<SubTotIVASTI>
6

7

Valor Sub Total
Impuesto Adicional

Valor de los Impuestos adicionales o específicos del
Subtotal. Obligatorio en caso de
transacciones
<SubTotAdicSTI>
relacionadas a los artículos de las letras a), b) y c) del
Art.37 de la Ley de IVA
Valor Sub Total Exento Valor no Afecto o Exento del Subtotal

<SubTotExeSTI>
8

Valor del Subtotal

Línea de Detalle

<LineasDeta>

Versión 4.2 2025-09-08

NUM

80

ALFA

TABLA de Líneas de Detalle que se agrupan en el
Subtotal. Hasta 60 repeticiones.

Número secuencial de la línea.
La obligatoriedad se refiere a que
si se incluye esta zona
debe haber al menos una línea y
este caso debe ir el dato de
número de línea.
Sin Validación

I

Obligatoriedad de
campo
Boleta

Boleta
exenta

N

1

1

I

3

3

N

3

3

I

3

3

I

3

3

I

2

3

I

3

3

Sin validación
2

NUM

18

NUM

18

NUM

18

NUM

Para uso y definición del emisor
electrónico

18

NUM

18

NUM

Sin validación. 16 enteros y 2
decimales. Aplica en subtotales
en $ u otra moneda.

I

3

3

18

NUM

Sin validación. 16 enteros y 2
decimales. Aplica en subtotales
en $ u otra moneda.

N

3

3

16 enteros 2 decimales
16 enteros 2 decimales
16 enteros 2 decimales

16 enteros 2 decimales

Valor de la línea de subtotal

<ValSubtotSTI>
9

2

Validación

Página 16 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

D.- Información de Descuentos o Recargos
Pueden ser de 0 hasta 20 líneas. Estos aumentan o disminuyen la base del impuesto.
Estos descuentos o recargos tienen una glosa que especifica a qué ítems se aplica. Por ejemplo, un descuento global
aplicado a un determinado tipo de producto o un descuento por pago contado que afecta a todos los ítems.
N°

CAMPOS

Largo

DESCRIPCIÓN

Validación

Tipo

Max

I

Obligatoriedad
de campo

Boleta Boleta
exenta
1

N° de Línea o
Secuencial

N° Número del ítem. Desde 1 a 20

<NroLinDR>
2

Tipo de movimiento

3
D(descuento) o R(recargo)

<TpoMov>
3

4

Glosa

<GlosaDR>

Especificación de descuento
recargo

Tipo de valor

%o$

Valor

<ValorDR>
6

Indicador exención

<IndExeDR>

Versión 4.2 2025-09-08

Valor del descuento o recargo en 16
enteros y 2 decimales
Indica si el descuento o recargo
afecta a ítems exentos o no
afectos a IVA

DoR

N

1

1

N

1

1

I

3

3

I

1

1

1

ALFA

45

ALFA

1

ALFA

18

NUM

I

1

1

1

1: Producto o servicio es exento o no afecto
NUM 2: Producto o servicio no es facturable5

N

2

2

Sin Validación

o

<TpoValor>
5

Número secuencial de la línea. La obligatoriedad
se refiere a que si se incluye esta zona debe
NUM haber al menos una línea y este caso debe ir el
dato de número de línea.

%o$
Sin validación

Página 17 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

E.- Datos de Referencia
Datos opcionales para indicar otros datos referenciales del documento. Pueden ir hasta 40 posibles repeticiones.
N°
1

CAMPOS
N° de Línea o
Secuencial

DESCRIPCIÓN
N° Número de Dato de referencia. De 1 a
40

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

N

2

2

N

2

2

I

3

3

I

3

3

Obligatoriedad
de campo

<NroLinRef>
2

3

Tipo
Documento
referencia
<TpoDocRef>

Folio de Referencia

<CodRef>

Identificación del documento de
referencia. Obligatorio en caso de que
se
informe <TpoDocRef>
Código alfanumérico establecido por la
Empresa para informar el dato al cliente.

Razón referencia

Detalle del dato

<FolioRef>
4

5

de Indica si el documento de referencia es
39: Boleta electrónica
41: Boleta no afecta
o exenta
electrónica
50: Guía de despacho
52: Guía de despacho electrónica
801 Orden de Compra
802 Nota de pedido
803 Contrato
804 Resolución
805 Proceso ChileCompra
806 Ficha ChileCompra
813 Pasaporte

Código referencia

<RazonRef>
6

Código Vendedor

<CodVndor>

Código Caja

<CodCaja>

5

ALFA

Si es alfabético no hay validación y el
contribuyente puede usarlo para referenciar
documentos no tributarios y distintos de los
especificados.

Folio de documento que referencia.
18

ALFA

18

ALFA

90

ALFA

8

ALFA Sin Validación

I

3

3

8

ALFA Sin Validación

I

3

3

De acuerdo con la Descripción

Sin validación

Código alfanumérico establecido por la
Empresa, a su Vendedor.
Este código puede estar asociado a
“INTERNET”

5

3

De acuerdo con la Descripción si se requiere
referenciar un documento tributario se debe
utilizar un valor Numérico que debe estar en el
rango indicado en la descripción.

Código alfanumérico establecido por la
Empresa, a la Caja

Ejemplos de estos ítems son: Cobro de ventas o servicios de otras empresas que ya pagaron el IVA. Por ejemplo, compras en
expendedoras automáticas pagando con Celular.

Versión 4.2 2025-09-08

Página 18 de 19

Formato Boletas Electrónicas de Ventas y Servicios
Servicio Impuestos Internos

F.- Datos de Georreferenciación
Datos opcionales para indicar Georreferenciación.
N°

CAMPOS

1

Latitud
<LatitudEmision>

2

Longitud
<LongitudEmision>

3

Sistema de Referencia
<SistemaReferencia>

DESCRIPCIÓN
Valor que corresponde a la latitud de la
ubicación geográfica en que es emitido
el documento en el estándar WGS84
en su modalidad decimal
Valor que corresponde a la longitud de
ubicación geográfica en que es emitido
el documento en el estándar WGS84
en su modalidad decimal
Identifica el código del sistema de
referencia de la georreferenciación.

Largo
Max

Tipo

30

ALFA

N

3

3

30

ALFA

N

3

3

1

NUM

N

3

3

Validación

I

1. WGS84

Obligatoriedad
de campo

G.- Timbre Electrónico SII del Documento
N°
1

CAMPOS

DESCRIPCIÓN

Timbre
Electrónico
del Contiene
la firma Electrónica
sobre
y el
Documento. Corresponde a una campos representativos del DTE
firma electrónica sobre los datos Código de Autorización de Folios (CAF)
principales. Es el mismo formato entregado por el SII. Corresponde a la
información del Código de Barras
de la Factura.
Bidimensional PDF417

Versión 4.2 2025-09-08

Largo

Tipo

Validación

I

Para una descripción detallada véanse
Anexos de Instructivo de Generación de
documentos.
ALFA

N

Página 19 de 19
