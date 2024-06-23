.. title: GtkEntry


Crear una ventana con un label, un campo de texto y mostrar el mensaje hola **nombre** con el valor ingresado en el entry.

.. image:: /images/Recetario/Gui/Gtk/Entry/Entry.png

.. code-block:: python

    import gtk
    import sys

    class Ventana(gtk.Window):
        '''clase que define una ventana que saluda'''

        def __init__(self):
            '''constructor, se llama al constructor de la clase padre'''
            gtk.Window.__init__(self)

            # un tamanio muy chico para que se expanda el minimo tamanio necesario
            self.set_default_size(10, 10)
            self.label = gtk.Label("nombre")
            self.entry = gtk.Entry()
            self.set_title("entry")
            # 5 pixeles de espacio entre el borde de la ventana y el primer
            # contenedor
            self.set_border_width(5)

            # 5 pixeles de espaciado entre cada widget
            hbox = gtk.HBox(spacing=5)
            hbox.pack_start(self.label)
            hbox.pack_start(self.entry)

            self.add(hbox)
            hbox.show_all()

            self.connect("delete-event", self.on_delete)
            # conectamos la senial activate (el usuario presiona enter)
            self.entry.connect("activate", self.on_entry_activate)

        def on_delete(self, window, event):
            '''llamado cuando se cierra la ventana'''
            sys.exit(0)

        def on_entry_activate(self, entry):
            '''llamada cuando se presiona enter en el entry, el primer elemento
            de toda senial de gtk es el elemento que emite la senial, asi que no
            necesitamos tener una referencia al elemento para interactuar con el'''
            message = gtk.MessageDialog(buttons=gtk.BUTTONS_OK,
                message_format="hola " + entry.get_text())
            message.run()
            message.hide()

    if __name__ == "__main__":
        hola = Ventana()
        hola.show()
        gtk.main()

