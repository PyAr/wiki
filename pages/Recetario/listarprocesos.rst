
Listar Procesos
===============

Esta receta muestra una forma de listar procesos en python que soporta múltiples sistemas operativos

En el ejemplo se muestra como listar información sobre los procesos corriendo bajo el usuario "root"

Hace falta instalar la libreria psutil_, disponible en aqui_. Hay paquetes para Debian_ y Ubuntu_, python-psutil.

::

    import psutil

    for pid in psutil.get_pid_list():
        proc = psutil.Process(pid)

        if proc.username != "root":
            continue

        print proc.name, proc.cmdline, proc.pid


En la versión 0.3 de psutil el Ejemplo puede quedar como:

::

    import psutil

    for proc in psutil.get_process_list():
        if proc.username != "root":
            continue
        print proc.name, proc.cmdline, proc.pid


.. ############################################################################

.. _psutil:
.. _aqui: http://code.google.com/p/psutil/

.. _Debian: http://packages.debian.org/python-psutil

.. _Ubuntu: http://packages.ubuntu.com/python-psutil
