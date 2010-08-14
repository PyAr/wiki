Diego Mascialino abrió un [[http://permalink.gmane.org/gmane.org.user-groups.python.argentina/38828|hilo]] en la ListaDeCorreo que reabrió un tema recurrentemente tratado: Cómo difundir el uso de Python (y por extensión del Software Libre) en las universidades, principalmentes en las carreras de ingeniería, ciencias de la computación y afines.

Esta página servirá para sistematizar lo expuesto en ese hilo así como nuevos aportes, tendientes a generar estrategias y materiales de difusión de Python como herramienta para estudiantes y docentes.

== Experiencias ==
=== FCEFyN - Universidad Nacional de Córdoba ===
 * 2010/8/13 Martín Gaitán :
  . (...) Desde el año pasado, impulsado por el Ing. Carlos Bartó, la mayoría de las cátedras de Informática, materia de primer año común a todas las carreras, utilizan Python, en reemplazo de C++ y Octave, siguiendo el libro "Introducción a la programación con Python" que utiliza el entorno PythonG. Según los comentarios de los docentes, los resultados hasta el momento han sido sobresalientes. (...)

== Artículos / Bibliografía ==
 * ''[[http://scholar.google.com.ar/scholar?cluster=4615917205655943662&hl=es&as_sdt=2000|Aprender a programar con Python: una experiencia docente]]'', A Marzal, D Llorense, I Gracia, Universitat Jaume I,
  . Resumen: La elección del primer lenguaje de programación es un debate recurrente entre los docentes universitarios de ingenierías informáticas. La Universitat Jaume I ha optado por una solución poco convencional: en el primer curso de dos titulaciones de ingenier ́ inform ́tica se aprende a programar con Python y C. Python es un lenguaje que está en auge en el mundo del software libre y que presenta una serie de caracter ́ısticas que lo hacen muy atractivo para ense ̃ar a programar. Como material de apoyo hemos escrito un libro de texto (accesible gratuitamente) y desarrollado un sencillo entorno de programaci ́multiplataforma para Python que se distribuye con licencia GPL: el entorno PythonG, formado por un intérprete interactivo, un editor, un depurador sencillo y una ventana con salida gráfica. Con el material docente elaborado se facilita la formación autodidacta para cualquiera que quiera aprender a programar desde cero. En este artículo reflexionamos sobre la idoneidad de Python como primer lenguaje de programación, describimos la experiencia docente de enseñar Python y C en primer curso y presentamos el entorno de progra- maciónn PythonG.

 * [[http://conference.scipy.org/scipy2010/misc/gunnar_ristroph_signals_systems.tar.gz|Signals and Systems in Python]], Gunnar Ristroph, Scipy Conference 2010
  . Abstract: Students will learn the basics of signal processing with examples in Python. Sampling and filtering of data will be covered in the time and frequency domain. Students will learn signal analysis and system simulation techniques.
  http://conference.scipy.org/scipy2010/tutorials.html#signals

 * [[http://www.csdassn.org/software_reports/gnumeric.pdf|Fixing Statistical Errors in Spreadsheet Software: The Cases of Gnumeric and Excel]], B. D. McCullough

 . The open source spreadsheet package "Gnumeric" was such a good clone of Microsoft Excel that it even had errors in its statistical functions similar to those in Excel's statistical functions. When apprised of the errors in v1.0.4, the developers of Gnumeric indicated that they would try to fix the errors. Indeed, Gnumeric v1.1.2, has largely fixed its flaws, while Microsoft has not fixed its errors through many successive versions. Persons who desire to use a spreadsheet package to perform statistical analyses are advised to use Gnumeric rather than Excel.

 . Plantea los errores existentes en las principales herramientas de planilla de cálculo en el ámbito de la estadística.

== Herramientas / Software ==
=== Reemplazo a Matlab (cálculo numérico) ===
 * [[http://numpy.scipy.org/|NumPy]] Genial para cálculo numérico. Introduce un nuevo tipo de datos: Arrays (parecidos al los de C) pero optimizados para cálculos. Permite hacer cálculos de tiras enormes de datos en una sola línea.
=== Reemplazo a Simulink ===
 * [[http://code.google.com/p/sympy/|SymPy]] Librerías para cálculo simbólico. Esta bastante verde todavía, ni se compara con las herramientas comerciales como Mathematica o MathCad, pero para cosas no muy complicadas es de buena ayuda. Si bien funciona en la consola exclusivamente, permite visualizar fórmulas de manera legible, introduciendolas con un sistema similar a LaTEX.
=== Listado de librerías de ploteo ===
 * [[http://matplotlib.sourceforge.net/|matplotlib]]: Muy recomendado. Puede requerir más trabajo que otras librerías más sensilla, pero tiene toda la funcionalidad de graficación que tiene Matlab.
 * [[https://launchpad.net/cairoplot|CairoPlot]]: Bueno, bonito y barato. Permite tener gráficos andando de manera rápida, pero su performance puede ser baja para ciertas aplicaciones.
 * [[http://gnuplot-py.sourceforge.net/|gnuplot.py]]: Wrapper sobre [[http://www.gnuplot.info/|gnuplot]]. Bersatil y rápido, si sos diseñador gráfico, te va a parecer muy feo.

http://stackoverflow.com/questions/1120542/what-is-the-best-plotting-library-for-python

----
CategoryProyectos
