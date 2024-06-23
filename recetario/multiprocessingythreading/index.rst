.. title: Multiprocessing y Threading


En esta receta se muestra cómo hacer para correr algo en otro thread o proceso con pocos cambios y cómo lograr comunicación entre ellos.

Notar que el pid de quién lanza doer es distinto al que imprime doer

Ejemplo con Multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import os
    import sys

    from multiprocessing import Process
    from multiprocessing import Queue

    class Doer(Process):

        def __init__(self, queue, state=None):
            Process.__init__(self)
            self.queue = queue
            self.state = state

        def _do_on_start(self):
            print "doint stuff on start"
            print "state:", self.state
            print "pid:", os.getpid()
            print

        def _on_end(self):
            print "doint stuff on end"
            print "state:", self.state
            print "pid:", os.getpid()
            print

        def run(self):
            self._do_on_start()

            msg = None
            while msg is None or msg != "exit":
                # blocks here
                msg = self.queue.get()
                print "handling message", msg

                # do stuff here according to the message
                if msg == "ping":
                    print "pong"
                elif isinstance(msg, tuple) and len(msg) == 2:
                    action, value = msg
                    if action == "set-state":
                        self.state = value
                        print "new state:", self.state
                elif msg != "exit":
                    print "unknown message", msg

                print

            self._on_end()

    def demo():
        queue = Queue()
        print "creating doer from process", os.getpid()
        doer = Doer(queue, 42)
        doer.start()
        queue.put("ping")
        queue.put("foo")
        queue.put(("set-state", "hola!"))

        queue.put("exit")

        doer.join()

    if __name__ == "__main__":
        demo()


corriendolo tenemos el resultado

.. code-block:: bash

   $ python controlled.py
   creating doer from process 11784
   doint stuff on start
   state: 42
   pid: 11785

   handling message ping
   pong

   handling message foo
   unknown message foo

   handling message ('set-state', 'hola!')
   new state: hola!

   handling message exit

   doint stuff on end
   state: hola!
   pid: 11785

Ejemplo con Threading
~~~~~~~~~~~~~~~~~~~~~

Para hacerlo andar con threading hay que solo cambiar de donde importamos las cosas, aquí esta la diferencia:

Notar que el pid de quién lanza doer es igual al que imprime doer.

.. code-block:: diff

    diff controlled.py controlledthread.py
    4,5c4,5
    < from multiprocessing import Process
    < from multiprocessing import Queue
    ---
    > from threading import Thread as Process
    > from Queue import Queue


.. code-block:: python

    import os
    import sys

    from threading import Thread as Process
    from Queue import Queue

    class Doer(Process):

        def __init__(self, queue, state=None):
            Process.__init__(self)
            self.queue = queue
            self.state = state

        def _do_on_start(self):
            print "doint stuff on start"
            print "state:", self.state
            print "pid:", os.getpid()
            print

        def _on_end(self):
            print "doint stuff on end"
            print "state:", self.state
            print "pid:", os.getpid()
            print

        def run(self):
            self._do_on_start()

            msg = None
            while msg is None or msg != "exit":
                # blocks here
                msg = self.queue.get()
                print "handling message", msg

                # do stuff here according to the message
                if msg == "ping":
                    print "pong"
                elif isinstance(msg, tuple) and len(msg) == 2:
                    action, value = msg
                    if action == "set-state":
                        self.state = value
                        print "new state:", self.state
                elif msg != "exit":
                    print "unknown message", msg

                print

            self._on_end()

    def demo():
        queue = Queue()
        print "creating doer from process", os.getpid()
        doer = Doer(queue, 42)
        doer.start()
        queue.put("ping")
        queue.put("foo")
        queue.put(("set-state", "hola!"))

        queue.put("exit")

        doer.join()

    if __name__ == "__main__":
        demo()


.. code-block:: bash

   $ python controlledthread.py
   creating doer from process 11812
   doint stuff on start
   state: 42
   pid: 11812

   handling message ping
   pong

   handling message foo
   unknown message foo

   handling message ('set-state', 'hola!')
   new state: hola!

   handling message exit

   doint stuff on end
   state: hola!
   pid: 11812

