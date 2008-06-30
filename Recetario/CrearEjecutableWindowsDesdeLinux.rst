= Empaquetando programas de Python para Windows desde Linux =

== La siguiente receta fue hecha utilizando: ==
 * Python 2.5
 * Wine 0.9.25
 * Debian GNU/Linux 4.0 (Etch)

== Ingredientes: ==
 * Una distribución de Linux.
 * Un Wine instalado. 
 * Un archivo de instalación de Python para Windows.
 * Archivos de instalación de las dependencias de su programa, también para Windows.
 * Pyinstaller

== Opcional: ==
 * Inno Setup Compiler http://www.innosetup.com/

== Instalando Python ==

 Para instalar el MSI de Python para Windows se usa:

|| $wine msiexec /i python-2.5.1.msi ||

 Luego instale las dependencias de su programa.

 Por ejemplo, para instalar PyGame:

|| $wine pygame-1.7.1release.win32-py2.5.exe ||

 O doble clic sobre el icono del programa.

 Es importante decirle que python haga los .pyc, cuando sea preguntado por el instalador.

'''Nota''': Aún habiendo hecho lo anterior, puede pasar que cuando se intenta "compilar", aparezca un mensaje que advierte que no se encontró un archivo .pyc, debe buscarse el .py correspondiente.  Y ejecutarlo con:

|| $ cd directorio_del_modulo ||
|| $ wine ~/.wine/drive_c/Python25/python.exe -m modulo.py||

Repita la operación con cada modulo en el que aparezca el error.


 Es importante hacer notar que aunque alguna característica del programa puede NO funcionar en Wine, como por ejemplo pygame, igualmente puede "compilarse" (empaquetarse) correctamente.


== Pyinstaller ==

 Pyinstaller no se instala, como py2exe.  Sin que se descomprime en un directorio.  Se necesita un directorio por cada versión de Python que uno quiera usar con Pyinstaller.

Para configurar Pyinstaller siga las instrucciones del manual.

Lo que no es claro en el manual es como crear los ejecutables.  La explicación es complicada y retorcida, sin embargo es muy sencillo.  Ejecute algo como:

$cd Pyinstaller-1.3
$wine c:\\Python25\\python.exe Makespec.py --noconsole --out=c:\\miproyecto\\PyinstallerDist c:\\miproyecto\\principal.py

Esto crea un archivo principal.spec en el directorio c:\\miproyecto\\PyinstallerDist

El archivo .spec se hace solo una vez, en general no es necesario cambiarlo.

Para automatizar la compilación primero borramos lo que este hecho de antes, esto hace más lento el empaquetamiento, pero evitamos el riesgo de que se empaqueten cosas viejas con las nuevas.  Especialmente si las modificaciones hechas son muy pequeñas.

$ rm ~/.wine/drive_c/miproyecto/PyinstallerDist/buildmiproyecto/*.*
$ rm ~/.wine/drive_c/miproyecto/PyinstallerDist/distmiproyecto/principal.exe

Luego creamos el ejecutable.

$ cd Pyinstaller-1.3
$ wine ~/.wine/drive_c/Python25/python.exe -O Build.py c:\\miproyecto\\PyinstallerDist\\principal.spec

A diferencia de Py2Exe, Pyinstaller no copia automáticamente el archivo w9xpopen.exe así que lo copiamos:

$ cp ~/.wine/drive_c/Python25/w9xpopen.exe ~/.wine/drive_c/miproyecto/PyinstallerDist/distprincipal/

Esto solo es necesario hacerlo una vez.

Inno Setup Compiler crea instaladores para Windows, funciona perfectamente bajo Linux con Wine.  Es una aplicación sumamente fácil de usar, y tiene un asistente muy bueno.  Por lo que no tiene sentido comentarla, sin embargo hay un truco que merece la pena.

Para automatizar la creación del instalador de nuestra aplicación podemos ejecutar:

$ wine ~/.wine/drive_c/Archivos\ de\ programa/Inno\ Setup\ 5/ISCC.exe /Q "c:\miproyecto\iss\principal.iss"

Como se darán cuenta, todas estas instrucciones de linea de comando se pueden colocar en un archivo de Bash, y hacer que todo el proceso de empaquetado quede totalmente automatizado.

#!/bin/bash
rm ~/.wine/drive_c/miproyecto/CDs/NuevasIdeas/*.*

cd Pyinstaller-1.3
rm ~/.wine/drive_c/miproyecto/PyinstallerDist/buildprincipal/*.*
rm ~/.wine/drive_c/miproyecto/PyinstallerDist/distprincipal/principal.exe

wine ~/.wine/drive_c/Python25/python.exe -O Build.py c:\\miproyecto\\PyinstallerDist\\principal.spec

wine ~/.wine/drive_c/Archivos\ de\ programa/Inno\ Setup\ 5/ISCC.exe /Q "c:\miproyecto\iss\NuevasIdeas.iss"

cp ~/.wine/drive_c/miproyecto/principal.py ~/.wine/drive_c/miproyecto/CDs/NuevasIdeas/Linux/bin
cp ~/.wine/drive_c/miproyecto/mimodulo.py ~/.wine/drive_c/miproyecto/CDs/NuevasIdeas/Linux/bin

cd ~/.wine/drive_c/miproyecto/CDs/NuevasIdeas/
tar -cf Linux-NuevasIdeas.tar Linux/
bzip2 Linux-NuevasIdeas.tar
