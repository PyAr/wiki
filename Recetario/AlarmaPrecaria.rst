= Alarma Precaria =

Alarma minima y basica de linea de comandos.

 {{{
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
}}}

== Comentarios ==

=== Facundo ===

Hay un par de cambios triviales para hacerle: se puede reemplazar el not_executed por un break, no hace falta declarar el encoding, y usar localtime() como corresponde..

{{{
#!/usr/bin/env python

import time
import os
while(True):
    dt = time.localtime()
    sleep(1)
    if dt.tm_hour == 8 and dt.tm_min == 30: # modificar hour y minute a la hora deseada
        os.system("xdg-open /home/user/ring.ogg") # RingTone (?)
        break
}}}

... pero realmente está mal planteado la resolución: no hay que usar un while ahí:


{{{
#!/usr/bin/env python

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
}}}
