---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_ic.pdf
titulo: FORMATO MENSAJE DE RESPUESTA
categoria: factura_electronica
---
FORMATO MENSAJE DE RESPUESTA
A DOCUMENTOS TRIBUTARIOS ELECTRÓNICOS

2005-04-13
Versión 1.0

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

FORMATO RESPUESTA A DOCUMENTOS TRIBUTARIOS ELECTRÓNICOS

ÍNDICE DE CONTENIDO
1.- INSTRUCCIONES GENERALES ....................................................................................................................................................................3
1.1) Referente al Archivo ........................................................................................................................................................................................3
1.2) Zonas del Mensaje de Respuesta....................................................................................................................................................................4
1.3) Instrucciones generales de formato para las Zonas .........................................................................................................................................4
1.4) Códigos de Obligatoriedad ..............................................................................................................................................................................5
2.- Mensaje de Respuesta de Documentos Tributario Electrónicos ....................................................................................................................6
a) Carátula ...........................................................................................................................................................................................................6
b) RECEPCION ENVÍO Detalle de Respuesta a Envíos (Entre 0 y 1000 ocurrencias.) ..................................................................................7
c) RESULTADO DTE. Detalle de Respuesta a Documentos. (Entre 0 y 1000 ocurrencias) ...........................................................................9
d) Firma del Envío ..............................................................................................................................................................................................9

Nota:
Cambios con respecto a la versión anterior de 2004-11-29 sólo en cuanto a textos referentes a ley N°
19.983, de mérito ejecutivo de la factura. (páginas 3 y 9).

Versión 1.0 2004-11-29

Pág. 2 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

1.- INSTRUCCIONES GENERALES
Las empresas autorizadas como emisores electrónicos son también receptores electrónicos y como tales, cada vez que reciban un envío de
DTE de un emisor electrónico autorizado deben generar una respuesta, en el formato establecido por el SII, en la que den cuenta del estado
de la recepción del envío. Adicionalmente, en forma posterior, podrían dar cuenta del estado de aceptación o rechazo de cada uno de los
DTE que componen el envío.
En este documento se describe el contenido que debe tener el mensaje de respuesta que puede utilizarse EXCLUYENTEMENTE para:
•
•

Dar cuenta del estado de la recepción de un envío (Acuse Recibo), o para
Dar cuenta del resultado de la revisión de documentos tributarios electrónicos de parte de un contribuyente.

La respuesta de acuse recibo de envíos puede contener el acuse de recibo de múltiples envíos y en ellos se identifica los folios recibidos en
el envío.
La respuesta acerca del rechazo o aceptación explícita de cada documento puede ser generada en múltiples archivos o en una sola
respuesta dependiendo de los procesos administrativos y autorizaciones al interior de la organización que cada receptor deba realizar para
determinar el estado final, en cuanto a la aceptación o rechazo, de cada uno de los DTEs componentes del envío.
En el caso de rechazo de una factura electrónica, según lo dispuesto por la ley N°19.983 sobre mérito ejecutivo de la factura, se debe
manifestar el rechazo mediante el envío de un mensaje de respuesta del resultado de la revisión de DTE, en el cual se informe expresa y
claramente tal situación en la Glosa de Motivo de Rechazo.
La información debe ser remitida, en el formato XML definido por el SII, al emisor de los documentos tributarios electrónicos y da cuenta de
del estado de su recepción y/o de la respuesta (aceptación o rechazo) que ameritan.
El archivo a entregar deberá cumplir con las especificaciones que se detallan a continuación:

1.1) Referente al Archivo
1. Formato XML definido por el SII.
2. Este archivo se envía al emisor del documento o documentos recibidos.
3. El archivo debe incluir la firma electrónica sobre toda la información, tal como lo establece el schema XML.

Versión 1.0 2004-11-29

Pág. 3 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

1.2) Zonas del Mensaje de Respuesta.
En los Archivos se distinguen las siguientes zonas:

a) Carátula
Contiene datos generales de la información del envío, como identificación del contribuyente que genera la respuesta y de aquél a quién va
dirigida, la fecha de generación y contacto (persona, teléfono o correo) para aclarar dudas. Obligatoriamente debe venir acompañada de un
detalle de Respuesta a Envíos o de un Detalle de Respuesta de Documentos.
El campo Identificador de respuesta es un número único asignado por el contribuyente que genera la respuesta, con el fin de futuras
referencias a ésta. La responsabilidad de este número es del contribuyente que recibe y genera la respuesta, y él determina si lo utiliza como
una secuencia general de todas las respuestas que genera o como un número secuencial por proveedor, o si no lo maneja (y lo utiliza en
cero) dado que recibe muy pocos documentos.

b) Detalle de Respuesta a Envíos (Entre 0 y 1000 ocurrencias.)
En esta Zona se detalla una línea por cada envío del que se acusa recibo. Opcionalmente se pueden indicar documentos específicos del
Envío que no se recibirán por alguno de los motivos que se indican en el detalle.

c) Detalle de Respuesta de Documentos (Entre 0 y 1000 ocurrencias.)
En esta Zona se detalla una línea por cada documento del que se requiere entregar una respuesta de aceptación o rechazo.

d) Firma del Envío.
Firma electrónica digital que avala la integridad de la respuesta y la autenticidad del remitente. Debe realizarse con un certificado digital
válidamente emitido.

1.3) Instrucciones generales de formato para las Zonas
-

Los largos indicados se refieren a tamaño máximo.
En la información de tipo numérica, los decimales se separan con punto y se deben indicar sólo cuando el valor que se desea incluir
contiene decimales significativos.
No deben separarse los miles con carácter alguno.
Todos los valores de montos deben venir en pesos.

En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben ser
reemplazados por la secuencia de escape que el estándar define para dichos caracteres.
Versión 1.0 2004-11-29

Pág. 4 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

1.4) Códigos de Obligatoriedad
1: Dato obligatorio. El dato debe estar siempre.
2: Dato condicional. El dato se registra sólo si está registrado en el documento emitido.
3: Opcional.

OBLIGATORIEDAD POR ZONAS:

ZONA

Código
Obligatoriedad

Observaciones

Carátula

1

Siempre obligatoria

Respuesta a Envíos

2

Respuesta a Documentos

2

Firma

1

Opcional, para dar cuenta
de recepción de archivo(s)
Opcional, para dar cuenta
de resultado de recepción
de documentos
Siempre obligatoria

Versión 1.0 2004-11-29

Pág. 5 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

2.- Mensaje de Respuesta de Documentos Tributario Electrónicos
a) Carátula
N°

NOMBRE DEL CAMPO

Tipo

LARGO
Máx.

OBSERVACIONES GENERALES

1

RUT Contribuyente Responde

ALFA

10

Corresponde al Rut del contribuyente que redacta la respuesta (DE)

1

2

RUT Contribuyente Recibe

ALFA

10

Corresponde al Rut del Contribuyente de quién se recibió envío o documentos. (PARA)

1

3

Identificador Respuesta

NUM

10

Numero único de identificación de la respuesta asignado por el que responde.

1

4

Número de Detalles

NUM

4

Numero de Envíos en Sección de Recepción o Numero de DTEs en Sección de
Resultados DTE, dependiendo de para qué se esté utilizando el mensaje.

1

5

Contacto

ALFA

40

Nombre Persona de Contacto para aclarar dudas

3

6

Teléfono contacto

NUM

40

Teléfono de Persona de Contacto

3

7

Correo contacto

ALFA

40

Correo electrónico de Contacto

3

8

Fecha Generación de Respuesta

ALFA

19

AAAA -MM-DDTHH:MI:SS Fecha-Hora de firma.

1

Versión 1.0 2004-11-29

Obligatoriedad

Pág. 6 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

b) RECEPCION ENVÍO
Detalle de Respuesta a Envíos (Entre 0 y 1000 ocurrencias.)
CAMPO

NOMBRE DEL CAMPO

Tipo

LARGO

OBSERVACIONES

Obligatoriedad

1

Nombre de Archivo

ALFA

80

Nombre del archivo recibido.

1

2

FECHA Recepción Envío

ALFA

10

Fecha y Hora (AAAA -MM-DDTHH:MI:SS)

1

3

Código del Envío

NUM

10

Número único, generado por el receptor de los DTEs, se usa para
identificación futura del envío

1

4

ID del Envío

ALFA

80

Valor del Atributo ID del Tag EnvíoDTE del Envío recibido

1

5

Digest del Envío

ALFA

28

Campo DigestValue de la Firma Digital del Envío recibido

2

6

RUT Emisor del Envío

ALFA

10

Con guión y dígito, sin puntos.
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

1

7

RUT Receptor del Envío

ALFA

10

Con guión y dígito, sin puntos.
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

1

8

Estado Recepción Envío

NUM

2

Se indica un
0: Envío Recibido Conforme.

1

1: Envío Rechazado – Error de Schema
2: Envío Rechazado - Error de Firma
3: Envío Rechazado - RUT Receptor No Corresponde
90: Envío Rechazado - Archivo Repetido
91: Envío Rechazado - Archivo Ilegible
99: Envío Rechazado – Otros
9

Glosa Estado Recepción Envío

ALFA

256

Repetir la glosa respectiva del Estado Recepción. En caso del estado
99 agregar información adicional .

1

10

Numero de Documentos

NUM

4

Numero de Documentos Incluidos en el Envío que se Informan como
Recibidos/No Recibidos

2

Tabla opcional. Se recomienda cuando hay documentos que no se quieren
recibir dentro del Envío por alguno de los motivos indicados mas delante.

2

DOCUMENTOS
ENVÍO

INCLUIDOS

EN

EL

11

Tipo de Documento

NUM

3

Tipo de DTE

1

12

FOLIO – Documento

NUM

10

Folio del DTE

1

13

FECHA Emisión Documento

ALFA

10

Fecha Emisión Contable del DTE (AAAA-MM- DD)

1

14

RUT Emisor del Documento

ALFA

10

Con guión y dígito
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

1

15

RUT Receptor del Documento

ALFA

10

Con guión y dígito
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
Versión 1.0 2004-11-29

1
Pág. 7 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE
entre 0 y 9 o K
16

Monto Total

NUM

18

Monto Total del DTE

1

17

Estado Recepción Documento

NUM

2

Se indica un

1

0: DTE Recibido OK
1: DTE No Recibido - Error de Firma
2: DTE No Recibido - Error en RUT Emisor
3: DTE No Recibido - Error en RUT Receptor
4: DTE No Recibido - DTE Repetido
99: DTE No Recibido - Otros
18

Glosa Observación

ALFA

256

Repetir la glosa respectiva del Estado Recepción. En caso del estado
99 agregar información adicional .

Versión 1.0 2004-11-29

1

Pág. 8 de 9

Servicio de Impuestos Internos
Formato Mensaje de Respuesta a DTE

c) RESULTADO DTE.
Detalle de Respuesta a Documentos. (Entre 0 y 1000 ocurrencias)
CAMPO

NOMBRE DEL CAMPO

Tipo

LARGO

OBSERV ACIONES

Obligatorieda
d

1

Tipo de Documento

NUM

3

Tipo de DTE

1

2

FOLIO – Documento

NUM

10

Folio del DTE

1

3

FECHA Emisión Documento

ALFA

10

Fecha del DTE (AAAA-MM-DD)

1

4

RUT Emisor del Documento

ALFA

10

Con guión y dígito, sin puntos.
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

1

5

RUT Receptor del Documento

ALFA

10

Con guión y dígito , sin puntos.
Cuerpo numérico entre 100.000 y 99 millones, guión y dígito verificador
entre 0 y 9 o K

1

6

Monto Total

NUM

18

Monto Total del DTE

1

7

Código de Envío

ALFA

10

Identificador del Envío en que se recibió el documento.

1

8

Estado

NUM

2

Se indica un

1

0: DTE Aceptado OK
1: DTE Aceptado con Discrepancia.
2: DTE Rechazado
9

Glosa Motivo rechazo o Discrepancia

ALFA

256

Indicar Glosa: ACEPTADO OK, o ACEPTADO CON DISCREPANCIAS, o
RECHAZADO e indicar adicionalmente el motivo de rechazo o
discrepancia cuando corresponda.

1

En caso de realizarse un rechazo de acuerdo a lo indicado en la Ley N°
19.983, sobre mérito ejecutivo de la factura, se deberá señalar expresa y
claramente el motivo de rechazo en esta glosa, haciendo referencia al N°
de Ley mencionada.
10

Código de Motivo
Discrepancia

de

Rechazo

o

NUM

3

Código numérico de rechazo o discrepancia para ser codificado a futuro

2

d) Firma del Envío
N° NOMBRE DEL CAMPO

Tipo

1

ALFA

SIGNATURE

LARGO
Máx.

OBSERVACIONES GENERALES

(*)

Obligatori
edad

Firma del Envío, utilizando un certificado digital emitido válidamente por una
entidad certificadora registrada en el SII. Firma basada en el estándar XML Digital
Signature.

*

1

Versión 1.0 2004-11-29

Pág. 9 de 9
