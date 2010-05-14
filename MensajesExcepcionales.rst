= Mensajes Excepcionales =

  ''"10. Los errores nunca deberían dejarse pasar silenciosamente."'' Zen de Python

Esta página busca ser una guía para las personas que se estén iniciando en este maravilloso lenguaje y se encuentren con errores comunes y no sepan como solucionarlos.

La idea es presentar ejemplos de excepciones, su traducción al español y una posible solución en cada caso.

== ¿Que son las excepciones? ==

Las Excepciones (`Exceptions` en inglés) son condiciones excepcionales que eleva el sistema operativo, el lenguaje, o nuestro mismo programa.

No necesariamente pueden ser un error, también existen advertencias que en general no interrumpen el flujo del programa.

== ¿Que son los tracebacks (trazas de rastreo)? ==

Las trazas de rastreo (`Traceback` en inglés) es la información que reúne el lenguaje para informarnos sobre una excepción que ha ocurrido.

Por ejemplo:

{{{#!code python
Traceback (most recent call last):
  File "form.py", line 78, in <module>
    f = Form("factura.csv")
  File "form.py", line 12, in __init__
    for linea in open(infile).readlines():
IOError: [Errno 2] No such file or directory: 'factura.csv'
}}}

Se traduciría a:
{{{
Traza de rastreo (llamada más reciente a lo último):
  Archivo "form.py", línea 78, en <módulo>
    f = Form("factura.csv")
  Archivo "form.py", línea 12, en __init__
    for linea in open(infile).readlines():
IOError: [Errno 2] No existe el archivo o directorio: 'factura.csv'
}}}

Y nos dice que:
 * Se produjo una excepción del tipo IOError con el mensaje "[Errno 2] No existe el archivo o directorio: 'factura.csv'"
 * El problema surgió en la línea 12 de `form.py` (dentro de la función `__init__`): {{{for linea in open(infile).readlines():}}}
 * Esta función fue llamada desde la línea 78 del mismo archivo (en el módulo, fuera de una función): {{{f = Form("factura.csv")}}} 
 * y así sucesivamente (si tuvieramos más llamadas encadenadas, la lista sería más larga)

En este ejemplo, vemos que le estamos pasando un nombre de archivo que no existe ('factura.csv'), y para corregir el error deberíamos modificar la línea 78.

Aquí es donde se ve la utilidad de las trazas, a veces el error no es culpa de la línea en el que es producido, sino viene arrastrando un dato o condición inválida desde otro punto del programa.

Que el árbol no nos impida ver el bosque ... :-)

== Errores comunes ==


=== Errores de Sangría (IdentationError) ===

   ''"7. La legibilidad cuenta."'' Zen de Python

En Python es fundamental dejar sangría (espacio antes de las instrucciones), que identifica el bloque al que pertenece, ya que no usamos llaves o palabras clave para delimitar los bloques como en otros lenguajes. Si bien esto ayuda a escribir código más prolijo evitando errores de anidación, puede ser raro hasta que uno se acostumbra.

Generalmente, cada vez que abramos un bloque (con una sentencia que termina en : -dos puntos- ), debemos incrementar la sangría. Por ej:

{{{#!code python
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
}}}

Que puede pasar si no lo hacemos...

==== Error de Sangría: se esperaba un bloque con sangría ====

{{{#!code python
>>> if True:
... print "verdad!"
  File "<input>", line 2
    print "verdad!"
        ^
IndentationError: expected an indented block
}}}

Aquí el `print` esta a la misma altura que el `if` (sin sangría), cuando deberíamos haber dejado el espacio correspondiente porque estamos abriendo un nuevo bloque con `:`

==== Error de Sangría: sangría no esperada ====
{{{#!code python
>>> print "hola"
>>>    print "chau"
  File "<input>", line 1
    print "chau"
   ^
IndentationError: unexpected indent
}}}

Aquí el `print "chau"` ''no'' esta a la misma altura que el `print "hola"`, como no abrimos un bloque con `:`, no es necesario dejar espacio para la sangría.

==== Error de Sangría: la nueva sangría no coincide con ningún otro nivel exterior ====
{{{#!code python
>>> def prueba():
...     if False:
...         pass
...   print "..."
  File "<input>", line 4
    print "..."
              
^
IndentationError: unindent does not match any outer indentation level
}}}

Aquí el `print "..."` ''no'' esta a la misma altura que el `if False` ni que el `pass` ni que el `def`, por lo que no se sabe a que bloque pertenece.
Si cerramos el bloque del `if` debería estar a la misma altura que este, y si pertenece al bloque `if`, debería estar dentro de este a la altura del `pass`.
Si el `print` no pertenece a la función, deberíamos ponerlo a la misma altura que el `def`


=== Errores de Sintaxis (SyntaxError) ===

  ''"13. Debería haber una — y preferiblemente sólo una — manera obvia de hacerlo."'' Zen de Python

La sintaxis, como en cualquier lenguaje, es fundamental para que Python entienda lo que estamos queriendole decir, ya que es estricto y se reusará a ejecutar cualquier código que no siga las reglas de sintáxis definidas (que por cierto, no son muchas), a saber:

 * '''Mayúsculas y Minúsculas, identificadores (nombres) y palabras clave''': empiezan con una letra, pueden continuar con letras (a..z o A..Z), dígitos (0..9) o guión bajo (_). Python reconoce la diferencia (es "case sensitive" o sensible a mayúsculas y minúsculas), por lo que {{{Hola}}} y {{{hola}}} son dos identificadores distintos! Se recomienda escribir:
  * Nombres de variable y módulos (archivos) en minúsculas con las palabras separadas por guión bajo ('_'), por ejemplo: {{{mi_variable_x}}}
  * Nombres de clases en CamelCase (primer letra de cada palabra en mayúscula, luego minúsculas, sin separar por espacios), por ejemplo: {{{MiClasePunto}}}
 * '''Palabras clave reservadas''': deben ser escritas tal cual, deben estar al principio de una linea y/o separadas con espacios y no pueden ser usadas como nombres de variables: and as assert break class continue def elif else except exec finally for global if import in is lambda or pass print raise return try with yield. 
   * Sentencias simples {{{assert pass del print return yield raise break continue import global exec}}}: son comprendidos dentro de una línea lógica y varias sentencias simples pueden estar en una sola línea separadas por punto y coma
   * Sentencias compuestas {{{if while for try with def class}}}: contienen (grupos de) otras sentencias; y de alguna manera afectan el control de la ejecución de los mismos. En general, abarcan múltiples líneas.
 * '''Literales''': los valores "constantes" pueden escribirse según su tipo:
  * Cadenas (strings): encerrados por comillas simples o dobles (sin diferencia), ej: {{{"mi cadena"}}} o {{{'mi cadena'}}}
   * Unicode: se identifican con una u antes de la cadena, por ej: {{{u"Mi texto en español"}}}
   * Raw (Crudo): se identifican con una r, son textos sin interpretar los escapes ("\"), por ej: {{{r"c:\config.sys"}}}
   * Con triple comilla simple ({{{'''}}}) o triple comilla doble ({{{"""}}} se encierran textos que se pueden extender varias líneas
  * Números: en general, solo números separados por el punto ("coma decimal"), ej: {{{1234.567}}}
   * Prefijos: se utilizan para diferenciar la base en que está escrito el número:
    * Hexadecimales (base 16): 0x1234
    * Binarios (base 2): 0b01010101 (solo Python 2.6 o superior)
    * Octales (base 8): 0o666 (solo Python 2.6 o superior), 0666 (solo Python 2.6 o inferior)
   * Sufijos: se utlizan para denotar el tipo de número:
    * Largos: 123456789012345678901234567890L (long)
    * Imaginarios: 1234j
   * Notación científica: se indica con una e o E en el medio: {{{1e100}}}, {{{3.14e-10}}} (no confundir con el número irracional, el exponente es en base 10)
 * '''Operadores''':
  * Unarios:  reciben un operando: {{{~ -}}}, por ej la negación: {{{-1}}}
  * Binarios: reciben dos operandos:
   * Aritméticos {{{+ - * ** / // %}}}: para cálculos, por ej: {{{1 + 2}}} (sumar 1 y 2)
   * Relacionales {{{< > <= >= == !=}}}: para comparaciones, por ej: {{{a != b}}} (¿a es diferente de b?)
   * A nivel de bit {{{<< >> & | ^}}}: por ej. {{{5>>6}}} (
 * '''Delimitadores''': determinados caracteres indican determinadas acciones y funcionan como "separadores", cualquier otro uso (o su no utilización) no especificado a continuación generará un error:
  * Paréntesis (): definen tuplas "de elementos": {{{(1,2,3,4)}}} o permiten llamar a una función/crear una clase, {{{mi_funcion(123)}}}
  * Corchetes []: definen listas "de elementos": {{{["uno", "dos", "tres"]}}} o permiten acceder por índice/clave a una colección: {{{mi_lista[posición]}}}
  * Diccionarios {}: definen diccionarios (asociando un valor a una clave) por ej. {{{{'clave':'valor'}}}} o conjuntos
  * Decorador @: aplican una función a una función o clase, por ej {{{@requiere_acceso}}}
  * Coma {{{,}}}: separa expresiones o elementos de una secuencia, por ej: {{{1, 2, 3}}}
  * Dos puntos {{{:}}}: inicia bloques (con o sin sangría), elementos en un diccionario o anotaciones en una función (Python3Mil)
  * Igual {{{=}}}: asigna una expresión a un nombre, por ej. {{{mi_variable=5}}} No confundir con igualdad: {{{a==b}}} También puede usarse la asignación aumentada, combinando un operador, por ej: {{{a+=1}}} (asigna el valor de {{{a+1}}} a {{{a}}})
  * Punto y coma {{{;}}}: separa varias instrucciones en una misma línea, por ej. {{{a=1; b=2; c=a+b}}}. ''Sí, se puede como en C, pero tratar de no usar...''
 * '''Comentarios''': cualquier línea que empieze con numeral (#) es un comentario y será ignorada (independientemente de lo que tiene adentro y si tiene sangría o no)
 * '''Caracteres sin significado''': No usar el signo pesos ($) o el signo de interrogación (?) ya que no se utilizan en Python fuera de las cadenas y producirá un error.

Esperando no haberlo abrumado con el resumen de la sintaxis del lenguaje (los interesados pueden ver la especificación completa en http://docs.python.org/), veamos que pasa si no la respetamos:

==== Error de Sintaxis: sintaxis inválida ====
{{{#!code python
>>> If a>1:
  File "<input>", line 1
    If a>1:
       ^
SyntaxError: invalid syntax
}}}

Python respeta mayúsculas y minusculas, {{{If}}} no es el {{{if}}} que queremos usar.
Tener cuidado sobre todo si venimos de lenguajes que son indiferentes a este tema (por. ej. Visual Basic)

{{{#!code python
>>> secuencia = 1 2
  File "<input>", line 1
    secuencia = 1 2
                  ^
SyntaxError: invalid syntax
}}}

Debemos indicar un operador entre las expresiones o un delimitador entre los elementos. 
En este caso nos falto la coma {{{secuencia = 1, 2}}}

{{{#!code python
>>> if a==1
...    print "a es verdadero!"
  File "<input>", line 1
    if a==1
       
^
SyntaxError: invalid syntax
}}}

Las sentencias compuestas, deben terminar con dos puntos (":") para indicar el nuevo bloque que afectan {{{if a==1:}}}

{{{#!code python
>>> while a=1:
  File "<input>", line 1
    while a=1:
           ^
SyntaxError: invalid syntax
}}}

La asignación no se puede usar en una expresión (comparación), por ej., para evitar los errores clásicos en C {{{while(v=1)...}}} donde nos asignaba {{{1}}} a {{{v}}} en vez de comparar si {{{v}}} era igual a {{{1}}}. En este caso, usar el operador de comparación {{{while a==1:}}}

{{{#!code python
>>> def a:
  File "<input>", line 1
    def a:
         ^
SyntaxError: invalid syntax
}}}

Por más que no tengamos parámetros en nuestra función, los paréntesis son obligatorios. Sería: {{{def a():}}}

==== Error de Sintaxis: FinDeLinea mientras se buscaba una cadena "simple" ====
{{{#!code python
>>> 'abc"
  File "<input>", line 1
    'abc"
        ^
SyntaxError: EOL while scanning single-quoted string
}}}

Las cadenas simples (de una sola línea) deben empezar y terminar en la misma línea y con el mismo caracter, comillas (") o tilde (').

==== Error de Sintaxis: FinDeArchivo mientras se buscaba una cadena de "múltiples líneas" ====

{{{#!code python
>>> """
... mucho 
... texto
...
SyntaxError: EOF while scanning triple-quoted string
}}}

Las cadenas de múltiples líneas, deben empezar con triple comilla o tilde, y terminar con lo mismo. Aquí faltó cerrar la cadena con {{{"""}}}
Nota: el error es simulado, es difícil que suceda en el intérprete, pero si ocurre en un archivo)

==== Error de Sintaxis: no esposible asignar a un operador ====
{{{#!code python
>>> numero+antiguo=1
  File "<input>", line 1
SyntaxError: can't assign to operator (<input>, line 1)}}}

El nombre de la variable es inválido, sería: {{{numero_mas_antiguo=1}}}

=== Errores de Nombres (NameError) ===

  ''"2. Explícito es mejor que implícito."'' Zen de Python

{{{#!code python
>>> saludo="Hola"
>>> print Saludo
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'Saludo' is not defined
}}}


=== Errores de Tipos (TypeError) ===

  ''"12. Cuando te enfrentes a la ambigüedad, rechaza la tentación de adivinar."'' Zen de Python

{{{#!code python
>>> a = 5
>>> b = "10"
>>> a+b
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
}}}

{{{#!code python
>>> fecha = datetime.date('2010','05','10')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: an integer is required
}}}

{{{#!code python
>>> lista = None
>>> for i in lista:
...     pass
...     
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'NoneType' object is not iterable
}}}

{{{#!code python
>>> a (1)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'int' object is not callable
}}}

{{{#!code python
>>> mayor()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: mayor() takes at least 1 argument (0 given)
}}}

{{{#!code python
>>> mayor(5,5,5)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: mayor() takes at most 2 arguments (3 given)
}}}

{{{#!code python
>>> mayor(param3=5)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: mayor() got an unexpected keyword argument 'param3'
}}}

{{{#!code python
>>> mayor(param2=5,3)
  File "<input>", line 1
SyntaxError: non-keyword arg after keyword arg (<input>, line 1)
}}}


=== Errores de Valores (ValueError) ===

{{{#!code python
>>> int("10,50")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '10,50'
}}}

{{{#!code python
>>> float("10,50")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for float(): 10,50
}}}

{{{#!code python
>>> fecha = datetime.date(10,5,2010)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: day is out of range for month
}}}

{{{#!code python
>>> a,b,c = (1,2,3,4)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: too many values to unpack
}}}

{{{#!code python
>>> x,y,z = 1, 2
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: need more than 2 values to unpack
}}}

{{{#!code python
>>> open("C:\xaraza")
ValueError: invalid \x escape
}}}


=== Errores de Atributos (AttributeError) ===

{{{#!code python
>>> fecha = None
>>> fecha.split("/")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'split'
}}}

{{{#!code python
>>> import csv
>>> csv.next()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'module' object has no attribute 'next'
}}}


=== Errores de Clave (KeyError) ===

{{{#!code python
>>> dict = {'clave': 'valor'}
>>> dict['clave2']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'clave2'
}}}

=== Otros Errores ===
{{{#!code python
>>> open("C:\saraza")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'C:\\saraza'
}}}
