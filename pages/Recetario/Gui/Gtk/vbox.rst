.. title: GtkVBox


ejemplo que muestra el uso de vbox (cajas verticales) para ordenar elementos de forma vertical

.. image:: /images/Recetario/Gui/Gtk/VBox/vbox.png

.. code-block:: python

    import gtk
    import sys

    class Ventana(gtk.Window):
        '''clase que define una ventana que saluda'''

        def __init__(self):
            '''constructor, se llama al constructor de la clase padre'''
            gtk.Window.__init__(self)

            self.set_default_size(200, 200)
            self.set_title("vbox")
            # creamos una caja vertical que contiene elementos
            # de manera vertical
            self.vbox = gtk.VBox()
            # agregamos tres elementos
            self.vbox.pack_start(gtk.Label("uno"))
            self.vbox.pack_start(gtk.Label("dos"))
            self.vbox.pack_start(gtk.Label("tres"))

            self.add(self.vbox)
            self.vbox.show_all()

            self.connect("delete-event", self.on_delete)

        def on_delete(self, window, event):
            '''llamado cuando se cierra la ventana'''
            sys.exit(0)

    if __name__ == "__main__":
        ventana = Ventana()
        ventana.show()
        gtk.main()

