= Comparación de Rendimiento entre Python, Java y .Net =

== Mito: ==
''Python es pesado''

== Hechos: ==

Comparando los instaladores de los entornos de desarrollo:
 * Python 2.5.1 installer windows: 10MB  
 * Java EE SDK 5: 124.25MB
 * Net Framework 2.0 SDK: 354MB 
 
Habría que ver bien que funionalidad trae cada uno, pero tomando muy por arriba, nos da una idea que el codigo python es mucho mas compacto, considerando que en 354MB entra mucha mas "complejidad" que en 10MB (codigo, documentación, herramientas, etc.).

Comparando los lenguajes:
 * Python es casi 3 veces mas compacto que Java, 6 veces mas que C. O sea, en C tenemos 6 lineas cuando en python 1 sola.
 * Python carga 6 veces mas rápido que Java cuando inicia
 * Python consume 4 veces menos memoria que java 
 * Python tiene extensiones en C/C++ que son más rápidas que código nativo java, por mas que java tenga un compilador jit 
 * Python es bastante mas lento que java si medimos los tiempos de ejecución de programas de uso intensivo de procesador. Igualmente, si se usan extensiones en  C para el "procesamiento intensivo", python es más rápido que java. 

== Resumen: ==
En resumen basandonos en las comparaciones anteriores:
 * Para aplicaciones interactivas que no tienen uso intensivo de procesador, que conectan la base de datos con la interfaz gráfica por decirlo asi, la "ventaja" de velocidad de lenguajes estaticos compilados es despreciable (el 99% del tiempo el código va a estar idle esperando por la db o la gui)
 * Para aplicaciones matematicas, o lo que sea que necesite procesamiento intensivo, siempre existen en python extenciones en C/C++ para acelerar las cosas, teniendo lo mejor de los dos mundos: velocidad de C/C++ y flexibilidad de Python
 * Para aplicaciones de sistema (system programing), una base de datos, un sistema operativo, etc., C o C++

''Nota'': Se puede estimar que .Net estaría a la altura de Java respecto al rendimiento, cosa que no se puede comprobar ya que .Net no corre en linux que es el sistema desde donde se efecturon las mediciones (ver fuentes)

== Observaciones: ==
Si tomaramos el rendimiento de un programador sólo en funcion de las lineas de código que produce (y estas serían constantes e intercambiables entre los distintos programadores, o sea, que todos los programadores rindieramos igual), se podría decir que un programador de python equivale a 3 programadores de java, o lo que es lo mismo, que un programador de python realiza su trabajo en 3 veces menos el tiempo. :)

== Fuentes: ==
 * [[http://en.wikipedia.org/wiki/Comparison_of_programming_languages|Comparaciones de los Lenguajes de Programación en Wikipedia]]
 * [[http://shootout.alioth.debian.org/gp4/benchmark.php?test=all&lang=all|Mediciones de Rendimiento de los lenguajes de programación (en alioth.debian.org)]]


= Análisis "en perspectiva" de comparaciones de rendimiento =

Analizando una comparativa de 9 lenguajes de programación / formas de compilación [[#1]], en el cuadro de la página 3 encontramos un resumen (no muy favorable) y un gráfico donde directamente se excluyo Python por el bajo desempeño en algunas de las pruebas.

Sin embargo, debemos ver estos datos en perspectiva, como se hace notar en el wiki de Python [[#3]].  Uno debe tener en cuenta si los puntos flacos del interprete afectan el desempeño de la propia aplicación.

Al mismo tiempo, en el sitio oficial de Python ([[#2]] y [[#3]]) se dan ejemplos de código y consejos para mejorar el desempeño.

Volviendo a la tabla comparativa de desempeño del articulo [[#1]], vemos que el desempeño de python en grandes operaciones matemáticas dista de ser el mejor (sea con enteros, punto flotante, punto flotante de doble precisión y trigonométricas). Para mejorarlo podemos usar Pyrex, que es un Python que se compila (aunque con limitaciones en la cantidad de módulos disponibles).  Pero su velocidad es casi tan buena como la de C++ puro y mayor que MatLab u Octave [[#4]].

Ahora bien, si nuestro punto critico no son los cálculos matemáticos, sino la velocidad de Entrada/Salida (I/O), vemos que en estos benchmarks la velocidad de Python es apenas menor que Visual C++, o incluso igual cuando se usa Psyco.



== Referencias ==
 1. <<Anchor(1)>> [[http://www.osnews.com/story/5602/Nine_Language_Performance_Round-up:_Benchmarking_Math_&_File_I_O/page3/|Comparación entre nueve lenguajes]]
 2. <<Anchor(3)>> [[http://wiki.python.org/moin/PythonSpeed|Cuestiones de Rendimiento (python.org)]]
 3. <<Anchor(4)>> [[http://wiki.python.org/moin/PythonSpeed/PerformanceTips|Tips para mejorar la Rendimiento de python (python.org)]]
 4. <<Anchor(6)>> [[http://scipy.org/PerformancePython|Rendimiento en python sobre operaciones matemáticas]]
