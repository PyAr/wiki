
Esta página es una ayuda a los programadores que vienen del mundo "visual" (VB clásico versiones 5.0 y 6.0)

VB.NET es otro lenguaje, por lo que esta comparación no se adecua (buscar Python vs .Net)

Diferencias entre Python y VB
-----------------------------

Tipado
~~~~~~

* Python es fuertemente tipado, VB no. En VB se puede hacer 1 +"2" = 3, en python hay que convertir explicitamente los tipos: 1 + int("2") = 3 (esto evita errores del tipo "1" + "1" + 2 que en VB da 13 en vez de 4 o "112"). Para los tipos similares (ej enteros y flotantes) no hace falta conversión (ni en Python ni en VB). Adicionalmente, en python se puede modificar el comportamiento de las operaciones aritmeticas y booleanas dependiendo del tipo del los objetos involucrados.

* Python es tipado dinámicamente, VB depende de la declaración de la variable (en python todas las variables equivalen al tipo ``Variant`` de VB, o sea, pueden adquirir cualquier tipo de datos). En VB no se puede cambiar el tipo de la variable en tiempo de ejecución si no son ``Variant`` (no se puede asignar un flotante a un entero), en Python no existe esta restricción.

* En Python no se puede utilizar variables indefinidas o sin inicializar, en VB si (mas allá de la instrucción ``Option Explicit`` que solo obliga a definir las variables, no a inicializarlas). En VB, a las variables sin inicializar se les asigna un valor implícito en el "aire" dependiendo del contexto (0, "", etc.), lo que permite usar variables inexistentes con valores indefinidos (una de las causas del célebre error "No coinciden los tipos"). 

* En Python no se define el tipo de la variable (ver tipado dinámico), solo basta con inicializar su valor (o None si no lo tiene). En VB en general es necesario hacer dos pasos, definir el tipo (``Dim var As tipo``) e inicializar la variable (salvo que el valor inicial sea el predeterminado que se le asigna implicitamente según el tipo, ej. enteros = 0). En general, se define el tipo para inicializarla con el valor predeterminado (para evitar el problema del punto anterior), perdiendo el dinamismo del lenguaje.

Tipos de datos
~~~~~~~~~~~~~~

* Python soporta nativamente cadenas (``string``/``unicode`` equivalente a ``String`` en VB), enteros (``int``/``long`` equivalentes a ``Byte``/``Integer``/``Long`` de VB), números de punto flotante (``float`` equivalentes a Single/Double de VB), booleanos (``bool`` True y False ídem que en VB). Tambien en la librería estandar se encuentra los tipos ``datetime`` para fechas (``Date``/``Time`` en VB), y ``Decimal`` para numeros con presición fija (similar a ``Currency`` en VB)

* En Python hay un solo tipo de objeto nulo: ``None``. En VB existe ``Nothing`` para objetos por referencia (mutables), ``Null`` para valores nulos (dentro de variables sin tipo), ``Empty`` para variables no definidas (no son posibles en Python), ``Missing`` para parámetros opcionales no pasados a la función. En Python cualquier variable puede se nula, en VB solo las variables sin tipo (causa del célebre error "Uso de null no válido").

* VB soporta colecciones (``Collection``) similares a los diccionarios (``dict``) de Python. En comparación, los diccionarios son más poderosos, tienen un método para ver si una clave esta definida (en VB la única forma de saberlo es tratar de obtener dicha clave y ver si se producía un error), se pueden recorrer sus claves (en VB solo es posible recorrer sus valores: ``For Each val in coleccion``). En VB se pueden usar colecciones sin clave, que serían el equivalente a las Listas (``list``) de Python. En VB, las claves deben ser cadenas, ya que si se utiliza números enteros se accede por posición. En Python no se puede acceder directamente por posición en los diccionarios (habría que obtener una lista de los valores) y las claves pueden ser cualquier valor inmutable (cadenas, enteros, etc.)

* Python no soporta arreglos o vectores nativamente. En VB los vectores o arreglos de longitud fija o variable serían el equivalente a las listas de Python, los cuales pueden ser redimensionados (preservando su valor o no, ``Redim Preserve arreglo()``). Los arreglos de VB solo se pueden recorrer por posición (en Python por posición ``lista[pos]`` y por comprension ``for elem in lista``) y no se puede "recortar" facilmente un subconjunto de elementos (en Python: ``lista[pos_inicial:pos_final]``). En vez de listas tambien se pueden utilizar arreglos con el módulo ``array``.

* En Python no existen Constantes (``Const`` en VB). Simplemente se definen como variables globales.

Funciones y Subrutinas
~~~~~~~~~~~~~~~~~~~~~~

* En Python no hay diferencia entre funciones y subrutinas (estas últimas en VB no devuelven resultado) y es obligatorio el uso de paréntesis para las llamadas, aunque no tenga parámetros o no se use el resultado devuelto (siempre devuelven un valor aunque no se lo utilize, si no se especifica devuelven None). 

* En Python los parámetros se pueden pasar por nombre y/o por posición, y los parametros optativos (por nombre) directamente no se pasan ni se dejan en blanco.

* Python no soporta variables estáticas (variables definidas dentro del contexto de una función, cuyo valor perdura entre los distintos llamados), pero si soporta generadores (donde se puede ir devolviendo resultado sin salir de la función, preservando los valores de las variables locales). Tambien se podría utilizar parametros opcionales mutables (ej. listas), que persisten entre llamados a la misma función.

Orientación a Objetos
~~~~~~~~~~~~~~~~~~~~~

* Si bien ambos son lenguajes multiparadigma, en python se puede programar funcionalmente además del modo procedural y orientado a objetos, con muy buenas herramientas de introspección y metaprogramación.

* Python soporta herencia (múltiple), constructores con parámetros, metodos de clase y estáticos, por lo que es un lenguaje más amigable desde el punto de vista de Orientación a Objetos. Las variables y métodos privados en python son semi-publicos, y python no soporta interfaces (aunque se pueden emular). Ambos soportan metodos y variables de instancia y propiedades. 

* Python no soporta atributos/propiedades por defecto. En VB, si no se especifica atributo, en general hay uno por defecto. Ej. ``col('hola')`` en una colección en realidad esta accediendo al método Item: ``col.Item('hola')``. Esto es similar a la sintaxis de Python para los diccionarios: ``dic['hola']`` es similar a ``dic.__getitem__('hola')``, pero en VB tiene un uso implicito mucho mas extendido.

Referencias
~~~~~~~~~~~

* Python no distingue entre manejo por referencia y por valor, pero si entre tipos mutables e inmutables. Los tipos mutables (listas, diccionarios y objetos del usuario) se utilizan siempre por "referencia". Los tipos inmutables (enteros, flotantes, cadenas) se utilizan siempre por "valor". 

* En Python, los tipos mutables (por "referencia") se asignan de la misma manera que los tipos inmutables (por "valor"). No hay una distinción explícita como en VB donde es necesario utilizar la instrucción ``Set variable = valor``, ni en los argumentos con los modificadores ``ByValue`` y ``ByRef``.

Módulos y Alcances
~~~~~~~~~~~~~~~~~~

* En Python no hay distinción entre archivos fuente de formularios, módulos, módulos de clase, etc. (todos reciben el nombre de módulo) y tampoco existe la restricción de una clase por módulo (como en los formularios y módulos de clase de VB).

* En Python tampoco se distingue entre Referencias y Componentes, manejando estas características como módulos y clases que se deben importar para poder utilizarlos.

* En Python si bien existen los alcances Globales y Locales, el global solo es para el módulo en el que se esta trabajando (debiendo importar explícitamente los nombres a utilizar de otros módulos). Esto es similar a ``modulo.variable`` de VB, pero los módulos no se importan ni crean automágicamente.

* En Python, en general, para modificar variables globales dentro de una función, se debe declarar la variable como global (instrucción ``global``), de lo contrario se crea una variable local (aunque la variable global exista).

Sintaxis
~~~~~~~~

* En Python la identación es obligatoria para definir los bloques, en VB es opcional y no define los bloques.

* Python no utiliza delimitadores de bloque: ni llaves ni palabras claves (``End For``, ``End If``, etc. de VB). 

* En Python para separar varias instrucciones se puede utilizar el punto y coma (dos puntos en VB). Este no delimita el final de la linea, ya que solo se puede hacer una instrucción multilinea terminando la linea que continua con una \ (guion bajo en VB) salvo excepciones (textos multiples lineas con ``"""`` o cuando se abre un paréntesis)

* Python no soporta la instrución de "comparación múltiple" (``Select`` en VB), se pueden utilizar varios ``if`` o un dicionario.

* Python no soporta ciclos "repetitivos" de manera directa (``For i = 1 To 10 Step 2`` en VB), siempre se debe recorrer listas (``for i in xrange(1,10,2)`` en Python).

* Python tiene solo una forma de ciclos condicionales (``while``), y se evalua siempre al comienzo del ciclo (similar al ``Do While condición`` de VB, pero ``While`` no se soporta al final del ciclo.)

* Python es sensible a mayúsculas y minúsculas, VB no (para bien o para mal...). Igualmente, VB "corrige" mayúsculas y minúsculas a medida que se escribe (esto es útil para ver si está definida la variable o no, pero tambien trae problemas si se redefinia la variable en otro contexto, cambia el nombre en el resto de los módulos). En Python, hay que escribir bien desde el principio el nombre de la variable.

Entorno de desarrollo integrado (IDE) y Migración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* En Python, no existe "Él" entorno de desarrollo integrado (Editor de Código y de Pantallas, Compilador, Depurador, etc.). Hay varias herramientas, que pueden llegar a usarse en conjunto (por ej. StaniPythonEditor_ es un editor + wxGlade para diseñar pantallas + WinPdb_ para depurar + PyChecker_ para verificar el código, etc.). Ver SPE, Boa, etc.

* Para el desarrollo rápido y simple, lo más parecido es PythonCard_, que incluye un diseñandor de pantallas y editor de código muy similar a VB, y el manejo de componentes es muy simple.

* Existe una herramienta para migrar código VB a Python: vb2py_, migra proyectos simples con relativa facilidad, y puede ser usada como referencia para ver la conversión entre el código de ambos lenguajes, documentado en la guía del usuario.

.. ############################################################################





.. _vb2py: http://vb2py.sourceforge.net/

.. _pythoncard: /pages/pythoncard.html
