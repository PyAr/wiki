.. title: Gtk Label Con Color


Ejemplo de cómo cambiar el color de un label sin usar pango markup

Observaciones: sí se comenta label.realize() el color que se imprime no es el que seteamos sino el por defecto.

.. code-block:: python

    import gtk

    window = gtk.Window()
    label = gtk.Label("label")
    window.add(label)
    window.connect('delete-event', gtk.main_quit)
    label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#f00'))
    label.realize()
    print label.style.fg[gtk.STATE_NORMAL]
    window.show_all()
    gtk.main()

