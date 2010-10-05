= Gtk Webkit Editor =

ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

para probarlo correlo, entra una direccion que empiece con http://, hace foco en alguna parte de la pagina y ponete a tipear como si fuera un editor de texto comun.

{{{
#!code python
import gtk
import webkit

class Editor(webkit.WebView):
    '''a webkit editor'''

    def __init__(self):
        webkit.WebView.__init__(self)
        self.connect('load-finished', self._loading_finished_cb)

    def _loading_finished_cb(self, *args):
        self.execute_script("document.designMode='On';")

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
}}}
