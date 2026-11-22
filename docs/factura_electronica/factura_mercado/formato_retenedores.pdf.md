---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_retenedores.pdf
titulo: INSTRUCTIVO DE LLENADO DE DTES PARA
categoria: factura_electronica
---
INSTRUCTIVO DE LLENADO DE DTES PARA
CONTRIBUYENTES QUE TENGAN LA CALIDAD DE
AGENTES RETENEDORES DE CAMBIOS DE SUJETO DE
IVA
2005-12-30

1

INSTRUCTIVO DE LLENADO DE DTES PARA CONTRIBUYENTES QUE
TENGAN LA CALIDAD DE AGENTES RETENEDORES DE CAMBIOS DE
SUJETO DE IVA
CONSIDERACIONES GENERALES:
La Res. Ex. SII N° 107, de fecha 20 de octubre de 2005, que estable las normas y procedimientos
respecto de la emisión de facturas de compra electrónicas, dispuso que los emisores electrónicos
que tengan la calidad de Agentes Retenedores de IVA, deberán especificar su calidad de tal en el
documento electrónico emitido, así como también deberán indicar el código para el tipo de
producto que corresponde a la transacción, el código de retención, la cantidad de unidades
transadas, la (s) unidad(es) de medida, la tasa de retención, el monto de IVA retenido, el monto no
retenido y comisiones, si corresponde.
Asimismo, estos contribuyentes estarán eximidos de la obligación de presentar la Declaración
Jurada sobre Informe Mensual Retenedores Cambios de Sujeto, por aquellos periodos mensuales
completos en los cuales se encuentren operando como emisores de documentos tributarios
electrónicos (en adelante DTE’s), y copulativamente, hubiesen documentado todas sus
transacciones asociadas al producto en el cual tienen la calidad de agentes retenedores, por medio
de DTE’s, de acuerdo a lo indicado en el presente instructivo.
De acuerdo a lo expresado anteriormente, en este documento se describe la forma en que deben
ser completados, específicamente, los Documentos Tributarios Electrónicos que dan cuenta de
operaciones realizadas por contribuyentes que tienen la calidad de Agentes Retenedores de IVA,
para emitir sus documentos, así como para poder acceder al beneficio señalado.
En este documento se describe el llenado de DTE’s para los siguientes documentos:

-

Factura Electrónica
Nota de Crédito Electrónica
Nota de Débito Electrónica
Factura de Compra Electrónica

CONTENIDO DE FACTURAS Y DOCUMENTOS ASOCIADOS:
Todo documento tributario electrónico que se emita, debe considerar en primer término las
especificaciones descritas en el documento “Formato de Documentos Tributarios Electrónicos”, que
se encuentra publicado en www.sii.cl y el cual es periódicamente actualizado.
Adicionalmente, y sólo para los contribuyentes aquí señalados, se deben incluir las indicaciones de
llenado que se informan en este Instructivo, lo cual es condición necesaria para eximirse de la
obligación de presentar la Declaración Jurada sobre Informe Mensual Retenedores Cambios de
Sujeto.
NOTAS:
Campo: establecido de acuerdo al Formato de Documentos Tributarios Electrónicos.
Valor: Datos a consignar en campos referidos. Entre comillas “” se indican los valores específicos.

2

I. FACTURA ELECTRÓNICA, NOTA DE CRÉDITO ELECTRÓNICA Y NOTA DE DÉBITO
ELECTRÓNICA ASOCIADAS
(No aplica en el caso del cambio de sujeto a productos vendidos por pequeños productores
agrícolas (PPA))
A. Sección de detalle
1. Campo Indicador Agente Retenedor (<IndAgente>): Señala la calidad de Agente Retenedor en
el producto transado. En caso de no ser Agente Retenedor del producto en cuestión, este campo no
se informa:
a. Valor: “R”.
b. Impresión: No imprimir.
c.

Obligatoriedad: Es obligatorio para todas las ventas (con y sin retención o anticipo) que
realicen los agentes retenedores de los productos o servicios en los cuales tienen dicha
calidad.

2. Campo Tipo código (<TpoCodigo>): Se debe utilizar la primera línea que soporta esta tabla.
a. Valor: “CPCS” (Código de Producto de Cambio de Sujeto).
b. Impresión: No imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor” se
encuentre activado (informado).

3. Campo Código del Ítem (<VlrCodigo>): Valor del Código “CPCS” señalado en el Campo “Tipo
código”:
El valor del código “CPCS” identifica el producto vendido asociado a un respectivo cambio de sujeto.
Si en el campo “Tipo código”, se indicó el valor “CPCS”, se debe completar este campo con algún
valor de la columna 6 de la tabla anexa.
a. Valor: Ver tabla anexa.
b. Impresión: Imprimir descripción acorde (se debe traducir el código del ítem utilizando la
columna 5 de tabla anexa). Si la glosa impresa del Nombre del Ítem o de la Descripción
Adicional ya incluye esta información, se puede obviar la impresión de la descripción de
este código.
c.

Obligatoriedad: Obligatorio.

4. Campo Cantidad (<QtyItem>): Indica la cantidad transada de los productos, no siendo
obligatorio en los cambios de sujeto de la construcción y servicios de maquila relacionados con los
cambios de sujeto de chatarra y berries.
a. Valor: Numérico, de acuerdo a la Unidad de Medida dispuesta en la tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor”, se
encuentre activado, no es obligatorio en excepciones señaladas.

5. Campo Unidad de Medida (<UnmdItem>): Descripción de la unidad de medida, sólo puede
corresponder a las medidas señaladas en tabla anexa y sólo de acuerdo a la codificación indicada.
No es obligatorio en los cambios de sujeto de la construcción y servicios de maquila relacionados
con los cambios de sujeto de chatarra y berries.
a. Valor: Ver columna 7 de tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor”, se
encuentre activado, no es obligatorio en excepciones señaladas.

6. Campo Cantidad de Referencia (<QtyRef>): Se utiliza para señalar una segunda unidad de
medida, la cual es obligatoria en los servicios de faenamiento de ganado (cambio de sujeto de la

3

carne) y ventas de ganado, debiendo indicarse el número de unidades o cabezas de animales
faenados y vendidos respectivamente.
a. Valor: Numéricos, de acuerdo a la Unidad de Medida 2 ó de referencia dispuesta en la
columna 8 de la tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en los casos señalados.

7. Campo Unidad de referencia (<UnmdRef>): Descripción de la unidad de medida, sólo puede
corresponder a unidades.
a. Valor: “UNID”.
b. Impresión: Imprimir glosa acorde.
c.

Obligatoriedad: Es obligatorio en los servicios de faenamiento de ganado (cambio de sujeto
de la carne) y ventas de ganado.

8. Campo Código Impuesto o Retenciones (<CodImpAdic>): Indica el código de retención asociado
al producto con cambio de sujeto, es obligatorio en las transacciones en que exista retención o
anticipo asociado.
a. Valor: Según tabla anexa final.
b. Impresión: No imprimir.
c.

Obligatoriedad: Obligatorio en los cambios de sujeto de carne, harina y medios de prepago
de telefonía e Internet (márgenes de comercialización).

9. Campo Monto Base Faenamiento (<MntBaseFaena>): Indica el monto base sobre el cual se debe
calcular la retención.
a. Valor: Numérico.
b. Impresión: Imprimir.
c.

Obligatoriedad: obligatorio para las transacciones del cambio de sujeto de la carne
asociadas a servicios de faenamiento de ganado.

10. Campo Monto Base Márgenes de Comercialización (<MntMargComer>): Indica el monto base
sobre el cual se debe calcular la retención.
a. Valor: Numérico.
b. Impresión: Imprimir.
c.

Obligatoriedad: obligatorio para las transacciones del cambio de sujeto de medios de
prepago de telefonía e Internet (márgenes de comercialización).

11. Campo Precio Unitario Neto Consumidor Final (<PrcConsFinal>): Indica el precio neto a
consumidor final del producto afectado con retención sobre márgenes de comercialización.
a. Valor: Numérico.
b. Impresión: Imprimir.

c. Obligatoriedad: Es obligatorio para el cambio de sujeto de medios de prepago de telefonía
e Internet.

B. Sección de Encabezado
1. Campo Monto base faenamiento carne (<MntBase>): Es la base de cálculo de la retención en los
servicios de faenamiento asociados al cambio de sujeto de la carne.
a. Valor: Numérico.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio, en el caso señalados.

4

2. Campo Monto Base de Márgenes de Comercialización (<MntMargenCom>): Es la base de cálculo
de la retención en el cambio de sujeto de medios de prepago de telefonía e Internet.
a. Valor: Numérico.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio, en los casos señalados.

3. Campo Código de Impuesto Adicional o Retención (<TipoImp>): Indica el código de retención
asociado al producto con cambio de sujeto.
a. Valor: Según tabla anexa.
b. Impresión: Imprimir glosa acorde.
c.

Obligatoriedad: obligatorio, en los cambios de sujeto de carne, harina y medios de
prepago.

4. Tasa de Impuesto o Retención (<TasaImp>): De acuerdo al código informado en el campo
Código de Impuesto Adicional o Retención.
5. Valor del Impuesto o Retención (<MontoImp>): Corresponde al valor calculado de acuerdo al
código informado en el campo Código de Impuesto Adicional o Retención.
II. FACTURA DE COMPRA ELECTRÓNICA, NOTA DE CRÉDITO ELECTRÓNICA Y NOTA DE
DÉBITO ELECTRÓNICA ASOCIADAS

A. Sección de detalle
1. Campo Indicador Agente Retenedor (<IndAgente>): Señala la calidad de Agente Retenedor en
el producto transado. En caso de no ser Agente Retenedor del producto en cuestión, este campo no
se informa:
a. Valor: “R”.
b. Impresión: No imprimir.
c.

Obligatoriedad: Es obligatorio para todas las compras con retención en las cuales el
comprador tenga la calidad de agente retenedor del producto o servicio.

2. Campo Tipo Código (<TpoCodigo>): Se debe utilizar la primera línea que soporta esta tabla.
a. Valor: “CPCS” (Código de Producto de Cambio de Sujeto).
b. Impresión: No imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor” se
encuentre activado (informado).

3. Campo Código del Ítem (<VlrCodigo>): Valor del Código “CPCS” señalado en el Campo “Tipo
código”:
El valor del código “CPCS” identifica el producto vendido asociado a un respectivo cambio de sujeto.
Si en el campo “Tipo código”, se indicó el valor “CPCS”, se debe completar este campo con algún
valor de columna 6 de la tabla anexa.
a. Valor: Ver tabla anexa.
b. Impresión: Imprimir descripción acorde (se debe traducir el código del ítem utilizando
la columna 5 de tabla anexa). Si la glosa impresa del Nombre del Ítem o de la
Descripción Adicional ya incluye esta información, se puede obviar la impresión de la
descripción de este código.
c.

Obligatoriedad: Obligatorio.

5

4. Campo Cantidad (<QtyItem>): Indica la cantidad transada de los productos, no siendo
obligatorio en los cambios de sujeto de la construcción y servicios de maquila relacionados con los
cambios de sujeto de chatarra y berries.
a. Valor: Numéricos, de acuerdo a la Unidad de Medida a utilizar dispuesta en la tabla
anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor”, se
encuentre activado, no es obligatorio en excepciones señaladas.

5. Campo Unidad de Medida (<UnmdItem>): Descripción de la unidad de medida, sólo puede
corresponder a las medidas señaladas en tabla anexa y de acuerdo a la codificación indicada. No es
obligatorio en los cambios de sujeto de la construcción y servicios de maquila relacionados con los
cambios de sujeto de chatarra y berries.
a. Valor: Ver columna 7 de tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en caso que el campo “Indicador Agente Retenedor”, se
encuentre activado, no es obligatorio en excepciones señaladas.

6. Campo Cantidad de Referencia (<QtyRef>): Se utiliza para señalar una segunda unidad de
medida, la cual es obligatoria en las compras de ganado asociadas a este cambio de sujeto,
debiendo indicarse el número de unidades o cabezas de animales comprados.
a. Valor: Numéricos, de acuerdo a la Unidad de Medida 2 ó de referencia, dispuesta en la
columna 8 de la tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: Obligatorio en los casos señalados.

7. Campo Unidad de referencia (<UnmdRef>): Descripción de la unidad de medida, sólo puede
corresponder a unidades.
a. Valor: “UNID”.
b. Impresión: Imprimir.
c.

Obligatoriedad: Es obligatorio en las compras de ganado asociadas a este cambio de
sujeto.

8. Campo Código Impuesto o Retenciones (<CodImpAdic>): indica el código y subcódigo de
retención asociado al producto con cambio de sujeto:
a. Valor: Según tabla anexa, dependiendo si la retención es parcial (códigos de 2 dígitos)
o total (códigos de 3 dígitos), columnas 2 y 3 de la tabla anexa.
b. Impresión: No imprimir.
c.

Obligatoriedad: Obligatorio.

B. Sección de Encabezado
1. Campo Código de Impuesto Adicional o Retención (<TipoImp>): Indica el código de retención
asociado al producto con cambio de sujeto.
a. Valor: según tabla anexa, dependiendo si la retención es parcial (códigos de 2 dígitos)
o total (códigos de 3 dígitos), columnas 2 y 3 de la tabla anexa.
b. Impresión: Imprimir.
c.

Obligatoriedad: obligatorio.

2. Tasa de Impuesto o Retención (<TasaImp>): De acuerdo al código informado en el campo
Código de Impuesto Adicional o Retención.

6

3. Valor del Impuesto o Retención (<MontoImp>): Corresponde al valor calculado de acuerdo al
código informado en el campo Código de Impuesto Adicional o Retención.
C. Sección de Información de Comisiones y otros Cargos
La facturación de las comisiones y otros cargos de operación deberá ser registrada en esta sección
de los Documentos Tributarios Electrónicos de acuerdo a lo señalado en el modelo general del
sistema de Facturación Electrónica, consignándolos como servicios afectos o exentos según su
caso. Valores deben ser expresados en positivo, puesto que se restan del campo “Monto Total” del
Encabezado.

7

TABLA ANEXA
Cambio de
Sujeto
(1)

Código
Cambio de
Sujeto

Código de
Cambio de
Sujeto

Campo:
Código
Impuesto o
Retenciones

Campo: Código
Impuesto o
Retenciones

(2)

Tasa de
Retención
Parcial o
Anticipo
Asociada (%)

Producto Cambio de Sujeto
(5)

(4)

Código Producto
Cambio Sujeto

Unidad de
Medida
1

Unidad de
Medida
2

Campo: Código
del Ítem

Campo:
Unidad de
Medida

Campo:
Unidad de
referencia

(7)

(8)

(cuando Campo
Tipo Código =
CPCS)

(cuando se
aplica tasa de
retención total
en un cambio de
sujeto de
retención
parcial)

(6)

(3)
Arroz
Berries

36
48

Carne (Servicios de 17
Faenamiento de
Ganado)

361
481

10%
14%

5%

Arroz
Frambuesa fresca
Frambuesa congelada
Arándano (blueberry)
Arándano (blueberry) congelado
Arándana (cranberry)
Arándana (cranberry) congelada
Frutilla
Frutilla congelada
Mora cultivada y mora híbrida(boysenberry)
Mora cultivada y mora híbrida (boysenberry) congelada
Otros
Servicios de maquila
Bovino
Ovino
Porcino
Equino
Caprino
Camélido

3600
4801
4802
4803
4804
4805
4806
4807
4808
4809
4810
4811
4812
1701
1702
1703
1704
1705
1706

TON
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
S/ Unidad de Medida
KG
KG
KG
KG
KG
KG

No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
UN
UN
UN
UN
UN
UN

8

Cambio de
Sujeto
(1)

Código
Cambio de
Sujeto

Código de
Cambio de
Sujeto

Campo:
Código
Impuesto o
Retenciones

Campo: Código
Impuesto o
Retenciones

(2)

Tasa de
Retención
Parcial o
Anticipo
Asociada (%)

Producto Cambio de Sujeto
(5)

(4)

Código Producto
Cambio Sujeto

Unidad de
Medida
1

Unidad de
Medida
2

Campo: Código
del Ítem

Campo:
Unidad de
Medida

Campo:
Unidad de
referencia

(7)

(8)

(cuando Campo
Tipo Código =
CPCS)

(cuando se
aplica tasa de
retención total
en un cambio de
sujeto de
retención
parcial)

(6)

(3)
Carne (Ventas de
Carne)

18

5%

Cartones

47

Siempre se aplica
retención total del IVA

Chatarra

38

Siempre se aplica
retención total del IVA

Construcción

41

Siempre se aplica
retención total del IVA

Bovino
Ovino
Porcino
Equino
Caprino
Camélido
Papel blanco
Cartón corrugado
Diarios
Otros
Acero dulce
Fierro
Cobre
Bronce
Latón
Aluminio
Otros
Servicios de maquila
Construcción

1801
1802
1803
1804
1805
1806
4701
4702
4703
4704
3801
3802
3803
3804
3805
3806
3807
3808
4100

KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
S/ Unidad de Medida
S/ Unidad de Medida

No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica

9

Cambio de
Sujeto
(1)

Código
Cambio de
Sujeto

Código de
Cambio de
Sujeto

Campo:
Código
Impuesto o
Retenciones

Campo: Código
Impuesto o
Retenciones

(2)

Tasa de
Retención
Parcial o
Anticipo
Asociada (%)

Producto Cambio de Sujeto
(5)

(4)

(cuando se
aplica tasa de
retención total
en un cambio de
sujeto de
retención
parcial)

Código Producto
Cambio Sujeto

Unidad de
Medida
1

Unidad de
Medida
2

Campo: Código
del Ítem

Campo:
Unidad de
Medida

Campo:
Unidad de
referencia

(7)

(8)

(cuando Campo
Tipo Código =
CPCS)
(6)

(3)
Especies
Hidrobiológicas

37

371

10%

Ganado

32

321

8%

Harina
Legumbres

19
30

301

12%
13%

Pescado
Moluscos
Crustáceos
Algas
Otros
Especies procesadas
Bovino
Ovino
Porcino
Equino
Caprino
Camélido
Harina
Frejoles
Lenteja
Garbanzo
Arvejas secas

3701
3702
3703
3704
3705
3706
3201
3202
3203
3204
3205
3206
1900
3001
3002
3003
3004

TON
TON
TON
TON
TON
TON
KG
KG
KG
KG
KG
KG
TON
TON
TON
TON
TON

No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
UN
UN
UN
UN
UN
UN
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica

10

Cambio de
Sujeto
(1)

Código
Cambio de
Sujeto

Código de
Cambio de
Sujeto

Campo:
Código
Impuesto o
Retenciones

Campo: Código
Impuesto o
Retenciones

(2)

Tasa de
Retención
Parcial o
Anticipo
Asociada (%)

Producto Cambio de Sujeto
(5)

(4)

Código Producto
Cambio Sujeto

Unidad de
Medida
1

Unidad de
Medida
2

Campo: Código
del Ítem

Campo:
Unidad de
Medida

Campo:
Unidad de
referencia

(7)

(8)

(cuando Campo
Tipo Código =
CPCS)

(cuando se
aplica tasa de
retención total
en un cambio de
sujeto de
retención
parcial)

(6)

(3)
Madera

33

331

8%

Medios de Prepago
de Telefonía e
Internet

50

Siempre se aplica
retención total del IVA

Pequeños
Productores
Agrícolas

39

Siempre se aplica
retención total del IVA

No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica

Bosque en pie
Astillas
Trozos pulpables
Trozos aserrables
Madera aserrada
Leña
Otros
Tarjeta de prepago para telefonía e Internet
Recarga electrónica de prepago para telefonía e Internet

3301
3302
3303
3304
3305
3306
3307
5001
5002

M3 o MR
M3, TBDM o TBDU
M3 o MR
M3
M3, PP o PM
KG o M3
M3
UN
UN

Productos vendidos por el Pequeño Productor Agrícola PPA

3900

S/ Unidad de Medida No Aplica

11

Cambio de
Sujeto
(1)

Código
Cambio de
Sujeto

Código de
Cambio de
Sujeto

Campo:
Código
Impuesto o
Retenciones

Campo: Código
Impuesto o
Retenciones

(2)

Tasa de
Retención
Parcial o
Anticipo
Asociada (%)

Producto Cambio de Sujeto
(5)

(4)

Código Producto
Cambio Sujeto

Unidad de
Medida
1

Unidad de
Medida
2

Campo: Código
del Ítem

Campo:
Unidad de
Medida

Campo:
Unidad de
referencia

(7)

(8)

(cuando Campo
Tipo Código =
CPCS)

(cuando se
aplica tasa de
retención total
en un cambio de
sujeto de
retención
parcial)

(6)

(3)
Productos
Silvestres

31

Trigo

34

Siempre se aplica
retención total del IVA

341

11%

Rosa mosqueta
Mora
Hongos
Frutos Espino
Hojas Boldo
Tilo
Manzanilla
Llantén
Toronjil
Cedrón
Hierbas pectorales
Romero
Quillay
Hierba de hipérico
Cera de abeja
Trigo

3101
3102
3103
3104
3105
3106
3107
3108
3109
3110
3111
3112
3113
3114
3115
3400

KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
KG
TON o QTAL

No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica
No Aplica

12

Unidades de medida:
Unidad de medida

Valor a informar
(Campos: Unidad de Medida y Unidad de referencia
son: alfanuméricos de largo 4)

Tonelada

TON

Kilogramo

KG

Unidades

UNID

Quintal (100 Kg.)

QTAL

Metro Cúbico

M3

Metro Ruma

MR

Tonelada BDMT

TBDM

Tonelada BDU

TBDU

Pulgada Pinera

PP

Pulgada Maderera

PM

13
