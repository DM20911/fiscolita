---
url: https://www.sii.cl/destacados/reavaluo_agricola/2024/INFORME_FINAL_LP-184_VF_RZ.pdf
titulo: INFORME FINAL
categoria: destacado
---
INFORME FINAL
“DETERMINACIÓN ZONAS DE SIMILAR POTENCIAL
PRODUCTIVO SILVOAGROPECUARIO (ZSPPS)”

Licitación LP-184

SII
Servicio de Impuestos Internos

Santiago, 02 de febrero 2024

Contenido

1.
2.

Introducción ........................................................................................................ 1
Metodología y resultados ................................................................................... 2
2.1 Generación y preparación de la base climática de alta resolución ............................. 2
2.2 Elaboración de Cartografía de micro-distritos agroclimáticos .................................... 5
2.3 Preparación de las variables climáticas secundarias para estimar el potencial agrícola
de las especies cultivadas. ............................................................................................... 22
2.4 Evaluación del potencial productivo de especies cultivadas ..................................... 27
2.4.1 Variables Bioclimáticas que se utilizaron para la estimación de potenciales de
producción para especies frutales, cultivos, praderas y plantaciones forestales. .......... 27
2.4.2 Variables Bioclimáticas que se utilizarán para la estimación de potenciales de
producción para cultivos anuales .................................................................................... 29
2.5 Calculo del índice de potencialidad agroclimática (IPAC).......................................... 30
2.5.1 Índices de potencial productivo para especies en riego y en secano .................... 52
2.6 Interfaz para la gestión de las bases de datos ........................................................... 55

3.
4.

Referencias bibliográficas ................................................................................. 59
Descripción del contenido de los shape y archivos adjuntos ........................... 60
Anexo 1 ............................................................................................................................ 60
Anexo 2 ............................................................................................................................ 62
Anexo 3 ............................................................................................................................ 63
Anexo 4: Manual de usuario ............................................................................................ 65

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
1. Introducción
La licitación LP-184 tuvo como objetivo la identificación de zonas con similar potencial
productivo silvoagropecuario a nivel nacional, considerando particularidades
agroclimáticas del territorio y diversas variables ambientales y territoriales que inciden
directamente en la capacidad productiva y competitividad de la producción
silvoagropecuaria. Esta herramienta está diseñada como un apoyo esencial en el proceso
de avalúo de los bienes raíces de la primera serie agrícola, conforme al artículo 4° de la ley
9.886 de bases sobre Contratos Administrativos de Suministro y Prestación de Servicios.
El enfoque técnico adoptado para alcanzar los objetivos de la licitación se basó en una
metodología que integra variables climáticas, agroclimáticas, modelación numérica,
sistema de información geográfica y características territoriales, adaptándose a la compleja
geografía chilena. Considerando la variabilidad climática que caracteriza al territorio, se
llevó a cabo una zonificación de microdistritos agroclimáticos, basada en una malla
geográfica con información detallada con una resolución de 1 km² (1980 - 2020). Cada punto
de esta malla incluye datos esenciales como temperaturas extremas, precipitación,
humedad del aire, radiación solar, evapotranspiración, número de días cálidos, horas de
frío, número de heladas y otras variables relevantes para el potencial productivo agrícola.
De este modo, la herramienta se sustenta en información histórica y modelos digitales de
elevación para modelar topoclimáticamente variables agroclimáticas primarias, derivando
luego variables agroclimáticas secundarias, necesarias para la determinación del potencial
productivo de diversas especies agrícolas.
Para sintetizar las complejas relaciones ecofisiológicas que condicionan la adaptación de
especies cultivadas a diversas condiciones climáticas, se utilizó el modelo ADAPTCHECK,
desarrollado por el equipo ejecutor en las últimas décadas. Este modelo analiza
exhaustivamente el ciclo fenológico de cada especie, evaluando en qué medida, las
condiciones climáticas satisfacen sus requerimientos para garantizar una producción
óptima en calidad y cantidad. Basado en una extensa base de datos, calibración y validación,
el sistema proporciona un diagnóstico detallado del comportamiento de cada especie
frente a variaciones climáticas, siendo un recurso esencial en la toma de decisiones para el
sector agrícola. Finalmente, se determinó la aptitud agroclimática de 11 especies frutales,
5 cultivos anuales, praderas naturales y plantaciones forestales para todo el territorio
nacional.

1

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
2. Metodología y resultados
Como consecuencia de una compleja geografía, las condiciones climaticas del territorio
varian significativamente en espacios territoriales relativamentelos estrechos. Este es el
caso de las temperaturas, la ventosidad, el riesgo de heladas y el regimen de
precipitaciones. Esto hace que los potenciales de produccion cambien abruptamente con la
distancia al mar, la altitud o la orientacion del relieve. Para capturar esta variabilidad se
realizó una zonificacion de microdistritos agroclimaticos, en base a una malla geografica
que contiene información con una resolución de 1 Km2 para el periodo 1980-2020. En cada
punto se dispone de las temperaturas extremas, precipitación, humedad del aire, radiacion
solar, evapotranspiracion, numero de días calidos, horas de frio, numero de heladas y otras
variables relevantes para el potencial productivo agrícola.
A partir de la información histórica y el modelo digital de elevación se modelaron
topoclimáticamente las variables agroclimáticas primarias (las que provienen de la red de
estaciones de tierra). Una vez modeladas estas variables, en cada punto se calculan
variables secundarias o derivadas como horas de frio, días grado, evapotranspiracion, defcit
hídrico, numero de días calidos. Con este conjunto de variables se determina el potencial
productivo de especies agrícolas.
Para sintetizar las relaciones ecofisiológicas que condicionan la adaptación de las especies
cultivadas frente a diversas condiciones climáticas, hemos usado el modelo ADAPTCHECK,
el cual el equipo ejecutor ha venido desarrollando en los últimos 20 años. Este modelo
realiza un completo recorrido del ciclo fenológico de cada especie, verificando en qué
medida las condiciones climáticas satisfacen los requerimientos de la especie para
garantizar una buena producción en calidad y cantidad. El sistema se basa en una extensa
base de datos que sintetiza la información experimental disponible sobre las respuestas
adaptativas de las especies frente a las variables del clima, de modo de proveer un acabado
diagnóstico del comportamiento que la especie tendrá en diversas condiciones climáticas.
2.1 Generación y preparación de la base climática de alta resolución
Se dispone de la línea base climática para el periodo 1980-2020 con datos de temperaturas,
humedad del aire, radiacion solar y precipitaciones. Esta base de datos se construyo a partir
de los datos de las estaciones de la Red Agroclimatica Nacional (INIA, FDF, Meteovid, DMC)
y datos de la dirección General de Aguas (DGA).
Dependiendo de la naturaleza de la estación meteorológica se contó con observaciones de:
temperatura, precipitación, humedad relativa y/o radiación solar. En total se utilizaron 350
2

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
estaciones de temperatura, humedad relativa y radiación solar, y 500 estaciones para las
precipitaciones distribuidas en el territorio nacional.

Figura 1. Red de estaciones climatologicas y complejidad del relieve
A pesar de este numero de estaciones meteorológicas disponibles, en algunas áreas,
especialmente montañosas, existe una baja densidad de estaciones. En estas áreas se
requiere densificar los datos climáticos para construir una cartografía de alta resolución
espacial. Para las temperaturas, se cuenta con metodologías apoyadas con imágenes
térmicas satelitales (NOAA-AVHRR) que permiten mejorar el análisis de los gradientes
térmicos generados por el relieve, la distancia al mar y la altitud (Figura 2).

3

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 2. Temperatura de aire desde datos satelitales.

La modelación se realiza con resolución de 1 x 1 km, mediante modelos regresivos no
lineales, donde cada punto contiene la información de las variables climáticas primarias
modeladas: temperaturas extremas, precipitación, humedad relativa, radiación solar. Una
vez modeladas las variables climáticas, los resultados se validaron confrontando los datos
modelados con los registros de tierra, en puntos donde se cuenta con estaciones
meteorologicas (Figura 3 y 4).

4

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 3. Validación modelo de temperaturas máxima de enero para una cuenca.
Temperatura modelada v/s temperatura observada proveniente de las estaciones
meteorológicas.

Figura 4. Validación modelo de precipitaciones anuales para una cuenca. Precipitación
modelada v/s precipitación observada proveniente de las estaciones meteorológicas.

2.2 Elaboración de Cartografía de micro-distritos agroclimáticos
Para establecer los subdistritos agroclimáticos o unidades climáticamente homogéneas, se
tilizó la técnica de clustering multivariado que considerará la temperatura máxima de enero
(lo que aporta el atributo de calidez del verano), la temperatura mínima de julio, las horas
frío, precipitación anual y altitud. El clustering agrupa puntos de una malla geográfica
entregando unidades territoriales que cumplen con el requisito de mínima varianza.
5

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Una vez definidos los microdistritos, ellos fueron superpuestos con los limites comunales
de modo de cortar las comunas, generando asi los “sectores” dentro de cada comuna. Cada
sector será entonces un territorio de similares condiciones climaticas, al interior de cada
comuna (Figura 5 a 20). }

Figura 5. Zonas de similares condiciones agroclimáticas para la región de Arica y
Parinacota

6

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 6. Zonas de similares condiciones agroclimáticas para la región de Tarapacá.

7

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 7. Zonas de similares condiciones agroclimáticas para la región de Antofagasta.

8

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 8. Zonas de similares condiciones agroclimáticas para la región de Atacama.

9

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 9. Zonas de similares condiciones agroclimáticas para la región de Coquimbo.

10

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 10. Zonas de similares condiciones agroclimáticas para la región de Valparaíso.

11

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 11. Zonas de similares condiciones agroclimáticas para la región Metropolitana.

12

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 12. Zonas de similares condiciones agroclimáticas para la región de O’Higgins.

13

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 13. Zonas de similares condiciones agroclimáticas para la región del Maule.

14

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 14. Zonas de similares condiciones agroclimáticas para la región de Ñuble.

15

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 15. Zonas de similares condiciones agroclimáticas para la región de Biobío.

16

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 16. Zonas de similares condiciones agroclimáticas para la región de La Araucanía.

17

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 17. Zonas de similares condiciones agroclimáticas para la región de Los Ríos.

18

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 18. Zonas de similares condiciones agroclimáticas para la región de Los Lagos.

19

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 19. Zonas de similares condiciones agroclimáticas para la región de Aysén.

20

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 20. Zonas de similares condiciones agroclimáticas para la región de Magallanes.

21

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
2.3 Preparación de las variables climáticas secundarias para estimar el potencial agrícola de
las especies cultivadas.
A través de modelos desarrollados por el equipo de trabajo, se calcularon variables
climáticas derivadas a nivel mensual como evapotranspiración de referencia, días grados
base 10, horas de frio, déficit hídrico, excedente hídrico, numero de heladas, índices de
aridez, índices de humedad, entre otras. Todas estas variables son relevantes para la
capacidad productiva de la tierra, algunas de ellas actuan como condicionantes del éxito de
las especies y otras como riesgos esporadicos, que pueden alcanzar dimensiones
catastroficas. Mientras las primeras se les trata como variables de efecto deterministico, las
segundas como variables aleatorias, asociadas a una probabilidad de ocurrencia.

Para establecer la micro-zonificacion climática se preparan mapas de las variables
principales, en alta resolución (1 x 1 Km). A continuación se presentan los resultados para
las prinicipales variables obtenidas de la actualización de la cartografía de variables
primarias y derivadas complementarias para el periodo 1980 – 2020 (figura 21 a 26)

22

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 21. Temperatura máxima para el mes de enero en el periodo 1980-2020 para cada
unidad (comuna + distrito agroclimático).

Figura 22. Temperatura mínima para el mes de julio en el periodo 1980-2020 para cada
unidad (comuna + distrito agroclimático).
23

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Precipitación anual:
La precipitación es una de las condicionantes más fuertes para la agricultura de secano. Por
otra parte, la tendencia decreciente en las precipitaciones será uno de los factores más
gravitantes en la seguridad de riego a futuro. Contrariamente, la disminución de las lluvias
estivales en la zona sur, está siendo un factor favorable para el desarrollo de una fruticultura
de clima mediterraneo, lo cual esta aumentando las opciones agricolas en latitudes más
altas.

Figura 23. Precipitación anual en el periodo 1980-2020 para cada unidad (comuna + distrito
agroclimático).

Horas de frío:
Existe una fuerte variación en las las horas de frio desde el litoral hacia el interior. Mientras
la baja disponibilidad de frio es una adversidad para las especies caducas, es una ventaja
para las especies persistentes. Igualmente el menor frio invernal es una ventaja para los
cultivos de secano, cuyo rendimiento es claramente más alta en zonas costeras.

24

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 24. Suma de horas de frío anuales en el periodo 1980-2020 para cada unidad
(comuna + distrito agroclimático).
Días grado:
Los días grado representa a la disponibilidad de calor para crecer y madurar que encuentran
los cultivos. La costa, claramente más fresca limitando a las especies más exigentes en calor,
las cuales aumentan su potencial hacia el interior. Por el contrario, las especies menos
tolerantes a las altas temperaturas, encuentran condiciones más favorables en las cercanias
de la costa.

25

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 25. Suma días grado anuales en el periodo 1980-2020 para cada unidad (comuna +
distrito agroclimático).

Figura 26. Déficit hídrico en el periodo 1980-2020 para cada unidad (comuna + distrito
agroclimático).
26

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

2.4 Evaluación del potencial productivo de especies cultivadas
La aptitud agroclimática de especies cultivadas se determina mediante el desarrollo de
índices de riesgos agroclimáticos que expresan el potencial productivo de estas especies.
Los índices proporcionan información sobre el grado de cumplimiento de las exigencias
bioclimáticas de las diferentes especies en un sitio. Los índices de riesgo se calculan en
base a una serie de variables que afectan al desarrollo y productividad de cada especie
durante las distintas fases fenológicas. Un riesgo será más alto en la medida de que más se
aparte la conducta de una variable climática del intervalo exigido por una especie.
Cuando se produce un desfase en una variable climática y las exigencias de la especie, los
efectos pueden seguir diversos conductos, pero finalmente se propagan hasta la
productividad y la calidad de la producción, incidiendo sobre el éxito productivo de la
especie en dicha condición climática. Será por lo tanto más riesgoso, colocar una especie
donde el número y dimensión de los desfases bioclimáticos sean mayores.
2.4.1 Variables Bioclimáticas que se utilizaron para la estimación de potenciales de producción para
especies frutales, cultivos, praderas y plantaciones forestales.

Las variables bioclimáticas determinantes del potencial productivo del clima y que serán
usadas en esta propuesta de trabajo son:
•
•
•
•
•
•
•
•
•
•
•
•
•

Número de heladas en el ciclo anual de cada especie
Número de heladas en floración
Temperatura máxima en flor y cuaja
Temperatura mínima en flor y cuaja
Precipitación en flor
Número de días con temperatura máxima sobre 25°C
Número de días con temperatura máxima sobre 20°C
Temperatura máxima en madurez
Temperatura mínima en madurez
Días cálidos a la madurez
Precipitación a la cosecha
Radiación solar a la madurez
Índice de frío invernal.

27

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Para cada una de estas variables se define un valor o rango óptimo para cada especie, tal
como se muestra en las siguientes tablas.
Las adversidades bioclimáticas pueden operar por déficit o por exceso, de modo que los
índices de riesgo se expresan en una escala de -3 a +3 (tabla 1)
Tabla 1. Índice de riesgo bioclimático por fase fenológica y escala de aptitud agroclimática.
Índice riesgo bioclimático
por fase fenológica
-3
-2
-1
0
+1
+2
+3

Aptitud
Fuertemente deficiente
Deficiente
Levemente deficiente
Ausencia de riesgo
Levemente excedentario
Moderadamente excedentario
Fuertemente excedentario

A continuación se presenta la aplicación del sistema de indices para dos especies frutales
en una localidad X

Tabla 2. Índices de riesgos bioclimáticos por fase fenológica para arándano
VARIABLE

VALOR

UNIDAD

VALOR RECOMENDABLE

Índice riesgo fase
fenológica

N° Heladas en el ciclo

0.3

N°

<2

N° Heladas en floración

0

N°

<1

T max en flor y cuaja

20.6

°C

15-20

T min en flor y cuaja

8.7

°C

8-14

Precipitación en flor

28.1

mm

<50

N° días con Tmax > 25°C

97.6

N°

50-90

N° días con Tmax > 20°C

158.5

N°

>90

T max pinta-madurez

27.8

°C

20-25

1

T min pinta-madurez

12.3

°C

8-12.5

1

Días cálidos a madurez

46

°C

Precipitación cosecha

7

mm

<30

Rad. solar madurez

621.7

cal/cm2 d

>400

Índice de frio invernal*

0.7

-

>0.95

1

-2

28

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Tabla 3. Índices de riesgos bioclimáticos por fase fenológica para cerezo
VARIABLE

VALOR

UNIDAD

VALOR RECOMENDABLE

N° Heladas en el ciclo

0.8

N°

<1.0

N° Heladas en floración

3.6

N°

<0.5

T max en flor y cuaja

16.3

°C

15-22

Índice riesgo fase
fenológica
3

T min en flor y cuaja

5.5

°C

7-14

-1

Precipitación en flor

87.1

mm

<30

3

N° días con Tmax > 25°C

74.2

N°

40-100

N° días con Tmax > 20°C

136.5

N°

>80

T max pinta-madurez

24.2

°C

22-26

T min pinta-madurez

8.5

°C

8-14

Precipitación cosecha

86.7

mm

<15

Rad. Solar madurez

519.8

cal/cm2 d

450-550

1

-

>0.95

Índice de frio invernal*

3

El índice de aptitud agroclimática (IAA), corresponde a 1 menos la suma de los valores
absolutos de todos los riesgos calculados por fase fenológica (ecuación 1) y la normalización
de este. Mientras menor sea su valor, más riesgosa se hace la producción de una especie.
Por lo general, en base a la experiencia, una especie puede alcanzar producciones
competitivas, con un índice integrado sobre 0.5. Las zonas más óptimas se sitúan por
encima de 0.7; un sector con índice 1, representa el óptimo bioclimático para la especie,
por cuanto representa ausencia de riesgos.

12

𝐼𝑛𝑑𝑖𝑐𝑒 𝑎𝑝𝑡𝑖𝑡𝑢𝑑 𝑎𝑔𝑟𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑎 = 1 − ∑ 𝐴𝑏𝑠(𝐼𝑛𝑑𝑖𝑐𝑒𝑠 𝑟𝑖𝑒𝑠𝑔𝑜𝑠 𝑏𝑖𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑜𝑠 𝑝𝑜𝑟 𝑓𝑎𝑠𝑒)
1

2.4.2 Variables Bioclimáticas que se utilizarán para la estimación de potenciales de producción para
cultivos anuales

Las variables bioclimáticas consideradas para la estimación del índice de riesgo, se muestran
separadas por cultivos. Al igual que en frutales, para cada variable se define un valor o rango
óptimo en las diferentes fases fenológicas, tal como se muestra en las tablas siguientes. El
índice integrado en este caso corresponde al promedio de los índices parciales.

29

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Trigo:
Las variables bioclimáticas consideradas para la estimación del índice en trigo fueron las
siguientes:
Número de heladas en el ciclo, temperatura máxima en flor, temperatura mínima en flor,
número de días templados (T>20°C), temperatura máxima a la maduración, temperatura
mínima a la maduración, precipitación a la cosecha, radiación solar a la maduración.
Tabla 4. Índices de riesgos bioclimáticos por fase fenológica para trigo
VARIABLE

VALOR

UNIDAD

VALOR RECOMENDABLE

N° Heladas en el ciclo

0.1

N°

<10

T max en flor y cuaja

21.3

°C

12-23

T min en flor y cuaja

7.5

°C

5-18

N° días con Tmax > 20°C

162

N°

>80

T max madurez

25.3

°C

18-28

T min madurez

7.8

°C

8-14

Precipitación cosecha

13.2

mm

<200

Rad. solar madurez

594.2

cal/cm2 d

>500

Índice riesgo fase
fenológica

-1

-1

Para resumir todas las limitaciones del clima en un solo indice para una determinada
especie, que llamaremos IAA, se usará un modelo aditivo como el siguiente:
10

𝐼𝑛𝑑𝑖𝑐𝑒 𝑎𝑝𝑡𝑖𝑡𝑢𝑑 𝑎𝑔𝑟𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑎 = 1 − ∑ 𝐴𝑏𝑠(𝐼𝑛𝑑𝑖𝑐𝑒𝑠 𝑟𝑖𝑒𝑠𝑔𝑜𝑠 𝑏𝑖𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑜𝑠 𝑝𝑜𝑟 𝑓𝑎𝑠𝑒)
1

Debido a que los riesgos agroclimáticos afectan de forma diferentes a cada especie, se
utilizaron ponderadores para cada indice de riesgo, los cuales pueden ser modificados en la
herramienta que se adjunta en esta entrega.
2.5 Calculo del índice de potencialidad agroclimática (IPAC)
Las posibilidades productivas de cada especie “e” en cada “sector climatico” en cada
comuna, queda representada por un indice de aptitud agroclimatica por especie (IACe). De
este modo, el indice de potencial agroclimatico del sector “s” (IPACs) corresponderá a la
suma ponderada de los IACe para todas las especies. Mientras más alto sea el IPAC, mayores
seran las opciones productivas del sector y mejores las condiciones de produccion que
encuentran las especies cultivadas. Para esto, se usaran como indicadoras, las mayores
30

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
especies futales y de cultivos anuales. Se usaran las 8 especies frutales mencionadas
anteriormente (arándanos, avellanos, cerezos, cítricos, duraznos, nogales, paltos y uva de
mesa)). Adicionalmente se evaluaran 5 especies anuales (trigo, papa, maiz, tomate,
porotos).
𝑁

𝐼𝑃𝐴𝐶𝑠 = ∑ 𝐼𝐴𝐶𝑒
1

Por este procedimiento, cada sector queda caracterizado por una serie de IACe y un valor
IPACs que caracteriza de manera integradora las capacidades productivas que ofrece el
clima del lugar. Se podrán usar ponderadores que permitan dar más peso a ciertas especies
que a otras, en funcion de condiciones comerciales y rentabilidad, las cuales son variables
en el tiempo.
Las especies analizadas en este estudio fueron: arándano, avellano, cerezo, citricos,
duraznos, nogal, palto, uva de mesa, manzano, , maíz, papa, poroto, tomate, trigo, praderas,
eucalipto y pino. En la última etapa se agregaron uva vinifera cepa blanca, uva vinifera cepa
tinta, dada la importancia que reviste en la producción nacional. Además, se incorporó
especie de pradera más resistente a las bajas temperaturas en la zona austral del país
En la tabla 5 se muestran especies que pueden ser análogas o próximas en sus
requerimiento bioclimáticos a las mencionadas anteriormente

31

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Tabla 5. Potencial productivo para especies análogas o próximas en sus requerimientos
bioclimáticos
Arándano
Avellano
Cerezo
Manzano
Cítricos
Durazno
Nogales
Palto
Uva de mesa
Maíz
Papa
Poroto
Tomate
Trigo
Eucalipto
Pino

Frambuesa

Peral
Naranjo, limón, Lima, Mandarina
Ciruela, Nectarino, Almendro, olivo

Kiwi
Pimentón, Girasol, esparrago, Sorgo, zapallo, melón, sandia
Cebolla, ajo, remolacha, repollo, raps
Garbanzo, Lenteja
Arroz
Cebada, Centeno, Avena

A continuación, se presentan los mapas que muestan los resultados obtenidos para los
índices de aptitud agroclimática tanto para los frutales como para los cultivos anuales. En
el caso de los frutales, se muestran los resultados desde la región de Atacama hasta la
región de Los Lagos, con el proposito de distinguir la mayor variabilidad espacial que
presentan. Sin embargo, en los shape adjuntos se incluyen los resultados para todo el
territorio nacional. Por otro lado, los ínidice de aptitud agroclimática para los cultivos
anuales se presentan en las figuras 27 a 45.

32

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 27. Índice de aptitud agroclimática para el arándano entre la región de Atacama y la
región de Los Ríos.

33

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 28. Índice de aptitud agroclimática para el avellano entre la región de Atacama y la
región de Los Ríos.

34

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 29. Índice de aptitud agroclimática para el cerezo entre la región de Atacama y la
región de Los Ríos.

35

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 30. Índice de aptitud agroclimática para los cítricos entre la región de Atacama y la
región de Los Ríos.

36

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 31. Índice de aptitud agroclimática para el durazno entre la región de Atacama y la
región de Los Ríos.

37

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 32. Índice de aptitud agroclimática para el nogal entre la región de Atacama y la
región de Los Ríos.

38

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 33. Índice de aptitud agroclimática para el palto entre la región de Atacama y la
región de Los Ríos.

39

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 34. Índice de aptitud agroclimática para la uva de mesa entre la región de Atacama
y la región de Los Ríos.

40

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 35. Índice de aptitud agroclimática para el manzano entre la región de Atacama y
la región de Los Ríos.

41

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 36. Índice de aptitud agroclimática para la uva vinifera de cepa blanca entre la región
de Atacama y la región de Los Ríos.

42

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 37. Índice de aptitud agroclimática para la uva vinifera de cepa tinta entre la región
de Atacama y la región de Los Ríos.

43

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 38. Índice de aptitud agroclimática para el maíz.

44

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 39. Índice de aptitud agroclimática para la papa.

45

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 40. Índice de aptitud agroclimática para el poroto.

46

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 41. Índice de aptitud agroclimática para el tomate.

47

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 42. Índice de aptitud agroclimática para el trigo.

48

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 43. Índice de aptitud agroclimática para las praderas en todo Chile.

49

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 44. Índice de aptitud agroclimática para eucalipto en todo Chile.

50

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 45. Índice de aptitud agroclimática para pino en todo Chile.

51

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
2.5.1 Índices de potencial productivo para especies en riego y en secano

Luego de obtenidos los indices de aptitud agroclimática para cada especie (e), se calculó el
índice de potencial agroclimático del sector o unidad (IPAC) corresponde al promedio de los
IAA para todas las especies bajo condiciones de riego y secano. Lo anterior como un
indicador de la aptitud de productiva de ese territorio. Mientras más alto sea el IPAC,
mayores serán las opciones productivas del sector (s) y mejores las condiciones de
producción que encuentran las especies.
∑ 𝐼𝐴𝐴𝑒
𝑁ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑒𝑠𝑝𝑒𝑐𝑖𝑒𝑠

𝐼𝑃𝐴𝐶𝑠 =

Por este procedimiento, cada sector comunal será caracterizado por una serie de IAA y un
valor IPACs que caracteriza de manera integradora las capacidades productivas que ofrece
el clima del lugar. Se podrán usar ponderadores que permitan dar más peso a ciertas
especies que a otras, en función de condiciones comerciales y rentabilidad, las cuales son
variables en el tiempo. La clasificación del potencial productivo agroclimático de acuerdo al
IPAC se muestra en la siguiente tabla:
Tabla 1. Clasificación del potencial productivo agroclimático de acuerdo al IPAC
CLASIFICACIÓN
IPAC

POTENCIAL PRODUCTIVO

0 > IPAC < 0.2
0.2 > = IPAC < 0.4
0.4 > = IPAC < 0.6
0.6 > = IPAC < 0.8
0.8 > = IPAC < 1

MUY BAJO
BAJO
MODERADO
ALTO
MUY ALTO

Las especies usadas para la obtención del IPAC bajo condiciones de riego son: Arándanos,
avellanos, cerezos, cítricos, duraznos, nogal, palto, uva de mesa, manzano, maíz, poroto,
tomate, papa y trigo y se muestran en la figura 4. En el caso del IPAC bajo condiciones de
secano, se utilizan las mismas especies, pero esta vez en condición de secano y se agregan
las praderas, pinos y eucalipto (figura 5).

52

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 46. Índice de Potencial Productivo Agroclimático (IPAC) por sector para las especies
bajo condiciones de riego.

53

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 47. Índice de Potencial Productivo Agroclimático (IPAC) por sector para las especies
bajo condiciones de secano.

54

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
2.6 Interfaz para la gestión de las bases de datos
Para gestionar y mantener actualizadas las bases de datos, así como para aplicar los
protocolos de indexación a los casos reales, se creó una interfaz que permita la integración
de los atributos de clima, aplicando el modelo de indexación para establecer la realidad de
predios agrícolas. Esta interfaz de usuario dispondrá de las herramientas para actualizar la
información, modificar el modelo de indexación utilizados ajustar los factores de
ponderación de cada una de las variables del modelo.
La herramienta adjunta se construyó en base a los índices obtenidos en las etapas
anteriores, para las diferentes especies de frutales, cultivos bajo condiciones de riego y
secano y para las praderas y plantaciones forestales. Estos índices representan la aptitud
agroclimática de especies cultivadas y se determinó mediante el desarrollo de índices de
riesgos agroclimáticos que expresan el potencial productivo de estas especies. Es
fundamental tener en cuenta que proporcionan información sobre el grado de
cumplimiento de las exigencias bioclimáticas de las diferentes especies en un sitio. Se
calcula en base a una serie de variables que afectan al desarrollo y productividad de cada
especie durante las distintas fases fenológicas.
El índice de aptitud agroclimática (IAA o IAC), corresponde a 1 menos la suma de los valores
absolutos de todos los riesgos calculados por fase fenológica, de modo que mientras menor
sea su valor, más riesgosa se hace la producción de una especie. Por lo general, en base a
la experiencia, una especie puede alcanzar producciones competitivas, con un índice
integrado sobre 0.5. Las zonas más óptimas se sitúan por encima de 0.7; un sector con índice
1, representa el óptimo bioclimático para la especie, por cuanto representa ausencia de
riesgos.
12

𝐼𝑛𝑑𝑖𝑐𝑒 𝑎𝑝𝑡𝑖𝑡𝑢𝑑 𝑎𝑔𝑟𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑎 = 1 − ∑ 𝐴𝑏𝑠(𝐼𝑛𝑑𝑖𝑐𝑒𝑠 𝑟𝑖𝑒𝑠𝑔𝑜𝑠 𝑏𝑖𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑜𝑠 𝑝𝑜𝑟 𝑓𝑎𝑠𝑒)
1

Debido a que los riesgos agroclimáticos afectan de forma diferentes a cada especie, se
utilizaron ponderadores para cada indice de riesgo, los cuales pueden ser modificados en la
herramienta que se adjunta en esta entrega.
Luego de obtenidos los indices de aptitud agroclimática para cada especie, se calculó el
índice de potencial agroclimático del sector o unidad (IPACs) el que corresponde al
promedio de los IAC para las especies bajo condiciones de riego y otro cálculo para las
especies cultivadas en secano. Lo anterior representa un indicador de la aptitud de
55

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
productiva de ese territorio. Mientras más alto sea el IPAC, mayores serán las opciones
productivas del sector y mejores las condiciones de producción encuentran las especies.
𝐼𝑃𝐴𝐶𝑠 =

∑ 𝐼𝐴𝐴𝑒
𝑁ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑒𝑠𝑝𝑒𝑐𝑖𝑒𝑠

Por este procedimiento, cada sector comunal será caracterizado por una serie de IAA y un
valor IPACs que caracteriza de manera integradora las capacidades productivas que ofrece
el clima del lugar. Se podrán usar ponderadores que permitan dar más peso a ciertas
especies que a otras, en función de condiciones comerciales y rentabilidad, las cuales son
variables en el tiempo.

56

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

A continuación, se presentan los detalles del funcionamiento de la herramienta. Se generó
una herramienta en excel que permite cambiar los ponderadores utilizados en los indices
bioclimaticos utilizados para calcular la aptitud productiva en cada cultivo. Por defecto, se
les asignó mayor ponderación a las horas de frio en especies caducas como cerezos,
avellano europeo y nogales, especies donde las horas de frio representan un factor
determinate en la cuaja y producción final. En el caso de las especies persistentes, como
paltos y citricos se le asignó mayor ponderación a las heladas en floración y en el ciclo ya
que este factor es crucial en la obtencion de fruta o perdida de producción.

Figura 48. Sección cálculo de íncides de aptitud productiva por especie. En esta sección es posible
cambiar el ponderador que se le asigna a cada índice bioclimatico por fase fenologica. Los cultivos
se encuentran separados en cada una de las hojas de la planilla excel.

En las 4 ultimas pestañas de la planilla excel se incluyen las secciones de cálculo de: Índice
potencialidad agroclimática integrado por sectores (IPACs) para las especies cultivas en
riego, Índice potencialidad agroclimática integrado por sectores (IPACs) para las especies
cultivadas en secano y las zonas con similar potencial productivo

57

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 49. Sección de cálculo de Índice potencialidad agroclimática (IPACe) e índice de
potencialidad agroclimática integrado por sector (IPACs)

Figura 50: Zonas con similar potencial agroclimático productivo.

58

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
3. Referencias bibliográficas
CIREN 1989 Requerimientos de clima y suelo. Frutales de hoja caduca. Publicación N°83
Hijmans, R.J., S.E. Cameron, J.L. Parra, P.G. Jones y A. Jarvis. (2005) Very high resolution
interpolated climate surfaces for global land
areas. International Journal of Climatology 25: 1965-1978.
IPCC. (2007) En: Parry, M.L.; Canziani, O.F.; Palutikof, J.P.; Van der Linden, P.J. y Hanson,
C.E. Climate Change 2007: Impacts, Adaptation and Vulnerability, Contribution of Working
Group II to the Fourth Assessment Report of the Intergovernmental Panel on Climate
Change, Cambridge University Press.
Santibáñez, F. 2001. El Modelado del Crecimiento, Desarrollo y Producción de Maíz, sobre
bases Ecofisiológicas, mediante el modelo SIMPROC. Revista de Agrometeorología
Argentina. 1: 7-16.
Santibáñez, F. et al 2017. Atlas Agroclimático de Chile: Tomo III. Regiones de Valparaíso,
Metropolitana O’Higgins y Maule. Facultad de Agronomía. Universidad de Chile. 208 pp.
WorldClim - Global Climate Data. http://www.worldclim.org/

59

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
4. Descripción del contenido de los shape y archivos adjuntos

Anexo 1

El archivo adjunto Unidades_variables.shp contiene variables agroclimáticas para cada
unidad de similares condiciones climáticas al interior de cada comuna. El significado de las
siglas presentes en el archivo se encuentra detallado a continuación:
TXE: Temperatura máxima enero (°C)
TNE: Temperatura mínima enero (°C)
TNJ: Temperatura mínima julio (°C)
TXJ: Temperatura mínima de julio (°C)
HRE: Humedad relativa enero (%)
HRJ: Humedad relativa julio (%)
RSE: Radiación solar enero (Cal/cm día)
RSJ: Radiación solar julio (Cal/cm día)
ETE: Evapotranspiración enero (mm)
ETJ: Evapotranspiración julio (mm)
SDGA: Suma días grados anuales. Días-grado o temperaturas efectivas (T>10oC). Constituye
un índice de disponibilidad de calor para el normal desarrollo y maduración de las especies
vegetales. La mayor precocidad se obtendrá en los lugares con la mayor suma de
temperaturas efectivas.
SHFM: Suma horas de frio mensuales. Suma número de horas en que la temperatura es
inferior a o 7.2°C.
PLH: Periodo libre de heladas (días).
NTH: Número total de heladas. Corresponde al número de días cuyas temperaturas
mínimas caen bajo los 0°C, pudiendo con ello crear condiciones adversas, por congelación
de los tejidos vegetales. Es una variable muy relevante para la sobrevivencia de las especies,
particularmente aquellas de origen subtropical, más sensibles a las heladas.
DCAL: Días cálidos. La mayoría de las plantas (principalmente especies templadas) y los
animales comienzan a tener problemas con su balance térmico con temperatura por encima
60

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
de los 25° C. Por esta razón a un día con temperatura máxima por encima de los 25° C se le
denomina “día cálido”. Mientras más horas la temperatura permanezca por sobre 25°C
menos eficiente se hace el metabolismo por cuanto gran parte del esfuerzo de plantas y
animales será dedicado a neutralizar los posibles efectos adversos de las altas
temperaturas.
PSEC: periodo seco. Período del año en que la precipitación es inferior al 50% de la demanda
evapotranspirativa (pp< 0.5ET). Cuando se produce esta condición normalmente los cultivos
necesitan de riego para subsistir. (Número de meses donde pp/etp < 0.5).
PHUM: Periodo Húmedo. Período del año en que la precipitación es superior a la demanda
evapotranspirativa (pp>ET). Cuando se produce esta condición, los suelos tienden a estar
bien abastecidos de agua y, posiblemente, parte de la lluvia escurre, percola hacia las napas
profundas o se acumula superficialmente. (Número de meses donde pp/etp >= 0.5).
PPA: Precipitación anual (mm)
DEFH: Déficit hídrico. El déficit hídrico es la diferencia negativa entre precipitación (P) y
evapotranspiración (Et). Esto representa la cantidad de agua potencialmente evaporada
que no está cubierta por la precipitación. Considerando que los suelos tienen una capacidad
limitada para almacenar agua, el déficit hídrico es normalmente una expresión del estrés
hídrico que las comunidades vegetales tienen que soportar a través del año. Existe una
relación proporcional entre el déficit hídrico y el grado de aridez climática. El déficit anual
de agua se calcula sumando las diferencias negativas mensuales (P - Et).
EXCH: Excedente hídrico. El excedente de agua es la diferencia positiva entre la
precipitación (P) y la evapotranspiración (Et). El excedente anual de agua se calcula
sumando las diferencias positivas mensuales (P - Et). Esta variable representa la cantidad
de agua potencialmente disponible para escurrir superficialmente y alimentar los cursos de
agua superficiales. La mayor parte del excedente de agua puede alimentar la corriente de
ríos o infiltrarse en el suelo, alimentando las aguas subterráneas.

61

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Anexo 2

Descripción de las variables bioclimáticas y el índice de aptitud agroclimática y las siglas
asociadas que se encuentran en el los shape de los cultivos y frutales, además en
HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm. El significado de las siglas
presentes en el archivo se encuentra detallado a continuación:

Unidad: Nombre de la comuna y número que identifica el distrito agroclimático al que
pertenece.
lat: Latitud
lon: Longitud
nhc: índice de riesgo bioclimático asociado al número de heladas en el ciclo.
nhf: índice de riesgo bioclimático asociado al número de heladas en floración.
txf: índice de riesgo bioclimático asociado a las temperaturas máximas en floración.
tnf: índice de riesgo bioclimático asociado a las temperaturas mínimas en floración.
pflor: índice de riesgo bioclimático asociado a la precipitación en floración.
T_25: índice de riesgo bioclimático asociado al número de días cálidos con temperaturas
superiores a 25°C.
T_20: índice de riesgo bioclimático asociado al número de días templados con temperaturas
superiores a 20°C.
Txmad: índice de riesgo bioclimático asociado a las temperaturas máximas en maduración.
Tnmad: índice de riesgo bioclimático asociado a las temperaturas mínimas en maduración.
ppcos: índice de riesgo bioclimático asociado a la precipitación a la cosecha.
rsmad: índice de riesgo bioclimático asociado a la radiación solar a la maduración.
ifrio: índice de riesgo bioclimático asociado al índice de frio
HR: índice de riesgo bioclimático asociado humedad relativa en floración
IAA: índice de aptitud agroclimática
IPAC: índice de potencial agroclimático integrado del sector o unidad

62

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Anexo 3

Descripción de las variables bioclimáticas y el índice de aptitud agroclimática y las siglas
asociadas que se encuentran en el shape INDICE_RIEGO e INDICE SECANO y en
HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm
Unidad: Nombre de la comuna y número que identifica el distrito agroclimático al que
pertenece.
lat: Latitud
lon: Longitud
IAA_ARANDA: Índice de aptitud agroclimática para el arándano.
IAA_AVELLA: Índice de aptitud agroclimática para el avellano.
IAA_CEREZO: Índice de aptitud agroclimática para el cerezo.
IAA_CITRI: Índice de aptitud agroclimática para los cítricos.
IAA_DURAZN: Índice de aptitud agroclimática para el durazno.
IAA_NOGAL: Índice de aptitud agroclimática para el nogal.
IAA_PALTO: Índice de aptitud agroclimática para el palto.
IAA_UVAMES: Índice de aptitud agroclimática para la uva de mesa.
IAA_UVABLA: Índice de aptitud agroclimática para la uva vinífera de cepa blanca.
IAA_UVATIN: Índice de aptitud agroclimática para la uva vinífera de cepa tinta.
IAA_MANZAN: Índice de aptitud agroclimática para el manzano.
IAA_MAIZ: Índice de aptitud agroclimática para el maíz.
IAA_PAPA: Índice de aptitud agroclimática para la papa.
IAA_POROTO: Índice de aptitud agroclimática para el poroto.
IAA_TOMATE: Índice de aptitud agroclimática para el tomate.
IAAA_TRIGO: Índice de aptitud agroclimática para el trigo.
PRADERA: Índice de aptitud agroclimática para la pradera (solo en secano).
IAA_EUCALIPTO: Índice de aptitud agroclimática para el eucalipto (solo en secano).
PINO: Índice de aptitud agroclimática para el pino (solo en secano).

63

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
IPAC_r: Índice de potencial agroclimático integrado del sector o unidad para condición de
riego.
IPAC_s: Índice de potencial agroclimático integrado del sector o unidad para condición de
secano.

64

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Anexo 4: Manual de usuario
(adjunto como un documento independiente)
1. Introducción
La licitación LP-184 tuvo como objetivo la identificación de zonas con similar potencial productivo
silvoagropecuario a nivel nacional, considerando particularidades agroclimáticas del territorio y
diversas variables ambientales y territoriales que inciden directamente en la capacidad productiva y
competitividad de la producción silvoagropecuaria. Esta herramienta está diseñada como un apoyo
esencial en el proceso de avalúo de los bienes raíces de la primera serie agrícola, conforme al artículo
4° de la ley 9.886 de bases sobre Contratos Administrativos de Suministro y Prestación de Servicios.
El enfoque técnico adoptado para alcanzar los objetivos de la licitación se basó en una metodología
que integra variables climáticas, agroclimáticas, modelación numérica, sistema de información
geográfica y características territoriales, en torno al potencial productivo de las tierras agrícolas.
Considerando la variabilidad climática que caracteriza al territorio, se llevó a cabo una zonificación
de microdistritos agroclimáticos, basada en una malla geográfica con información detallada con una
resolución de 1 km² (1980 - 2020). Cada punto de esta malla incluye datos esenciales como
temperaturas extremas, precipitación, humedad del aire, radiación solar, evapotranspiración,
número de días cálidos, horas de frío, número de heladas y otras variables relevantes para el
potencial productivo agrícola. De este modo, la herramienta se sustenta en información histórica y
modelos digitales de elevación para modelar topoclimáticamente variables agroclimáticas primarias,
derivando luego variables secundarias, necesarias para la determinación del potencial productivo
de diversas especies agrícolas.
Para sintetizar las complejas relaciones ecofisiológicas que condicionan la adaptación de especies
cultivadas a diversas condiciones climáticas, se utilizó el modelo ADAPTCHECK, desarrollado por el
equipo ejecutor en las últimas décadas. Este modelo analiza exhaustivamente el ciclo fenológico de
cada especie, evaluando en qué medida, las condiciones climáticas satisfacen sus requerimientos
para garantizar una producción óptima en calidad y cantidad. Basado en una extensa base de datos,
calibración y validación, el sistema proporciona un diagnóstico detallado del comportamiento de
cada especie frente a variaciones climáticas, siendo un recurso esencial en la toma de decisiones
para el sector agrícola. Finalmente, se determinó la aptitud agroclimática de 11 especies frutales, 5
cultivos anuales, praderas naturales y plantaciones forestales para todo el territorio nacional.

65

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
2. Metodología
Para determinar las zonas de similar potencial productivo em Chile, se siguió la metodología
detallada en el diagrama de la figura 1. Los microdistritos agroclimáticos, o unidades climáticamente
homogéneas, fueron obtenidos para el período 1980 - 2020 utilizando una técnica estadística que
permite la agrupación de unidades territoriales, misma metodología usada y validada en Atlas
Agroclimático de Chile (AGRIMED, 2015). Detalles de los datos y la metodología usada en esta
licitación se puede revisar en el informe final del proyecto.
Una vez establecidos los microdistritos agroclimáticos, se le superpusieron con los límites
comunales, manteniendo cada zona como un área con condiciones climáticas similares. Para cada
una de estas áreas, que cumplen con el requisito de homogeneidad, se realizó la modelación
topoclimática. Este proceso permitió obtener las variables agroclimáticas primarias, como las
temperaturas, humedad, radiación, precipitación, etc., utilizadas posteriormente en el cálculo de
variables agroclimáticas secundarias, tales como horas de frío, heladas, déficit hídrico, entre otras.
Se utilizó el modelo ADAPTCHECK, para sintetizar las relaciones ecofisiológicas que condicionan la
adaptación de las especies cultivadas frente a diversas condiciones climáticas. Este modelo realiza
un completo recorrido del ciclo fenológico de cada especie, verificando en qué medida las
condiciones climáticas satisfacen los requerimientos de la especie para garantizar una buena
producción en calidad y cantidad. ADAPTCHECK se basa en una extensa base de datos que sintetiza
la información experimental disponible sobre las respuestas adaptativas de las especies frente a las
variables del clima, de modo de proveer un acabado diagnóstico del comportamiento que la especie
tendrá en diversas condiciones climáticas.

66

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 1. Diagrama explicativo que detalla el proceso llevado a cabo durante el estudio.
(1) Descripción de las variables y siglas utilizadas en el Anexo 1. Los datos están disponibles en el
SHAPE_UNIDADES_VARIABLES.
(2) Descripción de las variables y siglas utilizadas en el Anexo 1. Los datos están disponibles en el
SHAPE_UNIDADES_VARIABLES.
(3) Descripción de las variables y siglas utilizadas en el Anexo 2. Los datos están disponibles en los shape de cada especie
en las carpetas CULTIVOS Y FRUTALES y en HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm
(4) Descripción de las variables y siglas utilizadas en el Anexo 3. Los datos están disponibles en el INDICE_RIEGO e INDICE
SECANO y en HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm

La aptitud agroclimática de especies cultivadas se determinó mediante el uso de índices de riesgos
agroclimáticos, los cuales expresan el potencial productivo de estas especies. Estos índices
proporcionan información sobre el grado de cumplimiento de las exigencias bioclimáticas de las
diferentes especies en un sitio determinado. El cálculo de los índices de riesgo se basa en una serie
de variables que afectan al desarrollo y productividad de cada especie durante las distintas fases
fenológicas (variables consideradas por el modelo ADAPTCHECK). Un riesgo será más alto en la
medida de que una variable climática más se aparte del intervalo considerado óptimo para una
especie.
Cuando se produce un desfase entre el valor de una variable climática y lo exigido por una especie,
los efectos pueden manifestarse de diversas maneras, pero finalmente se propagan hasta la
productividad y la calidad de la producción, incidiendo sobre el éxito productivo de la especie en

67

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
dicha condición climática particular. Será por lo tanto más riesgoso y menos productivo, colocar una
especie donde el número y dimensión de los desfases bioclimáticos sean mayores. Estas
adversidades bioclimáticas pueden operar por déficit o por exceso, reflejandose en los índices de
riesgo en una escala de -3 a +3 (tabla1)
Tabla 1. Índice de riesgo bioclimático por fase fenológica y escala de aptitud agroclimática.
Índice riesgo
bioclimático por
fase fenológica

Aptitud

-3

Fuertemente deficiente

-2

Deficiente

-1

Levemente deficiente

0

Ausencia de riesgo

+1

Levemente excedentario

+2

Moderadamente
excedentario

+3

Fuertemente excedentario

En la figura 2, se presentan las variables bioclimáticas utilizadas para estimar los potenciales de
producción del avellano en cinco zonas de la región del Maule. En el punto a, se evidencia la ausencia
de riesgo asociado al número de heladas en el ciclo, indicando que el número de ocurrencia de
heladas en estas zonas no representan una amenaza suficiente para afectar la producción de
avellanos. En el punto b, se observa que el riesgo está asociado a un exceso (+2), específicamente a
la temperatura máxima de maduración, o sea, la temperatura será más alta de lo recomendable para
esta especie, pudiendo ello representar un riesgo que afectará a la productividad de esta especie.
Por último, en el punto c, se observa que hay un déficit asociado al frío invernal, lo que podría afectar
al reposo, la inducción y la prolificidad floral de la especie.

68

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 2. Variables bioclimáticas utilizadas para estimar los potenciales de producción del avellano
en cinco localidades de la región del Maule
Una vez calculados los índices de riesgo para cada variable, el sistema suma los valores absolutos
de todos los riesgos. Como el valor absoluto de cada índice varía entre 0 y 3, entonces el máximo
valor de la suma es (Rmax):
Rmax = 3 * número de variables determinantes del riesgo total
El índice de aptitud agroclimática (IAA), corresponde a 1 menos la suma de los valores absolutos de
todos los riesgos normalizados, de modo que mientras menor sea su valor, más riesgosa se hace la
producción de una especie. Por lo general, en base a la experiencia, una especie puede alcanzar
producciones competitivas, con un índice integrado sobre 0.5. Las zonas más óptimas se sitúan por
encima de 0.7; un sector con índice 1, representa el óptimo bioclimático para la especie, por cuanto
representa ausencia de riesgos.
𝐼𝐴𝐴 = 1 − ∑12
1 𝐴𝑏𝑠(𝐼𝑛𝑑𝑖𝑐𝑒𝑠 𝑟𝑖𝑒𝑠𝑔𝑜𝑠 𝑏𝑖𝑜𝑐𝑙𝑖𝑚𝑎𝑡𝑖𝑐𝑜𝑠 𝑝𝑜𝑟 𝑓𝑎𝑠𝑒)/Rmax
Ecuación 1
Debido a que los riesgos agroclimáticos afectan de forma diferentes a cada especie, se utilizaron
ponderadores para cada indice de riesgo, los cuales pueden ser modificados en la herramienta que
se adjunta.
Luego de obtenidos los indices de aptitud agroclimática para cada especie, se calculó el índice de
potencial agroclimático integrado del sector o unidad (IPACs) el que corresponde al promedio de los
IAC (ecuación 2) bajo condiciones de riego y otro cálculo para secano. Lo anterior representa un
indicador integrado de la aptitud productiva de ese territorio, considerando el abanico de opciones
de cultivo, asi como los riesgos que encontrará la agricultura del lugar. Mientras más alto sea el IPAC,
mayores serán las opciones productivas del sector y mejores las condiciones de producción
encuentran las especies.

𝐼𝑃𝐴𝐶𝑠 =

∑ 𝐼𝐴𝐴𝑒
𝑁ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑒𝑠𝑝𝑒𝑐𝑖𝑒𝑠

69

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Ecuación 2

Por este procedimiento, cada sector comunal será caracterizado por una serie de IAA y un valor IPACs
que caracteriza de manera integradora las capacidades productivas que ofrece el clima del lugar
(figura 3). Se podrán usar ponderadores que permitan dar más peso a ciertas especies que a otras,
en función de condiciones comerciales y rentabilidad, las cuales son variables en el tiempo.

Figura 3. Descripción de la tabla de atributos de los IAA por especie e IPAC por sector en condiciones
de riesgo

70

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
3. Descripción de archivos y herramientas entregadas
Dentro de los archivos entregados en el estudio, se incluye un shape denominado
“Unidades_variables”, el cual contiene las variables agroclimáticas primarias y secundarias
correspondientes a cada una de las unidades o zonas previamente definidas. La figura 4 muestra la
tabla de atributos que se encuentra en este archivo. El glosario de términos se encuentra detallado
en el anexo 1.

Figura 4. Variables agroclimáticas para cada zona o unidad que se encuentra disponible en el
SHAPE_UNIDADES_VARIABLES. (Las siglas asociadas a cada variable están descritas en los anexos)
A continuación, se presenta el déficit hídrico como ejemplo de una de las variables obtenidas en la
primera parte del estudio y necesarias para la obtención de los potenciales agroclimáticos.

Figura 5. Déficit hídrico para todo el territorio chileno en el periodo 1980- 2020

71

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Otro de los productos proporcionados en el estudio se presenta en formato shape y como una
herramienta modificable (HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm). Esto se aplica a
cada una de las especies, ya sean frutales, cultivos, praderas o forestales. Cada conjunto de datos
incluye los índices relacionados con los distintos riesgos climáticos, así como el Índice de Aptitud
Agroclimática específico para la especie.

Figura 6. Tabla de atributos con las variables bioclimáticas utilizadas en el cálculo del IAA para
arándanos y figura con el índice de aptitud agroclimática. (Las siglas asociadas a cada variable están
descritas en los anexos)

72

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Si se desea ajustar los ponderadores de las variables bioclimáticas utilizadas en el cálculo del
potencial agroclimático, la herramienta facilita la recalibración del Índice de Aptitud Agroclimática
(IAA) para cada especie, permitiendo modificar la ponderación asignada a cada variable. Los
ponderados que aparecen en la figura 7 son los recomendados para el arándano y los utilizados en
el estudio

Figura 7. Ejemplo de la herramienta que permite el cambio de los ponderadores entre 0 y 1 (W) para
las variables bioclimáticas utilizadas en el cálculo del índice final (equivalente al IAA) por especies.
(Las siglas asociadas a cada variable están descritas en los anexos)

73

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Para condición de riego y secano están disponibles shape y planillas donde se encuentran
disponibles los IAA para todas las especies y el IPAC de riego y secano.

Figura 8. Descripción de la tabla de atributos de los IAA por especie e IPAC por sector en condiciones
de riesgo. Se incorporaron uvas viníferas de cepa blanca y tinta.

74

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 9. Descripción de la tabla de atributos de los IAA por especie e IPAC por sector en condiciones
de riesgo. Se incorporaron uvas viníferas de cepa blanca y tinta y praderas con una mayor tolerancia
a las bajas temperaturas en la zona austral

Dentro de la herramienta, se disponen de hojas de cálculo específicas utilizadas para el cálculo del
IPAC tanto para riego como para secano. El IPAC considera el promedio de los IAA de las especies
por zonas (ecuación 2).
A continuación, se presenta como ejemplo la hoja de cálculo que contiene el potencial productivo
de las especies condiciones de riego y el promedio de ellas (IPAC_Riego)

75

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Figura 10. Descripción de la planilla donde se realiza el cálculo de IPAC para el conjunto de las
especies por zonas. Se incorporaron uvas viníferas de cepa blanca y tinta.

76

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
En muchos casos la aptitud productiva es común a especies afines. Para extender el alcance de la
evaluación de la productividad, se pueden hacer las analogías siguientes entre especies:
Tabla 1. Potencial productivo para especies análogas o próximas en sus requerimientos bioclimáticos
Arándano
Avellano
Cerezo
Manzano
Cítricos
Durazno
Nogales
Palto
Uva de mesa
Maíz
Papa
Poroto
Tomate
Trigo
Eucalipto
Pino

Frambuesa

Peral
Naranjo, Limón, Lima, Mandarina
Ciruela, Nectarino, Almendro, Olivo

Kiwi
Pimentón, Girasol, Esparrago, Sorgo, Zapallo, Melón, Sandía
Cebolla, Ajo, Remolacha, Repollo, Raps
Garbanzo, Lenteja
Arroz
Cebada, Centeno, Avena

77

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Además, se incluye una clasificación del Índice de Potencial Agroclimático (IPAC) que se ajusta de
acuerdo a su potencial productivo en intervalos de 0.2, abarcando categorías desde muy bajo hasta
muy alto. Esta clasificación proporciona una perspectiva clara sobre el rendimiento agroclimático de
cada zona, permitiendo una evaluación más detallada de su idoneidad para diversos cultivos y
actividades agrícolas.

Figura 11. Clasificación sugerida para los IPAC

78

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Ejemplos
El uso del índice de potencial agroclimático (IPAC): En la figura 12, se presenta el índice de potencial
agroclimático por sector para condiciones de riego en la región del Maule. Considerando la
evaluación de los potenciales agroclimáticos, específicamente en la comuna de Colbún, se puede
observar que, en el sector más occidental de la comuna, el IPAC es de 0.84, indicando un potencial
productivo muy alto (tabla figura 11) al contar con riego y considerando la batería de especies
utilizadas. Al desplazarse a un sector intermedio de la comuna, se observa que el potencial
productivo disminuye a valores alrededor del 0.5, lo que implica un potencial moderado. Hacia la
cordillera, el potencial productivo cae a valores alrededor de 0.2, indicando un potencial bajo o muy
bajo, lo que sugiere que las producciones no son competitivas en esa área.
Es importante tener en cuenta que, en ausencia de riego, sería aplicar el IPAC para condiciones de
secano. Las diferencias resultantes se presentarán en ejemplos posteriores para una mejor
comprensión.

Figura 12. IPAC en condiciones de riego para la Región del Maule y la comuna de Colbún

79

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
En el caso de la figura 13, se presenta el índice de aptitud agroclimática para el arándano en riego.
Se realiza un análisis para evaluar cómo podría verse afectada la rentabilidad de la unidad productiva
considerando los factores agroclimáticos.

Figura 13. Aptitud agroclimática arándanos

80

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
En cuanto al uso de los resultados para el caso de riego o secano se muestra el ejemplo de la figura
14. Un predio que cuenta con riego ubicado en el punto morado en la figura, tendría valores de IPAC
de 0,6, indicando un alto potencial productivo según las condiciones agroclimáticas. Mientras que,
si el predio carece de riego, es decir bajo una condición de secano, los valores de IPAC disminuirían
a 0,27 de IPAC, representando un potencial productivo más bajo.

Figura 14. IPAC en condiciones de riego y secano para la Región de La Araucanía.

81

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Las limitaciones del suelo son adicionales a las climáticas, las cuales, por analogía pueden tratarse
de la misma forma. La inclusión de las variables de suelo está fuera del alcance de este proyecto, no
obstante, sugerimos usar una escala de evaluación como la siguiente:
Clase I, factor 1
Clase II, factor 0.9
Clase III, factor 0.70
Clase IV, factor 0.5
Clase V, factor Clase Variable según la limitación transitoria
Clase VI , FACTOR 0.25
Clase VII, factor 0.1
Clase VIII, factor 0, no agrícola
El índice de capacidad productiva final para cada especie quedaría como sigue:

Ip = Ic * Is

Donde, Ip: índice de potencial productivo clima-suelo, Ic: índice de potencial climático (IPAC), Is:
índice de clase de suelo,

82

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Anexo 1
El archivo adjunto Unidades_variables.shp contiene variables agroclimáticas para cada unidad de
similares condiciones climáticas al interior de cada comuna. El significado de las siglas presentes en
el archivo se encuentra detallado a continuación:
TXE: Temperatura máxima enero (°C)
TNE: Temperatura mínima enero (°C)
TNJ: Temperatura mínima julio (°C)
TXJ: Temperatura mínima de julio (°C)
HRE: Humedad relativa enero (%)
HRJ: Humedad relativa julio (%)
RSE: Radiación solar enero (Cal/cm día)
RSJ: Radiación solar julio (Cal/cm día)
ETE: Evapotranspiración enero (mm)
ETJ: Evapotranspiración julio (mm)
SDGA: Suma días grados anuales. Días-grado o temperaturas efectivas (T>10oC). Constituye un índice
de disponibilidad de calor para el normal desarrollo y maduración de las especies vegetales. La
mayor precocidad se obtendrá en los lugares con la mayor suma de temperaturas efectivas.
SHFM: Suma horas de frio mensuales. Suma número de horas en que la temperatura es inferior a o
7.2°C.
PLH: Periodo libre de heladas (días).
NTH: Número total de heladas. Corresponde al número de días cuyas temperaturas mínimas caen
bajo los 0°C, pudiendo con ello crear condiciones adversas, por congelación de los tejidos vegetales.
Es una variable muy relevante para la sobrevivencia de las especies, particularmente aquellas de
origen subtropical, más sensibles a las heladas.

83

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
DCAL: Días cálidos. La mayoría de las plantas (principalmente especies templadas) y los animales
comienzan a tener problemas con su balance térmico con temperatura por encima de los 25° C. Por
esta razón a un día con temperatura máxima por encima de los 25° C se le denomina “día cálido”.
Mientras más horas la temperatura permanezca por sobre 25°C menos eficiente se hace el
metabolismo por cuanto gran parte del esfuerzo de plantas y animales será dedicado a neutralizar
los posibles efectos adversos de las altas temperaturas.
PSEC: periodo seco. Período del año en que la precipitación es inferior al 50% de la demanda
evapotranspirativa (pp< 0.5ET). Cuando se produce esta condición normalmente los cultivos
necesitan de riego para subsistir. (Número de meses donde pp/etp < 0.5).
PHUM: Periodo Húmedo. Período del año en que la precipitación es superior a la demanda
evapotranspirativa (pp>ET). Cuando se produce esta condición, los suelos tienden a estar bien
abastecidos de agua y, posiblemente, parte de la lluvia escurre, percola hacia las napas profundas o
se acumula superficialmente. (Número de meses donde pp/etp >= 0.5).
PPA: Precipitación anual (mm)
DEFH: Déficit hídrico. El déficit hídrico es la diferencia negativa entre precipitación (P) y
evapotranspiración (Et). Esto representa la cantidad de agua potencialmente evaporada que no está
cubierta por la precipitación. Considerando que los suelos tienen una capacidad limitada para
almacenar agua, el déficit hídrico es normalmente una expresión del estrés hídrico que las
comunidades vegetales tienen que soportar a través del año. Existe una relación proporcional entre
el déficit hídrico y el grado de aridez climática. El déficit anual de agua se calcula sumando las
diferencias negativas mensuales (P - Et).
EXCH: Excedente hídrico. El excedente de agua es la diferencia positiva entre la precipitación (P) y la
evapotranspiración (Et). El excedente anual de agua se calcula sumando las diferencias positivas
mensuales (P - Et). Esta variable representa la cantidad de agua potencialmente disponible para
escurrir superficialmente y alimentar los cursos de agua superficiales. La mayor parte del excedente
de agua puede alimentar la corriente de ríos o infiltrarse en el suelo, alimentando las aguas
subterráneas.

Anexo 2

84

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

Descripción de las variables bioclimáticas y el índice de aptitud agroclimática y las siglas asociadas
que

se

encuentran

en

el

los

shape

de

los

cultivos

y

frutales,

además

en

HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm. El significado de las siglas presentes en el
archivo se encuentra detallado a continuación:

Unidad: Nombre de la comuna y número que identifica el distrito agroclimático al que pertenece.
lat: Latitud
lon: Longitud
nhc: índice de riesgo bioclimático asociado al número de heladas en el ciclo.
nhf: índice de riesgo bioclimático asociado al número de heladas en floración.
txf: índice de riesgo bioclimático asociado a las temperaturas máximas en floración.
tnf: índice de riesgo bioclimático asociado a las temperaturas mínimas en floración.
pflor: índice de riesgo bioclimático asociado a la precipitación en floración.
T_25: índice de riesgo bioclimático asociado al número de días cálidos con temperaturas superiores
a 25°C.
T_20: índice de riesgo bioclimático asociado al número de días templados con temperaturas
superiores a 20°C.
Txmad: índice de riesgo bioclimático asociado a las temperaturas máximas en maduración.
Tnmad: índice de riesgo bioclimático asociado a las temperaturas mínimas en maduración.
ppcos: índice de riesgo bioclimático asociado a la precipitación a la cosecha.
rsmad: índice de riesgo bioclimático asociado a la radiación solar a la maduración.
ifrio: índice de riesgo bioclimático asociado al ínidce de frio
HR: índice de riesgo bioclimático asociado humedad relativa en floración
IAA: índice de aptitud agroclimática

85

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
IPAC: índice de potencial agroclimático integrado del sector o unidad

86

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)
Anexo 3
Descripción de las variables bioclimáticas y el índice de aptitud agroclimática y las siglas asociadas
que se encuentran en el shape INDICE_RIEGO e INDICE SECANO y en
HERRAMIENTA_INDICES_FRUTALES_CULTIVOS_V3.xlsm
Unidad: Nombre de la comuna y número que identifica el distrito agroclimático al que pertenece.
lat: Latitud
lon: Longitud
IAA_ARANDA: Índice de aptitud agroclimática para el arándano.
IAA_AVELLA: Índice de aptitud agroclimática para el avellano.
IAA_CEREZO: Índice de aptitud agroclimática para el cerezo.
IAA_CITRI: Índice de aptitud agroclimática para los cítricos.
IAA_DURAZN: Índice de aptitud agroclimática para el durazno.
IAA_NOGAL: Índice de aptitud agroclimática para el nogal.
IAA_PALTO: Índice de aptitud agroclimática para el palto.
IAA_UVAMES: Índice de aptitud agroclimática para la uva de mesa.
IAA_UVABLA: Índice de aptitud agroclimática para la uva vinífera de cepa blanca.
IAA_UVATIN: Índice de aptitud agroclimática para la uva vinífera de cepa tinta.
IAA_MANZAN: Índice de aptitud agroclimática para el manzano.
IAA_MAIZ: Índice de aptitud agroclimática para el maíz.
IAA_PAPA: Índice de aptitud agroclimática para la papa.
IAA_POROTO: Índice de aptitud agroclimática para el poroto.
IAA_TOMATE: Índice de aptitud agroclimática para el tomate.
IAAA_TRIGO: Índice de aptitud agroclimática para el trigo.
PRADERA: Índice de aptitud agroclimática para la pradera (solo en secano).
IAA_EUCALIPTO: Índice de aptitud agroclimática para el eucalipto (solo en secano).
PINO: Índice de aptitud agroclimática para el pino (solo en secano).
IPAC_r: Índice de potencial agroclimático integrado del sector o unidad para condición de riego.
IPAC_s: Índice de potencial agroclimático integrado del sector o unidad para condición de secano.

87

Determinación de zonas de similar potencial productivo Silvoagropecuario (ZSPPS)

88
