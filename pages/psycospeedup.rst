.. title: PsycoSpeedUp


Acelera las aplicaciones en Python (JIT), disponible para 32bit.

::

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    try:
        import psyco  # Speed Up :)
        psyco.full()
    except ImportError:
        print(" ")
        print(" No PYTHON-PSYCO avaliable, this application will run slower... ") # imprime este mensaje si Psyco no esta disponible
        print(" ")
        pass
    # la aplicacion continuara funcionando si psyco no esta disponible, asi mismo continuara si es 64bit
    ########################## imports goes here
    # from foo import bar

