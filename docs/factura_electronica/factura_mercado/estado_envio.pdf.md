---
url: https://www.sii.cl/factura_electronica/factura_mercado/estado_envio.pdf
titulo: Manual de Desarrollador Externo
categoria: factura_electronica
---
Manual de Desarrollador Externo
Consulta de Estado de Upload Dte
OI2004_ CEUPDTE _MDE_1.10

Oficina Internet
Subdirección Informática
Servicio Impuestos Internos
Fecha: 08/11/2004

INDICE

CONTROL DE VERSIONES .................................................................................................................3
INTRODUCCIÓN .................................................................................................................................4
CAPITULO 1........................................................................................................................................5
OBJETIVOS Y CARACTERISTICAS ..................................................................................................5
1. O BJETIVOS DE LA APLICACIÓN................................ ................................ ................................ ............5
2. CARACTERÍSTICA DE LA APLICACIÓN ...................................................................................................5
CAPITULO 2........................................................................................................................................6
WSDL DE Q UERY EST U P ................................ ................................ ................................ ....................6
2.1.1 WSDL DE Q UERY ESTU P. JWS .....................................................................................................6
2.1.2
D ETALLE PARÁMETROS DEL WSDL .........................................................................................9
CAPITULO 3...................................................................................................................................... 10
DETALLE PARÁMETROS DEL SERVICIO....................................................................................... 10
3.1 PARÁMETROS DE E NTRADA ......................................................................................................... 10
3.1.1 EJEMPLO R EAL P ARÁMETROS DE E NTRADA FORMATO WSDL................................ .......................... 10
3.2 PARÁMETROS DE S ALIDA ............................................................................................................. 11
3.3 ESTADOS DE S ALIDA ................................................................................................................... 11
3.4 EJEMPLOS DE SALIDA ................................................................................................................. 12
3.4.1 EJEMPLO P ARÁMETROS DE S ALIDA WSDL CODIFICADO E STADO EPR ............................................ 12
CAMBIAR SALIDA DEACURDO A EJEMPLO 3.4.1.1 .................................................................................... 12
3.4.1.1 E JEMPLO PARÁMETROS DE SALIDA D ECODIFICADO ..................................................................... 12
3.5 ESTADOS DE S ALIDA POR ERROR.............................................................................................. 13
3.5.1 Errores de Consulta: ................................ ................................ ................................ .......... 13
3.5.2 Errores por Autenticación: ................................ ................................ ................................ .. 14
3.5.3 Otros Errores: .................................................................................................................... 14
3.5.1 EJEMPLODE SALIDA ERROR WSDL CODIFICADO (ERR_CODE 2) .............................................. 15
3.5.1.1 E JEMPLO DE S ALIDA ERROR WSDL DECODIFICADO ( ERR_CODE 2: ERROR: DE PROCESO) ..... 15
CAPITULO 4...................................................................................................................................... 16
EJEMPLOS DE SALIDA FORMATO XML........................................................................................ 16
4.1 EJEMPLO P ARÁMETROS DE S ALIDA E STADO RSC (RECHAZADO POR ERROR EN SCHEMA ) ..................... 16
4.2 EJEMPLO P ARÁMETROS DE S ALIDA E STADO SOK (S CHEMA V ALIDADO ).............................................. 16
4.3 EJEMPLO P ARÁMETROS DE S ALIDA E STADO CRT (CARATULA OK) ..................................................... 16
4.4 EJEMPLO P ARÁMETROS DE S ALIDA E STADO RFR (P ARAMETROS DE ENTRADA INCOMPLETOS )............... 17
4.5 EJEMPLO P ARÁMETROS DE S ALIDA E STADO FOK (ERROR : RETORNO DATOS) ............................... 17
4.6 EJEMPLO P ARÁMETROS DE S ALIDA E STADO PRD (ERROR : RETORNO DATOS ) ....................................17
4.7 EJEMPLO P ARÁMETROS DE S ALIDA E STADO RCT (RECHAZADO POR ERROR EN CARÁTULA ) .................. 18
4.8 EJEMPLO P ARÁMETROS DE S ALIDA E STADO EPR (ENVÍO P ROCESADO ).............................................. 18
4.9 EJEMPLO P ARÁMETROS DE S ALIDA SRV_CODE 1( ERROR: DE PROCESO )....................................... 18
4.10 EJEMPLO P ARÁMETROS DE S ALIDA ERR_CODE 2(ERROR: DE PROCESO )..................................... 18
4.11 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-3 (ERROR: RUT USUA RIO NO EXISTE) ................ 19
4.12 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO- 4(ERROR: OBTENCIÓN DE DATOS ).................... 19
4.13 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-5(ERROR: RETORNO DATOS) ............................... 19
4.14 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-6(ERROR: USUARIO NO AUTORIZADO) .............. 19
4.15 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO- 7(ERROR: RETORNO DATOS)............................... 19
4.16 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-8(ERROR: RETORNO DE DATOS) ......................... 20
4.17 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-9(ERROR: RETORNO DE DATOS )........................ 20
4.18 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-10(ERROR: VALIDA RUT)...................................... 20

1

4.19 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-11(ERROR: CONSULTA) ......................................... 20
4.20 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-12(ERROR: RETORNO CONSULTA) ...................... 20
4.21 EJEMPLO P ARÁMETROS DE S ALIDA ESTADO-13(ERROR: USUARIO NULO) ................................ 21
4.22 E JEMPLO P ARÁMETROS DE S ALIDA ESTADO-14 (ERROR: XML RETORNO) .............................. 21
4.23 EJEMPLO P ARÁMETROS DE S ALIDA E STADO 002 (ERROR: TOKEN INACTIVO) ............................. 21
4.24 EJEMPLO P ARÁMETROS DE S ALIDA E STADO 003 (ERROR: TOKEN NO EXISTE)............................ 21
4.25 EJEMPLO P ARÁMETROS DE S ALIDA E STADO 001 (ECOOKIE INACTIVO)........................................ 21
CAPITULO 5...................................................................................................................................... 22
GUIA PARA REALIZAR PRUEBAS................................ ................................ ................................ .. 22
REFERENCIAS .............................................................................................................................. 23

2

CONTROL DE VERSIONES
Versión

Fecha

CONTROL DE VERSIONES
Autor

1.0
29/01/2003
1.1
24/04/2003
1.3
22/04/2003
1.4
11/08/2003
Se agregaron Estados de salida

Zulema Olguín T.
Zulema Olguín T.
Zulema Olguín T.
Zulema Olguín T.

1.5
08/04/2004
Se modifico Url en Capitulo 5 (Guía
para Pruebas, le faltaba la “s” al http)

Zulema Olguín T

Revisor
Quentin Sherman
Quentin Sherman
Quentin Sherman

Donde decía:
http://maullin.sii.cl/DTEWS/QueryEstUp.j
ws?WSDL
http://maullin.sii.cl/DTEWS/QueryEstUp.j
ws?WSDL

Se cambio por:
https://maullin.sii.cl/DTEWS/QueryEstUp
.jws?WSDL
https://maullin.sii.cl/DTEWS/QueryEstUp
.jws?WSDL

1.6
08/04/2004
Se m odifico texto de introducción
(como acceder a los WS del SII)
1.7
07/05/2004
Se modifico texto de los mensajes
de salida: 3.5.3 Otros Errores
1.8
15/06/2004
Se agrego al XML de salida un
número de atención
(<NUM_ATENCIÓN>), ver punto 3.2
1.9
11/08/2004
Se modifica URL WS:

Zulema Olguín T.

Zulema Olguín T.

Zulema Olguín T.

Zulema Olguín T.

https://maullin.sii.cl/DTEWS/QueryE
stUp.jws?WSDL
1.10
08/11/2004
Se agrego estado “001” (Cookie
Inactivo), ver punto : 3.5.2

Zulema Olguín T
.

3

INTRODUCCIÓN
Consulta Estado de Upload DTE (CEUPDTE), como parte del proyecto Documentos
Tributarios Electrónicos (DTE), entrega a las empresas un servicio (“QueryEstUp”), el
cual permite consultar a través de WEB SERVICES, el estado de un archivo DTE
enviado al SII, mediante Upload.
Este documento está dirigido a quienes tengan la misión de utilizar y probar el servicio
mencionado anteriormente (QueryEstUp).
Para acceder a los servicios que ofrece el SII, se debe utilizar WSDL(Web Services
Definition Language).
WSDL es un lenguaje descriptor, basado en XML, que permite conocer en forma
abstracta, la gramática de los componentes de un Web Service (ubicación, formato,
tipos de datos, servicios, funciones, parámetros de entrada, salida, etc).
Para poder acceder a un WSDL, se debe conocer su ubicación, por ejemplo:
La ubicación del WSDL, para el ambiente de certificación de QueryEstUp.jws, es:
https://maullin.sii.cl/DTEWS/QueryEstUp.jws?WSDL.
Cuando el cliente conoce el WSDL del servicio, puede construir un Request en formato
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

4

CAPITULO 1
OBJETIVOS Y CARACTERISTICAS
1. Objetivos de la aplicación
El objetivo de este servicio es informar el Estado de un archivo DTE, enviado mediante
Upload.
2. Característica de la aplicación
ü El servicio QueryEstUp, es de tipo “Consulta” -”Respuesta
ü Es una aplicación B2B.
ü Esta aplicación puede ser utilizada por aquellos usuarios habilitados para su uso.

5

CAPITULO 2
WSDL DE QueryEstUp

La ubicación del WSDL, para esta aplicación (QueryEstUp) es:
https://maullin.sii.cl/DTEWS/QueryEstUp.jws?WSDL
2.1.1 WSDL de QueryEstUp.jws
<?xml version="1.0" encoding="UTF-8" ?>
<wsdl:definitions targetNamespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
xmlns="http://schemas.xmlsoap.org/wsdl/"
xmlns:apachesoap="http://xml.apache.org/xml-soap"
xmlns:impl="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
xmlns:intf="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<wsdl:types />
<wsdl:message name="getEstUpResponse">
<wsdl:part name="getEstUpReturn" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionMenorRequest" />
<wsdl:message name="getVersionPatchRequest" />
<wsdl:message name="getVersionMayorResponse">
<wsdl:part name="getVersionMayorReturn" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionMayorRequest" />
<wsdl:message name="getVersionPatchResponse">
<wsdl:part name="getVersionPatchReturn" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getEstUpRequest">
<wsdl:part name="RutCompania" type ="xsd:string" />
<wsdl:part name="DvCompania" type="xsd:string" />
<wsdl:part name="TrackId" type="xsd:string" />
<wsdl:part name="Token" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionMenorResponse">
<wsdl:part name="getVersionMenorReturn" type="xsd:string" />
</wsdl:message>
<wsdl:portType name="QueryEstUp">
<wsdl:operation name="getVersionMayor">
<wsdl:input message ="impl:getVersionMayorRequest"
name="getVersionMayorRequest" />
<wsdl:output message="impl:getVersionMayorResponse"
name="getVersionMayorResponse" />
</wsdl:operation>
<wsdl:operation name="getVersionMenor">
<wsdl:input message ="impl:getVersionMenorRequest"
name="getVersionMenorRequest" />
<wsdl:output message="impl:getVersionMenorResponse"
name="getVersionMenorResponse" />
</wsdl:operation>
<wsdl:operation name="getVersionPatch">
<wsdl:input message ="impl:getVersionPatchRequest"
name="getVersionPatchRequest" />
<wsdl:output message="impl:getVersionPatchResponse"
name="getVersionPatchResponse" />

6

</wsdl:operation>
<wsdl:operation name="getEstUp" parameterOrder="RutCompania DvCompania
TrackId Token">
<wsdl:input message ="impl:getEstUpRequest" name="getEstUpRequest"
/>
<wsdl:output message="impl:getEstUpResponse"
name="getEstUpResponse" />
</wsdl:operation>
</wsdl:portType>
<wsdl:binding name="QueryEstUpSoapBinding" type="impl:QueryEstUp">
<wsdlsoap:binding style="rpc"
transport="http://schemas.xmlsoap.org/soap/http" />
<wsdl:operation name="getVersionMayor">
<wsdlsoap:operation soapAction="" />
<wsdl:input name="getVersionMayorRequest">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:input>
<wsdl:output name="getVersionMayorResponse">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="getVersionMenor">
<wsdlsoap:operation soapAction="" />
<wsdl:input name="getVersionMenorRequest">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:input>
<wsdl:output name="getVersionMenorResponse">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="getVersionPatch">
<wsdlsoap:operation soapAction="" />
<wsdl:input name="getVersionPatchRequest">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:input>
<wsdl:output name="getVersionPatchResponse">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="getEstUp">
<wsdlsoap:operation soapAction="" />
<wsdl:input name="getEstUpRequest">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"

7

namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:input>
<wsdl:output name="getEstUpResponse">
<wsdlsoap:body
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
namespace="https://maullin.sii.cl/DTEWS/QueryEstUp.jws"
use="encoded" />
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:service name="QueryEstUpService">
<wsdl:port binding="impl:QueryEstUpSoapBinding" name="QueryEstUp">
<wsdlsoap:address
location="https://maullin.sii.cl/DTEWS/QueryEstUp.jws" />
</wsdl:port>
</wsdl:service>
</wsdl:definitions>

Figura 2.1.1

8

2.1.2 Detalle Parámetros del WSDL
De acuerdo a lo destacado en el recuadro del esquema WSDL figura 2.1.1,
QueryEstUp entrega sólo un servicio “getEstUp”, el cual requiere de los siguientes
parámetros de entrada: Rut, Dv, TrackId y Token.

9

CAPITULO 3
DETALLE PARÁMETROS DEL SERVICIO

3.1 Parámetros de Entrada
Los parámetros de entrada requeridos por el servicio, se detallan en el siguiente
ejemplo:
3.1.1 Ejemplo Real Parámetros de Entrada Formato WSDL
<SOAP-ENV:Envelope xmlns:SOAPENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SOAP-ENV:Body>
<m:getEstUp xmlns:m=" https://maullin.sii.cl/DTEWS/QueryEstUp.jws ">
<Rut xsi:type="xsd:string"></Rut>
<Dv xsi:type="xsd:string"></Dv>
<TrackId xsi:type="xsd:string"></TrackId>
<Token xsi:type="xsd:string"></Token>
</m:getEstUp>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope >

Donde:
Campo

Tipo

Rut
Dv

String numérico
String Alfanumérico

Largo
1-8
1-1

TrackId String numérico

1-10

Token

1-40

String Alfanumérico

Detalle
Corresponde al Rut Consultado
Corresponde al DV del Rut
Consultado
Corresponde al identificador de
Envió(similar
al
número
de
atención o folio)
Es un Token es un identificador
único el cual es almacenado y
enviado al cliente en el Header del
Response de la Autenticación
Automática
con
Certificado
Digital (CD), y permite la
búsqueda de toda la información
relacionada a una sesión del
cliente.

Obligatorios
S
S
S
S

10

3.2 Parámetros de Salida
La salida del Servicio corresponden a un “string” XML codificado, por lo tanto necesario
que el programa cliente sea capaz de decodificar el “string” y llevarlo a formato original,
los campos de retorno son: TRACKID, ESTADO y GLOSA, NUM_ATENCIÓN.
Donde:
Campo

Tipo

TRACKID

String numérico

ESTADO

String numérico

GLOSA

String Alfanumérico

NUM_ATENCION String

Largo
1-10
1-3
1-40
1-40

Detalle
identificador de Envió(similar al
número de atención o folio)
Código Estado
Detalle Código
Número
de
Atención,
Identificador de la consulta

Obligatorios
S
S
S
S

3.3 Estados de Salida
El resultado de la consulta puede arrojar uno de los siguientes Estados:
Estado
RSC
SOK
CRT
RFR
FOK
PDR
RCT
EPR

Tipo
String
String
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico

Glosa
Rechazado por Error en Schema
Schema Validado
Carátula OK
Rechazado por Error en Firma
Firma de Envió Validada
Envió en Proceso
Rechazado por Error en Carátula
Envió Procesado

11

3.4 Ejemplos de Salida
A continuación se mostrará una serie de ejemplos de salida en ambos formatos
Codificado y Decodificado.
3.4.1 Ejemplo Parámetros de Salida WSDL Codificado Estado EPR
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance ">
<soapenv:Body >
<ns1:getEstUpResponse
soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/ "
xmlns:ns1="https://maullin.sii.cl/DTEWS/QueryEstUp.jws ">
<getEstUpReturn xsi:type ="xsd:string">&lt;?xml version =&quot;1.0&quot;
encoding =&quot;UTF-8&quot;?&gt;
&lt;SII:RESPUESTA
xmlns:SII=&quot;http://www.sii.cl/XMLSchema&quot;&gt;&lt;SII:RESP_HDR&gt;&lt;TRACKID&gt;5329
2&lt;/TRACKID&gt;&lt;ESTADO&gt;EPR&lt;/ESTADO&gt;&lt;GLOSA&gt;Envio
Procesado&lt;/GLOSA&gt;&lt;/SII:RESP_HDR&gt;&lt;SII:RESP_BODY&gt;&lt;TIPO_DOCTO&gt;56&lt;/TI
PO_DOCTO&gt;&lt;INFORMADOS&gt;1&lt;/INFORMADOS&gt;&lt;ACEPTADOS&gt;0&lt;/ACEPTADOS&gt;&lt;RE
CHAZADOS&gt;1&lt;/RECHAZADOS&gt;&lt;REPAROS&gt;0&lt;/REPAROS&gt; &lt;NUM_ATENCION&gt;532 (
2004/06/14
16:44:20)&lt;/NUM_ATENCION&gt;&lt;/SII:RESP_BODY&gt;&lt;/SII:RESPUESTA&gt;</getEstUpReturn>
</ns1:getEstUpResponse>
</soapenv:Body>
</soapenv:Envelope>

Cambiar salida deacurdo a Ejemplo 3.4.1.1
3.4.1.1 Ejemplo Parámetros de Salida Decodificado
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<TRACKID>53292</TRACKID >
<ESTADO >EPR</ESTADO>
<GLOSA>Envio Procesado</GLOSA>
</SII:RESP_HDR>
- <SII:RESP_BODY>
<TIPO_DOCTO >56</TIPO_DOCTO>
<INFORMADOS>1</INFORMADOS>
<ACEPTADOS>0</ACEPTADOS>
<RECHAZADOS>1</RECHAZADOS>
<REPAROS>0</REPAROS>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20) </NUM_ATENCION>
</SII:RESP_BODY>
</SII:RESPUESTA>

12

3.5 Estados de Salida por ERROR
El resultado de la consulta puede arrojar uno de los siguientes Estados de Error:

3.5.1 Errores de Consulta:
ü SRV_CODE
ü SQL_CODE
ü ERR_CODE

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

SQL_CODE
0
OTRO

Tipo
S tring numérico
S tring numérico

Largo Glosa
1-2
Schema Validado
1-2
Código de Oracle

ERR_CODE
0
1

Tipo
S tring numérico
S tring numérico

2

S tring numérico

Largo Glosa
1-1
Se retorna el estado
1-1
El envío no es de la Empresa, faltan
parámetros de entrada.
1-1
Error de Proceso

13

3.5.2 Errores por Autenticación:

TOKEN
001
002
003

Tipo
S tring
S tring
S tring

Largo
1-3
1-3
1-3

Glosa
Cookie Inactivo(o Token Inactivo)
Token Inactivo
Token No Existe

3.5.3 Otros Errores:
ESTADO
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
-11
-12
-13
-14
Otros

Tipo
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico
String numérico

Largo Glosa
ERROR: RETORNO CAMPO ESTADO, NO
1-1
1-1
1-1
1-1
1-1
1-1
1-1
1-1
1-1
1-2
1-2
1-2
1-2
1-2

EXISTE
ERROR RETORNO
ERROR: RUT USUARIO NO EXISTE
ERROR OBTENCION DE DATOS
ERROR RETORNO DATOS
ERROR: USUARIO NO AUTORIZADO
ERROR RETORNO DATOS
ERROR: RETORNO DATOS
ERROR: RETORNO DATOS
ERROR: VALIDA RUT USUARIO
ERR_CODE, SQL_CODE, SRV_CODE
ERROR: RETORNO CONSULTA
ERROR RUT USUARIO NULO
ERROR XML RETORNO DATOS

14

3.5.1 Ejemplode Salida ERROR WSDL Codificado (ERR_CODE 2)
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soapenv:Body>
<ns1:getEstUpResponse
soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns1="
https://maullin.sii.cl/DTEWS/QueryEstUp.jws ">
<getEstUpReturn xsi:type="xsd:string">&lt;?xml version=&quot;1.0&quot;
encoding=&quot;UTF-8&quot;?&gt;
&lt;SII:RESPUESTA
xmlns:SII=&quot;http://www.sii.cl/XMLSchema&quot;&gt;&lt;SII:RESP_HDR&gt;&lt;E
STADO&gt;1&lt;/ESTADO&gt;&lt;ERR_CODE&gt;2&lt;/ERR_CODE&gt;&lt;SQL_CODE/&gt;&lt;SRV_COD
E/&gt;&lt;/SII:RESP_HDR&gt; &lt;NUM_ATENCION&gt;532 ( 2004/06/14
16:44:20)&lt;/NUM_ATENCION&gt;&lt;/SII:RESPUESTA&gt;</getEstUpReturn>
</ns1:getEstUpResponse>
</soapenv:Body>
</soapenv:Envelope>

3.5.1.1 Ejemplo de Salida ERROR WSDL Decodificado (ERR_CODE 2: ERROR: De
proceso)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO >-1</ESTADO>
<ERR_CODE>2</ERR_CODE>
<SQL_CODE />
<SRV_CODE />
</SII:RESP_HDR>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESPUESTA>

15

CAPITULO 4
EJEMPLOS DE SALIDA FORMATO XML

En este capítulo, se muestran los ejemplos de los posibles Estados de Salida de la
aplicación.
4.1 Ejemplo Parámetros de Salida Estado RSC ( Rechazado por Error en Schema)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>RSC</ESTADO>
<GLOSA>Rechazado por Error en Schema</ GLOSA >
<NUM_ATENCION >532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.2 Ejemplo Parámetros de Salida Estado SOK (Schema Validado)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>SDK</ESTADO>
<GLOSA >Schema Validado</ GLOSA >
<NUM_ATENCION >532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.3 Ejemplo Parámetros de Salida Estado CRT (Caratula OK)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>CRT</ESTADO>
<GLOSA >Caratula OK</ GLOSA >
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

16

4.4 Ejemplo Parámetros de Salida Estado RFR (Parametros de Entrada
Incompletos)

§
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>RFR</ESTADO>
<GLOSA>Rechazado por Error en Firma</GLOSA>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.5 Ejemplo Parámetros de Salida Estado FOK (Error: RETORNO DATOS)
§
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>05</ESTADO>
<GLOSA>Error: RETORNO DATOS</GLOSA>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.6 Ejemplo Parámetros de Salida Estado PRD (Error: Retorno Datos)
§
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>PRD</ESTADO>
<GLOSA>Error Retorno Datos</GLOSA>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

17

4.7 Ejemplo Parámetros de Salida Estado RCT ( Rechazado por Error en Carátula)
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>RCT</ESTADO>
<GLOSA>Rechazado por Error en Carátula</GLOSA>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.8 Ejemplo Parámetros de Salida Estado EPR (Envío Procesado)
§
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<TRACKID>251</TRACKID>
<ESTADO>EPR</ESTADO>
<GLOSA>Envio Procesado</GLOSA>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
- <SII:RESP_BODY>
<TIPO_DOCTO>33</TIPO_DOCTO>
<INFORMADOS>1</INFORMADOS>
<ACEPTADOS>1</ACEPTADOS>
<RECHAZADOS>0</RECHAZADOS>
<REPAROS>0</REPAROS>
</SII:RESP_BODY>
</SII:RESPUESTA>

4.9 Ejemplo Parámetros de Salida SRV_CODE 1(ERROR: De proceso )
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-11</ESTADO>
<ERR_CODE/>
<SQL_CODE />
<SRV_CODE/>1</ERR_CODE>
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.10 Ejemplo Parámetros de Salida ERR_CODE 2(ERROR: De proceso)
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-11</ESTADO>
<ERR_CODE>2</ERR_CODE>
<SQL_CODE />
<SRV_CODE />
<NUM_ATENCION>532 ( 2004/06/14 16:44:20)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

18

4.11 Ejemplo Parámetros de Salida ESTADO-3 (ERROR: RUT USUARIO NO EXISTE )
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-3</ESTADO>
<GLOSA>ERROR : RUT USUARIO NO EXISTE </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.12 Ejemplo Parámetros de Salida ESTADO-4(ERROR: OBTENCIÓN DE DATOS )
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-4</ESTADO>
<GLOSA>ERROR : OBTENCIÓN DE DATOS </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.13 Ejemplo Parámetros de Salida ESTADO-5(ERROR: RETORNO DATOS)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-5</ESTADO>
<GLOSA>ERROR : RETORNO DE DATOS</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.14 Ejemplo Parámetros de Salida ESTADO-6(ERROR: USUARIO NO AUTORIZADO)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-6</ESTADO>
<GLOSA>ERROR :USUARIO NO AUTORIZADO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.15 Ejemplo Parámetros de Salida ESTADO-7(ERROR: RETORNO DATOS)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-7</ESTADO>
<GLOSA>ERROR: RETORNO DATOS </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

19

4.16 Ejemplo Parámetros de Salida ESTADO-8(ERROR: RETORNO DE DATOS)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-8</ESTADO>
<GLOSA>ERROR: RETORNO DE DATOS </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.17 Ejemplo Parámetros de Salida ESTADO-9(ERROR: RETORNO DE DATOS )
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-9</ESTADO>
<GLOSA>ERROR: RETORNO DE DATOS </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.18 Ejemplo Parámetros de Salida ESTADO-10(ERROR: VALIDA RUT)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-10</ESTADO>
<GLOSA>ERROR: VALIDA RUT </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.19 Ejemplo Parámetros de Salida ESTADO-11(ERROR: CONSULTA)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-11</ESTADO>
<ERR_CODE>1</ERR_CODE>
<SQL_CODE>0</SQL_CODE>
<SRV_CODE>0</SRV_CODE>
<NUM_ATENCION>555 ( 2004/06/15 12:46:08)</NUM_ATENCION>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.20 Ejemplo Parámetros de Salida ESTADO-12(ERROR: RETORNO CONSULTA)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-12</ESTADO>
<GLOSA>ERROR: RETORNO DATOS </GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

20

4.21 Ejemplo Parámetros de Salida ESTADO-13(ERROR: USUARIO NULO)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-13</ESTADO>
<GLOSA>ERROR: RUT USUARIO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA

4.22 Ejemplo Parámetros de Salida ESTADO-14 (ERROR: XML RETORNO)
<?xml version="1.0" encoding="UTF-8" ?>
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>-14</ESTADO>
<GLOSA>ERROR: XML RETORNO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.23 Ejemplo Parámetros de Salida Estado 002 (ERROR: TOKEN INACTIVO)
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>002</ESTADO>
<GLOSA>TOKEN+INACTIVO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.24 Ejemplo Parámetros de Salida Estado 003 (ERROR: TOKEN NO EXISTE )
- <SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
- <SII:RESP_HDR>
<ESTADO>003</ESTADO>
<GLOSA>NO+EXISTE</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

4.25 Ejemplo Parámetros de Salida Estado 001 (ECOOKIE INACTIVO)
<?xml version="1.0" encoding="UTF-8" ?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<ESTADO>001</ESTADO>
<GLOSA>COOKIE INACTIVO</GLOSA>
</SII:RESP_HDR>
</SII:RESPUESTA>

21

CAPITULO 5
GUIA PARA REALIZAR PRUEBAS

Para probar el servicio, se deben seguir los siguientes pasos:
1.- Autenticarse mediante Autenticación Automática con Certificado Digital(CD).
El proceso de la Autenticación Automática con CD, permitirá obtener un Token, el cuál
es requerido como parámetro de Entrada por la aplicación (QueryEstUp).
Para la implementación de la Autenticación Automática, se recomienda ver Manual del
Desarrollador “Ws Autenticación con Certificado Digital”.
2.- Una vez obtenido el Token(de acuerdo a lo detallado más arriba en paso 1), se debe

invocar al sitio de Certificación, en donde se encuentra el WS para QueryEstUp:
https://maullin.sii.cl/DTEWS/QueryEstUp.jws?WSDL
3.- Luego, para realizar las pruebas, se le deben pasar los parámetros de entrada de la

consulta, Rut, Dv, TrackID y Token.
4.- Se obtiene Respuesta.
ü TRACKID
ü

ESTADO

ü GLOSA
ü NUM_ATENCIÓN
ü TIPO_DOCTO (Solo si Estado es EPR)
ü INFORMADOS (Solo si Estado es EPR)
ü ACEPTADOS (Solo si Estado es EPR)
ü RECHAZADOS (Solo si Estado es EPR)
ü REPAROS
(Solo si Estado es EPR)

Nota: El ambiente de producción, es idéntico al de certificación, solo cambia el nombre del servidor, tal
como se indica más abajo.

https://palena.sii.cl/DTEWS/QueryEstUp.jws?WSDL

22

REFERENCIAS

Para mayor información sobre temas tratados en este manual, se recomienda visitar:

Documentación WSDL: http://www.w3.org/TR/wsdl
Herramienta XMLSPY : http://www.xmlspy.com/features_wsdl.html

23
