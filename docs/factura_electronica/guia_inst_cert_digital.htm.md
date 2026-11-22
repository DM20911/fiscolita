---
url: https://www.sii.cl/factura_electronica/guia_inst_cert_digital.htm
titulo: GUÍA PARA INSTALAR EL CERTIFICADO DIGITAL
categoria: factura_electronica
---
# GUÍA PARA INSTALAR EL CERTIFICADO DIGITAL

Si Ud. posee un Certificado Digital para aplicar Firma Electrónica Avanzada (residente un dispositivo token), debe saltarse este paso de instalación de certificado y **sólo asegurar que el PC que está utilizando tiene inserto en un puerto USB el token y que haya instalado su driver (software que lo configura)**. Si las condiciones señaladas se cumplen, este Certificado digital para aplicar Firma Electrónica Avanzada podrá ser utilizado al momento de ingresar al sistema o cuando genere un documento electrónico.

1) Consultar a su Proveedor, proceso de instalación

A**nte****s de instalar el certificado,** consulte a su proveedor la forma de instalarlo.  
  
La instalación de su certificado depende de la entidad en la que lo adquiera. No obstante lo anterior, a continuación se presenta un “Ejemplo de configuración para habilitar la protección segura de claves privadas y de nivel seguridad de un Certificado”.

2) Seguridad

* Habilitar clave de uso, corresponde al nivel más alto de seguridad; con esta clave, sólo el usuario podrá acceder al uso del certificado digital.
* Modalidad Exportable, podrá trasladar su certificado en un pendrive e instalarlo en el PC que estime conveniente, procurando desinstalarlo después de usarlo.

**Ejempl****o de configuración para habilitar la protección segura de claves privadas y de nivel seguridad de un Certificado.**

**Paso 1.**  
Abra el archivo que contiene el certificado digital (de extensión .pfx)

**Paso 2.**  
Al inicio de la instalación, se solicitará la contraseña que le ha entregado el proveedor del certificado. Se recomienda habilitar protección segura de claves privadas.

**Paso 3.**  
Posteriormente, debe crear una **nueva contraseña**, la cual será utilizada cada vez que utilice el certificado. **Es muy importante recordar la contraseña ingresada, pues de otra forma no podrá utilizar su certificado digital**.

**Paso 4.**  
Una vez completado los datos, se debe pulsar  “Finalizar”, tal como se indica en la figura anterior.

**IMPORTANTE** al dejar la sesión de su navegador (Internet Explorer) abierta, una vez que se ha autenticado con el certificado digital en el sitio del SII, su autenticación no caducará hasta que este programa se cierre y, por lo tanto, dentro de esa sesión se podrá ejecutar cualquier acción en forma autenticada en el sitio (como emisión de facturas, rectificatorias de declaraciones, etc.).

**Ejemplo de Operación en Infocentro o Cyber-café**

**Paso 1.**  
Instalar su certificado digital, de acuerdo a la guía anterior.

**Paso 2.**  
Verificar que el PC tenga instalado “netFramework”, requerido por el Plug-in Firma Digital (si no está insalado, debe instalarlo). Puede hacerlo desde Microsoft o desde [.Net FrameWork 3.5](http://www.microsoft.com/es-es/download/details.aspx?id=21) en “Instrucciones de Uso de Facturación MIPYME”.

**Paso 3.**  
Configurar Internet Explorer de acuerdo a las instrucciones que aparecen en la guía de [Configuración del computador para uso del sistema de Facturación SII](factura_sii/configurar_computador.htm).
