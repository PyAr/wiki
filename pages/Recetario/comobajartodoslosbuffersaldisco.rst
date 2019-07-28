
  **Cuidado!** Esta receta no se aplica en todos los casos...

Cerrar Correctamente Tu Programa
================================

Mejores Practicas *(o Best Practice)* de como deberia cerrarse tu programa de una manera linux-friendly, para prevenir corrupcion/perdida de datos.

**Disclaimer:** Esto es mas relacionado al OS que a Python en si, valido para los SO tipo Unix, pero es importante para lograr una aplicacion que funcione como debe.

::

   import os

   # Tu programa debe invocar este comando y luego cerrarse.
   os.system('sync')

 **Por que?:**  En Linux los datos que teoricamente deberian estar escritos en el disco, no siempre lo estan en la realidad, por un periodo de tiempo variable de unos segundos podrian mantenerse en RAM, el tiempo en segundos varia segun las configuraciones del Kernel.

**Ejemplo:**

::

   cat /proc/sys/vm/dirty_writeback_centisecs
   500

Esto significa que ningun dato se escribira a disco realmente durante 5 Segundos, esto parece poco, pero en algunos casos como Notebooks o equipos con UPS este valor puede estar en 1500, es decir 15 segundos *(lo que es un monton en Infomatica)*, no piensen que este valor se puede reducir, esto tendria al Kernel contantemente escribiendo la RAM al disco,  esto es mas notable en EXT4 con Extents activados, alternativamente al ejemplo puedes agregar que detecte que OS es y ejecutar o no sync, tambien puede solucionar algunos "Segmentation Fault" misteriosos al cerrar tu programa.

En mi Notebook, obtengo este resultado, si escribo un programa que no invoca a sync puedo perder 10 segundos de datos:

::

   juan@wind:~$ cat /proc/sys/vm/dirty_writeback_centisecs
   1000

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas
