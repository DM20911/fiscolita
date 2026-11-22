---
url: https://www.sii.cl/factura_electronica/factura_mercado/formato_dte_202602.pdf
titulo: FORMATO DOCUMENTOS TRIBUTARIOS ELECTRÓNICOS
categoria: factura_electronica
---
FORMATO DOCUMENTOS TRIBUTARIOS ELECTRÓNICOS
2026-02
Versión 2.5

FORMATOS DOCUMENTOS TRIBUTARIOS ELECTRÓNICOS
BITÁCORA DE CAMBIOS ................................................................................................................................................................... 3
1.- INTRODUCCIÓN ............................................................................................................................................................................ 8
2.- CONTENIDO DE FACTURAS Y DOCUMENTOS ASOCIADOS. ................................................................................................... 8
2.1.- Zonas del documento electrónico ............................................................................................................................................. 9
Códigos de Obligatoriedad .......................................................................................................................................................... 10
2.2.- Detalle por Zona ..................................................................................................................................................................... 11
A.- ENCABEZADO ...................................................................................................................................................................... 12
B.- DETALLE DE PRODUCTOS O SERVICIOS ......................................................................................................................... 36
C.- SUBTOTALES INFORMATIVOS ........................................................................................................................................... 43
D.- INFORMACIÓN DE DESCUENTOS O RECARGOS ............................................................................................................ 44
E.- INFORMACIÓN DE REFERENCIA........................................................................................................................................ 45
F.- COMISIONES Y OTROS CARGOS ....................................................................................................................................... 48
G.-TIMBRE ELECTRÓNICO SII DEL DOCUMENTO.................................................................................................................. 49
H.- FECHA Y HORA DE FIRMA DIGITAL DEL DOCUMENTO COMPLETO .............................................................................. 49
I.- DATOS DE MANEJO DE LA MADERA ................................................................................................................................... 49
J.- FIRMA DIGITAL DEL DOCUMENTO COMPLETO ................................................................................................................ 50
3.- FORMATO DE IMPRESIÓN DE DOCUMENTOS ........................................................................................................................ 51
4.- CODIFICACIÓN TIPOS DE IMPUESTOS y RECARGOS ............................................................................................................ 51

Formato DTE

Versión 2.5 2026-02

Pág.2 de 51

BITÁCORA DE CAMBIOS
Cambios 16/02/2026
1)

En el campo “Indicador Tipo de traslado de bienes”, el tipo de traslado N°7, se cambia el nombre de “Guía de devolución” por “Devolución de Mercaderías”.

2)

En la subsección “Transporte” se agregan los campos Patente de Carro o remolque, Fecha de Salida, Hora de Salida y Fecha de Llegada, según Resolución
Ex. N°154, 2025.

3)

Se modifica la condición de uso de los siguientes campos de la guía de despacho: Patente, Rut transportista, Rut chofer, Nombre chofer, dirección destino.

4)

En el campo “Unidad de Medida”, se elimina la condicionalidad para el Indicador de tipo de Traslado de Bienes = 8 y 9.

5)

En la sección “Datos de manejo de la madera”, se agregan los campos de Georreferenciación de Destino de la madera, Rol Predio destino y Aviso Ejecución
de Faena, según Resolución Ex. N°75, 2024.

Cambios 05/02/2024
1)

En la sección “Datos de manejo de la madera”, Tag “Código Plan de Manejo Conaf”, (<CodPlanConaf>), pasa a tener largo máximo de 40 caracteres.

Cambios 07/12/2023
6)

En la sección “Datos de manejo de la madera”, Tag “Código Plan de Manejo Conaf”, (<CodPlanConaf>), pasa a ser alfanumérico.

7)

En la sección “Información de referencia”, Tag N° 2. “Tipo Documento de referencia”, (<TpoDocRef>), se incorpora el documento N°48: Comprobante de pago
electrónico.

Cambios 01/10/2022
Se agregan los siguientes campos:
•

Georreferencia de Emisión del DTE.

•

Rut y Nombre de Proveedor de SW.

•

Datos Manejo de Madera (Georreferenciación de Origen de la madera, Rol Predio origen y plan de manejo Conaf).

Cambios 14/09/2021
1)

En la sección “Información de Referencia”, Tag N° “Tipo Documento Referencia”, se incorporan nuevos documentos de referencia.
821: “Geo Referencia Predio”
822: “ROL Avalúo Predio”
823: “Plan Manejo – CONAF”

Cambios 15/11/2019
1)

En la sección “Encabezado”, Tag N°9 “Indicador Servicio”, (<IndServicio>), se incorpora un nuevo valor 6: Servicios prestados y utilizados totalmente en el
extranjero.

Cambios 10/07/2019
1)

En la sección “Información de Referencia”, Tag N°2 “Tipo Documento de referencia”, (<TpoDocRef>), se incorpora un nuevo documento de referencia.
820: Código de Inscripción en el Registro de Acuerdos con Plazo de Pago Excepcional.

Formato DTE

Versión 2.5 2026-02

Pág.3 de 51

Cambios 18/01/2018
1)

Se agrega el campo Tipo de Factura Especial <TipoFactEsp> dentro del área de Identificación del Documento <IdDoc>, para que se pueda emitir una factura
electrónica que se utilizará para la devolución de IVA de turista que se aplica en Arica. Cuando tome el valor <TipoFactEsp>=1, se podrá generar este tipo de
factura especial y validará para poder incorporar dos campos obligatorios, <TipoDocID> y <NumId>, datos que tendrán tipo de documento del turista y su número
correspondiente.

Cambios 31/05/2017
1)

Se agregan dos nuevos campos opcionales en el encabezado, dentro del área de Identificación del Documento <IdDoc>, para la caracterización de la Venta por
parte del Vendedor denominado “Tipo de Transacción de Venta” (<TpoTranVenta>), y de forma voluntaria la caracterización de la Compra por parte del
Comprador informada por el Vendedor, que se denomina “Sugerencia de Tipo de Transacción de Compra” (<TpoTranCompra>). Se crean con la finalidad de
facilitar el registro y caracterización de los documentos emitidos y recibidos, lo cual podrá predefinirse al momento de generarse el DTE.

2)

En documentos de exportación si bien se continua con la emisión en moneda extranjera la sección “Otra Moneda” es obligatorio informar la conversión a pesos
chilenos, para lo cual deberá indicar el tipo de moneda <TpoMoneda>, tipo de cambio <TpoCambio>, monto exento otra moneda <MntExeOtrMnda>y monto
total otra moneda <MntTotOtrMnda> en pesos chilenos.

3)

Para los documentos Factura Electrónica, Factura No Afecta o Exenta Electrónica, y Liquidaciones Factura Electrónica, deben informar obligatoriamente el
campo Forma de Pago <FmaPago>, en caso que no venga esta información se considerará por defecto que tiene el valor 2 (crédito).

Cambios 29/09/2014
1)

Se agrega nuevo código 271 para el Art. 42 a) inciso segundo, Bebidas analcohólicas y Minerales con elevado contenido de azúcares. (según indica la ley) en
la tabla CODIFICACIÓN TIPOS DE IMPUESTOS y RECARGOS

2)

Se elimina FORMATO DE IMPRESIÓN DE DOCUMENTOS, ya que está contenido en MANUAL DE MUESTRAS IMPRESAS en www.sii.cl

Cambios 27/07/2012
1)

El campo “Vía de Transporte”, Tag N°73 se modifica modalidad de información del campo en el documento impreso a I.

Cambios 08/04/2010
1)

En la sección Encabezado Tags N° 80 “Puerto de Embarque” y N° 82 “Puerto Desembarque”, opcionales en la emisión de Facturas de Exportación Electrónica

2)

En la sección “Información de Referencia”, Tag N°2 “Tipo Documento de referencia”, se modificaron los requerimientos de referencia en caso de emisión de
facturas de exportación electrónica

3)

En la sección “Información de Referencia”, Tag N°5 “RUT Otro contribuyente”, se detalla el uso del campo en los casos que se emitan documentos electrónicos
que referencian otros DTE, emitidos por RUTs fusionados o absorbidos.

4)

En la tabla de códigos de impuesto se agregan los códigos 51: Gas Natural Comprimido, 52: Gas Licuado de Petróleo y 53: Retención Suplementeros.

Cambios 08/03/2010
1)

En pág. 20, en la sección Encabezado, el Tag N°98 "FLETE" <MntFlete> y el Tag N°99 "SEGURO" <MntSeguro> deben ser estrictamente mayor que cero.

Cambios 10/09/2008
1)

Formato DTE

En Codificación Tipos de Impuesto y Recargos se elimina el código 29, que sólo puede ser utilizado en IEC por transportistas de carga, y se incorpora el código
35 para efecto de la emisión de documentos con impuesto específico gasolina.

Versión 2.5 2026-02

Pág.4 de 51

Cambios 20/07/2006
1)

El campo “Identificador Adicional del Emisor” se reubica al final del “ÁREA EMISOR” del Encabezad

2)

Se permite informar en la Guía de Despacho Electrónica, a nivel de Encabezado, los siguientes campos: “Identificador Adiciona l del Emisor”, “Modalidad de
Venta”, “Cláusula de Venta Exportación”, “Total Cláusula de venta Exportación”, “Vía de Transporte”, “Nombre o identificación del Medio de Transporte”, “Rut
Cía. Transportadora”, “Nombre Cía. Transportadora”, “Identificador Adicional Cía. Transportadora”, “Identificador Adicional Puerto de Embarque” e
“Identificador Adicional Puerto de Desembarque”. Anteriormente, estos campos sólo estaban definidos para la Factura de Exportación Electrónica, Nota de
Crédito y de Débito de Exportación Electrónica.

3)

Se permite informar en la Factura de Exportación Electrónica, Nota de Crédito y Nota de Débito de Exportación Electrónica, a nivel de Encabezado, los siguientes
campos: “Booking” y “Operador”. Anteriormente, estos campos sólo estaban definidos para la Guía de Exportación Electrónica.

Cambios 22/09/2005
1)

Se agregan cuatro nuevos Documentos Tributarios Electrónicos: Liquidación-Factura, Factura de Exportación, Nota de Crédito de Exportación y Nota de Débito
de Exportación.

2)

Se modifica la obligatoriedad de los campos de la guía de despacho para que considere la Guía de Despacho que será utilizada en el transporte para Exportación
y otros casos excepcionales

3)

Se agrega nueva sección: “COMISIONES Y OTROS CARGOS”, y campos que los agrupan en ENCABEZADO (“Valor Neto Comisiones y Otros Cargos”, “Valor
Comisiones y Otros Cargos No Afectos o Exentos” e “IVA Comisiones y Otros Cargos”. Esta área es obligatoria para Liquidaciones-Factura y opcional para
Facturas de Compra y Notas de Crédito/Débito que hacen referencia a Facturas de Compra.

4)

Se admiten valores negativos en Liquidaciones Factura para los siguientes campos:
Del ENCABEZADO: “Monto Neto”, “Valor Neto Comisiones y Otros Cargos”, “Monto no afecto o exento”, “Valor Comisiones y Otros Cargos No Afectos o
Exentos”, “IVA”, “IVA Propio”, “IVA Terceros”, “IVA Comisiones y Otros Cargos”, “Monto Total”, “Monto Total en Otra Moneda”
Del DETALLE: “Valor por línea de Detalle” y “Valor por línea de detalle en Otra Moneda”.
De COMISIONES Y OTROS CARGOS: “Valor” y “Valor IVA Comisión u Otro Cargo”.

5)

Se incorporan códigos referentes a Exportación en el campo: Indicador Tipo de traslado de bienes.

6)

Se incorpora en ENCABEZADO “Tipo de impresión”, el cual indica la modalidad en la cual ha sido impreso el documento (para Guía de Despacho).

7)

Se incorpora en ENCABEZADO campos para precisar forma de pago: “Tipo Cuenta de Pago”, “Banco de Pago”, “Cuenta de Pago”.

8)

Se incorpora en ENCABEZADO: “Correo Contacto Receptor”.

9)

Se incorpora en ENCABEZADO: “Forma de Pago Exportación” según tabla de Formas de pago de Aduana.

10) Se incorpora en ENCABEZADO “Código Otra moneda”, y “Tipo de Cambio” para indicar incorporación de valores opcionales en otra moneda.
11) Se incorpora en ENCABEZADO, los campos: Código Emisor Traslado Excepcional, Folio Autorización y Fecha Autorización, para diferenciar al emisor de una
Guía de Despacho que será utilizada en el transporte para Exportación y otros casos excepcionales.
12) Se incorpora en encabezado, sólo para documentos de Exportación “Tipo Moneda Transacción” para indicar cuando una Transacción de Exportación se está
registrando completa en otra moneda. Se especifica el Código de Moneda en que se registra la transacción de exportación.
13) Se incorporan campos en Otra Moneda para los campos:
Del ENCABEZADO: “Monto Neto”, “Monto no Afecto o Exento”, “Monto base faenamiento carne”, “IVA”, “Valor del Impuesto o Retención”, “IVA No Retenido” y
“Monto Total”.
Del DETALLE: “Precio Unitario del ítem”, “Descuento”, “Sub-descuento Valor”, “Recargo”, “Sub-Recargo Valor” y “Valor por línea de Detalle”.
De DESCUENTOS Y RECARGOS GLOBALES: “Valor”.
14) Se cambia nombre de “Indicador de Servicio Periódico” por “Indicador de Servicio”.
15) Se incorporan en el Encabezado, los campos opcionales: “Número Identificador del Receptor extranjero”, “Nacionalidad del Receptor Extranjero”, “RUT Chofer”
Formato DTE

Versión 2.5 2026-02

Pág.5 de 51

y “Nombre del Chofer”, “Términos del Pago – glosa”.
16) Se incorporan en el Encabezado, para los documentos de Exportación, y Guías de Despacho utilizadas en Exportación, los siguientes campos: “Forma de Pago
de Exportación”, Modalidad de Venta”, “Cláusula de venta”, “Total Cláusula de venta”, “País Receptor”, “País Destino”, “Vía de Transporte”, “Nombre o
Identificación del Medio de Transporte”, “Rut Cía. Transportadora”, “Nombre Cía. Transportadora”, “Tara”, “Unidad de medida de la Tara”, “Puerto de Embarque”,
“Puerto Desembarque”, “Total Ítems”, “Total Peso Bruto”, “Unidad Peso Bruto”, “Total peso Neto”, “Unidad peso neto”, “Total Bultos”, “Flete” y “Seguro”.
17) Se incorporan en el Encabezado “Identificador Adicional del Emisor”, “Código Adicional de Sucursal”, “Identificador Adicional del Receptor Extranjero”,
Identificador Adicional Cía. Transportadora”, “Identificador Adicional Puerto de Embarque”, “Identificador Adicional Puerto de Desembarque”, y en el Área de
Referencia “Código Adicional de otro contribuyente”. Todos para uso de documentos de Exportación como por ejemplo un número de locación u otro código de
necesidad del exportador:
18) Se incorpora en el Encabezado, para los documentos de Exportación, y Guías de Despacho utilizadas en Exportación, la Tabla: “Secuencia de Tipo de Bultos”,
la cual contiene los siguientes seis campos: “Tipo de Bulto”, “Cantidad de Bultos”, “Marcas”, “Id. Container”, “Sello” y “Emisor Sello”.
19) Se incorpora en el Encabezado campos “Booking” y “Operador” para Guías de Despacho para exportación.
20) Se incorpora nuevo campo opcional “Correo Contacto receptor” para especificar aparte de Contacto Receptor, específicamente un correo electrónico asociado
al contacto.
21) Se agrega en ENCABEZADO nuevo campo opcional “Monto Base de Márgenes de Comercialización”.
22) El IVA NO RETENIDO cambia su obligatoriedad: Se puede incorporar en facturas de Compra y Notas de Crédito o débito que referencian facturas de compra.
23) El campo “Crédito Especial 65% empresas constructoras” se inhibe (no aplica) para Factura de compra.
24) En DETALLE se abre el campo “Código Impuestos o Retenciones” en una tabla de hasta 4 códigos para aceptar más de un código de impuesto o retención.
25) En Detalle se incorporan campos: “Monto Base/Faenamiento/Márgenes de Comercialización” y “Precio Unitario Neto Consumidor Final”. Sólo para transacciones
realizadas por agentes retenedores
26) En DETALLE se incorpora campo “Indicador Agente Retenedor” que indica que se actúa como agente retenedor en determinado producto.
27) En DETALLE se incorpora “Tipo Código Subcantidad”
28) Se cambia formato de numéricos de montos de tal forma que acepten decimales para hacer documentos completos en moneda diferente de Pesos.
29) Referencias Campo Tipo Documento Referencia, se agregaron los siguientes códigos: 807: DUS, 808: B/L (Conocimiento de embarque), 809: AW B (Air Waybill),
810: MIC/DTA, 811: Carta de Porte, 812: Resolución del SNA donde califica Servicios de Exportación, 813: Pasaporte, 814: Certificado de Depósito Bolsa de
Productos de Chile, 815: Vale de Prenda Bolsa de Productos de Chile. 888: Referencia a Archivo adjunto.
30) Se crea un nuevo código de impuestos y recargos en la tabla 4, correspondiente a Factura de Compra y Notas de Crédito y de Débito relacionadas a Factura
de Compra, que no incluye retención de IVA (retención de IVA de 0%), código 49. También se agrega el código 50.
31) Se agrega sección “Subtotales Informativos”.
32) Debajo de cada campo se incluye el nombre del tag XML que tiene asociado dentro del schema. Por ejemplo <TipoDTE>.

Cambios 15/04/2005
1)

Se especifica más detalladamente el formato de impresión en relación a la Recepción conforme de Mercaderías o de prestación de servicios.

2)

Se modifica Schema XML en cuanto a estructura con inclusión de otros schemas.

Formato DTE

Versión 2.5 2026-02

Pág.6 de 51

Cambios 04/04/2005
1)

Se incorpora en ENCABEZADO, los campos opcionales: Monto Cancelado y Saldo Insoluto, para indicar pagos realizados y saldos adeudados al momento de
la emisión del documento

2)

Se incorpora en ENCABEZADO la Tabla de Montos de Pago, que contiene los tres campos: Fecha de Pago, Monto de Pago y Glosa asociada al pago, para
indicar los pagos parciales pactados entre las partes.

3)

Se incorpora en el formato de impresión la Recepción conforme de Mercaderías o de prestación de servicios, según la ley 19.983 que otorga Mérito Ejecutivo a
la factura y regula su transferencia.

Cambios 21/10/2004
1)

ENCABEZADO: Se aumenta el largo de los siguientes campos, antes 15 caracteres, ahora 20 caracteres.
Campos: CiudadOrigen, CiudadRecep, CiudadPostal, CiudadDest.

2)

DETALLE: Largo campo Tipo de código se amplía a 10 caracteres.

3)

DETALLE: Monto Período ahora puede ser negativo.

4)

REFERENCIAS: Se aumenta la cantidad de ocurrencias de la sección de Referencias. Antes 20, ahora se permite hasta 40 ocurrencias de esta sección.

5)

REFERENCIAS: Se aumenta el largo del campo Razón Referencia, antes 30 caracteres, ahora 90 caracteres.

Cambios 22/06/2004
1)

REFERENCIAS: Campo 2 Tipo Documento Referencia, se agregaron los siguientes códigos: 804: Resolución, 805: Proceso ChileCompra, 806: Ficha
ChileCompra.

2)

REFERENCIAS: Campo 4 Folio-de-Referencia, se cambió el tipo de datos, antes NUM, ahora ALFA, y el largo a 18 caracteres.

3)

Actualización punto 4. Codificación Tipo de Impuestos y Recargos. Tasa retención Carne Y Harina se corrigieron. Se eliminó código 16 y 40. Se agrego código
46. Se reordenó la Tabla por Código.

Formato DTE

Versión 2.5 2026-02

Pág.7 de 51

1.- INTRODUCCIÓN
En este documento se describe el contenido que deben tener los Documentos Tributarios Electrónicos (en adelante DTE). En
la definición de este contenido se ha considerado tanto la necesidad desde el punto de vista tributario como desde el punto de vista
comercial. El objetivo es tener un documento que sea un instrumento adecuado para el respaldo de la transacción desde el punto
de vista de las partes y contenga la información que se requiere para la fiscalización tanto del transporte de los bienes como del
pago de los tributos.
La información considerada es aquella específica de la transacción y que es necesaria para emisor y receptor. Si hay otra
información que el emisor requiere para sus procesos y que no requiere ser informada al receptor, entonces se trata de información
de gestión del emisor, que no requiere estar estructurada a nivel del formato compartido, y debe ser incorporada en otro(s)
documentos adjuntos que no recibirá el Servicio de Impuestos Internos o almacenada en otros archivos y no en el documento
tributario electrónico mismo.
En este documento se describe el formato electrónico de los siguientes documentos:
-

Factura Electrónica
Factura No Afecta o Exenta Electrónica
Guía de Despacho Electrónica
Nota de Crédito Electrónica
Nota de Débito Electrónica
Factura de Compra Electrónica
Liquidación Factura Electrónica
Factura de Exportación Electrónica
Nota de Crédito de Exportación Electrónica
Nota de Débito de Exportación Electrónica

2.- CONTENIDO DE FACTURAS Y DOCUMENTOS ASOCIADOS.
De acuerdo a lo dispuesto en el artículo 56° inciso 2 del D.L. N°825, el Servicio de Impuestos Internos podrá autorizar
documentos que no reúnan los requisitos exigidos por la Ley y el Reglamento, resguardando debidamente los intereses fiscales.
Sobre la base de esta disposición se define el formato de los documentos electrónicos y la obligatoriedad de los datos contenidos
en ellos. Los documentos electrónicos tienen un formato único en que la principal diferencia radica en la obligatoriedad o no de
algunos datos.
Todo documento tributario electrónico que se emita debe contener una firma electrónica digital, la que permite autenticar su origen
y asegurar su integridad. Como equivalente a esta firma electrónica, pero orientado a la versión impresa del documento, se
incluye un conjunto de caracteres que incluye también una función criptográfica y datos para su validación, el cual es referenciado
como timbre electrónico, que cumple la función de autenticar el documento impreso.
Formato DTE

Versión 2.5 2026-02

Pág.8 de 51

2.1.- Zonas del documento electrónico
En el documento tributario electrónico (DTE), se distinguen las siguientes zonas:
A.
B.

C.
D.
E.
F.
G.
H.

Datos de encabezado: corresponden a la identificación del documento, información del emisor, información del receptor y
monto total de la transacción.
Detalle por Ítem: En esta zona se debe detallar una línea por cada Ítem. Se debe detallar cantidad, valor, descuentos y
recargos por ítem, impuestos adicionales y valor neto. En el caso de la Liquidación-Factura, se detallan los datos de los
documentos liquidados.
Descuentos y Recargos: Esta zona se utiliza para especificar descuentos o recargos que afectan al total del documento y
que no se requiere especificar ítem a ítem.
Información de Referencia: En esta zona se deben detallar los documentos de referencia, por ejemplo, se debe identificar
la Guía de Despacho que se está facturando o la Factura que se está modificando con una Nota de crédito o de débito.
Comisiones y Otros Cargos: Obligatoria para Liquidación Factura y opcional para Factura de Compra y Nota de Crédito/Débito que corrijan operaciones
relacionadas con Facturas de Compra.
Timbre Electrónico SII: Firma electrónica sobre la información representativa del documento para permitir la validación del
documento impreso.
Fecha y hora de la firma electrónica
Firma Electrónica sobre toda la información anterior para garantizar la integridad del DTE enviado al SII

El documento no podrá exceder de 60 líneas de ítem Detalle. Además, en caso de requerir impresión, se debe poder imprimir en
un papel que no exceda de los máximos definidos en las normas del documento impreso.

Formato DTE

Versión 2.5 2026-02

Pág.9 de 51

La obligatoriedad de cada una de las zonas por tipo de documento se especifica en la siguiente Tabla.
OBLIGATORIEDAD DE LA ZONA SEGÚN TIPO DE DOCUMENTO
LIQUIDAC.
FACTURA

FACT
EXPORT.

NOTA
CRED.
EXPORT

NOTA DEB.
EXPORT.

1

1

1

1

1

1

1

1

1

1

1

3

3

3

3

3

3

3

0

2

2

2

0

2

2

2

2

2

1

1

2

2

2

1

1

0

0

0

2

2

2

2

0

0

0

Timbre

1

1

1

1

1

1

1

1

1

1

Fecha y hora de firma

1

1

1

1

1

1

1

1

1

1

Firma Electrónica

1

1

1

1

1

1

1

1

1

1

FACT.

FACT
EXENTA

GUIA

NOTA
CRED.

Encabezado

1

1

1

1

1

Detalle

1

1

1

1

Sub Total Informativo

3

3

3

Descuentos y Recargos

2

2

Información Referencia

2

Comisiones y Otros
Cargos

Zonas del Documento

NOTA DEBIT FACT. COMP.

Códigos de Obligatoriedad
0: No corresponde. Significa que el dato no debe ir en un determinado documento.
1: Dato obligatorio. El dato debe estar en el documento siempre, independiente de las características de la transacción.
2: Dato condicional. El dato no es obligatorio en todos los documentos, pero pasa a ser obligatorio en determinadas
operaciones si se cumple una cierta condición. Por ejemplo, si hay descuentos o recargos, éstos deben estar
registrados porque en caso contrario el documento estará descuadrado en cuanto a los montos de neto, IVA y Total.
3: Opcional.

Formato DTE

Versión 2.5 2026-02

Pág.10 de 51

2.2.- Detalle por Zona
A continuación, se especificarán el contenido de cada Zona, formato de cada dato de la zona, y códigos de obligatoriedad del dato
según tipo de documento.
El tipo de información puede ser alfanumérica (ALFA) o numérica (NUM), en ambos tipos de información el largo indicado
es el largo máximo.
En la información de tipo numérica, los decimales se separan con punto y se indican sólo cuando el valor que se desea
incluir contiene decimales significativos. No debe separarse los miles con carácter alguno.
En la información alfanumérica, algunos caracteres como ‘&’ y ‘<’ tienen un significado especial para XML y deben
ser reemplazados por la secuencia de escape que el estándar define para dichos caracteres.
La columna (*), indica que, si el documento recibido por el SII no contiene este campo, el DTE no se considerará
válidamente emitido y será rechazado. Esta columna está sólo en la Zona de encabezado. No se rechazan documentos por
errores de contenido por ejemplo errores como que el IVA no sea igual a la tasa del IVA por el Monto neto; las correcciones a
este tipo de errores deberán ser hechas vía Nota de Crédito o Nota de Débito.
En la columna I, se indica si el dato debe estar en la representación impresa del documento.
- Debajo de cada campo se incluye el nombre del tag XML que tiene asociado dentro del schema. Por ejemplo <TipoDTE>
N= No es obligatorio que el campo sea impreso en el documento.
I = Debe estar impreso. La impresión de un dato no debe necesariamente ser igual al formato que se
especifica en el presente documento. Como ejemplo, una fecha no tiene necesariamente que estar en el
formato AAAA-MM-DD, sino que puede ser impresa con el mes en letras o cambiando el orden en que
aparecen el año, el mes y día, de manera de facilitar su lectura. Adicionalmente, se puede optar porque
un dato que es obligatorio imprimir, esté preimpreso.
P = Debe estar impresa traduciendo el código a la correspondiente glosa (expresado en palabras.) Por ejemplo:
en el documento electrónico el tipo de documento está codificado, sin embargo, en la representación impresa
del documento se debe indicar el nombre del documento (Factura electrónica, Nota de Crédito electrónica,
etc.)

Formato DTE

Versión 2.5 2026-02

Pág.11 de 51

A.- ENCABEZADO
CAMPOS
1

VERSIÓN
AREA
<IdDoc>

2

Tipo Documento
Tributario
Electrónico
<TipoDTE>

DESCRIPCIÓN

Largo
Max

Tipo

3

Alfa

Versión del Formato utilizado

Validación
Valor: 1.0

OBLIGATORIEDAD
*

I

FACT

FACT
EXENT

*

N

1

1

1

1

1

IDENTIFICACIÓN DEL
DOCUMENTO

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

GUIA NOTA
CRED

Indica si el documento es:
33: Factura Electrónica
34: Factura No Afecta o Exenta
Electrónica
43: Liquidación-Factura Electrónica
46: Factura de Compra Electrónica.
52: Guía de Despacho Electrónica
56: Nota de Débito Electrónica
61: Nota de Crédito Electrónica
110: Factura de Exportación.
111: Nota de Débito de
Exportación.
112: Nota de Crédito de
Exportación

3

NUM

De acuerdo con la
descripción del Campo

*

P

1

1

1

1

1

1

1

1

1

1

Folio autorizado por el SII

10

NUM

Campo NUM

*

I

1

1

1

1

1

1

1

1

1

1

Fecha de emisión contable del docto
(AAAA-MM-DD)

10

ALFA

Fecha válida entre
2003-04-01 y 2050-12-31

*

I

1

1

1

1

1

1

1

1

1

1

NUM

1: Nota de Crédito sin
derecho a descontar
débito (Art. 70 DL 825 y
art. 38 reglamento DL
825)

N

0

0

0

2

0

0

0

0

0

0

1

NUM

1: Despacho por cuenta
del receptor del
documento (cliente o
vendedor en caso de
Facturas de compra.)
2: Despacho por cuenta
del emisor a
instalaciones del cliente
3: Despacho por cuenta
del emisor a otras
instalaciones (Ejemplo:
entrega en Obra)

N

2

2

2

0

0

2

0

2

0

0

1

NUM

1: Operación constituye
venta1

P

0

0

1

0

0

0

0

0

0

0

Folio Documento
3
<Folio>

4

Fecha de
Emisión
<FchEmis>

5

Indicador de No
Rebaja

Sólo para Notas de Crédito que no
tienen derecho a Rebaja del Débito

1

<IndNoRebaja>

6

Tipo de
Despacho
<TipoDespacho>

7

Indicador Tipo de
traslado de
bienes

Indica si el documento acompaña
bienes y el despacho es por cuenta
del vendedor o del comprador.
No se incluye si el documento no
acompaña bienes o se trata de una
Factura o Nota correspondiente a la
prestación de servicios.

Sólo para Guías de despacho. Indica
si el traslado de mercadería es por
Venta (valor 1) o por otros motivos
que no corresponden a

1 De acuerdo a la definición de "venta" establecida en el Artículo 2° del DL 825.

Formato DTE

Versión 2.5 2026-02

Pág.12 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

OBLIGATORIEDAD
Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

FAC

NOTA
DEBIT
EXPO

venta. (valores mayores a 1).
2: Ventas por efectuar
3: Consignaciones
4: Entrega gratuita
5: Traslados internos
6: Otros traslados no
venta
7: Devolución de
mercaderías
8: Traslado para
exportación. (No venta)
9: Venta para exportación

7: Para de devolución de
mercaderías que fueron trasladadas
para exportación desde la zona de
embarque.
<IndTraslado>
8 y 9: Para exportaciones, cuando se
dirige la mercadería hacia el puerto,
aeropuerto o aduana de embarque.
9: Entre otros, venta de mercaderías
que se entregan en Zona Primaria de
Aduanas para su exportación.
8

9

Tipo de
impresión
<TpoImpresion>

Indicador
Servicio

Describe modalidad de Impresión de
la representación impresa en formato
normal o en formato Ticket

Indica si la transacción corresponde a
la prestación de un servicio

1

1

Alfa

N (Normal) o T (Ticket)
Por omisión se asume
“N”

N

0

0

2

0

0

0

0

0

0

NUM

1: Factura de servicios
periódicos domiciliarios2
2: Factura de otros
servicios periódicos
3: Factura de Servicios.
(en caso de Factura de
Exportación: Servicios
calificados como tal por
Aduana)
Sólo para Facturas de
Exportación:
4: Servicios de Hotelería
5: Servicio de Transporte
Terrestre Internacional
6: Servicios prestados y
utilizados totalmente en el
extranjero

N

2

2

0

2

2

2

2

2

2

2

NUM

1: Montos de líneas de
detalle vienen
expresados en montos
brutos.

N

2

2

0

2

2

2

2

0

0

0

N

3

3

3

0

0

3

3

0

0

0

<IndServicio>

10

Indicador
Montos Brutos
<MntBruto>

Sugerencia Tipo
Transacción de
Compra
11
<TpoTranCompr
a>

Indica si las líneas de detalle,
descuentos y recargos se expresan
en montos brutos. (Sólo para
documentos sin impuestos
adicionales)
Es una sugerencia que indica el Tipo
de Transacción de Compra para el
comprador donde el vendedor no es
responsable por errores en su
digitación. Campo opcional para
indicar en el documento qué tipo de
compra es para el comprador (para el
Receptor de Factura o Emisor de
Factura de Compra).

1

1

NUM

Tipo de Compra para el
comprador:
1: Compras del Giro
2: Compras en
Supermercados o
similares
3: Adquisición Bien Raíz.
4: Compra Activo Fijo

0

2 Los servicios periódicos domiciliarios son aquellos identificados en DL 825, Art. 9° en que el impuesto se devenga en la fecha de vencimiento.

Formato DTE

Versión 2.5 2026-02

Pág.13 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

OBLIGATORIEDAD
Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

5: Compra con IVA Uso
Común
6: Compra sin derecho a
Crédito
7: Compra que no
corresponde incluir

Disponible sólo para facilitar el
registro en las compras. No obliga al
comprador a registrarlo de la misma
forma en sus compras.

12

Tipo Transacción
de Venta
<TpoTranVenta>

Indica el Tipo de Transacción de
Venta. Campo opcional a nivel de
Schema, pero obligatorio en su uso.
En caso de no informarse se asumirá
como “Ventas del Giro”. Se indica en
el documento qué tipo de Venta es
para el vendedor (para el Emisor de
Factura o Receptor de Factura de
Compra)

1

NUM

Tipo de Venta para el
vendedor:
1: Ventas del Giro
2: Venta Activo Fijo
3: Venta Bien Raíz

1

NUM

Valor 1: Contado;
2: Crédito
3: Sin costo (entrega
gratuita)

P

2

2

3

2

2

2

2

3

3

3

NUM

Para Factura de
Exportación Corresponde
al Código señalado en la
Tabla Formas de Pago
de Aduanas

P

0

0

3

0

0

0

0

3

3

3

Disponible para facilitar el registro en
las Ventas. Obliga al vendedor a
registrarlo de la misma forma en sus
ventas.

N

3

3

3

3

0

3

3

0

0

0

Inicialmente opcional en el Schema,
más adelante será un campo
obligatorio.
Indica en qué forma se pagará. En el
caso de una Factura por “Entrega
Gratuita”, se debe indicar el 3. Una
Factura de este tipo no tiene derecho
a crédito fiscal.

Forma de Pago
13
<FmaPago>

Para hacer uso de crédito fiscal las
facturas, facturas no afectas o
exentas, y las liquidaciones facturas
electrónicas, que tengan saldo
insoluto pendiente de pago al
momento de la emisión (CREDITO),
deberán cumplir con el requisito de
otorgar, o entenderse otorgado, el
recibo de mercaderías entregadas o
servicios prestados.
Es obligatorio informar este campo.
En caso de no existir este campo
se entenderá que tiene valor 2
(Crédito).

14

Forma de Pago
Exportación
<FmaPagExp>

Formato DTE

En el caso de Factura de exportación
se refiere a la forma de pago del
importador extranjero indicada en el
DUS (acreditivo, cobranza, anticipo,
contado) En el caso de una Factura
de exportación por “Muestras sin
carácter comercial”, según las
normas de Aduanas, debe indicar el
Cod. 21.
Versión 2.5 2026-02

2

Pág.14 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

OBLIGATORIEDAD
*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

15

Fecha de
cancelación
<FchCancel>

16

Monto
Cancelado

Sólo se utiliza si la factura ha sido
cancelada antes de la fecha de
emisión. (AAAA-MM-DD)

10

ALFA

Fecha válida entre
2002-08-01 y 2050-12-31
Campo Obligatorio para
Factura de exportación
cuando en “Forma de
Pago Exportación” se
indique “anticipo”

Al momento de emitirse el documento

18

NUM

Sin validación

I

3

3

3

3

3

3

3

3

3

3

Al momento de emitirse el documento

18

NUM

Sin validación

I

3

3

3

3

3

3

3

3

3

3

Opcional para especificar
programación de pagos
del documento

I

3

3

3

3

3

3

3

3

3

3

N

3

3

3

3

3

3

3

2

3

3

<MntCancel>
Saldo Insoluto
17
<SaldoInsol>
TABLA de
Montos de Pago
<MntPagos>

Hasta 30 repeticiones.
Contiene los 3 campos siguientes.

Fecha de Pago
18

Fecha de pago programado

10

ALFA

Fecha válida

N

1

1

1

1

1

1

1

1

1

1

Monto de pago programado

18

NUM

Sin validación

N

1

1

1

1

1

1

1

1

1

1

Glosa Adicional para calificar pago

40

ALFA

Sin validación

N

3

3

3

3

3

3

3

2

3

3

10

ALFA

Fecha válida, menor o
igual que “fecha hasta”

N

3

3

0

3

3

3

3

3

3

3

10

ALFA

Fecha válida, mayor que
valor de Periodo desde

N

3

3

0

3

3

3

3

3

3

3

2

ALFA

Valor: CH: Cheque.
CF: Cheque a fecha
LT:letra, EF:Efectivo, PE:
Pago A Cta. Cte.;
TC:Tarjeta Crédito,
OT:Otro

P

3

3

0

3

3

3

3

3

3

3

2

ALFA

Valor: CT: Cta.Cte;
AH:Ahorro, OT:Otra.

P

3

3

0

3

3

3

3

3

3

3

<FchPago>
Monto de Pago
19
<MntPago>

20

Glosa
descripción Pago
<GlosaPagos>
FIN TABLA
Período desde

21
<PeriodoDesde>
Período hasta
22
<PeriodoHasta>

Período de facturación para Servicios
Periódicos. Fecha desde
(Fecha inicial del servicio facturado)
Período de facturación para Servicios
Periódicos. Fecha hasta
(Fecha final del servicio facturado)

Medio de Pago
Indica en que modalidad se pagará.

23
<MedioPago>

24

Tipo Cuenta de
Pago
<TipoCtaPago>

Formato DTE

Cuenta

Versión 2.5 2026-02

Pág.15 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

OBLIGATORIEDAD
Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Cuenta de Pago
25

Numero de la Cuenta

20

ALFA

Sin validación

P

3

3

0

3

3

3

3

3

3

3

Banco de la Cuenta

40

ALFA

Sin validación

P

3

3

0

3

3

3

3

3

3

3

Es un código acordado entre las
empresas, que indica términos de
referencia
Ejemplos: Fecha Recepción Factura
(FRF), o Fecha entrega Mercaderías
(FEM), etc.

4

ALFA

Sin validación.

N

3

3

3

3

3

3

3

3

3

3

I

3

3

3

3

3

3

3

2

2

2

N

3

3

3

3

3

3

3

3

3

3

I

2

2

0

3

3

3

3

2

3

3

I

3

0

0

3

0

0

0

0

0

0

N

3

0

3

0

0

0

0

0

0

0

<NumCtaPago>
Banco de Pago
26
<BcoPago>

27

Términos del
pago- Código
<TermPagoCdg>
Términos del
Pago – glosa

28
<TermPagoGlos
a>
Términos del
pago- Días
29
<TermPagoDias
>

30

Fecha de
vencimiento
(pago)

Glosa que describe las condiciones
del pago del documento, codificado
en el campo: “Términos del pagoCódigo”

100

ALFA

En documentos de
Exportación Es
obligatorio si se indicó el
campo: “Términos del
pago-Código”

Cantidad de días de acuerdo al
código de Términos de pago: Ejemplo
5 días Fecha entrega Mercaderías
(Día = 5, Código =FEM)

3

NUM

Número mayor que cero

Fecha de vencimiento (AAAA-MMDD)

10

ALFA

Fecha válida entre
2002-08-01 y 2050-12-31

<FchVenc>
Valores posibles del 1 al
9
Factura Turista = 1
Campo que indica que es una factura
electrónica (tipo 33), con un formato
especial.
31

Tipo de Factura
Especial
<TipoFactEsp>

Este campo es opcional y solo se
debe utilizar en caso que se utilice un
tipo de facturación especial como la
facturación turista. Por defecto, para
facturación normal este campo no
debe ser informado.

1

NUM

Si se utiliza
<TipoFactEsp> = 1,
entonces el <RUTRecep>
=55555555-5, la comuna
debe ser
<CmnaOrigen>= Arica ó
Camarones ó
Putre ó General Lagos y
los datos del receptor
extranjero debe informar
<TipoDocID> y <NumId>
La Razón Social del
Receptor debe indicar
“Extranjero sin RUT”

Latitud
<LatitudEmision>
Formato DTE

Valor que corresponde a la latitud de la
ubicación geográfica en que es emitido
el documento en el estándar WGS84 en
su modalidad decimal

30

Versión 2.5 2026-02

ALFA

*

Pág.16 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

OBLIGATORIEDAD
Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Longitud

Valor que corresponde a la longitud de
ubicación geográfica en que es emitido
<LongitudEmision el documento en el estándar WGS84
en su modalidad decimal
>

Sistema de
Referencia
<SistemaReferen
cia>
FIN AREA

30

ALFA

1

NUM

Identifica el código del sistema de
referencia de la georreferenciación.

1. WGS84

*

N

3

0

3

0

0

0

0

0

0

0

*

N

3

0

3

0

0

0

0

0

0

0

1

1

1

1

1

1

1

1

1

1

IDENTIFICACIÓN DEL
DOCUMENTO

AREA
EMISOR
<Emisor>

10

ALFA

Cuerpo numérico
entre
100.000 y 99 millones, guion
y
dígito
verificador *
alfanumérico entre 0 y 9
oK

100

ALFA

Sin validación

I

1

1

1

1

1

1

1

1

1

1

80

ALFA

Sin validación

I3

1

1

1

1

1

1

1

1

1

1

20

ALFA

Sin validación

N

3

3

3

3

3

3

3

3

3

3

80

ALFA

N

3

3

3

3

3

3

3

3

3

3

6

NUM

N

1

1

1

1

1

1

1

1

1

1

Rut Emisor
32

33

Con guion y dígito verificador
<RUTEmisor>
Nombre o Razón
Social Emisor

I

1

1

1

1

1

1

1

1

1

1

<RznSoc>

34

Glosa indicando giro del emisor. No
Giro del negocio del
es preciso registrar todos los giros,
Emisor
sino que se podrá registrar sólo el
giro que corresponde a la
<GiroEmis>
transacción.
Teléfono Emisor

35

Hasta 2 Repeticiones
<Telefono>
Correo Emisor

36

<CorreoEmisor>
ACTECO

37

3

<Acteco>

Se acepta un máximo de 4 Códigos
de actividad económica del emisor
del DTE. Se puede incluir sólo el
código que corresponde a la
transacción.

NUM, máximo 4, deben
estar registrado en el SII

Este dato puede ir preimpreso, indicado todos los giros autorizados del emisor, al igual que en el documento manual.

Formato DTE

Versión 2.5 2026-02

Pág.17 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

OBLIGATORIEDAD
Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

38

Sólo para Guía de Despacho:
1: Exportador
2: Agente de Aduana (En la
Código
Emisor devolución de mercaderías de
Aduanas.
Traslado
Excepcional
3: Vendedor (Entre otros, se refiere a
aquel Productor que vende
mercadería con entrega en Zona
<CdgTraslado>
Primaria).
4: Contribuyente autorizado
expresamente por el SII.

1

NUM

5

NUM

Obligatorio si “Indicador
tipo de traslado” con valor
8y9

P

0

0

2

0

0

0

0

0

0

0

I

0

0

2

0

0

0

0

0

0

0

I

0

0

2

0

0

0

0

0

0

0

N

3

3

3

3

3

3

3

3

3

3

Sólo para Guía de Despacho:
39

Folio
Autorización
<FolioAut>

40

echa
Autorización

Corresponde al N° de Resolución del
SII donde en casos especiales se
autoriza al contribuyente a emitir
guías de despacho.
Sólo para Guía de Despacho:

Campo obligatorio
cuando se indique 4 en el
Código Emisor Traslado
Excepcional.
Fecha válida entre
2003-04-01 y 2050-12-31

10

ALFA

20

ALFA

Sin validación

9

NUM

Deber corresponder a un
código registrado en el
SII

N

2

2

2

2

2

2

2

2

2

2

20

ALFA

Sin validación

N

0

0

0

0

0

0

0

3

3

3

Datos correspondientes a Dirección
desde donde se despachan bienes o
de la sucursal que emite el
documento si no hay despacho de
bienes.

60

ALFA

Sin validación

I

1

1

1

3

3

1

1

1

3

3

45

Comuna Origen
<CmnaOrigen>

Análogo a Dirección Origen
Si se utiliza <TipoFactEsp> = 1,
entonces la comuna debe ser Arica ó
Camarones ó Putre ó General Lagos.

20

ALFA

Sin validación

I

1

1

1

3

3

3

3

3

3

3

46

Ciudad Origen
<CiudadOrigen>

Análogo a Dirección Origen

20

ALFA

Sin validación

N

3

3

3

3

3

3

3

1

3

3

<FchAut>

41

42

43

44

Fecha de emisión de la Resolución
de autorización (AAAA-MM-DD)

Campo obligatorio
cuando se indique 4 en el
Código Emisor Traslado
Excepcional.

Sucursal
<Sucursal>

Indica nombre de la sucursal que
emite el Documento. Corresponde a
un dato administrado por el emisor
que puede ser un texto o un número.

Código sucursal
<CdgSIISucur>

Código numérico entregado por el SII,
que identifica a cada sucursal que
está identificada en el Servicio de
Impuestos Internos. Si no hay
sucursales se puede omitir.

Código Adicional de
Código de identificación adicional
Sucursal
para uso libre
<CodAdicSucur>
Dirección Origen
<DirOrigen>

Formato DTE

Versión 2.5 2026-02

Pág.18 de 51

OBLIGATORIEDAD
CAMPOS
47

Código del
Vendedor

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

Largo
Max

Tipo

Glosa con identificador del vendedor

60

ALFA

Sin validación

N

3

3

3

3

3

3

3

3

3

3

Para documentos utilizados en
exportaciones. Código de
identificación adicional para uso libre.

20

ALFA

Sin validación

M

0

0

3

0

0

0

0

3

3

3

ALFA

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9
oK

I

2

2

2

2

2

0

0

0

0

0

1

1

1

1

1

1

1

1

1

1

I

1

1

1

1

1

1

1

1

1

1

N

3

3

3

3

3

3

3

3

3

3

I

1

1

1

1

1

1

1

1

1

1

I

3

0

0

3

0

0

0

0

0

0

DESCRIPCIÓN

Validación

*

<CdgVendedor>

48

Identificador
Adicional del
Emisor
<IdAdicEmisor>
FIN AREA
Rut Mandante

49

<RUTMandante>

AREA
<Receptor>

EMISOR
Corresponde al RUT del mandante si
el total de la venta o servicio es por
cuenta de otro el cual es responsable
del IVA devengado en el período
Con guion y dígito verificador

10

RECEPTOR
Corresponde al RUT del cliente,
excepto en la Factura de compra en
que se referencia al vendedor.

Rut Receptor
50
<RUTRecep>

Con guion y dígito verificador
En doctos. Exportac. 55.555.555-5

10

ALFA

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9
oK

20

ALFA

Sin validación

100

ALFA

Sin validación

20

ALFA

Sin validación

En Factura Electrónica si utiliza el
Tipo de Factura Especial Turista debe
ingresar el RUT 55.555.555-5

51

Código Interno
del Receptor
<CdgIntRecep>

52

Para identificación interna del
Receptor, por ejemplo código del
cliente, número de medidor, etc.

Nombre o Razón
Social Receptor
<RznSocRecep>

53

Número
identificador del
Receptor
extranjero
<NumId>

Formato DTE

Corresponde al número o código de
identificación personal del receptor
extranjero, otorgado por la
Administración tributaria extranjera u
organismo Gubernamental
competente. Se deben incluir guiones
y dígitos verificadores.
Es obligatorio cuando
<TipoFactEsp>=1

Versión 2.5 2026-02

Pág.19 de 51

OBLIGATORIEDAD
CAMPOS

54

Nacionalidad del
Receptor
Extranjero

DESCRIPCIÓN

FACT

GUIA

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

3

3

3

0

0

0

0

0

0

0

0

3

3

3

3

3

1

1

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

1

1

3

3

1

1

1

3

3

Largo
Max

Tipo

3

ALFA

Valores según Tabla de
Países www.aduana.cl

N

3

3

3

3

3

3

20

ALFA

Valor numérico 1 ó 2.

I

3

0

0

3

0

20

ALFA

Sin validación

N

0

0

0

0

40

ALFA

Sin validación

I

1

1

1

80

ALFA

Sin validación

N

3

3

80

ALFA

Sin validación

N

3

70

ALFA

I

1

Corresponde a la nacionalidad del
extranjero, según tabla de países de
Aduana

Validación

*

I

FACT
EXENT

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

<Nacionalidad>
Identificación del Documento con el
cual se identifica el turista.
55

Tipo de
Documento del
Turista

Valores:
1: Pasaporte
2: DNI

<TipoDocID>
Se activa y es obligatorio cuando
<TipoFactEsp>=1

56

Identificador
Adicional del
Receptor
Extranjero

Sólo para Documentos Exportación.
Código de identificación adicional
para uso libre

<IdAdicRecep>

57

Giro del negocio
del Receptor
<GiroRecep>

58

Contacto
receptor
<Contacto>

59

Correo Contacto
receptor
<CorreoRecep>

60

Dirección
Receptor
<DirRecep>

Formato DTE

Glosa impresa indicando giro del
receptor

Glosa con nombre y teléfono de
contacto en empresa del receptor
(para registrar el “Atención A:”)

e-mail de contacto en empresa del
receptor (para registrar el “Atención
A:”)

Dirección Legal del Receptor
(registrada en el SII)
En caso de documentos de
exportación, corresponde a la
dirección en el extranjero del
Receptor

Versión 2.5 2026-02

Pág.20 de 51

61

Comuna
Receptor
Análogo a Dirección Receptor

20

ALFA

I

1

1

1

3

3

1

1

3

3

3

<CmnaRecep>

Formato DTE

Versión 2.5 2026-02

Pág.21 de 51

OBLIGATORIEDAD
CAMPOS

FACT

GUIA

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

3

1

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

3

0

2

2

2

0

0

0

0

2

1

2

2

2

0

2

2

2

2

2

1

0

0

2

0

3

0

0

2

2

1

0

0

2

0

3

0

0

Largo
Max

Tipo

Análogo a Dirección Receptor

20

ALFA

N

3

3

3

3

3

3

Análogo a Dirección Receptor

70

ALFA

N

3

3

3

3

3

Análogo a Dirección Receptor

20

ALFA

N

3

3

3

3

Análogo a Dirección Receptor

20

ALFA

N

3

3

3

10

ALFA

I

2

2

2

I

I

DESCRIPCIÓN

Validación

*

I

FACT
EXENT

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

Ciudad Receptor
62
<CiudadRecep>

63

Dirección Postal
Receptor
<DirPostal>
Comuna Postal

64
<CmnaPostal>
Ciudad Postal
65
<CiudadPostal>

66

FIN AREA

RECEPTOR

Rut de
Solicitante de
factura

En casos de venta a público.
Es obligatorio si es distinto de Rut
receptor o Rut Receptor es persona
jurídica.
Con guion y dígito verificador

<RUTSolicita>

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9 o
K

AREA
TRANSPORTE
<Transporte>
Relevante si Indicador
Tipo de Despacho 2 o 3.

67

Información
Transporte4

Corresponde a la placa patente del
vehículo

8

ALFA

<Patente>

En caso de no conocer
los datos de la patente se
deben señalar en
forma expresa en el
documento., según
Resolución Ex. N°154,
2025.
Relevante si Indicador
Tipo de Despacho 2 o 3.

Patente de carro
o remolque4
<PatenteCarro>

Formato DTE

Corresponde a la placa patente del
carro, sea este remolque o
semirremolque

Versión 2.5 2026-02

8

ALFA

En caso de no conocer
los datos de la patente se
deben señalar en
forma expresa en el
documento., según
Resolución Ex. N°154,
2025.

Pág.22 de 51

Rut transportista4
68
<RUTTrans>

RUT Chofer4
69
<RUTChofer>

70

Nombre del
Chofer4

Con guion y dígito verificador
Indicador Tipo de Despacho es 2 o
3

Rut Chofer que realiza el transporte
de mercaderías.

10

ALFA

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9 o
K.

I

2

2

1

0

0

2

0

3

0

0

I

2

2

1

3

3

2

0

3

3

3

I

2

2

1

2

2

2

0

3

3

3

Obligatorio para
documentos que
acompañan traslado de
bienes.

10

ALFA

Con guion y dígito verificador

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9 o
K
Obligatorio para
documentos que
acompañan traslado de
bienes.
Sin validación
En caso de digitar el Rut
del chofer, debe indicarse
el nombre

30

<NombreChofer>

ALFA

Obligatorio para
documentos que
acompañan traslado de
bienes.

4

Esta información se debe registrar al momento de confeccionar el documento electrónico. En caso de no tenerla, deberán señalar en
forma expresa en el documento que no cuenta con la información, según Resolución Ex. N°154, 2025.

Formato DTE

Versión 2.5 2026-02

Pág.23 de 51

OBLIGATORIEDAD
CAMPOS

71

Dirección
Destino
<DirDest>

DESCRIPCIÓN

Largo
Max

Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Aplica si el destino es
distinto de Dirección
Receptor, o de Dirección
Emisor en el caso de
Factura de Compra

Datos correspondientes a Dirección
destino en documento que acompaña
productos o a la Dirección en que se
otorga el servicio en caso de Servicios
periódicos.

70

ALFA

Análogo Dirección Destino

20

ALFA

Ídem anterior

Análogo Dirección Destino

20

ALFA

Ídem anterior

I

2

2

1

3

3

2

0

2

3

3

I

2

2

1

3

3

2

0

3

3

3

N

3

3

3

3

3

3

0

2

3

3

Obligatorio para
documentos que
acompañan traslado de
bienes.

Comuna Destino
72

<CmnaDest>
Ciudad Destino

73

<CiudadDest>

Fecha de Salida
<FchSalida>

Fecha válida entre
2003-04-01 y 2050-12-31
Fecha efectiva de inicio del traslado
(AAAA-MM-DD)

10

ALFA

Obligatorio para
documentos que
acompañan traslado de
bienes.
Hora válida entre
00:00:00 y 23:59:59

I

2

2

1

3

3

2

0

3

3

3

Hora de inicio de traslado (HH:MI:SS)

5

ALFA

Obligatorio para
documentos que
acompañan traslado de
bienes.
Fecha válida entre
2003-04-01 y 2050-12-31

I

2

2

1

3

3

2

0

3

3

3

Fecha de llegada del traslado (AAAAMM-DD)

10

ALFA

Obligatorio para
documentos que
acompañan traslado de
bienes.

I

2

2

1

3

3

2

0

3

3

3

0

0

2

0

0

0

0

2

3

3

0

0

3

0

0

0

0

2

3

3

Hora de Salida
<HraSalida>

Fecha de
Llegada
<FchLlegada>

Sub-Área

TRANSPORTE.ADUANA
Indicar el Código según
tabla “Modalidad de
Venta” de Aduana.

Para doctos. utilizados en
exportación.
74

Modalidad de
Venta
<CodModVenta>

Formato DTE

Se refiere a si la exportación se
realiza bajo venta, En consignación, a
firme, en Consignación con mínimo a
firme, etc.)

Versión 2.5 2026-02

2

NUM

Campo Obligatorio para
Factura de Exportación,
excepto cuando en el
Campo “Indicador
Servicio” se indicó 3, 4 o
5 (hotelería o transporte
terrestre internacional)

P

Pág.24 de 51

75

Cláusula de
venta
Exportación

Indicar el Código según
Tabla “Cláusula compraventa” (Tabla Aduana)
Se refiere a la cláusula de venta
indicada en el DUS (FOB, CIF, etc.)

2

NUM

<CodClauVenta>

76

Total Cláusula de
venta
Exportación
<TotClauVenta>

77

Vía de
Transporte
<CodViaTransp>

Corresponde al valor total de la
exportación a pagar por el importador
según la cláusula de venta acordada
entre las partes y que se indica en el
DUS. (No incluye comisiones ni otros
gastos deducibles en el exterior)

18

Corresponde a la vía de transporte por
donde se envía la mercadería (aéreo,
terrestre, marítimo, etc.) al Extranjero

2

NUM

NUM

Campo Obligatorio,
excepto cuando en el
Campo “Indicador
Servicio” se indicó 3, 4 o
5.
Valor numérico de 18
dígitos con dos
decimales Campo
Obligatorio, excepto
cuando en el Campo
“Indicador Servicio” se
indicó 3, 4 o 5
Indicar el Código de la
vía de transporte utilizada
para transportar la
mercadería, según tabla
Vías de Transporte de
Aduana.

P

0

0

3

0

0

0

0

2

3

3

I

0

0

3

0

0

0

0

2

3

3

I

0

0

3

0

0

0

0

2

3

3

Campo Obligatorio, a
excepción cuando en el
“Indicador Servicio” se
registra la opción N°4

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

OBLIGATORIEDAD

Validación
*

78

Nombre o
Identificación del
Medio de
Transporte

Corresponde al nombre o glosa de la
nave transportista.

40

ALFA

I

FACT

FACT GUIA
EXENT

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT
EXPO

NOTA
CRED

NOTA
DEBIT

I

0

0

3

0

0

0

0

3

3

3

I

0

0

3

0

0

0

0

3

3

3

I

0

0

3

0

0

0

0

3

3

3

N

0

0

3

0

0

0

0

3

3

3

<NombreTransp>

79

Rut Cía.
Transportadora
<RUTCiaTransp>

80

Nombre Cía.
Transportadora
<NomCiaTransp>

81

Identificador
Adicional Cía.
Transportadora

Para doctos. utilizados en exportación.
Señale el Rol Único Tributario (RUT)
de la compañía transportista indicada
en el DUS. Si ésta es extranjera,
señale el RUT de la Agencia que la
representa en Chile.

10

ALFA

Nombre de la Cía. transportadora
declarada en el DUS.

40

ALFA

Identificación adicional para uso libre

20

ALFA

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9
oK

Sin validación

<IdAdicTransp>
Formato DTE

Versión 2.5 2026-02

Pág.25 de 51

82

83

84

85

Booking
<Booking>

Número de Booking o Reserva del
operador

20

ALFA

N

0

0

3

0

0

0

0

3

3

3

Código de Operador

20

ALFA

N

0

0

3

0

0

0

0

3

3

3

Puerto de embarque de mercancías

4

NUM

P

0

0

2

0

0

0

0

3

3

3

N

0

0

3

0

0

0

0

3

3

3

Operador
<Operador>
Puerto de
Embarque
<CodPtoEmbar
que>
Identificador
Adicional Puerto
de Embarque.

Identificación adicional para uso libre

20

<IdAdicPtoEmb
>

Formato DTE

Versión 2.5 2026-02

ALFA

Indicar el Código del
puerto de embarque
según tabla publicada en
www.aduana.cl
En Guías: obligatorio sólo
para Indicador tipo
traslado = 8 y 9
Sin validación
En Facturas de
Exportación: Obligatorio
excepto cuando el
“Indicador Servicio” = 4

Pág.26 de 51

OBLIGATORIEDAD
CAMPOS

86

87

DESCRIPCIÓN

Largo
Max

Tipo

Validación

*

FACT

I

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Indicar el Código del
puerto de Desembarque
según tabla publicada en
www.aduana.cl

Puerto
Desembarque

4

<CodPtoDesemb
>

NUM

En Guías: obligatorio sólo
para Indicador tipo
traslado = 8 y 9

P

0

0

2

0

0

0

0

3

3

3

En Facturas de
Exportación: Obligatorio
excepto cuando el
“Indicador Servicio” = 4

Identificador
Adicional Puerto
de Desembarque. Identificación adicional para uso libre

20

ALFA

Sin validación

N

0

0

3

0

0

0

0

3

3

3

7

NUM

Número entero

I

0

0

3

0

0

0

0

3

3

3

2

NUM

Código de la unidad de
medida, según tabla
“Unidades de Medida” de
Aduana

P

0

0

2

0

0

0

0

2

3

3

I

0

0

2

0

0

0

0

3

3

3

P

0

0

2

0

0

0

0

2

3

3

<IdAdicPtoDesem
b>
88

89

Tara
<Tara>
Unidad de medida
de la Tara
Indique la unidad de medida en la que
<CodUnidMedTar se encuentra expresado la Tara
a>

90

91

92

Total Peso Bruto
<PesoBruto>

Unidad Peso
Bruto

Señale con dos decimales, la
sumatoria de los pesos brutos de
todos los ítems del documento.

Valor Numérico de 10
enteros y dos decimales
12

NUM

Indique el código de la
unidad de medida, según
tabla Unidades de Medida
de Aduana

Indique la unidad de medida en la que
se encuentra el peso bruto de la
mercadería

2

Señale con dos decimales, la
sumatoria del peso neto de todos los
ítems del documento.

12

NUM

Valor Numérico de 10
enteros y dos decimales

N

0

0

3

0

0

0

0

3

3

3

Indique la unidad de medida en la que
<CodUnidPesoNe se encuentra el peso neto de la
mercadería
to>

2

NUM

Indique el código de la
unidad de medida, según
tabla Unidades de Medida
de Aduana

P

0

0

2

0

0

0

0

2

3

3

<CodUnidPesoBr
uto>

Total peso Neto
<PesoNeto>

NUM

En Guías: obligatorio sólo
para Indicador tipo
traslado = 8 y 9

Unidad peso neto
93

En Guías: obligatorio sólo
para Indicador tipo
traslado = 8 y 9

Formato DTE

Versión 2.5 2026-02

Pág.27 de 51

OBLIGATORIEDAD
CAMPOS
94

Total Ítems
<TotItems>

95

Total Bultos
<TotBultos>

Tabla:
Secuencia de
Tipo de Bultos
<TipoBultos>
96

Código Tipo de
bulto

97

Cantidad de
Bultos

Marcas
<Marcas>

99

Id. Container
<IdContainer>

100

Sello
<Sello>

101

Emisor Sello
<EmisorSello>

102

Flete
<MntFlete>

103

Largo
Max

Tipo

18

NUM

Indique el total de ítems del
documento

Seguro
<MntSeguro>

Código País
104 Receptor

Señale la cantidad total de bultos que
ampara el documento.

18

NUM

Tabla de descripción de los distintos
tipos de bultos. Se repite hasta 10
veces. Contiene los 6 campos
siguientes

*

I

FACT
EXENT

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Número entero sin
decimales

N

0

0

3

0

0

0

0

3

3

3

En Guías: obligatorio sólo
para Indicador tipo
traslado = 8 y 9

I

0

0

2

0

0

0

0

1

3

3

0

0

2

0

0

0

0

3

3

3

Sólo si se ha entregado la
información de Total de
Bultos

3

NUM

I

0

0

2

0

0

0

0

3

3

3

Señale la cantidad total de bultos de
este tipo.

10

NUM

I

0

0

2

0

0

0

0

2

3

3

Identificación de marcas, cuando es
distinto de contenedor

255

ALFA

I

0

0

2

0

0

0

0

2

3

3

Este campo y los dos siguientes sólo
se competan si el tipo de bulto es
contenedor. Incluye guion y DV de
contenedor

25

ALFA

Se utiliza cuando el tipo de
bulto es contenedor

0

0

3

0

0

0

0

3

3

3

Sello contenedor. Con digito
verificador

20

ALFA

Se utiliza cuando el tipo
de bulto es contenedor

N

0

0

3

0

0

0

0

3

3

3

Nombre emisor sello

70

ALFA

Se utiliza cuando el tipo
de bulto es contenedor

N

0

0

3

0

0

0

0

3

3

3

ALFA

Valor numérico de 14
enteros y cuatro
decimales, mayor que
cero

N

0

0

3

0

0

0

0

3

3

3

ALFA

Valor numérico de 14
enteros y cuatro
decimales, mayor que
cero

N

0

0

3

0

0

0

0

3

3

3

ALFA

Indicar el Código del país
del receptor extranjero de
la mercadería, según
tabla Países aduana

P

0

0

3

0

0

0

0

1

3

3

Monto del flete según moneda de
venta

Monto del seguro, según moneda de
venta

18

18

Análogo a Dirección Receptor

<CodPaisRecep>

Formato DTE

Validación

GUIA

Numero entero sin
decimales

Indique el código del tipo de bulto,
según tabla Tipos de Bultos ubicada
<CodTpoBultos> en www.aduana.cl

<CantBultos>
98

DESCRIPCIÓN

FACT

Versión 2.5 2026-02

3

I

Pág.28 de 51

OBLIGATORIEDAD
CAMPOS
Código País
105 Destino

DESCRIPCIÓN

Largo
Max

Análogo Dirección Destino

3

Tipo

ALFA

<CodPaisDestin>

106

FIN Sub-Area

TRANSPORTE.ADUANA

FIN AREA

TRANSPORTE

AREA
<Totales>

TOTALES

Tipo Moneda
Transacción
<TpoMoneda>

107

Monto neto
<MntNeto>

Monto no afecto o
108 exento
<MntExe>
Monto base
faenamiento
109 carne

Moneda en que se registra la
transacción de exportación.

*

I

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

Indicar el Código del país
del receptor extranjero de
la mercadería, según tabla
publicada en
www.aduana.cl

P

0

0

3

0

0

0

0

2

3

3

1

1

1

1

1

1

1

1

1

1

I

0

0

0

0

0

0

0

1

1

1

I

2

0

3

2

2

2

2

0

0

0

Todos los campos de
montos del documento
estarán indicados en esta
moneda.
15

ALFA

Suma de valores total de ítems afectos
-descuentos globales + recargos
globales (Asignados a ítems afectos).
Si está encendido el Indicador de
Montos Brutos (=1) entonces el resultado
anterior se debe dividir por
(1 + tasa de IVA)

Validación

FACT

Puede tener uno de los
valores indicados en el
schema, Por ejemplo:
“DOLAR USA”, “EURO”,
etc

Valor numérico de
acuerdo a descripción.
18

NUM

En Liquidaciones-Factura
puede tomar valor
negativo
Valor numérico de
acuerdo a descripción

Suma de valores total de ítems no
afectos o exentos -descuentos
globales + recargos globales
(Asignados a ítems exentos o no
afectos)

18

NUM

En Liquidaciones-Factura
puede tomar valor
negativo

I

2

1

3

2

2

2

2

1

1

1

Monto informado

18

NUM

Valores >0

I

2

0

3

2

2

0

0

0

0

0

Monto informado

18

NUM

Valor Numérico.

I

2

0

3

2

2

0

0

0

0

0

<MntBase>
Monto Base de
Márgenes de
110 Comercialización
<MntMargenCom>

Formato DTE

Versión 2.5 2026-02

Pág.29 de 51

OBLIGATORIEDAD
CAMPOS
111

112

113

114

DESCRIPCIÓN

Largo
Max

Tipo

5

NUM

Tasa IVA
<TasaIVA>

IVA
18

<IVA>

IVA propio
<IVAProp>

NUM

Las empresas que venden por cuenta
de un mandatario, pueden opcional
separar el IVA en propio y de terceros.
En todos estos casos el campo “IVA”
debe contener el IVA total de la
Factura

18

NUM

Ídem al anterior

18

NUM

TABLA de
Impuestos
Adicionales y
retenciones:

*

I

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

3 enteros, 2 decimales
En Porcentaje (Ej: 19.5)
Valor num.= a Monto neto
*tasa IVA
Mayor o igual a 0 excepto
en Liquidaciones-Factura,
en que puede tomar valor
negativo

I5

2

2

3

2

2

2

2

0

0

0

I

2

2

3

2

2

2

2

0

0

0

N

3

0

3

3

3

3

3

0

0

0

N

3

0

3

3

3

3

3

0

0

0

2

2

3

2

2

2

2

0

0

0

< que IVA

IVA terceros
<IVATerc>

Validación

FACT

En Liquidaciones-Factura
puede tomar valor
negativo
< que IVA
en Liquidaciones-Factura,
puede tomar valor
negativo

Se pueden incluir 20 repeticiones de
pares código – valor. Incluye los dos
campos siguientes.

<ImptoReten>

115

Código de
Impuesto
adicional o
Retención
<TipoImp>

116

Tasa de
Impuesto o
Retención
<TasaImp>

5

Código del impuesto o retención de
acuerdo a la codificación detallada en
tabla de códigos (ver Punto 4 del
índice).

3

ALFA

Código válido de impuesto
o retención (Ver Índice 4.Codificación Tipos de
Impuesto)

5

NUM

Según las tasa válida al
momento de la
transacción.

Incluye Retención de Cambio sujeto de
Construcción
Se debe indicar la tasa de Impuesto
adicional o retención. En el caso de
impuesto específicos se puede omitir

P6

2

2

2

2

2

2

2

0

0

0

I7

2

2

2

2

2

2

2

0

0

0

La impresión puede ser parte del título del campo

Formato DTE

Versión 2.5 2026-02

Pág.30 de 51

OBLIGATORIEDAD
CAMPOS

117

Valor del
Impuesto o
Retención.
<MontoImp>

DESCRIPCIÓN

Valor del impuesto o retención
asociado al código indicado
anteriormente

Largo
Max

18

Tipo

Validación

NUM

a) Tasa* (Suma de líneas
de detalle con código
de Impuesto adicional
o retención), excepto
Diesel, Gasolina,
margen de
comercialización e “Iva
anticipado faenamiento
carne”

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

I

2

2

2

2

2

2

2

0

0

0

b) Tasa * Monto base
faenamiento para Iva
anticipado faenamiento
carne
c) Valor numérico en
otros casos > 0

FIN TABLA

118

IVA no retenido
<IVANoRet>

119

Crédito especial
65% Empresas
Constructoras
<CredEC>

120

Garantía por
depósito de
envases o
embalajes (no
afecto)
<GrntDep>

121

Valor
Neto
Comisiones y
Otros Cargos

Impuestos Adicionales y retenciones:
Sólo en facturas de Compra en que
hay retención de IVA por el emisor y
Notas de Crédito o débito que
referencian facturas de compra.
No se registra si es igual a 0.

18

NUM

IVA - IVA Retenido por
producto

I

0

0

0

2

2

2

0

0

0

0

Artículo 21 del decreto ley N° 910/75.
Este Es el único código que opera en
forma opuesta al resto, ya que se resta
al IVA general

18

NUM

Valor num. = IVA *0,65

I

2

0

3

2

2

0

0

0

0

0

Sólo para empresas que usen envases
en forma habitual, por su giro principal.
Art.28, Inc3 Reglamento DL 825)
(Cervezas, Jugos, Aguas Minerales,
Bebidas Analcohólicas u otros
autorizados por Resolución especial).
Corresponde a la Sumatoria de las
líneas de detalle que indican Indicador
de facturación/ exención = 3

18

NUM

Valor Numérico de
acuerdo a descripción

I

2

2

0

2

2

0

0

0

0

0

18

NUM

I

0

0

0

2

2

2

2

0

0

0

Suma de detalle de Valores de
Comisiones y Otros Cargos

En Liquidaciones-Factura
puede tomar valor
negativo

<ValComNeto>

6

Valor numérico de
acuerdo a descripción.

En el título del campo, identificar si se trata de Impuesto adicional, especifico, retención y la tasa respectiva

7 La tasa puede ser parte del título del campo impreso

Formato DTE

Versión 2.5 2026-02

Pág.31 de 51

OBLIGATORIEDAD
CAMPOS

122

Valor Comisiones
y Otros Cargos
No Afectos o
Exentos

DESCRIPCIÓN
Suma de detalles de valores de
comisiones y otros cargos no afectos o
exentos

Largo
Max

Tipo

IVA Comisiones
y Otros Cargos
<ValComIVA>

124

Monto Total
<MntTotal>

Suma de detalle de IVA de Valor de
Comisiones y Otros Cargos

Monto neto + Monto no afecto o
exento + IVA + Impuestos Adicionales
+ Impuestos Específicos + Iva Margen
Comercialización +IVA Anticipado +
Garantía por depósito de envases o
embalajes - Crédito empresas
constructoras- IVA Retenido productos
(en caso de facturas de compra) Valor Neto Comisiones y Otros Cargos
- IVA Comisiones y Otros Cargos Valor Comisiones y Otros Cargos No
Afectos o Exentos.

18

NUM

18

NUM

128

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

En Liquidaciones-Factura
puede tomar valor
negativo.
Valores numéricos de
acuerdo a descripción.
En Liquidaciones-Factura
puede tomar valor
negativo

I

0

0

0

2

2

2

2

0

0

0

N

0

0

0

2

2

2

2

0

0

0

18

NUM

En LiquidacionesFactura, puede tomar
valor negativo

*

I

1

1

1

1

1

1

1

1

1

1

En Documentos de
exportación es “0” (cero) si
forma de pago es = 21 (sin
pago)

18

NUM

Valor Numérico
(Puede ser negativo)

N

2

2

2

2

2

2

0

0

0

0

Monto Total + Monto no Facturable

18

NUM

Valor Numérico
(Puede ser negativo)

N

3

3

3

3

3

3

3

0

0

0

<SaldoAnterior>

Saldo Anterior. Se incluye sólo con
fines de ilustrar con claridad el cobro.

18

NUM

Valor Numérico
(Puede ser negativo)

N

3

3

3

3

3

3

3

0

0

0

Valor a pagar

Valor cobrado

18

NUM

Valor Numérico sin
validación (Puede ser
negativo o cero)

N

3

3

3

3

3

3

3

0

0

0

Monto Período
<MontoPeriodo>

127

FACT
EXENT

Suma de montos de bienes o servicios
con Indicador de facturación/ exención
= 2 menos Suma de montos de bienes
o servicios con Indicador de
facturación/ exención = 6

Monto no
Facturable
<MontoNF>

126

I

Valor Numérico de acuerdo
a descripción

(Los Impuestos Adicionales y el IVA
Anticipado están detallados en la
TABLA de Impuestos Adicionales y
Retenciones)

125

*

GUIA

Valor Numérico de
acuerdo a descripción.

<ValComExe>

123

Validación

FACT

Saldo Anterior

<VlrPagar>
FIN AREA

Formato DTE

TOTALES ENCABEZADO

Versión 2.5 2026-02

Pág.32 de 51

OBLIGATORIEDAD
CAMPOS
AREA
<OtraMoneda>

129

Código Otra
moneda
<TpoMoneda>

130

Tipo de Cambio
<TpoCambio>

131

132

DESCRIPCIÓN

Largo
Max

Validación

*

I

3

Moneda alternativa en que se
expresan los Montos Totales.
En documentos de Exportación es
obligatorio informar este campo la
codificación de pesos chilenos
(PESO CL).
1. Factor de conversión utilizado de
pesos a Otra moneda
2. 6 enteros y 4 decimales
3. En documentos de Exportación
corresponde al tipo de cambio de
la fecha de emisión del
documento, publicado por el
Banco Central de Chile.
4. En documentos de Exportación
es obligatorio informar para la
conversión de otra moneda a
pesos chilenos, y se informa en
pesos chilenos.

Monto
base
faenamiento carne
133 Otra Moneda
Monto informado en Otra Moneda

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

3

3

3

FAC

OTRA MONEDA ENCABEZADO

Suma de valores total de ítems afectos
en Otra Moneda - descuentos globales
en Otra Moneda + recargos globales
Monto neto Otra
en Otra Moneda (Asignados a ítems
Moneda
afectos en Otra Moneda).
<MntNetoOtrMn
Si está encendido el Indicador de
da>
Montos Brutos (=1) entonces el
resultado anterior se debe dividir por
(1 + tasa de IVA)
Suma de valores total de ítems no
afectos o exentos en Otra Moneda descuentos globales en Otra Moneda
Monto no afecto
+ recargos globales en Otra Moneda
o exento en Otra
(Asignados a ítems exentos o no
Moneda
afectos en Otra Moneda)
<MntExeOtrMnd
En documentos de Exportación es
a>
obligatorio informar este campo en
pesos chilenos.

15

ALFA

Puede tener uno de los
valores indicados en el
schema, Por ejemplo:
“DOLAR USA”, “EURO”,
“PESO CL”, etc.

10

NUM

Valor numérico

3

2

3

2

3

2

3

2

3

2

3

P 2

2

2

2

2

N

3

3

2

3

3

3

3

3

3

3

I

3

0

3

3

3

3

0

0

0

0

I

3

3

3

3

3

3

0

3

3

3

I

3

0

3

3

3

0

0

0

0

0

14 enteros, 4 decimales
18

NUM

Valor numérico de
acuerdo a descripción.
Sin validación de fórmula

14 enteros, 4 decimales.
18

NUM

Valor numérico de
acuerdo a descripción
Sin validación de fórmula

18

<MntFaeCarneOtrM
nda>

Formato DTE

Tipo

FACT

Versión 2.5 2026-02

NUM

14 enteros, 4 decimales.
Valores >0

Pág.33 de 51

OBLIGATORIEDAD
CAMPOS

134

DESCRIPCIÓN

Monto informado en Otra Moneda
Monto Base de
Márgenes de
Comercialización
Otra Moneda

FACT

GUIA

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

0

0

0

2

2

0

0

0

2

2

2

0

0

0

Largo
Max

Tipo

Validación

18

NUM

Valor Numérico.

I

2

0

3

2

2

0

NUM

Sin validación. 14 enteros
y 4 decimales.
= a Monto neto en otra
moneda *tasa IVA
Mayor o igual a 0 excepto
Liquidaciones-Factura, en
que puede tomar valor
negativo

I

2

2

3

2

2

2

2

3

2

*

I

FACT
EXENT

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

<MntMargComO
trMnda>

135

IVA en otra
moneda

18

<IVAOtrMnda>

TABLA de
Impuestos
Adicionales y
retenciones en
Otra Moneda

Se pueden incluir 20 repeticiones de
pares código – valor. Incluye los dos
campos siguientes.

<ImpRetOtrMnd
a>

134

Código de
Impuesto
adicional o
Retención

Código del impuesto o retención de
acuerdo a la codificación detallada en
tabla de códigos (ver Punto 4 del
índice).

<TipoImpOtrMnda
>

Incluye Retención de Cambio sujeto de
Construcción

Tasa de
Impuesto o
135 Retención

Se debe indicar la tasa de Impuesto
adicional o retención. En el caso de
<TasaImpOtrMnda impuesto específicos se puede omitir
>

136

Valor del Impuesto Valor del impuesto o retención
o Retención.
asociado al código indicado

ALFA

5

NUM

Según las tasas válidas
al momento de la
transacción.

I9

2

2

2

2

2

2

2

0

0

0

NUM

a) Tasa* (Suma de líneas
de detalle con código
de Impuesto adicional
o retención), excepto
Diesel, Gasolina,
margen de

I

2

2

2

2

2

2

2

0

0

0

18

<VlrImpOtrMnda> anteriormente.

8

3

Código válido de impuesto
o retención (Ver Índice 4.Codificación Tipos de
Impuesto)

P8

2

2

2

2

2

2

2

0

0

0

En el título del campo, identificar si se trata de Impuesto adicional, especifico, retención y la tasa respectiva

9 La tasa puede ser parte del título del campo impreso

Formato DTE

Versión 2.5 2026-02

Pág.34 de 51

OBLIGATORIEDAD
CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ

FACT
EXPO

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

FAC

comercialización e “Iva
anticipado faenamiento
carne”
b) Tasa * Monto base
faenamiento para Iva
anticipado faenamiento
carne
c) Valor numérico en
otros casos > 0
FIN TABLA

137

IVA no retenido
Otra Moneda
<IVANoRetOtrM
nda>

138

Monto Total en
Otra Moneda
<MntTotOtrMnd
a>

Impuestos Adicionales y retenciones:
Sólo en facturas de Compra en que
hay retención de IVA por el emisor y
Notas de Crédito o débito que
referencian facturas de compra.
No se registra si es igual a 0.
Monto neto en Otra Moneda + Monto
no afecto o exento en Otra Moneda+
IVA en Otra Moneda+ Impuestos
Adicionales en Otra Moneda +
Impuestos Específicos En otra
Moneda+ Iva Margen Comercialización
en Otra Moneda + IVA Anticipado en
Otra Moneda - IVA Retenido productos
en Otra Moneda (en caso de facturas
de compra)

18

18

NUM

14 enteros 4 decimales.
Sin validación.
IVA en otra moneda - IVA
Retenido por producto en
otra moneda.

I

0

0

0

3

3

3

0

0

0

0

NUM

Valor Numérico
de acuerdo a descripción
14 enteros y 4 decimales
En Liquidaciones-Factura,
puede tomar valor
negativo.

I

2

2

2

2

2

2

2

2

2

2

Cuerpo numérico entre
100.000 y 99 millones,
guion y dígito verificador
alfanumérico entre 0 y 9
oK

N

3

3

3

3

3

3

3

3

3

3

N

3

3

3

3

3

3

3

3

3

3

En documentos de Exportación es
obligatorio informar este campo en
pesos chilenos.
RUT de la empresa proveedora del
sistema de emisión de boletas
electrónicas utilizado. Con guion y
dígito verificador
En caso de corresponder a un
desarrollo propio, debe informar el RUT
del emisor.

10

ALFA

Nombre o Razón Corresponde al Nombre o Razón social
Social Proveedor del Rut Proveedor. Si corresponde a un
<RznSocProvSW> desarrollo propio no informar.

80

ALFA

Rut Proveedor
<RutProvSW>

FIN AREA

Formato DTE

OTRA MONEDA ENCABEZADO

Versión 2.5 2026-02

Pág.35 de 51

B.- DETALLE DE PRODUCTOS O SERVICIOS
Corresponde a la información de un ítem. Debe ir al menos una línea de detalle. El máximo de ítems es de 60 y en un documento
se puede incluir sólo la cantidad de ítems que se pueda imprimir en una hoja, respetando la normativa de impresión del SII.

1

CAMPOS

DESCRIPCIÓN

N° de Línea o N°
Secuencial

Número del ítem. Desde 1 a 60

Largo
Max

Tipo

4

NUM

Número secuencial de la
línea.

10

ALFA

Sin validación.

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

* N

1

1

1

1

1

1

1

1

1

1

N

3

3

3

3

3

3

3

3

3

3

N

3

3

3

3

3

3

3

3

3

3

N

0

0

0

0

0

0

1

0

0

0

N

2

2

3

2

2

2

2

2

2

2

<NroLinDet>
TABLA de Códigos Se pueden incluir 5 repeticiones de
de Ítem
pares código – valor. Incluye los dos
campos siguientes.
2

Tipo código
<TpoCodigo>

Tipo de codificación utilizada para el
ítem

Ejemplo: EAN13, PLU,
DUN14, INT1, INT2,
EAN128, etc.

Standard: EAN, PLU, DUN o Interna
(Hasta 5 tipos de códigos)
3

Código del Ítem
<VlrCodigo>

Código del producto de acuerdo a
tipo de codificación indicada en campo
anterior

35

ALFA

3

ALFA Para liquidaciones se

(Hasta 5 códigos)
FIN TABLA
4

5

Tipo Documento
que se Liquida

Para liquidaciones se debe registrar el
código del docto. que se liquida.

<TpoDocLiq>

(Ej: :30, 33, 35, 39, 56, etc.)

Indicador de
facturación/
exención

Indica si el producto o servicio es
exento o no afecto a impuesto o si ya
ha sido facturado. (También se utiliza
para indicar garantía de depósito por
envases. Art.28,Inc3 Reglamento DL
825) (Cervezas, Jugos, Aguas
Minerales, Bebidas Analcohólicas u
otros autorizados por Resolución
especial)

<IndExe>

debe registrar código de
documento válido.
(electrónico o manual) o
99 en caso de Anticipo u
otras transacciones.
1

Si todos los ítems de una factura
tienen valor 1 en este indicador la
factura no puede ser factura
electrónica (código 33), debería ser
factura exenta (código 34).
Sólo en caso de Liquidación-Factura
que tenga ítems no facturables

NUM 1: No afecto o exento de

IVA (10)
2: Producto o servicio
no es facturable
3: Garantía de depósito
por envases (Cervezas,
Jugos, Aguas Minerales,
Bebidas Analcohólicas u
otros autorizados por
Resolución especial)
4: Ítem No Venta. (Para
facturas y guías de
despacho (ésta última
con Indicador Tipo de
Traslado de Bienes
igual a 1) y este ítem no

10 No se usa este campo si la factura es exenta en forma global.

Formato DTE

Versión 2.5 2026-02

Pág.36 de 51

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

será facturado.

negativos, se debe señalar el
indicador 2, e informar el valor con
signo negativo

5: Ítem a rebajar. Para
guías de despacho NO
VENTA que rebajan
guía anterior. En el área
de referencias se debe
indicar la guía anterior.
6: Producto o servicio
no facturable negativo
(excepto en
liquidaciones-factura)

AREA

RETENEDOR

<Retenedor>
6

Indicador Agente
Retenedor

0

3

2

2

2

0

0

0

0

NUM

I

2

0

3

2

2

2

0

0

0

0

18

NUM

I

2

0

3

2

2

2

0

0

0

0

18

NUM

I

2

0

3

2

2

0

0

0

0

0

I

1

1

1

1

1

1

1

1

1

1

I

3

3

3

3

3

3

3

3

3

ALFA

Sólo para transacciones realizadas por
Agentes Retenedores, según códigos
de retención 17

18

Sólo para transacciones realizadas por
Agentes Retenedores, según códigos
de retención 14 y 50

Precio Unitario Neto Sólo para transacciones realizadas por
Consumidor Final
Agentes Retenedores, según códigos
de retención 14, 17 y 50
<PrcConsFinal>

Monto Base
Faenamiento
<MntBaseFaena>

8

2

1

<IndAgente>
7

N

Obligatorio para agentes retenedores,
indica para cada transacción si es
agente retenedor del producto que está
vendiendo

Monto
Base
Márgenes
de
Comercialización

“R”

<MntMargComer>
9

10

FIN AREA

RETENEDOR

Nombre del Ítem

Nombre del producto o servicio

80

ALFA

Descripción Adicional del producto o
servicio. Se utiliza para pack, servicios
con detalle

1000

ALFA

Sin Validación

*

<NmbItem>

11

Descripción
Adicional
<DscItem>

Formato DTE

Versión 2.5 2026-02

Sin Validación

3

Pág.37 de 51

12

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

Cantidad de
referencia

Cantidad para la unidad de medida de
referencia (no se usa para el cálculo del
valor neto) en 12 enteros y 6 decimales.

18

NUM

Sin validación

<QtyRef>

14

Unidad de
referencia

Glosa con unidad de medida de
referencia

<UnmdRef>

Obligatorio para facturas de venta,
compra o notas que indican emisor
opera como Agente Retenedor

Precio de referencia Precio unitario para la unidad de
medida de referencia (no se usa para el
<PrcRef>
cálculo del valor neto) 12 enteros, 6
decimales.

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

N

2

3

2

2

2

2

3

3

3

3

N

2

3

2

2

2

2

3

3

3

3

En Guías de Despacho,
y en Indicador de tipo de
transporte 8 o 9, es
obligatoria si el campo
Cantidad no está en la
unidad Kgs brutos

Obligatorio para facturas de venta o
compra que indican emisor opera
como Agente Retenedor
13

*

4

ALFA

Sin validación
En Guías de Despacho
con Indicador de tipo de
Traslado de Bienes 8 o
9, es obligatoria si el
campo Cantidad no está
en la unidad Kgs brutos.
Adicionalmente en dicho
caso se debe utilizar
tabla de unidades de
Aduanas

18

NUM

Valor numérico 12
enteros, 6 decimales

N

2

3

3

2

2

2

3

3

3

3

18

NUM

Valor numérico 12
enteros, 6 decimales

I

2

3

1

2

2

2

3

2

2

2

N

3

3

3

3

3

3

3

3

3

3

Valor numérico <=
Cantidad

N

3

3

3

0

0

3

3

3

3

3

Sin validación

N

3

3

3

0

0

3

3

3

3

3

Obligatorio para facturas de venta,
compra o notas que indican emisor
opera como Agente Retenedor
15

Cantidad
<QtyItem>

Cantidad del ítem en 12 enteros y 6
decimales
Obligatorio para facturas de venta,
compra o notas que indican emisor
opera como Agente Retenedor

TABLA
de
Distribución de la
Cantidad

En Facturas de
Exportación Campo
obligatorio a excepción
cuando en el “Indicador
de Servicio” se registra
el valor 3, 4 o 5

Se pueden incluir 5 repeticiones de
pares cantidad – código. Incluye los
dos campos siguientes:

<Subcantidad>

16

Subcantidad_Distrib Cantidad del ítem en 12 enteros y 6
uida
decimales.

18

NUM

<SubQty>
17

Código subcantidad Código descriptivo. Se repite hasta
cinco veces.
<SubCod>

Formato DTE

Versión 2.5 2026-02

35

Pág.38 de 51

18

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

Tipo Código
Subcantidad

Sólo para documentos exportación

10

ALFA

Sin Validación

Del ítem

10

ALFA Fecha valida

Del ítem

10

Unidad de medida

4

*

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

LIQ
FAC

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

0

0

0

0

0

0

3

3

3

N

3

3

3

0

0

3

3

3

3

3

ALFA Fecha valida

N

3

3

3

0

0

3

3

3

3

3

ALFA Obligatorio para facturas

I

2

3

1

2

2

2

3

2

2

2

I

2

2

2

2

2

2

3

3

3

3

3

3

3

3

3

3

0

3

3

3

2

2

2

2

2

2

0

2

2

2

<TipCodSubQty>
FIN TABLA
19

Fecha elaboración
<FchElabor>

20

Fecha vencimiento
<FchVencim>

21

Unidad de Medida

de venta, compra o notas
que indican emisor opera
como Agente Retenedor

<UnmdItem>

En Facturas de
Exportación Campo
obligatorio a excepción
cuando en el “Indicador
de Servicio” se registra
el valor 3, 4 o 5. En
dicho caso se debe
utilizar tabla de
unidades de Aduanas

22

Precio Unitario del
Ítem

12 enteros, 6 decimales.

18

NUM Valor numérico

Para documentos de
traslados que no importen
venta podrá omitirse el
valor unitario.

<PrcItem>

23

TABLA

OTRA MONEDA DETALLE Hasta

<OtrMnda>

2 repeticiones para indicar
precios en monedas alternativas.

Precio unitario en
otra moneda

14 enteros, 4 decimales.

<PrcOtrMon>

Formato DTE

Versión 2.5 2026-02

18

NUM

14 enteros 4 decimales.
Obligatorio en Guías de
Despacho con Indicador
de tipo de Traslado de
Bienes = 9

N

Pág.39 de 51

24

<FctConv>

26

Descuento en Otra
Moneda
<DctoOtrMnda>

27

Recargo en Otra
Moneda
<RecargoOtrMnda>

28

Valor por línea de
detalle en Otra
Moneda

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

2

2

2

2

0

2

2

2

3

3

0

3

3

3

3

3

3

0

3

3

3

2

2

2

2

0

2

2

2

3

3

3

3

3

0

3

3

3

2

2

3

2

2

2

0

3

3

3

N

3

3

3

3

3

3

0

3

3

3

N

3

3

3

3

3

3

0

3

3

3

Indica moneda del campo anterior
“Precio Unitario en otra moneda”

3

ALFA

En Guía de Despacho
se debe indicar si se
informa un Precio
Unitario en otra
moneda, según tabla
Banco Central

N

2

2

Factor para convertir a $

10

NUM

Valor numérico

N

2

Dinero correspondiente al Descuento
en %. Totaliza todos los descuentos
otorgados al ítem en otra moneda

18

NUM Valor numérico. 14

N

Dinero correspondiente al Recargo en
%. Totaliza todos los recargos
otorgados al ítem en otra moneda

18

(Precio Unitario en otra moneda *
Cantidad) – Descuento en otra
moneda + Recargo en otra moneda.

18

Descuento (%) en 3 enteros y 2
decimales

5

NUM

18

NUM

Código otra
Moneda

Factor de
Conversión

FACT.
EXPOR

Tipo

DESCRIPCIÓN

<Moneda>

25

FACT

Largo
Max

CAMPOS

*

I

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

2

2

2

2

2

2

2

2

3

3

3

3

N

3

3

3

I

2

2

Valor numérico

N

3

Si va el descuento en
%, debe ir el monto
correspondiente.

I

Validación

FACT
EXENT

GUIA

LIQ
FAC

6 enteros y 4 decimales
En documentos de Exportación
corresponde al tipo de cambio de la
fecha de emisión del documento,
publicado por el Banco Central de
Chile.
enteros 4 decimales. Sin
validación.
NUM Valor numérico. 14

enteros 4 decimales. Sin
validación.
NUM

Valor numérico, 14
enteros y 4 decimales.
Obligatorio en Guías de
Despacho con Indicador
de tipo de Traslado de
Bienes = 9

<MontoItemOtrMnd
a>
FIN TABLA
29

Descuento en %
<DescuentoPct>

30

31

Monto Descuento

Correspondiente al anterior. Totaliza
todos los descuentos otorgados al
<DescuentoMonto> ítem
TABLA
de
Distribución del
Descuento

Se pueden incluir 5 repeticiones de
pares Tipo – Valor. Incluye los tres
campos siguientes:

Subdescuento-Tipo
de

Indica si el Subdescuento está en $ o
%

1

ALFA

"$" o "%"

<TipoDscto>

Formato DTE

Versión 2.5 2026-02

Pág.40 de 51

32

FACT

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Subdescuentovalor

16 enteros, 2 decimales

18

NUM Sin validación

N

3

3

Recargo (%) en 3 enteros y 2
decimales

5

NUM Valor numérico

N

2

Correspondiente al anterior. Totaliza
todos los recargos otorgados al ítem

18

NUM Si va el recargo en

I

Validación

*

I

FACT
EXENT

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

3

3

3

2

0

3

3

3

2

2

0

3

3

3

3

3

3

0

3

3

3

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

3

3

3

3

2

3

3

3

2

2

3

2

N

3

3

3

GUIA

LIQ
FAC

<ValorDscto>
FIN TABLA
33

Recargo en %
<RecargoPct>

34

Monto Recargo
<RecargoMonto>

TABLA
de
Distribución del
Recargo

%, debe ir el monto
correspondiente.

Se pueden incluir 5 repeticiones de
pares Tipo – Valor. Incluye los tres
campos siguientes:

<SubRecargo>

35

Sub-recargo-Tipo

Indica si el Sub-recargo está en $ o %

1

ALFA

"$" o "%"

N

3

3

3

3

3

3

0

3

3

3

16 enteros, 2 decimales

18

NUM

Sin validación

N

3

3

3

3

3

3

0

3

3

3

3

3

3

3

3

3

0

0

0

0

2

2

3

2

2

2

0

0

0

0

<TipoRecargo>
36

Sub-recargo- valor
<ValorRecargo>
FIN TABLA

TABLA de Códigos Se pueden incluir 2 repeticiones de
de
Impuesto códigos de impuesto o retención.
Adicional
y
Retenciones
37

Código Impuesto o Indica el código según tabla de
retenciones
códigos (Ver en Índice 4.- Codificación
Tipos de Impuesto).
<CodImpAdic>

6

ALFA De acuerdo con tabla de

N

codificación de
Impuestos en punto 4.

FIN TABLA

Formato DTE

Versión 2.5 2026-02

Pág.41 de 51

CAMPOS
38

DESCRIPCIÓN

Largo
Max

Tipo

18

NUM

Monto Ítem
(Valor por línea de
detalle)

(Precio Unitario * Cantidad) – Monto
Descuento + Monto Recargo

<MontoItem>

Validación

*

Valor numérico, de
acuerdo con descripción
y:
1) Debe ser cero
cuando:
•
Indicador de
facturación/ exención
tiene valor 4 o 5
• Es una Nota de
Crédito tipo fe de
erratas.(Ver campo
Código
de
Referencia
en
Referencias)

*

2)

Puede ser cero
cuando
el
documento es una
Guía de despacho
NO VENTA (Según
campo
Indicador
Tipo de traslado de
bienes
del
encabezado)

3)

En liquidaciones
factura puede ser
negativo.

I

I

FACT

1

FACT
EXENT

1

GUIA

1

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

1

1

1

LIQ
FAC

1

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

1

1

1

(11)

CUANDO ES CERO
PUEDE NO
IMPRIMIRSE o
Imprimirse un texto
explicatorio (s/valor, sin
costo, etc)

(11) En el caso que la Factura sea exenta, se entenderá que éste valor es el Valor exento por línea de detalle; lo mismo se apli ca cuando el ítem se ha marcado como no
afecto o exento a través del campo b4. En el resto de los casos, se entenderá que este valor corresponde al valor neto por línea de detalle.
Formato DTE

Versión 2.5 2026-02

Pág.42 de 51

C.- SUBTOTALES INFORMATIVOS
Pueden ser de 0 hasta 20 líneas. Estos subtotales no aumentan o disminuyen la base del impuesto, ni modifican los campos
totalizadores, sólo son campos informativos.
Estos subtotales tienen una glosa que especifica el concepto. Por ejemplo un subtotal aplicado a un determinado grupo de productos,
servicios o elementos.
En la representación impresa, estos subtotalizadores pueden intercalarse entre las líneas de detalle, o indicarse en forma agrupada en
una sección aparte.
N°

CAMPOS

DESCRIPCIÓN

Largo
Max

Número Subtotal
1

Tipo

Validación

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

1

1

1

LIQ FACT.
FAC EXPOR

Número de Subtotal

2

Número secuencial de
NUM acuerdo al número de
subtotales

N

1

1

1

1

1

1

Título para Subtotal

40

ALFA Sin validación

N

1

1

1

1

1

1

1

1

1

1

Ubicación para Impresión

2

NUM

Sin validación. De uso para
el contribuyente como
N
ayuda para indicar como
imprimirá subtotales.

3

3

3

3

3

3

3

3

3

3

Valor Neto del Subtotal

18

NUM

16 Enteros y 2 decimales.
Aplica en subtotales en $ u
N
otra moneda. SIN
VALIDACIÓN

3

3

3

3

3

3

3

0

0

0

Valor del IVA del Subtotal

18

16 Enteros y 2 decimales.
Aplica en subtotales en $ u
NUM
N
otra moneda. SIN
VALIDACIÓN

3

3

3

3

3

3

3

0

0

0

Valor de los Impuestos
adicionales o específicos del
Subtotal

18

NUM

16 Enteros y 2 decimales.
Aplica en subtotales en $ u
N
otra moneda. SIN
VALIDACIÓN

3

3

3

3

3

3

3

0

0

0

Valor no Afecto o Exento del
Subtotal

18

16 Enteros y 2 decimales.
Aplica en subtotales en $ u
NUM
N
otra moneda. SIN
VALIDACIÓN

3

3

3

3

3

3

3

3

3

Valor de la línea de subtotal

18

NUM

16 Enteros y 2 decimales.
Aplica en subtotales en $ u
N
otra moneda. SIN
VALIDACIÓN

3

3

3

3

3

3

3

3

3

3

2

Número de línea de
NUM detalle.
Hasta 60 repeticiones

3

3

3

3

3

3

3

3

3

3

<NroSTI>

1

Glosa
2
<GlosaSTI>
Orden
3
<OrdenSTI>
Subtotal Neto
4
<SubTotNetoSTI>
Subtotal IVA
5
<SubTotIVASTI>
Subtotal Impuestos
adicionales o
6 específicos
<SubTotAdicSTI>

7

Subtotal no
Afecto o Exento
<SubTotExeSTI>
Valor del Subtotal

8
<ValSubtotSTI>
LINEAS
9
<LineasDeta>

Formato DTE

Versión 2.5 2026-02

N

Pág.43 de 51

D.- INFORMACIÓN DE DESCUENTOS O RECARGOS
<DscRcgGlobal>
Pueden ser de 0 hasta 20 líneas. Estos aumentan o disminuyen la base del impuesto.
Estos descuentos o recargos tienen una glosa que especifica el concepto. Por ejemplo un descuento global aplicado a un determinado tipo de producto o un
descuento por pago contado que afecta a todos los ítems.
En caso que se apliquen descuentos o recargos globales y
a) en la Zona de Detalle hayan ítems con distintos códigos de impuesto o retenciones, el campo “tipo de valor” del descuento debe ser %.
b) En la Zona de Detalle hayan algunos ítems afectos, otros exentos y otros no facturables (con “Indicador de Facturación Exención”=1 o 2), hay tres casos:
• Si el descuento afecta sólo a los ítems exentos se debe indicar un 1 en el “Indicador de Facturación/Exención”
• Si el descuento afecta sólo a los ítems afectos no debe llevar el “Indicador de Facturación/Exención”
• Si el descuento/recargo afecta sólo a los ítems no facturables se debe indicar un 2 en el “Indicador de Facturación/exención”
• Si el descuento afecta a todos, deben haber tres líneas: Una con el descuento para el descuento de los afectos, otra para el descuento de los
exentos y otra para los no facturables.

N°

1

CAMPOS
N° de Línea o N°
Secuencial

DESCRIPCIÓN

Largo
Max

I

FACT

FACT
EXENT

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

N

1

1

1

1

1

1

0

Validación

Tipo

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

1

1

1

LIQ FACT.
FAC EXPOR

Número de descuento o recargo.
De 1 a 20.

2

Número secuencial de la línea.
La obligatoriedad se refiere a
que si se incluye esta zona
NUM
debe haber al menos una línea
y este caso debe ir el dato de
número de línea.

D(descuento) o R(recargo)

1

ALFA D o R

N

1

1

1

1

1

1

0

1

1

1

Especificación de descuento o
recargo

45

ALFA Sin Validación

I

3

3

3

3

3

3

0

3

3

3

Indica si es Porcentaje o
Monto

1

ALFA “%” o “$”

I

1

1

1

1

1

1

0

1

1

1

Valor del descuento o recargo
en 16 enteros y 2 decimales

18

Sin validación. Monto si tipo de
NUM valor es Monto
(Porcentaje otro caso)

I

1

1

1

1

1

1

0

3

3

3

Valor en otra moneda

18

Sin validación. 14 Enteros y 4
NUM decimales. Aplica en montos de
desctos. o recargos

I

3

3

3

3

3

3

0

1

1

1

Indica si el descuento o
recargo afecta a ítems exentos
o no afectos a IVA.

1

NUM

N

2

2

2

2

2

2

0

2

2

2

<NroLinDR>
Tipo de movimiento
2
<TpoMov>
Glosa
3
<GlosaDR>
4

Tipo de valor
<TpoValor>
Valor

5
<ValorDR>
Valor en otra moneda
6
<ValorDROtrMnda>

7

Indicador de
facturación/ exención
<IndExeDR>

Formato DTE

Versión 2.5 2026-02

1: No afecto o exento de IVA
2: No facturable

Pág.44 de 51

E.- INFORMACIÓN DE REFERENCIA
De 0 a 40 posibles repeticiones.
N°

CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

I FACT FACEXE

GUIA

NOTA
CRED

NOTA
DEB

FAC
COMP

LIQ

FACT
EXPO

FAC

1

N° Línea o N° Sec.
<NroLinRef>

2

Tipo Documento de
referencia
<TpoDocRef>

Formato DTE

Número de la referencia. De 1 a 40

2

NUM

Número secuencial de la línea.

Indica si el documento de referencia
es:
30: Factura
32: Factura de venta bienes y servicios
no afectos o exentos de IVA
35: Boleta
38: Boleta exenta
45: Factura de compra
48: Comprobante de pago electrónico
55: Nota de débito
60: Nota de crédito
103: Liquidación
40: Liquidación Factura
43: Liquidación-Factura Electrónica
33: Factura Electrónica
34: Factura No Afecta o Exenta
Electrónica
39: Boleta Electrónica
41: Boleta Exenta Electrónica
46: Factura de Compra Electrónica.
56: Nota de Débito Electrónica
61: Nota de Crédito Electrónica
50: Guía de Despacho.
52:Guía de Despacho Electrónica
110: Factura de Exportación
Electrónica
111: Nota de Débito de Exportación
Electrónica
112: Nota de Crédito de Exportación
Electrónica
801: Orden de Compra
802: Nota de pedido
803: Contrato
804: Resolución
805: Proceso ChileCompra
806: Ficha ChileCompra
807: DUS
808: B/L (Conocimiento de embarque)
809: AWB (Air Waybill)
810: MIC/DTA
811: Carta de Porte
812: Resolución del SNA donde
califica Servicios de Exportación
813: Pasaporte
814: Certificado de Depósito Bolsa
Prod. Chile.
815: Vale de Prenda Bolsa Prod. Chile
820: Código de Inscripción en el
Registro de Acuerdos con Plazo de
Pago Excepcional

3

ALFA

De acuerdo con la Descripción
Si se requiere referenciar un
documento tributario se debe
utilizar un valor Numérico que
debe estar en el rango indicado
en la descripción.

Versión 2.5 2026-02

NOTA NOTA
CRED DEBIT
EXPO EXPO

N

1

1

1

1

1

1

1

1

1

1

I

1

1

1

1

1

1

1

1

1

1

Si es alfabético no hay
validación y el contribuyente
puede usarlo para referenciar
documentos no tributarios y
distintos de los especificados.
En el caso de factura de
exportación se puede indicar un
DUS por factura,
En el caso de exportaciones por
vía terrestre y servicio de
transporte
internacional
(“Indicador Servicio”=5), se
puede indicar sólo una Carta de
Porte por factura.
En el caso de la Nota de Crédito
y de Débito de Exp. es obligatorio
referenciar
la
factura
de
exportación que modifica.
Por cada Guía de Despacho se
puede referenciar sólo 1 DUS o
MIC

Pág.45 de 51

821: Geo Referencia Predio
822: ROL Avalúo Predio
823: Plan de Manejo – CONAF

1
3

Indicador de
Referencia Global
<IndGlobal>

Documento afecta a un número de
más de 20 documentos del mismo
Tipo Documento de referencia

NUM Valor =1
Ejemplo: Factura de
todas las guías del
mes.

2

2

2

2

2

2

2

2

2

2

1

1

1

1

1

1

1

1

1

1

Se explicita la Razón en Razón
Referencia
18
4

FOLIO- de
referencia

Identificación
referencia.

del

documento

de

<FolioRef>

5

RUT
Otro
contribuyente
<RUTOtr>

6

Identificador
Adicional de otro
contribuyente

Sólo si el documento de referencia es
de tipo tributario y fue emitido por otro
12

10

ALFA Cuerpo numérico entre 100.000 y N
99 millones, guion y dígito
verificador alfanumérico entre 0 y
9o K

0

0

0

2

2

2

0

3

3

3

20

ALFA Sin validación

N

0

0

0

0

0

0

0

3

3

3

I

1

1

1

1

1

1

1

1

1

1

N

3

3

3

1

1

3

3

3

1

1

contribuyente
(Con guion y dígito verificador)
Código de identificación adicional para
uso libre

Folio de documento que
ALFA referencia.
I
Debe ser cero sólo si el
documento tiene encendido el
Indicador de referencia global.
Puede ser alfanumérico si se trata
de un documento no tributario
(rango del 800)

<IdAdicOtr>
7

FECHA de la
Referencia

Fecha del docto de referencia

10

ALFA

Fecha válida entre
2002-08-01 y 2050-12-31

<FchRef>
8

Código de
referencia
<CodRef>

12

Código utilizado para los siguientes
1
casos:
a) Nota de Crédito que elimina
documento de referencia en forma
completa (Factura de venta, Nota
de débito, o Factura de compra
b) Nota de crédito que corrige un
texto del documento de referencia
(ver campo Corrección Factura)
c) Nota de Débito que elimina una
Nota de Crédito en la referencia en
forma completa
d) Notas de crédito o débito que
corrigen montos de otro
documento
CASOS a) b) y c) DEBEN TENER UN
ÚNICO
DOCUMENTO
DE
REFERENCIA.

NUM

1: Anula Documento de
Referencia
2: Corrige Texto Documento de
Referencia
3: Corrige montos

Esto se aplica cuando: i) se emiten Facturas de Compra por bienes y se debe referenciar el número de la Guía de Despacho emitida por el Vendedor; ii) emitir Notas de Crédito o Débito que
referencian DTE emitido por contribuyente fusionado o absorbido. No se usa para referenciar una Orden de Compra porque éste no es un documento tributario.
Formato DTE
Versión 2.5 2026-02
Pág.46 de 51

9

Razón referencia
<RazonRef>

Formato DTE

Explicitar razón. Ejemplo una Nota de 90
Crédito que hacer referencia a una
factura, indica "descuento por pronto
pago" o "error en precio" etc.

Versión 2.5 2026-02

ALFA Sin validación

3

3

3

3

3

3

3

3

3

Pág.47 de 51

3

F.- COMISIONES Y OTROS CARGOS
Pueden ser de 0 hasta 20 líneas. No modifican la base del impuesto de la operación principal.
Se incorpora en caso que se apliquen comisiones/otros cargos, obligatoriamente en Liquidaciones-Factura Electrónicas y
opcionalmente en Facturas de Compra Electrónica, o en Notas de Crédito/Débito Electrónicas que corrijan Facturas de Compra.
N°

CAMPOS

DESCRIPCIÓN

Largo

Tipo

Validación

I

Max
1

N° de Línea o N°
Secuencial

Número de comisión u otro cargo.
De 1 a 20.

2

NUM

Número secuencial de la línea. La obligatoriedad
se refiere a que si se incluye esta zona debe haber
al menos una línea y este caso debe ir el dato de
número de línea.

N

1

1

1

1

C (comisión) u O (otros cargos)

1

ALFA

“C” u “O”

N

1

1

1

1

Especificación de la comisión u otro
cargo

60

ALFA

Sin Validación

I

1

1

1

1

Valor porcentual de la comisión u
otro cargo, en 2 enteros y 2
decimales

4

NUM

Sin Validación

I

3

3

3

3

Valor Neto de la comisión/otro cargo

18

NUM

En Notas de Crédito, Notas de Débito y Facturas
de Compra.

I

1

1

1

1

I

1

1

1

1

I

2

2

2

2

<NroLinCom>
2

Tipo de movimiento

NOTA NOTA FACT. LIQCRÉD DÉB COMP FACT

<TipoMovim>
3

Glosa
<Glosa>

4

Tasa comisión u otro
cargo
<TasaComision>

5

Valor Comisión Neto
<ValComNeto>

Puede ser cero si el Valor Comisión Exento es
distinto de cero.
En Liquidaciones-Factura puede ser negativo
6

Valor Comisión Exento
<ValComExe>

Valor Exento de la comisión/otro
cargo

18

NUM

En Notas de Crédito, Notas de Débito y Facturas
de Compra:
Puede ser cero si el Valor Comisión Neto es
distinto de cero.
En Liquidaciones-Factura puede ser negativo

7

Valor IVA Comisión u
Otro Cargo

Valor del IVA de la comisión/otros
cargos

<ValComIVA>

18

NUM

Valor * Tasa IVA
En Notas de Crédito, Notas de Débito y Facturas
de Compra.
En Liquidaciones-Factura puede ser negativo

Formato DTE

Versión 2.5 2026-02

Pág.48 de 51

G.-TIMBRE ELECTRÓNICO SII DEL DOCUMENTO
Largo
Max

N°

CAMPOS

DESCRIPCIÓN

1

Timbre
Electrónico
del
Documento. Corresponde a una
firma electrónica sobre los datos
principales del DTE

Contiene la firma Electrónica sobre
campos representativos del DTE, fecha y
hora de generación del timbre electrónico
y el Código de Autorización de Folios
(CAF) entregado por el SII. Corresponde a
la información del Código de Barras
Bidimensional PDF417

Tipo

Validación

ALFA

Ejemplo Campos representativos: Rut
Emisor, Rut Receptor, Tipo Documento,
Folio, IVA, Monto Neto y CAF
Para una descripción detallada véanse
Anexos de Instructivo de Generación de
documentos.

H.- FECHA Y HORA DE FIRMA DIGITAL DEL DOCUMENTO COMPLETO
N°

CAMPOS

DESCRIPCIÓN

1

Fecha y hora de la firma digital
del DTE

Fecha y hora en formato AAAA-MMDDTHH:MI:SS

Largo

Tipo

Validación

19

ALFA

Fecha y hora válidas en formato indicado

I.- DATOS DE MANEJO DE LA MADERA
Datos opcionales para indicar Georreferenciación.
CAMPOS

DESCRIPCIÓN

Largo
Max

Tipo

Validación

*

I

FACT

FACT
EXENT

N

1

0

GUIA

NOTA
CRED

NOTA
DEBIT

FACT.
COMP

0

0

0

LIQ
FAC

FACT.
EXPOR

NOTA
CRED
EXPO

NOTA
DEBIT
EXPO

0

0

0

Comuna del Rol Predial
Corresponde al código de la comuna
de Origen
del Rol Predial de Origen
<ComunaRolOrigen>

6

Código Conara de la
Comuna
NUM
*
https://zeus.sii.cl/avalu_cgi
/br/brch10.sh

Manzana del Rol Predial
Corresponde al número de la
de Origen
manzana del Rol Predial de Origen
<MnzRolOrigen>

6

NUM

N

1

0

1

0

0

0

0

0

0

0

Número del predio del
Corresponde al número del predio del
Rol Predial de Origen
Rol Predial de Origen
<PrdRolOrigen>

6

NUM

N

1

0

1

0

0

0

0

0

0

0

Comuna del Rol Predial
Corresponde al código de la comuna
de Destino
del Rol Predial de Destino
<ComunaRolDestino>

6

Código Conara de la
*
NUM Comuna
https://zeus.sii.cl/avalu_cgi/
br/brch10.sh

N

1

0

1

0

0

0

0

0

0

0

Manzana del Rol Predial
Corresponde al número de la
de Destino
manzana del Rol Predial de Destino
<MnzRolDestino>

6

NUM

N

1

0

1

0

0

0

0

0

0

0

Formato DTE

Versión 2.5 2026-02

1

0

Pág.49 de 51

Número del predio del
Corresponde al número del predio del
Rol Predial de Destino
Rol Predial de Destino
<PrdRolDestino>

6

NUM

N

1

0

1

0

0

0

0

0

0

0

Código Plan de Manejo
Corresponde al código del plan de
Conaf
manejo Conaf
<CodPlanConaf>

40

ALFA

N

1

0

1

0

0

0

0

0

0

0

Aviso Ejecución de Corresponde al código del aviso de
Faena
inicio de ejecución de faena
<AvisoejecucionFaena>

40

ALFA

N

3

0

3

0

0

0

0

0

0

0

30

ALFA

1

0

0

0

0

0

0

0

30

ALFA

30

ALFA

30

ALFA

Valor que corresponde a la latitud de
Latitud
la ubicación geográfica de Origen de
<LatitudOrigenMadera
la madera en el estándar WGS84 en
>
su modalidad decimal
Valor que corresponde a la longitud
Longitud
de ubicación geográfica de Origen de
<LongitudOrigenMadera
la madera en el estándar WGS84 en
>
su modalidad decimal
Valor que corresponde a la latitud de
Latitud
la ubicación geográfica de Destino de
<LatitudDestinoMadera
la madera en el estándar WGS84 en
>
su modalidad decimal
Valor que corresponde a la longitud
Longitud
de ubicación geográfica de Destino
<LongitudDestinoMader
de la madera en el estándar WGS84
a>
en su modalidad decimal
Sistema de Referencia Identifica el código del sistema de
<SistemaReferenciaMd referencia de la georreferenciación.
era>

*

1

* N

1

0

*

N

1

0

1

0

0

0

0

0

0

0

*

N

1

0

1

0

0

0

0

0

0

0

*

N

1

0

1

0

0

0

0

0

0

0

*

N

1

0

1

0

0

0

0

0

0

0

NUM 1. WGS84

J.- FIRMA DIGITAL DEL DOCUMENTO COMPLETO
Largo
Max

N°

CAMPOS

DESCRIPCIÓN

1

Certificado Digital

Información pública del Certificado Digital
necesaria para validar la firma.

Certificado vigente, no revocado y
autorizado ante el SII al momento de
generar la firma

Firma Electrónica

Firma electrónica sobre todo el
documento. (Encabezado, Detalle,
Descuentos - Recargos, Información de
Referencia, Fecha y Hora de Firma del
DTE y Timbre Electrónico.)

Firma electrónica según el estándar XML
Digital Signature. Para descripción
detallada véase Schema XML del DTE
definido por el SII y el sitio:
http://www.w3.org/TR/2002/REC-xmldsigcore-20020212/

2

Formato DTE

Versión 2.5 2026-02

Tipo

Validación

Pág.50 de 51

3.- FORMATO DE IMPRESIÓN DE DOCUMENTOS
Se elimina este capítulo por estar contenida en MANUAL DE MUESTRAS IMPRESAS en www.sii.cl SISTEMA DE FACTURACIÓN DE
MERCADO, opción Ayudas

4.- CODIFICACIÓN TIPOS DE IMPUESTOS y RECARGOS
Código
cambio de
Código sujeto en
retención
total
14

15

Nombre

Descripción general

IVA de margen de
comercialización

Para Facturas de venta del contribuyente

Documentos en que se aplica

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

Corresponde al IVA retenido en Facturas Factura de Compra emitida cod (45, 46)
de compra del contribuyente que genera el Notas de Crédito cod (60, 61)
libro.

IVA retenido total

Suma de retenciones con tasa de IVA

Notas de Débito (55, 56)

17

IVA ANTICIPADO
FAENAMIENTO CARNE

Tasa de 5% sobre Monto base
faenamiento. Se registra el monto de IVA
anticipado cobrado al cliente.

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

18

IVA ANTICIPADO CARNE

Tasa de 5%. Se registra el monto de IVA
anticipado cobrado al cliente.

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

19

IVA ANTICIPADO HARINA

Tasa de 12%. Se registra el monto de IVA
anticipado cobrado al cliente.

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

23

IMPUESTO ADICIONAL
Art 37 Letras a, b, c

Tasa del 15%
a) Artículos oro, platino, marfil
b) Joyas, piedras preciosas
c) Pieles finas

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

24

DL 825/74, ART. 42, letra b)

Tasa del 31,5%
Licores,
Piscos, whisky, aguardiente, y vinos
licorosos o aromatizados.

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

25

DL 825/74, ART. 42, letra c)

Tasa del 20,5%
Vinos

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

26

DL 825/74, ART. 42, letra c)

Tasa del 20,5%
Cervezas y bebidas alcohólicas

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

27

DL 825/74, ART. 42, letra a)

Tasa del 10%
Bebidas analcohólicas y minerales

Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

Formato DTE

Observaciones

Versión 2.5 2026-02

Pág.51 de 51

Código
cambio de
Código sujeto en
retención
total

Nombre

Descripción general

Tasa del 18%
DL 825/74, ART. 42, letra a) Bebidas analcohólicas y Minerales con
Inciso Segundo
elevado contenido de azúcares. (según
indica la ley)

271

28

301

31

Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)
Se usa en las Facturas que emite el vendedor. Se
registra en el IEV.
En el IEC se registra separado sólo si el comprador
tiene derecho al crédito; en caso contrario va en el
campo “Impuesto sin derecho a crédito”

Impuesto específico diésel

IVA RETENIDO
LEGUMBRES

• Si se retuvo el 10%, el monto retenido se
registra en el IEC en Retención parcial

Factura de Compra emitida cod (45, 46)

• Si se retuvo el total del IVA, por ser NDF
se registra también en Retención Total.

Notas de Débito cód. (55, 56)

IVA RETENIDO
SILVESTRES

• Total del IVA retención. El monto retenido
se registra en el IEC en Retención total.

Notas de Crédito cód (60, 61)

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
Notas de Débito cód. (55, 56)

Normalmente 8% retención.
32

321

IVA RETENIDO GANADO

• Si se retuvo el 8%, el monto retenido se
registra en el IEC en Retención parcial

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)

• Si se retuvo el total del IVA, por ser NDF,
se registra en el IEC en Retención Total.

Notas de Débito cód. (55, 56)

Normalmente 8% retención.
33

331

IVA RETENIDO MADERA

• Si se retuvo el 8%, el monto retenido se
registra en el IEC en Retención parcial

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)

• Si se retuvo el total del IVA, por ser NDF,
se registra en el IEC en Retención Total.

Notas de Débito cód. (55, 56)

Normalmente 4% retención.
34

341

• Si se retuvo el 4%, el monto retenido se
registra en el IEC en Retención parcial

IVA RETENIDO TRIGO

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)

Notas de Débito cód. (55, 56)
• Si se retuvo el total del IVA por ser NDF
se registra en el IEC en Retención Total.

35

36

Impuesto específico gasolina

361

Formato DTE

IVA RETENIDO ARROZ

4,5 a 6 UTM por m3. Artículo 6, Ley N°
18.502, y artículos 1° y 3° del Decreto
Supremo N° 311/86. No da derecho a
crédito. Se considera rebaja transitoria del
componente variable dispuesto por la Ley
20.259.

Se usa en las Facturas que emite el vendedor, en el
IEV.
No se registra separado en el IEC. En el IEC se debe
incorporar este monto en el campo “Impuesto sin
derecho a crédito”

Normalmente 10% retención.

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)

• Si se retuvo el 10%, el monto retenido se
registra en el IEC en Retención parcial

Versión 2.5 2026-02

Observaciones

Facturas cod (30, 33)

1,5 UTM por m3. Traspasado al
comprador por compra de diésel. Artículo
6, Ley N° 18.502, y artículos 1° y 3° del
Decreto Supremo N° 311/86.
Normalmente 10% retención.

30

Documentos en que se aplica

Notas de Débito cód. (55, 56)

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos
En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos
En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos
En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos
En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

Pág.52 de 51

Código
cambio de
Código sujeto en
retención
total

Nombre

Descripción general

Documentos en que se aplica

Observaciones

• Si se retuvo el total del IVA por ser NDF
se registra en el IEC en Retención Total.
Normalmente 10% retención.
IVA RETENIDO
37

371

• Si se retuvo el 10%, el monto retenido se Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
registra en el IEC en Retención parcial
Notas de Débito cód. (55, 56)
• Si se retuvo el total del IVA por ser NDF
se registra en el IEC en Retención Total.

HIDROBIOLO
GICAS

38

IVA RETENIDO CHATARRA

Factura de Compra emitida cod (45, 46)
total del IVA retención. El monto retenido Notas de Crédito cod (60, 61)
se registra en el IEC en Retención total.
Notas de Débito cód. (55, 56)

39

IVA RETENIDO PPA

Factura de Compra emitida cod (45, 46)
total del IVA retención. El monto retenido Notas de Crédito cod (60, 61)
se registra en el IEC en Retención total.
Notas de Débito cód. (55, 56)

41

IVA RETENIDO
CONSTRUCCION

Se retiene el total del IVA.

44

IMPUESTO ADICIONAL
Art 37 Letras e, h, I, l

45

IMPUESTO ADICIONAL
Art 37 Letras j

Tasa del 15% en 1era venta
a) Alfombras, tapices
b) Casa rodantes
c) Caviar
d) Armas de aire o gas
Tasa del 50% en 1era venta
a) Pirotecnia

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

Factura de compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
Notas de Débito cód. (55, 56)
Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)
Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)
Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

46

IVA RETENIDO ORO

Retención del 100% del IVA

47

IVA RETENIDO CARTONES

Retención Total

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

IVA RETENIDO
FRAMBUESAS

Retención 14%

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

FACTURA DE COMPRA SIN
RETENCIÓN (hoy utilizada
sólo por Bolsa de Productos 0% de retención
de Chile, lo cual es validado
por el sistema)

Factura de Compra emitida cod (45, 46)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

En caso de cambio de sujeto, en
transacciones de Agentes
retenedores, consulte códigos
asociados de productos

48

481

49

Formato DTE

Versión 2.5 2026-02

Pág.53 de 51

Código
cambio de
Código sujeto en
retención
total

Nombre

Descripción general

Documentos en que se aplica
Facturas cod (30, 33)
Notas de Crédito cod (60, 61)
Notas de Débito cod (55, 56)

50

IVA de margen de
comercialización
de
instrumentos de prepago

Para Facturas de venta del contribuyente

51

Impuesto
gas
natural
comprimido; 1,93 UTM/KM3,
Art. 1°, Ley
N° 20.052

Para Facturas de venta del contribuyente

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

52

Impuesto gas licuado de
petróleo; 1,40 UTM/M3, Art
1°, Ley N° 20.052

Para Facturas de venta del contribuyente

Facturas (cod 30, 33)
Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)

53

Impuesto Retenido
Suplementeros Art 74 N°5
Ley de la Renta

Para Facturas de venta del contribuyente, Facturas (cod 30, 33)
retención del 0,5% sobre el precio de venta Notas de Crédito (cod 60, 61)
Notas de Débito (cod 55, 56)
al público.

Formato DTE

Versión 2.5 2026-02

Observaciones

Pág.54 de 51
