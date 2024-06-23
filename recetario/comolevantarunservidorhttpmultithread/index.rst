.. title: Como Levantar Un Servidor Http Multithread


Este ejemplo muestra cómo levantar un servidor web en Python sirviendo el contenido del directorio actual utilizando threads para manejar las solicitudes.

Para usarlo, simplemente hay que llamar a este módulo desde la línea de comando, si se llamara test.py entonces correr "python test.py"

.. code-block:: python

    import SocketServer
    import BaseHTTPServer
    import SimpleHTTPServer

    class Server(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
        pass

    if __name__ == '__main__':
        SimpleHTTPServer.test(ServerClass=Server)

