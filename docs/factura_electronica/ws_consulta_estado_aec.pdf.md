---
url: https://www.sii.cl/factura_electronica/ws_consulta_estado_aec.pdf
titulo: Manual de Desarrollador Externo
categoria: factura_electronica
---
Manual de Desarrollador Externo
Web Service de :
Consulta Estado Envío de AEC al Registro
Consulta de Cesiones

Oficina Factura Electrónica
Subdirección Informática
Servicio Impuestos Internos
Fecha: 05/02/2008

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

INDICE
INTRODUCCIÓN............................................................................................................................................ 4
CAPITULO 1 .................................................................................................................................................. 5
OBJETIVOS Y CARACTERISTICAS ......................................................................................................... 5
1.1 OBJETIVOS DE LA APLICACIÓN .............................................................................................................. 5
1.2 CARACTERÍSTICA DE LA APLICACIÓN ..................................................................................................... 5
CAPITULO 2 .................................................................................................................................................. 6
WSDL DE WSRPETCCONSULTA .................................................................................................................. 6
2.1 GRAMÁTICA DEL WSDL ....................................................................................................................... 6
2.1.1 WSDL de wsRPETCConsulta .................................................................................................. 6
2.1.2 Funciones disponibles en este servicio. ................................................................................... 7
CAPITULO 3 .................................................................................................................................................. 8
DETALLE DE PARÁMETROS DE LAS FUNCIONES ............................................................................... 8
3.1 PARÁMETROS DE ENTRADA .................................................................................................................. 8
3.1.1 Función getEstEnvio................................................................................................................. 8
3.1.2 Función getEstCesion............................................................................................................... 9
3.1.3 Función getEstCesionRelac ................................................................................................... 10
3.2 CAMPOS DE SALIDA ........................................................................................................................... 11
3.2.1 Función getEstEnvio............................................................................................................... 11
3.2.2 Función getEstCesion............................................................................................................. 12
3.2.3 Función getEstCesionRelac ................................................................................................... 13
3.3 CÓDIGOS DE ESTADO ........................................................................................................................ 14
CAPITULO 4 ................................................................................................................................................ 15
GUIA PARA REALIZAR PRUEBAS ......................................................................................................... 15
4.1 PRUEBA DEL SERVICIO ....................................................................................................................... 15
REFERENCIAS............................................................................................................................................ 16

Página 2 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

BITÁCORA DE CAMBIOS
Cambios 05/02/2008
1) Se agrega la función getEstCesionRelac que entrega los datos registrados en el SII, para una cesión
de documento tributario electrónico, a los usuarios autorizados de un contribuyente vinculado con la
cesión ya sea como tenedor o como receptor de dicho documento.

Página 3 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

INTRODUCCIÓN
El servicio wsRPETCConsulta, forma parte del sistema Registro Electrónico de Cesión de Créditos
(RPETC), y corresponde a un servicio que permite a las empresas (contribuyentes) consultar por el
estado de envios de archivos electrónicos de Cesión (AEC) y por el estado de una Cesión.
Este documento está dirigido a quienes tengan la misión de utilizar y probar este servicio.
La forma de acceder a este servicio es a través de WSDL (Web Services Definition Language). Este es un
lenguaje descriptor, basado en XML, que permite conocer en forma abstracta, la gramática de los
componentes de un webservice (ubicación, formato, tipos de datos, servicios, funciones, parámetros de
entrada, salida, etc).
El WSDL que se detalla en este documento apunta al ambiente de certificación del SII, sin embargo este
ambiente es una copia fiel del ambiente de producción.
La ubicación del WSDL de wsDTECorreo es:
Certificación : https://maullin.sii.cl/DTEWS/services/wsRPETCConsulta?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/wsRPETCCOnsulta?wsdl

Una vez que el cliente conoce el WSDL del webservice, debe construir un Request en formato SOAP
(Simple Object Access Protocolo), para luego enviarlo hacia el proveedor de servicio (SII), previa
Autenticación.
Respecto a la Autenticación, para poder realizar consultas hacia cualquier webservice entregado por el
SII, los clientes deben estar previamente autenticados a través de la AUTENTICACIÓN AUTOMATICA.

Requisitos de uso.
Para poder utilizar este manual, es necesario tener previo conocimiento de XML, Web Services y
Certificado Digital.
Recomendaciones.
Se recomienda el uso de la herramienta XMLSPY5 de la Altova ( http://www.altova.com ).

Página 4 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

CAPITULO 1
OBJETIVOS Y CARACTERISTICAS
1.1 Objetivos de la aplicación
El servicio wsRPETCConsulta, forma parte del proyecto Registro Electrónico de Cesión de Créditos
(RPETC), y corresponde a un servicio que permite a las empresas (contribuyentes) consultar en línea por
el estado de los envíos de AEC y por estado de una Cesión.
1.2 Característica de la aplicación
El servicio wsRPETCConsulta es de tipo “Consulta-Respuesta”
Es una aplicación B2B.
Esta aplicación puede ser utilizada por cualquier contribuyente que tenga Certificado Digital y conozca
los datos solicitados por la consulta específica.

Página 5 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

CAPITULO 2
WSDL de wsRPETCConsulta
2.1 Gramática del WSDL
El siguiente cuadro muestra el WSDL del web service wsRPETCConsulta.
2.1.1

WSDL de wsRPETCConsulta

<?xml version="1.0" encoding="UTF-8" ?>
- <wsdl:definitions targetNamespace="http://DefaultNamespace"
xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:apachesoap="http://xml.apache.org/xmlsoap" xmlns:impl="http://DefaultNamespace" xmlns:intf="http://DefaultNamespace"
xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
+ <wsdl:message name="getVersionResponse">
+ <wsdl:message name="getVersionPatchResponse">
+ <wsdl:message name="getVersionMayorResponse">
+ <wsdl:message name="getEstCesionRelacResponse">
+ <wsdl:message name="getEstEnvioResponse">
<wsdl:message name="getStateRequest" />
- <wsdl:message name="getEstCesionRelacRequest">
<wsdl:part name="Token" type="xsd:string" />
<wsdl:part name="RutEmisor" type="xsd:string" />
<wsdl:part name="DVEmisor" type="xsd:string" />
<wsdl:part name="TipoDoc" type="xsd:string" />
<wsdl:part name="FolioDoc" type="xsd:string" />
<wsdl:part name="RutEmpresa" type="xsd:string" />
<wsdl:part name="DVEmpresa" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionPatchRequest" />
<wsdl:message name="getVersionMayorRequest" />
+ <wsdl:message name="getEstCesionResponse">
- <wsdl:message name="getEstCesionRequest">
<wsdl:part name="Token" type="xsd:string" />
<wsdl:part name="RutEmisor" type="xsd:string" />
<wsdl:part name="DVEmisor" type="xsd:string" />
<wsdl:part name="TipoDoc" type="xsd:string" />
<wsdl:part name="FolioDoc" type="xsd:string" />
<wsdl:part name="IdCesion" type="xsd:string" />
</wsdl:message>
+ <wsdl:message name="getVersionMenorResponse">
<wsdl:message name="getVersionMenorRequest" />
<wsdl:message name="getVersionRequest" />
- <wsdl:message name="getEstEnvioRequest">
<wsdl:part name="Token" type="xsd:string" />
<wsdl:part name="TrackId" type="xsd:string" />
</wsdl:message>
+ <wsdl:message name="getStateResponse">
+ <wsdl:portType name="wsRPETCConsulta">
+ <wsdl:binding name="wsRPETCConsultaSoapBinding" type="intf:wsRPETCConsulta">
+ <wsdl:service name="wsRPETCConsultaService">
</wsdl:definitions>

Página 6 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

2.1.2

Funciones disponibles en este servicio.

Como muestra el wsdl anterior, este servicio se cuenta con varias funciones entre las que se destacan:
: Entrega el estado de un envío.
: Entrega los datos registrados en el SII para una cesión de documento,
esta consulta requiere la clave de acceso a la cesión .
getEstCesionRelac : Entrega los datos registrados en el SII, para una cesión de
documento tributario electrónico, a los usuarios autorizados de un
contribuyente vinculado con la cesión ya sea como tenedor o como
receptor de dicho documento.

getEstEnvio
getEstCesión

Página 7 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

CAPITULO 3
DETALLE DE PARÁMETROS DE LAS FUNCIONES
3.1 Parámetros de Entrada
Los parámetros de entrada requeridos por cada función del servicio, se detallan a continuación:
3.1.1

Función getEstEnvio

<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<SOAP-ENV:Body>
<m:getEstEnvio xmlns:m="http://DefaultNamespace" SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<Token xsi:type="xsd:string">String</Token>
<TrackId xsi:type="xsd:string">String</TrackId>
</m:getEstEnvio>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Donde:
Parámetro
Token

Tipo
String Alfanumérico

Largo
1-40

TrackId

String numérico

1-10

Detalle
El Token es un identificador único que
identifica a un contribuyente, el cual es
almacenado y enviado al cliente en el
Header del
Response de la
Autenticación
Automática
con
Certificado Digital (CD), y permite la
búsqueda de toda la información
relacionada a una sesión del cliente.
Trackid del envío que se consulta.

Página 8 de 16

Obligatorio
S

S

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.1.2

Función getEstCesion

<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<SOAP-ENV:Body>
<m:getEstCesion xmlns:m="http://DefaultNamespace"
SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<Token xsi:type="xsd:string">String</Token>
<RutEmisor xsi:type="xsd:string">String</RutEmisor>
<DVEmisor xsi:type="xsd:string">String</DVEmisor>
<TipoDoc xsi:type="xsd:string">String</TipoDoc>
<FolioDoc xsi:type="xsd:string">String</FolioDoc>
<IdCesion xsi:type="xsd:string">String</IdCesion>
</m:getEstCesion>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Donde:
Parámetro
Token

Tipo
String Alfanumérico

Largo
1-40

RutEmisor
DVEmisor
TipoDoc

String numérico
String Alfanumérico
String numérico

1-10
1
1-3

FolioDoc
IdCesion

String numérico
String Alfanumérico

1-10
1-20

Detalle
Obligatorio
El Token es un identificador único que
S
identifica a un contribuyente, el cual es
almacenado y enviado al cliente en el
Header del Response de la Autenticación
Automática con Certificado Digital (CD), y
permite la búsqueda de toda la información
relacionada a una sesión del cliente.
Rut del emisor del documento cedido
S
Dígito verificador
S
Código del Tipo de Documento:
S
33 : Factura Electrónica
34 : Factura no Afecta o Exenta Electrónica
Folio del documento cedido.
S
Clave de acceso a la información de la
N
cesión. Este parámetro es opcional, en caso
de no venir solo entrega información sobre si
esta cedido o no el documento consultado.

Página 9 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.1.3

Función getEstCesionRelac

<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<SOAP-ENV:Body>
<m:getEstCesionRelac xmlns:m="http://DefaultNamespace" SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<Token xsi:type="xsd:string">String</Token>
<RutEmisor xsi:type="xsd:string">String</RutEmisor>
<DVEmisor xsi:type="xsd:string">String</DVEmisor>
<TipoDoc xsi:type="xsd:string">String</TipoDoc>
<FolioDoc xsi:type="xsd:string">String</FolioDoc>
<RutEmpresa xsi:type="xsd:string">String</RutEmpresa>
<DVEmpresa xsi:type="xsd:string">String</DVEmpresa>
</m:getEstCesionRelac>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Donde:
Parámetro
Token

Tipo
String
Alfanumérico

Largo
1-40

RutEmisor
DVEmisor

1-10
1

TipoDoc

String numérico
String
Alfanumérico
String numérico

FolioDoc
RutEmpresa

String numérico
String numérico

1-10
1-10

DVEmpresa

String
Alfanumérico

1

1-3

Detalle
Obligatorio
El Token es un identificador único que
S
identifica a un contribuyente, el cual es
almacenado y enviado al cliente en el
Header del Response de la Autenticación
Automática con Certificado Digital (CD), y
permite la búsqueda de toda la información
relacionada a una sesión del cliente.
Rut del emisor del documento cedido
S
Dígito verificador del Rut Emisor
S
Código del Tipo de Documento:
33 : Factura Electrónica
34 : Factura no Afecta o Exenta Electrónica
Folio del documento cedido.
Este Rut debe corresponder a una empresa
que se encuentre vinculada con el
documento consultado, ya sea como
Tenedor o Receptor.
Dígito verificador del Rut Empresa

Página 10 de 16

S
S
S

S

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.2 Campos de Salida
La salida de cada función corresponden a un “string” XML codificado, que se compone de dos secciones
principales:
RESP_HDR
: Esta sección es común a ambas funciones y corresponde al estado de la
operación que se realiza, se compone de:
Campo
ESTADO

Tipo
String Alfanumérico

GLOSA

String Alfanumérico

Detalle
Resultado de la operación consulta. Ver detalle en
punto 3.3.
En caso de error, glosa del error ocurrido.

RESP_BODY : Esta sección es propia de cada función, entrega los datos de salida de cada
consulta. A continuación se detallan para cada una de ellas.
3.2.1

Función getEstEnvio

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<SII:ESTADO>0</SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY>
<TRACKID>36322</TRACKID>
<ESTADO_ENVIO>EOK</ESTADO_ENVIO>
<DESC_ESTADO>Envio Aceptado</DESC_ESTADO>
</SII:RESP_BODY>
</SII:RESPUESTA>

Donde:
Campo
TRACKID
ESTADO_ENVIO

Tipo
String numérico
String Alfanumérico

Detalle
TrackId consultado.
Estado del envío:
UPL
RCP
RSC
SOK
RFS
FSO
RCR
COK
VDC
RDC
VCS
RCS
EOK
EAN

DESC_ESTADO

String Alfanumérico

Envío En Proceso de Upload
Envío Recibido
Rechazado por Error en Schema
Schema Validado
Rechazado por Firma de Sobre
Firma de Sobre Validada
Error en Carátula
Carátula OK
Validación de Documento
Documento Invalido
Validación de Cesiones
Cesión Invalida
Envío Aceptado
Envío Anulado

Descripción del estado.

Página 11 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.2.2

Función getEstCesion

La respuesta de esta función varía dependiendo del parámetro de entrada opcional “IdCesion”. En el
caso en que se incluya, la respuesta entrega detalles de la cesión, en caso de existir. En el caso que no
se incluya, la respuesta solo informa en la sección RESP_HDR, el estado del documento (cedido o no).
a. Respuesta detallada (la consulta incluye el parámetro de entrada IdCesion)

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<SII:ESTADO>0</SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY>
<RUT_TENEDOR>2-7</RUT_TENEDOR>
<FECHA_ULT_ANOT>2005-05-04 18:13:06</FECHA_ULT_ANOT>
<DEC_JURADA>EXISTE</DEC_JURADA>
</SII:RESP_BODY>
</SII:RESPUESTA>

Donde:
Campo
RUT_TENEDOR
FECHA_ULT_ANOT
RUT_COBRANZA
DIR_COBRANZA
DEC_JURADA

Tipo
String numérico
String Alfanumérico
String Alfanumérico
String Alfanumérico
String Alfanumérico

Detalle
Rut y Dv del tenedor actual del documento.
Fecha última anotación en el Registro.
En caso de estar en cobro, Rut y Dv del cobrador.
En caso de estar en cobro, Dirección de Cobranza.
Indica si existe o no una Declaración Jurada asociada.

b. Respuesta General (la consulta NO incluye el parámetro de entrada IdCesion)
<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<SII:ESTADO>0</SII:ESTADO>
<SII:GLOSA>Documento Cedido</SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY/>
</SII:RESPUESTA>

Donde:
Campo
ESTADO

Tipo
String Alfanumérico

GLOSA

String Alfanumérico

Detalle
Resultado de la operación consulta:
0 : si el documento esta cedido
<> 0 : en caso de no existir o no estar cedido.
Descripción del estado.

Página 12 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.2.3

Función getEstCesionRelac

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR>
<SII:ESTADO>0</SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY>
<RUT_TENEDOR>2-7</RUT_TENEDOR>
<FECHA_ULT_ANOT>2005-05-04 18:13:06</FECHA_ULT_ANOT>
<DEC_JURADA>EXISTE</DEC_JURADA>
</SII:RESP_BODY>
</SII:RESPUESTA>

Donde:
Campo
RUT_TENEDOR
FECHA_ULT_ANOT
RUT_COBRANZA
DIR_COBRANZA
DEC_JURADA

Tipo
String numérico
String Alfanumérico
String Alfanumérico
String Alfanumérico
String Alfanumérico

Detalle
Rut y Dv del tenedor actual del documento.
Fecha última anotación en el Registro.
En caso de estar en cobro, Rut y Dv del cobrador.
En caso de estar en cobro, Dirección de Cobranza.
Indica si existe o no una Declaración Jurada asociada.

Página 13 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

3.3 Códigos de Estado
El resultado de los requerimiento pueden arrojar uno de los siguientes valores de Estado:
Estado
0
1
2
3
4
5
6
7
8
9
10
-15

Glosa
Requerimiento recibido OK.
Error de datos.
Error No se encontró información
Error autenticación: Token Inactivo
Error autenticación: Token no existe
Error autenticación.
Error Interno.
Error Interno.
Error Interno.
Error autenticación: No se pueden obtener permisos
Error permisos: Usuario conectado [%s] no tiene permiso
en empresa [%s]
Error permisos: Empresa Relacionada no esta vinculada
con el documento consultado.

Página 14 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

CAPITULO 4
GUIA PARA REALIZAR PRUEBAS
4.1 Prueba del Servicio
Para probar el servicio, se deben seguir los siguientes pasos:
1.- Autenticarse mediante Autenticación Automática con Certificado Digital (CD).
Nota:

El proceso de la Autenticación Automática con CD, permitirá obtener un Token, el cuál es
requerido como parámetro de entrada por el web service wsRPETCConsulta.
Para la implementación de la autenticación, se recomienda ver “Manual del Desarrollador
Autenticación Automática”.

2.- Una vez obtenido el Token, se debe invocar al sitio donde se encuentra el webservice wsDTECorreo,
ejemplo:
Certificación : https://maullin.sii.cl/DTEWS/services/wsRPETCConsulta?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/wsRPETCConsulta?wsdl

3.- Luego, para realizar las pruebas, seleccionar una de las funciones del WS, invocarla pasándole los
parámetros de entrada requeridos.
4.- Verificar respuesta.

Página 15 de 16

WS Consulta de Estado – RPETC
Versión 1.2 – 05/02/2008

REFERENCIAS
Para mayor información sobre temas tratados en este manual, se recomienda visitar:

Documentación WSDL:
http://www.w3.org/TR/wsdl
Herramienta XMLSPY :
http://www.xmlspy.com/features_wsdl.html
Manual del Desarrollador Autenticación Automática :
http://www.sii.cl/factura_electronica/autenticacion.pdf

Página 16 de 16
