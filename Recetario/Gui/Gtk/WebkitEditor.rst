
Gtk Webkit Editor
=================

ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

para probarlo correlo, entra una direccion que empiece con http://, hace foco en alguna parte de la pagina y ponete a tipear como si fuera un editor de texto comun.

un ejemplo de su uso (tarea del autor encontrar los cambios |wink|

`webkit.png </wiki/Recetario/Gui/Gtk/WebkitEditor/attachment/585/webkit.png>`_

::

    import gtk
    import webkit

    class Editor(webkit.WebView):
        '''a webkit editor'''

        def __init__(self):
            webkit.WebView.__init__(self)
            self.set_editable(True)

    class EditorWindow(gtk.Window):
        '''the editor window'''

        def __init__(self):
            gtk.Window.__init__(self)
            self.set_title("webkit editor")
            self.set_default_size(800, 600)

            self.entry = gtk.Entry()
            self.entry.set_text("http://webkit.org")
            self.entry.connect('activate', self._on_entry_activate)
            self.editor = Editor()
            scroll = gtk.ScrolledWindow()
            scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
            scroll.set_shadow_type(gtk.SHADOW_IN)

            scroll.add(self.editor)

            vbox = gtk.VBox()
            vbox.pack_start(self.entry, False)
            vbox.pack_start(scroll)

            self.add(vbox)
            vbox.show_all()

        def load(self, url):
            '''load the given url in the editor and set it to editable'''
            self.editor.open(url)

        def _on_entry_activate(self, entry):
            '''callback called when the user hits enter on the entry'''
            self.load(entry.get_text())

    if __name__ == '__main__':
        window = EditorWindow()
        window.show()
        window.entry.activate()
        gtk.main()


Tengan en cuenta que en Ubuntu inferior 10.04 python-webkit en gtk nececita SI o SI llamar a "gtk.gdk.threads_init()", si no tira error:

::

   GLib-ERROR **: The thread system is not yet initialized.
   aborting...
   Cancelado

Entonces deberan agregar un "gtk.gdk.threads_init()" antes de llamar a "EditorWindow_()", el final del codigo les quedara de la siguiente manera:

::

    if __name__ == '__main__':
        gtk.gdk.threads_init()
        window = EditorWindow()
        window.show()
        window.entry.activate()
        gtk.main()


-------------------------



  CategoryRecetas_

