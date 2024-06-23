.. title: Obtener Sensacion Termica


* Cómo obtener la Sensación Térmica o Temperatura Aparente usando Python, ejemplo simple.

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    import math

    t= 20 # Temperatura
    v = 20 # Velocidad del Viento
    st = 33 + (t- 33)*(0.474 + 0.454 * math.sqrt((v))-0.0454*v)
    print st


**Ejemplo:**

.. code-block:: bash

    /usr/bin/env python st.py
    12.24


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

