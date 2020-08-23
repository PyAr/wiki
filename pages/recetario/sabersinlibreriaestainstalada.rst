.. title: Saber si N libreria esta instalada


Cómo saber si N librería está instalada SIN ingresar al intérprete de Python. Funciona en la Bash de Linux.

.. code-block:: bash

   python -c 'import libreria'&&echo OK

Ejemplo:

.. code-block:: bash

   juan@maverick:~$ python -c 'import gtk'&&echo OK
   OK
   juan@maverick:~$ python -c 'import libreriaquenoestainstalada'&&echo OK
   Traceback (most recent call last):
     File "<string>", line 1, in <module>
   ImportError: No module named libreriaquenoestainstalada
   juan@maverick:~$

