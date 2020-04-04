
GtkHolaMundo
------------

Crea y muestra una ventana que muestra el famoso mensaje hola mundo.

.. image:: /images/Recetario/Gui/Gtk/HolaMundo/Hola%20mundo.png

.. code-block:: python

    import gtk
    import sys

    # se crea la ventana
    window = gtk.Window()
    # seteamos el tamanio de la ventana
    window.set_default_size(200, 200)
    # se crea la etiqueta que va a mostrar el mensaje
    label = gtk.Label("Hola pyar!")
    # se setea el el titulo de la ventana
    window.set_title("hola mundo")
    # agregamos el label a la ventana
    window.add(label)
    # mostramos la ventana y todo lo que contiene
    window.show_all()

    def on_window_close(window, event):
        '''este metodo es llamado cuando se aprieta la equis para cerrar la
        ventana'''
        # cerramos el programa retornando 0 (exito)
        sys.exit(0)

    # conectamos la senial delete-event que es emitida cuando se presiona la
    # equis en la ventana
    window.connect("delete-event", on_window_close)

    # llamamos al main loop para que muestre la ventana y
    # procese los eventos
    gtk.main()

