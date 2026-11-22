---
url: https://www.sii.cl/documentos/resoluciones/2011/reso44.pdf
titulo: Anexo – : Formato de los archivos digitales correspondientes a nóminas que deben enviar los Depósitos de Valores al Servicio de Impuestos Internos (SII).
categoria: otros
---
ANEXO
“Formato de los archivos digitales correspondientes a nóminas que deben enviar los
Depósitos de Valores al Servicio de Impuestos Internos (SII).”
1. Objetivo
Este documento tiene como objetivo detallar el formato de los archivos “Informe de Eventos de
Capital” e “Informe de Movimientos”, que los Depósitos de Valores deberán proveer al Servicio de
Impuestos Internos (SII) hasta el 31 de marzo de cada año, con información correspondiente a las
operaciones realizadas hasta el día 31 de diciembre del año inmediatamente anterior, de los
instrumentos que se encuentren acogidos al artículo 104 de la Ley de Impuesto a la Renta (LIR).
Los mencionados archivos deberán ser generados por cada Depósito de Valores y enviados al SII, a
través de una aplicación Web autenticada del SII.

2. Informe de Eventos de Capital
Este archivo provee información de los eventos de capital de los instrumentos que se encuentran
acogidos al artículo 104 de la Ley de Impuesto a la Renta (LIR).

2.1 Nombre del Archivo
DV_{RUT del Depósito de Valores}_Capital.DAT

2.2 Formato de Registro
DESCRIPCIÓN
Fecha de pago, Fecha. AAAAMMDD (1)
Moneda del Instrumento (2)
Código de Instrumento (3)
Tipo de Instrumento (4)
Código Pagador (5)
RUT del Pagador (6)
Código Emisor (7)
RUT Emisor, sin edición (8)
Código del Responsable (9)
RUT del Responsable, sin edición (10)
Código Beneficiario (11)
RUT del Beneficiario (12)
Código del Titular de la Cuenta donde se Registran los
Valores (13)
RUT del Titular de la Cuenta donde se Registran los Valores
(14)
Número de Cuenta donde se Registran los Valores (15)
Posición nominal (16)
Tipo posición vencida (17)
Código de Operación (18)
Moneda de pago (19)
Monto total pagado en moneda del instrumento (20)
Monto de amortización pagado en moneda del instrumento
(21)
Monto de interés pagado en moneda del instrumento (22)

UBICACIÓN
INICIAL
FINAL
1
8
9
10
11
22
23
24
25
29
30
39
40
44
45
54
55
59
60
69
70
74
75
84
85
89

FORMATO
9(08)
9(02)
X(12)
9(02)
9(05)
X(10)
9(5)
X(10)
9(5)
X(10)
9(05)
X(10)
9(05)

90

99

X(10)

100
108
127
129
131
133
152

107
126
128
130
132
151
170

9(8)
9(15)V9(04)
X(02)
X(02)
9(02)
9(15)V9(04)
9(15)V9(04)

171

189

9(15)V9(04)

Código de Formato:
9: Valor numérico
X: Valor alfanumérico
V9: parte decimal

1

2.3 Descripción de Campos
(1) Fecha de Pago, fecha de pago de los eventos de capital informados en la cartola, en donde:
AAAA: Año
MM: Mes
DD: Día
(2) Moneda del Instrumento, corresponde al código de la moneda en la cual está expresado el
instrumento (conocida también como moneda de origen del instrumento). Los códigos válidos son:
CÓDIGO
60
61
62
63
64
65
66
67
68
69
70
71

DESCRIP. CORTA DESCRIP LARGA
: PESOS
Pesos
: UF
Unidad de Fomento
: US$ REF
Dólar Referencial
: US$ PREF
Dólar Preferencial
: US$ OBS
Dólar Observado
: IVP
Índice Valor Promedio
: US$CHILEAP Dólar Vendedor Banco Chile Apertura
: US$ESTADO Dólar Banco del Estado
: EURO
Euro
: US$PARALEL Dólar Paralelo
: US$CHILE12 Dólar Vendedor Banco Chile 12 AM
: ICP
Índice de Cámara Promedio

(3) Código de Instrumento, código del instrumento (nemotécnico) para el cual se informa el evento
de capital.
(4) Tipo de Instrumento, corresponde al código del tipo de instrumento. Los valores válidos son:
CÓDIGO
01
02
03
04
06
08
11
12
15
16
19
21
22
23
24
25
27
29
31
44
45
46
47
49
50
51
52
53
54
55
56

DESCRIP. CORTA
BONO SUB
Debentures
BONO BANCO
BONO FLOT
tds
bca
PRD
DPF
PDBC
PRBC
PRC
LH
LH&
LH&&
LH*
LH**
BR
ACCION
CFI
CERO
ESTF
ECNS
ECS
CFM
BCP
BCU
BCD
BTP
BTU
PCX
BCX

DESCRIP LARGA
Bono Subordinado
Debentures
Bono Banco
Bono Flotante
Título de deuda securitizada
Bono convertible en acciones
Pagaré Reajustable dólares Bco. Central
Depósito a Plazo Fijo
Pagaré Descontable Bco. Central
Pagaré Reajustable Bco. Central
Pagaré Reajustable con Cupones
Letra Hipotecaria
Letra Hipotecaria 1 cupón precortado
Letra Hipotecaria 2 cupones precortados
Letra Hipotecaria 1 cupón precortado
Letra Hipotecaria 2 cupones precortados
Bono Reconocimiento
Acciones
Cuota Fondos de Inversión
Cupón de Emisión Reajustable Opcional
Emisiones Securitizadas Tasa Flotante
Efectos de Comercio No Seriados
Efectos de Comercio Seriados
Cuotas de Fondos Mutuos
Bono Banco Central de Chile en Pesos
Bono Banco Central de Chile en UF
Bono Banco Central de Chile en Dólares
Bono TGR en Pesos
Bono TGR en UF
Pagaré Reajustable US$ BCCH Pagadero US$
Bono BCCH en Dólares Pagadero en US$

2

CÓDIGO
57
58
59
60
70
71
72
73
74

DESCRIP. CORTA
Xero
OSA
Bono MINVU
Paga REPINP
BCP
BCU
BCD
BTP
BTU

DESCRIP LARGA
Cupón de Emisión Reajustable Opcional US$ Pagadero US$
Opción pref. de Suscripción de Acciones
Bonos Leasing MINVU
Pagarés Preparación INP
Bono Bco. Central en Pesos – Art. 104
Bono Bco. Central en UF – Art. 104
Bono Bco. Central en Dólares – Art. 104
Bono TGR en $ - Art. 104
Bono TGR en UF - Art. 104

(5) Código de Pagador, corresponde al código asignado por el Depósito de Valores a la entidad que
efectuará el pago del evento de capital. Si este código no existiera o no se ajustara al formato del
campo debe indicarse sólo con ceros. Ejemplo:
Largo máximo del campo = 5
Código 1 = 12345 se informa de la misma manera.
Código 2 = 435 se informa como “00000”.
Código 3 = Ax445782929087 se informa como “00000”.
(6) RUT del Pagador, corresponde al RUT del Pagador de los eventos de capital. Formato:
999999999X, ejemplo: 095437234K.
(7) Código Emisor, corresponde al código asignado por el Depósito de Valores al Emisor del
instrumento. Si este código no existiera o no se ajustara al formato del campo debe indicarse sólo con
ceros. Ejemplo:
Largo máximo del campo = 7
Código 1 = 1234567 se informa de la misma manera.
Código 2 = 435 se informa como “0000000”.
Código 3 = Ax445782929087 se informa como “0000000”.
(8) RUT Emisor, formato: 999999999X, ejemplo: 095437234K
(9) Código del Responsable, corresponde al código asignado por el Depósito de Valores a la
entidad responsable de efectuar el pago de los eventos de capital. Si este código no existiera o no se
ajustara al formato del campo debe indicarse sólo con ceros. Ejemplo:
Largo máximo del campo = 9
Código 1 = 123456789 se informa de la misma manera.
Código 2 = 435 se informa como “000000000”.
Código 3 = Ax445782929087 se informa como “000000000”.
(10) RUT del Responsable, corresponde al RUT de la entidad responsable de efectuar el pago de
los eventos de capital. Formato: 999999999X, ejemplo: 095437234K.
(11) Código Beneficiario, corresponde al código asignado por el Depósito de Valores al Beneficiario
del evento de capital. Si este código no existiera o no se ajustara al formato del campo debe indicarse
sólo con ceros. Ejemplo:
Largo máximo del campo = 11
Código 1 = 12345678901 se informa de la misma manera.
Código 2 = 435 se informa como “00000000000”.
Código 3 = Ax445782929087 se informa como “00000000000”.
(12) RUT del Beneficiario, corresponde al Rut del Beneficiario de los eventos de capital. Formato:
999999999X, ejemplo: 095437234K.
(13) Código del Titular de la Cuenta donde se Registran los Valores, corresponde al código
asignado por el Depósito de Valores a la entidad que mantiene los valores afectos al evento de
capital, en alguna cuenta abierta a su nombre en el Depósito de Valores. Esta puede ser una cuenta
de Valores Propios o una cuenta de Terceros Agrupada. Si este código no existiera o no se ajustara
al formato del campo debe indicarse sólo con ceros. Ejemplo:
Largo máximo del campo = 13
Código 1 = 1234567890123 se informa de la misma manera.

3

Código 2 = 435 se informa como “0000000000000”.
Código 3 = Ax445782929087 se informa como “0000000000000”.
(14) RUT del Titular de la Cuenta donde se Registran los Valores, corresponde al RUT de la
entidad que mantiene los valores afectos al evento de capital, en alguna cuenta abierta a su nombre
en el Depósito de Valores. Esta puede ser una cuenta de Valores Propios o una cuenta de Terceros
Agrupada.
(15) Número de Cuenta donde se Registran los Valores, corresponde al número de la cuenta en
donde se mantienen los valores para los cuales se está informando el Evento de Capital.
(16) Posición nominal, corresponde a la cantidad de nominales del instrumento, afectos al evento de
capital informado. Campo numérico de largo 19, compuesto por 15 enteros y 4 decimales.
(17) Tipo posición vencida, detalla el estado de la posición vencida pudiendo ser:
DI
BL

:
:

Disponible
Bloqueada

(18) Código de Operación, corresponde al código que identifica el tipo de operación que se informa.
Los códigos válidos son:
VC
VT
VI

: Vencimiento Cupón
: Vencimiento Título
: Vencimiento Instrumento

(19) Moneda de Pago, corresponde a la moneda definida para pagar el instrumento. Los códigos
válidos son:
CÓDIGO
60
64
68

DESCRIP. CORTA
: PESOS
: US$ OBS
: EURO

DESCRIP LARGA
Pesos
Dólar Observado
Euro

(20) Monto total pagado en moneda del instrumento, corresponde al valor total pagado por el
Responsable expresado en la moneda del instrumento. Campo numérico de largo 19, compuesto por
15 enteros y 4 decimales. Este equivale a la suma algebraica de los campos “Monto de amortización
pagado” y “Monto de interés pagado” descritos a continuación.
(21) Monto de amortización pagado en moneda del instrumento, corresponde al valor de la
amortización pagado por el Responsable, expresado en la moneda del instrumento. Campo numérico
de largo 19, compuesto por 15 enteros y 4 decimales.
(22) Monto de interés pagado en moneda del instrumento, corresponde al valor del interés
pagado por el Responsable, expresado en la moneda del instrumento. Campo numérico de largo 19,
compuesto por 15 enteros y 4 decimales.

3. Informe de Movimientos
Este archivo provee información de los movimientos de los instrumentos que se encuentran acogidos
al artículo 104 de la Ley de Impuesto a la Renta (LIR).

3.1 Nombre del Archivo
DV_{RUT del Depósito de Valores}_Movimientos.DAT

4

3.2 Formato de Registro

DESCRIPCIÓN
Fecha de Movimiento, Fecha AAAAMMDD (1)
Tipo de Movimiento (2)
Código de Instrumento (3)
Moneda del Instrumento (4)
Código del Titular de la Cuenta Afecta al Movimiento (5)
RUT del Titular de la Cuenta Afecta al Movimiento (6)
Número de Cuenta Afecta al Movimiento (7)
Tipo de Cuenta Afecta al Movimiento (8)
Saldo Inicial del Instrumento (9)
Monto del Movimiento (10)
Saldo Final del Instrumento (11)

UBICACIÓN
INICIAL
FINAL
1
8
9
11
12
23
24
25
26
30
31
40
41
48
49
49
50
68
69
87
88
106

FORMATO
9(08)
X(3)
X(12)
9(02)
9(05)
X(10)
9(8)
9(1)
9(15)V9(04)
9(15)V9(04)
9(15)V9(04)

3.3 Descripción de Campos
(1) Fecha de Movimiento, fecha en la cual se ejecutó el movimiento, en donde:
AAAA:
MM:
DD:

Año
Mes
Día

(2) Tipo de Movimiento, corresponde al tipo de movimiento resultante asociado al instrumento, para
la Fecha de Movimiento y la Cuenta informada. Los códigos válidos son:
CAR:
ABO:

Cargo Posición
Abono Posición

Si la suma de todos los cargos es superior a la suma de todos los abonos este campo se informa con
el valor “CAR”, en caso contrario se informa con el valor “ABO”.
(3) Código de Instrumento, corresponde al código del instrumento (nemotécnico) para el cual se
informa el movimiento.
(4) Moneda del Instrumento, corresponde a la moneda del instrumento para el cual se informa el
movimiento.
(5) Código del Titular de la Cuenta Afecta al Movimiento, corresponde al código asignado por el
Depósito de Valores a la entidad a nombre de la cual se encuentra abierta la cuenta afecta al
movimiento. Si la cuenta corresponde a una Cuenta de Terceros Individual se indica el código
correspondiente al Tercero, mientras que si la cuenta corresponde a una Cuenta Propia o a una
Cuenta de Tercero Grupal, se indica el código correspondiente al Depositante Mandatario. Si este
código no existiera o no se ajustara al formato del campo debe indicarse sólo con ceros. Ejemplo:
Largo máximo del campo = 5
Código 1 = 12345 se informa de la misma manera.
Código 2 = 435 se informa como “00000”.
Código 3 = Ax445782929087 se informa como “00000”.
(6) RUT del Titular de la Cuenta Afecta al Movimiento, corresponde al RUT de la entidad a nombre
de la cual se encuentra abierta la cuenta afecta al movimiento. Si la cuenta corresponde a una
Cuenta de Terceros Individual se indica el RUT correspondiente al Tercero, mientras que si la cuenta
corresponde a una Cuenta Propia o a una Cuenta de Tercero Grupal, se indica el RUT
correspondiente al Depositante Mandatario. Formato: 999999999X, ejemplo: 095437234K.
(7) Número de Cuenta Afecta al Movimiento, corresponde al número de la cuenta para la cual se
está informando el movimiento.

5

(8) Tipo de Cuenta Afecta al Movimiento, corresponde al tipo de cuenta para la cual se está
informado el movimiento. Los códigos válidos son:
1:

Valores Propios

2:
3:

Valores de Terceros Grupal
Valores de Terceros Individual

(9) Saldo Inicial del Instrumento, corresponde al saldo del instrumento registrado en la cuenta,
expresado en la moneda del instrumento, antes de ejecutado el movimiento. Campo numérico de
largo 19, compuesto por 15 enteros y 4 decimales.
(10) Monto del Movimiento, corresponde al monto del movimiento resultante asociado al
instrumento, para la Fecha de Movimiento y la Cuenta informada. Este monto se expresa en la
moneda del instrumento. Campo numérico de largo 19, compuesto por 15 enteros y 4 decimales.
Equivale al valor absoluto de la diferencia resultante entre la suma de todos los movimientos de cargo
y la suma de todos los movimientos de abono, para la Fecha de Movimiento y la Cuenta informada en
la Cartola.
(11) Saldo Final del Instrumento, corresponde al saldo del instrumento registrado en la cuenta,
expresado en la moneda del instrumento, después de ejecutado el movimiento. Campo numérico de
largo 19, compuesto por 15 enteros y 4 decimales.

6
