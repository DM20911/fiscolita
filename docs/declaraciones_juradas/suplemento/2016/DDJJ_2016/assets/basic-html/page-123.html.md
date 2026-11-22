---
url: https://www.sii.cl/declaraciones_juradas/suplemento/2016/DDJJ_2016/assets/basic-html/page-123.html
titulo: Suplemento Declaraciones Juradas 2016
categoria: declaraciones_juradas
---
|  |  |
| --- | --- |
|  |  |

* [Скачать PDF](./../common/downloads/Suplemento_Declaraciones_Juradas_2016.pdf)

 123 / 125

Basic version

123 / 125

Ediciones Especiales

diciembre de 2015

125

**6.**

**Construcción del archivo de la declaración.**

El archivo en que se presentará la declaración deberá construirse de acuerdo a las especificaciones acá descritas en formato

de archivo de texto plano, señalando primero la sección a la que corresponde la información y a continuación el detalle de los

registros que la componen, de manera que el archivo se conformará del siguiente modo:

Sección A

Detalle registros sección A

------------------------------------

Sección B

Detalle registros sección B

-----------------------------------

Sección C

Detalle registros sección C

-----------------------------------

Cuadro Resumen de la declaración

Detalle registros cuadro resumen

-----------------------------------

Para asegurar la integridad de la información y su correcta carga se deben seguir las siguientes reglas generales:

•

El archivo debe tener por nombre: CF\_TR\_RutDeclarante\_AT.dat

Donde “RutDeclarante” corresponde a la cadena formada por el Rut y Dv (sin guión) del declarante y “AT” al año tributario al

que corresponde la declaración.

Ejemplo: CF\_TR\_12345678K\_2014.dat

•

Evitar el uso de tildes, signos de puntuación y/o signos aritméticos en la información que se ingrese, salvo en el caso de la

dirección email en que en el cuerpo se permite el uso del guión (-), guión bajo o “underline” (\_) y en el dominio el uso del

punto.

•

La letra “Eñe” (ñ o Ñ) debe cambiarse a “Ene” (n o N).

•

Los datos correspondientes a fechas se ingresarán en campos numéricos con formato ddmmaaaa.

•

Respetar el largo y tipo de dato de cada campo. Si el dato a informar es de un largo menor se debe completar a la derecha

con tantos espacios en blanco, en el caso de campos alfanuméricos, o a la izquierda con tantos ceros, en el caso de campos

numéricos, sean necesarios para alcanzar el largo máximo de dicho campo.

Ejemplos:

**1.**

**Dato a ingresar: “465”, Largo máximo de campo: 5**

**Se debe ingresar: “00465”**

**2.**

**Dato a ingresar: “Daniel Muñoz G.”, Largo máximo de campo: 20**

Se debe ingresar: “Daniel

**x**

Munoz

**x**

G

**xxxxxx**

“ (note que se eliminó el punto después de la letra “G” y se agregaron los

espacios en blanco, representados por cada

**“x”,**

hasta completar el largo máximo del campo).

El formato de registro de los campos de cada sección se detalla a continuación, señalando la ubicación inicial y final del dato dentro

de la línea de registro y la ubicación del separador que se utilizará (en este caso un punto y coma), por otro lado se utilizará la

siguiente nomenclatura para indicar tipo de dato y largo de campo:

Tipo de Dato: N = numérico; A= alfanumérico, y

Largo de campo: (X), donde X= 1, 2, 3, …, N número de caracteres

Ejemplos:

Campo numérico de largo 5 = N(5)

Campo alfanumérico de largo 25 = A(25)

**FORMATO DE REGISTRO**

**D**

**E**

**S**

**C**

**R**

**I**

**P**

**C**

**I**

**Ó**

**N**

**D**

**E**

**L**

**O**

**S**

**C**

**A**

**M**

**P**

**O**

**S**

Inicial

Final

1

8

N(8)

9

10

10 A(1)

11

12

26 A(15)

27

28

57 A(30)

58

59

59 N(1)

60

61 140 A(80)

141

142 146 N(5)

147

148 177 A(30)

178

179 198 A(20)

199

200 219 A(20)

220

221 230 N(10)

231

232 241 N(10)

242

243 244 A(2)

245

Inicial

Final

1

15 A(15)

16

17

46 A(30)

47

48

55 N(8)

56

57

58 A(2)

59

60

61 A(2)

62

Inicial

Final

CIUDAD

CORREO ELECTRÓNICO (nombre)

Ubicación Datos

Formato

Nombre Campo

ROL ÚNICO TRIBUTARIO: CUERPO DEL RUT

TAX ID

TAX ID TRUST

NOMBRE O RAZÓN SOCIAL

FECHA DE CREACIÓN

PAÍS DE RESIDENCIA

PAÍS DE CREACIÓN, REGISTRO UORIGEN

Ubicación separador (punto y coma)

Ubicación separador (punto y coma)

**Sección A: Datos del Declarante**

CORREO ELECTRÓNICO (dominio)

ROL ÚNICO TRIBUTARIO: DÍGITO VERIFICADOR

**Sección B: DATOS DE CONFORMACIÓN DEL TRUST**

Nombre Campo

Ubicación Datos

Formato

FAX

TELÉFONO

PAÍS DE RESIDENCIA

NOMBRE O RAZÓN SOCIAL

TIPO DECLARANTE

DOMICILIO POSTAL

COMUNA

**Sección C: DATOS DE CONSTITUYENTES, TRUSTEES Y BENEFICIARIOS**

Nombre Campo

Ubicación Datos

Formato Ubicación separador (punto y coma)

**M**

**P**

**O**

**S**

**S**

**e**

**c**

**c**

**i**

**ó**

**n**

**A**

**:**

**I**

**D**

**E**

**N**

**T**

**I**

**F**

**I**

**C**

**ACIÓN DEL DECLARANTE.**

En esta sección el declarante deberá indicar los datos referentes a su propia identificación y la calidad que dese

sobre los Trust que informe, señalando los siguientes datos:

60

61 A(2)

62

Inicial

Final

1

15 A(15)

16

17

17 N(1)

18

19

48 A(30)

49

50

64 A(15)

65

66

73 N(8)

74

75

75 A(1)

76

77 156 A(80)

157

158 159 A(2)

160

Inicial

Final

1

5

N(5)

6

7

21 A(15)

22

23

27 N(5)

28

29

33 N(5)

34

35

39 N(5)

40

41

48 N(8)

49

50

50 A(1)

51

PAÍS DE CREACIÓN, REGISTRO UORIGEN

DOMICILIO

**Sección C: DATOS DE CONSTITUYENTES, TRUSTEES Y BENEFICIARIOS**

Nombre Campo

Ubicación Datos

Formato Ubicación separador (punto y coma)

TAX ID TRUST

NOMBRE O RAZÓN SOCIAL

TAX ID INFORMADO

RUT INFORMADO: CUERPO DEL RUT

RUT INFORMADO: DÍGITO VERIFICADOR

TIPO INFORMADO

PAÍS DE RESIDENCIA

**CUADRO RESUMEN FINAL DE LA DECLARACION**

Nombre Campo

Ubicación Datos

Formato Ubicación separador (punto y coma)

RUT REPRESENTANTE LEGAL: DÍGITO VERIFICADOR

NÚMERO DE TRUST INFORMADOS

TAX ID TRUST

N° DE CONSTITUYENTES

N° DE TRUSTEES

N° DE BENEFICIARIOS

RUT REPRESENTANTE LEGAL: CUERPO DEL RUT

**DESCRIPCIÓN DE LOS CAMPOS**

**Sección A: IDENTIFICACIÓN DEL DECLARANTE.**

En esta sección el declarante deberá indicar los datos referentes a su propia identificación y la calidad que desempeña sobre los

Trust que informe, señalando los siguientes datos:

**“Rol Único Tributario”:**

Número de RUT que posee el declarante. Consta del cuerpo (8 caracteres) y dígito verificador (1 carácter).

Ambas partes deben ir separadas por punto y coma.

**Ejemplo:**

RUT = 12345678-K se ingresa como 12345678;K

**“Tax ID”:**

Se debe indicar el Tax ID o número de identificación fiscal que posee el declarante en su país de origen, en caso de

declarantes extranjeros que han constituido residencia en Chile.

**“Nombre o Razón Social”:**

Deberá indicar el nombre o razón social del declarante.

**“Tipo Declarante”:**

Deberá indicar mediante el código adecuado, el tipo de declarante de acuerdo al siguiente recuadro:

**Código Descripción**

1

Trustee

2

Administrador de Trust

3

Ambas

**“Domicilio Postal”:**

Deberá indicar el domicilio postal del declarante.

**“Comuna”:**

Deberá indicar el código de la comuna del domicilio postal de acuerdo a la tabla “Códigos de Comuna” del anexo N°

1 de este instructivo.

**“Ciudad”:**

Debe indicar el nombre de la ciudad en que se encuentra el domicilio postal informado.

**“Correo Electrónico”:**

Debe indicar la dirección de correo electrónico del declarante. Consta del nombre del email (20 caracteres)

y dominio del correo (20 caracteres). Ambas partes deben ir separadas por punto y coma.

**Ejemplo:**

[mi\_email@mail.com](mailto:mi_email@mail.com)

se ingresa como mi\_email

**xxxxxxxxxxxx**

;mail.com

**xxxxxxxxxxxx**

donde cada “

**x**

” representa un

espacio en blanco utilizado para completar el largo máximo del campo correspondiente.

**“Fax”:**

Debe indicar el número de fax en formato código de área + número.

**Ejemplo:**

32-12345678 se ingresa como 3212345678

**“Teléfono”:**

Debe indicar el número de teléfono en formato código de área + número.

**Ejemplo:**

**Número de Teléfono Fijo:**

02-12345678 se ingresa como 0212345678

**Número de Celular:**

91234567 se ingresa como 0991234567

**“País de Residencia”:**

Debe ingresar el código del país de residencia del declarante. El código a utilizar será de los disponibles

en la tabla “Códigos de País” contenida en el anexo N° 2 de este instructivo.

**Sección B: DATOS DE CONFORMACIÓN DEL TRUST.**

En esta sección el declarante debe registrar los datos de identificación del Trust creado de acuerdo a disposiciones de derecho

extranjero.

Los datos a registrar serán los siguientes:

**“Tax ID”:**

Se debe indicar el Tax ID o número de identificación fiscal asignado al Trust en el país de residencia.

**“Nombre o Razón Social”:**

Deberá indicar el nombre o razón social del Trust con que se encuentra registrado en el país de

residencia.

[1](./page-1.html)
…
[114](./page-114.html)
[115](./page-115.html)
[116](./page-116.html)
[117](./page-117.html)
[118](./page-118.html)
[119](./page-119.html)
[120](./page-120.html)
[121](./page-121.html)
[122](./page-122.html)
[123](./page-123.html)
[124](./page-124.html)
[125](./page-125.html)
[Servicio de Impuestos Internos](https://www.sii.cl/)
