
Keyboard Leds Demo
==================

* Como controlar los 3 Leds del Teclado usando Python, ejemplo simple, requiere Privilegios elevados en el equipo.

**Nota:** *Si tu teclado es a Baterias (Bluetooth, Wireless), el uso intensivo de este Script reducira la duracion de las mismas.*

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    import fcntl
    import os
    import time

    KDSETLED = 0x4B32
    SCR_LED  = 0x01
    NUM_LED  = 0x02
    CAP_LED  = 0x04

    console_fd = os.open('/dev/console', os.O_NOCTTY)

    all_on = SCR_LED | NUM_LED | CAP_LED
    all_off = 0

    while 1:
        fcntl.ioctl(console_fd, KDSETLED, all_on)
        time.sleep(0.1) # Aca se cambia el tiempo, o podria realizar una funcion mas compleja
        fcntl.ioctl(console_fd, KDSETLED, all_off)
        time.sleep(0.1) # Here changes the Timming, or something more complex


**Ejemplo:**

::

   sudo /usr/bin/env python keyboardleds.py

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas.html
