
Root Check
==========

Comprobar si somos o no root y actuar en funcion de eso, ideal medida de seguridad.

* Toda aplicacion que NO requiera privilegios elevados no deberia poder ejecutarse como root.

::

   if os.geteuid()==0: # non-root check
       sys.exit(" ERROR: Do not run as root...\n")
   else:
       print " You are normal user... \n"

Ejemplo:

::

   juan@maverick:~$ /usr/bin/env python test.py

    You are normal user...

   juan@maverick:~$ sudo /usr/bin/env python test.py

    ERROR: Do not run as root...

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas.html
