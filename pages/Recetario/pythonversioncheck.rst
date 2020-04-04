.. title: Python Version Check


Chequear la version de Python, y salir o imprimir error en funcion de eso.

.. code-block:: python

   if sys.hexversion > 0x02060000: # Python version check
       print "\n Python version > 2.6.0\n" # Aca va que hacer si es mayor, continua
   else:
       print "\n ERROR: Python version < 2.6.0\n" # Aca va que hacer si es menor, error

Ejemplo:

.. code-block:: bash

   juan@maverick:~$ /usr/bin/env python test.py

    Python version > 2.6.0


