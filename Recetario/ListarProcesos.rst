= Listar Procesos =

Esta receta muestra una forma de listar procesos en python que soporta múltiples sistemas operativos

En el ejemplo se muestra como listar información sobre los procesos corriendo bajo el usuario "root"

{{{
#!code python
import psutil

for pid in psutil.get_pid_list():
    proc = psutil.Process(pid)

    if proc.username != "root":
        continue

    print proc.name, proc.cmdline, proc.pid

}}}
