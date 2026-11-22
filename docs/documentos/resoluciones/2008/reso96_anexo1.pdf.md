---
url: https://www.sii.cl/documentos/resoluciones/2008/reso96_anexo1.pdf
titulo: Registro Tributario de Castigo de Deudas Incobrables – Anexo 1: Formato “ ”
categoria: otros
---
ANEXO N° 1

Registro Tributario de Castigo de Deudas Incobrables
SECCIÓN A: Identificación del contribuyente emisor
N°

Posición
Desde
Hasta

CAMPOS

Largo

Carácter

Validaciones de Formato

RUT Contribuyente
1

RUT

1

8

8

NUM

>0 Obligatorio

DV

9

9

1

Debe cumplir con módulo 11

2
3
4
5
6
7

Nombre o Razón social
Domicilio Postal
Comuna
Correo electrónico
Teléfono
Año tributario informado

10
40
50
65
85
95

39
49
64
84
94
102

30
10
15
20
10
8

ALFA
ALFA
ALFA
ALFA
ALFA
NUM
NUM

8

Código de moneda en que se informa

103

105

3

NUM

Largo

Carácter

8
1
30

NUM

AAAA: año informado
Tabla Códigos Suplemento Declaraciones
Juradas

SECCIÓN B: Datos de deudas incobrables castigadas
Columna

Posición
Desde
Hasta

CAMPOS

Columnas " Identificación del deudor o cliente"
RUT del deudor o cliente
(1)

RUT
DV

106
114
(2)
Nombre o Razón social del deudor o cliente
115
Columnas “ Datos de la operación que dio origen al crédito o deuda.”

113
114
144

Código tipo documento

145

146

2

NUM

(4)

Otro tipo de documento
Fecha documento

147
162

161
169

15
8

ALFA
FECHA

Número documento

170

179

10

NUM

(5)

(7)

Código tipo de operación

180

181

2

NUM

(8)

Monto total de la operación

182

211

30

NUM

(9)

Código de moneda operación

212

214

3

ALFA

Columnas " Datos del crédito otorgado"

>0 Obligatorio
Debe cumplir con módulo 11

ALFA

(3)

(6)

Validaciones de Formato

Códigos:
01 Factura
02 Factura de exportación
03 Boleta
04 Boleta de Honorarios
05 Sin documento
06 Otro tipo de documento
Si columna (3) = 06
DDMMAAAA
DD: día informado
MM: mes informado
AAAA: año informado

Códigos:
01 Venta de bienes del giro
02 Venta de bienes que no son del giro
03 Prestación de servicios del giro
04 Prestación de otros servicios
05 Operación de Crédito de dinero
(Préstamo)
06 Otra
Tabla Códigos Suplemento Declaraciones
Juradas

(10)

Código tipo documento

215

216

2

NUM

(11)
(12)

Otro tipo de documento
Fecha del documento

217
232

231
239

15
8

ALFA
FECHA

(13)

Número documento

240

249

10

NUM

Monto del crédito otorgado

250

279

30

Código de moneda de la deuda o crédito

280

282

3

312

30

NUM

327
335

15
8

ALFA
FECHA

(19)
N° comprobante contable
336
350
Columanas " Datos del crédito castigado según normas de la Ley de la Renta"
Monto pesos de crédito castigado s/ normas Ley de
351
380
(20)
la Renta
(21)
Año tributario
381
384

15

ALFA

30

NUM

4

NUM

30

NUM

(14)
(15)

Columanas " Datos del crédito castigado según registros contables"
Monto total del crédito castigado s/registros
(16)
283
contables en pesos
(17)
N° cuenta contable
313
(18)
Fecha del registro contable
328

(22)

Diferencia temporal

385

414

Códigos:
01 Letra de cambio
02 Pagaré
03 Cheque
04 Escritura pública
05 Escritura privada
06 No se emitió documento
07 Otro
Si columna (10) = 07
DDMMAAAA
DD: día informado
MM: mes informado
AAAA: año informado

<= al monto registrado en la columna (8)
ALFA

(23)

Motivos del castigo

415

434

20

ALFA

(24)
(25)

Otro motivo
Observaciones

435
455

454
474

20
20

ALFA
ALFA

Largo

Carácter

Tabla Códigos Suplemento Declaraciones
Juradas

DDMMAAAA
DD: día informado
MM: mes informado
AAAA: año informado

AAAA: año castigo
Resultado de la diferencia entre la columna
(16) y la columna (20)

Códigos:
01 Incumplimiento al requerimiento de pago
02 Quiebra del deudor
03 Deudor inubicable o desaparecido
04 Fallecimiento del deudor
05 Cesación de pagos del deudor hecha
valer ante un Tribunal por la empresa
06 Otro motivo
Si columna (23) = 06

SECCIÓN C: Resumen de datos informados
N°

CAMPOS

Posición
Desde
Hasta

1

Total castigos según registros contables

475

504

30

NUM

2

Total castigos según normas Ley de la Renta

505

534

30

NUM

3

Total diferencias temporales

535

564

30

NUM

4

Total de registros informados

565

594

30

NUM

Validaciones de Formato
Sumatoria de los registros informados en la
columna (16) de la sección B
Sumatoria de los registros informados en la
columna (20) de la sección B
Resultado de la diferencia entre el campo
N°1 y el campo N°2 de esta sección.
>=0
Contar el total de registros informados en la
sección B.
