---
url: https://www.sii.cl/servicios_online/windows8.pdf
titulo: CONFIGURACIÓN DE COMPUTADOR PARA CONTRIBUYENTES
categoria: servicios_online
---
CONFIGURACIÓN DE COMPUTADOR PARA CONTRIBUYENTES
USUARIOS DE FACTURACIÓN ELECTRÓNICA MIPYME QUE USAN
WINDOWS 8
Debido a que el nuevo sistema Operativo Windows 8 no trae activada la componente .NET
Framework 3.5, requerida por el sistema de Facturación Electrónica del Portal MIPYME , los
contribuyentes que utilicen dicho sistema operativo deben realizar uno de los 2 procedimientos
que a continuación se indican, antes de efectuar la Configuración de 9 pasos publicada en la
Portal MIPYME del SII.
En ambos casos se debe haber iniciado la sesión con un usuario que tenga privilegio de
Administrador.

Para configurar tiene dos opciones, las cuales se muestran a continuación:
1)

Habilitar .Net Framework 3.5 desde el Panel de Control

2)

Habilitar .Net Framework 3.5 desde disco del sistema

1) Habilitar .Net Framework 3.5 desde el Panel de Control
Esta opción requiere tener conexión a Internet.
1.1) En el Panel de Control, elija Programas y Características:

1.2) Seleccione Activar o Desactivar características de Windows

1.3) Seleccione .Net FrameWork 3.5

1.4) Espere hasta que la activación de la característica finalice

Si aparece este mensaje, debe seleccionar la opción de Descargar Archivos desde Windows
Update

2) Habilitar .Net Framework 3.5 desde disco del sistema
Si no puede conectar el equipo a Internet, puede habilitar .NET Framework 3.5 usando el disco de
instalación (imagen ISO o DVD) desde el que instaló Windows 8. Monte el disco de instalación de
Windows 8 y escriba el comando siguiente desde un símbolo del sistema con privilegios de
adminstrador:
Dism /online /enable-feature /featurename:NetFx3 /All /Source:x:\sources\sxs
/LimitAccess
donde x: es la letra de unidad para la imagen ISO o el DVD de Windows 8.

En ambos casos, si .Net Framework quedó correctamente instalado, al ingresar a Activar o
Desactivar características de Windows, tal como se indica en el punto 1.2, .Net Framework 3.5,
debe aparecer activado, como se muestra en la imagen siguiente:

Más detalle sobre la instalación de .Net Framework 3.5 en Widows 8 se puede encontrar en la
siguiente página de Microsoft: http://msdn.microsoft.com/es-es/library/hh506443.aspx
