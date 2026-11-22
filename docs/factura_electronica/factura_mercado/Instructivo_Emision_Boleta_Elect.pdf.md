---
url: https://www.sii.cl/factura_electronica/factura_mercado/Instructivo_Emision_Boleta_Elect.pdf
titulo: INSTRUCTIVO TÉCNICO
categoria: factura_electronica
---
INSTRUCTIVO TÉCNICO
BOLETA ELECTRÓNICA
Instructivo para la Emisión y Envío de las Boletas Electrónicas de Ventas y
Servicios

28/10/2021

Modificaciones sobre versión anterior:
Se actualizan Protocolos TLS soportados, y se informa inicio de vigencia de actualización.

Instructivo para la Emisión y Envío al SII de Boletas Electrónicas
Objetivo
Entregar los antecedentes necesarios para que los contribuyentes autorizados por el SII para emitir
boleta electrónica, puedan generar y enviar al SII documentos válidos, de acuerdo a la normativa
vigente del SII.
Introducción
El 24 de febrero de 2020 se publicó en el Diario Oficial la Ley 21.210 que Moderniza la Legislación
Tributaria Entre otras medidas, la citada ley establece la obligatoriedad de emitir la boleta
electrónica de ventas y servicios de manera que:
• Los contribuyentes que actualmente emiten factura electrónica tienen como plazo 24 de
agosto del presente año para comenzar a emitir boleta electrónica.
• Los contribuyentes que actualmente no emiten factura tienen como plazo el 24 de febrero
de 2021 para comenzar a emitir boleta electrónica.
Posteriormente, el 2 de julio, el SII emitió la Resolución Exenta SII N° 74, que instruye sobre
procedimiento para emitir boletas electrónicas y con el propósito de adecuar el cumplimiento de
los requisitos a los respectivos periodos. La obligatoriedad inicia a contar del 01 de enero de 2021
para los contribuyentes inscritos en factura electrónica, y a contar del 01 de marzo de 2021 para
aquellos que no tengan tal calidad. No obstante, los contribuyentes que opten por realizar los envíos
previo a su obligación podrán hacerlo siguiendo las presentes instrucciones.
Principales cambios introducidos por la Normativa
Si bien el documento boleta electrónica existe hace varios años y actualmente es utilizada por un
número considerable de contribuyentes, hasta la publicación de la ley 21.210 su uso era voluntario.
A continuación, se detalla, junto con la ya mencionada obligatoriedad, los principales cambios
introducidos por la normativa:
•
•
•
•
•

Obligatoriedad de emitir boleta electrónica
Obligatoriedad de enviar al SII copia de cada boleta electrónica emitida
Obligatoriedad de enviar diariamente al SII el Resumen de Ventas Diarias (RVD) ex RCOF
(Reporte de Consumo de Folios)
La boleta electrónica deberá indicar separadamente el IVA y otros impuestos señalados en
la Resolución N° 74.
Se elimina la obligación de llevar y mantener el libro de boletas electrónicas

Este resumen sólo indica los cambios de mayor impacto. El contribuyente debe revisar la Res. SII N°
74 y asegurarse de cumplir con todas las obligaciones que ella establece para los contribuyentes
que emiten boleta electrónica. Ver la Res. N° 74 en:
http://www.sii.cl/normativa_legislacion/resoluciones/2020/reso74.pdf

Consideraciones Técnicas para la Generación y Envío al SII de la Boleta Electrónica
El modelo de operación de la boleta electrónica es el mismo de la factura electrónica, sin embargo,
el gran volumen de información asociado a la boleta electrónica hace aconsejable desacoplar la
plataforma dedicada a recepción de boleta electrónica de la de factura electrónica. Con esto, se
producen algunas diferencias entre ambos documentos tributario electrónicos que es conveniente
tener presente:
•

•

•

•

•
•

•

•

•

Todos los servicios de automatización de procesos deben ser realizados con protocolo TLS
1.2 o superior, tanto en ambientes de certificación como los de producción. Protocolos
anteriores, ya sea TLS 1.0 o TLS 1.1, no serán permitidos a contar de las siguientes fechas:
o Certificación y Pruebas: a contar del 19 de noviembre de 2021.
o Producción: a contar de enero de 2022.
El mecanismo de envío de la información de boleta electrónica será similar al de la factura
electrónica (upload automatizado), sin embargo, los servidores dedicados a la recepción
boleta electrónica serán distintos de los que se utilizan en la recepción de factura
electrónica (Palena y Maullin).
Los servicios de autenticación, consulta de estado de un envío y estado de un documento
serán distintos. Factura electrónica continuará con los Webs Services Soap actuales y para
la boleta electrónica se habilitará servicios Rest.
El Token de autenticación obtenido para el envío de factura electrónica y servicios asociados
j para el envío y consultas de boleta electrónica y se deberá obtener uno específico para ese
fin.
No hay cambios en la obtención de folios autorizados
No hay cambios en el envío de RCOF que pasa a denominarse Registro de Ventas Diario, ya
que utiliza el mismo schema XML y sólo se elimina la obligación de enviar el detalle de folios
utilizados y/o anulados.
El schema xml del envío de boleta electrónica fue actualizado con la incorporación de un par
de tags en la referencia y la obligatoriedad de algunos tags. Se estableció un límite máximo
de 500 boletas electrónicas por envío.
El diagnostico de validación de los envíos de boleta electrónica se entregará mediante un
servicio Rest que tiene como entrada el track id del envío. Factura electrónica continuará
recibiendo sus diagnósticos a través de e-mail.
El track id asociado a boleta electrónica tendrá 15 dígitos de largo. Factura electrónica
continuará utilizando el track id actual de 10 posiciones de largo.

Estas consideraciones suponen que el lector ya está familiarizado con la factura electrónica y su
modo de operación y solo enfatiza los cambios que se introducen con la obligatoriedad de enviar la
boleta electrónica al SII.
Si Ud. no ha trabajado con factura electrónica anteriormente, le será de utilidad revisar la
documentación que se indica en el punto siguiente.

Términos de Uso de la API SII
Esta API provee los servicios que permiten a los contribuyentes integrar sus sistemas de emisión de
boleta electrónica con el sitio del SII para cumplir con las obligaciones que la normativa establece.
El SII se reserva el derecho de suspender unilateralmente, en forma temporal o definitiva, el acceso
a los servicios de esta API ante la detección de cualquier anormalidad que a su parecer contravenga
el uso idóneo y responsable de ellos, en particular, un uso de los servicios para fines distintos a los
señalados anteriormente.
Los términos de uso general del sitio web del SII se encuentran en:
http://www.sii.cl/sobre_el_sii/terminos_sitio_web.html

Documentación Previamente Publicada en el Sitio del SII
En el Instructivo Técnico de Factura Electrónica, publicado en:
http://www.sii.cl/ayudas/ayudas_por_servicios/2004-instructivo-2007.html
se encuentra toda la información necesaria para generar y enviar al SII documentos tributarios
electrónicos que es aplicable también a la boleta electrónica, salvo las consideraciones indicadas
anteriormente Se sugiere revisar lo siguiente:
•
•
•
•

Descripción del Formato de Documentos Tributarios Electrónicos
Schemas XML (EnvioDTE, EnvioBoleta, RDV exRCOF)
Automatización de Procesos (Autenticación, Envío y Consultas de Factura Electrónica con
WS)
Instructivo para la Emisión de Documentos Tributarios Electrónicos

Documentación de los Nuevos Servicios Relacionados con el Envío al SII y Consultas sobre Boletas
Electrónicas
La documentación de los servicios disponibles, se encuentra publicada en la siguiente URL
https://www4c.sii.cl/bolcoreinternetui/api/.
En resumen, se habilitan las siguientes funcionalidades para la Boleta Electrónica:
•
•
•
•

Servicios de Autenticación Boleta Electrónica (Semilla y Token)
Envío de Boleta Electrónica
Consulta del estado del envío de la Boleta Electrónica
Consulta de Boleta Electrónica

Esta documentación se generó de acuerdo al estándar OAS 3.0 de especificación de APIs RESTful,
utilizando el software Swagger.
