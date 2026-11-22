---
url: https://www.sii.cl/factura_electronica/factura_mercado/inst_set_pruebas.pdf
titulo: INSTRUCCIONES PARA LA CONSTRUCCIÓN DE DOCUMENTOS
categoria: factura_electronica
---
INSTRUCCIONES PARA LA CONSTRUCCIÓN DE DOCUMENTOS
ELECTRÓNICOS CON LOS DATOS DEL SET DE PRUEBAS.

TRIBUTARIOS

INTRODUCCIÓN
Este es el primer paso del proceso de certificación para convertirse en emisor, autorizado
por el SII, de Factura Electrónica.
Varias de las actividades que debe efectuar el Usuario Administrador para completar esta
etapa se realizan a través de las opciones del ambiente de Certificación (también conocido
como ambiente de pruebas), por lo que recomendamos obtener el Manual de Operación
desde el submenú “Documentación para Empresas Autorizadas”. En dicho Manual se
describen las opciones disponibles en el ambiente de Certificación que el SII ha habilitado
para que las empresas postulantes efectúen las pruebas.
En esta primera etapa del proceso de certificación el Usuario Administrador debe enviar al
SII documentos tributarios electrónicos preparados con los datos entregados por el SII en el
Set de Pruebas y generados de acuerdo al formato XML establecido por el SII.
I.- RESPECTO A LA CONFECCIÓN DE CADA DOCUMENTO
1.
2.
3.
4.

Ud. ha recibido un conjunto de datos que debe utilizar para confeccionar los
documentos de prueba.
Previo a emitir los documentos debe solicitar folios por tipo de documento.
Debe generar un documento DTE para cada caso incluido en el SET.
Para generar cada documento del SET:
a. Asigne un folio autorizado.
b. Agregue un Rut receptor de un cliente existente. Utilice RUT distintos para las
distintas facturas.
c. Agregue fecha del día.
d. En la glosa del ítem debe anotar exactamente lo indicado en el caso; debe incluir
acentos, ñ u otros que se indiquen. No debe agregar líneas adicionales de ítems.
e. Debe registrar los valores de cantidad y precio unitario que se indiquen en cada
caso.
- En el Caso de las Notas de Crédito por devolución de mercaderías, el precio
unitario debe corresponder al precio de la Factura original.
- En el caso de Notas de Crédito por diferencia de precio, la diferencia se
debe aplicar a todas las unidades del ítem respectivo
f. Las líneas de detalle deben ir en el orden especificado.
g. Utilice la tasa del IVA que corresponda a la fecha de emisión del DTE.

5.

En el sector encabezado: Calcule los valores de Monto Neto, Exento y otros, que
correspondan según el caso. Asegúrese de incorporar todos los datos que son
obligatorios, según el tipo de documento y el caso.

6.

En el sector de referencias: En la primera línea de referencia de cada DTE del set de
prueba debe indicar:
-

El texto “SET“ como “Tipo de Documento de Referencia” y
El texto “CASO xxxxx-x” en el campo “Razón referencia”

Como ejemplo, si ha confeccionado un DTE del Set de prueba, cuyo N° de caso es
1062-1,

Ud. debe agregar en el campo correspondiente a “tipo de documento de referencia”
la palabra SET y en el campo “Razón referencia” el texto CASO 1062-1
Las otras referencias que sea preciso agregar dado el tipo de documento
correspondiente a la prueba, deben ir a partir de la línea 2.
II.- RESPECTO AL ENVIO DEL SET DE PRUEBAS
Mientras realice las pruebas, puede enviar los documentos en tantos envíos como desee,
pero en el envío de los Set reportados para la Revisión del SII, debe incluir todos los
documentos de los Sets de pruebas y en el mismo orden en que le fueron entregados.
En la carátula de cada envío debe indicar:
• Rut del Contribuyente
• Rut del firmante autorizado (quien envía)
• Rut del Receptor. Indicar Rut 60803000-K, que corresponde al RUT del SII
• Número y Fecha de Resolución: Indique el número y fecha que está publicado en
los datos de su empresa en el ambiente de certificación
• Tipos de documentos enviados y cantidad de cada uno
Si envía un documento del Set de prueba y éste es aceptado con reparos, deberá usar un
folio distinto para enviar el documento nuevamente, ya que en caso contrario el documento
será rechazado por folio duplicado.

III.- RESPECTO A LA CONFECCIÓN DEL ARCHIVO INFORMACIÓN ELECTRONICA DE
VENTAS (IEV)
Debe confeccionar este Libro, incorporando sólo la información de los documentos que son
parte de sus SET de prueba y que han sido reportados para revisión. En el Archivo IEV, se
deben incluir Facturas, Notas de Crédito y Notas de Débito electrónicas.
1.

Zona Carátula: Debe indicar la siguiente información:
Rut del Contribuyente
Rut del firmante autorizado
Período Tributario: Los documentos del SET de prueba deben ser emitidos de forma
que sean todos del mismo período tributario. En la carátula deberá indicarse ese
período tributario.
• Número y Fecha de Resolución: Indique el número y fecha que está publicado en los
datos de su empresa en el ambiente de certificación
• Tipo de Operación. Venta
• Tipo de Libro: ESPECIAL
• Tipo de envío: TOTAL
• Folio Notificación: Registrar 1
•
•
•

2.
3.

Zona Resumen período: Debe entregar totalizados los campos por tipo de documento
Zona Detalle: Debe registrar para cada documento del SET de Prueba
• Los datos contenidos del documento

•

Agregar datos obligatorios en caso que se requiera. Verificar el documento “Formato
Información Electrónica de Compras y Ventas” .

IV.- RESPECTO A LA CONFECCIÓN DEL ARCHIVO INFORMACIÓN ELECTRONICA DE
COMPRAS
Ud. debe confeccionar este Libro, incorporando sólo la información de los documentos que
se le han entregado en el SET de prueba de Libro de Compras.
1.

Zona Carátula: Debe indicar la siguiente información:
Rut del Contribuyente
Rut del firmante autorizado
Período Tributario: Se asume que el período tributario es el mismo del Libro de
Ventas.
• Número y Fecha de Resolución: Indique el número y fecha que está publicado en los
datos de su empresa en el ambiente de certificación
• Tipo de Operación. Compra
• Tipo de Libro: ESPECIAL
• Tipo de envío: TOTAL
• Folio Notificación: Registrar 2
•
•
•

2.
3.

Zona Resumen período: Debe entregar totalizados los campos por tipo de documento
Zona Detalle: Debe registrar la información que se le ha entregado en el Set respectivo
Considerar los datos informados en el Set de prueba de Compras.
Calcular los datos que se requieran para completar la información necesaria de un
documento de compra; se deberá completar, según sea el caso, el Monto Neto,
Exento, tasa de IVA, IVA, Monto Total.
• Agregar datos del emisor del documento para lo cual se deberán usar Rut válidos.
• Agregar otros datos obligatorios que se requieran según el documento y sus
características. Verificar el documento “Formato Información Electrónica de Compras
y Ventas”
•
•
