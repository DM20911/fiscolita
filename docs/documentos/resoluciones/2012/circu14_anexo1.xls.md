---
url: https://www.sii.cl/documentos/resoluciones/2012/circu14_anexo1.xls
titulo: circu14_anexo1.xls
categoria: otros
---
## Hoja: Formato Registro

|FORMULARIO 18XX||||||
|Declaración Jurada Anual sobre operaciones en instrumentos de deuda de oferta pública acogidos al artículo 104 de la Ley sobre Impuesto a la Renta, ||||||
|efectuadas por corredores de bolsa, agentes de valores u otros intermediarios, por cuenta de terceros.||||||
|AÑO TRIBUTARIO  :  2012||||||
REGISTRO TIPO 0 :   Utilizado si y solo si se envia el archivo por Upload (INTERNET)|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||Desde|Hasta|||
1|Tipo de registro||1|1|1|N|=0 
2|Año Tributario||2|5|4|N|=2012
3|Número Formulario||6|9|4|N|=18XX
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
4|Número de RUT||10|17|8|N|>0
5||Dígito verificador|18|18|1|C|Módulo 11
6||Total de Registros a transmitir|19|25|7|N|>0
|Código certificación||||||
7||Código empresa|26|27|2|C|Autorizada por SII
8||Número de cliente|28|31|4|N|Del software autorizado
9|Checksum declarante||32|41|10|N|>=0
10|Checksum SII||42|51|10|N|= 0
11|Código de presentación||52|52|1|C|I: Internet
12|Tipo de Declaración||53|53|1|C|O:original R: rectificatoria
13|Nº de folio||54|60|7|N|>0
|Fecha de envío||||||
14||Día|61|62|2|N|=0
15||Mes|63|64|2|N|=0
16||Año|65|68|4|N|=0
|Hora de envío||||||
17||Hora|69|70|2|N|=0
18||Minuto|71|72|2|N|=0
19||Segundo|73|76|4|N|=0
20|Número de Versión||77|78|2|N|=01
21|Número de Atención||79|86|8|N|=0
22|Blancos||87|122|36|C|
|LARGO DEL REGISTRO||||122||
|Tipo de registro||||||
1||Determina tipo|1|1|1|N|=1 
2||Determina orden preced.|2|2|1|N|=1
3|Año Tributario||3|6|4|N|=2012
4|Número Formulario||7|10|4|N|=18XX
|Folio||||||
5||    Código de presentación|11|11|1|C|"Código de Presentación igual en los registros 1,2 y 3
F = Formulario, I = Internet ó M = Excepción"
6||    Nº de folio|12|18|7|N|>0
7|Tipo de Declaración||19|19|1|C|O:original R: rectificatoria
|    Rectificatoria|||||| 
|      RUT  anterior||||||
8||Número de RUT|20|27|8|N|>0 : Rectificatoria; =0:Original
9||Dígito verificador|28|28|1|C|"Módulo 11: Si tipo Declaración es ""R""; 0 Si tipo Declaración es ""O"""
|      Folio anterior||||||
10||Cód.de presentación|29|29|1|C|"I, M ó F: Si Tipo Declaración es ""R"" (Rectificatoria); Blanco: Si Tipo Declaración es ""O"" (Original)"
11||Nº folio|30|36|7|N|>0: Si tipo Declaración es “R” (Rectificatoria) ; =0 Si tipo Declaración es “O” (Original)
12|Blancos||37|42|6|C|Igual a Blanco
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
13||Número de RUT|43|50|8|N|>0 Obligatorio
14||Dígito verificador|51|51|1|C|Módulo 11
15|Razón Social o Nombre||52|81|30|C|Obligatorio, diferente de Blanco
16|Tipo Declarante||82|83|2|N|{1, 2, 3}
|Nº de Teléfono||||||
17||Cód Pais|84|85|2|N|=56
18||Cód.  Ärea Ciudad|86|87|2|N|>= 0
19||Teléfono|88|94|7|N|>= 0
|Nº de Fax||||||Obligatorio, diferente de 0
20||Cód Pais|95|96|2|N|=56
21||Cód.  Ärea Ciudad|97|98|2|N|>0
22||Teléfono|99|105|7|N|>0
23|Blancos||106|106|1|C|blanco 
|Código certificación||||||Solo para archivos computacionales Internet
24||Código empresa|107|108|2|C|Autorizada por SII
25||Número de cliente|109|112|4|N|Del software autorizado
|Localización del docto.||||||Los Campos Unidad, Número de Caja y Número de Paquete deben ser iguales a los mismos campos del Registro 2; Archivos Internet y Medios completar con ceros
||Caja|||||
26||     Unidad|113|117|5|N|=0
27||     Número de caja|118|120|3|N|=0
28||Número de paquete|121|125|5|N|=0
29|Blancos||126|122|-3|C|blanco 
|LARGO DEL REGISTRO||||122||
|Tipo de registro||||||
1||Determina tipo|1|1|1|N|=1 
2||Determina orden preced.|2|2|1|N|=2
3|Dirección Postal||3|37|35|C|Obligatorio, diferente de Blanco
4|Comuna||38|52|15|C|Obligatorio, diferente de Blanco
5|Correo Electrónico||53|82|30|C|Obligatorio diferente de Blanc0, formato: _________@__. ___ 
6|Blancos||83|122|40|C|blanco 
|LARGO DEL REGISTRO||||122||
|DATOS DE LOS DECLARADOS||||||
REGISTROS TIPO 2: DATOS DE LOS DECLARADOS|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||Desde|Hasta|||
1|Tipo de registro||1|1|1|N|=2 
2|Número Formulario||2|5|4|N|=18XX
|Folio||||||
3||    Código de presentación|6|6|1|C|"Código de Presentación igual en los registros 1,2 y 3
F = Formulario, I = Internet ó M = Excepción"
4||    Nº de folio|7|13|7|N|>0
5|Tipo de Declaración||14|14|1|C|O:original R: rectificatoria
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
6||Número de RUT|15|22|8|N|>0 Obligatorio
7||Dígito verificador|23|23|1|C|Módulo 11
8|Número de Línea||24|31|8|N|>0
|Rut  Emisor||||||
9||Número de RUT|32|39|8|N|>0 Obligatorio
10||Dígito verificador|40|40|1|C|Módulo 11
|Rut Inversionista||||||
11||Número de RUT|41|48|8|N|>0 Obligatorio
12||Dígito verificador|49|49|1|C|Módulo 11
13|Tipo Contribuyente||50|51|2|N|Obligatorio {1, 2}
14|Nemotécnico SVS||52|76|25|C|Obligatorio
|Fecha Operación||||||01/01/(AT-1) <= Fecha Operación <= 31/12/(AT-1) con AT = Año Declaración Formulario 18XX
15||día|77|78|2|N|dd        = día , 0<día<32 / Obligatorio
16||mes|79|80|2|N|mm      = mes , 0<mes<13 / Obligatorio 
17||año|81|82|2|N|aaaa / Obligatorio > = (AT-1) con AT = Año Declaración Formulario 18XX
18|Tipo Movimiento||83|84|2|N|Obligatorio {1, 2, 3}
19|Moneda o Unidad de Reajuste del instrumento||85|86|2|N|Obligatorio,  Tipo {1: Peso, 2: Dolar, 3: EURO, 4: UF, 5: IVP, 6: Otro }
20|N° Cuenta DCV||87|94|8|N|
|Monto Nominal movimiento (en moneda o unidad de reajuste)||95|109|15|N|Obligatorio >= 0
|Localización del docto.||||||Los Campos Unidad, Número de Caja y Número de Paquete deben ser iguales a los mismos campos del Registro 2; Archivos Internet y Medios completar con ceros
||Caja|||||
25||     Unidad|110|114|5|N|=0
26||     Número de caja|115|117|3|N|=0
27||Número de paquete|118|122|5|N|=0
|LARGO DEL REGISTRO||||122||
REGISTRO TIPO 3: CUADRO RESUMEN DE LA DECLARACIÓN|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||desde|hasta|||
|Tipo de registro||||||
1||    Determina tipo|1|1|1|N|=3 
2||    Determina orden preced.|2|2|1|N|=1
3|Número Formulario||3|6|4|N|=18XX
|Folio||||||
4||    Código de presentación|7|7|1|C|"Código de Presentación igual en los registros 1,2 y 3
F = Formulario, I = Internet ó M = Excepción"
5||    Nº de folio|8|14|7|N|>0
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
6||Número de RUT|15|22|8|N|>0 Obligatorio
7||Dígito verificador|23|23|1|C|módulo 11
8|Cantidad Total de Datos Informados||24|38|15|N|> 0
10|Monto total movimientos||39|53|15|N|>=0
11|Blancos||54|122|69|C|
|TOTAL RESUMEN||||122||


## Hoja: Layout DJ 1874 Bonos 104

||||Declaración Jurada Anual sobre operaciones sobre instrumentos de deuda de oferta pública acogidos al artículo 104 de la Ley sobre Impuesto a la Renta, efectuadas por Corredores de Bolsa, Agentes de Valores u Otros Intermediarios, por cuenta de terceros inversionistas.||||||||
||||||||||||F 1874
|||||||||||Folio|
||Sección A: IDENTIFICACIÓN DEL DECLARANTE (CORREDORES DE BOLSA, AGENTES DE VALORES U OTROS INTERMEDIARIOS)||||||||||
||ROL ÚNICO TRIBUTARIO (C1)||NOMBRE O RAZÓN SOCIAL|||||TIPO DECLARANTE (C2)|||
||DOMICILIO POSTAL|||||||COMUNA|||
||TELÉFONO||FAX||||CORREO ELECTRÓNICO||||
||Sección B: DATOS DE LOS INFORMADOS||||||||||
|N°|RUT Emisor|RUT Inversionista|Tipo contribuyente|Nemotécnico SVS|Fecha Operación|Tipo de Movimiento|Moneda o unidad de reajuste|N° Cuenta DCV|"Monto Nominal Movimiento
(en moneda o unidad de reajuste del instrumento)"||
||C3|C4|C5|C6|C7|C8|C9|C10|C11||
||Sección C: DATOS DE OPERACIONES PROPIAS||||||||||
||CUADRO RESUMEN FINAL DE LA DECLARACIÓN||||||||||
||Cantidad Total de Datos Informados|Monto total movimientos (en moneda o unidad de reajuste del instrumento)|||||||||
||C12|C13|||||||||
DECLARO BAJO JURAMENTO QUE LOS DATOS CONTENIDOS EN EL PRESENTE DOCUMENTO SON LA EXPRESIÓN FIEL DE LA VERDAD, POR LO QUE ASUMO LA RESPONSABILIDAD CORRESPONDIENTE||||||||||||


## Hoja: Hoja1


