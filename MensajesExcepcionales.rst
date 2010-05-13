= Mensajes Excepcionales =

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

{{{#!code python
>>> def a:
  File "<input>", line 1
    def a:
         ^
SyntaxError: invalid syntax
}}}

{{{#!code python
>>> a+1=2
  File "<input>", line 1
SyntaxError: can't assign to operator (<input>, line 1)
}}}

{{{#!code python
>>> If a:
  File "<input>", line 1
    If a:
       ^
SyntaxError: invalid syntax
}}}

{{{#!code python
>>> a b
  File "<input>", line 1
    a b
      ^
SyntaxError: invalid syntax
}}}

{{{#!code python
>>> if a
...    print "a es verdadero!"
  File "<input>", line 1
    if a
       
^
SyntaxError: invalid syntax
}}}

=== Errores de Nombres (NameError) ===

{{{#!code python
>>> saludo="Hola"
>>> print Saludo
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'Saludo' is not defined
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

=== Errores de Tipos (TypeError) ===

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
