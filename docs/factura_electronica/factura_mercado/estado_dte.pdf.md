---
url: https://www.sii.cl/factura_electronica/factura_mercado/estado_dte.pdf
titulo: Manual de Desarrollador Externo
categoria: factura_electronica
---
Manual de Desarrollador Externo
Consulta de Estado DTE
OI2004_CEDTE_MDE_1.10

Oficina Internet
Subdirección Informática
Servicio Impuestos Internos
Fecha:22/12/2010

INDICE
CONTROL DE VERSIONES.......................................................................................................................... 3
INTRODUCCIÓN............................................................................................................................................ 4
CAPITULO 1 .................................................................................................................................................. 6
OBJETIVOS Y CARACTERISTICAS .......................................................................................................... 6
1. OBJETIVOS DE LA APLICACIÓN .................................................................................................................... 6
2. CARACTERÍSTICA DE LA APLICACIÓN ........................................................................................................... 6
CAPITULO 2 .................................................................................................................................................. 7
WSDL DE QUERYESTDTE ............................................................................................................................ 7
2.1 GRAMÁTICA DEL WSDL ........................................................................................................................... 7
2.1.1
WSDL DE QUERYESTDTE.JWS ........................................................................................................ 7
2.1.2
DETALLE PARÁMETROS DEL WSDL ................................................................................................ 9
CAPITULO 3 ................................................................................................................................................ 10
DETALLE PARÁMETROS DEL SERVICIO .............................................................................................. 10
3.1 PARÁMETROS DE ENTRADA .................................................................................................................. 10
3.1.1 EJEMPLO REAL PARÁMETROS DE ENTRADA FORMATO WSDL .............................................................. 10
3.2 PARÁMETROS DE SALIDA ...................................................................................................................... 12
3.3 VALORES DE SALIDA ............................................................................................................................. 12
3.4 EJEMPLOS DE SALIDA .......................................................................................................................... 13
3.4.1 EJEMPLO PARÁMETROS DE SALIDA WSDL CODIFICADO...................................................................... 13
FIGURA 3-5................................................................................................................................................. 13
3.4.1.1 EJEMPLO PARÁMETROS DE SALIDA DECODIFICADO .......................................................................... 13
FIGURA 3-6................................................................................................................................................. 13
3.5 VALORES DE SALIDA POR ERROR ...................................................................................................... 14
3.5.1 Errores de Consulta: ................................................................................................................... 14
3.5.2 Errores por Autenticación: .......................................................................................................... 16
3.5.3 OTROS ERRORES:................................................................................................................... 16
TABLA 3-11 .................................................................................................................................................. 16
3.5.1 EJEMPLO DE SALIDA ERROR WSDL CODIFICADO (ERR_CODE 1) ................................................. 17
FIGURA 3-12............................................................................................................................................... 17
3.5.1.1 EJEMPLO DE SALIDA ERROR WSDL DECODIFICADO (ERR_CODE 1: DOCUMENTO RECIBIDO POR EL
SII PERO DATOS NO COINCIDEN CON LOS REGISTRADOS) ............................................................................ 17
FIGURA 3-13............................................................................................................................................... 17
CAPITULO 4 ................................................................................................................................................ 18
EJEMPLOS DE SALIDA FORMATO XML ............................................................................................... 18
4.1 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO
DOK (DTE RECIBIDO) ........................... 18
4.2 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO DNK (DOCUMENTOS RECIBIDOS, DATOS NO
COINCIDEN) ............................................................................................................................................... 18
4.3 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO FAU (DTE NO RECIBIDO) ........................... 18
4.4 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO FNA (DTE NO RECIBIDO ) ....................... 19
4.5 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO FAN (DOCUMENTO ANULADO ) ................ 19
4.6 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO EMP(EMPRESA NO AUTORIZADA ... ) ........ 19
4.7 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO TMD (EXISTE NOTA DE DEBITO ... ) ........ 20
4.8 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO TMC(EXISTE NOTA DE CRÉDITO ... ) ........ 20
4.9 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO MMD(EXISTE NOTA DE DEBITO ... ) .......... 20
4.10 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO NNC(EXISTE NOTA DE CRÉDITO ... ) ...... 21
4.11 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO AND(EXISTE NOTA DE DEBITO... ).......... 21

1

4.12 EJEMPLO PARÁMETROS DE SALIDA ERR_CODE, ESTADO ANC (EXISTE NOTA DE CRÉDITO... ) ..... 21
4.13 EJEMPLO PARÁMETROS DE SALIDA TOKEN ESTADO 002 (ERROR: TOKEN INACTIVO) ................... 22
4.14 EJEMPLO PARÁMETROS DE SALIDA TOKEN ESTADO 003 (ERROR: TOKEN NO EXISTE) ................... 22
4.15 EJEMPLO PARÁMETROS DE SALIDA TOKEN ESTADO 003 (ERROR: TOKEN NO EXISTE) ................... 22
4.16 EJEMPLO PARÁMETROS DE SALIDA OTROS ERRORES –1 (ERROR: RETORNO CAMPO ESTADO,
NO EXISTE) ............................................................................................................................................. 22
4.17 EJEMPLO PARÁMETROS DE SALIDA OTROS ERRORES –2 (ERROR RETORNO) ............................... 22
4.18 EJEMPLO PARÁMETROS DE SALIDA OTROS ERRORES –3 (ERROR RETORNO) ............................... 23
CAPITULO 5 ................................................................................................................................................ 24
GUIA PARA REALIZAR PRUEBAS .......................................................................................................... 24
REFERENCIAS ........................................................................................................................................ 25

2

CONTROL DE VERSIONES
CONTROL DE VERSIONES
Versión

Fecha

1.0
1.1
1.2

29/01/2003
17/03/2003
28/05/2003

1.3

11/08/2003

1.4

08/03/2004

Cambio

Se agrego Log QuryEstDte_yyyymm.log
- Se modifico lista de Estados de salida de la
aplicación.
- Se modificaron Ejemplos en XML
Se Agregaron Otros Estados de Errores y sus
respectivas salidas en XML
Se modifico Url en Capitulo 5 (Guía para Pruebas, le
faltaba la “s” al http)
Donde decía:
http://maullin.sii.cl/DTEWS/QueryEstDte.jws?WSDL
Se cambio por:
https://maullin.sii.cl/DTEWS/QueryEstDte.jws?WSDL

1.5

08/04/2004

1.6
1.7

07/05/2004
14/06/2004

1.8

08/11/2004

1.9
1.10

12/11/2004
22/12/2010

Se modifico texto de introducción (como acceder a los
WS del SII)
Se modifico texto de los mensajes de salida : 3.5.3
Se agrego al XML de salida un número de atención
(<NUM_ATENCIÓN>), ver punto 3.2
Se agrego estado “001” (Cookie Inactivo), ver punto :
3.5.2
Se modifico largo estado Glosa, ver punto 3.2
Se cambia estado: NNC por MMC

3

INTRODUCCIÓN
Consulta Estado DTE, como parte del proyecto Documentos Tributarios Electrónicos
(DTE), permite consultar el estado de un DTE.
Existen dos maneras de realizar la consulta de estado de un DTE:
9 Consulta Mediante Web Service (WS)
9 Consulta Mediante página Web
En este manual solo abordará el tema relacionado con la consulta mediante Web
Services.
Para acceder a la consulta mediante página web, se debe ingresar a la página principal
del SII (http://www.sii.cl), donde encontrará el link : Factura Electrónica
Por lo tanto, este documento está dirigido a quienes tengan la misión de utilizar y probar
el Web Services de consulta estado DTE (QueryEstDte.jws).
Para acceder a los servicios que ofrece el SII, se debe utilizar WSDL(Web Services
Definition Language).
WSDL es un lenguaje descriptor, basado en XML, que permite conocer en forma
abstracta, la gramática de los componentes de un Web Service (ubicación, formato,
tipos de datos, servicios, funciones, parámetros de entrada, salida, etc).
Para poder acceder a un WSDL, se debe conocer su ubicación, la ubicación del WSDL
que se detalla en este documento apunta al ambiente de certificación del SII, sin
embargo este ambiente es una copia fiel del ambiente de producción.
La ubicación del WSDL de QueryEstDte.jws es:
https://maullin.sii.cl/DTEWS/QueryEstDte.jws?WSDL

4

Una vez que el cliente conoce el WSDL del WS, puede construir un Request en formato
SOAP (Simple Object Access Protocolo), para luego enviarlo hacia el proveedor de
servicio, previa Autenticación.
Respecto a la Autenticación, para poder realizar consultas hacia cualquier Web Service
entregado por el SII, los clientes deben estar previamente autenticados a través de la
AUTENTICACIÓN AUTOMATICA.
Para la implementación de la Autenticación Automática, es necesario ver Manual de
Desarrollador – OI2003_AUTAUTOM_MDE_1.2
Requisitos de uso.
Para poder utilizar este manual, es necesario tener previo conocimiento de XML, Web
Services y Certificado Digital.
Recomendaciones: Se recomienda el uso de la herramienta XMLSPY5 de la Altova
GmbH http://www.altova.com

5

CAPITULO 1
OBJETIVOS Y CARACTERISTICAS

1. Objetivos de la aplicación
El objetivo de este servicio es informar el Estado de un DTE.
2. Característica de la aplicación
9 El servicio QueryEstDte.jws, es de tipo “Consulta” -”Respuesta
9 Es una aplicación B2B.
9 Esta aplicación puede ser utilizada por aquellos usuarios habilitados para su uso.

6

CAPITULO 2
WSDL de QueryEstDte
2.1 Gramática del WSDL
En el siguiente ejemplo se detallan los parámetros utilizados por el WSDL de
QueryEsDte.jws.
2.1.1 WSDL de QueryEstDte.jws
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions targetNamespace="https://maullin.sii.cl/DTEWS/QueryEstDte.jws" xmlns="http://schemas.xmlsoap.org/wsdl/"
xmlns:apachesoap="http://xml.apache.org/xml-soap" xmlns:impl="https://maullin.sii.cl/DTEWS/QueryEstDte.jws"
xmlns:intf="https://maullin.sii.cl/DTEWS/QueryEstDte.jws" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<wsdl:types/>
<wsdl:message name="getEstDteRequest">
<wsdl:part name="RutConsultante" type="xsd:string"/>
<wsdl:part name="DvConsultante" type="xsd:string"/>
<wsdl:part name="RutCompania" type="xsd:string"/>
<wsdl:part name="DvCompania" type="xsd:string"/>
<wsdl:part name="RutReceptor" type="xsd:string"/>
<wsdl:part name="DvReceptor" type="xsd:string"/>
<wsdl:part name="TipoDte" type="xsd:string"/>
<wsdl:part name="FolioDte" type="xsd:string"/>
<wsdl:part name="FechaEmisionDte" type="xsd:string"/>
<wsdl:part name="MontoDte" type="xsd:string"/>
<wsdl:part name="Token" type="xsd:string"/>
</wsdl:message>
<wsdl:message name="getEstDteResponse">
<wsdl:part name="getEstDteReturn" type="xsd:string"/>
</wsdl:message>
<wsdl:portType name="QueryEstDte">
<wsdl:operation name="getEstDte" parameterOrder="RutConsultante DvConsultante RutCompania DvCompania
RutReceptor DvReceptor TipoDte FolioDte FechaEmisionDte MontoDte Token">
<wsdl:input message="impl:getEstDteRequest" name="getEstDteRequest"/>
<wsdl:output message="impl:getEstDteResponse" name="getEstDteResponse"/>
</wsdl:operation>
</wsdl:portType>apBinding" type="impl:QueryEstDte">
<wsdlsoap:binding style="rpc" transport="http://s
<wsdl:binding name="QueryEstDteSo chemas.xmlsoap.org/soap/http"/>
<wsdl:operation name="getEstDte">
<wsdlsoap:operation soapAction=""/>
<wsdl:input name="getEstDteRequest">
<wsdlsoap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstDte.jws" use="encoded"/>
</wsdl:input>
<wsdl:output name="getEstDteResponse">
<wsdlsoap:body encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstDte.jws" use="encoded"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:service name="QueryEstDteService">
<wsdl:port binding="impl:QueryEstDteSoapBinding" name="QueryEstDte">
<wsdlsoap:address location="https://maullin.sii.cl/DTEWS/QueryEstDte.jws"/>
</wsdl:port>
</wsdl:service>
</wsdl:definitions>

Figura 2-1

7

8

2.1.2 Detalle Parámetros del WSDL
De acuerdo a lo destacado en el recuadro del Figura 2-1, QueryEstDte entrega sólo
un metodo “getEstDte”, el cual requiere los siguientes parámetros de entrada:
9
9
9
9
9
9
9
9
9
9
9

RutConsultante
DvConsultante
RutCompania
DvCompania
RutReceptor
DvReceptor
TipoDte
FolioDte
FechaEmisionDte
MontoDte
Token.

9

CAPITULO 3
DETALLE PARÁMETROS DEL SERVICIO
3.1 Parámetros de Entrada
Los parámetros de entrada requeridos por el servicio, se detallan en el siguiente
ejemplo:
3.1.1 Ejemplo Real Parámetros de Entrada Formato WSDL
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SOAP-ENV:Body>
<m:getEstDte xmlns:m="http://maullin.sii.cl/DTEWS/QueryEstDte.jws">
<RutConsultante xsi:type="xsd:string">String</RutConsultante>
<DvConsultante xsi:type="xsd:string">String</DvConsultante>
<RutCompania xsi:type="xsd:string">String</RutCompania>
<DvCompania xsi:type="xsd:string">String</DvCompania>
<RutReceptor xsi:type="xsd:string">String</RutReceptor>
<DvReceptor xsi:type="xsd:string">String</DvReceptor>
<TipoDte xsi:type="xsd:string">String</TipoDte>
<FolioDte xsi:type="xsd:string">String</FolioDte>
<FechaEmisionDte xsi:type="xsd:string">String</FechaEmisionDte>
<MontoDte xsi:type="xsd:string">String</MontoDte>
<Token xsi:type="xsd:string">String</Token>
</m:getEstDte>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Figura 3-1

Donde:
Campo

Tipo

RutConsultante
DvConsultante
RutCompania
DvCompania
Rutreceptor
DvReceptor
TipoDte
FolioDte
FechaEmisionDte

String numérico
String Alfanumérico
String numérico
String Alfanumérico
String numérico
String Alfanumérico
String numérico
String numérico
String Date

Largo Detalle
1-8
1-1
1-8
1-1
1-8
1-1
1-3
1-10
1-10

MontoDte
Token

String numérico
String Alfanumérico

1-15
1-40

Rut Consultante
DV del Rut del Consultante.
Rut del Emisor.
Dv del Emisor.
Rut del Receptor.
Dv del receptor.
Tipo del DTE.
Folio del DTE.
Fecha de Emisión del DTE, en
formato DDMMAAAA.
Monto Total del DTE.
Es un Token es un identificador único
el cual es almacenado y enviado al
cliente en el Header del Response
de la Autenticación Automática con
Certificado Digital (CD), y permite la
búsqueda de toda la información
relacionada a una sesión del cliente.

Obligatorios
S
S
S
S
S
S
S
S
S
S
S

Tabla 3-2

10

11

3.2 Parámetros de Salida
La salida del Servicio corresponden a un “string” XML codificado, por lo tanto necesario
que el programa cliente sea capaz de decodificar el “string” y llevarlo a formato original,
los campos de retorno son: ESTADO y GLOSA, ERR_CODE, GLOSA_ERR, NUM_ATENCIÓN.
Donde:
Campo

Tipo

ESTADO

String

GLOSA
ERR_CODE
GLOSA_ERR
NUM_ATENCION

String
String
String
String

Largo
1-3
1-238
1-3
1-238
1-40

Detalle
Código Estado
Detalle Código
Código Error
Glosa Error
Número de Atención,
Identificador de la
consulta.

Obligatorios
S
S
S
S
S

Tabla 3-3

3.3 Valores de Salida
El resultado de la consulta puede arrojar uno de los siguientes valores:
Estado

Tipo

Largo

Glosa

DOK

String

1-3

DNK

String

1-3

FAU
FNA
FAN
EMP

String
String
String
String

1-3
1-3
1-3
1-3

TMD

String

1-3

TMC

String

1-3

MMD

String

1-3

MMC

String

1-3

AND
ANC

String
String

1-3
1-3

Documento Recibido por el SII. Datos
Coinciden con los Registrados.
Documento Recibido por el SII pero Datos NO
Coinciden con los registrados.
Documento No Recibido por el SII.
Documento No Autorizado.
Documento Anulado.
Empresa no autorizada a Emitir Documentos
Tributarios Electrónicos
Existe Nota de Debito que Modifica Texto
Documento.
Existe Nota de Crédito que Modifica Textos
Documento.
Existe Nota de Debito que Modifica Montos
Documento.
Existe Nota de Crédito que Modifica Montos
Documento.
Existe Nota de Debito que Anula Documento
Existe Nota de Crédito que Anula Documento

Tabla 3-4

12

3.4 Ejemplos de Salida
A continuación se mostrarán algunos ejemplos de salida en ambos formatos
“Codificado” y “Decodificado”.
3.4.1 Ejemplo Parámetros de Salida WSDL Codificado
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<ns1:getEstDteResponse soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:ns1="https://maullin.sii.cl/DTEWS/QueryEstDte.jws">
<getEstDteReturn xsi:type="xsd:string">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;SII:RESPUESTA
xmlns:SII=&quot;http://www.sii.cl/XMLSchema&quot;&gt;&lt;SII:RESP_HDR&gt;&lt;ESTADO&gt;DNK&lt;/ESTADO&gt;&lt;GL
OSA&gt;DTE Recibido&lt;/GLOSA&gt;&lt;ERR_CODE&gt;1&lt;/ERR_CODE&gt;&lt;GLOSA_ERR&gt;Documento Recibido
por el SII pero Datos NO Coinciden con los registrados&lt;/GLOSA_ERR&gt; &lt;NUM_ATENCION&gt;532 ( 2004/06/14
16:44:20)&lt;/NUM_ATENCION&gt;&lt;/SII:RESP_HDR&gt;&lt;/SII:RESPUESTA&gt;</getEstDteReturn>
</ns1:getEstDteResponse>
</soapenv:Body>
</soapenv:Envelope>

Figura 3-5

3.4.1.1 Ejemplo Parámetros de Salida Decodificado

<?xml version="1.0" encoding="UTF-8" ?>
- <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
- <soapenv:Body>
- <ns1:getEstDteResponse
soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:ns1="https://maullin.sii.cl/DTEWS/QueryEstDte.jws">
<getEstDteReturn xsi:type="xsd:string"><?xml version="1.0" encoding="UTF8"?> <SII:RESPUESTA
xmlns:SII="http://www.sii.cl/XMLSchema"><SII:RESP_HDR><ESTADO>DNK</ESTAD
O><GLOSA>DTE Recibido</GLOSA><ERR_CODE>1</ERR_CODE><GLOSA_ERR>Documento
Recibido por el SII pero Datos NO Coinciden con los
registrados</GLOSA_ERR> <NUM_ATENCION>532 ( 2004/06/14
16:44:20)</NUM_ATENCION></SII:RESP_HDR></SII:RESPUESTA></getEstDteReturn
>
</ns1:getEstDteResponse>
</soapenv:Body>
</soapenv:Envelope>

Figura 3-6

13

3.5 Valores de Salida por ERROR
El resultado de la consulta puede arrojar uno de los siguientes Estados de Error:

3.5.1 Errores de Consulta:
9
9
9
9

SRV_CODE
SQL_CODE
ERR_CODE
NUM_ATENCION

Donde :
SRV_CODE
0
1
2

Tipo
String numérico
String numérico
String numérico

Largo
1-1
1-1
1-1

Glosa
Todo Ok
Error en Entrada
Error SQL

Tabla 3-7

SQL_CODE
0
OTRO

Tipo
String numérico
String numérico

Largo Glosa
Schema Validado
1-2
Código de Oracle
1-2
Tabla 3-8

ERR_CODE

Tipo

Largo Glosa

0

String numérico

1-1

1

String numérico

1-1

3
4
5
6

String numérico
String numérico
String numérico
String numérico

1-1
1-1
1-1
1-1

10

String numérico

1-2

11

String numérico

1-2

12

String numérico

1-2

13

String numérico

1-2

14
15
Otro

String numérico
String numérico

1-2
1-2

Documento Recibido por el SII. Datos Coinciden
con los Registrados.
Documento Recibido por el SII pero Datos NO
Coinciden con los registrados.
Documento No Recibido por el SII.
Documento No Autorizado.
Documento Anulado.
Empresa no autorizada a Emitir Documentos
Tributarios Electrónicos
Existe Nota de Debito que Modifica Texto
Documento.
Existe Nota de Crédito que Modifica Textos
Documento.
Existe Nota de Debito que Modifica Montos
Documento.
Existe Nota de Crédito que Modifica Montos
Documento.
Existe Nota de Debito que Anula Documento
Existe Nota de Crédito que Anula Documento
Error Interno.

Tabla 3-9

14

15

3.5.2 Errores por Autenticación:

TOKEN
001
002
003

Tipo
String
String
String

Largo
1-3
1-3
1-3

Glosa
Cookie Inactivo (o token no existe)
Token Inactivo
Token No Existe

Tabla 3-10

3.5.3 Otros Errores:
Estado
-1
-2
-3
-4
Otros

Tipo
String
String
String
String
String

Largo

Glosa

1-1
1-1
1-1
1-1
1-1

ERROR: RETORNO CAMPO ESTADO
ERROR RETORNO
ERROR RETORNO
ERROR RETORNO.

Tabla 3-11

16

3.5.1 Ejemplo de Salida ERROR WSDL Codificado (ERR_CODE 1)

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<ns1:getEstDteResponse soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:ns1="https://maullin.sii.cl/DTEWS/QueryEstDte.jws">
<getEstDteReturn xsi:type="xsd:string">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;SII:RESPUESTA
xmlns:SII=&quot;http://www.sii.cl/XMLSchema&quot;&gt;&lt;SII:RESP_HDR&gt;&lt;ESTADO&gt;DNK&lt;/ESTADO&gt;&lt;GL
OSA&gt;DTE Recibido&lt;/GLOSA&gt;&lt;ERR_CODE&gt;1&lt;/ERR_CODE&gt;&lt;GLOSA_ERR&gt;Documento Recibido
por el SII pero Datos NO Coinciden con los registrados&lt;/GLOSA_ERR&gt; &lt;NUM_ATENCION&gt;532 ( 2004/06/14
16:44:20)&lt;/NUM_ATENCION&gt;&lt;/SII:RESP_HDR&gt;&lt;/SII:RESPUESTA&gt;</getEstDteReturn>
</ns1:getEstDteResponse>
</soapenv:Body>
</soapenv:Envelope>

Figura 3-12

3.5.1.1 Ejemplo de Salida ERROR WSDL Decodificado (ERR_CODE 1: Documento
Recibido por el SII pero Datos NO Coinciden con los registrados)

<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>DNK</ESTADO>
<GLOSA>DTE Recibido</GLOSA>
<ERR_CODE>1</ERR_CODE>
<GLOSA_ERR>Documento Recibido por el SII pero Datos NO Coinciden con
los registrados</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

Figura 3-13

17

CAPITULO 4
EJEMPLOS DE SALIDA FORMATO XML

En este capítulo, se muestran los ejemplos de los posibles Estados de Salida de la
aplicación.
4.1 Ejemplo Parámetros de Salida ERR_CODE, Estado

DOK (DTE Recibido)

<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>DOK</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>0</ERR_CODE>
<GLOSA_ERR>Documento Recibido por el SII. Datos Coinciden con
los Registrados</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.2 Ejemplo Parámetros de Salida ERR_CODE, Estado DNK (Documentos Recibidos,
datos no Coinciden)
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>DNK</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>1</ERR_CODE>
<GLOSA_ERR>Documento Recibido por el SII pero Datos NO
Coinciden con los registrados</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.3 Ejemplo Parámetros de Salida ERR_CODE, Estado FAU (DTE no Recibido)
- <SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>FAU</ESTADO>
<GLOSA_ESTADO>DTE No Recibido</GLOSA_ESTADO>
<ERR_CODE>3</ERR_CODE>
<GLOSA_ERR>Documento No Recibido por el SII</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

18

4.4 Ejemplo Parámetros de Salida ERR_CODE, Estado FNA (DTE no Recibido )
- <SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>FNA</ESTADO>
<GLOSA_ESTADO>DTE No Recibido</GLOSA_ESTADO>
<ERR_CODE>4</ERR_CODE>
<GLOSA_ERR>Documento No Autorizado</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.5 Ejemplo Parámetros de Salida ERR_CODE, Estado FAN (Documento Anulado )
- <SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>FAN</ESTADO>
<GLOSA_ESTADO>DTE No Recibido</GLOSA_ESTADO>
<ERR_CODE>5</ERR_CODE>
<GLOSA_ERR>Documento Anulado</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.6 Ejemplo Parámetros de Salida ERR_CODE, Estado EMP(Empresa No autorizada
... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>EMP</ESTADO>
<GLOSA_ESTADO>DTE No Recibido</GLOSA_ESTADO>
<ERR_CODE>6</ERR_CODE>
<GLOSA_ERR>Empresa No Autorizada a Emitir Documentos
Tributarios Electronicos</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

19

4.7 Ejemplo Parámetros de Salida ERR_CODE, Estado TMD (Existe Nota de Debito
... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>TMD</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>10</ERR_CODE>
<GLOSA_ERR>Existe Nota de Debito que Modifica el Texto
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

Nota: Este ejemplo corresponde a un Documento Referenciado, lo que significa que los
datos coinciden, pero el documento está referenciado por una Nota de Crédito o
Debito.
4.8

Ejemplo Parámetros de Salida ERR_CODE, Estado TMC(Existe Nota de Crédito

... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>TMC</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>11</ERR_CODE>
<GLOSA_ERR>Existe Nota de Crédito que Modifica el Texto
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.9

Ejemplo Parámetros de Salida ERR_CODE, Estado MMD(Existe Nota de Debito

... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>MMD</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>12</ERR_CODE>
<GLOSA_ERR>Existe Nota de Debito que Modifica Montos
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

20

4.10

Ejemplo Parámetros de Salida ERR_CODE,

Estado MMC(Existe Nota de

Crédito ... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>MMC</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>13</ERR_CODE>
<GLOSA_ERR>Existe Nota de Crédito que Modifica Montos
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.11

Ejemplo Parámetros de Salida ERR_CODE, Estado AND(Existe Nota de

Debito... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>AND</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>14</ERR_CODE>
<GLOSA_ERR>Existe Nota de Debito que anula
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.12

Ejemplo Parámetros de Salida ERR_CODE,

Estado ANC (Existe Nota de

Crédito... )
<SII:RESPUESTA xmlns:SII="http://www.ssi.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>ANC</ESTADO>
<GLOSA_ESTADO>DTE Recibido</GLOSA_ESTADO>
<ERR_CODE>15</ERR_CODE>
<GLOSA_ERR>Existe Nota de Crédito que anula
Documento</GLOSA_ERR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

21

4.13 Ejemplo Parámetros de Salida Token Estado 002 (ERROR: TOKEN INACTIVO)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<ESTADO>002</ESTADO>
<GLOSA>TOKEN+INACTIVO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.14 Ejemplo Parámetros de Salida Token Estado 003 (ERROR: TOKEN NO EXISTE)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<ESTADO>003</ESTADO>
<GLOSA>NO+EXISTE</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.15 Ejemplo Parámetros de Salida Token Estado 003 (ERROR: TOKEN NO EXISTE)
<?xml version="1.0" encoding="UTF-8" ?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<ESTADO>001</ESTADO>
<GLOSA>COOKIE INACTIVO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.16 Ejemplo Parámetros de Salida Otros ERRORES –1 (ERROR: RETORNO CAMPO
ESTADO, NO EXISTE)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-1</ESTADO>
<GLOSA>ERROR RETORNO CAMPO ESTADO, NO EXISTE</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.17 Ejemplo Parámetros de Salida Otros ERRORES –2 (ERROR RETORNO)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-2</ESTADO>
<GLOSA>ERROR RETORNO </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

22

4.18 Ejemplo Parámetros de Salida Otros ERRORES –3 (ERROR RETORNO)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-3</ESTADO>
<GLOSA> ERROR RETORNO </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

23

CAPITULO 5
GUIA PARA REALIZAR PRUEBAS

Para probar el servicio, se deben seguir los siguientes pasos:

1.- Autenticarse mediante Autenticación Automática con Certificado Digital(CD).
Nota:
El proceso de la Autenticación Automática con CD, permitirá obtener un Token, el
cuál es requerido como parámetro de Entrada por el WS QueryEstDte.jws.
Para la implementación de la Autenticación Automática, se recomienda ver
Manual del Desarrollador “Ws Autenticación con Certificado Digital”.
2.- Una vez obtenido el Token(de acuerdo a lo detallado más arriba en paso 1), se debe

invocar al sitio donde se encuentra el WS (QueryEstDte), Ejemplo:
https://maullin.sii.cl/DTEWS/QueryEstDte.jws?WSDL

3.- Luego, para realizar las pruebas, al WS invocado, se le deben pasar los parámetros

de entrada requeridos para la consulta, estos son: RutConsultante , DvConsultante,
RutCompania,
DvCompania
,
RutReceptor,
FechaEmisionDte, MontoDte y Token

DvReceptor,

TipoDte,

FolioDte,

4.- Como respuesta del WS se obtiene los siguientes tag.
9
9
9
9
9

ESTADO
GLOSA
ERR_CODE
GLOSA_ERR
NUM_ATENCION

Nota: El ambiente de producción, es idéntico al de certificación, solo cambia el nombre del servidor, tal
como se indica más abajo.
https://palena.sii.cl/DTEWS/QueryEstDte.jws?WSDL

24

REFERENCIAS

Para mayor información sobre temas tratados en este manual, se recomienda visitar:

Documentación WSDL: http://www.w3.org/TR/wsdl
Herramienta XMLSPY : http://www.xmlspy.com/features_wsdl.html

25
