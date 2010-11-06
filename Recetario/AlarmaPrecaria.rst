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
