= Comparación de Rendimiento entre Python, Java y .Net =

== Mito: ==
''Python es pesado''

== Hechos*: ==

Comparando los instaladores de los entornos de desarrollo:
 * Python 2.5.1 installer windows: 10MB  
 * Java EE SDK 5: 124.25MB
 * Net Framework 2.0 SDK: 354MB 
 
Habría que ver bien que funionalidad trae cada uno, pero tomando muy por arriba, nos da una idea que el codigo python es mucho mas compacto, considerando que en 354MB entra mucha mas "complejidad" que en 10MB (codigo, documentación, herramientas, etc.).

Comparando los lenguajes:
 * Python es casi 3 veces mas compacto que Java, 6 veces mas que C. O sea, en C tenemos 6 lineas cuando en python 1 sola. ** 
 * Python carga 6 veces mas rápido que Java cuando inicia
 * Python consume 4 veces menos memoria que java 
 * Python tiene extensiones en C/C++ que son más rápidas que código nativo java, por mas que java tenga un compilador jit 
 * Python es bastante mas lento que java si medimos los tiempos de ejecución de programas de uso intensivo de procesador. Igualmente, si se usan extensiones en  C para el "procesamiento intensivo", python es más rápido que java. 

== Resumen ==
En resumen basandonos en las comparaciones anteriores:
 * Para aplicaciones interactivas que no tienen uso intensivo de procesador, que conectan la base de datos con la interfaz gráfica por decirlo asi, la "ventaja" de velocidad de lenguajes estaticos compilados es despreciable (el 99% del tiempo el código va a estar idle esperando por la db o la gui)
 * Para aplicaciones matematicas, o lo que sea que necesite procesamiento intensivo, siempre existen en python extenciones en C/C++ para acelerar las cosas, teniendo lo mejor de los dos mundos: velocidad de C/C++ y flexibilidad de Python
 * Para aplicaciones de sistema (system programing), una base de datos, un sistema operativo, etc., C o C++

''Nota'': Se puede estimar que .Net estaría a la altura de Java respecto al rendimiento, cosa que no se puede comprobar ya que .Net no corre en linux que es el sistema desde donde se efecturon las mediciones (ver fuentes)

== **Observaciones ==
Si tomaramos el rendimiento de un programador sólo en funcion de las lineas de código que produce (y estas serían constantes e intercambiables entre los distintos programadores), se podría decir que un programador de python equivale a 3 programadores de java, o lo que es lo mismo, que un programador de python realiza su trabajo en 3 veces menos el tiempo. :)

== * Fuentes: ==
 * [http://en.wikipedia.org/wiki/Comparison_of_programming_languages Comparaciones de los Lenguajes de Programación en Wikipedia]
 * [http://shootout.alioth.debian.org/gp4/benchmark.php?test=all&lang=python&lang2= Mediciones de Rendimiento de los lenguajes de programación (en alioth.debian.org)]
