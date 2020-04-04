.. title: GtkErrorHandler


Si aplicamos el decorador error_handler a una función, cuando lance una excepción, vamos a obtener un dialogo modal mostrandomos el traceback.  Recomiendo usarlo solo para debug o versiones beta, un usuario no debería ver el traceback crudo.

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import gtk

    def error_handler(function):
        def out(*args, **kwargs):
            try:
                return function(*args, **kwargs)

            except KeyboardInterrupt:
                raise KeyboardInterrupt

            except:
                from traceback import format_exc
                error = gtk.MessageDialog(
                    type=gtk.MESSAGE_ERROR,
                    buttons=gtk.BUTTONS_OK,
                    message_format=''.join(format_exc())
                    )
                error.set_title("Something went wrong!")
                if error.run() == gtk.RESPONSE_OK:
                    print "Error OK"
                else:
                    print "Error closed"
                error.hide()
        return out

    class Gui:
        def __init__(self):
            self.window = gtk.Window()
            self.window.set_default_size(200,200)
            self.window.set_title("Simple PyGTK example")

            self.vbox = gtk.VBox()

            self.button = gtk.Button("Click me!")

            self.vbox.pack_start(self.button)

            self.window.add(self.vbox)

            self.button.connect("clicked", self.on_clicked)
            self.window.connect("destroy", lambda x: gtk.main_quit())
            self.window.show_all()
            self.window.show()

        @error_handler
        def on_clicked(self, widget):
           raise IndexError

    if __name__ == "__main__":
        app = Gui()
        gtk.main()

