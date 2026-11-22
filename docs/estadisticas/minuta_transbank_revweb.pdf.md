---
url: https://www.sii.cl/estadisticas/minuta_transbank_revweb.pdf
titulo: Minuta: Resultados Resolución Transbank
categoria: otros
---
Minuta: Resultados Resolución Transbank

Resumen
Mediante un análisis a posteriori, se estima que los contribuyentes involucrados en la Resolución N°51 de
01/02/de 2015 que establece que el voucher de las transacciones pagadas con tarjetas de crédito o débito
sea válido como boleta, aumentaron sus débitos de IVA entre un 10,2% y un 10,6%, y emitieron un 7%
más de estos documentos durante 2016. Además, se observa que el efecto es un poco mayor en las
empresas pequeñas que en las microempresas y hay evidencia de que en el rubro de hoteles y
restaurantes se presenta un efecto mayor que en el rubro de comercio. Cuando se analiza la variación en
los créditos fiscales, no hay evidencia estadística de cambios significativos.

Antecedentes


A partir del 1 de febrero de 2015, se estableció mediante la Resolución N° 51 que el voucher
emitido en las transacciones con tarjetas de crédito o débito sería el comprobante tributario
equivalente a la boleta de ventas y servicios en todos los establecimientos que emiten
boletas en papel, en transacciones pagadas mediante estos medios electrónicos.



A partir de agosto de 2015, se incluyen en el Formulario 29 (“F29”), de declaración mensual de
impuestos, dos códigos nuevos, en los cuales se debe registrar el monto de débito proveniente
de las ventas por medio electrónico y el número de estas transacciones:






El comprador o cliente final deberá seguir solicitando la boleta en los siguientes casos:






1

Código 758: Destinado a registrar la cantidad de comprobantes o recibos de pago emitidos
por el terminal para transacciones, por aquellas ventas efectuadas por medios electrónicos
durante el período que se está declarando, por concepto de ventas y/o servicios afectos.
Código 759: Destinado a registrar el monto de débito fiscal incluido en los comprobantes o
recibos de pago por el mismo tipo de transacción ya mencionado.

Si el establecimiento emite boletas electrónicas de ventas y servicios.
Si el establecimiento opera con máquinas registradoras, terminales de puntos de ventas,
impresoras fiscales u otro dispositivo similar, autorizados por el SII para emitir vales en
reemplazo de boletas.
Si se realiza el pago en efectivo u otro medio distinto a tarjetas de crédito o débito.
Si la compra o el servicio adquirido está exento de IVA.



El SII cuenta con información sobre los comercios que operan con Transbank y sobre sus
transacciones, identificando a los que pueden operar con la modalidad de voucher por boleta.



De acuerdo a información de SBIF, el uso de tarjetas de débito y crédito registra un aumento
sostenido, pasando de 3 millones en 1995, a 34 millones de tarjetas en mayo de 2017. Solo desde
el 2014 al 2016, el aumento es del 22%

http://www.sii.cl/documentos/resoluciones/2015/reso05.pdf
1

Minuta: Resultados Resolución Transbank



En tanto, las transacciones anuales con tarjeta de debido llegan a 800 millones y con tarjeta de
crédito a 300 millones, superando a las transacciones con efectivo y cheque. Lo anterior
muestra la relevancia de facilitar el cumplimiento tributario en este tipo de operaciones.

Análisis
El objetivo es medir si hay un aumento en los códigos de débitos por ventas (voucher Transbank más
boletas de papel) en las empresas que utilizan este medio de pago electrónico y son afectadas por la
Resolución. Para esto se desarrolla un Modelo de Diferencias en Diferencias para medir el aumento en
los códigos declarados por el grupo de tratamiento (el que fue afectado por la Resolución) versus un
grupo de control. Se define como “periodo base” (o t=0), el año previo a la Resolución, que corresponde
al 2014. Debido a que a partir de agosto de 2015 se exigió el uso de los nuevos códigos en el F29, se
decide usar el año 2016 para medir el efecto (t=1).
Los grupos de control y tratamiento utilizados en el análisis son los siguientes:
-

Grupo Control 1: Se construye un grupo de control que busca representar lo que ocurre en el
resto de la economía que no es influenciada directamente por operaciones con Transbank.
Consiste en una muestra aleatoria de contribuyentes que no pertenecen a la nómina de
Transbank, que no declaran el Código 759 del F29 y que no se encuentren incluidos en la nómina
de emisores de boletas electrónicas, usuarios de impresoras fiscales, terminales de punto de
venta, y usuarios de máquinas registradoras. El grupo Control 1 utilizado para las estimaciones
finales alcanzó a 22.403 contribuyentes.
2

Minuta: Resultados Resolución Transbank

-

-

Grupo Control 2: Este grupo de control busca considerar la influencia de los medios de pago
electrónicos en los contribuyentes. Al grupo de control 1 se le agregan los contribuyentes que
pertenecen a la nómina de emisores de boletas electrónicas, usuarios de impresoras fiscales,
terminales de punto de venta, y usuarios de máquinas registradoras. Estos últimos utilizan
Transbank, pero no son afectados por la Resolución. El grupo Control 2 utilizado para las
estimaciones finales alcanzó a 25.824.
Grupo de Tratamiento: Contribuyentes que pertenecen a la nómina Transbank y que durante
el primer trimestre de 2016 declaran en el código 759 del F29 un promedio mayor a cero. El
grupo de tratamiento utilizado para las estimaciones finales fue de 37.325 contribuyentes. En el
siguiente cuadro se presenta su distribución por tamaño de ventas. Además, por rubro económico
se concentran en el sector comercio con un 67% y en el sector restaurantes y hoteles con un
17% de contribuyentes2 .
Distribución por tamaño de grupo Transbank3
Sin ventas
20
0%
Micro
17.298
46%
Pequeña
17.649
47%
Mediana
1.948
5%
Grande
410
1%
Total
37.325
100%

Del análisis de los distintos grupos, se desprende que la muestra aleatoria de contribuyentes no afectados
por la Resolución representa, como es de esperarse, al total de la economía, lo que implica una alta
cantidad de empresas sin ventas o con ventas muy bajas, lo cual no ocurre en el grupo de Transbank, ya
que además tiene la restricción adicional que el código 759 de los débitos sea mayor a cero, lo que
produce que los grupos no sean muy parecidos en la zona inferior de la distribución4. Para solucionar esta
situación, se decidió eliminar del grupo de control 1 a los contribuyentes que estuvieran bajo cierto valor,
valor que fue definido como el percentil 5 de la variable de interés en el grupo de tratamiento (las
empresas ubicadas bajo el 5% de la variable débito ordenada de menor a mayor).
Además, se efectuaron las siguientes consideraciones:
Se considera solo a contribuyentes vigentes y que presenten declaración en el periodo previo a
la Resolución y al periodo posterior. De esta forma se construye un panel balanceado.
Las estimaciones utilizando el grupo de control 1 no consideran las empresas de tamaño grande 5.
Se realizan estimaciones de Diferencia en Diferencia con las variables en niveles, en logaritmos y
para la mediana.
Las variables de interés para las que se mide el efecto son las siguientes:
Débitos: código 111 + código 759
Documentos: código 110 + código 758

2

Para la clasificación por rubro económico se utilizó la marca correspondiente al año 2015.
Para la clasificación por tamaño se utilizó la marca correspondiente al año 2015.
4
Esto quiere decir, que si las empresas se ordenaran en función de la variable debito de menor a
mayor, el número de empresas con débitos pequeños es muy distintos para los grupos de control y
tratamiento.
3

5

Al incluir este grupo de empresas las estimaciones no eran consistentes y se hacían no significativas,
principalmente por el alto peso relativo de este grupo en las variables de débitos.
3

Minuta: Resultados Resolución Transbank

Para tener un orden de magnitud, en el cuadro siguiente se presenta el promedio mensual de los débitos
y del n° de documentos para el grupo de tratamiento, para los años 2014 y 2016.
Promedio mensual del grupo de tratamiento (Transbank)
Año
2014
2016

Débitos($)
N° Documentos
1.559.929
1.740
1.765.529
2.451

Resultados
Se realizan estimaciones utilizando ambos grupos de control. En las tablas de resultados que siguen, se
presentan los rangos del efecto promedio porcentual de estas estimaciones; utilizando la declaración
promedio, es posible cuantificar estos efectos en recaudación. De forma adicional para la robustez de los
resultados, se presenta la estimación utilizando la mediana de las variables de interés. Esta última es una
regresión de cuantiles, que implica una especificación útil cuando existe gran dispersión en los datos, ya
que la mediana es menos sensible a los valores extremos que la media.
Se estimaron resultados para todo el universo: microempresas, empresas pequeñas, para el rubro de
comercio6 y para el rubro de hoteles y restaurantes. Como se aprecia de las tablas, a pesar de usar
muestras diferentes, los resultados son consistentes y de magnitudes similares.
En la tabla 1 se observan los resultados utilizando toda la muestra, el efecto promedio en los débitos
declarados está entre 10,2% y 10,6%, esto implica que el grupo que fue afectado por la nueva normativa
declaró débitos mayores que los grupos de control que no fueron afectados por la normativa. De la misma
forma, estos contribuyentes declararon un 7% más de documentos de débitos que los grupos de control.
Por lo tanto, la política del voucher como boleta incrementó tanto el monto del débito como
el número de documentos declarados. El efecto en la mediana de los débitos declarados está entre
12,3% y 14,0%, y en los documentos declarados entre 5,9% y 6,5%, lo que viene a confirmar el efecto
positivo en el pago de impuestos de la política.
Tabla 1: Efecto en el débito y en el número de boletas considerando toda la muestra
Universo
Débitos
N° Documentos
Aumento Promedio

10,2% - 10,6%

$148.450 - $165.352

7,0% - 7,0%

172 - 174

Aumento Mediana

12,3% - 14,0%

$78.679 - $85.211

5,9% - 6,5%

23 - 27

En las siguientes tablas se presentan los resultados de las estimaciones para subgrupos de contribuyentes.
En la tabla 2 y tabla 3 se estima solo para el grupo de microempresa y para el grupo de empresas
pequeñas, respectivamente. Se observa que el efecto porcentual promedio es más alto en las empresas
pequeñas que en las microempresas, tanto para los débitos como para el número de documentos.
En las empresas pequeñas el efecto en los débitos declarados está entre 10,4% y 13,8%, y en las
microempresas entre 9,0% y 10,8%. El número de documentos emitidos en las empresas pequeñas
aumenta entre un 9,5% y un 11,1%, y en las microempresas entre un 4,1% y 5,5%. Los efectos

6

Corresponde al rubro H - comercio al por mayor y menor, rep. veh.automotores/enseres domésticos.
4

Minuta: Resultados Resolución Transbank

estimados para el cambio en la mediana de ambos tipos de empresas, tanto para los débitos como para
el número de documentos, es significativo y porcentualmente un poco mayor a los efectos promedios.
Tabla 2: Efecto en el débito y en el número de boletas en las Microempresas
Microempresas
Débitos
N° Documentos
Aumento Promedio

9,0% - 10,8%

$30.107 - $37.228

4,1% - 5,5%

40 - 58

Aumento Mediana

13,6% - 13,8%

$37.314 - $38.554

5,7% - 6,2%

10 - 11

Tabla 3: Efecto en el débito y en el número de boletas en Empresas Pequeñas
Empresas Pequeñas
Débitos
N° Documentos
Aumento Promedio

10,4% - 13,8%

$187.245 - $244.125

9,5% - 11,1%

317 - 359

Aumento Mediana

12,8% - 14,2%

$169.215 - $184.117

10,1% - 10,3%

90- 91

Debido a que el uso de medios electrónicos como forma de pago es utilizado con mayor frecuencia en
algunos sectores económicos, en la tabla 4 y tabla 5 se presentan los resultados utilizando los
contribuyentes que pertenecen a los rubros de comercio y, por otra parte, a los del rubro de hoteles y
restaurantes. Los resultados indican que el efecto fue mayor en el rubro de hoteles y restaurantes, tanto
para los débitos declarados como para el número de documentos emitidos. En el rubro de restaurantes y
hoteles el aumento porcentual del débito se encuentra entre 11,5% y 14,2%, mientras que en el rubro
comercio está entre 9,9% y 10,6%. Por el lado de los documentos emitidos el aumento está entre 6,6%
y 8,5% para el rubro de hoteles y restaurantes, y entre 6,0% y 6,8% para el rubro comercio.
Tabla 4: Efecto en el débito y en el número de boletas en rubro Comercio
Comercio
Débitos
N° Documentos
Aumento Promedio

9,9% - 10,6%

$154.231 - $157.161

6,0% - 6,8%

163 - 185

Aumento mediana

13,5% - 14,4%

$89.796 - $90.716

4,3% - 5,3%

20 - 23

Tabla 5: Efecto en el débito y en el número de boletas en rubro Hoteles y Restaurantes
Hoteles y Restaurantes
Débito
N° Documentos
Aumento Promedio

11,5% - 14,2%

$203.849 - $248.898

6,6% - 8,5%

156 - 209

Aumento mediana

17,4% - 21,0%

$130.159 - $151.983

10,4% - 10,7%

49 - 53

Por otra parte, se estiman los códigos de crédito para determinar si al mismo tiempo existe un
abultamiento de créditos en el periodo que pueda compensar el aumento de débitos, y los resultados no
muestran valores significativos para las variables de crédito (código 537 del F29).

5

Minuta: Resultados Resolución Transbank

Considerando a los contribuyentes afectados por la nueva normativa, estos resultados
implican, utilizando el efecto promedio de la tabla 1, que se generó una declaración adicional
en los débitos del año 2016 entre $99 y $110 millones de dólares.

Conclusiones
Se observa que existe evidencia estadística en relación a que los contribuyentes afectados por la
Resolución que establece que el voucher de las transacciones pagadas con tarjetas de crédito o débito
es válido como boleta aumentan sus débitos por estas transacciones entre un 10,2% y un 10,6%, y
emiten un 7% más de estos documentos. Considerando estimaciones para el efecto en la mediana, los
resultados positivos de la medida se mantienen.
Al separar el análisis por tamaño de empresas, se observa que el efecto es un poco mayor en las empresas
pequeñas que en las microempresas. Y analizando por rubros económicos, hay evidencia que en el rubro
de hoteles y restaurantes se presenta un efecto mayor al rubro de comercio. Cuando se analizan los
códigos de créditos, no hay evidencia estadística de cambios significativos.

Los resultados anteriores implican que la decisión que establece que el voucher de las transacciones
pagadas con tarjetas de crédito o débito sea válido como boleta origina una declaración adicional de
débitos para el año 2016 de entre $99 y $110 millones de dólares anuales.
Este incremento explica en torno al 8% de la mayor recaudación del IVA, en términos nominales, para el
año 2016 (respecto al 2015).

6
