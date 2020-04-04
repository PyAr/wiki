.. title: Python 3000 = Py3K = 3.x


Python 3.0 es la última versión del lenguaje, actualmente en desarrollo. Se pueden ver todas las características en el `PEP 3000`_ y derivados.

¿Python 3.0 no es compatible hacia atras con versiones previas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sí, del mismo PEP se lee que "Python 3000 romperá la compatibilidad hacia atrás", pero esto no es tan grave como parece, las modificaciones son menores y tienen mucho menos impacto que los cambios que suceden en otros lenguajes (como por ej. en VB 6.0 a VB.NET como caso extremo, pero tambien en menor medida como sucedió con PHP 5, Perl 6, Java 2, .NET 2.0, etc.)

Por ello, no hay motivo para alarmarse, dejar de usar python o firmar peticiones como pasó con Visual Basic Classic (6.0). La transición, en la mayoría de los casos, va a ser transparente o con cambios mínimos, sin tener que reescribir todo el código (ver más abajo).

Lo que es conveniente es escribir el nuevo código (aún en Python 2.4 o Python 2.5) teniendo en cuenta las modificaciones de Python 3.0, para evitar complicaciones futuras y facilitar la transición automática.

¿Que cambia en Py3K?
~~~~~~~~~~~~~~~~~~~~

Se puede encontrar la lista de cambios en `"Whats New 3.0"`_. En general, son correcciones de desambiguedades y comportamientos duplicados, unificaciones, limpieza de cosas obsoletas y algunas mejoras. A continuación se resumen, agrupados por "afinidad", en un orden arbitrario (el impacto de cada uno dependerá de como uno use el lenguaje):

* La instrucción ``print`` se reemplaza con una función ``print()``

  * Viejo: ``print "La respuesta es", 2*2`` Nuevo: ``print("La respuesta es", 2*2)``

  * Viejo: ``print x,``  Nuevo: ``print(x, end=" ")`` (no saltar a la próxima linea)

  * Viejo: ``print`` Nuevo: ``print()`` (imprimir una línea en blanco)

  * Viejo: ``print >>sys.stderr, "fatal error"`` Nuevo: ``print("fatal error", file=sys.stderr)``

  * Viejo: ``print (x, y)`` Nuevo: ``print((x, y))`` (llamar con una tupla como primer parámetro)

  * Nuevo: ``print("Hay <", 2**32, "> posibilidades!", sep="")`` imprime ``Hay <4294967296> posibilidades!`` (no usar espacio como separador)

* Strings

  * Python 3.0 usa clases ``str`` (strings unicode) y ``bytes`` (datos binarios), en vez de ``unicode`` y ``str`` (strings de 8-bits)

  * Se elimina ``basestring``, ya que se unificó en ``str``

  * Literales para datos binarios, ej. ``b"abc"``, crea una instancia de ``bytes``

  * En los archivos de texto, se obliga a usar una codificación (encoding)

  * Se elimina ``string.letters`` y similares (``string.lowercase`` y ``string.uppercase``). Usar ``string.ascii_letters``

  * UTF-8 es la codificación del código fuente por defecto. Se agrega la posibilidad de tener identificadores con "letras" no ASCII.

  * Nuevo esquema para el formateo de strings: ``"hola {quien}".format(quien="mundo")`` (se mantiene el % estilo C)

* Iterables

  * ``zip()``, ``map()`` y ``filter()`` devuelven iteradores. Un ajuste rápido sería por ej. ``list(map(...))``, pero algo mejor es usar comprehensión de listas (especialmente si se usa ``lambda``).

  * ``builtin.sorted()`` y ``list.sort()`` no aceptan un argumento cmp

  * Se elimina ``__getslice__()`` y similares

  * ``xrange()`` se renombra a ``range()``

  * ``.next()`` se renombra a ``__next__()``, se incorpora un nuevo builtin ``next()`` para llamara al método ``__next__()``

  * Unpacking extendido de iterables. Ahora se puede escribir ``a, b, *rest = some_sequence``

* Diccionarios:

  * ``dict.keys()``, ``dict.items()`` y ``dict.values()`` devuelven vistas en vez de listas (objetos que reflejan el contenido del diccionario). Por ejemplo, esto no funcionará: ``k = d.keys(); k.sort()``. Usar ``k = sorted(d)`` en su lugar.

  * Se eliminan ``dict.iterkeys()``, ``dict.itervalues()`` y ``dict.iteritems()`` (ver anterior)

  * Se elimina ``dict.has_key()``, usar operador ``in`` en su lugar. Ej. ``'x' in dict.keys()`` en vez de ``dict.has_key('x')``

* Enteros:

  * ``1/2`` devuelve un float (la división entera devuelve un float). Usar ``1//2`` para obtener el resultado truncado (entero)

  * ``long`` se renombra a ``int`` (se unifican los enteros)

  * Se remueve ``sys.maxint``. Usar ``sys.maxsize``

  * La ``repr()`` de un entero largo no incluye el prefijo L

* Excepciones:

  * Deben derivar de ``BaseException``

  * Se elimina ``StandardError``

  * Se deben lanzar con un ``raise Exception(args)`` en vez de ``raise Exception, args``

  * Se elimina el comportamiento de sequencias (slicing!) y el atributo ``message`` de las instancias

  * Caputra de excepciones: nueva sintaxis ``except clases as instancia`` en vez de ``except clases, instancia``. La instancia se libera al finalizar el bloque.

  * Encadenado de excepciones (nuevos atributos)

  * Mejoras en los mensajes de error en windows

* Clases y Metaclases

  * Se remueven las clases "clasicas"

  * Se incorpora una nueva sintaxis de metaclases

  * Abstract Base Classes (ABCs); decoradores ``@abstractmethod`` and ``@abstractproperty``; ABCs colecciones y numéricas

  * Decoradores de Clases

  * Nuevo ``super()``. Se puede invocar sin argumentos y la clase correcta será elegida

* Comparaciones

  * Se elimina ``<>`` (usar ``!=``)

  * ``!=`` devuelve lo opuesto de ``==``, salvo que ``==`` devuelva NotImplemented.

  * Los operadores de ordenamiento se comportan diferentes cuando se compara tipos incompatibles (lanza excepción)

* Funciones, argumentos y valores devueltos

  * Se estandariza las anotaciones de los parámetros y resultados de las funciones: ``def dividir(a: int, b: int) -> float:``. Como anotación se puede usar cualquier expresión arbitraria: ``def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):``

  * Argumentos Keyword-only. Se debe incluir el nombre del argumento despues del ``*arg``

  * Instrucción ``nonlocal`` (para usar variables de ambitos exteriores pero no globales)

  * Se elimina el unpacking tuplas en parametros. En vez de ``def foo(a, (b, c)): ....`` usar ``def foo(a, b_c): b, c = b_c``

* Varios

  * Se elimina la comilla invertida (usar ``repr()``)

  * ``as`` y ``with`` son palabras reservadas (keywords)

  * ``True``, ``False``, and ``None`` son palabras reservadas (keywords)

  * ``raw_input()`` se renombra a ``input()``, para el comportamiento anterior de ``input()``, usar ``eval(input())``

  * Literales octales, binarios, ``oct()`` y ``bin()``. En vez de ``0666``, escribir ``0o666``. Ídem binarios

  * Se elimina: ``apply()``, ``callable()``, ``coerce()``, ``execfile()``, ``file()``, ``reduce()``, ``reload()``

  * ``exec()`` is ahora una function.

  * Nuevo representacion de formato punto flotante libre. ``repr(11./5)`` devuelve ``2.2`` en vez de ``2.2000000000000002``

  * Se eliminan ``__oct__()`` and ``__hex__()``. ``oct()`` y ``hex()`` usan ``__index__()``

  * Se elimina soporte para ``__members__`` and ``__methods__``

* Módulos

  * Se elimina el módulo ``cPickle``. Usar ``pickle`` en su lugar. Eventualmente existirá un modulo acelerador transparente.

  * Se eliminan los módulos ``StringIO`` y ``cStringIO``. En su lugar, importar ``io.StringIO`` o ``io.BytesIO`` (ver arriba)

  * Se elimina el módulo ``imageop``

  * Se eliminan los módulos ``audiodev``, ``Bastion``, ``bsddb185``, ``exceptions``, ``linuxaudiodev``, ``md5``, ``MimeWriter``, ``mimify``, ``popen2``, ``rexec``, ``sets``, ``sha``, ``stringold``, ``strop``, ``sunaudiodev``, ``timing``, y ``xmllib``

  * Se elimina el módulo ``new``

  * Se elimina functiones ``os.tmpnam()``, ``os.tempnam()`` y ``os.tmpfile()`` en favor del módulo ``tempfile``

¿Como hacer la transición a Py3K?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para facilitar la transición, Python 2.6 soportará compatibilidad hacia adelante:

* "Modo de Advertencia Py3k", el cual advertirá dinamicamente (en tiempo de ejecución) sobre las características que dejaran de funcionar en Python 3.0.

* Contenerá versiones "backportadas" de las nuevas caracteristicas de Py3K, tanto activadas con ``__future__`` o permitiendo usar la sintaxis nueva o vieja.

Adicionalmente, y en vez de implementar todas las nuevas características en Python 2.6, existe una herramienta de conversión de código fuente (2to3), que ayudará a la traducción automática del código fuente.

Suponiendo que se tengan test de unidades con cobertura aproximadamente completa, el modo recomendado de desarrollo para proyectos que deban soportar tanto Python 2.6 como 3.0 sería:

1. Portar el proyecto a Python 2.6.

#. Activar el modo de advertencia de Py3k

#. Testear y editar hasta que no queden advertencias

#. Usar la herramienta 2to3 para convertir el código fuente a la sintáxis 3.0. No editar manualmente la salida de este programa!

#. Probar el código fuente convertido bajo Python 3.0

#. Si se encuentran problemas, hacer las correcciones en el código fuente de la versión 2.6 y volver al paso 3

#. Al momento de publicar, publicar versiones separadas del proyecto sobre 2.6 y 3.0

¿Es necesario esperar a Python 3.0 para comenzar nuevos proyectos?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Pregunta**:

  > Ahora que estoy leyendo veo que python 3 no es compatible con la versión 2 y hay algunos cambios en la sintaxis. No sería conveniente arrancar con la sintaxis 3 directamente (si bien leo por ahí que esta en versión alfa todavía).

**Respuesta**

No, Python 3.0 es sólo para que el resto del mundo empiece a ponerse a tiro.

Estamos planeando liberar 3.0 final tipo por agosto (el "tipo por" es para asombro de Bob), y es para afirmar APIs y conceptos... la realidad es que Python 3 va a ser tan usable como Python 2 en la versión 3.1.

Asi que, a menos que quieras entrar en producción dentro de dos años, largá con Py2 tranquilo.

Para un ejemplo, elijamos una biblioteca de terceros bien conocida: PIL, que es para tratamiento de imágenes.  Como Python 3 cambia un montón de cosas, el "viejo PIL" no funciona, y tienen que adaptarlo para el nuevo Python.

Entonces, cuando larguemos Py3.0, estamos consolidando las bases y diciendo: "Ok, PIL, esta es la API, fijate y adaptate". Entonces, durante unos meses la gente de PIL se adpata a lo nuevo, y cuando sale Py3.1, vos ya tenés PIL.

Pero en 3.0 no lo tenés. Por eso digo que 3.0 no es para producción, sino para que el resto del mundo (PIL y otras bibliotecas) se pongan a tiro.

(Respuesta de FacundoBatista_ tomada de la Lista)

.. ############################################################################

.. _PEP 3000: http://www.python.org/dev/peps/pep-3000/

.. _"Whats New 3.0": http://docs.python.org/dev/3.0/whatsnew/3.0.html


.. _facundobatista: /miembros/facundobatista

