.. title: Reloj Digital


* Crear un Reloj digital simple, empleando un Label de TK.

**Screenshot:**

.. image:: /images/RelojDigital/temp.jpg

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    from Tkinter import *
    import time
    #
    root = Tk()
    root.focus()
    root.title("ǝɯıʇ uoɥʇʎd")
    root.config(cursor='watch')
    time1 = ''
    clock = Label(root, font=('ubuntu', 30, 'bold'), bg='#3C3B37', fg='white', bd=0)
    clock.pack(fill=BOTH, expand=1)
    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)
    tick()
    root.mainloop()


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

