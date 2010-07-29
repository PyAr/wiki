Otro ejemplo del uso de threads con gtk, compare con el [[GtkMultiThread|otro ejemplo]] que utiliza colas


{{{
#!code python
import time
import random
import threading

import gtk
import gtk.gdk


texts = ['eggs', 'spam', 'pyar', 'gtk']

class molesto(threading.thread):
    '''un thread que quiere molestar el main thread'''

    def __init__(self, label):
        threading.thread.__init__(self)
        self.setdaemon(true)
        self.label = label

    def run(self):
        '''metodo principal del thread, duerme un tiempo aleatorio y despues
        cambia el Label'''

        while true:
            time.sleep(random.random() * 5)
            texto = self.getname() + ' ' + random.choice(texts)

            gtk.gdk.threads_enter()
            # zona critica de gtk
            print self.getname(), 'escribiendo', texto
            self.label.set_text(texto)
            gtk.gdk.threads_leave()

class ventana(gtk.window):
    '''ventana con un label, ninguna locura'''

    def __init__(self):
        gtk.window.__init__(self)
        self.set_default_size(640, 480)
        self.set_title('gtk con threads')
        self.label = gtk.label('')
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
}}}
