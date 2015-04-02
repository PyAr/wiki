
tkScrollWhell
-------------

Usando la rueda de Scroll del raton con TK. Ejemplo simple con un poco de imaginacion puede manejar mas cosas.

::

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from Tkinter import *
    root = Tk()
    label = Label(root, text='Elija su Sexo usando la Rueda Scroll del Raton:')
    label.pack()
    optionlist = ("Femenino", "Masculino")
    var = StringVar()
    var.set(optionlist[0])
    optmen = OptionMenu(root, var, "Femenino", "Masculino")
    #
    def mouse_wheel(event):  # responde a la rueda de scroll
            if event.num == 5 or event.delta == -120:
                var.set(optionlist[0])
            if event.num == 4 or event.delta == 120:
                var.set(optionlist[1])
    #
    optmen.bind("<Button-4>", mouse_wheel)
    optmen.bind("<Button-5>", mouse_wheel)
    optmen.pack()
    root.mainloop()

