.. title: Como Levantar Un Servidor Http Multithread


este ejemplo muestra como levantar un servidor web en python sirviendo el contenido del directorio actual utilizando threads para manejar las solicitudes.

para usar simplemente hay que llamar a este modulo desde la linea de comando, si se llamara test.py entonces correr "python test.py"

::

    import SocketServer
    import BaseHTTPServer
    import SimpleHTTPServer

    class Server(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
        pass

    if __name__ == '__main__':
        SimpleHTTPServer.test(ServerClass=Server)

