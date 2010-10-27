= Listar Procesos =

Esta receta muestra una forma de listar procesos en python que soporta múltiples sistemas operativos

En el ejemplo se muestra como listar información sobre los procesos corriendo bajo el usuario "root"

Hace falta instalar la libreria [[http://code.google.com/p/psutil/|psutil]], disponible en [[http://code.google.com/p/psutil/|aqui]]. Hay paquetes para [[http://packages.debian.org/python-psutil|Debian]] y [[http://packages.ubuntu.com/python-psutil|Ubuntu]], python-psutil.

{{{
#!code python
import psutil

for pid in psutil.get_pid_list():
    proc = psutil.Process(pid)

    if proc.username != "root":
        continue

    print proc.name, proc.cmdline, proc.pid

}}}

En la versión 0.3 de psutil el Ejemplo puede quedar como:

{{{
#!code python
import psutil

for proc in psutil.get_process_list():
    if proc.username != "root":
        continue
    print proc.name, proc.cmdline, proc.pid

}}}
