.. title: ButtonBox


este ejemplo muestra como usar un contenedor de botones para agregar botones y hacer que mantengan su tamanio óptimo y se distribuyan por la pantalla de manera homogénea.

.. image:: /images/Recetario/Gui/Gtk/ButtonBox/buttonbox-demo.png

.. code-block:: python

    import gtk

    window = gtk.Window()
    window.set_default_size(640, 480)
    window.set_title("button box demo")

    vbox = gtk.VBox()

    hbox1 = gtk.HButtonBox()
    hbox1.pack_start(gtk.Button(stock=gtk.STOCK_OK))

    def build_bbox():
            """build a hbox fill it with example buttons and return it"""
            hbox = gtk.HButtonBox()

            hbox.pack_start(gtk.Button(stock=gtk.STOCK_YES))
            hbox.pack_start(gtk.Button(stock=gtk.STOCK_NO))

            return hbox

    hbox2 = build_bbox()
    hbox2.set_layout(gtk.BUTTONBOX_SPREAD)

    hbox3 = build_bbox()
    hbox3.set_layout(gtk.BUTTONBOX_EDGE)

    hbox4 = build_bbox()
    hbox4.set_layout(gtk.BUTTONBOX_START)

    hbox5 = build_bbox()
    hbox5.set_layout(gtk.BUTTONBOX_END)

    hbox6 = build_bbox()
    hbox6.set_layout(gtk.BUTTONBOX_END)
    help_button = gtk.Button(stock=gtk.STOCK_HELP)
    hbox6.pack_start(help_button)
    hbox6.set_child_secondary(help_button, True)

    vbox.pack_start(hbox1)
    vbox.pack_start(hbox2)
    vbox.pack_start(hbox3)
    vbox.pack_start(hbox4)
    vbox.pack_start(hbox5)
    vbox.pack_start(hbox6)

    window.add(vbox)
    window.show_all()

    window.connect('destroy', gtk.main_quit)

    gtk.main()


Mas Información
---------------

* http://pygtk.org/docs/pygtk/class-gtkhbuttonbox.html

* http://pygtk.org/docs/pygtk/class-gtkbuttonbox.html

* http://pygtk.org/docs/pygtk/class-gtkbox.html

.. _buttonbox: /Recetario/Gui/Gtk/buttonbox
