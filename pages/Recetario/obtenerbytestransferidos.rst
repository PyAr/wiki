
Obtener la cantidad de Bytes transferidos
=========================================

Imprime la cantidad de datos en Bytes transferidos en la interfaz indicada.

::

   interface= 'eth0'
   for line in open('/proc/net/dev', 'r'):
       if interface in line:
           data = line.split('%s:' % interface)[1].split()
           rx_bytes, tx_bytes = (data[0], data[8])
   print '%s bytes received' % rx_bytes
   print '%s bytes sent' % tx_bytes

Ejemplo:

::

   juan@maverick:~$ /usr/bin/env python prueba.py
   2066696798 bytes received
   169266445 bytes sent

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas.html
