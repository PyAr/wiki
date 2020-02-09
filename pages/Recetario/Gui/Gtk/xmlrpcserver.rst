
Servidor XMLRPC dentro de un hilo gtk

::

    from SimpleXMLRPCServer import SimpleXMLRPCServer
    import gtk
    import gobject
    import time

    def hello(name):
            dialog = gtk.Dialog("Hello dialog",
                            None,
                            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                            (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                    gtk.STOCK_OK, gtk.RESPONSE_ACCEPT,)
                            )
            label = gtk.Label('Hello %s'%name)
            dialog.vbox.pack_start(label)
            label.show()
            response = dialog.run()
            dialog.destroy()
            return response
    def change_time(label):
            label.set_text(repr(time.time()))
            return True
    def handle_request(source, condition, webservice):
            try:
                    webservice.handle_request()
            except:
                    pass
            return True

    s = SimpleXMLRPCServer(('localhost',8080))
    s.register_function(hello)
    gobject.io_add_watch(s.socket, gobject.IO_IN,
                         handle_request, s)
    win = gtk.Window()
    win.connect('destroy', gtk.main_quit)
    win.set_size_request(300,300)
    label = gtk.Label('Main window')
    gobject.timeout_add(100, change_time, label)
    win.add(label)
    win.show_all()
    gtk.main()


-------------------------



  CategoryRecetas_

.. _dialog: /pages/Recetario/Gui/Gtk/dialog.html
.. _categoryrecetas: /pages/categoryrecetas.html
