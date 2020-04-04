.. title: Web Server Gateway Interface


WSGI es una interface simple y universal entre los servidores web y las aplicaciones web o frameworks (ver más en  `PEP 333`_)

WSGI es similar a la especificación Java Servlet o ASP/ASP.NET. En general, es mucho más simple que dichas especificaciones, y se basa en el estandard CGI con mejoras "pitónicas" para hacerla reentrante, persistente, etc.

Resumen de la Especificación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Del lado de la aplicación, se especifica un punto de entrada (objeto, método, función), con dos parámetros: las variables de entorno (``environ`` y la función para iniciar la respuesta ``start_response(status,response_headers)`` que envía el estado y los encabezados), y debe devolver un iterable con los datos para enviar al cliente.

* Del lado del servidor, se invoca la aplicación por cada pedido que recibe del cliente HTTP, con las variables de entorno establecidas (estilo CGI)

Ejemplo
~~~~~~~

::

   # Aqui va mi 'Hola PyAr!, pero con WSGI, una maravilla de Python.

   from wsgiref.simple_server import make_server

   def hello(environ, start_response):
       start_response('200 OK',[('Content-type','text/plain')])
       return ['Hola PyAr!']

   httpd = make_server('',8000, hello).serve_forever()

(copiado de un mail "hello-word" de la lista)

Variables de entorno (diccionario {{{environ}}})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El diccionario ``environ`` que se recibe con cada pedido HTTP, contiene las variables estándard de la especificación CGI, entre ellas:

* REQUEST_METHOD: método "GET", "POST", tec.

* SCRIPT_NAME : la parte inicial de la "ruta", que corresponde a la aplicación

* PATH_INFO: la segunda parte de la "ruta", determina la "ubicación" virtual dentro de la aplicación

* QUERY_STRING: la porción de la URL que sigue al "?", si existe

* CONTENT_TYPE, CONTENT_LENGTH de la petición HTTP

* SERVER_NAME, SERVER_PORT, que combinadas con SCRIPT_NAME y PATH_INFO dan la URL

* SERVER_PROTOCOL: la versión del protocolo ("HTTP/1.0" or "HTTP/1.1")

* Variables HTTP

Configuración apache + mod_python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mod_python tiene varios handlers o "controladores" (ver `documentación`_):

* Handler PSP: utilizado para procesar documentos .psp con código python y html mezclado (similar a PHP)

* Handler CGI: emula el entorno CGI (no confundir con WSGI). No es reentrante ni persistente, y es el método más lento para ejecutar scripts web, pero a su vez es históricamente "compatible" con scripts viejos.

* Handler Publisher: es un poco mas de "alto nivel". En general, se usaría si uno quiere hacer una aplicación sencilla, con las url mapeadas automáticamente a funciones, etc.

* Handler propio: más rapido, pero a costa de tener que programar a mas "bajo nivel" (directamente con las interfaces de apache). Aplicaciones mas avanzadas que requieren un mayor control sobre las url, encabezados, etc., usan handlers propios (ejemplo: trac, moin, etc.):

Igualmente, estos Handlers no son compatibles con WSGI, por eso no recomendaría usar ninguno de ellos directamente, sino a través del wrapper WSGI (con ModPythonGateway_) que es un handler "propio" que traduce las peticiones al estandar WSGI.  Es algo mucho mas estandar, valga la redundancia, y el día de mañana se puede usar cualquier servidor compatible con python, no solo apache.

Además, puede utilizarse directamente mod_wsgi (ver siguiente sección).

Ejemplos de configuración (tanto en /etc/apache2/... en un archivo .htaccess en el mismo directorio):

::

     # handler Publisher:
     #  se ejecutará cualquier archivo .py del directorio, llamando a la función de la url:
     #  http://www.mysite.com/hello.py/say  ejecutara el script hello.py, funcion say
     <Directory /var/www/html/python/>
         SetHandler mod_python
         PythonHandler mod_python.publisher
         PythonDebug On
     </Directory>

     # Handler PSP:
     #  se ejecutará cualquier archivo .psp (código python embebido en texto html)
     <Directory /var/www/html/psp/>
        AddHandler mod_python .psp
        PythonHandler mod_python.psp
     </Directory>

     # Handler CGI:
     #  se ejecutará los scripts .py (scripts normales de python) simil linea de comandos
     <Directory /var/www/cgi-bin/>
        SetHandler mod_python
        PythonHandler mod_python.cgihandler
        Options ExecCGI
     </Directory>

     # handler propio:
     #  se ejecuta el archivo myscript.py función handler(req)
     <Directory /mywebdir>
          AddHandler mod_python .py
          PythonHandler myscript
          PythonDebug On
     </Directory>

Para configurar una aplicación wsgi en mod_python:

::

   SetHandler python-program
   PythonHandler modpython_gateway::handler
   PythonOption wsgi.application app::WSGIApp
   PythonPath "['C:/Archivos de programa/Apache Software Foundation/Apache2.2/htdocs/app'] + sys.path"
   PythonOption SCRIPT_NAME /app

Descripción:

* Se habilita el handler propio

* Se establece el handler a ejecutar (en este caso, el wrapper wsgi)

* Se especifican las opciones de la aplicación wsgi (app es el nombre de archivo, WSGIApp es el punto de entrada)

* Se agrega el script de la aplicación al path para poder ejecutarla

* Se establece el nombre del script a mostrar (sino, en ocasiones, apache puede informar mal o de manera distinta el nombre de script con problemas en el ruteo de urls)

Configuración apache + mod_wsgi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para usar WSGI directamente desde apache, existe mod_wsgi, que es un módulo mas reciente, totalmente codificado en C para una mejor performance y estabilidad, que simplifica y resuelve las carencias de mod_python:

Ejemplo 1: ejecutar en el mismo proceso que apache (no independiente, estilo mod_python/php/etc.). En este caso se mapea la url /app al script wsgi app.py:

::

   WSGIScriptAlias /app /usr/local/apache/app.py

Ejemplo 2: ejecutar en un proceso (interprete) independiente con un usuario arbitrario diferente de apache (estilo FastCGI, mejorando seguridad y performance):

::

   WSGIDaemonProcess site-1 user=trac group=trac threads=25
   WSGIScriptAlias /site-1 /usr/local/apache/app.py
   <Directory /usr/local/apache>
   WSGIProcessGroup site-1
   WSGIApplicationGroup %{GLOBAL}
   </Directory>

Configuración lighttpd + wsgi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://cleverdevil.org/computing/24/python-fastcgi-wsgi-and-lighttpd

* http://svn.saddi.com/py-lib/trunk/fcgi.py (en realidad es un handler FastCGI compatible con WSGI)

Ejemplo "avanzado"
~~~~~~~~~~~~~~~~~~

Con respecto a la diferencia con PHP/PSP, la mayoría de las aplicaciones web en python tienen un solo punto de entrada (un solo .py), que funciona como "despachador", dependiendo de que url te piden, se llama a una función o a otra (generalmente se usa la variable de entorno SCRIPT_NAME o similar, o directamente usar cherrypy, django, turbogears, etc., para que ruteen las peticiones a las clases/funciones que correspondan)

Ejemplo muy simple con WSGI:

::

   def App(environ, start_response):
           "Punto de entrada WSGI"
           if environ['SCRIPT_NAME'].endswith("xxxx"):
                   respuesta_html = xxxx(environ)
           elif environ['SCRIPT_NAME'].endswith("yyyy"):
                   respuesta_html = yyyy(environ)
           else:
                   respuesta_html = "<html><body><p>la url es
   inválida!</p></body></html>"
           start_response ("200 Ok", [('Content-Type','text/html')])
           yield respuesta_html

Entonces, si te llaman www.tuservidor.com/aplicacion/xxxx haces una cosa (xxxx), mientras que si llaman a www.tuservidor.com/aplicacion/yyyy haces otra (yyyy). En comparación con php/psp, sería como llamar a www.tuservidor.com/aplicacion.psp?funcion=xxxx o www.tuservidor.com/aplicacion.psp?funcion=yyyy.

Esto es un poco mas difícil de entender, pero a la larga es mas flexible porque  no te limita a tener un archivo (estructura "física") para cada dirección  (estructura "lógica"), limpiando un poco la url de extensiones .py, signos  de interrogación, etc. , haciéndolas mas fáciles de entender para el  usuario.

.. ############################################################################

.. _PEP 333: http://www.python.org/dev/peps/pep-0333/

.. _documentación: http://www.modpython.org/live/current/doc-html/

.. _ModPythonGateway: http://www.aminus.net//wiki/ModPythonGateway

