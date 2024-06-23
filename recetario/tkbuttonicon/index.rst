.. title: tkButtonIcon


Crea botones con Íconos. Si es en Windows sacar el '@'+ de la ruta al ícono. Los archivos se pueden pasar a .XBM con Gimp.

Ideal para crear mini-toolbars con íconos personalizados.

.. code-block:: python

    #!code python
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from Tkinter import *
    root = Tk()
    #
    boton1 = Button(root, bitmap='error')
    boton1.pack()
    boton2 = Button(root, bitmap='hourglass')
    boton2.pack()
    boton3 = Button(root, bitmap='info')
    boton3.pack()
    boton4 = Button(root, bitmap='questhead')
    boton4.pack()
    boton5 = Button(root, bitmap='warning')
    boton5.pack()
    boton6 = Button(root, bitmap='question')
    boton6.pack()
    boton7 = Button(root, bitmap='gray75')
    boton7.pack()
    boton8 = Button(root, bitmap='gray50')
    boton8.pack()
    boton9 = Button(root, bitmap='gray25')
    boton9.pack()
    boton10 = Button(root, bitmap='gray12')
    boton10.pack()
    boton11 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/icon'), state=DISABLED)
    boton11.pack()
    boton12 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/calculator'), cursor='hand2')
    boton12.pack()
    boton13 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/boxes'), relief=FLAT)
    boton13.pack()
    boton14 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/noletters'), bg='green')
    boton14.pack()
    boton15 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/dot'), bg='red')
    boton15.pack()
    boton16 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/Down'), bg='blue')
    boton16.pack()
    boton17 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/flagdown'), fg='green')
    boton17.pack()
    boton18 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/mailfull'), fg='red')
    boton18.pack()
    boton19 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/opendot'), fg='blue')
    boton19.pack()
    boton20 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/stipple'), bg='black', fg='grey')
    boton20.pack()
    boton21 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/target'), highlightcolor='red')
    boton21.pack()
    boton22 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/terminal'))
    boton22.pack()
    boton23 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/letters'))
    boton23.pack()
    boton24 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/tie_fighter'))
    boton24.pack()
    boton25 = Button(root, bitmap=('@'+'/usr/include/X11/bitmaps/woman'), bg='pink')
    boton25.pack()
    # botonX = Button(root, bitmap=('@'+'/path/to/your/custom/icon.xbm'), bg='someColor', fg='AnotherColor')
    # botonX.pack()
    #
    root.mainloop()

