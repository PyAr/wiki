
Alarma Precaria
===============

Alarma mínima y básica de linea de comandos.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import time
    import os
    not_executed = 1
    while(not_executed):
        dt = list(time.localtime())
        hour = dt[3]
        minute = dt[4]
        sleep(1)
        if hour == 8 and minute == 30: # modificar hour y minute a la hora deseada
            os.system("xdg-open /home/user/ring.ogg") # RingTone (?)
            not_executed = 0


Comentarios
-----------

Facundo
~~~~~~~

Hay un par de cambios triviales para hacerle: se puede reemplazar el not_executed por un break, no hace falta declarar el encoding, y usar localtime() como corresponde..

::

    #!/usr/bin/env python

    import time
    import os
    while(True):
        dt = time.localtime()
        sleep(1)
        if dt.tm_hour == 8 and dt.tm_min == 30: # modificar hour y minute a la hora deseada
            os.system("xdg-open /home/user/ring.ogg") # RingTone (?)
            break


... pero realmente está mal planteado la resolución: no hay que usar un while ahí:

::

    import time
    import os

    # modificar hour y minute a la hora deseada
    HOUR = 8
    MIN = 30

    t = time.localtime()
    nowhms = t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec
    alarm = HOUR * 3600 + MIN * 60
    delta = alarm - nowhms
    if delta < 0:
        # tomorrow
        delta += 3600 * 24
    time.sleep(delta)
    os.system("xdg-open /home/user/ring.ogg") # RingTone (?)


DanielMoisset
~~~~~~~~~~~~~

Yo prefiero no scar cuentas de fecha a mano, y en vez que datetime haga el trabajo sucio. Sobre todo porque maneja mejor casos delicados (que pasa si pongo la alarma justo antes de un cambio a horario de verano?) sin tener que pensarlos

::

    import time, datetime
    import os

    # modificar hour y minute a la hora deseada

    HOUR = 8
    MIN = 30

    now = datetime.datetime.now()
    alarm = now.replace(hour=HOUR, minute=MIN)
    if alarm < now:
        # Set the alarm tomorrow
        alarm += datetime.timedelta(days=1)
    time.sleep((alarm-now).seconds)
    os.system("xdg-open /home/user/ring.ogg") # RingTone (?)


Juancarlospaco
~~~~~~~~~~~~~~

*Por lo menos en Linux se necesita el Shebang y declarar encoding, por que sino al usar "Vídeo-de-Música.ogv" de Ringtone traen problemas los acentos.*

-------------------------



A esta altura creo que es mas importante agregar el correcto coloreado de sintaxis y cuidar la ortografia, a discutir si poner o no el encoding y el shebang. La idea es que las recetas sean genericas, con ese encoding y ese shebang, no cubris todos los casos. Pej, copias y pegas, y tu editor guarda en latin1??

Si funciona con:

::

    usuario@maquina: ~$ python receta.py


Es mas que suficiente. -- JoaquinSorianello_ `[[DateTime(2010-11-08T10:56:40-0300)]]`_

.. _joaquinsorianello: /pages/joaquinsorianello.html
.. _categoryrecetas: /pages/categoryrecetas.html
