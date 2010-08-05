=!Web2Py =

== Introducción ==

!Web2Py es un framework WEB (marco de trabajo / herramienta de desarrollo) de muy fácil uso y aprendizaje, completamente funcional para crear aplicaciones web 2.0 de manera totalmente interactiva (diseño y programación por el navegador web!).  
Incluye las últimas tecnologías de una forma simple y clara (javascript, ajax, css, etc.). 

 * Sitio Oficial: http://www.web2py.com/
 * Sitio en Español: http://www.web2py.com.ar/

== Como instalar y ejecutar Web2Py: ==

Web2py viene con baterías incluidas, por lo que su instalación es muy simple:

=== Windows ===

Pasos:
 * Descargar el paquete todo-en-uno [[http://www.web2py.com/examples/static/web2py_win.zip|web2py_win.zip]] 
 * Descomprimirlo
 * Ejecutar (doble click) en `web2py.exe` 

=== Linux (Debian y derivados) ===

Pasos:
 * Instalar las dependencias (python y conectores a la base de datos)
 * Descargar el código fuente [[http://www.web2py.com/examples/static/web2py_src.zip|web2py_src.zip]] 
 * Descomprimir
 * Iniciar `web2py.py`

Ejemplo:
{{{#!code bash
sudo apt-get install python psycopg2
wget http://www.web2py.com/examples/static/web2py_src.zip
unzip web2py_src.zip
cd web2py
python web2py.py
}}}

== Arranque ==

Al ejecutar web2py nos mostrará la pantalla de bienvenida:

{{attachment:bienvenida.png}}

Web2py trae incorporado un servidor web para desarrollo, para iniciarlo deberemos elegir y ingresar una contraseña de administrador propia (por ej. 'abc') y presionar `start`:

{{attachment:servidor.png}}

== Bienvenida ==

Al iniciar, web2py lanzará un explorador con la página de [[http://127.0.0.1:8000/welcome/default/index|bienvenida]] predeterminada:

{{attachment:welcome.png}}

== Interfaz Administrativa ==

Allí podremos ver los ejemplos interactivos, documentación y lo más importante, empezar a crear y editar nuestras aplicaciones web, yendo a la  [[http://127.0.0.1:8000/admin/||interfaz administrativa]]:

{{attachment:admin-login.png}}

En dicha página, ingresar la contraseña previamente escogida en los pasos previos, y se abrirá un índice con las aplicaciones instaladas en esta instancia:

{{attachment:admin-site.png}}

Por ejemplos, podemos ingresar a la aplicación [[http://127.0.0.1:8000/admin/default/design/welcome|welcome]] (bienvenida), presionando el enlace EDIT (editar):

{{attachment:admin-design.png}}

Y allí, por ejemplo, podemos modificar el código fuente del controlador principal ([[http://127.0.0.1:8000/admin/default/edit/welcome/controllers/default.py|default.py]] presionando en el link edit (editar):

{{attachment:admin-edit.png}}
