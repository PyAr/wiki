
Obtener ip Publica
==================

* Como obtener la ip Publica, usando Python, ejemplo simple.

**Nota:** *Que tengas direccion ip publica no implica que tengas conectividad.*

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- 
    import urllib
    ip = urllib.urlopen('http://automation.whatismyip.com/n09230945.asp').read() # esta URL puede ser reemplazada con otra que preste similar servicio
    print ip


**Ejemplo:**

::

   sudo /usr/bin/env python getip.py
   190.139.27.XXX

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

