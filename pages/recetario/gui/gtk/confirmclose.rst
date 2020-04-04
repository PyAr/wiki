.. title: GtkConfirmClose


Ejemplo de como solicitar confirmación de cierre en una ventana

.. code-block:: python

    import sys
    import gtk

    class VentanaPrincipal(gtk.Window):
        '''la ventana principal'''

        def __init__(self):
            '''constructor'''
            gtk.Window.__init__(self)
            self.set_default_size(300, 200)
            self.set_title('Ejemplo')

            label = gtk.Label('cerrame')
            label.show()

            self.add(label)
            self.connect('delete-event', self._on_close)

        def _on_close(self, widget, event):
            '''metodo llamado cuando aprietan el boton cerrar'''
            if not self.confirmar_cierre():
                return True
            else:
                sys.exit(0)

        def confirmar_cierre(self):
            '''muestra un dialogo que pregunta si esta seguro que
            quiere cerrar, devuelve True si selecciona si'''
            dialogo = gtk.MessageDialog(self, type=gtk.MESSAGE_QUESTION,
                buttons=gtk.BUTTONS_YES_NO,
                message_format="Esta seguro que desea salir?")

            response = dialogo.run()
            dialogo.hide()

            if response == gtk.RESPONSE_YES:
                return True

            return False


    def test():
        '''prueba la implementacion'''
        ventana = VentanaPrincipal()
        ventana.show()
        gtk.main()

    if __name__ == '__main__':
        test()

