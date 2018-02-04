
tkWindowIcon
------------

Crea una ventana con Icono de ventana. Los archivos se pueden pasar a .XBM con Gimp.

::

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


