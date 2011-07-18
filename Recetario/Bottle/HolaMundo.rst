= Hola Mundo Bottle =

 * Como hacer un hola mundo en Bottle, ejemplo simple.

{{{
#!code python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run
@route('/')
def index():
    return 'Hola Mundo!'
run()
}}}

'''Ejemplo:'''

{{{
juan@wind:~$ /usr/bin/env python holamundo.py
Bottle server starting up (using WSGIRefServer())...
Listening on http://127.0.0.1:8080/
Use Ctrl-C to quit.

localhost.localdomain - - [18/Jul/2011 18:22:09] "GET / HTTP/1.1" 200 11
localhost.localdomain - - [18/Jul/2011 18:22:09] "GET /favicon.ico HTTP/1.1" 404 687
^C
juan@wind:~$
}}}

~-''Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.''-~

~-''Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.''-~
