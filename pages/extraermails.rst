
Extraer direcciones de email de un texto
----------------------------------------

Código
::::::

::

    >>> import re
    >>> mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
    >>> mailsrch.findall(texto)


El código anterior devuelve una lista de strings, donde cada string es una dirección de email. El texto original puede contener basura como espcios, comas u otros caracteres.

Autor
:::::

JuanjoConti_

Fuente
::::::

http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

.. ############################################################################


.. _juanjoconti: /juanjoconti
