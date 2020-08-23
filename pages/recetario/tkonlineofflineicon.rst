.. title: tkOnLineOffLineIcon


Crea un ícono que cambia de estado según si se esta o no conectado a Internet. Notar que se pueden cambiar más propiedades del botón que las que este simple ejemplo cambia.

.. code-block:: python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from Tkinter import *
    import socket
    root = Tk()
    # Comprobador de conexion a Internet
    inet = Button(root, bitmap='info', fg='green', bg='white')
    inet.pack(pady=20, padx=20)
    #
    try:
        socket.gethostbyname('google.com')
        c = socket.create_connection(('google.com', 80), 1)
        m = socket.gethostbyname('google.com')
        print m  # imprime la ip de google.com para pruebas
        c.close()
    except socket.gaierror:
        print (" ERROR: DNS Error... ")
        inet.config(bitmap='error', fg='red', bg='black') # cambia a un icono de error
    except socket.error:
        print (" ERROR: Connection error... ")
        inet.config(bitmap='error', fg='red', bg='black') # cambia a un icono de error
    #
    root.mainloop()

