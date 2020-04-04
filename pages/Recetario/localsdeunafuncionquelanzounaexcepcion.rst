.. title: Locals De Una Funcion Que Lanzo Una Excepcion


ejemplo de como obtener las variables locales a la función que lanzo una excepion.

En realidad son los locals de la funcion llamada.

Lo uso para pasarle los locals de la funcion a un template de django desde un decorador.

.. code-block:: python

    import inspect

    def fun():
        a, b = 1, "dos"

        raise Exception("hi!")

    try:
        fun()
    except Exception, error:
        fun_frame = inspect.trace()[1][0]
        print "locals in fun: ", fun_frame.f_locals
        del fun_frame

