---
url: https://www.sii.cl/factura_electronica/Webservice_Registro_Reclamo_DTE_V1.2.pdf
titulo: Web Service de Consulta y Registro
categoria: factura_electronica
---
Web Service de Consulta y Registro
Aceptación/Reclamo a DTE recibido

de

Versión 1.2
07/08/2017

Subdirección Informática
Área Factura Electrónica

Web Service de Consulta y Registro de Aceptación/Reclamo a DTE recibido
Introducción
Con motivo de la modificación a ley 19.983, introducida por la Ley 20.956, que señala que el Recibo de las Mercaderías o Servicios Prestados se
debe efectuar dentro de los 8 días a contar de la recepción del DTE, caso contrario se presumirá recibida la mercadería o que los servicios han sido
prestados si es que no se ha Reclamado en contra de su contenido o de la falta total o parcial de la entrega de las mercaderías o de la prestación
del servicio, el SII habilitó en su sitio una aplicación que permite a los contribuyentes relacionados con un DTE (emisor, receptor o tenedor vigente
del DTE) consultar o registrar la aceptación o reclamo a dicho DTE.
El presente documento describe la forma de realizar las mismas acciones que permite la aplicación antes mencionada, en forma automatizada,
utilizando un Web Service. Para utilizar el Web Service es necesario estar previamente autenticado con certificado digital de acuerdo a lo señalado
en http://www.sii.cl/factura_electronica/factura_mercado/autenticacion.pdf

¿Quiénes pueden utilizar el Web Service?
El Representante Legal o usuarios autorizados de la empresa emisora o receptora del documento que se desea Consultar o Aceptar/Reclamar.
Adicionalmente, también tiene acceso al WS el tenedor vigente y sus usuarios autorizados.

WSDL del Web Service
Ambiente de Certificación contribuyentes: https://ws2.sii.cl/WSREGISTRORECLAMODTECERT/registroreclamodteservice?wsdl

Ambiente de Producción: https://ws1.sii.cl/WSREGISTRORECLAMODTE/registroreclamodteservice?wsdl

Nombre Método WS: ingresarAceptacionReclamoDoc
Parámetros de entrada:
N°
NOMBRE DEL CAMPO

1

RUT emisor

Tipo

LARGO
MÁX.

NUM

8

(rutEmisor)

OBSERVACIONES GENERALES

VALIDACIONES

Corresponde al cuerpo numérico del Rut del
contribuyente emisor del documento, sin puntos ni
comas

Valor mínimo 1000. Formato numérico de
ingreso.

Este es el RUT del emisor del documento.
2

DV Emisor

ALFA

1

Digito verificador del cuerpo del RUT de campo RUT
Emisor.

Módulo 11 aplicado al RUT Emisor, en caso de
ser “K”, siempre debe ser mayúscula.

NUM

2

Indica que el documento informado es:

Formato numérico de ingreso.

33: Factura Electrónica.

Se debe revisar si el DTE es del tipo que el
servicio opera.
De otra forma devolver mensaje:
Tipo de documento no corresponde (distinto
de los tipos citados anteriormente).

(dvEmisor)
3

Tipo de Documento
(tipoDoc)

34: Factura No Afecta o Exenta Electrónica.
43: Liquidación Factura Electrónica.
4

Número de Folio
(folio)

NUM

10

Número de folio que identifica el documento
generado por el emisor. (La tripleta Rut Emisor‐Tipo
de Documento y Número de Folios, debe ser única).

Formato numérico de ingreso.

5

Acción Documento
(accionDoc)

ALFA

3

Acción a registrar sobre el documento.
Puede ser:






ACD: Acepta Contenido del Documento
RCD: Reclamo al Contenido del Documento
ERM: Otorga Recibo de Mercaderías o
Servicios
RFP: Reclamo por Falta Parcial de Mercaderías
RFT: Reclamo por Falta Total de Mercaderías

La acción a realizar sea de entre las indicadas
arriba (ACD, ERM, RCD, RFP, RFT), de otra forma
devolver mensaje Acción inválida.
Se debe revisar que el DTE consultado esté
emitido y recibido en el SII desde el 14 de enero
2017 en adelante.
De otra forma devolver mensaje:
Documento no emitido y/o recibido en el SII
desde el 14 de enero de 2017 en adelante.
Si la acción es distinta de CNS (ACD, ERM, RCD,
RFP, RFT)) y la autenticación no corresponde a
Empresa Receptora o Representante Legal o
usuario autorizado de la empresa receptora
(excepto si solo está autorizado a consulta),
devolver mensaje: Acción autorizada sólo para
empresa receptora.
1) Si la fecha‐hora de Anotación está dentro de
los primeros 8 días corridos (contadas desde la
fecha‐hora de recepción del documento en el
SII, registrada en DTE_Control_DTE hasta la
fecha‐hora actual).
Si no tiene grabado ningún registro de eventos
(reclamos o acuses de recibo), o si tiene
grabado solamente eventos distintos de ACD,
ERM, RCS, RFP y RFT:
Grabar el evento cualquiera solicitado.
Mensaje: Acción completada OK.

Si tiene una anotación previa de Reclamo (RCD,
RFP, RFT).
Si el evento a grabar es ERM, NO GRABARLO.
Mensaje: No se puede acusar recibo de
mercadería de DTE previamente reclamado
por XXX (RCD, RFP, RFT).
Si el evento a grabar es cualquiera de Reclamo
válido de grabar con el WebService (RCD, RFP,
RFT), distinto de los reclamos anteriores.
GRABARLO.
Mensaje: Acción completada OK.
Si el evento a grabar es uno de Reclamo válido
de grabar con el WebService que ya está
previamente grabado. NO GRABARLO.
Mensaje: Evento previamente registrado.
Si el evento a grabar es ACD. NO GRABARLO.
Mensaje: No se puede dar por aceptado DTE
previamente reclamado por XXX (RCD, RFP,
RFT).
Si tiene anotación previa ACD.
Si el evento a grabar es ERM, GRABARLO.
Mensaje: Acción completada OK.
Si el evento a grabar es cualquiera de Reclamo
válido de grabar con el WebService (RCD, RFP,
RFT). NO GRABARLO.
Mensaje: No se puede reclamar DTE
previamente aceptado.
Si el evento a grabar es ACD. NO GRABARLO.
Mensaje: Evento registrado previamente.

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

OBSERVACIONES GENERALES

VALIDACIONES

Si tiene anotación previa ERM.
Si el evento a grabar es ACD. GRABARLO.
Mensaje: Acción completada OK.
Si el evento a grabar es cualquiera de Reclamo
válido de grabar con el WebService (RCD, RFP,
RFT). NO GRABARLO.
Mensaje: No se puede reclamar DTE
previamente registrado como que acuso
recibo de mercadería.
Si el evento a grabar es ERM. NO GRABARLO.
Mensaje: Evento registrado previamente.
2) Si la fecha‐hora de Anotación es después de
los primeros 8 días corridos (contadas desde la
fecha‐hora de recepción del documento en el
SII, registrada en DTE_CONTROL_DRTE hasta la
fecha‐hora actual).
PASADOS 8 DÍAS NO SE PUEDEN INCORPORAR
EVENTOS.
Mensaje: Pasados 8 días después de la
recepción no es posible registrar reclamos o
eventos.

Parámetros de salida:
NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

OBSERVACIONES GENERALES

VALIDACIONES

1

Código de Respuesta

NUM

2

Corresponde a resultado de la transacción:
0: Acción Completada OK.
1: Rut Emisor Erróneo.
2: Número de Folio Erróneo.
3: Tipo de documento no corresponde.
4: Acción inválida.
5: DTE ya está reclamado por XXX);
Donde XXX, es el tipo de evento de reclamo que se
haya registrado (RFP, RFT, RCD)
6: No se puede acusar recibo de mercadería de DTE
previamente reclamado por XXX);
Donde XXX, es el tipo de evento de reclamo que se
haya registrado (RFP, RFT, RCD)
7: Evento registrado previamente.
8: Pasados 8 días después de la recepción no es
posible registrar reclamos o eventos.
9: No existen registros de acuerdo a los parámetros
ingresados.
10: Documento no emitido y/o recibido en el SII desde
el 14 de Enero de 2017 en adelante.
11: No se puede reclamar DTE previamente aceptado.
12: No se puede dar por aceptado DTE previamente
rechazado por XXX);

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

OBSERVACIONES GENERALES

VALIDACIONES

Donde XXX, es el tipo de evento de reclamo que se
haya registrado (RFP, RFT, RCD)
13: No se puede reclamar DTE previamente registrado
como que acuso recibo mercadería.
14: Acción autorizada sólo para empresa receptora o
emisora.
15: Listado de eventos del documento.
16: Documento no presenta eventos de reclamos o
acuse de recibo.
17: Acción autorizada solo para empresa receptora.
18: Documento no ha sido recibido.
19: Reclamo de mercaderías ya realizado.
‐1: Error Interno. Rut Receptor del Documento debe
reintentar enviar la transacción más tarde.
2

Descripción Respuesta

ALFA

70

Describe el tipo de error catalogado con algunos de los
códigos enunciados anteriormente.

Observaciones:
1.

Si nuestro servicio esta abajo o si el contribuyente receptor, tiene problemas de comunicación para realizar sus aceptaciones de documentos o reclamos,
debe reintentar, enviar más tarde.

Nombre Método WS: listarEventosHistDoc
Parámetros de entrada:

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

1

RUT emisor

NUM

8

(rutEmisor)

OBSERVACIONES GENERALES

VALIDACIONES

Corresponde al cuerpo numérico del Rut del
contribuyente emisor del documento, sin puntos ni
comas

Valor mínimo 1000. Formato numérico de
ingreso.

Este es el RUT del emisor del documento.
2

DV Emisor

ALFA

1

Digito verificador del cuerpo del RUT de campo RUT
Emisor.

Módulo 11 aplicado al RUT Emisor, en caso de
ser “K”, siempre debe ser mayúscula.

NUM

2

Indica que el documento informado es:

Formato numérico de ingreso.

33: Factura Electrónica.

Se debe revisar si el DTE es del tipo que el
servicio opera.
De otra forma devolver mensaje:
Tipo de documento no corresponde (distinto
de los tipos citados anteriormente).

(dvEmisor)
3

Tipo de Documento
(tipoDoc)

34: Factura No Afecta o Exenta Electrónica.
43: Liquidación Factura Electrónica.
4

Número de Folio
(folio)

NUM

10

Número de folio que identifica el documento
generado por el emisor. (La tripleta Rut Emisor‐Tipo
de Documento y Número de Folios, debe ser única).

Formato numérico de ingreso.

Parámetros de salida:

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

1

Código de Respuesta

NUM

2

OBSERVACIONES GENERALES

Corresponde a resultado de la transacción:
1: Rut Emisor Erróneo.
2: Número de Folio Erróneo.
3: Tipo de documento no corresponde.
8: Pasados 8 días después de la recepción no es
posible registrar reclamos o eventos.
10: Documento no emitido y/o recibido en el SII desde
el 14 de Enero de 2017 en adelante.
14: Acción autorizada sólo para empresa receptora o
emisora.
15: Listado de eventos del documento.
16: Documento no presenta eventos de reclamos o
acuse de recibo
17: Acción autorizada solo para empresa receptora.
18: Documento no ha sido recibido.

VALIDACIONES

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

2

Descripción Respuesta

ALFA

70

OBSERVACIONES GENERALES

Describe el tipo de error catalogado con algunos de los
códigos enunciados anteriormente. Además, incluye
eventos no registrados por el WS:
NCA: Recepción de NC de anulación que referencia al
documento.
ENC: Recepción de NC, distinta de anulación, que
referencia al documento.

VALIDACIONES

Nombre Método WS: consultarDocDteCedible
Parámetros de entrada:
N°
NOMBRE DEL CAMPO

1

RUT emisor

Tipo

LARGO
MÁX.

NUM

8

(rutEmisor)

OBSERVACIONES GENERALES

VALIDACIONES

Corresponde al cuerpo numérico del Rut del
contribuyente emisor del documento, sin puntos ni
comas

Valor mínimo 1000. Formato numérico de
ingreso.

Este es el RUT del emisor del documento.
2

DV Emisor

ALFA

1

Digito verificador del cuerpo del RUT de campo RUT
Emisor.

Módulo 11 aplicado al RUT Emisor, en caso de
ser “K”, siempre debe ser mayúscula.

NUM

2

Indica que el documento informado es:

Formato numérico de ingreso.

33: Factura Electrónica.

Se debe revisar si el DTE es del tipo que el
servicio opera.
De otra forma devolver mensaje:
Tipo de documento no corresponde (distinto
de los tipos citados anteriormente).

(dvEmisor)
3

Tipo de Documento
(tipoDoc)

34: Factura No Afecta o Exenta Electrónica.
43: Liquidación Factura Electrónica.
4

Número de Folio
(folio)

NUM

10

Número de folio que identifica el documento
generado por el emisor. (La tripleta Rut Emisor‐Tipo
de Documento y Número de Folios, debe ser única).

Formato numérico de ingreso.

Parámetros de salida:

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

1

Código de Respuesta

NUM

2

OBSERVACIONES GENERALES

Corresponde a resultado de la transacción:
1: Rut Emisor Erróneo.
2: Número de Folio Erróneo.
10: Documento no emitido y/o recibido en el SII desde
el 14 de Enero de 2017 en adelante.
18: Documento no ha sido recibido.
20: Tipo de documento no es cedible.
21: DTE No cedible, referenciado por nota de crédito
de anulación del emisor dentro de los primeros 8 días
22: No existe registro de reclamo o de recepción de
mercadería o servicios.
23: DTE Cedible, sin reclamos
24: DTE No Cedible, DTE reclamado por el receptor
25: DTE Cedible, habiendo pasado 8 días se entiende
dado acuse de recibo

2

Descripción Respuesta

ALFA

70

Describe el tipo de error catalogado con algunos de los
códigos enunciados anteriormente.

VALIDACIONES

Nombre Método WS: consultarFechaRecepcionSii
Parámetros de entrada:

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

1

RUT emisor

NUM

8

(rutEmisor)

OBSERVACIONES GENERALES

VALIDACIONES

Corresponde al cuerpo numérico del Rut del
contribuyente emisor del documento, sin puntos ni
comas

Valor mínimo 1000. Formato numérico de
ingreso.

Este es el RUT del emisor del documento.
2

DV Emisor

ALFA

1

Digito verificador del cuerpo del RUT de campo RUT
Emisor.

Módulo 11 aplicado al RUT Emisor, en caso de
ser “K”, siempre debe ser mayúscula.

NUM

2

Indica que el documento informado es:

Formato numérico de ingreso.

33: Factura Electrónica.

Se debe revisar si el DTE es del tipo que el
servicio opera.

(dvEmisor)
3

Tipo de Documento
(tipoDoc)

34: Factura No Afecta o Exenta Electrónica.
43: Liquidación Factura Electrónica.
4

Número de Folio
(folio)

NUM

10

Número de folio que identifica el documento
generado por el emisor. (La tripleta Rut Emisor‐Tipo
de Documento y Número de Folios, debe ser única).

Formato numérico de ingreso.

Parámetros de salida:

N°

NOMBRE DEL CAMPO

Tipo

LARGO
MÁX.

1

Fecha Recepción SII

VARC
HAR

100

OBSERVACIONES GENERALES

Corresponde a la fecha de recepción del documento
en el SII.

VALIDACIONES

Anexo : Ejemplos de ingreso de evento de un documento DTE y consulta de eventos del
documento
Nombre Método WS: ingresarAceptacionReclamoDoc

Nombre Método WS: listarEventosHistDoc

Nombre Método WS: consultarDocDteCedible

Método WS: consultarFechaRecepcionSii

Tabla de Modificaciones

Versión Fecha

Autor

Descripción

1.0

21/12/2016

CV

Versión Inicial

1.1

16-06-2017

CV

Se agrega método consultarFechaRecepcionSii

1.2

07-08-2017

CV

Describe eventos no registrados por el WS y
entregados en lista de eventos.
