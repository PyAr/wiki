.. title: Recetario


*Nuestro CookBook, en vías desarrollo.* A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un cheff experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

.. contents::

Configuracion del entorno python
--------------------------------

* `Creando un nuevo proyecto python </Recetario/creandounnuevoproyectopython>`__: Receta para crear un entorno de trabajo y un esqueleto minimo para un nuevo proyecto Python

* `Autocompletado en consola interactiva </Recetario/autocomplecionenconsolainteractiva>`__: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython.

Estructuras de datos
--------------------

* `Iterar Sobre Pares </Recetario/iterarsobrepares>`__

Expresiones regulares
---------------------

* `Extraer todos los mails de un texto </Recetario/extraermails>`__ de un texto utilizando el módulo re.

Formatos, datos, números y conversiones
---------------------------------------

* `aLetras </Recetario/aletras>`__ : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

* `reverse </Recetario/reverse>`__ : Función que invierte los caracteres.

* `validar cuit </Recetario/validarcuit>`__: Función para validar un CUIT/CUIL estilo 00-00000000-0

* `digito_verificador_modulo10 </Recetario/calculardigitoverificadormodulodiez>`__: Función para generar el dígito verificador módulo 10

* `Normalizar caracteres Unicode </Recetario/normalizarcaracteresunicode>`__ para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe.

* `Obtener Sensacion Termica </Recetario/obtenersensaciontermica>`__: Calcular la Sensacion Termica o Temperatura Aparente.

* `Interceptar los prints </Recetario/interceptarprints>`__ sirve para hacer reemplazos en las strings que se van a imprimir, por ejemplo para agregar un timestamp.

Frameworks Web
--------------

Django
~~~~~~

* `Test Forumario Con File Upload </Recetario/Django/testformularioConfileupload>`__:  un ejemplo de como probar un formulario que tiene un campo para subir un archivo.

* `Obtener Clase Original Cuando Hay Herencia </Recetario/Django/obtenerclaseoriginalcuandohayherencia>`__: Cuando usamos herencia de modelos, si ``bar`` y ``baz`` son subclases de ``foo``, podemos hacer que ``foo.objects.all()`` devuelva instancias de ``bar`` o ``baz`` dependiendo de cómo creamos el objeto orignalmente.

Bottle
~~~~~~

* `Hola Mundo </Recetario/Bottle/holamundo>`__: una aplicacion minima que muestra el mensaje hola mundo.

* `Mini Galeria de Imagenes </Recetario/Bottle/galeria>`__: una aplicacion minima que muestra una Galeria de Imagenes Animada.

.. _recetario_interaces_graficas:

Interfaces graficas
-------------------

Gtk
~~~

* `Hola Mundo </Recetario/Gui/Gtk/holamundo>`__ : una ventana que muestra el mensaje hola mundo

* `Hola Mundo con objetos </Recetario/Gui/Gtk/holamundooo>`__ : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

* `Entry </Recetario/Gui/Gtk/entry>`__ : una ventana que solicita un valor y luego lo muestra en una ventana aparte

* `Entry solo numeros </Recetario/Gui/Gtk/entrysolonumeros>`__: un ejemplo de como permitir el ingreso de solo numeros en un gtk.Entry

* `HBox </Recetario/Gui/Gtk/hbox>`__ : ejemplo que muestra como organizar elementos continuos horizontalmente

* `VBox </Recetario/Gui/Gtk/vbox>`__ : ejemplo que muestra como organizar elementos continuos verticalmente

* `Grid </Recetario/Gui/Gtk/grid>`__ : ejemplo que muestra como organizar elementos en forma de grilla

* `Button </Recetario/Gui/Gtk/button>`__ : ejemplo que muestra como crear botones de diversas maneras

* `Button Box </Recetario/Gui/Gtk/buttonbox>`__ : ejemplo que muestra como crear botones y agruparlos en un contenedor

* `Autocomplete </Recetario/Gui/Gtk/autocomplete>`_ : ejemplo que muestra como crear un campo de texto con auto complesion

* `Dialog </Recetario/Gui/Gtk/dialog>`__ : ejemplo para crear dialogos modales

* `Menu </Recetario/Gui/Gtk/menu>`__ :  ejemplo que mustra como crear un menu con distintos items

* `Print no gtk </Recetario/Gui/Gtk/printnongtk>`__ : ejemplo sobre como usar el dialogo de impresion de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

* `Rich text </Recetario/Gui/Gtk/richtext>`__: ejemplo sobre como insertar texto con formato basico a un textview

* `Confirm close </Recetario/Gui/Gtk/confirmclose>`__: ejemplo sobre como solicitar confirmacion para el cierre de una ventana

* `Multi Thread </Recetario/Gui/Gtk/multithread>`__: ejemplo de como manipular la GUI desde múltiples threads sin usar locks (con colas)

* `Multi thread 2 </Recetario/Gui/Gtk/multithread2>`__: ejemplo de como manipular la GUI usando múltiples threads

* `Runner </Recetario/Gui/Gtk/runner>`_ ejemplo de como correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk

* `Funcion Runner </Recetario/Gui/Gtk/funcionrunner>`__ idem al anterior pero usando una funcion en lugar de un objeto

* `Label con color </Recetario/Gui/Gtk/labelconcolor>`__: ejemplo de como cambiar el color de un label sin usar pango markup

* `Servidor XMLRPC </Recetario/Gui/Gtk/xmlrpcerver>`__ Servidor XMLRPC dentro de un hilo gtk

* `Stock items </Recetario/Gui/Gtk/stockitems>`__: ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre

* `Webkit Editor </Recetario/Gui/Gtk/webkiteditor>`__: ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

* `Status Icon </Recetario/Gui/Gtk/statusicon>`__: ejemplo de aplicación con ícono en el system tray.

* `Error Handler </Recetario/Gui/Gtk/errorhandler>`__: un ejemplo de capturar una excepción y mostrarla en un dialogo modal

* `List View </Recetario/Gui/Gtk/listview>`__: un ejemplo de como mostrar elementos en una

* `Emulador Terminal </Recetario/Gui/Gtk/EmuladorTerminal>`__: un ejemplo de como hacer una terminal visual al estilo gnome-terminal

Gtk + glade
~~~~~~~~~~~

GtkGladeHolaMundoOO : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

Qt
~~

* `Multi Thread </Recetario/qt/qtmultithread>`__: ejemplo de como manipular la GUI usando múltiples threads sin usar locks (con colas)

* `Imprimir Pagina </Recetario/qt/qtimprimirpagina>`__: ejemplo de como imprimir una pagina web a pdf

* `Extraer Texto Recurso </Recetario/qt/qtextraertextorecurso>`__ : como extraer un archivo de texto embebido en el sistema de recursos de PyQt

* http://www.youtube.com/playlist?list=PLA955A8F9A95378CE : Python GUI Development with QT (videos 7 horas)

Pythoncard (wxPython)
~~~~~~~~~~~~~~~~~~~~~

* `PythonCard </Recetario/pythoncard>`__: Ejemplo de como hacer una aplicación de escritorio desde 0 (para principiantes)

Tkinter + ttk
~~~~~~~~~~~~~

* `Hola mundo </Recetario/ttkholamundo>`__: una ventana que muestra el mensaje hola mundo (usando Tk themed widgets).

* `Window Icon </Recetario/tkwindowicon>`__: una ventana con icono (usando Tk).

* `Button Icon </Recetario/tkbuttonicon>`__: unos botones con iconos, ideal mini-toolbar (usando Tk).

* `Scroll Wheel </Recetario/tkscrollwhell>`__: usando la rueda de Scroll del raton (usando Tk).

* `Online/Offline Icon </Recetario/tkOnlineOfflineIcon>`__: Icono de On Line u Off Line simple (usando Tk).

* `Version Print </Recetario/tkversionprint>`__: Obtener la version de TK que se esta usando.

* `Gtk on Tk </Recetario/gtkontk>`__: Usar temas de GTK en Tk *(Hack)*.

* `Wizards </Recetario/tkwizards>`__: Crear un Wizard amigable de multiples paginas (siguiente, siguiente, ... terminar)

* `Displace LCD 7 Segmentos </Recetario/displaylcd7segmentos>`__: Crear un Widget de Canvas tipo Display LCD de 7 Segmentos.

* `Boton Grafico </Recetario/botongraficotk>`__: Crear botones graficos personalizados de 3 estados con TK.

* `Ventana Password </Recetario/ventanapasswordvibra>`__: Crear una ventana de password que Vibra si la password es incorrecta.

* `Reloj Dijital </Recetario/relojdigital>`__: Crear un Reloj Digital simple, trucando un Label.

Emails
------

* `Gmail </Recetario/gmailmail>`__ : Cómo enviar emails usando Gmail como SMTP

* `Email con Adjunto </Recetario/emailconadjunto>`__ : Cómo enviar emails con adjuntos binarios

Creación de ejecutables para Windows
------------------------------------

* `Desde Linux </Recetario/crearejecutablewindowsdesdelinux>`__ : Cómo crear ejecutables para Windows desde Linux con Wine.

* `En Windows </Recetario/crearejecutablewindows>`__: Cómo crear ejecutables para Windows nativamente.

Hilos y concurrencia
--------------------

* `Comunicar Threads Con Queue </Recetario/comunicarthreadsconqueue>`__: ejemplo sobre como comunicar y sincronizar threads usando colas

* `Multiprocessing y threading </Recetario/MultiprocessingYThreading>`__: ejemplo simple de como las apis de threading y multiprocessing son intercambiables.

Web
---

* `Servidor Simple </Recetario/comolevantarunservidorhttpsimple>`__: Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local

* `Servidor Multithread </Recetario/comolevantarunservidorhttpmultithread>`__: Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local manejando los requests con threads

Xml
---

* `Xml a Diccionario </Recetario/xmladiccionario>`__: este ejemplo muestra como convertir un string xml en un conjunto de diccionarios y listas anidadas, también provee de dos clases que permiten acceder a los diccionarios y listas como si fueran objetos.

* `SimpleXmlElement </Recetario/simplexmlelement>`__: ejemplo de manejo de xml por elementos simples (simil php), permite leer y/o crear xml accediendo a los tags como si fueran atributos de un objeto.

Pdf
---

* `Generación de Facturas en PDF </Recetario/facturapyfpdf>`__: Ejemplo de como generar una factura gráficamente en PDF utilizando PyFpdf

* `Modificación de Estilos en rst2pdf </Recetario/estilosrst2pdf>`__: Explicación de Roberto Alsina, sobre cómo modificar los estilos de diseño en rst2pdf

Dbf
---

* `Leer y modificar Archivos .DBF </Recetario/dbfpy>`__: Ejemplo de como leer y modificar bases de datos en formato DBF

Windows
-------

* `Servidor Interfase C.O.M. </Recetario/servidorcom>`__: Ejemplo de como exponer objetos python a otros lenguajes (VB, VFP, etc.) vía interfase COM

* `Llamar a librerías nativas con ctypes </Recetario/winbatt>`__: Ejemplo de como usar ctypes para llamar a bibliotecas nativas usando estructuras C.

Python Internals
----------------

* `Locals De Una Funcion Que Lanzo Una Excepcion </Recetario/localsdeunafuncionquelanzounaexcepcion>`__: ejemplo de como obtener las variables locales a la función que lanzo una excepion

* `Psyco Speed Up </Recetario/psycospeedup>`__: Como acelerar las aplicaciones con Psyco, si esta presente.

* `Mapeando Memoria </Recetario/mapeandomemoria>`__: Cómo generar un mapa de la memoria con heapy

Numpy, Scipy, Matplotlib
------------------------

* `Histograma </Recetario/histograma>`__: Ejemplo sencillo de uso de la función *hist*

Administracion de Sistemas Operativos
-------------------------------------

* `Listar procesos </Recetario/listarprocesos>`__: como listar procesos multiplataforma

* `Chequear Interfaces Internet Linux </Recetario/chequearinterfacesinternetlinux>`__

* `Xdg-Sudo </Recetario/xdg-sudo>`__: El sudo Grafico Universal, para Escritorios GTK/QT/whatever, inspirado en *xdg-open* de Linux.

* `Chequeo de Paquetes, APT, Linux </Recetario/chequeo_de_paquetes_apt_linux>`__: Chequear si un Programa esta instalado, o no, y si existe en Linux.

Internet
--------

* `Revisar conexion </Recetario/revisarconexion>`__: revisar si estamos conectados a internet conexión.

* `Obtener Bytes transferidos </Recetario/obtenerbytestransferidos>`__: obtener la cantidad de datos transferidos en Bytes.

* `Ip publica </Recetario/ippublica>`__ : obtener la direccion ip publica usando 3 lineas de Python.

* `Obtener ubicacion geografica </Recetario/obtenerubicaciongeografica>`__: obtener datos de la ubicacion geografica (Geo-Location) usando Python-Geoip.

Misceláneo
----------

* `Matrix </Recetario/matrixpythontoy>`__: Efecto "The Matrix" en linea de comandos, ideal CLI Screen Saver / Screen Lock.

* `Saber si libreria esta instalada </Recetario/sabersinlibreriaestainstalada>`__: Saber si N Libreria esta instalada sin ingresar al interprete de Python.

* `Python version check </Recetario/pythonversioncheck>`__: Chequea la version de Python, y sale o imprime error en funcion de eso.

* `Root check </Recetario/rootcheck>`__: Comprobar si somos root y actuar en funcion de eso, orientado a Linux.

* `Como bajar todos los buffers al disco </Recetario/comobajartodoslosbuffersaldisco>`__: Best Practice para un programa en Linux para cerrarse.

* `Progressbar y urllib2 </Recetario/progressbarurllib2>`__: Como descargar algo de internet y mostrar una barrita de progreso.

* `Chequear distro version </Recetario/checkdistroversion>`__: Chequea la version de la Distribucion Linux y actuar en funcion de eso.

* `Alarma precaria </Recetario/alarmaprecaria>`__: Alarma minima y basica de linea de comandos.

* `Keyboard leds demo </Recetario/keyboardledsdemo>`__: Como controlar los Leds del Teclado con Python.

* `Notificar dispositivos usb </Recetario/notificardispositivosusb>`__ : Como detectar y notificar dispocitivos USB en Linux.

Python en Apache OpenOffice / LibreOffice
-----------------------------------------

* `Hola Mundo </Recetario/pyUNO/holamundo>`__

* `Mi primer macro </Recetario/pyUNO/miprimermacro>`__

Crypto
------

* `Blowfish con Blowfishpy </Recetario/Crypto/BlowfishConBlowfishpy>`__: como encriptar usando el modulo blowfish.py

Divertidos
----------

* `Nado sincronizado </Recetario/Fun/nadosincronizado>`__: bailarín de nado sincronizado en tu consola!

* `Nado sincronizado disco </Recetario/Fun/nadosincronizadodisco>`__: bailarín de nado sincronizado en tu consola con luces de colores!

* `Mini space inviders </Recetario/Fun/minispaceinvaders>`__: Un mini space invaders usando caracteres.

