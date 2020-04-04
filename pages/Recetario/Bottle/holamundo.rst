.. title: Hola Mundo Bottle


* Como hacer un hola mundo en Bottle_, ejemplo simple.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from bottle import route, run
    @route('/')
    def index():
        return 'Hola Mundo!'
    run()


**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python holamundo.py
   Bottle server starting up (using WSGIRefServer())...
   Listening on http://127.0.0.1:8080/
   Use Ctrl-C to quit.

   localhost.localdomain - - [18/Jul/2011 18:22:09] "GET / HTTP/1.1" 200 11
   localhost.localdomain - - [18/Jul/2011 18:22:09] "GET /favicon.ico HTTP/1.1" 404 687
   ^C
   juan@wind:~$

-------------------------



* Mejorando nuestro  hola mundo en Bottle_, ejemplo mas completo, ideal para Plantilla para una App nueva.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    from bottle import route
    from bottle import run
    from bottle import redirect
    from bottle import debug
    from bottle import error
    from bottle import request
    from bottle import abort
    import os
    #
    @route('/')
    def index():
        return 'Hola Mundo!'

    # Ejemplo de uso de bottle.request para mostrar tu direccion ip
    @route('/tuip') # ingresando a esa URL devuelve tu IP
    def show_ip():
        ip = request.environ.get('REMOTE_ADDR')
        return ip

    # Ejemplo de uso de bottle.error para el 404, la pagina no existe
    @error(404)
    def mistake404(code): # Usando HTML directamente, de ejemplo.
        return '<title>bottle app</title><br><b>ERROR 404:la pagina no existe.</b>'

    # Ejemplo de uso de bottle.abort para URL no permitida, error 401
    @route('/restricted')
    def restricted():
        abort(401, 'ERROR 401:URL no permitida.')

    # Ejemplo de Redireccion bottle.redirect de URL, por URL incorrecta
    @route('/index.php') # si va a index.php
    def wrong():
        redirect("/") # enviarlo a "/"

    ###############################################################################

    # Ejecucion de Main
    def main():
        debug(True)# True para desarrollo, False para Produccion
        #
        # Por que es esto?: Puerto <1024 requiere Privilegios elevados
        if os.geteuid()==0: # root check
            run(host='0.0.0.0', port=80, reloader=True)
        else:
            run(host='127.0.0.1', port=8080, reloader=True)

    if __name__=="__main__":
        main()


*Nota: Hay mas Features en* Bottle_*, pero eso es suficiente para un Hola Mundo completo y didactico.*

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

.. ############################################################################

.. _Bottle: http://bottlepy.org

