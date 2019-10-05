
Gtk ListView
------------

`gtklistexample.png </images/Recetario/Gui/Gtk/ListView/gtklistexample.png>`_

::

    import gtk
    import gobject

    class GtkListExample(gtk.Window):
        '''clase que representa una ventana con una lista'''

        def __init__(self, width=640, height=480, title="gtk list example",
                on_exit=gtk.main_quit):
            '''constructor'''
            # llamamos al constructor de la clase padre
            gtk.Window.__init__(self)

            # establecemos el tamanio
            self.set_default_size(width, height)
            # establecemos el titulo
            self.set_title(title)

            # creamos el modelo de cada fila
            # el modelo y la vista se crean separadamente y se relacionan despues
            # https://es.wikipedia.org/wiki/Modelo_Vista_Controlador
            self.model = gtk.ListStore(str, int, bool)
            # creamos el widget que va a mostrar la lista y le pasamos el modelo
            self.list = gtk.TreeView(self.model)

            # creamos los objetos que van a renderizar los atributos
            textrenderer = gtk.CellRendererText()
            # seteamos una propiedad
            textrenderer.set_property("xalign", 0.5)
            # un renderer para renderizar booleanos como checkbox
            boolrenderer = gtk.CellRendererToggle()

            # creamos las columnas de la lista
            # no necesariamente todos los elementos del modelo se deben mostrar
            # tampoco es necesario que se muestren en el orden del modelo, por
            # eso creamos las columnas para decirle que elementos del modelo
            # mostrar y como mostrarlos
            column1 = gtk.TreeViewColumn("nombre", textrenderer, text=0)
            column1.set_expand(True)

            column2 = gtk.TreeViewColumn("edad", textrenderer, text=1)
            column2.set_expand(True)

            column3 = gtk.TreeViewColumn("algo", boolrenderer, active=2)
            column3.set_expand(True)

            # agregamos las columnas
            self.list.append_column(column1)
            self.list.append_column(column2)
            self.list.append_column(column3)

            # agregamos la lista a la ventana
            self.add(self.list)
            # mostramos el widget
            self.list.show_all()
            # conectamos un manejador para cuando aprieten cerrar
            self.connect('delete-event', on_exit)

        def add_item(self, string, number, boolean):
            # agregamos una fila al modelo
            self.model.append((string, number, boolean))

    if __name__ == "__main__":
        window = GtkListExample()
        window.show()
        window.add_item("bob", 26, True)
        window.add_item("patricio", 24, True)
        window.add_item("arenita", 27, False)

        gtk.main()

