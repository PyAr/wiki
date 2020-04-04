.. title: Matrix Python Toy


Efecto "The Matrix" en linea de comandos, con modificacion es util de Screen Saver o Screen Lock

.. code-block:: python

   import os, time, random, sys

   class message(str):
       def __new__(cls, text, speed):
           self = super(message, cls).__new__(cls, text)
           self.speed = speed
           self.y = -1*len(text)
           self.x = random.randint(0, display().width)
           self.skip = 0
           return self

       def move(self):
           if self.speed > self.skip:
               self.skip += 1
           else:
               self.skip = 0
               self.y += 1

   class display(list):
       def __init__(self):
           self.height, self.width = [int(x) for x in os.popen('stty size', 'r').read().split()]
           self[:] = [' ' for y in xrange(self.height) for x in xrange(self.width)]

       def set_vertical(self, x, y, string):
           string = string[::-1]
           if x < 0:
               x = 80 + x
           if x >= self.width:
               x = self.width-1
           if y < 0:
               string = string[abs(y):]
               y = 0
           if y + len(string) > self.height:
               string = string[0:self.height - y]
           if y >= self.height:
               return
           start = y*self.width+x
           length = self.width*(y+len(string))
           step = self.width

           self[start:length:step] = string

       def __str__(self):
           return ''.join(self)

   i_message = raw_input("Input a message: ")
   messages = [message(i_message, random.randint(1, 5))]
   for t in xrange(1000):
       messages.append(message(i_message, random.randint(1, 5)))
       d = display()
       for text in messages:
           d.set_vertical(text.x, text.y, text)
           text.move()
       sys.stdout.write(str(d))
       sys.stdout.flush()
       del d
       time.sleep(0.1)

Ejemplo:

.. code-block:: bash

   juan@maverick:~$ /usr/bin/env python matrix.py
   Input a message: PYTHON

