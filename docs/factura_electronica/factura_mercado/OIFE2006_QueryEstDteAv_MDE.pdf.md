---
url: https://www.sii.cl/factura_electronica/factura_mercado/OIFE2006_QueryEstDteAv_MDE.pdf
titulo: Manual de Desarrollador Externo
categoria: factura_electronica
---
Manual de Desarrollador Externo
Consulta Avanzada Estado de DTE

Oficina Informática Factura Electrónica
Subdirección Informática
Servicio Impuestos Internos
Versión : 1.0
Fecha
: 03/05/2007

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

INDICE
CONTROL DE VERSIONES .................................................................................................................2
INTRODUCCIÓN .................................................................................................................................3
CAPITULO 1........................................................................................................................................4
OBJETIVOS Y CARACTERISTICAS ..................................................................................................4
1.1 OBJETIVOS DE LA APLICACIÓN .......................................................................................................4
1.2 CARACTERÍSTICA DE LA APLICACIÓN ..............................................................................................4
CAPITULO 2........................................................................................................................................5
WSDL DE Q UERY ESTD TEA V ...............................................................................................................5
2.1 GRAMÁTICA DEL WSDL...............................................................................................................5
CAPITULO 3........................................................................................................................................6
DETALLE DE PARÁMETROS DE LA FUNCION GET E ST DTE AV .............................................................6
3.1 PARÁMETROS DE E NTRADA ..........................................................................................................6
3.2 PARÁMETROS DE SALIDA .............................................................................................................7
3.2.1 Sección RESP_HDR...........................................................................................................7
3.2.2 Sección RESP_BODY.........................................................................................................7
3.3 VALORES DE SALIDA ...................................................................................................................8
3.3.1
RESP_HDR/ESTADO......................................................................................................8
3.3.2
RESP_BODY/RECIBIDO ...............................................................................................8
3.3.3
RESP_BODY/ESTADO ...................................................................................................8
3.4 EJEMPLOS DE S ALIDA ................................................................................................................9
3.4.1 Documento Recibido y Datos Coinciden ................................ ................................ ............9
3.4.2 Documento Recibido y Datos No Coinciden .......................................................................9
3.4.3 Error de Autenticación ......................................................................................................9
3.4.4 Error en Parámetros de Entrada...................................................................................... 10
CAPITULO 4...................................................................................................................................... 11
GUIA PARA REALIZAR PRUEBAS................................ ................................ ................................ .. 11
4.1 PRUEBA DEL S ERVICIO .............................................................................................................. 11
REFERENCIAS ................................................................................................................................. 12

Subdirección de Informática – Oficina Factura Electrónica
Página : 1 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

CONTROL DE VERSIONES
Versión

Fecha

1.0

24-07-2006

Motivo
Versión Inicial.

Subdirección de Informática – Oficina Factura Electrónica
Página : 2 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

INTRODUCCIÓN
El servicio QueryEstDteAv, forma parte del proyecto Documentos Tributarios Electrónicos (DTE), y
corresponde a un servicio que permite a las empresas (contribuyentes) consultar en forma automática por
el estado en que se encuentra un DTE enviado al SII, además de corroborar los datos asociados al
documento.
La forma de acceder a este servicio es a través de WSDL 1 (Web Services Definition Language).
El WSDL que se detalla en este documento apunta al ambiente de certificación del SII, sin embargo este
ambiente es una copia fiel del ambiente de producción.
La ubicación del WSDL de QueryEstDteAv es:
Certificación : https://maullin.sii.cl/DTEWS/services/QueryEstDteAv?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/QueryEstDteAv?wsdl

Una vez que el cliente conoce el WSDL del webservice, debe construir un Request en formato SOAP
(Simple Object Access Protocolo), para luego enviarlo hacia el proveedor de servicio (SII), previa
Autenticación.
Respecto a la Autenticación, para poder realizar consultas hacia cualquier webservice entregado por el
SII, los clientes deben estar previamente autenticados a través de la AUTENTICACIÓN AUTOMATICA.
Este documento está dirigido a quienes tengan la misión de utilizar y probar este servicio.

Requisitos de uso.
Para poder utilizar este manual, es necesario tener previo conocimiento de XML, Web Services y
Certificado Digital.

Recomendaciones.
Se recomienda el uso de la herramienta XMLSPY5 de la Altova ( http://www.altova.com ).

1

WSDL: Lenguaje descriptor, basado en XML, que permite conocer en forma abstracta, la gramática de
los componentes de un web service (ubicación, formato, tipos de datos, servicios, funciones, parámetros
de entrada, salida, etc).
Subdirección de Informática – Oficina Factura Electrónica
Página : 3 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

CAPITULO 1
OBJETIVOS Y CARACTERISTICAS
1.1 Objetivos de la aplicación
El objetivo de este servicio es entregar una herramienta que permita consultar por el estado de un DTE y
corroborar los datos asociados a dicho DTE.

1.2 Característica de la aplicación
ü

El servicio QueryEstDteAv, es de tipo “Consulta-Respuesta”.

ü

Es una aplicación B2B.

ü

Esta aplicación puede ser utilizada por aquellos usuarios habilitados para su uso.

ü

Para realizar una consulta el contribuyente autenticado, debe tener representación sobre la empresa
emisora del documento.

Subdirección de Informática – Oficina Factura Electrónica
Página : 4 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

CAPITULO 2
WSDL de QueryEstDteAv
2.1 Gramática del WSDL
El siguiente cuadro muestra el WSDL del web service QueryEstDteAv.

<?xml version="1.0" encoding="UTF-8" ?>
- <wsdl:definitions targetNamespace="http://DefaultNamespace"
xmlns="http://schemas.xmlsoap.org/wsdl/"
xmlns:apachesoap="http://xml.apache.org/xml-soap"
xmlns:impl="http://DefaultNamespace" xmlns:intf="http://DefaultNamespace"
xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
+ <wsdl:message name="getVersionResponse">
+ <wsdl:message name="getVersionPatchResponse">
+ <wsdl:message name="getVersionMayorResponse">
- <wsdl:message name="getEstDteAvRequest">
<wsdl:part name="RutEmpresa" type="xsd:string" />
<wsdl:part name="DvEmpresa" type="xsd:string" />
<wsdl:part name="RutReceptor" type="xsd:string" />
<wsdl:part name="DvReceptor" type="xsd:string" />
<wsdl:part name="TipoDte" type="xsd:string" />
<wsdl:part name="FolioDte" type="xsd:string" />
<wsdl:part name="FechaEmisionDte" type="xsd:string" />
<wsdl:part name="MontoDte" type="xsd:string" />
<wsdl:part name="FirmaDte" type="xsd:string" />
<wsdl:part name="Token" type="xsd:string" />
</wsdl:message>
- <wsdl:message name="getEstDteAvResponse">
<wsdl:part name="getEstDteAvReturn" type="xsd:string" />
</wsdl:message>
<wsdl:message name="getVersionPatchRequest" />
<wsdl:message name="getVersionMayorRequest" />
+ <wsdl:message name="getVersionMenorResponse">
<wsdl:message name="getVersionMenorRequest" />
<wsdl:message name="getVersionRequest" />
+ <wsdl:portType name ="QueryEstDteAv">
+ <wsdl:binding name="QueryEstDteAvSoapBinding" type="intf:QueryEstDteAv">
+ <wsdl:service name="QueryEstDteAvService">
</wsdl:definitions>

Como se muestra en los recuadros del WSDL, el servicio QueryEstDteAv, tiene la función
getEstDteAv, la que permite realizar la consulta. A continuación se detallan los parámetros de entrada y
la salida de esta función.

Subdirección de Informática – Oficina Factura Electrónica
Página : 5 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

CAPITULO 3
DETALLE DE PARÁMETROS DE LA FUNCION getEstDteAv
3.1 Parámetros de Entrada
Los parámetros de entrada requeridos por el servicio, se detallan en el siguiente cuadro:
<SOAP- ENV:Envelope xmlns:SOAP- ENV ="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAPENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<SOAP-ENV:Body>
<m:getEstDteAv xmlns:m="http://DefaultNamespace" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<RutEmpresa xsi:type="xsd:string">String</RutEmpresa>
<DvEmpresa xsi:type="xsd:string">String</DvEmpresa>
<RutReceptor xsi:type="xsd:string">String</RutReceptor>
<DvReceptor xsi:type="xsd:string">String</DvReceptor>
<TipoDte xsi:type="xsd:string">String</TipoDte>
<FolioDte xsi:type="xsd:string">String</FolioDte>
<FechaEmisionDte xsi:type="xsd:string">String</FechaEmisionDte>
<MontoDte xsi:type="xsd:string">String</MontoDte>
<FirmaDte xsi:type="xsd:string">String</FirmaDte>
<Token xsi:type="xsd:string">String</Token>
</m:getEstDteAv>
</SOAP- ENV:Body>
</SOAP- ENV:Envelope>

Donde:
Campo
RutEmpresa
DvEmpresa
RutReceptor
DvReceptor
TipoDte
FolioDte
FechaEmisionDte

Tipo
String numérico
String Alfanumérico
String numérico
String Alfanumérico
String numérico
String numérico
String Date

Largo
1-8
1-1
1-8
1-1
1-3
1-10
1-10

MontoDte
FirmaDte

String numérico
String Alfanumérico

1-15
1-500

Token

String Alfanumérico

1-40

Detalle
Obligatorio
Rut del Emisor.
S
Dv del Emisor.
S
Rut del Receptor.
S
Dv del receptor.
S
Tipo del DTE.
S
Folio del DTE.
S
Fecha de Emisión del DTE, en formato
S
DD-MM-AAAA.
Monto Total del DTE.
S
Firma del DTE.
S
Corresponde al tag:
DTE/Signature/SignatureValue
del
xml asociado al documento.
Identificador único de autenticación que
S
identifica a un contribuyente. Se obtiene
como respuesta de servicio de
Autenticación
Automática
con
Certificado Digital (CD).

Subdirección de Informática – Oficina Factura Electrónica
Página : 6 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

3.2 Parámetros de Salida
La salida del servicio corresponde a un “string” XML codificado. La respuesta esta organizada en dos
secciones:
ü RESP_HDR
ü RESP_BODY

3.2.1

Sección RESP_HDR

Esta sección entrega el resultado de la operación a través de los campos :
Campo
ESTADO
GLOSA

3.2.2

Tipo
Numérico
String

Largo
1-2
1-238

Detalle
Indica el resultado de la operación
En caso de error, breve descripción del
error

Obligatorio
S
N

Sección RESP_BODY

Esta sección entrega el detalle del estado del documento consultado a través de los campos:
Campo
RECIBIDO

Tipo
String

Largo
1-2

ESTADO
GLOSA
TRACKID
NUMATENCION

String
String
Numérico
String

1-3
1-238
1-20
1-40

Detalle
Indica si el documento fue recibido por el
SII
Estado en que se encuentra
Descripción del estado
Trackid asociado al documento
Numero de Atención asociado a la
consulta

Subdirección de Informática – Oficina Factura Electrónica
Página : 7 de 13

Obligatorio
S
S
S
N
S

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

3.3 Valores de Salida
Algunos de los campos tienen asociado valores codificados, los que se detallan a continuación:

3.3.1

RESP_HDR/ESTADO
ESTADO
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
11
12
13
14

3.3.2

Descripción
Consulta procesada OK.
Token inactivo (expirado)
Token no existe
Error Interno (ver glosa)
Error Interno
Error parámetros de entrada (ver glosa)
Error Interno
Error Interno
Error Interno
Usuario no autorizado en empresa
Error Interno
Error Interno
Error Interno
Error Interno
Error Interno

RESP_BODY/RECIBIDO
RECIBIDO
Descripción
SI
Documento fue recibido por el SII
NO
Documento no ha sido recibido por el SII

3.3.3

RESP_BODY/ESTADO
ESTADO
EMP
TMD
TMC
MMD
MMC
AND
ANC
DOK
DNK
FNA
FAN
FAU

Descripción
Empresa No Autorizada a Emitir Documentos Tributarios Electrónicos
Existe Nota de Débito que Modifica Textos Documento
Existe Nota de Crédito que Modifica Textos Documento
Existe Nota de Débito que Modifica Montos Documento
Existe Nota de Crédito que Modifica Montos Documento
Existe Nota de Débito que Anula Documento
Existe Nota de Crédito que Anula Documento
Documento Recibido por el SII. Datos Coinciden con los Registrados
Documento Recibido por el SII pero Datos NO Coinciden con los
registrados
Documento No Autorizado
Documento Anulado
Documento No Recibido por el SII

Subdirección de Informática – Oficina Factura Electrónica
Página : 8 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

3.4 Ejemplos de Salida
A continuación se muestran algunos ejemplos de salidas.

3.4.1

Documento Recibido y Datos Coinciden

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>0</SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY >
<RECIBIDO>SI</RECIBIDO>
<ESTADO>DOK</ESTADO>
<GLOSA>Documento Recibido por el SII. Datos Coinciden con los Registrados </GLOSA >
<TRACKID>36440</TRACKID>
<NUMATENCION>137416 [25/07/2006 12:08:20] </NUMATENCION>
</SII:RESP_BODY >
</SII:RESPUESTA >

3.4.2

Documento Recibido y Datos No Coinciden

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>0</SII:ESTADO>
</SII:RESP_HDR>
<SII:RESP_BODY >
<RECIBIDO>SI</RECIBIDO>
<ESTADO>DNK</ESTADO>
<GLOSA>Documento Recibido por el SII pero Datos NO Coinciden con los registrados</GLOSA>
<NUMATENCION>137417 [25/07/2006 12:11:03] </NUMATENCION>
</SII:RESP_BODY >
</SII:RESPUESTA >

3.4.3

Error de Autenticación

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>2</SII:ESTADO>
<SII:GLOSA >Token no existe</SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

Subdirección de Informática – Oficina Factura Electrónica
Página : 9 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

3.4.4

Error Autenticación Expirada

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>1</SII:ESTADO>
<SII:GLOSA >Token Inactivo</SII:GLOSA >
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

3.4.5

Error en Parámetros de Entrada

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>5</SII:ESTADO>
<SII:GLOSA >DV Rut Empresa no correspo nde. </SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

3.4.6

Error de Permisos

<?xml version="1.0" encoding="UTF-8"?>
<SII:RESPUESTA xmlns:SII="http://www.sii.cl/XMLSchema">
<SII:RESP_HDR >
<SII:ESTADO>9</SII:ESTADO>
<SII:GLOSA >Usuario no tiene permiso en empresa</SII:GLOSA>
</SII:RESP_HDR>
<SII:RESP_BODY />
</SII:RESPUESTA >

Subdirección de Informática – Oficina Factura Electrónica
Página : 10 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

CAPITULO 4
GUIA PARA REALIZAR PRUEBAS
4.1 Prueba del Servicio
Para probar el servicio, se deben seguir los siguientes pasos:
1.- Autenticarse mediante Autenticación Automática con Certificado Digital (CD).
Nota:

El proceso de la Autenticación Automática con CD, permitirá obtener un Token, el cuál es
requerido como parámetro de entrada por el web service QueryEstDteAv.
Para la implementación de la autenticación, se recomienda ver “Manual del Desarrollador
Autenticación Automática”.

2.- Una vez obtenido el Token, se debe invocar al sitio donde se encuentra el web service
QueryEstDteAv, ejemplo:
Certificación : https://maullin.sii.cl/DTEWS/services/QueryEstDteAv?wsdl
Producción

: https://palena.sii.cl/DTEWS/services/QueryEstDteAv?wsdl

3.- Luego, para realizar las pruebas, al WS invocado, se le deben pasar los parámetros de entrada
requeridos por la función getEstDteAv, estos son: RutEmpresa, DvEmpresa, RutReceptor,
DvReceptor, TipoDte, FolioDte, FechaEmisionDte, MontoDte, FirmaDte, Token.
4.- Como respuesta del WS se obtiene un XML.

Subdirección de Informática – Oficina Factura Electrónica
Página : 11 de 13

WS de Consulta Avanzada del Estado de un DTE
Versión 1.0 – 03/05/2007

REFERENCIAS
Para mayor información sobre temas tratados en este manual, se recomienda visitar:

Documentación WSDL:
http://www.w3.org/TR/wsdl
Herramienta XMLSPY :
http://www.xmlspy.com/features_wsdl.html
Manual del Desarrollador Autenticación Automática :
http://www.sii.cl/factura_electronica/autenticacion.pdf

Subdirección de Informática – Oficina Factura Electrónica
Página : 12 de 13
