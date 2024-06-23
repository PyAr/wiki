.. title: Ventana de Password que Vibra


* Crear una ventana para passwords que vibra si la password es incorrecta. El campo de texto oculta los caracteres en pantalla. La vibración es configurable.

**Screenshot:**

.. image:: /images/VentanaPasswordVibra/temp.jpg

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    from Tkinter import *
    from time import sleep
    from random import randint
    #
    # correct password is: password
    #
    def check(Event = None):
        if hash(var.get()) != -1767432613:  # hash for password
            o = root.geometry()
            l['text'] = 'Wrong Password:\nAttemp will be logged and reported.'
            l.config(fg='red')
            for times in range(50):
                     root.geometry("+%d+%d" %(int(root.geometry().split("+")[1])+randint(-69, 69), int(root.geometry().split("+")[2])+randint(-69, 69)))
                     root.update()
                     sleep(.05)
                     root.geometry(o)
            root.geometry(o)
            root.update()
        else:
            l['text'] = 'OK: Connected to FBI Main Server...'
            print ('\nConnected to FBI Main Server...\n')
            l.config(fg='black')
            root.iconify()
            sleep(.25)
            root.deiconify()
            root.geometry()
        var.set("")
    #
    root = Tk()
    root.resizable(0, 0)
    root.title("FBI VPN Client")
    root.geometry("+800+350")
    root.wm_attributes("-topmost", 1)
    root.focus()
    root.config(bg='#F2F1F0', cursor='hand2')
    var = StringVar()
    l = Label(root, text = "FBI Login: Please type your password...", font=('ubuntu', 10), bg='#F2F1F0', bd=0, relief='flat', cursor='hand2')
    l.grid()
    a = Entry(root, font=('ubuntu', 12, 'bold'), show = '●', bg='#D7DAED', bd=0, relief='flat', cursor='xterm', highlightcolor='red', textvariable = var)  # show = '*'
    a.grid(row = 1, column = 0, padx = 10, pady = 10)
    a.bind("<Return>", check)
    a.focus()
    root.mainloop()


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

