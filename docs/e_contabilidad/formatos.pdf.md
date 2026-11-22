---
url: https://www.sii.cl/e_contabilidad/formatos.pdf
titulo: Formatos de Libros Contables Electrónicos
categoria: otros
---
Formatos de Libros Contables Electrónicos

1.
Diccionario de Cuentas ...................................................................................................... 2
2.
Certificado de Autorización de Libro (CAL) ....................................................................... 3
3.
Comprobante de Certificación (COCERTIF) ..................................................................... 4
4.
Envío Obligatorio ............................................................................................................... 5
5.
Comprobante de Cierre (COCIERRE) ............................................................................... 6
6.
Resúmenes ........................................................................................................................ 7
6.1.
Resumen Diario ............................................................................................................. 7
6.2.
Resumen Mayor ............................................................................................................ 9
7.
Balance ............................................................................................................................ 11
8.
Envío de Libros ................................................................................................................ 12
8.1.
Información General del envío .................................................................................... 12
8.2.
Libro Diario .................................................................................................................. 13
8.3.
Libro Mayor .................................................................................................................. 15
9.
Libros de Compra y Venta ............................................................................................... 17
10.
Anexos ......................................................................................................................... 17
10.1.
Tabla 1: Códigos de Archivos Contables ................................................................ 17
10.2.
Tabla 2: Códigos de tipos de Libros........................................................................ 17

Versión al 22/04/2010
Modificación 22/04/2010: Se corrigen tipos de datos en Libro Mayor y Libro Diario para que el
documento esté de acuerdo al esquema.
Modificación 14/03/2006: Se agrega campo “Parcial” en Envío de Libros.
Modificación 10/01/2007: El formato de los Libros de Compra y Venta se asimila al formato de
Factura electrónica.
Modificación 15/03/2008: Corrige Descripción de Envío Obligatorio y Envío de Libros, eliminando el
Libro de Compras y ventas, el cual se ajusta en su totalidad a lo determinado en factura
Electrónica.
Modificación 17/09/2008: Corrige descripción de Campos Saldo Debe y Saldo Haber en Resumen
del Mayor, para los movimientos del período. Corrige descripción de campos “Saldo Deudor” y
“Saldo Acreedor” en balance.

1

1. Diccionario de Cuentas
El diccionario informa la correspondencia entre las cuentas contables que mantiene el
contribuyente y las Cuentas SII. El diccionario se debe mandar cada año aun cuando no haya
cambios en el plan de cuentas del SII.
El diccionario permite al contribuyente no modificar su plan de cuentas existente, estableciendo un
“puente” que relaciona sus cuentas con las cuentas tipo establecidas por el SII.

Campo

Oblig Tipo

1 Rut
contribuyente
2 Periodo
Tributario
3 Rectificatoria

1 R
1

Largo
Max

Descripción
Rut del contribuyente emisor del libro.
Año contable en formato AAAA

2 N

2 En caso de error se puede reenviar.
Se debe agregar un número de secuencia, partiendo por el número 1

4.1 Clasific de
Cuenta

1 N

4.2 Código Cuenta

1 A

1 Clasificación de cuenta
1: Activo
2: Pasivo
3: Patrimonio
4: Pérdidas y Ganancias
5: Orden
20 Código de Cuenta de la empresa.

4.3 Glosa Cuenta

1 A

40 Nombre de la cuenta de la empresa.

4.4 Código SII

1 A

16 Código cuenta SII asociado a la cuenta respectiva de la empresa.

4 Cuenta

5 Rut Firmante

1 R

6 Fecha Firma

1 A

Rut del firmante por parte del contribuyente.
19 Fecha y Hora de la Firma de este documento. En formato AAAA-MMDDTHH:MI:SS

7 Firma electrónica

2

2. Certificado de Autorización de Libro (CAL)
El CAL, uno por cada agrupación de Libros Contables Electrónicos, es otorgado por el SII al Rut
que ha efectuado las pruebas. A través de la entrega del CAL, el SII confirma que ese
contribuyente es capaz de generar el respectivo Libro Contable Electrónico.
El CAL incluye la siguiente información:

Campo

Oblig

Tipo

1 Rut Distribuidor

1 R

2 Tipo certificado

1

3 Clase

1

4 Tipo del Libro
Contable

1 N

5 Fecha Emisión

1 A

6 Período Vigencia

1 N

7 Fecha Firma

1 A

8 Firma Electrónica

1 XML

Largo
Max

Descripción

10 Rut de quien ha efectuado las pruebas de formato de los
Libros en el SII.
Este rut puede pertenecer a un contribuyente de primera o
segunda categoría.
C: Certificación. Se utiliza para efectuar las pruebas de
archivos
P: Producción. Lo entrega el SII, una vez que se hayan
efectuado las pruebas respectivas.
1 : C o n t r i b u y e n t e . S ó l o p a r a s u p r o pi o u s o . E s t e C A L n o s e
puede endosar.
2: Holding. Para uso de quien lo obtuvo y para empresas
del holding. Este CAL es endosable.
3: Empresa Software: Este CAL es endosable.
4: Prestador de Servicios Contables. Cal endosable.
4 1: Contable. Incluye, Diario, Mayor, Balance
6: Compra y Venta
10 Fecha en que el SII emite el CAL.
En formato AAAA-MM-DD
4 Año de operación del CAL.
19 Fecha y Hora de la Firma de este documento. En formato
AAAA-MM-DDTHH:MI:SS
Firma Electrónica del SII sobre este documento.

3

3. Comprobante de Certificación (COCERTIF)
El COCERTIF es utilizado por contribuyentes que no han efectuado las pruebas de archivos
directamente en el SII. Corresponde a un CAL tipo 2, 3 o 4, el cual es endosado por una empresa
autorizada (distribuidor), contiene los datos del contribuyente y está firmado por un usuario
autorizado del distribuidor.

Campo

Oblig

Tipo

Largo
Max

Descripción

1 Rut Contribuyente

1 R

Rut del contribuyente al que se le endosa el CAL.

2 Fecha Emisión

1 A

3 CAL

1 XML

4 Rut Firmante
Distribuidor

1 A

10 Rut de firmante autorizado por el Distribuidor a firmar este
tipo de documentos.

5 Fecha Firma

1 A

19 Fecha y Hora de la Firma de este documento. En formato
AAAA-MM-DDTHH:MI:SS

6 Firma Electrónica

1 XML

10 Fecha de Emisión del COCERTIF. Formato AAAAMMDD
Certificado de Au torización del Libro (CAL )

Firma Electrónica sobre este documento.

4

4. Envío Obligatorio
El envío obligatorio es una especie de sobre, que en su interior, contiene los Resúmenes de los
libros, el Balance y el Diccionario. Se compone de una carátula y los Comprobantes de Cierre de
Diario, Mayor, Balance y el Diccionario.

Campo

Oblig

Tipo

Largo
Max

Descripción

1 Rut Envía

1 R

2 Rut Contribuyente

1 A

10 Rut del contribuyente

Rut del firmante autorizado a enviar libros

3 Fecha Firma

1 A

19 Fecha y Hora de la Firma de este documento. En formato
AAAA-MM-DDTHH:MI:SS.

5

5. Comprobante de Cierre (COCIERRE)
El Comprobante de Cierre es el componente principal del envío obligatorio, pues contiene los
resúmenes de los libros Diario y Mayor, junto con incluir el Balance y el Diccionario. Además
incluye el CAL o Cocertif, según el tipo de autorización que tenga el contribuyente.

Los Comprobantes de Cierre pueden enviarse separadamente tanto por libro, de esta forma se
podrían tener las siguientes alternativas:
Alternativa 1: Envío de toda la información anual.
En un LceCoCierre incluir Resumen de Diario, Resumen de Mayor, Balance y Diccionario
con el respectivo CAL O COCERTIF (Correspondiente a los Libros Contables).
Alternativa 2: Efectuar dos envíos.
En un envío incluir Resumen de Diario y Resumen de Mayor. En otro LceCoCierre incluir
Balance y Diccionario,
Ambos envíos deben agrega el respectivo CAL O COCERTIF (Correspondiente a los
Libros Contables).
Alternativa 3: Efectuar tres envíos.
Consiste en efectuar un envío por cada libro: un envío para el Mayor, otro para el Diario.
En cada uno de los LceCoCierre se deberá incluir el CAL o COCERTIF respectivo.
En otro LceCoCierre incluir Balance y Diccionario
Un contribuyente podría mantener sus libros Diario y Mayor efectuando cierres mensuales, si ese
es el caso, el contribuyente puede enviar por separado cada uno de los resúmenes o incluir los
doce comprobantes de cierre en un mismo envío obligatorio.
No se pueden mezclar años distintos en un CoCierre

6

6. Resúmenes
Un COCIERRE contiene Los resúmenes de libros deben ser enviado en los envíos obligatorios y
en los envíos de libros.
En el caso de los envíos obligatorios el resumen del libro debe incluir toda la información del
periodo declarado
Para el caso de los envíos de libros (a pedido por notificación), su resumen debe corresponder al
detalle de la solicitud, por ejemplo si se solicita la información de dos cuentas contables del libro
mayor, en el resumen que va en ese envío, se deberá entregar la información de esas dos
cuentas.

6.1.

Resumen Diario

En el Resumen Diario se deberán registrar cronológicamente la suma de los comprobantes y
movimientos por cada día que se efectúen registros contables.

7

Campo
1 Rut
Contribuyente
2 Periodo
Tributario

Oblig

Tipo
1 R
1

2.1 Inicial

1 N

2.2 Final

1 N

Largo
Max

Descripción
Rut del contribuyente
Indica los meses del año comercial que se están informando.
Si es un resumen de un Libro anual del año 2005 se debe
indicar
Inicial: 200501
Final : 200512
6 Si es un Resumen del Libro de Enero de 2005
Inicial: 200501
6 Final : 200501

3 Moneda

2 N

Código de Moneda: Obligatorio si la información en el libro
está en una moneda distinta de pesos. Ver en el siguiente link
http://www.sii.cl/declaraciones_juradas/suplemento/2005/54.p
df

4 Rectificatoria

2 N

2 En caso que se efectúen rectificaciones al libro, se debe
reenviar. Este campo corresponde a un número secuencia, el
cual debe coincidir con el del Libro respectivo.
Información Diaria del Libro. Es una por cada día en que se
efectúen registros contables. Sólo para el período tributario
informado en el libro.

5.1 Fecha contable

1 A

10 En formato AAAA-MM-DD Indica la fecha de contabilización.
Sólo se indican las fechas en que se hicieron
contabilizaciones.

5.2 Cantidad de
Comprobantes

1 N

18 Cantidad de Comprobantes que se han registrado en la fecha
contable

5.3 Cantidad
Movimientos

1 N

18 Cantidad Total de movimientos para la fecha contable. Un
movimiento es una línea de registro.

5.4 Suma Valor
Comprobante

1 N

18 Suma de todos los comprobantes que se han registrado en la
fecha contable

5 Registro Diario

6 Cierre

6.1 Cantidad de
Comprobantes
6.2 Cantidad
Movimientos

Datos al cierre del Diario. Si el Diario es mensual,
corresponde a los valores al cierre mensual que deben
considerar la Apertura + Registros en el período
1 N

18 Suma Cantidad de Comprobantes (Período)

1 N

18 Suma Cantidad de Movimientos (Período)

6.3 Suma Valor
Comprobante

1 N

18 Suma de todos los comprobantes del Periodo

6.4 Valor
Acumulado

1 N

18 Valor acumulado a la fecha de cierre. Corresponde a Suma
Valor Comprobante apertura + Sumatoria Suma Valor
Comprobante (Periodo)

7 Rut Firma

1 R

8 Fecha Firma

1 A

9 Firma
Electrónica

Rut del firmante del Resumen Diario
19 Fecha y Hora de la Firma de este documento.
En formato AAAA-MM-DDTHH:MI:SS
Del resumen

8

6.2.

Resumen Mayor

En el resumen del Libro Mayor se deberán registrar las cantidades, montos de los movimientos y
saldos de las distintas cuentas durante el periodo informado. El orden en que se informan las
cuentas debe ser el mismo que el orden de las cuentas del diccionario.

Campo
1 Rut
Contribuyente
2 Periodo
Tributario

Oblig

Tipo
1 R
1

2.1 Inicial

1 N

2.2 Final

1 N

3 Moneda

2 N

4 Rectificatoria

2 N

5 Cuenta

Largo
Max

Descripción
Rut de contribuyente autorizado
Indica los meses del año comercial que se están informando. Si
es un resumen de un Libro anual del año 2005 se debe indicar
Inicial: 200501
Final : 200512
Si es un Resumen del Libro de Enero de 2005
Inicial: 200501
6 Final : 200501
6
Código de Moneda: Obligatorio si la información en el libro está
en moneda distinta de pesos. Ver en el siguiente link
http://www.sii.cl/declaraciones_juradas/suplemento/2005/54.pdf
2 En caso que se efectúen rectificaciones al libro, se debe
reenviar. Este campo corresponde a un número secuencia, el
cual debe coincidir con el del Libro respectivo.
Información por cada cuenta. Sólo para el período tributario
informado en el libro. Se informan sólo las cuentas que tengan
movimientos en el período y/o Saldo al finalizar éste. Se
informan al último nivel de las cuentas.

9

5.1 Código Cuenta

1 A

20 Los códigos de Cuenta deben estar informados en el diccionario.

5.2 Cantidad de
Movimientos

1 N

18 Cantidad total de movimientos de esa cuenta en el período
Informado

6 Cierre

Datos al cierre del Mayor. Si el Mayor es mensual, corresponde
a los valores al cierre mensual que deben considerar la Apertura
+ Registros en el período

6.1 Montos periodo

Valores de los movimientos del período. Sólo se informa si hubo
al menos un movimiento, ya sea debe o haber en el período.

6.1.1 Debe

2 N

18 Suma de montos al debe, de la cuenta, en el período (no incluye
el saldo inicial). No es obligatorio registrar si es 0.

6.1.2 Haber

2 N

18 Suma de montos al haber, de la cuenta, en el período (no
incluye el saldo inicial). No es obligatorio registrar si es 0.

6.1.3 Saldo Deudor

2 N

18 Considera sólo los movimientos del período. Se trata del
diferencial del período entre Debe (6.1.1) y Haber (6.1.2). No es
obligatorio si no hubo ningún movimiento (Es decir si Debe y
Haber son ambos igual a 0) Se indica “Deudor” si Debe Haber
>0 o Debe - Haber=0 Se indica “Acreedor” si Haber – Debe >0

6.1.4 Saldo Acreedor

2 N

18

6.2 Montos
Acumulados

Valores de los movimientos al cierre del Período, incluyendo
apertura

6.2.1 Debe

2 N

6.2.2 Haber

2 N

18 Haber del período + Haber apertura

6.2.3 Saldo Deudor

2 N

6.2.4 Saldo Acreedor

2 N

18 Se calcula en base a los dos campos anteriores Saldo Deudor:
Debe - Haber >0 o Debe-Haber=0 Saldo Acreedor: Haber –
Debe >0
18

7 Rut Firma

1 R

8 Fecha Firma

1 A

9 Firma
Electrónica

18 Debe del período + Debe apertura

Rut del firmante del Resumen Diario
19 Fecha y Hora de la Firma de este documento. En formato AAAAMM-DDTHH:MI:SS.
Del resumen

10

7. Balance

Campo

Oblig

Tipo

Largo
Max

Descripción

1 Rut
Contribuyente
2 Periodo
Tributario

1 R

Rut de contribuyente autorizado

1

Indica el mes de cierre del balance. En los envíos obligatorios el
mes debe ser 12.

3 Moneda

2 N

Código de Moneda: Obligatorio si la información en el libro está
en una moneda distinta de pesos. Ver en el siguiente link
http://www.sii.cl/declaraciones_juradas/suplemento/2005/54.pdf

4 Rectificatoria

2 N

5 Cuenta

2 En caso que se reemita, se debe reenviar. Es un número
secuencia, el cual debe coincidir con el del Libro respectivo.
Información por cada cuenta. Es obligatorio informar las cuentas
que tengan saldo al finalizar el período o que tuvieron
movimiento.

5.1 Código Cuenta

1 A

20 Los códigos de Cuenta deben estar informados en el diccionario.

5.2 Debe

1 N

18 Total de montos al debe de la cuenta al terminar el período,
incluye el valor de apertura. Se registra si es 0

5.3 Haber

1 N

18 Total de montos al haber de la cuenta al terminar el período,
incluye el valor de apertura. Se registra si es 0.

5.4 Saldo Deudor

2 N

18 Saldo Deudor: Debe Haber >0 o Debe Haber=0

5.5 Saldo Acreedor

2 N

18 Saldo Acreedor: Haber – Debe >0

6 Rut Firma

1 R

7 Fecha Firma

1 A

8 Firma
Electrónica

Rut del firmante del Resumen Diario
19 Fecha y Hora de la Firma de este documento. En formato AAAAMM-DDTHH:MI:SS.
Del resumen

11

8. Envío de Libros
Un envío de Libros está conformado por Información general del envío, por los libros mismos y,
sólo en caso que los libros correspondan a un período no cerrado, se debe enviar adicionalmente
el Diccionario para permitir la “traducción” de las cuentas de la empresa a los códigos SII y el
Cocertif o CAL, según corresponda.

8.1.

Información General del envío

Campo

Oblig

Tipo

1 Rut Envía

1 R

2 Rut Contribuyente

1 A

Largo
Max

Descripción
Rut del firmante autorizado a enviar libros

10 Rut del contribuyente

3 Notificación
3.1 Tipo

1 N

3.2 Número
4 Fecha Firma

1: Formulario 3301 2: Formulario 3302
Número de Notificación. Folio preimpreso en el formulario

1 A

19 Fecha y Hora de la Firma de este documento. En formato
AAAA-MM-DDTHH:MI:SS.

En el envío se pueden enviar un solo libro o varios libros. En general, un libro de un período
tributario será requerido completo, es decir con el total de la información a nivel de cuentas en el
caso del Mayor, o el total de los comprobantes y movimientos del Diario. Sin embargo, también se
podrá requerir el envío de un Libro en forma parcial, por ejemplo la información de una única
cuenta, en el caso del mayor. En este último caso, se deberá anotar el campo “parcial”
adicionalmente, junto al esquema de cada libro que tenga esta característica

12

Campo

Oblig

1 Parcial

8.2.

Tipo
2 B

Largo
Max

Descripción
True: en caso que el respectivo libro sea “parcial”. Este
campo no se requiere si el libro enviado es completo ya
que se asume “false”.

Libro Diario

El Libro Diario Contiene el Resumen Diario (6.1) y la información de detalle a nivel de
comprobantes. Su registro debe ser cronológico.

13

Campo

Oblig

Tipo

Largo
Max

Descripción

1 Valor apertura

2 N

18 Sólo si hay saldos al inicio del período informado. Por
ejemplo, si el inicio del periodo informado es el 1 de enero,
no debe ir esta información. Indica el Total del valor de los
comprobantes al terminar el periodo anterior.

2 Tipo Comprobante

1 A

1 I: Ingreso
E: Egreso
T: Traspaso
U: Unico
O: Otro

3 Número
Comprobante
4 Fecha Contable

1 A

18

1 A

10 AAAA-MM-DD

5 Glosa análisis

3 A

120 Glosa del tipo de movimiento

6 Movimientos
6.1 Codigo cuenta

1

6.2 RUT
6.3 Nombre

2 R
2 A

6.4 Tpo Documento

2 A

Movimientos del comprobante. Debe haber al menos 2
movimientos
Código cuenta del contribuyente
Información que permite el análisis de la cuenta. El tipo de
120 información debe permitir que en un proceso de
fiscalización se pueda efectuar análisis.
60

6.5 Número

2 A

18

6.6 Fecha emisión

2 A

10

6.7 Fecha vencimiento

2 A

10

6.8 Glosa Ref

2

6.8.1 Glosa

2 A

Información adicional, que permite el análisis de la cuenta.
Glosa ref: indica el tipo de información que se
detallará. Ref: Indica el dato especifico Por ejemplo si se
requiere detallar un numero de cuenta cte. se anotará
Glosa Ref.: “Cuenta Cte. Banco XXXX”
REF: 023457890
30 Se pueden indicar hasta 4 datos adicionales

6.8.2 Ref

2 A

20

6.9 Debe

2 N

6.10 Haber

2 N

18

1 N

18 Debe ser igual a suma de “Debe” y suma de “Haber” de
todos los movimientos.

7 Valor Comprobante

18 Debe o haber del movimiento en la cuenta. Debe existir uno
de ambos campos

14

8.3.

Libro Mayor

El Libro Mayor Contiene el Resumen Mayor (6.2) y la información de detalle a nivel de cuentas. El
orden de las cuentas debe ser igual a las del resumen. Las cuentas que se deben informar son
aquellas que tienen saldo y/o movimientos.

15

Campo

Oblig

Tipo

1 Código Cuenta

1 A

2 Apertura

2

Largo
Max

Descripción

20 Código de la cuenta del plan contable del contribuyente. Se
informa sólo las cuentas que tienen saldo apertura y/o
movimientos en el periodo informado
Sólo si hay saldos al inicio del período informado

2.1 Debe

2 N

18 Total debe hasta el periodo anterior. Corresponde al Debe
al cierre del periodo anterior. Es obligatorio si ha habido
movimientos al Debe en los periodos anteriores.

3.1 Haber

1 N

18 Total haber hasta el periodo anterior. Corresponde al Haber
al cierre del periodo anterior. Es obligatorio si ha habido
movimientos al Haber en los periodos anteriores.

3.2 Saldo Deudor

2 N

18 Si se informa apertura, entonces debe existir Saldo

3.3 Saldo Acreedor

2 N

18 Deudor o Acreedor

4 Movimientos

2

4.1 Tpo Comprobante

1 A

4.2 Número
Comprobante

1 A

Sólo si hay movimientos en la cuenta, durante el período
informado. Se deben informan todos los movimientos del
periodo.
1 I: Ingreso
E: Egreso
T: Traspaso
U: Unico
O: Otro
18 Puede ser alfanumérico. Esto se aplica en aquellos casos
en que cada comprobante tiene un distintivo que
corresponde a una parte alfanumérica, para identificar el
tipo de transacción o el sistema del que proviene, y un
correlativo por tipo de transacción.

4.3 Fecha Contable

1 A

10 AAAA-MM-DD

4.4 Glosa análisis

2 A

120 Glosa del tipo de movimiento

4.5 RUT

2 R

4.6 Nombre

2 A

Información que permite el análisis de la cuenta. El tipo de
información debe permitir que en un proceso de
120 fiscalización se pueda efectuar análisis.

4.7 Tpo Documento

2 A

15

4.8 Número

2 A

18

4.9 Fecha emisión

2 A

10

4.10 Fecha vencimiento

2 A

10

4.11 Glosa Ref

2

Información adicional, que permite el análisis de la cuenta.
Glosa ref: indica el tipo de información que se
30 detallará. Ref: Indica el dato especifico Por ejemplo si se
requiere detallar un numero de cuenta cte. se anotará
20 Glosa Ref.: “Cuenta Cte. Banco XXXX”
REF: 023457890
Se pueden indicar hasta 4 datos adicionales

4.11.1 Glosa

2 A

4.11.2 Ref

2 A

4.12 Debe

2 N

18 Debe o haber del movimiento. Debe existir uno de ambos
campos.

4.13 Haber

2 N

18

16

9. Libros de Compra y Venta
Los libros de compras y Venta de un contribuyente que no es facturador electrónico, deben ser
enviados mensualmente en el formato establecido en el Instructivo IECV:
http://www.sii.cl/factura_electronica/formato_iecv.pdf
Agregando el CAL o Cocertif respectivo.

10.

Anexos

10.1.

Tabla 1: Códigos de Archivos Contables
CODIGO
DIARIO
MAYOR
BALANCE

10.2.

DIARIO
MAYOR
BALANCE

LIBRO

Tabla 2: Códigos de tipos de Libros
Código
Agrupación
1 CONTABLE
6 COMPRA Y VENTA

Libros que incluye la agrupación
Diario, Mayor, Balance,
Libro de Compras, Libro de Ventas

17
