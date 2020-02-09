
Mensajes Excepcionales
======================

  *"10. Los errores nunca deberían dejarse pasar silenciosamente."* PythonZen_

Esta página busca ser una guía para las personas que se estén iniciando en este maravilloso lenguaje y se encuentren con errores comunes y no sepan como solucionarlos.

La idea es presentar ejemplos de excepciones, su traducción al español y una posible solución en cada caso.

¿Que son las excepciones?
-------------------------

Las Excepciones (``Exceptions`` en inglés) son condiciones excepcionales que eleva el sistema operativo, el lenguaje, o nuestro mismo programa.

No necesariamente pueden ser un error, también existen advertencias que en general no interrumpen el flujo del programa.

¿Que son los tracebacks (trazas de rastreo)?
--------------------------------------------

Las trazas de rastreo (``Traceback`` en inglés) es la información que reúne el lenguaje para informarnos sobre una excepción que ha ocurrido.

Por ejemplo:

::

    Traceback (most recent call last):
      File "form.py", line 78, in <module>
        f = Form("factura.csv")
      File "form.py", line 12, in __init__
        for linea in open(infile).readlines():
    IOError: [Errno 2] No such file or directory: 'factura.csv'


Se traduciría a:

::

   Traza de rastreo (llamada más reciente a lo último):
     Archivo "form.py", línea 78, en <módulo>
       f = Form("factura.csv")
     Archivo "form.py", línea 12, en __init__
       for linea in open(infile).readlines():
   IOError: [Errno 2] No existe el archivo o directorio: 'factura.csv'

Y nos dice que:

* Se produjo una excepción del tipo IOError con el mensaje "[Errno 2] No existe el archivo o directorio: 'factura.csv'"

* El problema surgió en la línea 12 de ``form.py`` (dentro de la función ``__init__``): ``for linea in open(infile).readlines():``

* Esta función fue llamada desde la línea 78 del mismo archivo (en el módulo, fuera de una función): ``f = Form("factura.csv")`` 

* y así sucesivamente (si tuvieramos más llamadas encadenadas, la lista sería más larga)

En este ejemplo, vemos que le estamos pasando un nombre de archivo que no existe ('factura.csv'), y para corregir el error deberíamos modificar la línea 78.

Aquí es donde se ve la utilidad de las trazas, a veces el error no es culpa de la línea en el que es producido, sino viene arrastrando un dato o condición inválida desde otro punto del programa.

Que el árbol no nos impida ver el bosque ... 🙂

Errores comunes
---------------

Errores de Sangría (IdentationError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"7. La legibilidad cuenta."* PythonZen_

En Python es fundamental dejar sangría (espacio antes de las instrucciones), que identifica el bloque al que pertenece, ya que no usamos llaves o palabras clave para delimitar los bloques como en otros lenguajes. Si bien esto ayuda a escribir código más prolijo evitando errores de anidación, puede ser raro hasta que uno se acostumbra.

Generalmente, cada vez que abramos un bloque (con una sentencia que termina en : -dos puntos- ), debemos incrementar la sangría. Por ej:

::

    def mayor(param1, param2=0):
        if param1 is None:
            return "El valor es None=Nulo! :S"
        elif param1>param2:
            print param1,"es mayor a", param2
            return "todo bien :)"
        else:
            print param1,"es menor a", param2
            return "todo mal :("

    print mayor(5)


Que puede pasar si no lo hacemos...

Error de Sangría: se esperaba un bloque con sangría
:::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> if True:
    ... print "verdad!"
      File "<input>", line 2
        print "verdad!"
            ^
    IndentationError: expected an indented block


Aquí el ``print`` esta a la misma altura que el ``if`` (sin sangría), cuando deberíamos haber dejado el espacio correspondiente porque estamos abriendo un nuevo bloque con ``:``

Error de Sangría: sangría no esperada
:::::::::::::::::::::::::::::::::::::

::

    >>> print "hola"
    >>>    print "chau"
      File "<input>", line 1
        print "chau"
       ^
    IndentationError: unexpected indent


Aquí el ``print "chau"`` *no* esta a la misma altura que el ``print "hola"``, como no abrimos un bloque con ``:``, no es necesario dejar espacio para la sangría.

Error de Sangría: la nueva sangría no coincide con ningún otro nivel exterior
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> def prueba():
    ...     if False:
    ...         pass
    ...   print "..."
      File "<input>", line 4
        print "..."

    ^
    IndentationError: unindent does not match any outer indentation level


Aquí el ``print "..."`` *no* esta a la misma altura que el ``if False`` ni que el ``pass`` ni que el ``def``, por lo que no se sabe a que bloque pertenece. Si cerramos el bloque del ``if`` debería estar a la misma altura que este, y si pertenece al bloque ``if``, debería estar dentro de este a la altura del ``pass``. Si el ``print`` no pertenece a la función, deberíamos ponerlo a la misma altura que el ``def``

Errores de Sintaxis (SyntaxError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"13. Debería haber una — y preferiblemente sólo una — manera obvia de hacerlo."* PythonZen_

La sintaxis, como en cualquier lenguaje, es fundamental para que Python entienda lo que estamos queriendole decir, ya que es estricto y se reusará a ejecutar cualquier código que no siga las reglas de sintáxis definidas (que por cierto, no son muchas), a saber:

* **Mayúsculas y Minúsculas, identificadores (nombres) y palabras clave**: empiezan con una letra, pueden continuar con letras (a..z o A..Z), dígitos (0..9) o guión bajo (_). Python reconoce la diferencia (es "case sensitive" o sensible a mayúsculas y minúsculas), por lo que ``Hola`` y ``hola`` son dos identificadores distintos! Se recomienda escribir:

  * Nombres de variable y módulos (archivos) en minúsculas con las palabras separadas por guión bajo ('_'), por ejemplo: ``mi_variable_x``

  * Nombres de clases en CamelCase_ (primer letra de cada palabra en mayúscula, luego minúsculas, sin separar por espacios), por ejemplo: ``MiClasePunto``

* **Palabras clave reservadas**: deben ser escritas tal cual, deben estar al principio de una linea y/o separadas con espacios y no pueden ser usadas como nombres de variables: and as assert break class continue def elif else except exec finally for global if import in is lambda or pass print raise return try with yield. 

  * Sentencias simples ``assert pass del print return yield raise break continue import global exec``: son comprendidos dentro de una línea lógica y varias sentencias simples pueden estar en una sola línea separadas por punto y coma

  * Sentencias compuestas ``if while for try with def class``: contienen (grupos de) otras sentencias; y de alguna manera afectan el control de la ejecución de los mismos. En general, abarcan múltiples líneas.

* **Literales**: los valores "constantes" pueden escribirse según su tipo:

  * Cadenas (strings): encerrados por comillas simples o dobles (sin diferencia), ej: ``"mi cadena"`` o ``'mi cadena'``

    * Unicode: se identifican con una u antes de la cadena, por ej: ``u"Mi texto en español"``

    * Raw (Crudo): se identifican con una r, son textos sin interpretar los escapes ("\"), por ej: ``r"c:\config.sys"``

    * Con triple comilla simple (``'''``) o triple comilla doble (``"""`` se encierran textos que se pueden extender varias líneas

  * Números: en general, solo números separados por el punto ("coma decimal"), ej: ``1234.567``

    * Prefijos: se utilizan para diferenciar la base en que está escrito el número:

      * Hexadecimales (base 16): 0x1234

      * Binarios (base 2): 0b01010101 (solo Python 2.6 o superior)

      * Octales (base 8): 0o666 (solo Python 2.6 o superior), 0666 (solo Python 2.6 o inferior)

    * Sufijos: se utlizan para denotar el tipo de número:

      * Largos: 123456789012345678901234567890L (long)

      * Imaginarios: 1234j

    * Notación científica: se indica con una e o E en el medio: ``1e100``, ``3.14e-10`` (no confundir con el número irracional, el exponente es en base 10)

* **Operadores**:

  * Unarios:  reciben un operando: ``~ -``, por ej la negación: ``-1``

  * Binarios: reciben dos operandos:

    * Aritméticos ``+ - * ** / // %``: para cálculos, por ej: ``1 + 2`` (sumar 1 y 2)

    * Relacionales ``< > <= >= == !=``: para comparaciones, por ej: ``a != b`` (¿a es diferente de b?)

    * A nivel de bit ``<< >> & | ^``: por ej. ``5>>6`` (

* **Delimitadores**: determinados caracteres indican determinadas acciones y funcionan como "separadores", cualquier otro uso (o su no utilización) no especificado a continuación generará un error:

  * Paréntesis (): definen tuplas "de elementos": ``(1,2,3,4)`` o permiten llamar a una función/crear una clase, ``mi_funcion(123)``

  * Corchetes []: definen listas "de elementos": ``["uno", "dos", "tres"]`` o permiten acceder por índice/clave a una colección: ``mi_lista[posición]``

  * Diccionarios {}: definen diccionarios (asociando un valor a una clave) por ej. ``{'clave':'valor'``} o conjuntos

  * Decorador @: aplican una función a una función o clase, por ej ``@requiere_acceso``

  * Coma ``,``: separa expresiones o elementos de una secuencia, por ej: ``1, 2, 3``

  * Dos puntos ``:``: inicia bloques (con o sin sangría), elementos en un diccionario o anotaciones en una función (Python3Mil_)

  * Igual ``=``: asigna una expresión a un nombre, por ej. ``mi_variable=5`` No confundir con igualdad: ``a==b`` También puede usarse la asignación aumentada, combinando un operador, por ej: ``a+=1`` (asigna el valor de ``a+1`` a ``a``)

  * Punto y coma ``;``: separa varias instrucciones en una misma línea, por ej. ``a=1; b=2; c=a+b``. *Sí, se puede como en C, pero tratar de no usar...*

* **Comentarios**: cualquier línea que empieze con numeral (#) es un comentario y será ignorada (independientemente de lo que tiene adentro y si tiene sangría o no)

* **Caracteres sin significado**: No usar el signo pesos ($) o el signo de interrogación (?) ya que no se utilizan en Python fuera de las cadenas y producirá un error.

Esperando no haberlo abrumado con el resumen de la sintaxis del lenguaje (los interesados pueden ver la especificación completa en http://docs.python.org/), veamos que pasa si no la respetamos:

Error de Sintaxis: sintaxis inválida
::::::::::::::::::::::::::::::::::::

::

    >>> If a>1:
      File "<input>", line 1
        If a>1:
           ^
    SyntaxError: invalid syntax


Python respeta mayúsculas y minusculas, ``If`` no es el ``if`` que queremos usar. Tener cuidado sobre todo si venimos de lenguajes que son indiferentes a este tema (por. ej. Visual Basic)

::

    >>> secuencia = 1 2
      File "<input>", line 1
        secuencia = 1 2
                      ^
    SyntaxError: invalid syntax


Debemos indicar un operador entre las expresiones o un delimitador entre los elementos.  En este caso nos falto la coma ``secuencia = 1, 2``

::

    >>> if a==1
    ...    print "a es verdadero!"
      File "<input>", line 1
        if a==1

    ^
    SyntaxError: invalid syntax


Las sentencias compuestas, deben terminar con dos puntos (":") para indicar el nuevo bloque que afectan ``if a==1:``

::

    >>> while a=1:
      File "<input>", line 1
        while a=1:
               ^
    SyntaxError: invalid syntax


La asignación no se puede usar en una expresión (comparación), por ej., para evitar los errores clásicos en C ``while(v=1)...`` donde nos asignaba ``1`` a ``v`` en vez de comparar si ``v`` era igual a ``1``. En este caso, usar el operador de comparación ``while a==1:``

::

    >>> def a:
      File "<input>", line 1
        def a:
             ^
    SyntaxError: invalid syntax


Por más que no tengamos parámetros en nuestra función, los paréntesis son obligatorios. Sería: ``def a():``

Error de Sintaxis: FinDeLinea mientras se buscaba una cadena "simple"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> 'abc"
      File "<input>", line 1
        'abc"
            ^
    SyntaxError: EOL while scanning single-quoted string


Las cadenas simples (de una sola línea) deben empezar y terminar en la misma línea y con el mismo caracter, comillas (") o tilde (').

Error de Sintaxis: FinDeArchivo mientras se buscaba una cadena de "múltiples líneas"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> """
    ... mucho 
    ... texto
    ...
    SyntaxError: EOF while scanning triple-quoted string


Las cadenas de múltiples líneas, deben empezar con triple comilla o tilde, y terminar con lo mismo. Aquí faltó cerrar la cadena con ``"""`` Nota: el error es simulado, es difícil que suceda en el intérprete, pero si ocurre en un archivo)

Error de Sintaxis: no es posible asignar a un operador
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> numero+antiguo=1
      File "<input>", line 1
    SyntaxError: can't assign to operator (<input>, line 1)


El nombre de la variable es inválido, sería: ``numero_mas_antiguo=1``

Error de Sintaxis: "token" inválido
:::::::::::::::::::::::::::::::::::

::

    >>> print 08
      File "<stdin>", line 1
        print 08
               ^
    SyntaxError: invalid token


El compilador de Python es muy estricto, y si no recibe el símbolo/componente léxico correcto ("token") nos emitirá estos errores. En este caso, se debe a que los numeros que comienzan con 0 es un caso especial de notación octal (base 8), por lo que solo acepta números del 0 al 7. Para corregir el error, eliminar el 0 que precede al número ``print 8``

Errores de Nombres (NameError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"2. Explícito es mejor que implícito."* PythonZen_

Si bien Python es dinámico y no tenemos que declarar las variables y funciones al principio de nuestro programa, estas deben existir (estar definidas o "inicializadas") antes de poder usarlas.

O sea, previamente debimos haberle asignado un valor a una variable (con ``=``), definido una función con ``def`` o clase con ``class``. Tener en cuenta que Python justamente es dinámico, y si el interprete no pasa por la linea de la definición, no se define, por más que este el código en el archivo.

En otros lenguajes, si la variable no esta definida, a veces toma un valor arbitrario (nulo, 0 o cadena vacia) o queda declarada sin inicializar (tomando cualquier valor que esté en la memoria), con los consiguientes errores que esto puede ocasionar. Para prevenir esto, en Python es necesario explicitamente definir ("inicializar") la variable con un valor inicial.

Error de Nombre: el nombre 'variable' no está definido
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> saludo="Hola"
    >>> print Saludo
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'Saludo' is not defined


Estamos queriendo usar un nombre (identificador) de algo que no existe. En este caso la variable ``Saludo`` no está inicializada, ya que el nombre de variable correcta es ``saludo`` (notar la diferencia de mayúsculas y minúsculas que comentamos en la sección anterior)

Error de Nombre: el nombre global 'variable' no está definido
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> def mi_func():
    ...     print variable
    ...
    >>> mi_func()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in mi_func
    NameError: global name 'variable' is not defined
    >>>


Similar al anterior, estamos queriendo usar una variable que no definimos previamente (ahora dentro de una función). O definimos la variable globalmente (fuera de la función), o localmente (dentro de la función).

Error de no vinculación local: la variable local 'xxx' fue referenciada antes de asignarla
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> variable = 1
    >>> def mi_func():
    ...     print variable
    ...     variable = variable + 1
    ...
    >>> mi_func()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in mi_func
    UnboundLocalError: local variable 'variable' referenced before assignment


Una variación del anterior, pero en este caso, debemos usar la sentencia ``global variable`` dentro de la función, ya que, sinó, al asignarle un valor dentro de la función, se convierte automáticamente en una variable local, por más que exista globalmente (y da error si la asignación no está al principio de la función antes de usar la variable):

::

    variable = 1
    def mi_func():
        global variable
        print variable
        variable = variable + 1


Errores de Tipos (TypeError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"12. Cuando te enfrentes a la ambigüedad, rechaza la tentación de adivinar."* PythonZen_

Si si, Python es fuertemente tipado, en general no hará mágia con nuestros datos para convertirlos de un tipo a otro, si no se lo pedimos explícitamente.

No como en otros lenguajes, que cambiarían el tipo de una variable silenciosamente dependiendo del contexto (que puede ser ambiguo, por ej. ¿convertir a ``float`` o ``int``?) con el consiguiente arrastre de un error difícil de solucionar.

Error de Tipo: tipo de operando no soportado para +: 'int' y 'str'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> a = 5
    >>> b = "10"
    >>> a+b
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


Típico, en algunos lenguajes esto puede resultar "510" o 15 (dependiendo como entienda el contexto, el órden de los operandos, etc.) ya que hacen una conversión de tipos implícita.

En Python, gentilmente nos avisa que, explicitamente debemos convertir el número a cadena (``str(a)+b`` que resulta en "510") o la cadena en número (``a+int(b) que resulta en 15``.

Error de Tipo: se requiere un entero
::::::::::::::::::::::::::::::::::::

::

    >>> fecha = datetime.date('2010','05','10')
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: an integer is required


Algunas funciones validan los parámetros de entrada, en este caso ``datetime.date`` solicita enteros.  Sería ``datetime.date(int('2010'),int('05'),int('10'))``

Error de Tipo: el objeto 'NoneType' no es iterable
::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> secuencia = None
    >>> for i in secuencia:
    ...     pass
    ...
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'NoneType' object is not iterable


Para iterar (recorrer uno a uno los elementos de una secuencia o colección), por ej. en un ``for``, es necesario que esta sea realmente una secuencia o iterable (tuplas, listas, diccionario, conjunto, etc.)  

Funciones
~~~~~~~~~

Podemos tener errores de tipo o de sintaxis respecto a las funciones, por ejemplo:

Error de Tipo: objeto 'int' no es llamable
::::::::::::::::::::::::::::::::::::::::::

::

    >>> a=1
    >>> a (1)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'int' object is not callable


Estamos queriendo llamar a una variable que tiene un entero, cosa que no se puede (no es una "función llamable"). Seguramente, o la variable no debería haber sido un entero, o en vez de llamarla deberíamos aplicar algún operador o método sobre ella.

Error de Tipo: función() toma al menos un argumento (0 dados)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> mayor()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: mayor() takes at least 1 argument (0 given)


Al definir la función, dijimos que tenía dos parámetros (``param1`` y ``param2=0``). Salvo que el parámetro tenga un valor por defecto (en el caso de param2 es 0), debemos pasarlo al llamar a la función. Revisar...

Error de Tipo: función() toma como mucho 2 argumentos (3 dados)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> mayor(5,5,5)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: mayor() takes at most 2 arguments (3 given)


Similar al anterior, pero le pasamos más parámetros de los que necesita la función.  Revisar...

Error de Tipo: función() tuvo un argumento por nombre inesperado 'paramx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> mayor(param3=5)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: mayor() got an unexpected keyword argument 'param3'


Idem al anterior, tratamos de pasarle un parámetro (esta vez por nombre), que tampoco esta definido en la misma. Revisar....

Error de Sintáxis: argumento por posición luego de argumento por nombre
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> mayor(param2=5,3)
      File "<input>", line 1
    SyntaxError: non-keyword arg after keyword arg (<input>, line 1)


Los parámetros por posición se pasan antes que los parámetros por nombre: ``mayor(3,param2=5)``

Errores de Valores (ValueError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

De manera similar a los errores de tipos, cuando pasemos un dato que no se puede convertir o es inválido, Python nos mostrará estos mensajes:

Error de Valor: literal inválido para int() con base 10: 'xxxx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> int("10ab")
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '10ab'


En este caso '10ab', salvo que las letras sean un error te escritura, estamos intentando convertir un valor hexadecimal (base 16) a entero, sin especificarlo, por lo que intenta base 10 por defecto. Lo correcto sería ``int("10ab",16)``

Igualmente siempre es conveniente capturar este tipo de errores, para validar que el dato a convertir es realmente un número, y sinó, tomar una medida adecuada.

Error de Valor: literal inválido para float() con base 10: 'xxxx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> float("10,50")
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    ValueError: invalid literal for float(): 10,50


Lo mismo que el anterior, pero con la salvedad que para python debemos indicar los decimales con el punto (.) y no la coma (,). Podríamos convertirlo facilmente: ``float("10,50".replace(",",".")``

Error de Valor: el día esta fuera de rango para el mes
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> fecha = datetime.date(10,5,2010)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    ValueError: day is out of range for month


Estamos intentando pasar un valor a la función en el parámetro que no corresponde: ``datetime.date(año, mes, día)`` Sería ``fecha = datetime.date(2010,5,10)``

Error de Valor: demasiados valores para desempaquetar
:::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> a,b,c = (1,2,3,4)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    ValueError: too many values to unpack


En Python, podemos asignar varios elementos a una lista de destinos, pero la cantidad de destinos y de elementos a asignar deben coincidir.  En este caso, ``a=1``, ``b=2``, ``c=3`` y al cuarto elemento ya no hay a que asignarlo.  Podríamos agregar un destino más: ``a,b,c,d = (1,2,3,4)`` o sacar un elemento a asignar de la expresión: ``a,b,c = (1,2,3)``.

Error de Valor: necesita más de 2 valores para desempaquetar
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> x,y,z = 1, 2
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    ValueError: need more than 2 values to unpack


Caso inverso al anterior, nos falta un elemento en la expresión de asignación (o nos sobra un destino). Posible solución: sacamos un destino ``x,y = 1, 2`` o agregamos un elemento: ``x,y,< = 1, 2 ,3``

Error de Valor: caracter de escape \x inválido
::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> open("C:\xaraza.txt")
    ValueError: invalid \x escape


En los strings (cadenas), ciertos caracteres tienen un significado especial. Es el caso de la barra invertida ("\"), que identifica que lo que sigue definie un caractér especial ("\n" para el salto de linea, "\xfe" para el caracter cuyo código hexadecimal es FE, etc.) Si queremos una barra invertida (por ejemplo, en un directorio de windows), debemos usar strings crudos (raws): r"C:\xaraza.txt" o doble barra invertida: "C:\\xaraza.txt"

Errores de Atributos (AttributeError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Practicamente todo en Python es un objeto, y estos objetos tienen métodos y "propiedades" (ambos denominados atributos). Si intentamos acceder a un atributo que no pertenece al objeto, se producirá uno de los siguientes errores:

Error de Atributo: el objeto 'NoneType' no tiene el atributo 'split'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> fecha = None
    >>> fecha.split("/")
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'split'


En este caso estamos queriendo invocar a un método ``split`` que no esta definido para este tipo de objeto (aquí ``None``, pero podría ser cualquier otro). Seguramente la variable fecha debería ser otra cosa, o nos equivocamos de método a invocar.

Error de Atributo: el objeto 'modulo' no tiene el atributo 'next'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> import csv
    >>> csv.next()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'next'


Similar al anterior, pero en este caso estamos importando un módulo ``csv`` que no tiene la función ``next``}. En este caso particular, ``next`` es un método de la instancia de ``csv_reader``, no del módulo.

Errores de Índice (IndexError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error de Índice: el índice de lista esta fuera de rango
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> l=[1,2,3]
    >>> l[3]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range


En este caso, la lista tiene 3 elementos, y se acceden desde la posición 0 hasta la 3 (como en C), lo correcto sería ``l[2]`` para el tercer elemento.

Errores de Clave (KeyError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los diccionarios se acceden por clave asociativa, si la clave no existe, se producirá un error:

::

    >>> dict = {'clave': 'valor'}
    >>> dict['clave2']
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    KeyError: 'clave2'


En este caso, podríamos acceder al valor de correcto usando ``dict['clave']`` que sí existe, o pedir ``dict.get('clave2')`` que si la clave no existe, devolverá ``None`` y no producirá una excepción.

Otros Errores
~~~~~~~~~~~~~

Los errores del sistema operativo y bibliotecas relacionadas también se expresan como excepciones:

IOError: [Errno 2] No existe el archivo o directorio: 'C:\\saraza'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> open("C:\saraza")
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    IOError: [Errno 2] No such file or directory: 'C:\\saraza'


El archivo solicitado no existe, si queremos crearlo deberíamos pasarle un segundo parámetro que lo especifique: ``open("saraza","a")`` o ``open("saraza","w")``

Advertencias
~~~~~~~~~~~~

Como comentabamos, hay Excepciones que no son errores, sino advertencias.  Se usan para avisarnos sobre algún cambio en el lenguaje o código potencialmente incorrecto o perjudicial:

Advertencia de "Deprecación": el módulo md5 esta desaconsejado; use en su lugar haslib
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

    >>> import md5
    __main__:1: DeprecationWarning: the md5 module is deprecated; use hashlib instead


En esta versión de Python, el módulo md5 existe por compatibilidad hacia atrás.  En versiones posteriores podría no existir más. Se recomienda revisar la recomendación que nos da Python: el módulo hashlib.

.. ############################################################################




.. _pythonzen: /pages/pythonzen/index.html
.. _python3mil: /pages/python3mil/index.html
