---
url: https://www.sii.cl/factura_electronica/factura_mercado/casos_especiales_registro_documentos.pdf
titulo: Ejemplos de Registro de Documentos en la
categoria: factura_electronica
---
Ejemplos de Registro de Documentos en la
IECV y en la Declaración Jurada 3327 y 3328
En el presente documento se indica cómo se registran correctamente los documentos en
la información electrónica de compras y ventas (IECV) y para generar envíos de los
archivos correspondientes a las declraciones 3327 y 3328, se incluyen los códigos XML
para una mejor comprensión para las empresas que desarrollan o utilizan software propio
de facturación electrónica.
I.
Casos especiales en el registro de documentos en la Información Electrónica de
Compras.
1.
Registrar documentos con IVA no recuperable
2.
Registrar documentos con IVA uso común
3.
Registrar documentos con Impuestos adicionales que NO tienen derecho a crédito
4.
Registrar documentos con Impuestos adicionales que tienen derecho a crédito
5.
Registrar documentos de Activo Fijo

2
2
3
4
5
6

II.
Casos especiales en el registro de documentos en la Información Electrónica de
Ventas
1.
Registrar facturas de compra recibidas con retención total
2.
Registrar facturas de compra recibidas con retención parcial
3.
Registrar ventas por cuenta de terceros

7
7
8
9

III.
1.
2.

Registro de Liquidaciones y Liquidaciones Factura
Comisionista o Consignatario
Mandante

10
10
10

1

I. Casos especiales en el registro de documentos en la
Información Electrónica de Compras.
Es importante que los documentos se registren la Información Electrónica de compras
indicando el código de documento correcto, Por ejemplo:
Las facturas de proveedores tienen los códigos de documentos 30 y 33, este
último si se trata de un documento electrónico.
En cambio, las facturas de compra (emitidas por el comprador) tienen los
códigos de documento 45 y 46, este ultimo si se trata de un documento
electrónico.

1. Registrar documentos con IVA no recuperable
El campo destinado a IVA no recuperable se utiliza cuando se sabe, al momento de
registrar un documento recibido, que el IVA de dicho documento no tendrá derecho a ser
recuperado por ser una compra destinada a operaciones exentas, estar registrado fuera
de plazo, corresponder a entregas gratuitas, corresponder a gastos rechazados u otra
situación que no de derecho a crédito fiscal.
Para registrar una factura cuyo IVA no se puede recuperar, se debe hacer lo siguiente a
nivel de detalle en el libro:
El Monto IVA <MntIVA> debe dejarse en valor 0 y en la SubTabla de IVA no
recuperable se debe indicar:
o Código de IVA no recuperable <CodIVANoRec>, que es el IVA no
recuperable.
o Monto de IVA no recuperable <MntIVANoRec>, que corresponde al monto
del IVA de la factura.
Por ejemplo, para registrar una factura que no tiene derecho a crédito por estar destinada
a ventas exentas, con los siguientes montos, debe ser registrada de este modo:
Total Neto

15.000

IVA (19%)

2.850

Total

17.850

Junto con ingresar los tags comunes como Rut, Fecha, hay que tener en cuenta que se
deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>15000</MntNeto>
<MntIVA>0</MntIVA>
<IVANoRec>
<CodIVANoRec>1</CodIVANoRec>
<MntIVANoRec>2850</MntIVANoRec>
</IVANoRec>
<MntTotal>17850</MntTotal>

2

2. Registrar documentos con IVA uso común
El campo IVA de uso común es utilizado cuando el crédito fiscal de una factura está
asociado tanto a operaciones afectas como exentas o no gravadas y, el monto de IVA a
recuperar solo se podrá determinar al final del mes, mediante una proporción.
Se debe utilizar lo que se denomina IVA uso común y factor de proporcionalidad, de la
siguiente forma:
A nivel de detalle del libro, el Monto IVA <MntIVA> debe dejarse en valor 0 y en el
campo IVA uso común <IVAUsoComun> se debe registrar el IVA de la factura.
Posteriormente, una vez ingresados todos los documentos con IVA uso común, en
el Resumen del Libro de Compras se deberán indicar los siguientes campos:
o Factor de proporcionalidad <FctProp> registrando el porcentaje de IVA
recuperable.
o Total Crédito IVA uso común <TotCredIVAUsoComun> que
corresponderá al factor de proporcionalidad multiplicado por el total de iva
uso común registrado en las facturas.
Por ejemplo, para registrar una factura con IVA de uso Común, con los siguientes montos,
debe ser registrada de este modo:
Monto Neto 120.400
19% IVA

22.876

Total

143.276

Junto con ingresar los tags comunes como Rut, Fecha, etc., hay que tener en cuenta que
se deben registrar los siguientes datos en la sección de detalle correspondiente a la
factura, como se indica a continuación:
<MntNeto>120400</MntNeto>
<MntIVA>0</MntIVA>
<IVAUsoComun>22876</IVAUsoComun>
<MntTotal>143276</MntTotal>

*Factor de proporcionalidad determinado para el periodo: 0,6

Luego, en la sección de resumen periodo de la Información Electrónica de Compra, se
debe indicar el factor de proporcionalidad asociado al tipo de documento de la siguiente
forma.
<TotIVAUsoComun>22876</TotIVAUsoComun>
<FctProp>0.6</FctProp>
<TotCredIVAUsoComun>13726</TotCredIVAUsoComun>

3

3. Registrar documentos con Impuestos adicionales que NO tienen derecho
a crédito
La forma correcta de registrar el impuesto adicional recargado en un documento recibido,
cuando éste impuesto adicional no tiene derecho a crédito es la siguiente:
Registrar los datos básicos del documento y luego registrar el impuesto adicional en el
campo Impuestos sin derecho a crédito <MntSinCred>
Por ejemplo, para registrar una factura cuyos impuestos adicionales no tienen derecho a
crédito, con los siguientes montos, debe ser registrada de este modo:
Ejemplo: comerciante minorista que vende al consumidor.
Monto Neto 40.000
19% IVA

7.600

Imp. ILA

10.500

Total

58.100

Junto con ingresar los tags comunes como Rut, Fecha, hay que tener en cuenta que se
deben registrar los siguientes datos, cómo se indica a continuación:
<MntNeto>40000</MntNeto>
<MntIVA>7600</MntIVA>
<MntSinCred>10500</MntSinCred>
<MntTotal>58100</MntTotal>

4

4. Registrar documentos con Impuestos adicionales que tienen derecho a
crédito
Si un contribuyente tiene derecho a recuperar como crédito algún impuesto adicional en
particular, los documentos que ingrese a su Información Electrónica de Compras con
aquel impuesto los deberá registrar de la siguiente forma:
Registrar los datos básicos del documento y luego registrar el impuesto adicional
en la tabla otros impuestos, indicando:
o Código del Impuesto <CodImp> que corresponde al tipo de impuesto
adicional.
o Tasa del Impuesto <TasaImp> que corresponde a su tasa.
o Monto del Impuesto <MntImp> que es el monto del impuesto.
Por ejemplo para registrar un documento como el que sigue, correspondiente a la compra
de vinos, con los siguientes datos, se deben registrar de este modo:

Monto Neto 110.000
19% IVA

20.900

15% ILA

16.500

Total

147.400

Junto con registrar los tags comunes como Rut, Fecha, hay que tener en cuenta que se
deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>110000</MntNeto>
<MntIVA>20900</MntIVA>
<OtrosImp>
<CodImp>25</CodImp>
<TasaImp>15</TasaImp>
<MntImp>16500</MntImp>
</OtrosImp>
<MntTotal>147400</MntTotal>

5

5. Registrar documentos de Activo Fijo
Si un contribuyente adquiere un bien para su activo fijo, deberá registrar el documento
que contiene dicha información en la información electrónica de compra de la siguiente
forma:
Registrar los datos básicos del documento.
Registrar la cantidad de IVA que tiene derecho a crédito fiscal en el campo
<MntIVA>, la parte no recuperable se deberá registrar como se explica en el caso
I.1 y el IVA Uso Común se deberá registrar como se explica en el caso I.2.
Registrar la cantidad de IVA (recuperable) que corresponde a activo fijo en el
campo <MntIVAActivoFijo>
Registrar adicionalmente la cantidad del Monto Neto que corresponde a activo fijo
en el campo <MntActivoFijo>
Por ejemplo para registrar un documento como el que sigue, correspondiente a la compra
de un bien correspondiente al activo fijo de la empresa, se deben ingresar los datos de la
siguiente forma:
Monto Neto 291.000
19% IVA

55.290

Total

346.290

Junto con registrar los tags comunes como Rut, Fecha, etc., hay que tener en cuenta que
se deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>291000</MntNeto>
<MntIVA>55290</MntIVA>
<MntActivoFijo>291000</MntActivoFijo>
<MntIVAActivoFijo>55290</MntIVAActivoFijo>
<MntTotal>346290</MntTotal>

6

II. Casos especiales en el registro de documentos en la
Información Electrónica de Ventas
1. Registrar facturas de compra recibidas con retención total
En algunos casos especiales, la obligatoriedad de la emisión de los documentos es
responsabilidad del vendedor, lo cual es llamado cambio de sujeto del IVA, en estos
casos se emiten facturas de compra, a continuación se explica cómo se deben registrar
estos documentos.
Si un contribuyente recibe un factura de compra (esto es, realiza una venta y el
comprador emite el documento), deberá registrarla en el libro de ventas, a nivel de detalle,
de la siguiente forma:
Registrar los datos básicos, incluyendo el monto neto, IVA y total tal cual aparece
en la factura.
Registrar la retención total en el campo IVA Retenido Total <IVARetTotal>
Por ejemplo, para registrar una factura de compra recibida con retención total de IVA, con
los siguientes montos, debe ser registrada de este modo:
Neto

75.000

19% IVA a retener

14.250

Subtotal

89.250

menos 19% IVA retenido

14.250

Total

75.000

Junto con ingresar los tags comunes como Rut, Fecha, etc., hay que tener en cuenta que
se deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>75000</MntNeto>
<MntIVA>14250</MntIVA>
<IVARetTotal>14250</IVARetTotal>
<MntTotal>75000</MntTotal>

7

2. Registrar facturas de compra recibidas con retención parcial
Si un contribuyente recibe una factura de compra, que señala una retención parcial del
IVA, deberá registrarla en el libro de ventas, a nivel de detalle, de la siguiente forma:
Registrar los datos básicos, incluyendo el monto neto, IVA (19%) y total tal cual
aparece en la factura.
Registrar el monto de la retención en el campo IVA Retenido Parcial
<IVARetParcial>
Registrar el IVA no Retenido en el campo <IVANoRetenido>
Por ejemplo, para registrar una factura de compra recibida con retención parcial de IVA,
con los siguientes montos, debe ser registrada de este modo:
Neto

75.000

8% IVA a retener

6.000

11% IVA no retenido

8.250

Subtotal

89.250

menos 8% IVA retenido

6.000

Total

83.250

Junto con ingresar los tags comunes como Rut, Fecha, etc., hay que tener en cuenta que
se deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>75000</MntNeto>
<MntIVA>14250</MntIVA>
<IVARetParcial>6000</IVARetParcial>
<MntTotal>83250</MntTotal>
<IVANoRetenido>8250</IVANoRetenido>

8

3. Registrar ventas por cuenta de terceros
Cuando se emiten documentos que representan una venta por cuenta de terceros
(consignación o comisionista ), es necesario desglosar la cantidad de IVA por cuenta de
terceros. Para ello se debe informar lo siguiente:
Registrar los datos básicos, incluyendo el monto neto y total, tal cual aparece en la
factura.
En el campo <MntIVA> se debe informar el total del IVA del documento.
En el campo <IVATerceros> se debe ingresar la porcion del monto de IVA por
cuenta de terceros.
En el campo <IVAPropio> se debe ingresar la porción del monto de IVA propio de
la venta, si no hay, se informa un cero.
Así los campos quedarán relacionados de tal forma que MntIVA=IVATerceros+IVAPropio.
Se debe tener en cuenta también que si se trata de un documento electrónico dichos
campos deben venir informados de la misma forma en el documento original.
Por ejemplo una factura por los siguientes montos, que representa una venta sólo por
cuenta de terceros, debe ser registrada en la IEV de la siguiente forma:
Monto Neto
IVA 19%
Total

70.000
13.300
83.300

Junto con ingresar los tags comunes como Rut, Fecha, hay que tener en cuenta que se
deben registrar los siguientes datos, como se indica a continuación:
<MntNeto>70000</MntNeto>
<MntIVA>13300</MntIVA>
<IVAPropio>0</IVAPropio>
<IVATerceros>13300</IVATerceros>
<MntTotal>83300</MntTotal>

9

III. Registro de Liquidaciones y Liquidaciones Factura
Los comisionistas o consignatarios por cuenta de terceros están obligados a emitir a fin de
cada mes a su mandante una liquidación o liquidación factura por las ventas que efectuó
por cuenta de él.
Dichos documentos se registran de una forma particular, dependiendo si es el emisor o
receptor de ésta.

1. Comisionista o Consignatario
El comisionista o consignatario es el emisor del documento y deberá registrar en su
información electrónica de ventas la liquidación/liquidación factura que emita de la
siguiente forma:
Registrar los datos básicos, incluyendo el monto neto, IVA y total tal cual aparece
en la liquidación / liquidación factura emitida.
Si se tratase de una liquidación factura, se deberán registrar adicionalmente los
valores neto, exento e IVA de las comisiones y otros cargos respectivos en la
subtabla <TotLiquidaciones>.

2. Mandante
El mandante es quien recibe el documento y deberá registrarlo en su información
electrónica de ventas y, si se trata de una liquidación factura deberá registrarlo también en
la información electrónica de compras, por el crédito fiscal asociado a la comisión.
Información Electrónica de Ventas
Registrar los datos básicos, incluyendo el monto neto, IVA y total tal cual aparece
en la liquidación / liquidación factura.
Se deberá ingresar el RUT del emisor de la liquidación / liquidación factura en la
subtabla <TotLiquidaciones>.
Si se tratase de una liquidación factura, se deberán registrar adicionalmente los
valores neto, exento e IVA de las comisiones y otros cargos respectivos en la
subtabla <TotLiquidaciones>.
Información Electrónica de Compras
Registrar los datos básicos de la Liquidación Factura.
En el campo <MntIVA> se debe ingresar el valor IVA de la comisión (siempre que
sea recuperable), asimismo se deben registrar en los campos <MntNeto> y
<MntExe> los valores neto y exento de la comisión respectivamente.
Por Ejemplo, el Contribuyente RUT 1-9 (comisionista o consignatario) le emite una
liquidación factura al Contribuyente RUT 2-7 (mandante o comitente) con los montos que
se presentan a continuación, deberá ser registrada en los libros de la siguiente forma:

10

Neto Liquidación

2.000.000

19% IVA Liquidación

380.000

Subtotal

2.380.000

Neto Comisiones

100.000

19% IVA Comisión

19.000

Total

2.261.000

Comisionista o Consignatario:
Cabe tener presente que el comisionista o consignatario deberá registrar de una forma
especial las ventas por cuenta de terceros, tal como se explica a continuación::
El Comisionista o Consignatario (Rut 1-9) deberá registrar en su libro de ventas los datos
principales de la liquidación factura y las comisiones en los campos destinados para ello:
<MntNeto>2000000</MntNeto>
<MntIVA>380000</MntIVA>
<Liquidaciones>
<RutEmisor>1-9</RutEmisor>
<TotValComNeto>100000</TotValComNeto>
<TotValComExe>0</TotValComExe>
<TotValComIVA>19000</TotValComIVA>
</Liquidaciones>

Mandante:
El Mandante o Comitente (RUT 2-7) deberá registrar la liquidación factura completa en su
Libro de Ventas, indicando en la Sección liquidaciones el Rut del Comisionista, tal como
se muestra en el siguiente código:
<MntNeto>2000000</MntNeto>
<MntIVA>380000</MntIVA>
<Liquidaciones>
<RutEmisor>1-9</RutEmisor>
<TotValComNeto>100000</TotValComNeto>
<TotValComExe>0</TotValComExe>
<TotValComIVA>19000</TotValComIVA>
</Liquidaciones>

Adicionalmente el mandante deberá registrar la comisión que le cobraron, en su libro de
Compra, ingresando el documento liquidación factura con los siguientes datos:
<MntExe>0</MntExe>
<MntNeto>100000</MntNeto>
<MntIVA>19000</MntIVA>

11
