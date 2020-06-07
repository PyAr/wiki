.. title: Qt Multi Thread


ejemplo de como manipular la interfaz grafica desde multiples threads.

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    #qt_multithread.py

    #Modificado de la versión original de Mariano Guerra para GTK ( http://python.org.ar/pyar/GtkMultiThread )
    #Versión para Qt por Ernesto Savoretti

    from PyQt4 import QtCore, QtGui
    import time
    import Queue
    import random
    import threading
    import sys

    TEXTS = ['eggs', 'spam', 'pyar', 'gtk', 'qt']

    class Molesto(threading.Thread):
        '''un thread que quiere molestar el main thread'''

        def __init__(self, cola):
            threading.Thread.__init__(self)
            self.setDaemon(True)
    #        self.label = label # no usar en este thread!

            self.cola = cola

        def run(self):
            '''metodo principal del thread, duerme un tiempo aleatorio y despues
            pone algo en la cola para que el main thread lo haga'''

            while True:
                time.sleep(random.random() * 5)
                texto = self.getName() + ' ' + random.choice(TEXTS)
                print self.getName(), 'escribiendo', texto
                self.cola.put(texto)

    class Ventana(QtGui.QWidget):
        '''ventana con un label, ninguna locura'''

        def __init__(self, parent = None):
            QtGui.QWidget.__init__(self, parent)
            self.setGeometry(50, 50, 640, 480)
            self.setWindowTitle('Qt con threads')
            layout = QtGui.QHBoxLayout()
            self.label = QtGui.QLabel(self, text = '')
            layout.addWidget(self.label)
            self.setLayout(layout)
            self.cola = Queue.Queue()
            self.hincha_b = Molesto(self.cola)

            self.hincha_b.start()

            self.timer = QtCore.QTimer(self)
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.queue_manager)
            self.timer.start()
            self.show()

        def queue_manager(self):
            try:
                while True:
                    texto = self.cola.get(True, 0.1)
                    print texto
                    self.label.setText(texto)
            except Queue.Empty:
                pass

            return True

    if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        w = Ventana()
        app.exec_()

