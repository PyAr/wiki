.. title: La cuestión


Al efectuar búsquedas en Internet, estamos acostumbrados a que no se distinga entre mayúsculas y minúsculas, y que se ignoren los acentos de las palabras. Para hacer esto en Python, antes que nada necesitamos una función que convierta los strings a la forma especificada. Una que haga lo siguiente:

::

   >>> normalizar_string(u'Mónica Viñao')
   'monica vinao'

Usando unicodedata.normalize
----------------------------

Unicode define equivalencias entre caracteres, o secuencias de caracteres, de los distintos estándares (ver http://en.wikipedia.org/wiki/Unicode_equivalence). Y define formas normales a las que podemos llevar un texto. Entonces podemos lograr la transformación que queremos haciendo una normalización. Los caracteres se descomponen, ignorando la parte que no es ASCII:

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from unicodedata import normalize

    def normalizar_string(unicode_string):
        u"""Retorna unicode_string normalizado para efectuar una búsqueda.

        >>> normalizar_string(u'Mónica Viñao')
        'monica vinao'

        """
        return normalize('NFKD', unicode_string).encode('ASCII', 'ignore').lower()

    if __name__ == "__main__":
        import doctest
        doctest.testmod()


¡Gracias a Martin Conte Mac Donell!

.. _unicode: /unicode
