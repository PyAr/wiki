.. title: Comunicar threads con colas


El siguiente ejemplo muestra como se pueden comunicar threads a traves de cola y como se puede utilizar las caracteristicas de las colas para hacer que un hilo solo trabaje cuando hay algo para hacer.

En el ejemplo se crean 2 clases:

* Reader: se bloquea esperando un mensaje de una cola llamada self.in_queue, cuando hay algo lo imprime, si el mensaje es 'quit' saluda y finaliza

* Writer: se bloquea esperando un mensaje de una cola llamada self.in_queue, cuando hay algo lo invierte y lo envia a la cola de salida (self.out_queue), si el mensaje es 'quit', lo pone en self.out_queue, saluda y finaliza.

En el ejemplo se crea un hilo Reader, un Writer, se inicializan ambos y se conecta la cola de salida de Writer con la entrada de Reader, de esta manera, cualquier mensaje enviado a la cola de entrada de Writer sera invertida, enviada por la salida, la cual sera leida por Reader e impresa, al introducir el mensaje 'quit' ambos threads finalizan.

::

   import Queue
   import threading

   # este thread se bloquea esperando que venga algo en la cola,
   # lo unico que hace es imprimirlo. Si el mensaje es quit finaliza
   class Reader(threading.Thread):
      def __init__(self, in_queue):
          threading.Thread.__init__(self)
          self.in_queue = in_queue

      def run(self):
          while True:
              msg = self.in_queue.get()
              if msg == 'quit':
                  print 'reader se va!'
                  break

              print 'leido ' + msg

   # este thread se bloquea esperando que venga algo en la cola de entrada,
   # cuando llega algo lo escribe al reves en la cola de salida.
   class Writer(threading.Thread):
      def __init__(self, in_queue, out_queue):
          threading.Thread.__init__(self)
          self.in_queue = in_queue
          self.out_queue = out_queue

      def run(self):
          while True:
              msg = self.in_queue.get()
              if msg == 'quit':
                  print 'writer se va!'
                  self.out_queue.put(msg)
                  break

              print 'escrito ' + msg

              self.out_queue.put(msg[::-1])

   # aca creo un lector y un escritor, le doy de salida a writer la
   # entrada de reader, por lo tanto lo que escriba writer lo va a
   # leer reader al reves el recorrido es asi:
   # mensaje -> entra a writer -> lo invierte -> lo envia a la salida -> entra a reader
   def test():
      in_queue =  Queue.Queue()
      out_queue =  Queue.Queue()
      reader = Reader(out_queue)
      writer = Writer(in_queue, out_queue)

      reader.start()
      writer.start()

      in_queue.put('buenas')
      in_queue.put('como va')
      in_queue.put('quit')

   if __name__ == '__main__':
      test()

En este ejemplo, los hilos estan dormidos y solo se despiertan cuando hay algo que hacer, lo hacen y se vuelven a bloquear.

  Usando esta estrategia nos queda el hilo principal libre para hacer lo que queramos (por ejemplo el main loop de un widget toolkit) el cual no se vera bloqueado por el trabajo realizado por los hilos.

Mas info sobre el modulo Queue: https://docs.python.org/current/library/queue.html

Asynchronous Queue a partir de Python 3.4:  https://docs.python.org/current/library/asyncio-queue.html

la salida obtenida ejecutando el archivo:

::

   escrito buenas
   leido saneub
   escrito como va
   leido av omoc
   writer se va!
   reader se va!

