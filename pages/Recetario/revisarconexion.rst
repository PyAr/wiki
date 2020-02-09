
Revisar Conexion
================

como revisar si tenemos conexion a internet

Para no depender de programas externos (tené en cuenta que, por ejemplo, ping seguramente no recibe los mismos parámetros en Linux que en Windows), podés intentar abrir un socket a algún servidor externo y enviar algo.

Si el DNS resuelve podés chequear con socket.gethostbyname('google.com'). 

::

   import socket
   try:
       socket.gethostbyname('google.com')
       c = socket.create_connection(('google.com', 80), 1)
       c.close()
   except socket.gaierror:
       print "DNS error"
   except socket.error:
       print "Connection error"

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas.html
