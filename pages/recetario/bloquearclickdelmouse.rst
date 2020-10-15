.. title: Bloquear Click Del Mouse


Cómo bloquear el click izquierdo del mouse cuando se tipea en el teclado,
usando Python, en Linux, ejemplo simple, requiere Privilegios elevados en el equipo.

.. note:

    Usar con atencion que tu GUI no requiera clicks del mouse, ten en cuenta las personas con discapacidades.

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import os
    import time
    #
    kb = file('/dev/console')
    while True:
        os.system('xmodmap -e "pointer = default"') # Aca lo activamos
        kb.read(3)
        os.system('xmodmap -e "pointer = 0 2 3"') # Aca lo desactivamos
        time.sleep(0.5) # duerme, prueba reducir este valor para mas reaccion


Ejemplo:
--------

.. code-block:: console

    sudo /usr/bin/env python blockclick.py


.. note::

    Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.

    Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.
