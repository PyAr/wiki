.. title: Reverse (a.k.a. "esrever")


* Una humilde funcion para dar vuelta los caracteres usando Python, letras o numeros, ejemplo simple.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    def reverse(this):
        return ' '.join(''.join(list(things)[::-1]) for things in this.split())
    inputz = raw_input()
    print reverse(inputz)


**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python reverse.py
   import antigravity
   tropmi ytivargitna

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

