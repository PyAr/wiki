Entendiendo Decoradores en Python
=================================

Una nota sobre lo que sigue
---------------------------

Lo siguiente no es un artículo propiamente dicho, sino la 
*desgravación* de una charla que fue presentada en forma oral, no
desde un medio de audio, sino de mi memoria!
Espero que al lector le sea de utilidad.

.. image:: imgs/juanjocharla.jpg
   :align: center
   :alt: Ok, la foto no es *exactamente* de mi charla sobre decoradores, pero es de una charla que di ese mismo día :)

Introducción
------------
 
Los siguientes son los tópicos que traté en la charla:


* El principio de todo        
* ¿Qué es un decorador?       
* Funciones decoradoras       
* Decoradores con parámetros  
* Clases decoradores          
* Decorar clases             


Por supuesto, ya que vamos a hablar de decoradores, he aquí una foto
alusiva.

El principio de todo
--------------------

Todo en Python es un objeto                                  
                             
* Identidad                  
* Tipo                       
* Valor                      

Python es un objeto, todo. Los números, strings, listas,
tuplas y otras cosas más raras: los módulos son objetos, el código 
fuente es un objeto. Todo es un objeto. TODO.

Cada objeto tiene 3 características o atributos: identidad, tipo y valor.

Objetos
--------

Veamos algunos ejemplos. El número 1 es un objeto. Usando la 
función built-in ``id`` podemos averiguar su identidad. 
Su tipo es ``int`` y su valor es obviamente 1.

.. code-block:: pycon

    >>> a = 1
    >>> id(a)
    145217376
    >>> a.__add__(2)
    3

Al ser un objeto, podemos aplicarle algunos de sus métodos.
``__add__`` es el método que se llama cuando utilizamos el 
símbolo ``+``.

Otros objetos: 

.. code-block:: python

    [1, 2, 3]   # listas
    5.2         # flotantes
    "hola"      # strings

Funciones
----------

Si todo son objetos, las funciones también son objetos.

.. code-block:: python

    def saludo():
        print "hola"
        
Podemos obtener el id de una función mediante ``id``, acceder
a sus atributos o incluso hace que otro nombre apunte al mismo
objeto función:

.. code-block:: pycon
        
    >>> id(saludo)
    3068236156L
    >>> saludo.__name__
    'saludo'
    >>> dice_hola = saludo
    >>> dice_hola()
    hola

Decorador (definición no estricta)
----------------------------------

Vamos a tomarnos por un momento una libertad y diremos que
un decorador es una *función* **d** que recibe como parámetro 
otra *función* **a** y retorna una nueva *función* **r**.

.. raw:: pdf

  Spacer 0 24
  
* d: función decoradora
* a: función a decorar
* r: función decorada

Podemos aplicar el decorador utilizando una notación funcional:

.. code-block:: python

    a = d(a)

Veamos ahora cómo implementamos un decorador genérico:

Código
-------

.. code-block:: python

    def d(a):
        def r(*args, **kwargs):
            # comportamiento previo a la ejecución de a
            a(*args, **kwargs)
            # comportamiento posterior a la ejecución de a
        return r

Definimos una función **d**, nuestro decorador, y en su cuerpo se define
una nueva función **r**, aquella que vamos a retornar. En el cuerpo de 
**r** ejecuta **a**, la función decorada.

Cambiemos ahora los comentarios por código que haga algo:

Código
--------

.. code-block:: python

    def d(a):
        def r(*args, **kwargs):
            print "Inicio ejecucion de", a.__name__
            a(*args, **kwargs)
            print "Fin ejecucion de", a.__name__
        return r

Cuando ejecutemos una función decorada con el decorador anterior, 
se mostrará un poco de texto, luego se ejecuta la función decorada
y se finaliza con un poco más de texto. Veamos un ejemplo.

En ``suma2`` nos guardamos la versión decorada de ``suma``. Veamos ahora lo que pasa cuando la ejecutamos:

Manipulando funciones
---------------------

.. code-block:: python

    def suma(a, b):
        print a + b

.. code-block:: pycon

    >>> suma(1,2)
    3
    >>> suma2 = d(suma)
    >>> suma2(1,2)
    Inicio ejecucion de suma
    3
    Fin ejecucion de suma
    >>> suma = d(suma)
    >>> suma(1, 2)
    Inicio ejecucion de suma
    3
    Fin ejecucion de suma

Así mismo podemos guardarnos directamente en ``suma`` la versión decorada
de ``suma`` y ahora nunca más a lo largo del programa se tendrá acceso
a la versión original.

La anterior forma de aplicar un decorador es la forma *funcional*.
Tenemos una más linda:

Azúcar sintáctica
-----------------

A partir de Python 2.4 se incorporó la notación con @ para los decoradores de funciones.

.. code-block:: python

    def suma(a, b):
        return a + b
        
    suma = d(suma)
    
.. code-block:: python

    @d
    def suma(a, b):
        return a + b

En la porción de código anterior se pueden ver dos ejemplos en donde
comparamos las formas de aplicar un decorador.

Lo siguiente es ver ejemplos de decoradores *reales*:

Atención
--------

Anti-ejemplo: el decorador malvado.

.. code-block:: python

    def malvado(f):
        return False

.. code-block:: pycon

    >>> @malvado
    ... def algo():
    ...     return 42
    ... 
    >>> algo
    False
    >>> algo()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'bool' object is not callable

Este decorador es tramposo, por que en lugar de devolvernos una
nueva función, nos devuelve un objeto booleano.
Obviamente cuando lo intentamos ejecutar, obtenemos un error.

Siguiente ejemplo:

Decoradores en cadenados
------------------------

Su aplicación es similar al concepto matemático de componer funciones.

.. code-block:: python

    @registrar_uso
    @medir_tiempo_ejecucion
    def mi_funcion(algunos, argumentos):
        # cuerpo de la funcion

Es equivalente a:

.. code-block:: python

    def mi_funcion(algunos, argumentos):
        # cuerpo de la funcion

    mi_funcion = registrar_uso(medir_tiempo_ejecucion(mi_funcion))

Vamos adentrándonos un poco más en los laberintos oscuros Decoradores
los decoradores: <<<< ESTA FRASE NO LA ENTENDI

Decoradores con parámetros
--------------------------

* Permiten tener decoradores más flexibles.
* Ejemplo: un decorador que fuerce el tipo de retorno de una función.

Supongamos que queremos un decorador que convierta a string todas
las respuestas de una función. Se usaría de esta forma:

.. code-block:: python

    @to_string
    def count():
        return 42

.. code-block:: pycon

    >>> count()
    '42'
    
# en la siguiente frase corregi el verbo por que estas saltando de primera plural  persona a segunda singular
¿Cómo se implementaria? Veamos una primera aproximación:

.. code-block:: python

    def to_string(f):
        def inner(*args, **kwargs):
            return str(f(*args, **kwargs))
        return inner

# la palabra "anda" suele sonar antinatural en la lectura segun mi amigo perezreverte
# pero no asi en la charla cotidiana
Esta forma funciona, pero pensemos si podemos hacerlo de una forma más
genérica. La siguiente es la forma de utilizar el decorador ``typer``:

.. code-block:: python

    @typer(str)
    def c():
        return 42
    
    @typer(int)
    def edad():
        return 25.5
    
.. code-block:: pycon
    
    >>> edad()
    25


En realidad, ``typer`` no es un decorador, es una fábrica de decoradores.

.. code-block:: python

    def typer(t):
        def _typer(f):
            def inner(*args, **kwargs):
                r = f(*args, **kwargs)
                return t(r)
            return inner
        return _typer
        
Notemos que ``_typer`` es el verdadero decorador, la función externa
recibe un parámetro ``t`` que es utilizado para definir la naturaleza
del decorador a crear.

Ahora nos vamos un poco más lejos y veremos:

Clases decoradoras
------------------

Caracteristicas:
    * Decoradores con estado.
    * Código mejor organizado.

El primer ejemplo es similar a nuestra primera función decoradoradora:

.. code-block:: python

    class Decorador(object):

        def __init__(self, a):
            self.variable = None
            self.a = a

        def __call__(self, *args, **kwargs):
            # comportamiento previo a la ejecución de a
            self.a(*args, **kwargs)
            # comportamiento posterior a la ejecución de a

#me sonaba mal la oracion indirecta aca
La siguiente ejemplifica como usarlo:

.. code-block:: python

    @Decorador
    def nueva_funcion(algunos, parametros):
        # cuerpo de la funcion

Funcionamiento paso a paso:
    * Se instancia un objeto del tipo ``Decorador`` con ``nueva_función`` como argumento.
    * Cuando llamamos a ``nueva_funcion`` se ejecuta el método ``__call__`` del objeto instanciado.

También podemos aplicarlo, utilizando la vieja notación:

.. code-block:: python

    def nueva_funcion(algunos, parametros):
        # cuerpo de la funcion
    nueva_funcion = Decorador(nueva_funcion)

Con estos ejemplos vistos, podemos hacer una definición más estricta
de decoradores:

Decorador (definición más estricta)
-----------------------------------

Un decorador es una *callable* **d** que recibe como parámetro un *objeto*
**a** y retorna un nuevo objeto **r** (por lo general del mismo tipo que el orginal
o con su misma interfaz).

.. raw:: pdf

  Spacer 0 24
  
* d: objeto de un tipo que defina el método ``__call__``
* a: cualquier objeto
* r: objeto decorado

.. code-block:: python

    a = d(a)

Decorar clases (Python >= 2.6)
------------------------------
A partir de Python 2.6, se permite el uso de la notación con @ antes
de la definición de una clase. Esto da lugar al concepto de decoradores
de clases. Si bien antes de 2.6 se podía decorar una clase (utilizando
la notación funcional), recién con la introducción de este azúcar sintácticase empezó a hablar más de decoradores de clases. 

Un primer ejemplo:

Identidad:

.. code-block:: python

    def identidad(C):
        return C

Retorna la misma clase que estamos decorando.

.. code-block:: pycon

    >>> @identidad
    ... class A(object):
    ...     pass
    ...
    >>> A()
    <__main__.A object at 0xb7d0db2c>

Cambiar totalmente una clase:

.. code-block:: python

    def abuse(C):
        return "hola"

.. code-block:: pycon

    >>> @abuse
    ... class A(object):
    ...     pass
    ...
    >>> A()
    Traceback (most recent call last):
      File "", line 1, in
    TypeError: 'str' object is not callable
    >>> A
    'hola'

Similar a uno de los ejemplos del princpio, el ejemplo nos muestra
que lo que retorne un decorador tiene que tener una interfaz Similar
a la del objeto que estamos decorando, así tiene sentido cambiar el
uso de la versión original del objeto, por una cambiada.

Reemplazar con una nueva clase:
    
.. code-block:: python
    
    def reemplazar_con_X(C):
        class X():
            pass
        return X

.. code-block:: pycon

    >>> @reemplazar_con_X
    ... class MiClase():
    ...     pass
    ...
    >>> MiClase
    <class __main__.X at 0xb78d7cbc>    

En el caso anterior vemos que la clase bue cambiada complemtamente
por una clase totalmente diferente.

Instancia:

.. code-block:: python
    
    def instanciar(C):
        return C()

.. code-block:: pycon

    >>> @instanciar
    ... class MiClase():
    ...     pass
    ...
    >>> MiClase
    <__main__.MiClase instance at 0xb7d0db2c>

Como último ejemplo de decoradores de clase vemos un decorador que
una vez aplicado, instancia la clase y asocia este objeto a su 
nombre. Puede verse como una forma de implementar el patrón
Singleton, estudiado en programación. # cita de singleton a wikipedia

Para terminar:

Dónde encontramos decoradores?
------------------------------

Permisos en Django

.. code-block:: python

    @login_required
    def my_view(request):
        ...

URL routing en Bottle

.. code-block:: python

    @route('/')
    def index():
        return 'Hello World!'

Standard library

.. code-block:: python

    classmethod, staticmethod, property

Muchas gracias!
---------------

.. image:: imgs/mister.jpg
   :scale: 80 %
   :align: center

La charla cerraba agradeciendo al público por su atensión. Aprovecho en esta
ocación para agradecerles a César Portela y a Juan BC por leer el borrador
de esta *desgravación*.

Datos y contacto
----------------

PyConAr 2010 - Córdoba - 15/10/2010

* Comentarios, dudas, sugerencias: jjconti@gmail.com
* Blog: http://www.juanjoconti.com.ar
* Twitter: @jjconti

* http://www.juanjoconti.com.ar/categoria/aprendiendo-python/
* http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/
* http://www.juanjoconti.com.ar/2009/07/16/decoradores-en-python-ii/
* http://www.juanjoconti.com.ar/2009/12/30/decoradores-en-python-iii/
* http://www.juanjoconti.com.ar/2010/08/07/functools-update_wrapper/

* Slides originales de esta charla: http://www.juanjoconti.com.ar/files/charlas/DecoradoresPyConAr2010.pdf

