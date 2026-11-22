---
url: https://www.sii.cl/documentos/resoluciones/2004/reso98_anexo.doc
titulo: Instructivo Corredores de Bolsa – Anexo:
categoria: otros
---










INSTRUCTIVO TÉCNICO PARA GENERACIÓN DE DTES DE CORREDORES DE BOLSA Y AGENTES DE VALORES

2004-10-05
CONSIDERACIONES GENERALES:

En este documento se describe la forma en que deben ser completados, específicamente, los Documentos Tributarios Electrónicos (en adelante DTE’s) que dan cuenta de operaciones realizadas por Corredores de Bolsa y Agentes de Valores, por cuenta propia y de terceros.

Por la especial naturaleza de las transacciones realizadas por estos contribuyentes, en forma previa a comenzar a emitir estos documentos, deberán cumplir con las siguientes obligaciones:
Contar con el giro de “Comisionista de la Bolsa”, código de actividad económica N° 81032.
Realizar correctamente el test de prueba entregado por el SII
Ser autorizado expresamente por el SII, para operar utilizando DTE’s en transacciones de intermediación.
En este documento se describe el llenado de DTE’s, que es común para los siguientes documentos:
Factura Electrónica
Factura No Afecta o Exenta Electrónica
Nota de Crédito Electrónica
Nota de Débito Electrónica
Este Servicio ha decidido eximir a estos contribuyentes de la obligación de emitir la Declaración Jurada Formulario 1891, por aquellos periodos anuales completos en los cuales se encuentren operando como emisores de documentos tributarios electrónicos, y copulativamente, hubiesen documentado todas sus transacciones bursátiles de terceros, por medio de DTE’s. Esto será debidamente establecido mediante resolución que oportunamente emitirá el SII.

CONTENIDO DE FACTURAS Y DOCUMENTOS ASOCIADOS:
	 
Todo documento tributario electrónico que se emita, debe considerar en primer término las especificaciones descritas en el documento “Formato de Documentos Tributarios Electrónicos”, que se encuentra publicado en  HYPERLINK "http://www.sii.cl" www.sii.cl y el cual es periódicamente actualizado.

Adicionalmente, y sólo para los contribuyentes aquí señalados, se deben incluir las indicaciones de llenado que se informan en este Instructivo, lo cual es condición necesaria de la autorización otorgada que permite emitir DTE´s por sus transacciones de intermediación de valores.

NOTAS:

Campo: establecido de acuerdo al Formato de Documentos Tributarios Electrónicos.

Valor / valores: Datos a consignar en campos referidos. Entre comillas “” se indican los valores específicos.




CAMPOS ESPECIALES A CONSIDERAR EN EL DETALLE DE TRANSACCIONES DE INTERMEDIACIÓN:

En sección de detalle de DTE’s

Campo Tipo de Código: Señalar el nombre del código de valores:

Valor: “VALORES”
Impresión: No imprimir
Obligatoriedad: Obligatorio

Campo Código del Ítem: Código del Instrumento transado, consignar sólo un código:

Valores: “1”, “2”, “3”, “4”, “5”, “6”, “9” y “99”, correspondientes a: 
ValorInstrumento1Acciones2Dólares3Oro4Otras operaciones de futuro5Opciones6Documentos de Renta Fija9Otros Instrumentos de Inversión99Otros que no sean Instrumentos de InversiónImpresión: Imprimir descripción de la glosa (ACCIONES, ORO, ETC.), y no código
Obligatoriedad: Obligatorio

Campo Indicador de facturación / exención: Indica:

Valores: “2” o “6”, Detalle no facturable positivo y detalle no facturable negativo, el valor de la línea de detalle es siempre positivo
Impresión: No imprimir
Obligatoriedad: Obligatorio

Campo Nombre del Ítem: Nombre o Razón social del valor transado, número de serie, otra información:

Valor: Nombre del valor transado. En caso de acciones, nombre de la acción según su código nemotécnico, separando un espacio para indicar otras singularidades. Ejemplo: “COTEC 44587277577 ADFADVD”
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo Descripción Adicional: Tipo de Transacción:

Valores: “COMPRA” o “VENTA”
Impresión: Imprimir glosa explicativa acorde
Obligatoriedad: Obligatorio

Campo Precio de referencia: En caso de venta de valores comprados por el mismo intermediario, se debe indicar el Precio unitario de la compra de dichos valores, en términos nominativos:

Valor: Numérico 12 enteros, 6 decimales
Impresión: Imprimir
Obligatoriedad: Opcional

Campo Cantidad: Cantidad transada de acciones, dólares, oro, etc:

Valor: Numérico 12 enteros, 6 decimales
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campos de la Tabla de Distribución de la Cantidad: para informar transacciones con acciones, afectas o exentas del Impuesto a la Renta, según lo establecido en el Art. 18 ter, del mismo cuerpo legal:

Subcampo Subcantidad_Distribuida: cantidad de acciones de cada tipo:
Valor: Numérico 12 enteros, 6 decimales
Impresión: Imprimir
Subcampo Código subcantidad: Indica si acción es afecta o exenta:
Valor: “AFECTO” o “EXENTO”, según se encuentren afectos o exentos al Impuesto a la Renta
Impresión: Imprimir glosa acorde
Obligatoriedad Tabla de Distribución de la Cantidad: Opcional.

Campo Fecha de elaboración: Fecha de la transacción:

Valor: Fecha válida (AAAA-MM-DD)
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo Fecha de vencimiento: Corresponde a la fecha de compra de valores que se están vendiendo:

Valor: Fecha válida (AAAA-MM-DD)
Impresión: Imprimir
Obligatoriedad: Opcional

 Campo Precio Unitario del Ítem en pesos: Precio unitario de los valores transados:

Valor: Numérico 12 enteros, 6 decimales
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo Moneda: Para el caso de transacciones de moneda extranjera se deberá indicar el código de la moneda, de acuerdo a la codificación de Monedas del Bco. Central:

Valor: Código según tabla de codificación de Monedas del Banco Central
Impresión: Glosa relacionada
Obligatoriedad: Condicional

Campo Factor de Conversión: Se señalará el valor del tipo de cambio para operaciones de moneda extranjera:

Valor: Numérico 6 enteros, 4 decimales
Impresión: Imprimir
Obligatoriedad: Condicional

En sección de Encabezado de DTE’s

Campo Giro del negocio del Emisor: Indicar giro relacionado:

Valor: “Corredores de Bolsa” o “Agente de Valores”
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo ACTECO: Código de Actividad Económica, indicar el código 81032:

Valor: “81032”
Impresión: No imprimir
Obligatoriedad: Obligatorio

Campo Rut Receptor: Para el caso de transacciones de moneda extranjera que superen los US $10.000, o en su defecto, el valor que se exija mediante Resolución del SII; se deberá indicar el Rut del receptor del documento. En caso de receptores extranjeros sin número de Rut, se debe consignar el Rut: 55.555.555-5, e indicar el número de Identificación extranjero (Ejemplo: ID pasaporte) en el campo siguiente (Código interno del Receptor):

Valor: Número de RUT y dígito verificador
Impresión: Imprimir
Obligatoriedad: Condicional
Campo Código interno del Receptor: Ligado a la obligación anterior, y en caso de tratarse de personas que no cuenten con un número de Rut nacional, se deberá indicar en este campo el número identificatorio extranjero:

Valor: Número de ID de pasaporte o documento identificación extranjero.
Impresión: Imprimir
Obligatoriedad: Condicional

Campo Rut de Solicitante de factura: corresponde al Rut de la persona titular de los valores que se enajenan o se adquieren. Aplicable sólo a valores nominativos:

Valor: Número de Rut
Impresión: No imprimir
Obligatoriedad: Opcional, y sólo en caso de valores nominativos

Campo Monto Total: Valor totalizado de las comisiones y cargos, afectos y exentos:

Valor: Numérico 18 enteros
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo Monto no Facturable: Valor total de la(s) operación(es) o instrumentos transados:

Valor: Numérico 18 enteros
Impresión: Imprimir
Obligatoriedad: Obligatorio

Campo Monto Período: Monto Total + Monto no Facturable. Valor total a pagar en favor del cliente (negativo) o total apagar en favor del corredor (positivo):

Valor: Numérico 18 enteros
Impresión: Imprimir
Obligatoriedad: Obligatorio


FACTURACIÓN DE DERECHOS DE BOLSA, COMISIONES Y OTROS CARGOS:

La facturación de las comisiones y otros cargos de operación deberá ser registrada en los Documentos Tributarios Electrónicos de acuerdo a lo señalado en el modelo general del sistema de Facturación Electrónica, consignándolos como servicios afectos o exentos según su caso, y adicionalmente:

En sección de detalle de DTE’s

Campo Código del Ítem: Código de la comisión:

Valor: “0” (cero), correspondiente a la comisión cobrada
Impresión: No imprimir
Obligatoriedad: Obligatorio
PAGE  


PAGE  5





