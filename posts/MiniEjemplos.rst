
Mini Ejem
=========

Esta es una colección de ejemplos cortos que pueden servir para demostrar la potencia del lenguaje. Cada ejemplo consta de un enunciado, seguido de una posible implementación en Python.

Hola mundo
----------

El clásico de clásicos: mostrar *Hola mundo* por pantalla.

::

   >>> print "Hola mundo"
   Hola mundo

Invertir un texto
-----------------

Mostrar un texto invertido (de atrás para adelante)

::

   >>> print "Hola mundo"[::-1]
   odnum aloH

Trabajar con listas
-------------------

Generar una lista de los cubos de los números del 1 al 10

::

   >>> [numero ** 3 for numero in range(1, 11)]
   [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

Generar una lista de los cubos de los números *impares* entre 1 y 10

::

   >>> [numero ** 3 for numero in range(1, 11) if numero % 2 == 1]
   [1, 27, 125, 343, 729]

Funciones
---------

::

   >>> def hola(nombre):
   ...     print u"Hola, %s, ¿cómo estás?" % nombre
   ...
   >>> hola('Mls')
   Hola, Matías, ¿cómo estás?

