
Chequeo de Paquetes con APT
===========================

* Como saber si un paquete esta instalado, o no, y si el mismo existe usando Python, ejemplo interactivo simple.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    import apt
    #
    cache = apt.Cache()
    cache.open()
    program = raw_input(' Cual es el nombre del programa?: ')
    if program in cache:
        if cache[program].is_installed:
            print (' El programa esta instalado!\n')
        else:
            print (' El programa no esta instalado!\n')
    else:
        print (' Estas seguro del Nombre del programa?, el programa no existe!\n')


**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: python
    El programa esta instalado!
   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: monodevelop
    El programa no esta instalado!
   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: hjklsdajflkdshjdskabnv         
    Estas seguro del Nombre del programa?, el programa no existe!
   juan@wind:~$

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

