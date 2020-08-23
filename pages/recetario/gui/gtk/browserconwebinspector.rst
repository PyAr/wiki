.. title: Gtk Browser Con Web Inspector


Esta receta va más allá del "navegador en python en N lineas" (donde N < 30).

En este caso vemos cómo agregar el web inspector para inspeccionar y debuggear la página que estamos viendo.

El resultado al principio es algo así:

.. image:: /images/Recetario/Gui/Gtk/BrowserConWebInspector/brser1.png

Luego de hacer click derecho en la página y hacer click en "Inspect Element" tenemos algo así:

.. image:: /images/Recetario/Gui/Gtk/BrowserConWebInspector/brser2.png

El código:

.. code-block:: python

    import sys
    import gtk
    import webkit

    class Browser(gtk.Window):
        def __init__(self, url=''):
            gtk.Window.__init__(self)

            self.url = url
            self.view = webkit.WebView()

            self.set_title('Browser')
            self.set_default_size(640, 480)

            scroll = gtk.ScrolledWindow()
            scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
            scroll.set_shadow_type(gtk.SHADOW_IN)

            scroll.add(self.view)

            vbox = gtk.VBox()

            entry = gtk.Entry()
            entry.connect('activate', self._on_url_changed)

            if self.url:
                entry.set_text(self.url)
                self.open(self.url)

            vbox.pack_start(entry, False)
            vbox.pack_start(scroll, True, True)

            panels = gtk.VPaned()
            panels.add1(vbox)
            panels.show_all()

            settings = self.view.get_settings()
            settings.set_property("enable-developer-extras", True)

            def activate_inspector(self, *args):
                view = webkit.WebView()

                panels.add2(view)
                panels.set_position(panels.get_allocation().height / 2)
                view.show()

                return view

            inspector = self.view.get_web_inspector()
            inspector.connect("inspect-web-view", activate_inspector)

            self.add(panels)

            self.connect('delete-event', lambda *args: sys.exit(0))

        def open(self, url):
            if not url.startswith('http://') and not url.startswith('https://'):
                self.url = 'http://' + url
            else:
                self.url = url

            self.view.open(self.url)

        def _on_url_changed(self, entry):
            '''called when the url changes'''
            url = entry.get_text()
            self.open(url)

    if __name__ == '__main__':
        browser = Browser('www.google.com/search?q=python%20argentina')
        browser.show()
        gtk.main()

