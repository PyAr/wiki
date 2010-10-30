= CheckDistroVersion =

Chequea la version de la Distribucion Linux, y actua en funcion de eso.

{{{
import platform

osInfo = ('Ubuntu', '10.10', 'maverick')
sysInfo = platform.linux_distribution()

if osInfo == sysInfo:
    print(" OK ")
    # Aca va que hacer si esta OK
else:
    print(" ERROR ")
    # Aca va que hacer si la version no es correcta
}}}
