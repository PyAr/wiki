.. title: GtkMultiThread


Ejemplo de como manipular la api desde multiples threads sin usar locks. Compare con el `otro ejemplo`_ que no utiliza colas.

::

    import gtk
    import time
    import Queue
    import random
    import gobject
    import threading

    TEXTS = ['eggs', 'spam', 'pyar', 'gtk']

    class Molesto(threading.Thread):
        '''un thread que quiere molestar el main thread'''

        def __init__(self, label, cola):
            threading.Thread.__init__(self)
            self.setDaemon(True)
            self.label = label # no usar en este thread!
            self.cola = cola

        def run(self):
            '''metodo principal del thread, duerme un tiempo aleatorio y despues
            pone algo en la cola para que el main thread lo haga'''

            while True:
                time.sleep(random.random() * 5)
                texto = self.getName() + ' ' + random.choice(TEXTS)
                print self.getName(), 'escribiendo', texto
                self.cola.put((self.label.set_text, (texto,), {}))

    class Ventana(gtk.Window):
        '''ventana con un label, ninguna locura'''

        def __init__(self):
            gtk.Window.__init__(self)
            self.set_default_size(640, 480)
            self.set_title('gtk con threads')
            self.label = gtk.Label('')
            self.add(self.label)
            self.label.show()


    queue = Queue.Queue()
    def queue_manager():
        try:
            while True:
                method, args, kwargs = queue.get(True, 0.1)
                print 'ejecutando', method.__name__, 'con', args, kwargs
                method(*args, **kwargs)
        except Queue.Empty:
            pass

        return True

    if __name__ == '__main__':
        gtk.gdk.threads_init()
        gobject.timeout_add(200, queue_manager)
        ventana = Ventana()
        ventana.show()
        threads = [Molesto(ventana.label, queue) for x in range(10)]
        for thread in threads:
            thread.start()
        gtk.main()


.. ############################################################################

.. _otro ejemplo: /Recetario/Gui/Gtk/multithread2

