.. title: GtkHBox


ejemplo que muestra el uso de hbox (cajas horizontales) para ordenar elementos de forma horizontal

.. image:: /images/Recetario/Gui/Gtk/HBox/hbox.png

.. code-block:: python

    import gtk
    import sys

    class Ventana(gtk.Window):
        '''clase que define una ventana que saluda'''

        def __init__(self):
            '''constructor, se llama al constructor de la clase padre'''
            gtk.Window.__init__(self)

            self.set_default_size(200, 200)
            self.set_title("hbox")
            # creamos una caja horizontal que contiene elementos
            # de manera horizontal
            self.hbox = gtk.HBox()
            # agregamos tres elementos
            self.hbox.pack_start(gtk.Label("uno"))
            self.hbox.pack_start(gtk.Label("dos"))
            self.hbox.pack_start(gtk.Label("tres"))

            self.add(self.hbox)
            self.hbox.show_all()

            self.connect("delete-event", self.on_delete)

        def on_delete(self, window, event):
            '''llamado cuando se cierra la ventana'''
            sys.exit(0)

    if __name__ == "__main__":
        ventana = Ventana()
        ventana.show()
        gtk.main()

