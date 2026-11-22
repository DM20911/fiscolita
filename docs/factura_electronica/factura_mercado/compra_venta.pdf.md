---
url: https://www.sii.cl/factura_electronica/factura_mercado/compra_venta.pdf
titulo: Nuevas validaciones a la Información Electrónica de Compras y
categoria: factura_electronica
---
Nuevas validaciones a la Información Electrónica de Compras y
Ventas (IECV), Documentos Tributarios Electrónicos (DTE) y
Declaraciones Juradas 3327 y 3328.
El presente documento lista las nuevas validaciones que se efectuarán a IECV, a los DTE,y a las
Declaraciones 3327 y 3328, las que se han implementado para evitar errores en el registro de los
documentos informados.
Las validaciones incorporadas arrojarán como resultado rechazos y reparos:
Si las validaciones tienen como resultado un rechazo, no permitirán el ingreso de la IECV o
DTE o Declaraciones Juradas 3327 y 3328 al SII. Los contribuyentes deben corregir la
información con rechazo, antes de volver a enviar.
Si las validaciones tienen como resultado un reparo, permitirán el ingreso de la IECV, DTE o
Declaraciones Juradas 3327 y 3328 al SII. De ser necesario, el contribuyente deberá corregir
dicha información.
Consideraciones de las tablas siguientes:
Salvo que se indique lo contrario, todas las validaciones se hacen sobre documentos vigentes
(no anulados).
Cuando se nombra un documento, se debe considerar también su homólogo electrónico (por
ejemplo, si se nombra factura, se refiere también a factura electrónica), salvo que se indique lo
contrario.

Información Electrónica de Compras y F3327.
Las validaciones que se efectuarán son las siguientes:

N°

Validaciones Detalle IEC (Libro de Compra) y envíos de F3327

Resultado

1

Si el documento incorpora Monto Neto, entonces debe registrar monto en el IVA

Rechazo

2

Si el documento incorpora Montos en el IVA, entonces debe consignar Monto Neto

Rechazo

3

Si el documento incorpora Monto de IVA No Recuperable, entonces se debe registrar un
Código de IVA No Recuperable asociado.

Rechazo

4

Si el documento incorpora un código de IVA No Recuperable, entonces el documento debe
registrar un monto de IVA Recuperable.

Rechazo

5

Todo documento con Monto Neto o Monto Exento o Monto IVA, debe incorporar Monto Total.

Rechazo

6

Todo documento que incorpora Monto Total, entonces, debe también consignar Monto Neto o
Monto Exento o Monto IVA

Rechazo

1

N°

Validaciones Detalle IEC (Libro de Compra) y envíos de F3327

Resultado

7

Para Facturas, Facturas Exentas, Liquidaciones Factura, Facturas de Compra, Notas de
Crédito y Débito, entre otros, deben traer Fecha de Emisión del documento.

Rechazo

8

Para Facturas, Facturas Exentas, Liquidaciones Factura, Facturas de Compra, Notas de
Crédito y Débito, entre otros, debe declararse el Rut del proveedor

Rechazo

9

Para Facturas, Liquidaciones Factura, Facturas de Compra, entre otros, debe declararse la
Tasa de Impuesto

Reparo

10

Para Facturas, Facturas Exentas, Liquidaciones Factura, Facturas de Compra, entre otros,
debe consignar Monto Total distinto de cero

Reparo

11

Para Facturas, Liquidaciones Factura, Facturas de Compra, entre otros, debe consignarse con
Monto IVA

Rechazo

12

Para Facturas, Liquidaciones Factura, Facturas de Compra, entre otros, debe declararse
Monto Neto distinto de cero.

Reparo

13

Las Facturas Exentas, deben poseer Monto Exento distinto de cero. Este documento no debe
indicar Monto Neto y Monto IVA , o bien se debe registrar con valor cero.

Rechazo

14

Las notas de crédito y débito, deben venir Monto Total.

Rechazo

15

La tasa del IVA por el Monto Neto debe ser igual al IVA declarado en el documento, el cual se
descompone en IVA Recuperable, IVA No Recuperable e IVA de Uso Común,
Tasa de IVA * Monto Neto = Monto IVA Recuperable + IVA No Recuperable + IVA Uso Común

Reparo

El Monto Total de un documento debe cuadrar con la suma de los Montos Neto, Exento, IVA,
IVA No Recuperable, IVA de Uso Común, Otros Impuestos Sin Crédito, Impuestos Adicionales,
menos las Retenciones.

Reparo

17

En la Información electrónica de Compras (libro de compras) solo pueden declararse
documentos con IVA recuperable del periodo actual o de los dos anteriores.

Reparo

18

Si registra en su documento IVA por Activo Fijo, este debe ser inferior o igual al Monto de IVA
del documento

Rechazo

19

El campo excepción emisor/receptor solo aplica a las notas de crédito y débito, para el
contribuyente que genera el libro.

Rechazo

20

Los documentos no deben venir repetidos en libro de compra, es decir, no se puede ingresar
un mismo documento dos veces con el mismo RUT, tipo de documento y folio.

Reparo

16

2

Información Electrónica de Ventas y F3328
Las validaciones que se efectuarán son las siguientes:

N°

Validaciones Detalle IEV (Libro de Venta) y envíos de F3328

21

Para los documentos que dan derecho a crédito fiscal o documentos de exportación o
documentos exentos, entre otros documentos, al declararse el Monto Neto o el Monto Exento o Rechazo
el Monto IVA, debe declararse Monto Total

22

Para los documentos que dan derecho a crédito fiscal o documentos de exportación o
documentos exentos, entre otros documentos, si se declara un Monto Total, debe declararse
también el Monto Neto o Monto Exento o Monto IVA

Resultado

Rechazo

23

Para los documentos vigentes que dan derecho a crédito fiscal o de exportación o exentos,
Rechazo
entre otros documentos, debe declararse la Fecha de Emisión del documento

24

Para los documentos vigentes que dan derecho a crédito fiscal o de exportación o exentos,
entre otros documentos, deben venir con el Rut del receptor del documento (excepto en
facturas de compra)

Rechazo

25

La Tasa de Impuesto es obligatoria para al menos los siguientes documentos Facturas,
Liquidación, Liquidaciones Factura, Facturas de Compra, entre otros documentos.

Reparo

26

Para Facturas, Facturas de Compra, Factura de Exportación, y otros documentos asociado a
las zonas francas, debe declararse el Monto Total distinto de cero

Reparo

27

En todas las Facturas debe declararse el Monto de IVA

Rechazo

28

En todas las Facturas debe declararse el Monto distintos de cero.

Rechazo

29

En todas las Facturas Exentas debe declararse el Monto Exento distinto de cero y no debe
declararse Monto Neto y Monto IVA, o bien, declararlos con valor cero

Rechazo

30

En todas las notas de crédito y débito debe declararse el Monto Total

Rechazo

31

El IVA Retenido Parcial, IVA Retenido Total o el IVA No Retenido solo pueden declararse en
liquidaciones, liquidaciones factura, facturas de compra, notas de crédito y notas de débito.

Rechazo

32

Cuando se declara el monto del IVA, este IVA debe ser igual a la tasa de IVA vigente para el
periodo por el monto neto del documento.

Reparo

33

El Monto Total declarado en el documento debe corresponder a la suma de los Montos Neto,
Exento, IVA, IVA No Recuperable, IVA de Uso Común, Otros Impuestos Sin Crédito,
Impuestos Adicionales, menos las Retenciones, Comisiones y Crédito Empresas
Constructoras.

Reparo

El Total Monto del Periodo es la suma de Total Monto No Facturable y Monto Total.

Reparo

34

3

N°

Validaciones Detalle IEV (Libro de Venta) y envíos de F3328

Resultado

35

El mes correspondiente a la fecha de emision de cada documento debe ser igual al mes del
libro, con excepcion de los documentos correspondientes a facturación de servicios periodicos
domiciliarios.

Rechazo

Si existen ventas por cuenta de terceros, debe registar tanto el IVA propio, (la parte que le
corresponde pagar), y el IVA Terceros (parte que es responsabilidad del tercero). El Monto de
IVA deberá ser igual a la suma del IVA Propio y el IVA Terceros.

Reparo

Si en documentos declara IVA Retenido Total, IVA Retenido Parcial o IVA No Retenido
mayores que cero, el monto de IVA recuperable deberá ser igual a la suma de éstos (Monto
IVA =IVA no Retenido + IVA Retenido Parcial + IVA Retenido Total).

Reparo

38

Para las liquidaciones factura, el IVA de las Comisiones debe ser igual a la tasa del IVA (19%)
por el Valor Neto de las Comisiones.

Reparo

39

El campo excepción emisor/receptor (campo que identifica si la nota de crédito o débito hace
referencia a una factura de compra) solo puede utilizarse en notas de crédito y débito.

Rechazo

40

Tipo de Impuesto asociado a la Ley N°18.211, debe ser solamente para el documento Solicitud
Reparo
de Registro de Factura, por operaciones en Zona Franca.

41

Los documentos no deben venir repetidos en libro de venta, es decir, no se puede ingresar un
mismo documento dos veces con el mismo RUT, tipo de documento y folio.

36

37

Reparo

Resumen Información Electrónica de Ventas
Las siguientes validaciones se aplicarán a los documentos que se declaran únicamente resumidos
en la Información electrónica de ventas (boletas, pasajes y otros registros).

N°

Validaciones Resumen IEV (Libro de Venta) y envíos de F3328

42

Para las boletas, boletas exentas, boletas no afectas u otros, si se declara el Total Monto Neto
o Total Monto Exento o Total Monto IVA o Total Pasaje Internacional o Total Pasaje Nacional, Rechazo
debe declararse Total Monto Total.

43

Para las boletas, boletas exentas o no afectas o documentos cuyo tratamiento se asocie al
uso de boletas, si se declara el Monto Total del documento, deben declararse los campos
Total Monto Neto o Total Monto Exento o Total Monto IVA o Total Venta Pasaje Internacional
o Total Venta Pasaje Nacional.

Rechazo

44

Para las boletas o boletas exentas o boletas no afectas o documentos cuyo tratamiento se
asocie al uso de boletas, el total del documento debe ser mayor que cero.

Reparo

45

Los resúmenes de ventas de boletas y/o boletas electrónicas, debe declararse el Total Monto
IVA

Rechazo

46

Los resúmenes de ventas con boleta y boleta electrónica, debe declararse el Total Monto Neto
Rechazo
y debe ser mayor que cero.

Resultado

4

N°

Validaciones Resumen IEV (Libro de Venta) y envíos de F3328

Resultado

47

Los resúmenes de ventas con boleta exenta, debe declararse el Total monto exento mayor
que cero. Sin embargo, el Monto neto y monto IVA no deben venir declarados

Rechazo

48

Para los resúmenes de las ventas informadas en boleta liquidación, boletas de módulo zona
franca, u otros registros que aumenten o disminuyan débito, deben declararse los montos
totales.

Rechazo

49

Al ingresar los resúmenes por ventas de pasajes nacionales sin factura, el monto exento
informado, o bien el monto de las ventas de pasajes nacionales, debe ser mayor que cero

Rechazo

50

Al ingresar los resúmenes por ventas de pasajes internacionales sin factura, el monto exento
Rechazo
informado, o bien el monto de las ventas de pasajes internacionales, debe ser mayor que cero

51

Para algunos documentos tributarios, el IVA declarado en los documentos debe coincidir con
la tasa de IVA por el monto neto.

Reparo

52

El Monto Total corresponde a la suma de Monto Neto, Monto Exento, Monto IVA, Total Pasaje
y Total Pasaje Internacional

Reparo

53

En caso que se registren Montos Totales del Periodo y Montos No Facturables, deben
considerar la suma de los Montos Totales por documento del periodo, Monto No facturable
debe ser igual a la suma del Monto Total Periodo..

Reparo

En caso que se registre (para los documentos del periodo) IVA Propio o IVA Tercero, la suma
de ambos montos debe ser igual al IVA de los documentos

Reparo

54

Validaciones a los Documentos Tributarios Electrónicos
Las siguientes validaciones se aplicarán a los documentos electrónicos expresamente nombrados.
Estas validaciones no se aplican a las DJ 3327 y3328.

N°

Validaciones a los Documentos Tributarios Electrónicos

Resultado

55

Para facturas electrónicas debe declararse Monto IVA y debe ser entero mayor o igual a cero

Rechazo

56

Para las facturas electrónicas debe declararse monto neto y este debe ser mayor que cero.

Reparo

57

Para las facturas exentas electrónicas debe declararse monto exento y este debe ser mayor
que cero.
Si se declara Monto Neto o Monto IVA, estos deben ser cero.

Rechazo

5
