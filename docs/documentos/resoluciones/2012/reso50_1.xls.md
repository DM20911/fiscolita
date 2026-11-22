---
url: https://www.sii.cl/documentos/resoluciones/2012/reso50_1.xls
titulo: reso50_1.xls
categoria: otros
---
## Hoja: F1848 LAYOUT

|||Declaración jurada anual sobre transacciones efectuadas por inversionistas extranjeros, sin domicilio ni residencia en Chile, acogidos al régimen simplificado de obtención de RUT y/o liberados de las obligaciones de inicio de actividades, llevar contabilidad y declarar anualmente sus rentas, y sobre cumplimiento de requisitos e inversiones acogidas al artículo 106 de la Ley de la Renta.||||||||||F|1848|
|||||||||||||FOLIO||
||||AÑO TRIBUTARIO  20XX|||||||||||
Sección A : Identificación del agente (declarante)|||||||||||||||
ROL ÚNICO TRIBUTARIO C1|||NOMBRE O RAZÓN SOCIAL||||||||||||
DOMICILIO POSTAL|||||||COMUNA||||||||
CORREO ELECTRÓNICO|||||||FAX||TELÉFONO||||||
Sección B:  Transacciones informadas (datos de los inversionistas extranjeros, transacciones realizadas, inversiones y cumplimiento requisitos art. 106 LIR, gastos, retención y/o pago de impuestos y exenciones aplicadas). |||||||||||||||
Línea   |INVERSIONISTA EXTRANJERO||TRANSACCIONES Y SITUACIÓN DEL INVERSIONISTA EXTRANJERO|||||||CUMPLIMIENTO DE REQUISITOS E INVERSIONES ACOGIDAS AL ART. 106 LIR|||||
|RUT|Modalidad de actuación|Tipo de operación o situación del inversionista |Tipo de instrumento o contrato|Fecha de la operación o fecha cambio situación del inversionista|"Monto de la operación 
en pesos"|Moneda o unidad original de operación|Monto de la operación en moneda o unidad original|"Gastos 
en pesos"|Tipo Inversionista Art. 106 LIR |Fecha de contrato|Inversionista no tiene EP en Chile y no participará en el control de los emisores|Inversiones realizadas por cuenta propia del inversionista y como beneficiario efectivo|INGRESO CAPITALES |
||||||||||||||País origen divisas internadas|RUT banco en que se liquidaron las divisas
1|||||||||||||||
2|||||||||||||||
3|||||||||||||||
4|||||||||||||||
5|||||||||||||||
|Sección B (continuación)||||||||||||||
|RETENCIONES Y/O PAGOS DE IMPUESTOS||||||BENEFICIOS TRIBUTARIOS||||||||
|RUT responsable del entero del impuesto|Base imponible (pesos)|Tasa de impuesto|Crédito impuesto 1° categoría o inciso 4° artículo 108 LIR (pesos)|Impuesto retenido y/o pagado (pesos)|Folio F50|Norma que establece el beneficio tributario|Referencia legal otros beneficios tributarios|Monto exento o beneficiado (pesos)||||||
|CUADRO RESUMEN FINAL DE LA DECLARACIÓN||||||||||||||
|N° Transacciones informadas||Monto total de impuestos retenidos y/o pagados (pesos)||Monto total exento o beneficiado (pesos)||||||||||
|DECLARO BAJO JURAMENTO QUE LOS DATOS CONTENIDOS EN EL PRESENTE DOCUMENTO SON LA EXPRESIÓN FIEL DE LA VERDAD, POR LO QUE ASUMO LA RESPONSABILIDAD CORRESPONDIENTE||||||||||||||


## Hoja: Formato Registro

|FORMULARIO 1848||||||
|Declaración jurada anual sobre transacciones efectuadas por inversionistas extranjeros, sin domicilio ni residencia en Chile, acogidos al régimen simplificado de obtención de RUT y/o liberados de las obligaciones de inicio de actividades, llevar contabilidad y declarar anualmente sus rentas, y sobre cumplimiento de requisitos e inversiones acogidas al artículo 106 de la Ley de la Renta.||||||
|AÑO TRIBUTARIO  :  2012||||||
REGISTRO TIPO 0 :   Utilizado si y solo si se envia el archivo por Upload (INTERNET)|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||Desde|Hasta|||
1|Tipo de registro||1|1|1|N|=0 
2|Año Tributario||2|5|4|N|=2012
3|Número Formulario||6|9|4|N|=1848
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
|Número de RUT||10|17|8|N|>0
4||Dígito verificador|18|18|1|C|Módulo 11
5||Total de Registros a transmitir|19|25|7|N|>0
6|Total de Registros a transmitir||26|32|7|N|>0
|Código certificación||||||
7||Código empresa|33|34|2|C|Autorizada por SII
8||Número de cliente|35|38|4|N|Del software autorizado
9|Checksum declarante||39|48|10|N|>=0
10|Checksum SII||49|58|10|N|= 0
11|Código de presentación||59|59|1|C|I: Internet
12|Tipo de Declaración||60|60|1|C|O:original R: rectificatoria
13|Nº de folio||61|67|7|N|>0
|Fecha de envío||||||
14||Día|68|69|2|N|=0
15||Mes|70|71|2|N|=0
16||Año|72|75|4|N|=0
|Hora de envío||||||
17||Hora|76|77|2|N|=0
18||Minuto|78|79|2|N|=0
19||Segundo|80|83|4|N|=0
20|Número de Versión||84|85|2|N|=01
21|Número de Atención||86|93|8|N|=0
22|Blancos||94|244|151|C|
|LARGO DEL REGISTRO||||244||
|Tipo de registro||||||
1||Determina tipo|1|1|1|N|=1 
2||Determina orden preced.|2|2|1|N|=1
3|Año Tributario||3|6|4|N|=2012
4|Número Formulario||7|10|4|N|=1848
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
16|Dirección Postal||82|116|35|C|Obligatorio, diferente de Blanco
17|Comuna||117|131|15|C|Obligatorio, diferente de Blanco
18|Correo Electrónico||132|161|30|C|Obligatorio diferente de Blanc0, formato: _________@__. ___ 
|Nº de Fax ||||||
19||Cód Pais|162|163|2|N|=56
20||Cód.  Ärea Ciudad|164|165|2|N|>= 0
21||Teléfono|166|172|7|N|>= 0
|Nº de Teléfono||||||Obligatorio, diferente de 0
22||Cód Pais|173|174|2|N|=56
23||Cód.  Ärea Ciudad|175|176|2|N|>0
24||Teléfono|177|183|7|N|>0
25|Blancos||184|184|1|C|blanco 
|Código certificación||||||Solo para archivos computacionales Internet
26||Código empresa|185|186|2|C|Autorizada por SII
27||Número de cliente|187|190|4|N|Del software autorizado
|Localización del docto.||||||Los Campos Unidad, Número de Caja y Número de Paquete deben ser iguales a los mismos campos del Registro 2; Archivos Internet y Medios completar con ceros
||Caja|||||
28||     Unidad|191|195|5|N|=0
29||     Número de caja|196|198|3|N|=0
30||Número de paquete|199|203|5|N|=0
31|Blancos||204|244|41|C|blanco 
|LARGO DEL REGISTRO||||244||
|DATOS DE LOS DECLARADOS||||||
REGISTROS TIPO 2: DATOS DE LOS DECLARADOS|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||Desde|Hasta|||
1|Tipo de registro||1|1|1|N|=2 
2|Número Formulario||2|5|4|N|=1848
|Folio||||||
3||    Código de presentación|6|6|1|C|"Código de Presentación igual en los registros 1,2 y 3
F = Formulario, I = Internet ó M = Excepción"
4||    Nº de folio|7|13|7|N|>0
5|Tipo de Declaración||14|14|1|C|O:original R: rectificatoria
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
6||Número de RUT|15|22|8|N|>0 Obligatorio
7||Dígito verificador|23|23|1|C|Módulo 11
8|Número de Línea||24|31|8|N|>=0
|Inversionista Extranjero||||||
||Rut |||||
9||Número de RUT|32|39|8|N|Opcional, de existir debe ser > 0
10||Dígito verificador|40|40|1|C|Módulo 11
11||Modalidad de actuación|41|41|1|N|1 o 2 o Vacio o Blanco
|Transacciónes y situación del inversionista extranjero||||||
12||Tipo de Operación o situación del inversionista|42|43|2|N| Tipo  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} / Opcional
13||Tipo de Instrumento o Contrato|44|45|2|N| Tipo  {1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14} / Opcional
||Fecha de la Operación o fecha cambio situación del inversionista|||||
14||día|46|47|2|N|dd        = día , 0<día<32 / Opcional
15||mes|48|49|2|N|mm      = mes , 0<mes<13 / Opcional
16||año|50|53|4|N|aaaa > = 2011 / Opcional
17||Monto de la Operación (en pesos)|54|68|15|N|Valor sin decimales / Opcional
18||Moneda o unidad original de operación|69|71|3|N|"Tabla ""Códigos de monedas asociados al formulario 1862"" para el A.T. 20XX"
19||Monto de la Operación en moneda o unidad original|72|86|15|N|Valor con dos decimales / Opcional
20||Gastos en pesos|87|101|15|N|Valor sin decimales / Opcional
|Cumplimiento de requisitos e inversiones acogidas al art. 106 LIR||||||
21||Tipo Inversionista Art. 106 LIR|102|103|2|C| Tipo  {a, b, c, d, e, f1, f2, f3, f4} / Opcional
||Fecha de contrato|||||
22||día|104|105|2|N|dd        = día , 0<día<32 / Opcional
23||mes|106|107|2|N|mm      = mes , 0<mes<13 / Opcional
24||año|108|111|4|N|aaaa > = 2011 / Opcional
25||Inversionista no tiene EP en Chile y no participará en el control de los emisores|112|113|2|C| Tipo  {SI, NO} / Opcional
26||Inversiones realizadas por cuenta propia del inversionista y como beneficiario efectivo|114|115|2|C| Tipo  {SI, NO} / Opcional
27||Inversionista dejó de cumplir requisitos Art. 106 LIR|116|117|2|C| Tipo  {SI, NO} / Opcional
|    Ingreso de Capitales||||||
28||País origen divisas internadas|118|120|3|N|"Tabla Código de Países asociados al Formulario 1862"" para el A.T. 20XX "
||RUT banco en que se liquidaron las divisas|||||Rut debe cumplir Modulo 11
29||Número de RUT|121|128|8|N|Opcional, de existir debe ser > 0
30||Dígito verificador|129|129|1|C|Módulo 11
|Retenciones y/o Pagos de Impuestos||||||
||RUT Responsable del Entero del Impuesto|||||Rut debe cumplir Modulo 11
31||Número de RUT|130|137|8|N|Opcional, de existir debe ser > 0
32||Dígito verificador|138|138|1|C|Módulo 11
33||Base Imponible (pesos)|139|153|15|N|Valor sin decimales / Opcional, de existir debe ser > 0
34||Tasa de Impuesto|154|155|2|N|Valor expresado en porcentaje en dos dígitos y un decimal / Opcional, de existir debe ser > 0
35||Crédito Impuesto 1° Categoría o inciso 4° artículo 108 LIR (pesos)|156|170|15|N|Valor sin decimales / Opcional, de existir debe ser > 0
36||Impuesto Retenido y/o pagado (en pesos)|171|185|15|N|Valor sin decimales / Opcional, de existir debe ser > = 0
37||Folio F50|186|195|10|C|Opcional
|Beneficios Tributarios||||||
38||Norma que establece el beneficio tributario|195|196|2|N| Tipo  {1, 2, 3, 4, 5, 6, 10} / Opcional
39||Referencia legal otros beneficios tributarios|197|206|10|C|
40||Monto exento o beneficiado (pesos)|207|221|15|N|
41|Blancos||222|222|1|C|blanco 
42|Número de Línea||223|230|8|N|>=0
|Localización del docto.||||||Los Campos Unidad, Número de Caja y Número de Paquete deben ser iguales a los mismos campos del Registro 2; Archivos Internet y Medios completar con ceros
||Caja|||||
29||     Unidad|231|235|5|N|=0
30||     Número de caja|236|238|3|N|=0
31||Número de paquete|239|243|5|N|=0
|LARGO DEL REGISTRO||||244||
REGISTRO TIPO 3: CUADRO RESUMEN DE LA DECLARACIÓN|||||||
Nº|CAMPOS||POSICION||LARGO|CARACTER|VALIDACIONES DE FORMATO
|||desde|hasta|||
|Tipo de registro||||||
1||    Determina tipo|1|1|1|N|=3 
2||    Determina orden preced.|2|2|1|N|=1
3|Número Formulario||3|6|4|N|=1848
|Folio||||||
4||    Código de presentación|7|7|1|C|"Código de Presentación igual en los registros 1,2 y 3
F = Formulario, I = Internet ó M = Excepción"
5||    Nº de folio|8|14|7|N|>0
|Rut Declarante||||||"Rut Declarante debe cumplir Modulo 11
y Rut Declarante Registro Tipo i = Rut Declarante Registro Tipo j  { i, j = 0, 1, 2, 3}"
6||Número de RUT|15|22|8|N|>0 Obligatorio
7||Dígito verificador|23|23|1|C|módulo 11
8|N° de Transacciones Informadas||24|31|8|N|>= 0 
10|Monto Total de Impuestos retenidos y/o pagados (pesos)||32|46|15|N|>= 0
11|Monto total exento o beneficiado (pesos)||47|61|15|N|>= 0
12|Blancos||61|243|183|C|
|TOTAL RESUMEN||||244||

