#format rst

Web2Py
======

Introducción
------------

Web2Py es un framework WEB (marco de trabajo / herramienta de desarrollo) de muy fácil uso y aprendizaje, completamente funcional para crear aplicaciones web 2.0 de manera totalmente interactiva (diseño y programación por el navegador web!).   Incluye las últimas tecnologías de una forma simple y clara (javascript, ajax, css, etc.). 

* Sitio Oficial: http://www.web2py.com/

* Sitio en Español: http://www.web2py.com.ar/

* Grupo de usuarios en español: http://groups.google.com/group/web2py-usuarios

* Documentación Principal (libro publicado en html de acceso gratuito): http://www.web2py.com/book

* Hoja de referencia rápida: `attachment:web2py-referencia.pdf`_web2py-referencia.pdf`attachment:None`_

Como instalar y ejecutar Web2Py:
--------------------------------

Web2py viene con baterías incluidas, por lo que su instalación es muy simple:

Windows
~~~~~~~

Pasos:

* Descargar el paquete todo-en-uno `web2py_win.zip`_ 

* Descomprimirlo

* Ejecutar (doble click) en ``web2py.exe`` 

Linux (Debian y derivados)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pasos:

* Instalar las dependencias (python y conectores a la base de datos)

* Descargar el código fuente `web2py_src.zip`_ 

* Descomprimir

* Iniciar ``web2py.py``

Ejemplo:

::

   .. raw:: html
      <span class="line">sudo apt-get install python psycopg2
      </span><span class="line">wget http://www.web2py.com/examples/static/web2py_src.zip
      </span><span class="line">unzip web2py_src.zip
      </span><span class="line"><span class="nb">cd </span>web2py
      </span><span class="line">python web2py.py
      </span>

Recorrida
---------

A continuación mostraremos una breve recorrida sobre las características principales de web2py.

**Nota**: Los links solo funcionan si está web2py funcionando en la máquina local, puerto 8000 (configuración por defecto).

Arranque
~~~~~~~~

Al ejecutar web2py nos mostrará la pantalla de bienvenida:

`attachment:bienvenida.png`_

Web2py trae incorporado un servidor web para desarrollo, para iniciarlo deberemos elegir y ingresar una contraseña de administrador propia (por ej. 'abc') y presionar ``start``:

`attachment:servidor.png`_

Bienvenida
~~~~~~~~~~

Al iniciar, web2py lanzará un explorador con la página de bienvenida_ predeterminada:

`attachment:welcome.png`_

Interfaz Administrativa
~~~~~~~~~~~~~~~~~~~~~~~

Allí podremos ver los ejemplos interactivos, documentación y lo más importante, empezar a crear y editar nuestras aplicaciones web, yendo a la  http://127.0.0.1:8000/admin/:

`attachment:admin-login.png`_

En dicha página, ingresar la contraseña previamente escogida en los pasos previos, y se abrirá un índice con las aplicaciones instaladas en esta instancia:

`attachment:admin-site.png`_

Por ejemplos, podemos ingresar a la aplicación welcome_ (bienvenida), presionando el enlace EDIT (editar):

`attachment:admin-design.png`_

Y allí, por ejemplo, podemos modificar el código fuente del controlador principal (`default.py`_ presionando en el link edit (editar):

`attachment:admin-edit.png`_

Administración de Base de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web2py viene con una controlador llamado AppAdmin_ que sirve para consultar, modificar e importar/exportar los datos de nuestra aplicación. Se ingresa por la interfaz administrativa, en el link `Database Administration`_:

`attachment:appadmin-index.png`_

Allí podemos agregar un nuevo registro, por ejemplo en la tabla usuarios (insert new record):

`attachment:appadmin-insert.png`_

Y también es posible realizar consultas y actualizaciones:

`attachment:appadmin-query.png`_

.. ############################################################################

.. _web2py_win.zip: http://www.web2py.com/examples/static/web2py_win.zip

.. _web2py_src.zip: http://www.web2py.com/examples/static/web2py_src.zip

.. _bienvenida: http://127.0.0.1:8000/welcome/default/index

.. _welcome: http://127.0.0.1:8000/admin/default/design/welcome

.. _default.py: http://127.0.0.1:8000/admin/default/edit/welcome/controllers/default.py

.. _AppAdmin: ../AppAdmin

.. _Database Administration: http://127.0.0.1:8000/welcome/appadmin/

