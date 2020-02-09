
Recetario
=========

*Nuestro CookBook, en vías desarrollo.* A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un cheff experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

.. contents::

-------------------------



Configuracion del entorno python
--------------------------------

Crear un entorno virtual y un esqueleto de proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Creando un nuevo proyecto python </pages/Recetario/creandounnuevoproyectopython>`_: Receta para crear un entorno de trabajo y un esqueleto minimo para un nuevo proyecto Python.html

Mejorando el interprete python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Autocompletado en consola interactiva </pages/Recetario/autocomplecionenconsolainteractiva>`_: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython..html

Estructuras de datos
--------------------

IterarSobrePares
~~~~~~~~~~~~~~~~

Expresiones regulares
---------------------

Extraer todos los mails de un texto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/ExtraerMails`_ de un texto utilizando el módulo re.

Formatos, datos, números y conversiones
---------------------------------------

aLetras
~~~~~~~

aLetras_ : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

Reverse
~~~~~~~

Reverse_ : Función que invierte los caracteres.

validar_cuit
~~~~~~~~~~~~

`</pages/Recetario/validarcuit>`_ : Función para validar un CUIT/CUIL estilo 00-00000000-0.html

digito_verificador_modulo10
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`</pages/Recetario/calculardigitoverificadormodulodiez>`_ : Función para generar el dígito verificador módulo 10.html

Normalizar caracteres Unicode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es bueno `</pages/Recetario/normalizarcaracteresunicode>`_ para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe..html

ObtenerSensacionTermica_: Calcular la Sensacion Termica o Temperatura Aparente.

Interceptar los prints
~~~~~~~~~~~~~~~~~~~~~~

`</pages/Recetario/interceptarprints>`_ sirve para hacer reemplazos en las strings que se van a imprimir, por ejemplo para agregar un timestamp..html

Frameworks Web
--------------

Django
~~~~~~

`Django/TestFormularioConFileUpload`_ :  un ejemplo de como probar un formulario que tiene un campo para subir un archivo.

`Django/ObtenerClaseOriginalCuandoHayHerencia`_ : Cuando usamos herencia de modelos, si ``bar`` y ``baz`` son subclases de ``foo``, podemos hacer que ``foo.objects.all()`` devuelva instancias de ``bar`` o ``baz`` dependiendo de cómo creamos el objeto orignalmente.

Bottle
~~~~~~

`Hola Mundo`_ : una aplicacion minima que muestra el mensaje hola mundo.

`Mini Galeria de Imagenes`_ : una aplicacion minima que muestra una Galeria de Imagenes Animada.

Interfaces graficas
-------------------

Gtk
~~~

`/Gui/Gtk/HolaMundo`_ : una ventana que muestra el mensaje hola mundo

`/Gui/Gtk/HolaMundoOO`_ : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

`/Gui/Gtk/Entry`_ : una ventana que solicita un valor y luego lo muestra en una ventana aparte

`/Gui/Gtk/EntrySoloNumeros`_: un ejemplo de como permitir el ingreso de solo numeros en un gtk.Entry

`/Gui/Gtk/HBox`_ : ejemplo que muestra como organizar elementos continuos horizontalmente

`/Gui/Gtk/VBox`_ : ejemplo que muestra como organizar elementos continuos verticalmente

`/Gui/Gtk/Grid`_ : ejemplo que muestra como organizar elementos en forma de grilla

`/Gui/Gtk/Button`_ : ejemplo que muestra como crear botones de diversas maneras

`/Gui/Gtk/ButtonBox`_ : ejemplo que muestra como crear botones y agruparlos en un contenedor

`/Gui/Gtk/AutoComplete`_ : ejemplo que muestra como crear un campo de texto con auto complesion

`/Gui/Gtk/Dialog`_ : ejemplo para crear dialogos modales

`/Gui/Gtk/FileChooser`_ : ejemplo que permite al usuario seleccionar un archivo

`/Gui/Gtk/Menu`_ :  ejemplo que mustra como crear un menu con distintos items

`/Gui/Gtk/TextArea`_ : ejemplo sobre manipulacion basica de un area de texto con scroll

`/Gui/Gtk/PrintNonGtk`_ : ejemplo sobre como usar el dialogo de impresion de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

`/Gui/Gtk/RichText`_: ejemplo sobre como insertar texto con formato basico a un textview

`/Gui/Gtk/ConfirmClose`_: ejemplo sobre como solicitar confirmacion para el cierre de una ventana

`/Gui/Gtk/MultiThread`_: ejemplo de como manipular la GUI desde múltiples threads sin usar locks (con colas)

`/Gui/Gtk/MultiThread2`_: ejemplo de como manipular la GUI usando múltiples threads

`/Gui/Gtk/Runner`_ ejemplo de como correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk

`/Gui/Gtk/FuncionRunner`_ idem al anterior pero usando una funcion en lugar de un objeto

`/Gui/Gtk/LabelConColor`_: ejemplo de como cambiar el color de un label sin usar pango markup

`/Gui/Gtk/XMLRPCServer`_ Servidor XMLRPC dentro de un hilo gtk

`/Gui/Gtk/StockItems`_: ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre

`/Gui/Gtk/WebkitEditor`_: ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

`/Gui/Gtk/StatusIcon`_: ejemplo de aplicación con ícono en el system tray.

`/Gui/Gtk/ErrorHandler`_: un ejemplo de capturar una excepción y mostrarla en un dialogo modal

`/Gui/Gtk/ListView`_: un ejemplo de como mostrar elementos en una

`/Gui/Gtk/EmuladorTerminal`_: un ejemplo de como hacer una terminal visual al estilo gnome-terminal

Gtk + glade
~~~~~~~~~~~

GtkGladeHolaMundoOO : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

GtkGladeSignals_ : manejo basico de señales

Qt
~~

QtMultiThread_ : ejemplo de como manipular la GUI usando múltiples threads sin usar locks (con colas)

`/QtImprimirPagina`_: ejemplo de como imprimir una pagina web a pdf

`/QtExtraerTextoRecurso`_ : como extraer un archivo de texto embebido en el sistema de recursos de PyQt

http://www.youtube.com/playlist?list=PLA955A8F9A95378CE : Python GUI Development with QT (videos 7 horas)

Pythoncard (wxPython)
~~~~~~~~~~~~~~~~~~~~~

PythonCard_: Ejemplo de como hacer una aplicación de escritorio desde 0 (para principiantes)

Tkinter + ttk
~~~~~~~~~~~~~

ttkHolamundo_: una ventana que muestra el mensaje hola mundo (usando Tk themed widgets).

tkWindowIcon_: una ventana con icono (usando Tk).

tkButtonIcon_: unos botones con iconos, ideal mini-toolbar (usando Tk).

tkScrollWhell_: usando la rueda de Scroll del raton (usando Tk).

tkOnlineOfflineIcon_: Icono de On Line u Off Line simple (usando Tk).

tkVersionPrint_: Obtener la version de TK que se esta usando.

GTKonTK_: Usar temas de GTK en Tk *(Hack)*.

TKWizards_: Crear un Wizard amigable de multiples paginas (siguiente, siguiente, ... terminar)

DisplayLCD7Segmentos_: Crear un Widget de Canvas tipo Display LCD de 7 Segmentos.

BotonGraficoTK_: Crear botones graficos personalizados de 3 estados con TK.

VentanaPasswordVibra_: Crear una ventana de password que Vibra si la password es incorrecta.

RelojDigital_: Crear un Reloj Digital simple, trucando un Label.

Emails
------

GMail
~~~~~

`/GmailMail`_ : Cómo enviar emails usando Gmail como SMTP

Email con adjuntos
~~~~~~~~~~~~~~~~~~

`/EmailConAdjunto`_ : Cómo enviar emails con adjuntos binarios

Creación de ejecutables para Windows
------------------------------------

Desde Linux
~~~~~~~~~~~

`/CrearEjecutableWindowsDesdeLinux`_ : Cómo crear ejecutables para Windows desde Linux con Wine.

En Windows
~~~~~~~~~~

`/CrearEjecutableWindows`_: Cómo crear ejecutables para Windows nativamente.

Hilos y concurrencia
--------------------

threads
~~~~~~~

ComunicarThreadsConQueue_: ejemplo sobre como comunicar y sincronizar threads usando colas

Web
---

HTTP servers
~~~~~~~~~~~~

Servidor Simple
:::::::::::::::

ComoLevantarUnServidorHttpSimple_  Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local

Servidor Multithread
::::::::::::::::::::

ComoLevantarUnServidorHttpMultithread_  Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local manejando los requests con threads

Xml
---

Xml a Diccionario
~~~~~~~~~~~~~~~~~

XmlADiccionario_: este ejemplo muestra como convertir un string xml en un conjunto de diccionarios y listas anidadas, también provee de dos clases que permiten acceder a los diccionarios y listas como si fueran objetos.

SimpleXmlElement
~~~~~~~~~~~~~~~~

SimpleXmlElement_: ejemplo de manejo de xml por elementos simples (simil php), permite leer y/o crear xml accediendo a los tags como si fueran atributos de un objeto.

Pdf
---

Generación de Facturas en PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/FacturaPyFpdf`_: Ejemplo de como generar una factura gráficamente en PDF utilizando PyFpdf_

Modificación de Estilos en rst2pdf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/EstilosRst2Pdf`_: Explicación de Roberto Alsina, sobre cómo modificar los estilos de diseño en rst2pdf

Dbf
---

Leer y modificar Archivos .DBF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/DbfPy`_: Ejemplo de como leer y modificar bases de datos en formato DBF

Windows
-------

Servidor Interfase C.O.M.
~~~~~~~~~~~~~~~~~~~~~~~~~

`/ServidorCom`_: Ejemplo de como exponer objetos python a otros lenguajes (VB, VFP, etc.) vía interfase COM

Llamar a librerías nativas con ctypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/WinBatt`_: Ejemplo de como usar ctypes para llamar a bibliotecas nativas usando estructuras C.

Python Internals
----------------

LocalsDeUnaFuncionQueLanzoUnaExcepcion_: ejemplo de como obtener las variables locales a la función que lanzo una excepion

PsycoSpeedUp_: Como acelerar las aplicaciones con Psyco, si esta presente.

MapeandoMemoria_: Cómo generar un mapa de la memoria con heapy

Numpy, Scipy, Matplotlib
------------------------

`/Histograma`_: Ejemplo sencillo de uso de la función *hist*

Administracion de Sistemas Operativos
-------------------------------------

`/ListarProcesos`_: como listar procesos multiplataforma

`/ChequearInterfacesInternetLinux`_

Xdg-Sudo_: El sudo Grafico Universal, para Escritorios GTK/QT/whatever, inspirado en *xdg-open* de Linux.

`Chequeo de Paquetes, APT, Linux`_: Chequear si un Programa esta instalado, o no, y si existe en Linux.

Internet
--------

`/RevisarConexion`_: revisar si estamos conectados a internet conexión.

`/ObtenerBytesTransferidos`_: obtener la cantidad de datos transferidos en Bytes.

ipPublica_ : obtener la direccion ip publica usando 3 lineas de Python.

`/ObtenerUbicacionGeografica`_: obtener datos de la ubicacion geografica (Geo-Location) usando Python-Geoip.

Misceláneo
----------

`/MatrixPythonToy`_: Efecto "The Matrix" en linea de comandos, ideal CLI Screen Saver / Screen Lock.

`/SaberSiNlibreriaEstaInstalada`_: Saber si N Libreria esta instalada sin ingresar al interprete de Python.

`/PythonVersionCheck`_: Chequea la version de Python, y sale o imprime error en funcion de eso.

`/RootCheck`_: Comprobar si somos root y actuar en funcion de eso, orientado a Linux.

`/ComoBajarTodosLosBuffersAlDisco`_: Best Practice para un programa en Linux para cerrarse.

`/ProgressbarUrllib2`_: Como descargar algo de internet y mostrar una barrita de progreso.

`/CheckDistroVersion`_: Chequea la version de la Distribucion Linux y actuar en funcion de eso.

`/AlarmaPrecaria`_: Alarma minima y basica de linea de comandos.

`/KeyboardLedsDemo`_: Como controlar los Leds del Teclado con Python.

`/NotificarDispositivosUsb`_ : Como detectar y notificar dispocitivos USB en Linux.

Python en Apache OpenOffice / LibreOffice
-----------------------------------------

`/pyUNO/HolaMundo`_: Hola Mundo

`/pyUNO/MiPrimerMacro`_: Mi primer macro

Crypto
------

`/Crypto/BlowfishConBlowfishpy`_: como encriptar usando el modulo blowfish.py

Multiprocessing y threading (y otras yerbas)
--------------------------------------------

`/MultiprocessingYThreading`_: ejemplo simple de como las apis de threading y multiprocessing son intercambiables.

Divertidos
----------

`/Fun/NadoSincronizado`_: bailarín de nado sincronizado en tu consola!

`/Fun/NadoSincronizadoDisco`_: bailarín de nado sincronizado en tu consola con luces de colores!

`/Fun/MiniSpaceInvaders`_: Un mini space invaders usando caracteres.

-------------------------

 CategoryRecetas_

.. ############################################################################

.. _Recetario/CreandoUnNuevoProyectoPython: /pages/Recetario/creandounnuevoproyectopython.html

.. _Autocompletado en consola interactiva: /pages/Recetario/autocomplecionenconsolainteractiva.html






.. _Hola Mundo: /pages/Recetario/Bottle/holamundo.html

.. _Mini Galeria de Imagenes: /pages/Recetario/Bottle/galeria.html




.. _aletras: /pages/aletras.html
.. _reverse: /pages/reverse.html
.. _obtenersensaciontermica: /pages/obtenersensaciontermica.html
.. _qtmultithread: /pages/qtmultithread.html
.. _pythoncard: /pages/pythoncard.html
.. _ttkholamundo: /pages/ttkholamundo.html
.. _tkwindowicon: /pages/tkwindowicon.html
.. _tkbuttonicon: /pages/tkbuttonicon.html
.. _tkscrollwhell: /pages/tkscrollwhell.html
.. _tkonlineofflineicon: /pages/tkonlineofflineicon.html
.. _tkversionprint: /pages/tkversionprint.html
.. _gtkontk: /pages/gtkontk.html
.. _tkwizards: /pages/tkwizards.html
.. _displaylcd7segmentos: /pages/displaylcd7segmentos.html
.. _botongraficotk: /pages/botongraficotk.html
.. _ventanapasswordvibra: /pages/ventanapasswordvibra.html
.. _relojdigital: /pages/relojdigital.html
.. _comunicarthreadsconqueue: /pages/comunicarthreadsconqueue.html
.. _comolevantarunservidorhttpsimple: /pages/comolevantarunservidorhttpsimple.html
.. _comolevantarunservidorhttpmultithread: /pages/comolevantarunservidorhttpmultithread.html
.. _xmladiccionario: /pages/xmladiccionario.html
.. _simplexmlelement: /pages/simplexmlelement.html
.. _localsdeunafuncionquelanzounaexcepcion: /pages/localsdeunafuncionquelanzounaexcepcion.html
.. _psycospeedup: /pages/psycospeedup.html
.. _mapeandomemoria: /pages/mapeandomemoria.html
.. _ippublica: /pages/ippublica.html
.. _categoryrecetas: /pages/categoryrecetas.html
