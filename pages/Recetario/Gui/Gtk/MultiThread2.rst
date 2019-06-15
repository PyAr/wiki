
Otro ejemplo del uso de threads con gtk, compare con el `otro ejemplo`_ que utiliza colas

::

    import time
    import random
    import threading

    import gtk
    import gtk.gdk


    texts = ['eggs', 'spam', 'pyar', 'gtk']

    class molesto(threading.Thread):
        '''un thread que quiere molestar el main thread'''

        def __init__(self, label):
            threading.Thread.__init__(self)
            self.setDaemon(True)
            self.label = label

        def run(self):
            '''metodo principal del thread, duerme un tiempo aleatorio y despues
            cambia el Label'''

            while True:
                time.sleep(random.random() * 5)
                texto = self.getName() + ' ' + random.choice(texts)

                gtk.gdk.threads_enter()
                # zona critica de gtk
                print self.getName(), 'escribiendo', texto
                self.label.set_text(texto)
                gtk.gdk.threads_leave()

    class ventana(gtk.Window):
        '''ventana con un label, ninguna locura'''

        def __init__(self):
            gtk.Window.__init__(self)
            self.set_default_size(640, 480)
            self.set_title('gtk con threads')
            self.label = gtk.Label('')
            self.add(self.label)
            self.label.show()

    if __name__ == '__main__':
        gtk.gdk.threads_init()
        ventana = ventana()
        ventana.show()
        threads = [molesto(ventana.label) for x in range(10)]
        for thread in threads:
            thread.start()
        gtk.main()


.. ############################################################################

.. _otro ejemplo: GtkMultiThread

