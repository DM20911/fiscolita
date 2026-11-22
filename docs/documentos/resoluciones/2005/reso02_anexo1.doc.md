---
url: https://www.sii.cl/documentos/resoluciones/2005/reso02_anexo1.doc
titulo: Formato de Registro e Instrucciones – ANEXOS -
categoria: otros
---
Auxiliar de Registro Impuesto Timbres y Estampillas de Bancos e Instituciones Financieras, según Resolución Ex. SII N°______/ de fecha .....


Nº

CAMPOS
POSICIÓN
LARGO
CARACTER
OBSERVACIONES
Desde
Hasta

1
Rut del Deudor		
	Número de RUT   	
	Dígito Verificador	

1
9

8
9

8
1

N
C

>0
Módulo 11
2
TAX-ID del Deudor


10
24
15
C


3


Nombre o Razón Social del Deudor
25
74
50
C


4

Código País de residencia del Deudor
75
77
3
C

5
Rut del Acreedor
              Número de RUT   	
	Dígito Verificador	

78
86

85
86

8
1

N
C

>0
Módulo 11

6

TAX-ID del Acreedor
87
101
15
C

7
Nombre o Razón Social del Acreedor
102
151
50
C


8

Código País de residencia del Acreedor
152
154
3
C


9

Folio del Documento
155
169
15
C

10
Tipo de Operación
170

171
2
C
Se adjunta descripción de los tipos de operación

11

Fecha de Emisión del Documento
172
179
8
Fecha
dd/mm/aaaa

12

Fecha de Vencimiento del Documento
180
187
8
Fecha
dd/mm/aaaa
13
Norma Eximitoria
188
189
2
C
Se adjunta descripción de los tipos de norma eximitoria

14

Descripción de la Norma Eximitoria
190
289
100
C


15

Monto de Operaciones Exentas
290
304
15
N


16

Monto de Operaciones Afectas (Base Imponible)
305

319
15
N


17

Tasa del Impuesto Aplicada
320
334
15
N
Porcentaje %

18

Monto del Impuesto 
335
349
15
N



LARGO DEL REGISTRO  349



INSTRUCCIONES

I.- Formato de los archivos:

Los archivos digitales del Auxiliar de Registro de Impuesto Timbres y Estampillas, deben ser enviados, a la Subdirección de Informática de la Dirección Nacional del Servicio de Impuestos Internos, en archivos planos, tipo texto o ASCII, a través de discos compactos (CD), cintas magnéticas u otro medio tecnológico que permita el procesamiento electrónico de datos.

Los discos compactos (CD), cintas magnéticas u otro medio tecnológico que se emplee, deberán ser rotulados con el RUT, nombre del banco y período al cual corresponden los archivos.

Los Archivos no deben estar totalizados.

Cada archivo debe estar denominado por el año y el mes en que fueron generados, con cuatro y dos  dígitos respectivamente, además de considerar tres dígitos que identifiquen al Banco o entidad declarante.
Ej.:[AAMMBBB]

II.- Formato de los campos:

Se registrarán los documentos emitidos, con mención en columnas separadas de los campos establecidos en el formato de registro presentado. Estos estarán separados por punto y coma (;), sin considerar espacios en blanco.

Los campos alfanuméricos (caracteres) deben justificarse a la izquierda, en forma continua hasta alcanzar el máximo del registro cuando corresponda. Si el campo no fuese completado con la información, se llenará con espacios en todas las posiciones del campo. 

Los campos numéricos deben justificarse a la derecha, en forma continua hasta alcanzar el largo máximo del registro cuando corresponda. Si el campo no contuviese información o no fuese completado, deberá ser llenado con ceros "0".

Todos los valores de montos deben ser indicados en pesos chilenos, se debe efectuar la conversión de las operaciones en moneda extranjera, de acuerdo al valor del dólar observado publicado por el Banco Central de Chile o el valor de cotización de la moneda respectiva (paridad), correspondiente a la fecha de la operación.

Los campos numéricos deben registrarse sin separador de miles.

Los valores deben registrarse sin decimales, a excepción del campo de “Tasas del Impuesto Aplicada” que debe contener tres decimales, siendo la coma el indicador de decimal.

Los campos alfanumércios no deben contener palabras con acento, y no se debe incluir caracteres especiales, tales como, °, @, etc.

Si el formato definido para algún campo, relativo a expresiones en montos de dinero o cualquier otro, fuera insuficiente para almacenar la información pertinente, no debe ampliarse la longitud del campo, ni informarse un dato que no corresponda al verdadero, sino que deberá comunicarse a la Subdirección de Informática de la Dirección Nacional del Servicio de Impuestos Internos para que reformule los formatos relativos al archivo. 



III.- Descripción de los campos

En el campo "Rut del Deudor", se deberá registrar el Rut del deudor o nombre de quien tiene la calidad de deudor en la operación. Si se tratare de una persona o entidad que no posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "TAX-ID del Deudor", se deberá indicar TAX-ID o número de registro tributario del país que corresponda, si no cuenta con esta información deberá indicar el Rut o identificación que corresponda a la persona que actúa como representante o responsable en Chile. Si se tratare de una persona o entidad que posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "Nombre o Razón Social del Deudor", se deberá registrar el nombre o razón social del deudor.

En el campo “Código País de residencia del Deudor”, se deberá indicar el código del país que corresponda a la identificación presentada por el deudor (persona a nombre de quien se realiza la operación), es decir, el país que otorgó el pasaporte u otro documento de identificación. El código a utilizar deberá ser obtenido de la Tabla de Códigos indicada en el Suplemento Declaraciones Juradas del Servicio de Impuestos Internos. Si se tratare de una persona o entidad que posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "Rut del Acreedor”, se deberá indicar el Rut del Acreedor de la Operación. Si se tratare de una persona o entidad que no posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "TAX-ID del Acreedor", se deberá indicar TAX-ID o número de registro tributario del país que corresponda, si no cuenta con esta información deberá indicar el Rut o identificación que corresponda a la persona que actúa como representante o responsable en Chile. Si se tratare de una persona o entidad que posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "Nombre o Razón Social del Acreedor", se deberá registrar el nombre o razón social del acreedor.

En el campo “Código País de residencia del Acreedor”, se deberá indicar el código del país que corresponda a la identificación presentada por el acreedor, es decir, el país que otorgó el pasaporte u otro documento de identificación. El código a utilizar deberá ser obtenido de la Tabla de Códigos indicada en el Suplemento Declaraciones Juradas del Servicio de Impuestos Internos. Si se tratare de una persona o entidad que posea RUT o cédula de identidad otorgados en Chile, deberá dejar este campo blanco.

En el campo "Folio del documento", se deberá indicar el número de documento u operación que identifique la emisión u suscripción del documento o la fecha en que se efectuó la operación.

En la columna "Tipo de Operación", se deberá indicar el código de acuerdo al tipo de operación.

No se deberán informar aquellas operaciones en que el Notario u Oficial del Registro Civil haya efectuado retención del impuesto.



CÓDIGOS TIPOS DE OPERACIÓN
Código
Descripción
01
Mutuos de dinero. (Art.1 N°3)
02
Pagarés, letras de cambio. (Art.1 N°3)
03
Descuento bancario de letras. (Art.1 N°3)
04
Colocación de bonos, debentures, pagarés y otros valores inscritos en el Registro de Valores en conformidad a la Ley N° 18045. (Art. 1 N°3 y Art. 2 bis)
05
Emisión de bonos y debentures  no acogidos a la Ley N°18045. (Art.1 N°3)
06
Préstamos bancarios otorgados en cuenta especial, con o sin garantía documentaria. (Art 1 N°3)
07
Libranzas, créditos simples o documentarios y otros documentos en general que contengan una operación de crédito de dinero. (Art.1 N°3)
08
Entrega de dinero a interés, excepto cuando el depositario sea un banco. (Art.1 N°3)
09
Diferencia de impuesto originada en base imponible definitiva superior a base imponible provisoria respecto de operaciones de crédito de dinero celebradas en el país. (Art.7)
10
Préstamos u otras operaciones de crédito de dinero, efectuadas con letras o pagarés, por bancos e instituciones financieras registradas en el Banco Central de Chile en el caso de operaciones desde el exterior. (Art.1 N°3)
11
Operaciones de crédito de dinero provenientes del extranjero en las que no se hayan emitido o suscrito documentos. (Art.1 N°3)
12
Operaciones de crédito de dinero provenientes del extranjero en las que se hayan emitido o suscrito documentos. (Art.1 N°3)
13
Diferencia de impuesto originada en base imponible definitiva superior a base imponible provisoria correspondiente a operaciones celebradas con personas del exterior. (Art.7)
14
Prórroga o renovación de  las operaciones de crédito interno gravadas en el N°3 del Artículo 1. (Art.2 N°2)
15
Prórroga o renovación de las operaciones de crédito del exterior gravadas en el N°3 del Artículo 1 . (Art.2 N°2)
16
Capitalización de intereses correspondientes a operaciones de crédito de dinero internas. (Art. 2 N°1)
17
Capitalización de intereses correspondientes a operaciones gravadas celebradas con personas del exterior.  (Art. 2 N°1)
18
Cada una de las operaciones de crédito de dinero que se realicen en virtud de lo pactado en contratos de apertura o líneas de crédito y las otorgadas para el uso de tarjetas de crédito para contribuyentes del Impuesto de Primera Categoría, que no sean contribuyentes del Art. 20 N° 2 de la Ley de la Renta, y para quienes no sean contribuyentes de dicho impuesto siempre que no se trate de tarjetas destinadas al uso particular de personas naturales . (Art.24 N°9).
19
Operaciones de crédito de dinero otorgadas para el uso de tarjetas de crédito, celebradas por contribuyentes del Art.20 N°2 de la Ley de Impuesto a la Renta o tarjetas que estén destinadas exclusivamente al uso particular de personas naturales que no sean contribuyentes del Impuesto de Primera Categoría. (Art. 24 N°9)

SE INFORMARÁN EN FORMA GLOBALIZADA, SIN INDICAR DETALLE DE OPERACIONES

20
Cada una de las operaciones de crédito de dinero celebradas con personas del exterior que se realicen en virtud de lo pactado en contratos de apertura o líneas de crédito. (Art.24 N°9)
21
Actas de protesto de letras de cambio y pagarés a la orden. (Art.4)
22
Entrega de facturas o cuentas en cobranza a instituciones bancarias y financieras. (Art.1 N°3)
23
Cartas de crédito cuando no se emitan o suscriban otros documentos para garantizar su pago, relacionadas con importaciones no afectas con el impuesto  del Art.3. (Art.1 N°3)
24
Documentos gravados emitidos para garantizar cartas de crédito, relacionadas con importaciones no afectas con el impuesto del Art.3.  (Art. 1 N° 3)
25
Pago de importaciones o ingresos de mercaderías a zonas francas, cuando dicho pago sea efectuado  con divisas propias y con una fecha  posterior a la de aceptación del documento de destinación aduanera o de ingreso a zona franca. (Art.3)
26
Pago de importaciones o ingresos de mercaderías a zonas francas, cuando dicho pago sea posterior a fecha de aceptación del documento de destinación aduanera o de ingreso a zona franca  y se realice con divisas adquiridas a entidades bancarias, casas de cambio u otros. (Art.3)


En la columna "Fecha de emisión del documento", se deberá registrar la fecha de emisión que deberá corresponder a la fecha de emisión o suscripción del documento o la fecha en que se efectuó la operación.							

En la columna "Fecha de vencimiento del documento", se deberá registrar la fecha de vencimiento que deberá corresponder a la fecha en que se hará exigible el pago de la obligación.								

En la columna "Norma Eximitoria", los contribuyentes deberán informar las operaciones señaladas en el N°3 del artículo 1 y en los artículos  2, 2 bis y 3, que hayan quedado exentas, cualquiera sea la norma eximitoria, salvo que se hayan aplicado las exenciones dispuestas en los N°s 6 y 11 del artículo 24. No deberán informarse las operaciones indicadas en el N°1 del artículo 1°, ni las operaciones del artículo 4 que estén exentas. Las prórrogas o renovaciones a las que no se les aplique el impuesto en razón de operar el tope o máximo señalado en el Art. 2 inciso 3°, no deberán ser informadas.	

En la columna "Norma Eximitoria", se deberá indicar el código de acuerdo a los siguientes conceptos:								
								
CÓDIGOS NORMA EXIMITORIA
Cód.
Descripción
01
El Fisco (Art.23 N°1 D.L. N° 3.475)
02
Las Municipalidades (Art.23 N°2 D.L. N° 3.475)
03
Las Universidades del Estado y demás Universidades reconocidas por éste y el Consejo de Rectores(Art.23 N°3 D.L. N° 3.475)
04
Las representaciones de naciones extranjeras acreditadas en el país, y las instituciones internacionales a que Chile pertenezca y respecto de las cuales se haya estipulado la exención de todo impuesto, cualquiera sea su naturaleza, o, específicamente, la liberación de los tributos que afecten a los documentos. (Art.23 N°4 D.L. N° 3.475)
05
Sociedad Constructora de Establecimientos Educacionales S.A. (Art.23 N° 5 D.L. N° 3.475)
06
Sociedad Constructora de Establecimientos Hospitalarios S.A. (Art.23 N° 6 D.L. N° 3.475)

07
Cuerpo de Bomberos (Art.23 N° 7 D.L. N° 3.475)
08
Cooperativas, de conformidad con lo establecido en el R.R.A. 20, de 1963. (Art.23 N° 8 D.L. N° 3.475)

09
Instituciones con personalidad jurídica cuyo fin sea el culto(Art.23 N°9 D.L. N° 3.475)

10
Fundación Niño y Patria e Instituto de Viviendas Populares INVICA. (Art.23 N°10 D.L. N° 3.475)
11
Cruz Roja Chilena y la Fundación Nacional del Niño Rural. (Art.23 N°11 D.L. N° 3.475)
12
Consejo Nacional de Protección a la Ancianidad- CONAPRAN, Corporación de Ayuda al menor- CORDAM, Corporación de Ayuda al Niño Limitado - COANIL, y Hogar de Niños Arturo Prat. (Art.23 N°12 D.L. N° 3.475)
13
El Instituto de Normalización Previsional. (Art.23 N°13 D.L. N° 3.475)
14
Documentos que den cuenta o se emitan en relación con préstamos o créditos otorgados del exterior por organismos financieros multilaterales, y los relativos a la emisión de bonos que se coloquen en el exterior emitidos o suscritos por el Fisco o el Banco Central de Chile. (Art.24 N°1 D.L. N° 3.475)
15
Documentos que den cuenta de operaciones, actos o contratos exentos, en conformidad al Decreto Supremo Nº 1.101, del Ministerio de Obras Públicas, de 1960, que fija el texto definitivo del D.F.L. Nº 2, sobre Plan Habitacional; a la Ley Nº16.807, de 1968, que fija el texto definitivo del D.F.L. Nº205, de 1960, sobre Sistemas de Ahorro y Préstamos para la Vivienda; a la Ley Nº 16.528, de 1966, sobre Estímulos a las Exportaciones; y las operaciones, actos y contratos que realicen los Servicios Regionales y Metropolitano de Vivienda y Urbanismo, a que se refiere el Decreto Ley número 1.305, de 1976. (Art.24 N°2 D.L. N° 3.475).
16
Bonos, pagarés, vales de impuesto, letras de cambio y demás actos y contratos mencionados en el artículo 1º Nº 3 de este decreto ley, emitidos o aceptados por el Fisco. (Art.24 N°3 D.L. N° 3.475).
17
Las aceptaciones Bancarias Latinoamericanas ALALC (ABLAS) (Art.24 N°7 D.L. N° 3.475).
18
Los actos y contratos que se ejecuten o celebren en la provincia de la Isla de Pascua por personas domiciliadas en ella respecto de actividades o bienes que digan relación con ese mismo territorio. (Art.24 N°8 D.L. N° 3.475)
19
Contratos de apertura o línea de crédito e instrumentos en que se documenten dichas líneas o contratos de apertura, sin perjuicio de pagarse el impuesto de que trata el Nº 3 del artículo 1º de este decreto ley, respecto de todas y cada una de las operaciones de crédito que se realicen en virtud de lo pactado en la apertura o línea de crédito. (Art.24 N°9 D.L. N° 3.475)
20
Documentos necesarios para efectuar las importaciones de bienes internados al amparo de las franquicias establecidas en el inciso vigésimo tercero del artículo 35 de la Ley Nº 13.039, como asimismo, los documentos necesarios para efectuar las importaciones de CKD y SKD que efectúen las industrias terminales acogidas al régimen de compensación que regula el inciso tercero del artículo 3º de la ley Nº 18.483. (Art.24 N°10 D.L. N° 3.475)
21
Las cartas de crédito para importaciones que se abran con fondos propios del importador. (Art.24 N°12 D.L. N° 3.475)
22
Documentos donde conste el otorgamiento de mutuos por parte de la Corporación de Fomento de la Producción a bancos, a otras instituciones financieras y a empresas de leasing. (Art.24 N°13 D.L. N° 3.475)
23
Los créditos otorgados desde el exterior a bancos o instituciones financieras locales, con el exclusivo objeto de financiar operaciones de importación o internación de mercaderías al país, o bien que tengan por único objeto ser colocados en el exterior.(Art.24 N°15 D.L. N° 3.475)
24
Los documentos necesarios para el otorgamiento de préstamos y demás operaciones de crédito de dinero, por parte de Bancos e Instituciones Financieras desde Chile hacia otros países. (Art.24 N°16 D.L. N° 3.475)
25
Los documentos que se emitan o suscriban con motivo del otorgamiento de préstamos con garantía hipotecaria a personas naturales o préstamos de enlace que se otorguen mientras se perfecciona la operación hipotecaria definitiva, que estén destinados exclusivamente a pagar préstamos, de igual naturaleza, que se hubieren utilizado en la adquisición, construcción o ampliación de una vivienda. Lo anterior, siempre que al momento del otorgamiento de dichos créditos, éstos hubieren devengado la tasa máxima del impuesto de esta ley y que el impuesto se hubiere pagado efectivamente. Igualmente esta exención se aplicará cuando el préstamo que se paga anticipadamente, se hubiere acogido a lo dispuesto en este número o en otra disposición legal que exima total o parcialmente al préstamo del impuesto establecido en este decreto ley. (Art.24 N°17 D.L. N° 3.475)

26
Otros. Especifique en la columna “Descripción Norma Eximitoria”
					
En la columna “Descripción de la Norma Eximitoria”, se deberá señalar la norma eximitoria que se utiliza, que no corresponda a las excepciones descritas en los Artículos N°s. 23 y 24 de la Ley de Impuesto de Timbres y Estampillas.

En la columna "Monto de operaciones exentas", se deberá indicar el monto de las operaciones exentas que corresponda al documento u operación.	

En la columna "Monto de operaciones afectas", se deberá indicar el monto de las operaciones afectas que corresponda al documento u operación.

En la columna "Tasa del Impuesto aplicada", se deberá indicar la tasa del Impuesto de Timbres y Estampillas aplicada.					

En la columna "Monto del impuesto", se deberá indicar el monto que resulte de multiplicar el monto de las operaciones afectas por la tasa del impuesto aplicada.

									
						
 PAGE 1




