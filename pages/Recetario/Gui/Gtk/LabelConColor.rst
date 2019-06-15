
Gtk Label Con Color
===================

ejemplo de como cambiar el color de un label sin usar pango markup 

observaciones, si se comenta label.realize() el color que se imprime no es el que seteamos si no el por defecto.

::

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

