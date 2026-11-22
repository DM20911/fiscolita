---
url: https://www.sii.cl/servicios_online/1041-informacion_tecnica-1324.html
titulo: Aspectos técnicos
categoria: servicios_online
---
## Aspectos técnicos

En esta opción Ud. obtendrá aspectos técnicos que es preciso considerar en la construcción de los Libros Contables Electrónicos.

#### [1.- Compresión de Archivos](#collapseOne)

El SII, ha establecido que el tamaño máximo de un archivo a enviar es de 20 Mega. Dado el gran tamaño de los archivos los contribuyentes pueden enviar comprimida la información de acuerdo a http://www.gzip.org/. Donde hay software para variadas plataformas.

Estos deben ser archivos con extension \*.gz.

#### [2.- Especificación técnica de Firma Digital](#collapseOne2)

Todo documento va acompañado de una firma digital, calculada con la llave privada de un certificado digital otorgado por una empresa certificadora de identidad acreditada por el SII.

La firma digital del LCE, así como la del envío de LCE, está basada en el estándar XMLDSIG, pero con algunas restricciones respecto a la obligatoriedad y a los algoritmos de firma y hash permitidos.

Para validar adecuadamente la firma digital del LCE, el SII requiere que se incorpore la siguiente información de firma electrónica en cada LCE:

<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">

<SignedInfo>

<CanonicalizationMethod

Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />

<SignatureMethod

Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />

<Reference URI="#XXXXX">

<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />

<DigestValue>... </DigestValue>

</Reference>

</SignedInfo>

<SignatureValue>... </SignatureValue>

<KeyInfo>

<KeyValue>

<Valores Llave Publica>

> Si la llave es RSA se debe indicar
>
> <RSAKeyValue>
>
> <Modulus>... </Modulus>
>
> <Exponent>... </Exponent>
>
> </RSAKeyValue>
>
> Si la llave es DSA se debe indicar
>
> <DSAKeyValue>

<P>... </P>

<Q>... </Q>

<G>... </G>

<Y>... </Y>

</DSAKeyValue>

</KeyValue>

<X509Data>

<X509Certificate>... </X509Certificate>

</X509Data>

</KeyInfo>

</Signature>

#### [3.- Campo ID](#collapseOne3)

El valor que se coloca en los ID (el cual es el mismo que se utiliza en el campo Signature/SignedInfo/Reference/Uri) debe ser conformado de la siguiente manera:

**<Nombre del Documento>\_<datos de la Identificacion>**

En donde:

* **Nombre del Documento:** Es el nombre del documento sin la palabra "Documento" que se firma. Ejemplos Para el "DocumentoDiarioRes" debería ser: "DiarioRes"
* **Datos de la Identificación:** Son Información relevante de la sección de "Identificación"

Se detalla a continuación como sería para cada Documento FIRMADO:

* [a) Resumen del diario:](javascript:void(0);)

  **DiarioRes\_<RutContribuyente>\_<Periodo/Inicial>\_<Periodo/Final>[\_<Moneda>][\_<Rectificatoria>]**

  Ejemplos:
    
  DiarioRes\_1-9\_2005-01\_2005-12
    
  DiarioRes\_1-9\_2005-01\_2005-12\_USD
    
  DiarioRes\_1-9\_2005-01\_2005-12\_USD\_1
    
  DiarioRes\_1-9\_2005-01\_2005-12\_1
* [b) Resumen del Mayor](javascript:void(0);)

  **MayorRes\_<RutContribuyente>\_<Periodo/Inicial>\_<Periodo/Final>[\_<Moneda>][\_<Rectificatoria>]**
* [c) Balance](javascript:void(0);)

  **Balance\_<RutContribuyente>\_<PeriodoTributario>[\_<Moneda>][\_<Rectificatoria>]**

  Ejemplos:
    
  Balance\_1-9\_2005-01
    
  Balance\_1-9\_2005-01\_USD\_1
    
  Balance\_1-9\_2005-01\_1
* [d) Resumen de Compra](javascript:void(0);)

  **CompraRes\_<RutContribuyente>\_<PeriodoTributario>[\_<Rectificatoria>]**

  Ejemplos:
    
  CompraRes\_1-9\_2005-01
    
  CompraRes\_1-9\_2005-01\_1
* [e) Resumen del Venta](javascript:void(0);)

  **VentaRes\_<RutContribuyente>\_<PeriodoTributario>[\_<Rectificatoria>]**

  Ejemplos:
    
  VentaRes\_1-9\_2005-01
    
  VentaRes\_1-9\_2005-01\_1
* [f) Comprobante de Certificación](javascript:void(0);)

  **CoCertif\_<RutContribuyente>\_<FchEmision>\_<DocumentoCal/RutDistribuidor>\_  
  <DocumentoCal/TipoCertificado>\_<DocumentoCal/Clase>\_  
  <DocumentoCal/TipoLCE>\_<<DocumentoCal/PeriodoVigencia>**

  Ejemplo:
    
  CoCertif\_1-9\_2005-01-15\_2-7\_C\_2\_1\_2006
* [g) Envío de Libros](javascript:void(0);)

  **EnvioLibros\_<RutEnvia>\_<RutContribuyente>\_<Notificacion/Tipo>\_<Notificacion/Folio>**

  Ejemplo:
    
  EnvioLibros\_1-9\_2-7\_1\_123456
* [h) Envío Obligatorio](javascript:void(0);)

  **EnvioOblig\_<RutEnvia>\_<RutContribuyente>**

  Ejemplo:
    
  EnvioOblig\_1-9\_2-7
* [i) Diccionario](javascript:void(0);)

  **Diccionario\_<RutContribuyente>\_<PeriodoTributario>[\_<Rectificatoria>]**

  Ejemplo:
    
  Diccionario\_1-9\_2005-01
    
  Diccionario\_1-9\_2005-01\_1
