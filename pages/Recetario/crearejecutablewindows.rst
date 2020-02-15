
Empaquetando programas de Python para Windows
---------------------------------------------

Descripción
:::::::::::

En esta receta se muestra como:

* Crear un ejecutable (.EXE) nativo para windows (que no requiera tener Python instalado)

* Generar un archivo autoextraible similar a un instalador (pero más simple)

Ver adjuntos:

* : aplicación de ejemplo

* : script de "compilación" para py2exe

* : instalador autoextraible producido con esta receta

Requerimientos:
:::::::::::::::

* `Python 2.5`_

* `Py2Exe 0.6`_

* 7-Zip_ (opcional, para crear el archivo autoextraible)

Ejemplo
:::::::

Como ejemplo tomamos una aplicación simple *hola.py*:

::

    # -*- coding: iso-8859-1 -*-

    print "hola mundo"


"Compilando" Python con Py2Exe
::::::::::::::::::::::::::::::

Py2Exe_ empaqueta los archivos necesarios para ejecutar la aplicación sin necesitad de instalar Python ni sus dependencias.

Para crear el ejecutable es necesario crear un script de setup que extiende las utilidades de distribución de python (DistUtils_), *setup.py*:

::

    from distutils.core import setup
    import py2exe

    setup(console=['hola.py'])


Luego en la carpeta de la aplicación, por línea de comandos, ejecutamos este script:

::

   python setup.py py2exe

Con lo que se generará una carpeta *dist* con los siguientes archivos:

* *hola.exe*: ejecutable

* *python25.dll*: runtime de python

* *library.zip*: librerias empaquetadas

* y varios archivos más dependiendo de la versión y dependencias instaladas

Este directorio se puede comprimir en un zip y enviar, ya que es todo lo que se necesita para ejecutar la aplicación.

**Nota**: ver la salida de Py2Exe_ ya que algunas librerias del sistema operativo no pueden ser distribuidas y deben estar instaladas en la máquina destino.

Creando un instalador simple con 7-Zip
::::::::::::::::::::::::::::::::::::::

Con 7-zip se puede crear un único archivo comprimido autoextraible (ejecutable), con una muy buena tasa de compresión y de manera muy simple.

Para ello, ejecutar 7-Zip en la linea de comandos sobre la carpeta de la aplicación:

::

   7z.exe a -sfx setup.exe dist

Con esto nos creará un archivo *setup.exe* que al ejecutarlo descomprimirá automáticamente la carpeta de nuestra aplicación. Este archivo contiene todo lo necesario para ejecutar la aplicación.

Este ejemplo usa la línea de comando, pero también se puede usar la interfase visual integrada al explorador de windows de 7-Zip (click derecho sobre la carpeta *dist*, en el menú contextual elejir 7-zip, añadir al archivo, y tildar opción "Crear archivo SFX")

Con 7- Zip también es posible:

* Agregar un autoextractor gráfico (ventana más amigable)

* Modificar los mensajes y solicitar confirmación para extraer los archivos (mediante archivos de configuración)

* Ejecutar un programa luego de extraer los archivos

* Ejecutar un instalador propio (pero tiene que estar hecho en C)

* etc.

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Python 2.5: http://www.python.org/download/

.. _Py2Exe 0.6: http://www.py2exe.org/

.. _7-Zip: http://www.7-zip.org/

.. _py2exe: /py2exe
.. _distutils: /distutils
.. _marianoreingart: /marianoreingart
.. _categoryrecetas: /categoryrecetas
