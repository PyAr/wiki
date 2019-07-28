
Validar CUIT
------------

Descripción
:::::::::::

*validar_cuit(cuit)* es una función a la que se le pasa un CUIT/CUIL (cadena '00-00000000-0') y devuelve True si el CUIT es válido (tiene la longitud y formato correcto, y su digito verificador esta ok).

El CUIT/CUIL es el código único de de identificación tributaria/laboral, que se le asigna a cada persona física o jurídica (sociedades) alcanzadas por el sistema impositivo argentino.

**Aclaración**: que el CUIT sea válido no quiere decir que la persona titular exista y esté habilitada por los organismos correspondientes.

Siempre se debe verificar la vigencia del CUIT en la página de la AFIP (Administración Federal de Ingresos Públicos). Por el momento es una página web, quizas en un futuro ofrezcan un servicio web para automatizar el proceso. Tambien es posible bajarse un padrón (archivo de texto plano), tarea para otra receta |smile|

Ejemplos:
:::::::::

::

    >>> validar_cuit("00-00000000-0")
    True
    >>> validar_cuit("00-00000000-1")
    False


Código:
:::::::

::

    def validar_cuit(cuit):
        # validaciones minimas
        if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
            return False

        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        cuit = cuit.replace("-", "") # remuevo las barras

        # calculo el digito verificador:
        aux = 0
        for i in xrange(10):
            aux += int(cuit[i]) * base[i]

        aux = 11 - (aux - (int(aux / 11) * 11))

        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9

        return aux == int(cuit[10])


Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. _marianoreingart: /pages/marianoreingart
.. _categoryrecetas: /pages/categoryrecetas
