---
url: https://www.sii.cl/servicios_online/1039-configuracion_firefox-1182.html
titulo: Configuración de Mozilla para factura electrónica SII
categoria: servicios_online
---
## Configuración de Mozilla para factura electrónica SII

Para usar el navegador Mozilla Firefox con las aplicaciones de Facturación Electrónica Gratuita SII, Contabilidad Simplificada o Completa Electrónicas del SII, primero debe [Instalar su certificado digital](1039-certificado_digital-1182.html#instalo) y seguir lo indicado en Configuración del Computador estándar; luego de eso, debe realizar lo siguiente:

#### [1.- Activar Pop-ups (pantallas emergentes)](#collapseOne)

1.1.- Abra el Mozilla, ir a **Herramientas, Opciones**:

En la sección **Contenido** quite momentáneamente la selección del checkbox **Bloquear Ventanas Emergentes** y luego acepte el cambio, tal como se destaca en la siguiente figura:

Asegure que Mozilla le permite emitir Facturas Electrónicas, luego de esto podrá restablecer el bloqueo de ventanas emergentes, dejando como excepción los servidores del SII de la siguiente manera:

1.2.- Ahora puede restablecer el bloqueo de elementos emergentes, dejando como excepción los servidores del SII; en **Herramientas, Opciones**, sección **Contenidos**, presione botón **Excepciones** y agregue servidores SII digitando \***.sii.cl** y presionando botón Permitir.

Luego de esta modificación, asegure que Mozilla le permita emitir facturas, en caso que esto no ocurra, deberá deshacer lo modificado en este punto 1.2.-

#### [2.- Importar el certificado digital a Mozilla FIrefox](#collapseTwo)

Considerando que su certificado digital está instalado en Internet Explorer, será necesario importarlo hacia Mozilla Firefox, ya que ambos navegadores utilizan distintos repositorios para almacenar y recuperar los certificados digitales. Para realizar la importación hacia Mozilla, debe contar con el certificado digital en un archivo de extensión pfx (si no cuenta con este archivo lo puede obtener exportando su certificado digital desde Internet Explorer e incluyendo la clave privada).

2.1.- Luego de haber realizado la configuración estándar de las aplicaciones del SII para Internet Explorer, abra el Mozilla, ir a **Herramientas, Opciones**:

2.2.- En **Opciones** ir a **Avanzado** y seleccione la pestaña **Certificados**, botón **Ver Certificados**:

2.3.- En la pestaña **Sus Certificados** presionar botón **Importar**:

2.4.- Luego debe buscar en el PC la carpeta en donde está almacenado el certificado digital de la persona que se autenticará en los sistemas del SII, es un archivo con extensión **pfx**, que también lo puede obtener exportando el certificado desde Internet Explorer; lo selecciona y presiona botón **Abrir**:

2.5.- El certificado digital podría solicitar una contraseña maestra de seguridad; si esto ocurre, ingrese una cualquiera y presione botón **Aceptar**, o vaya al **Punto 4** de este manual:

2.6.- Luego el certificado digital solicitará la contraseña con que fue generado (o exportado), la ingresa y presiona botón **Aceptar**:

2.7.- Finalmente Mozilla entregará el siguiente mensaje:

2.8.- Luego cada vez que se autentique o firme un documento, Mozilla entregará el siguiente mensaje, que deberá **Aceptar**; pudiendo además seleccionar el checkbox “**Recordar esta decisión**”

#### [3.- Opcional: Permitir transacciones con protocolo de seguridad SSL](#collapseThree)

Las dos siguientes opciones deberá ejecutarlas solo en caso de ser necesario; si al autenticarse usando Mozilla, observa el siguiente error:

* Conexión segura fallida
* Código de error: ssl\_error\_renegotiation\_not\_allowed

Entonces es necesario permitir conexión con protocolo SSL, en tal caso debe proceder como sigue:

3.1.- Teclee ” **about:config** ” en la barra de su navegador Mozilla:

La advertencia: ¡Zona hostil para manazas!, no la considere (“manaza” = “manos de hacha”)
y presione el botón que sale en el área central: **¡Tendré cuidado, lo prometo!**

3.2.- Luego debe buscar la cadena:   
**security.ssl.allow\_unrestricted\_renego\_everywhere\_\_temporarily\_available\_pref**  
y cambiar de valor de false a true, para ello debe dar doble click a esa línea y cambiará el nombre a negrita dejando el valor true.

3.3.- Luego debe cerrar Firefox y vuelva a entrar, con esta configuración podrá facturar y llevar contabilidad en las aplicaciones gratuitas del SII.

#### [4.- Opcional: Resetear contraseña maestra de Mozilla](#collapseFour)

En caso que luego de autenticarse con certificado digital en las aplicaciones del SII, esto es, después de **Aceptar** el siguiente mensaje:

Mozilla podría solicitarle una contraseña maestra desconocida por Ud, como muestra el siguiente recuadro:

Si la conoce ingrésela; en caso contrario, deberá resetear la contraseña maestra de Mozilla.  
La contraseña maestra (o Master Password) es una contraseña propia de Mozilla con el fin de aumentar el nivel de seguridad. Si la tiene establecida, Firefox se la solicitará cada vez que tenga que hacer uso de su certificado electrónico.

Si no conoce esta contraseña maestra no podrá utilizar el certificado electrónico instalado en el navegador. Para lo cual existe la opción de **Restablecer Contraseña**, que elimina la contraseña maestra actual y permite establecer una nueva, **pero esta acción elimina todos los certificados electrónicos que estuvieran instalados**. En este caso, asegúre que dispone de una copia de seguridad del certificado electrónico para poder volver a instalarlo (es archivo con extensión .pfx obtenido al exportar su certificado, incluyendo la clave privada). En caso de no contar con este archivo, será necesario adquirir un nuevo certificado.

Si dispone de una copia de seguridad de su certificado y quiere restablecer la contraseña maestra, teclee en la barra de direcciones del navegador lo siguiente:  
“ **chrome://pippki/content/resetpassword.xul** “   
Luego presione la tecla **Enter**

Aparecerá una nueva pantalla donde deberá presionar el botón **Restablecer**.

**ADVERTENCIA**: Antes de presionar el botón, lea y entienda el mensaje que le está entregando Mozilla:

“Si restablece su contraseña maestra, todas las contraseñas web, y de correo electrónico almacenados, los datos de los formularios, certificados personales y claves privadas serán olvidadas. ¿Seguro que quiere restablecer su contraseña maestra?”.

En caso que esté seguro presione botón **Restablecer**

El olvido de las contraseñas, aplicará únicamente sobre las contraseñas que haya guardado en Mozilla y no las de otros navegadores. En este punto se recomienda reiniciar el PC.  
Luego de Restablecer la contraseña maestra, Mozilla le solicitará una nueva:

Para lo cual debe ingresarla o bien puede desactivar el uso de contraseña maestra en **Herramientas, Opciones, Seguridad**, desmarcando checkbox **Usar Contraseña Maestra**.

Luego continúa importando nuevamente el certificado digital, es decir:

Luego:

Ahora Mozilla, le solicitará la contraseña original del certificado digital.

Y la contraseña que estableció, si es que lo hizo, cuando instalo el certificado en Internet Explorer; en caso que no haya establecido una nueva contraseña, ésta debe ser la original del certificado digital:

Luego recibirá el siguiente mensaje:

Seguido esto, debe **Aceptar** este recuadro y el siguiente, volviendo al menú principal de Mozilla.  
Ahora está en condiciones de usar las aplicaciones del SII que requieran identificación con certificado digital, usando el navegador Mozilla.
