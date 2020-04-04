.. title: tkWindowIcon


Crea una ventana con Icono de ventana. Los archivos se pueden pasar a .XBM con Gimp.

.. code-block:: python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from Tkinter import *
    root = Tk()
    #
    try:
        root.wm_iconbitmap('@'+'/usr/include/X11/bitmaps/icon')  # Ruta al icono, formato .XBM
    except TclError:
        print(" ")
        print(" ERROR: Icon File not found... ") # imprime este mensaje si el icono no se encuentra
        print(" ")
        pass
    #
    root.mainloop()

Si estamos en Windows es mejor usar la funcion iconbitmap('Icono.ico') que tambien se puede pasar la imagen a .ico con Gimp.

.. code-block:: python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    from Tkinter import *
    root = Tk()
    #
    try:
        root.iconbitmap('Icono.ico')  # icono en  formato .ico de windows
    except TclError:
        print(" ")
        print(" ERROR: Icon File not found... ") # imprime este mensaje si el icono no se encuentra
        print(" ")
        pass
    #
    root.mainloop()
