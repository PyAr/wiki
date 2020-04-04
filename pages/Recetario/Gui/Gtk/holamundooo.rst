.. title: GtkHolaMundoOO


ejemplo que hace lo mismo que GtkHolaMundo_ pero orientado a objetos

.. image:: /images/Recetario/Gui/Gtk/HolaMundoOO/Hola%20mundo%20oo.png

::

    import gtk
    import sys

    class HolaMundo(gtk.Window):
        '''clase que define una ventana que saluda'''

        def __init__(self):
            '''constructor, se llama al constructor de la clase padre'''
            gtk.Window.__init__(self)

            self.set_default_size(200, 200)
            self.label = gtk.Label("Hola pyar")
            self.set_title("hola mundo oo")
            self.add(self.label)
            self.label.show()

            self.connect("delete-event", self.on_delete)

        def on_delete(self, window, event):
            '''llamado cuando se cierra la ventana'''
            sys.exit(0)

    if __name__ == "__main__":
        hola = HolaMundo()
        hola.show()
        gtk.main()


.. _GtkHolaMundo: /Recetario/Gui/Gtk/holamundo
