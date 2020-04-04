.. title: Mini Galeria de Imagenes Bottle


* Como hacer una Mini Galeria de Imagenes en Bottle_, ejemplo basado en el Hola Mundo.

Usa Bottle_ para servir 1 pagina incrustada en la propia aplicacion, la misma desplega HTML, CSS y Js.

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
    GALLERY = """
    <!DOCTYPE HTML>
    <html>
      <head>
        <title>PYTHON-BOTTLE DEMO</title>
        <link rel="shortcut icon" href="http://python.org.ar/images/pyar.ico" type="image/x-icon"/>
        <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
        <style type="text/css"> body { background-color: black; } </style>
    <script language="JavaScript">
    <!--
    if (document.images) {
        demo1 = new Image();
        demo1.src = "http://www.gstatic.com/webp/gallery/5.webp";
        demo2 = new Image();
        demo2.src = "http://www.gstatic.com/webp/gallery/2.webp";
        demo3 = new Image();
        demo3.src = "http://www.gstatic.com/webp/gallery/3.webp";
        demo4 = new Image();
        demo4.src = "http://www.gstatic.com/webp/gallery/4.webp";
    }
    function timeimgs(numb) {  // Reusable timer
        thetimer = setTimeout("imgturn('" +numb+ "')", 1000);
    }
    function imgturn(numb) {
        if (document.images) {
            if (numb == "4") {
                document["demo"].src = eval("demo4.src");
                timeimgs('1');
            }
        else {
            document["demo"].src = eval("demo" + numb + ".src");
            timeimgs(numb = ++numb);
            }
        }
    }
    // -->
    </script>
    </head>
    <body onload="timeimgs('1');">
    <div align="center">
        <img src="http://www.gstatic.com/webp/gallery/1.webp" name="demo" width="1024" height="768" alt="demo" title="PYTHON-BOTTLE DEMO">
    </div>
    </body>
    </html>
    """
    #
    @route('/')
    def index():
        return GALLERY

    # Ejemplo de uso de bottle.request para mostrar tu direccion ip
    @route('/tu_ip') # ingresando a esa URL devuelve tu IP
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


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

.. ############################################################################

.. _Bottle: http://bottlepy.org

