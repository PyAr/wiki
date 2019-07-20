
Empaquetando programas de Python para Windows desde Linux
=========================================================

La siguiente receta fue hecha utilizando:
-----------------------------------------

* Python 2.5

* Wine 0.9.25

* Debian GNU/Linux 4.0 (Etch) http://www.debian.org/

Ingredientes:
-------------

* Una distribución de Linux http://distrowatch.com/.

* Un Wine instalado http://www.winehq.org/.

* Un archivo de instalación de Python para Windows http://www.python.org/download/.

* Archivos de instalación de las dependencias de su programa, también para Windows.

* Pyinstaller http://pyinstaller.python-hosting.com/

Opcional:
~~~~~~~~~

* Inno Setup Compiler http://www.innosetup.com/

Instalando Python
-----------------

Para instalar el MSI de Python para Windows se usa:

::

   $wine msiexec /i python-2.5.1.msi

Luego instale las dependencias de su programa.

Por ejemplo, para instalar pygame:

::

   $wine pygame-1.7.1release.win32-py2.5.exe

O doble clic sobre el icono del programa.

Es importante decirle que python haga los .pyc, cuando sea preguntado por el instalador.

[Table not converted]

::

   $ cd directorio_del_modulo
   $ wine ~/.wine/drive_c/Python25/python.exe -m modulo.py

Es importante hacer notar que aunque alguna característica del programa puede NO funcionar en Wine, como por ejemplo pygame, igualmente puede "compilarse" (empaquetarse) correctamente.

Pyinstaller
-----------

Pyinstaller no se instala, como py2exe.  Sin que se descomprime en un directorio.  Se necesita un directorio por cada versión de Python que uno quiera usar con Pyinstaller.

Para configurar Pyinstaller siga las instrucciones del manual.

Lo que no es claro en el manual es como crear los ejecutables.  La explicación es complicada y retorcida, sin embargo es muy sencillo.  Ejecute algo como:

::

   $cd Pyinstaller-1.3
   $wine c:\\Python25\\python.exe Makespec.py --noconsole --out=c:\\miproyecto\\Pyinstallerdist c:\\miproyecto\\principal.py

Esto crea un archivo principal.spec en el directorio c:\\miproyecto\\Pyinstallerdist

El archivo .spec se hace solo una vez, en general no es necesario cambiarlo.

Para automatizar la compilación primero borramos lo que este hecho de antes, esto hace más lento el empaquetamiento, pero evitamos el riesgo de que se empaqueten cosas viejas con las nuevas.  Especialmente si las modificaciones hechas son muy pequeñas.

::

   $ rm ~/.wine/drive_c/miproyecto/Pyinstallerdist/buildmiproyecto/*.*
   $ rm ~/.wine/drive_c/miproyecto/Pyinstallerdist/distmiproyecto/principal.exe

Luego creamos el ejecutable.

::

   $ cd Pyinstaller-1.3
   $ wine ~/.wine/drive_c/Python25/python.exe -O Build.py c:\\miproyecto\\Pyinstallerdist\\principal.spec

A diferencia de py2exe, pyinstaller no copia automáticamente el archivo w9xpopen.exe así que lo copiamos:

::

   $ cp ~/.wine/drive_c/Python25/w9xpopen.exe ~/.wine/drive_c/miproyecto/Pyinstallerdist/distprincipal/

Esto solo es necesario hacerlo una vez.

Inno Setup Compiler
-------------------

Inno Setup Compiler crea instaladores para Windows, funciona perfectamente bajo Linux con Wine.  Es una aplicación sumamente fácil de usar, y tiene un asistente muy bueno.  Por lo que no tiene sentido comentarla, sin embargo hay un truco que merece la pena.

Para automatizar la creación del instalador de nuestra aplicación podemos ejecutar:

::

   $ wine ~/.wine/drive_c/Archivos\ de\ programa/Inno\ Setup\ 5/ISCC.exe /Q "c:\miproyecto\iss\principal.iss"

Automátizando la creación del instalador
----------------------------------------

Como se darán cuenta, todas estas instrucciones de linea de comando se pueden colocar en un archivo de Bash, y hacer que todo el proceso de empaquetado quede totalmente automatizado.

::

   rm ~/.wine/drive_c/miproyecto/CDs/Nuevasideas/*.*

   cd Pyinstaller-1.3
   rm ~/.wine/drive_c/miproyecto/Pyinstallerdist/buildprincipal/*.*
   rm ~/.wine/drive_c/miproyecto/Pyinstallerdist/distprincipal/principal.exe

   wine ~/.wine/drive_c/Python25/python.exe -O Build.py c:\\miproyecto\\Pyinstallerdist\\principal.spec

   wine ~/.wine/drive_c/Archivos\ de\ programa/Inno\ Setup\ 5/ISCC.exe /Q "c:\miproyecto\iss\Nuevasideas.iss"

   cp ~/.wine/drive_c/miproyecto/principal.py ~/.wine/drive_c/miproyecto/CDs/Nuevasideas/Linux/bin
   cp ~/.wine/drive_c/miproyecto/mimodulo.py ~/.wine/drive_c/miproyecto/CDs/Nuevasideas/Linux/bin

   cd ~/.wine/drive_c/miproyecto/CDs/Nuevasideas/
   tar -cf Linux-Nuevasideas.tar Linux/
   bzip2 Linux-Nuevasideas.tar

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas
