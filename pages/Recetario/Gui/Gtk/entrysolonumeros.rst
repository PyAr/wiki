
GtkEntrySoloNumeros
===================

Este ejemplo muestra como permitir el ingreso de solo números en un gtk.Entry, a través de la señal insert-text_ de gtk.Editable (clase de la que hereda gtk.Entry) y usando el método stop_emission_ de gobject para vitar que la señal se propague y sea manejada por el handler por defecto para la señal (que es el que inserta el carácter en el widget)

.. image:: /images/Recetario/Gui/Gtk/EntrySoloNumeros/Only%20numbers.png

::

    '''ejemplo sobre solo dejar ingresar numeros en un campo de text
    tambien sirve para cadenas de texto pegadas en el entry con ctrl-v
    '''

    import re
    import gtk

    ONLY_NUMBERS = re.compile('^[0-9]*$')

    def on_insert_text(editable, new_text, new_text_length, position):
        '''called when text is inserted on an entry'''
        if ONLY_NUMBERS.match(new_text) is None:
            editable.stop_emission('insert-text')

    entry = gtk.Entry()
    entry.connect('insert-text', on_insert_text)
    window = gtk.Window()
    window.set_title('only numbers')
    window.add(entry)
    window.connect('delete-event', gtk.main_quit)
    window.show_all()

    gtk.main()


.. ############################################################################

.. _insert-text: http://library.gnome.org/devel/pygtk/stable/class-gtkeditable.html#signal-gtkeditable--insert-text

.. _stop_emission: http://library.gnome.org/devel/pygobject/stable/class-gobject.html#method-gobject--stop-emission

