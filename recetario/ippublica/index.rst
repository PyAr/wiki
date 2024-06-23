.. title: Obtener ip Publica


* Cómo obtener la IP Pública, usando Python, ejemplo simple.

**Nota:** *Que tengas dirección IP pública no implica que tengas conectividad.*

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import urllib
    ip = urllib.urlopen('http://automation.whatismyip.com/n09230945.asp').read() # esta URL puede ser reemplazada con otra que preste similar servicio
    print ip


**Ejemplo:**

.. code-block:: python

   sudo /usr/bin/env python getip.py
   190.139.27.XXX

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

