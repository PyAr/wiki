.. title: Comobajartodoslosbuffersaldisco

  **Cuidado!** Esta receta no se aplica en todos los casos...

Cerrar correctamente tu programa
================================

Mejores Prácticas *(o Best Practice)* de cómo debería cerrarse tu programa de una manera linux-friendly, para prevenir corrupción/pérdida de datos.

**Disclaimer:** Esto es más relacionado al OS que a Python en si, válido para los SO tipo Unix, pero es importante para lograr una aplicacion que funcione como debe.

.. code-block:: python

   import os

   # Tu programa debe invocar este comando y luego cerrarse.
   os.system('sync')

 **¿Por qué?:**  En Linux los datos que teóricamente deberían estar escritos en el disco, no siempre lo estan en la realidad, por un período de tiempo variable de unos segundos podrían mantenerse en RAM. El tiempo en segundos varía según las configuraciones del Kernel.

**Ejemplo:**

.. code-block:: bash

   cat /proc/sys/vm/dirty_writeback_centisecs
   500

Esto significa que ningun dato se escribirá a disco realmente durante 5 Segundos, esto parece poco, pero en algunos casos como Notebooks o equipos con UPS este valor puede estar en 1500, es decir 15 segundos *(lo que es un montón en Infomática)*. No piensen que este valor se puede reducir, esto tendría al Kernel contantemente escribiendo la RAM al disco. Esto es más notable en EXT4 con Extents activados. Alternativamente al ejemplo puedes agregar que detecte que OS es y ejecutar o no sync, también puede solucionar algunos "Segmentation Fault" misteriosos al cerrar tu programa.

En mi Notebook, obtengo este resultado: 

(Si escribo un programa que no invoca a sync puedo perder 10 segundos de datos).

.. code-block:: bash

   juan@wind:~$ cat /proc/sys/vm/dirty_writeback_centisecs
   1000

