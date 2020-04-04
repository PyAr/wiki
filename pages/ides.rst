.. title: Comparación de entornos de desarrollo


En esta pagina se pretende mostrar una lista de las herramientas que pueden ser usadas para desarrollar código en python, van desde las soluciones mas amistosas con los principiantes, hasta editores simples con soporte para el lenguaje.

IDEs
----

Eclipse + pydev
~~~~~~~~~~~~~~~

Pydev es un plugin que permite a los usuarios usar Eclipse para el desarrollo de Python y Jython, haciendo de eclipse una IDE de primera clase para desarrollar python. Este plugin viene con muchas características, como por ejemplo complesión de código, resaltado de sintaxis, analizador de sintaxis, refactor, debug y muchos mas.

http://pydev.sourceforge.net/ http://www.eclipse.org/

Netbeans (nbpython)
~~~~~~~~~~~~~~~~~~~

nbpython es una extensión de netbeans que permite utilizar esta IDE como entorno para desarrollos en python, algunas de sus características son el resaltado de sintaxis, complesión de código, soporte para proyectos python soporte para jython, soporte para pyunit, debugger, administración de versiones, manejo de la librería estándar, ejecución de scripts python etc.

https://nbpython.dev.java.net/ http://www.netbeans.org/

SPE IDE
~~~~~~~

Entorno de desarrollo multiplataforma para python

http://pythonide.blogspot.com/

Eric
~~~~

Eric is una IDE para python y ruby, escrita en python. Esta basada en Qt, integrando el control de edición scintilla. Esta diseñado para ser usable ya sea como editor para pequeños scripts como así también para administración de proyectos profesionales. Eric provee un sistema de plugins que permite ser extendido fácilmente.

http://www.die-offenbachs.de/eric/index.html

Komodo Edit
~~~~~~~~~~~

Komodo Edit es un editor open source para expertos en lenguajes dinámicos.

http://www.activestate.com/Products/komodo_ide/komodo_edit.mhtml

Geany
~~~~~

Geany es un editor de texto que usa el toolkit GTK2 toolkit con funciones básicas de un entorno de desarrollo integrado. Es desarrollado para proveer de una IDE pequeña y rápida, que tenga pocas dependencias de otros paquetes. Soporta múltiples tipos de archivo y tiene algunas características muy interesantes.

opinion de un nuevo usuario de geany:

::

   <achuni>: no es muy featurefull
   <achuni>: (hasta hace una semana yo usaba gedit)
   <achuni>: pero tiene todo lo que yo necesitaba
   <achuni>: syntax highlighting
   <achuni>: line numbering
   <achuni>: code folding
   <achuni>: usa tabs como gedit pero cambiás de tab con ctrl+pgup/pgdown (en vez de ctrl+alt+pgup/pdgown)
   <achuni>: podés elegir en qué encoding guardar *y abrir* los archivos
   <achuni>: indentar/desindentar y comentar/descomentar bloques de código
   <achuni>: está en ubuntu, y hay un instalador .exe para Windows que te da la misma misma interfaz en ambos OS
   <achuni>: tiene más cosas, pero eso es lo que me gustó. Y tiene todo eso sin las 40 ventanitas de configuración de kate/eric

http://www.geany.org/

Editra
~~~~~~

Editra es un editor de texto multiplataforma con una implementación que se centra en crear una interfaz fácil de usar y características que faciliten el desarrollo de código. Actualmente soporta resaltado de sintaxis y una variedad de otras características muy útiles para mas de 60 lenguajes de programación.

::

   fisa dijo:

   Al final me quedo con Editra, tiene las cosas que me interesan, y no
   demasiado de lo que no me interesa:
   - aceptablemente rapido
   - se integra con el versionado de codigo
   - autocompletado simple que no molesta
   - consola integrada
   - navegador de codigo (clases, metodos, etc.)
   - multiplataforma (en el trabajo hay windows :( ) y portable (te
   llevas la carpeta y listo, con configuracion y todo si pones adentro
   la .Editra)

   fisa actualiza su opinión en 2016:

   Hace rato que ya no lo uso, y el último release fue del 2013, así que no lo recomendaría más.
   (por mi cuenta ahora uso mucho vim, y recomiendo sublime text o ninja-ide para principiantes)

http://editra.org/

WingIDE
~~~~~~~

Bastante completo y multiplataforma, hecho especialmente para python. Tiene versiones comerciales y versiones gratis.

http://www.wingware.com/

IDLE
~~~~

Es parte de la distribución de Python. Muy buen soporte del lenguaje, class browser, debug y otras características. Lo mejor: el autocompletado (expand-word) es utilizando las palabras que encuentra en el archivo lo cual es muy simple y muy útil ("Simple is better than complex"). Lo peor: no usa solapas, cada archivo que abrís es una ventana aparte.

http://www.python.org/idle/doc/idlemain.html

PyCharm
~~~~~~~

PyCharm_ JetBrains — es un Python IDE con un completo juego de herramientas para el desarrollo productivo con el lenguaje de programacion Python. Adicionalmente, el IDE provee capacidades de alto rango para desarrolladores profesionales de Web con el framework Django. http://www.jetbrains.com/pycharm/index.html

NINJA-IDE
~~~~~~~~~

NINJA-IDE (Ninja Is Not Just Another IDE), es un IDE para Python hecho en Python. El objetivo de este proyecto es lograr un IDE especialmente diseñado para el desarrollo de aplicaciones Python, incorporando las características tradicionales de cualquier IDE y agregando funcionalidades extra con la que a todo programador de este lenguaje le gustaría contar. Esta desarrollado utilizando PyQt_ y gracias al sistema de Plugins que posee NINJA-IDE, hace que este sea fácilmente extensible. Realizado por miembros de PyAr_ y otros Colaboradores.

http://ninja-ide.org

Spyder
~~~~~~

Spyder_ es un IDE para python con edición avanzada, testing interactivo, introspección, etc... Esta especialmente recomendado para computación cientifica gracias a NumPy (algebra lineal), SciPy (procesamiento de imágenes y señales), matplotlib (ploteo interactivo en 2D/3D) y sporte a mlab de MayaVi (visualizacion 3D intetarctiva). Tiene un workflow especializado para "no programadores", aunque puede ser muy útil también para programdores. Spyder también puede ser usado como una librería, ya que probee poderosos widgets de PyQt4 relacionados con la consola.

http://packages.python.org/spyder/

PyScripter
~~~~~~~~~~

Windows-only, algo viejito, lleno de features (autocompletado, debugging, etc), utiliza pocos recursos, con versión portable y sencillo de usar

Visual Studio Code
~~~~~~~~~~~~~~~~~~

Gratuito, propiedad de Microsoft, multiplataforma. Bastante rápido.

https://code.visualstudio.com/

Editores de texto avanzados
---------------------------

Vim
~~~

Vim es un editor de texto altamente configurable que permite editar texto de manera eficiente. Es una versión mejorada del editor de texto vi, distribuido con casi todos los sistemas UNIX.

http://www.vim.org

Una **configuración** para vim orientada a python y fácil de instalar es esta (mantenida por fisa, de pyar): http://fisadev.github.io/fisa-vim-config

Emacs
~~~~~

Emacs es un editor de texto con una gran cantidad de funciones, muy popular entre programadores y usuarios técnicos.

http://www.gnu.org/software/emacs/emacs.html

Gedit
~~~~~

Gedit es el editor por defecto de gnome, mientras que apunta a la simplicidad y facilidad de uso, gedit es un editor de texto de propósito general muy poderoso.

http://www.gnome.org/projects/gedit/

Kate
~~~~

Kate es el editor de texto con capacidades extra de kde, tiene algunas características que facilitan el desarrollo de software.

http://kate-editor.org/

Marave
~~~~~~

Hecho y mantenido por Roberto Alsina, miembro de PyAr_

http://marave.googlecode.com/

Textmate
~~~~~~~~

Corre solo en MacOSX, muy fácilmente personalizable en cualquier lenguaje. Uno puede hacer un script y registrarlo como comando, ese script puede recibir el texto actualmente seleccionado, el documento actual, y alguna otra cosa que no recuerdo. El script lo procesa y devuelve un texto, que puede ser usado para reemplazar la seleccion actual, ponerse en un documento nuevo, y alguna otra cosa que no me acuerdo. Tiene una licencia comercial y privativa pero si sos usuario de OSX seguramente no te moleste.

http://macromates.com/

Scribes
~~~~~~~

Scribes_ es un editor de textos para GNOME escrito en Python. Entre sus `características`_ se destacan: autocompletado , templates (también conocido como **snippets**), indentado automático y marcado de línea (bookmarks). Vean la `demostración`_ para enamorarse 😉

.. ############################################################################

.. _PyCharm: http://www.jetbrains.com/pycharm/index.html




.. _Spyder: http://packages.python.org/spyder/





.. _Scribes: http://scribes.sourceforge.net/

.. _características: http://scribes.sourceforge.net/features.html

.. _demostración: http://scribes.sourceforge.net/demo.htm

.. _pyqt: /CharlasAbiertas2010/pyqt
.. _pyar: /pyar
