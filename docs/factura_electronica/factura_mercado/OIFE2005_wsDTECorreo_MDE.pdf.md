---
url: https://www.sii.cl/factura_electronica/factura_mercado/OIFE2005_wsDTECorreo_MDE.pdf
titulo: Manual de Desarrollador Externo
categoria: factura_electronica
---
Manual de Desarrollador Externo
Solicitud Reenvío de Correo Validación DTE

Oficina Factura Electrónica
Subdirección Informática
Servicio Impuestos Internos
Fecha:11/05/2007

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

INDICE
INTRODUCCIÓN .................................................................................................................................3
CAPITULO 1........................................................................................................................................4
OBJETIVOS Y CARACTERISTICAS ..................................................................................................4
1.1 OBJETIVOS DE LA APLICACIÓN .......................................................................................................4
1.2 CARACTERÍSTICA DE LA APLICACIÓN ..............................................................................................4
CAPITULO 2........................................................................................................................................5
WSDL DE WSDTECORREO .................................................................................................................5
2.1 GRAMÁTICA DEL WSDL...............................................................................................................5
2.1.1 WSDL de wsDTECorreo ...................................................................................................5
CAPITULO 3........................................................................................................................................6
DETALLE DE PARÁMETROS DEL SERVICIO ...................................................................................6
3.1 PARÁMETROS DE E NTRADA ..........................................................................................................6
3.1.1 Ejemplo Real Parámetros de Entrada Formato WSDL ........................................................6
3.2 PARÁMETROS DE SALIDA .............................................................................................................7
3.2.1 Ejemplos de Salida Formato WSDL ...................................................................................7
3.3 VALORES DE SALIDA ...................................................................................................................8
3.4 VALORES DE ESTADO PARA SALIDAS CON ERROR ..........................................................................8
3.4.1 Errores de Datos: .............................................................................................................8
3.4.2 Errores por Autenticación: .................................................................................................8
3.4.3 Otros Errores: ..................................................................................................................8
CAPITULO 4........................................................................................................................................9
GUIA PARA REALIZAR PRUEBAS ................................ ................................ ................................ ....9
4.1 PRUEBA DEL S ERVICIO ................................................................................................................9
REFERENCIAS ................................................................................................................................. 10

Página 2 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

INTRODUCCIÓN

El servicio wsDTECorreo, forma parte del proyecto Documentos Tributarios Electrónicos (DTE), y
corresponde a un servicio que permite a las empresas (contribuyentes) solicitar en forma automática al SII
el reenvío de los correos con diagnostico de validación DTE para trackids específicos.
Este documento está dirigido a quienes tengan la misión de utilizar y probar este servicio.
La forma de acceder a este servicio es a través de WSDL (Web Services Definition Language). Este es un
lenguaje descriptor, basado en XML, que permite conocer en forma abstracta, la gramática de los
componentes de un webservice (ubicación, formato, tipos de datos, servicios, funciones, parámetros de
entrada, salida, etc).
El WSDL que se detalla en este documento apunta al ambiente de certificación del SII, sin embargo este
ambiente es una copia fiel del ambiente de producción.
La ubicación del WSDL de wsDTECorreo es:
Certificación : https://maullin.sii.cl/DTEWS/services/wsDTECorreo?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/wsDTECorreo?wsdl

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

Página 3 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

CAPITULO 1
OBJETIVOS Y CARACTERISTICAS
1.1 Objetivos de la aplicación
El servicio wsDTECorreo, forma parte del proyecto Documentos Tributarios Electrónicos (DTE), y
corresponde a un servicio que permite a las empresas (contribuyentes) solicitar en forma automática al SII
el reenvío de los correos con diagnostico de validación DTE para trackids específicos.

1.2 Característica de la aplicación
ü

El servicio wsDTECorreo es de tipo “Consulta-Respuesta”

ü

Es una aplicación B2B.

ü

Esta aplicación puede ser utilizada por aquellos usuarios habilitados para su uso.

ü

Para solicitar un reenvío de correo el contribuyente autenticado, debe tener representación sobre la
empresa emisora de los documentos.

Página 4 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

CAPITULO 2
WSDL de wsDTECorreo

2.1 Gramática del WSDL
El siguiente cuadro muestra el WSDL del webservice wsDTECorreo.

2.1.1

WSDL de wsDTECorreo

<?xml version="1.0" encoding="UTF-8" ?>
- <wsdl:definitions targetNamespace="http://DefaultNamespace"
xmlns="http://schemas.xmlsoap.org/wsdl/"
xmlns:apachesoap="http://xml.apache.org/xml-soap"
xmlns:impl="http://DefaultNamespace"
xmlns:intf="http://DefaultNamespace"
xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
- <wsdl:message name="reenvioCorreoRequest">
<wsdl:part name="Token" type="xsd:string" />
<wsdl:part name="RutEmpresa" type="xsd:string" />
<wsdl:part name="DvEmpresa" type="xsd:string" />
<wsdl:part name="TrackId" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getEnvRequest" />
+ <wsdl:message name="getVersionMayorResponse">
- <wsdl:message name="reenvioCorreoResponse">
<wsdl:part name="reenvioCorreoReturn" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionMenorRequest" />
<wsdl:message name="getVersionMayorRequest" />
+ <wsdl:message name="getEnvResponse">
<wsdl:message name="getVersionPatchRequest" />
+ <wsdl:message name="getVersionMenorResponse">
+ <wsdl:message name="getVersionPatchResponse">
+ <wsdl:portType name="wsDTECorreo">
+ <wsdl:binding name="wsDTECorreoSoapBinding"
type="impl:wsDTECorreo">
+ <wsdl:service name="wsDTECorreoService">
</wsdl:definitions>
Figura 2-1

Página 5 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

CAPITULO 3
DETALLE DE PARÁMETROS DEL SERVICIO

3.1 Parámetros de Entrada
Los parámetros de entrada requeridos por el servicio, se detallan en el siguiente ejemplo:

3.1.1

Ejemplo Real Parámetros de Entrada Formato WSDL

<SOAP- ENV:Envelope xmlns:SOAP-ENV ="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema -instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<S O A P- ENV:Body >
<m:reenvioCorreo xmlns:m="http://DefaultNamespace" SOAPENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<Token xsi:type ="xsd:string">String</Token>
<RutEmpresa xsi:type ="xsd:string">String</RutEmpresa>
<DvEmpresa xsi:type ="xsd:string">String</DvEmpresa>
<TrackId xsi:type="xsd:string">String</TrackId>
</m:reenvioCorreo >
</S O A P- ENV:Body >
</SOAP- ENV:Envelope>

Figura 3-1
Donde:
Campo
Token

Tipo
String Alfanumérico

Largo
1-40

RutEmpresa
DvEmpresa
TrackId

String numérico
String Alfanumérico
String numérico

1-8
1-1
1-10

Detalle
El Token es un identificador único que
identifica a un contribuyente , el cual es
almacenado y enviado al cliente en el
Header del
Response de la
Autenticación
Automática
con
Certificado Digital (CD), y permite la
búsqueda de toda la información
relacionada a una sesión del cliente.
El contribuyente autenticado debe tener
representación
sobre
la
empresa
emisora.
Rut de la Empresa emisora del envio
Dv del Emisor.
Trackid al que se le solicita el reenvío.
Tabla 3-1

Página 6 de 10

Obligatorio
S

S
S
S

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

3.2 Parámetros de Salida
La salida del servicio corresponden a un “string” XML codificado, por lo tanto, es necesario que el
programa cliente sea capaz de decodificar el “string” y llevarlo a formato original, los campos de retorno
son: ESTADO y GLOSA, ERR_CODE, GLOSA_ERR, NUM_ATENCIÓN.

3.2.1

Ejemplos de Salida Formato WSDL

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema ">
<SII:RESP_HDR>
<SII:ESTADO>0 </SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

Figura 3-2 Respuesta Correcta

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema ">
<SII:RESP_HDR>
<SII:ESTADO>105</SII:ESTADO>
<SII:GLOSA>TRACKID NO EXISTE</SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

Figura 3-3 Respuesta con error

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RES P_HDR>
<SII:ESTADO>114</SII:ESTADO>
<SII:GLOSA >ENVIO NO HA CONCLUIDO VALIDACION</SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

Figura 3-4 Respuesta con error, no existe correo para reenvio
Donde:
Campo
ESTADO

String

Tipo

Largo
1-3

GLOSA

String Alfanumérico

1-40

Detalle
Código Estado de la
operación
En caso de Error indica
una glosa descriptiva del
error.

Tabla 3-2

Página 7 de 10

Obligatorios
S
S

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

3.3 Valores de Salida
El resultado del requerimiento puede arrojar uno de los siguientes valores:
Estado
0
<> 0

Tipo
String
String

Largo
1-3
1-3

Glosa
Requerimiento recibido OK.
Ha ocurrido un error.

Tabla 3-3

3.4 Valores de estado para salidas con ERROR

3.4.1

Errores de Datos:

El resultado de la consulta puede arrojar uno de los siguientes Estados de Error:
Estado
101

String

Tipo

Largo
1-3

102
105
106

String
String
String

1-3
1-3
1-3

114

String

1-3

Glosa
Error en dígito verificador del Rut de la
empresa.
Faltan datos de entrada
Error TrackId no existe
Usuario autenticado no tiene permisos sobre
Empresa.
Envío solicitado no ha concluido su validación,
por lo tanto no existe correo.

Tabla 3-4

3.4.2

Errores por Autenticación:

Estado
104

Tipo
String numérico

Largo
1-3

Glosa
Token Inactivo o No Existe

Tabla 3-5

3.4.3

Otros Errores:

Estado
103
107
108
110
111
112
113

Tipo
String
String
String
String
String
String
String

Largo
1-3
1-3
1-3
1-3
1-3
1-3
1-3

Glosa
Error Interno.
Error Interno
Error Interno
Error Interno
Error Interno
Error Interno
Error Interno

Tabla 3-6

Página 8 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

CAPITULO 4
GUIA PARA REALIZAR PRUEBAS

4.1 Prueba del Servicio
Para probar el servicio, se deben seguir los siguientes pasos:
1.- Autenticarse mediante Autenticación Automática con Certificado Digital (CD).
Nota:

El proceso de la Autenticación Automática con CD, permitirá obtener un Token, el cuál es
requerido como parámetro de entrada por el webservice wsDTECorreo.
Para la implementación de la autenticación, se recomienda ver “Manual del Desarrollador
Autenticación Automática”.

2.- Una vez obtenido el Token, se debe invocar al sitio donde se encuentra el webservice wsDTECorreo,
ejemplo:
Certificación : https://maullin.sii.cl/DTEWS/services/wsDTECorreo?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/wsDTECorreo?wsdl

3.- Luego, para realizar las pruebas, al WS invocado, se le deben pasar los parámetros de entrada
requeridos por la función reenvioCorreo, estos son: Token, RutEmpresa, DvEmpresa, TrackId.
4.- Como respuesta del WS se obtiene un XML con los siguientes tags:
ü
ü

ESTADO
GLOSA (solo en caso de error)

Página 9 de 10

WS para Reenvío de Correos con Diagnóstico de Validación DTE
Versión 1.0 – 10/01/2006

REFERENCIAS
Para mayor información sobre temas tratados en este manual, se recomienda visitar:

Documentación WSDL:
http://www.w3.org/TR/wsdl
Herramienta XMLSPY :
http://www.xmlspy.com/features_wsdl.html
Manual del Desarrollador Autenticación Automática :
http://www.sii.cl/factura_electronica/autenticacion.pdf

Página 10 de 10
