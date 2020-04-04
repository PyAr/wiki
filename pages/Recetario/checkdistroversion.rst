.. title: CheckDistroVersion


Chequea la versión de la Distribución Linux, y actúa en función de eso. Utiliza el módulo platform_

::

    import platform

    osInfo = ('Ubuntu', '10.10', 'maverick')
    sysInfo = platform.linux_distribution()

    if osInfo == sysInfo:
        print(" OK ")
        # Aca va que hacer si esta OK
    else:
        print(" ERROR ")
        # Aca va que hacer si la version no es correcta


.. ############################################################################

.. _platform: http://www.python.org/doc//current/library/platform.html
