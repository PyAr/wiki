.. title: Recetario


*Nuestro CookBook, en vías desarrollo.* A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un chef experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

.. contents::

Configuración del entorno python
--------------------------------

* `Creando un nuevo proyecto python </recetario/creandounnuevoproyectopython>`__: Receta para crear un entorno de trabajo y un esqueleto mínimo para un nuevo proyecto Python

* `Autocompletado en consola interactiva </recetario/autocomplecionenconsolainteractiva>`__: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython.

Estructuras de datos
--------------------

* `Iterar Sobre Pares </recetario/iterarsobrepares>`__

Expresiones regulares
---------------------

* `Extraer todos los mails de un texto </recetario/extraermails>`__ de un texto utilizando el módulo re.

Formatos, datos, números y conversiones
---------------------------------------

* `aLetras </recetario/aletras>`__ : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

* `reverse </recetario/reverse>`__ : Función que invierte los caracteres.

* `validar cuit </recetario/validarcuit>`__: Función para validar un CUIT/CUIL estilo 00-00000000-0

* `digito_verificador_modulo10 </recetario/calculardigitoverificadormodulodiez>`__: Función para generar el dígito verificador módulo 10

* `Normalizar caracteres Unicode </recetario/normalizarcaracteresunicode>`__ para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe.

* `Obtener Sensación Térmica </recetario/obtenersensaciontermica>`__: Calcular la Sensación Térmica o Temperatura Aparente.

* `Interceptar los prints </recetario/interceptarprints>`__ sirve para hacer reemplazos en las strings que se van a imprimir, por ejemplo para agregar un timestamp.

Frameworks Web
--------------

Django
~~~~~~

* `Test Formulario Con File Upload </recetario/django/testformularioConfileupload>`__:  un ejemplo de como probar un formulario que tiene un campo para subir un archivo.

* `Obtener Clase Original Cuando Hay Herencia </recetario/django/obtenerclaseoriginalcuandohayherencia>`__: Cuando usamos herencia de modelos, sí ``bar`` y ``baz`` son subclases de ``foo``, podemos hacer que ``foo.objects.all()`` devuelva instancias de ``bar`` o ``baz`` dependiendo de cómo creamos el objeto originalmente.

Bottle
~~~~~~

* `Hola Mundo </recetario/bottle/holamundo>`__: una aplicación mínima que muestra el mensaje hola mundo.

* `Mini Galería de Imágenes </recetario/bottle/galeria>`__: una aplicación mínima que muestra una Galería de Imágenes Animada.

.. _recetario_interaces_graficas:

Interfaces graficas
-------------------

Gtk
~~~

* `Hola Mundo </recetario/gui/gtk/holamundo>`__ : una ventana que muestra el mensaje hola mundo

* `Hola Mundo con objetos </recetario/gui/gtk/holamundooo>`__ : una ventana que muestra el mensaje hola mundo programado utilizando orientación a objetos

* `Entry </recetario/gui/gtk/entry>`__ : una ventana que solicita un valor y luego lo muestra en una ventana aparte

* `Entry solo números </recetario/gui/gtk/entrysolonumeros>`__: un ejemplo de cómo permitir el ingreso de solo números en un gtk.Entry

* `HBox </recetario/gui/gtk/hbox>`__ : ejemplo que muestra cómo organizar elementos continuos horizontalmente

* `VBox </recetario/gui/gtk/vbox>`__ : ejemplo que muestra cómo organizar elementos continuos verticalmente

* `Grid </recetario/gui/gtk/grid>`__ : ejemplo que muestra cómo organizar elementos en forma de grilla

* `Button </recetario/gui/gtk/button>`__ : ejemplo que muestra cómo crear botones de diversas maneras

* `Button Box </recetario/gui/gtk/buttonbox>`__ : ejemplo que muestra cómo crear botones y agruparlos en un contenedor

* `Autocomplete </recetario/gui/gtk/autocomplete>`_ : ejemplo que muestra cómo crear un campo de texto con auto complesion

* `Dialog </recetario/gui/gtk/dialog>`__ : ejemplo para crear diálogos modales

* `Menu </recetario/gui/gtk/menu>`__ :  ejemplo que muestra cómo crear un menú con distintos ítems

* `Print no gtk </recetario/gui/gtk/printnongtk>`__ : ejemplo sobre cómo usar el diálogo de impresión de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

* `Rich text </recetario/gui/gtk/richtext>`__: ejemplo sobre cómo insertar texto con formato básico a un textview

* `Confirm close </recetario/gui/gtk/confirmclose>`__: ejemplo sobre cómo solicitar confirmación para el cierre de una ventana

* `Multi Thread </recetario/gui/gtk/multithread>`__: ejemplo de cómo manipular la GUI desde múltiples threads sin usar locks (con colas)

* `Multi thread 2 </recetario/gui/gtk/multithread2>`__: ejemplo de cómo manipular la GUI usando múltiples threads

* `Runner </recetario/gui/gtk/runner>`_ ejemplo de cómo correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk

* `Función Runner </recetario/gui/gtk/funcionrunner>`__ idem al anterior pero usando una función en lugar de un objeto

* `Label con color </recetario/gui/gtk/labelconcolor>`__: ejemplo de cómo cambiar el color de un label sin usar pango markup

* `Servidor XMLRPC </recetario/gui/gtk/xmlrpcerver>`__ Servidor XMLRPC dentro de un hilo gtk

* `Stock items </recetario/gui/gtk/stockitems>`__: ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre

* `Webkit Editor </recetario/gui/gtk/webkiteditor>`__: ejemplo de cómo usar webkit para editar páginas HTML como si fuera un editor

* `Status Icon </recetario/gui/gtk/statusicon>`__: ejemplo de aplicación con ícono en el system tray.

* `Error Handler </recetario/gui/gtk/errorhandler>`__: un ejemplo de capturar una excepción y mostrarla en un diálogo modal

* `List View </recetario/gui/gtk/listview>`__: un ejemplo de cómo mostrar elementos en una

* `Emulador Terminal </recetario/gui/gtk/EmuladorTerminal>`__: un ejemplo de cómo hacer una terminal visual al estilo gnome-terminal

Gtk + glade
~~~~~~~~~~~

GtkGladeHolaMundoOO : una ventana que muestra el mensaje hola mundo programado utilizando orientación a objetos

Qt
~~

* `Multi Thread </recetario/qt/qtmultithread>`__: ejemplo de cómo manipular la GUI usando múltiples threads sin usar locks (con colas)

* `Imprimir Pagina </recetario/qt/qtimprimirpagina>`__: ejemplo de cómo imprimir una página web a pdf

* `Extraer Texto Recurso </recetario/qt/qtextraertextorecurso>`__ : cómo extraer un archivo de texto embebido en el sistema de recursos de PyQt

* http://www.youtube.com/playlist?list=PLA955A8F9A95378CE : Python GUI Development with QT (videos 7 horas)

Pythoncard (wxPython)
~~~~~~~~~~~~~~~~~~~~~

* `PythonCard </recetario/pythoncard>`__: Ejemplo de cómo hacer una aplicación de escritorio desde 0 (para principiantes)

Tkinter + ttk
~~~~~~~~~~~~~

* `Hola mundo </recetario/ttkholamundo>`__: una ventana que muestra el mensaje hola mundo (usando Tk themed widgets).

* `Window Icon </recetario/tkwindowicon>`__: una ventana con icono (usando Tk).

* `Button Icon </recetario/tkbuttonicon>`__: unos botones con iconos, ideal mini-toolbar (usando Tk).

* `Scroll Wheel </recetario/tkscrollwhell>`__: usando la rueda de Scroll del ratón (usando Tk).

* `Online/Offline Icon </recetario/tkOnlineOfflineIcon>`__: Icono de On Line u Off Line simple (usando Tk).

* `Version Print </recetario/tkversionprint>`__: Obtener la versión de TK que se está usando.

* `Gtk on Tk </recetario/gtkontk>`__: Usar temas de GTK en Tk *(Hack)*.

* `Wizards </recetario/tkwizards>`__: Crear un Wizard amigable de múltiples páginas (siguiente, siguiente, ... terminar)

* `Displace LCD 7 Segmentos </recetario/displaylcd7segmentos>`__: Crear un Widget de Canvas tipo Display LCD de 7 Segmentos.

* `Boton Grafico </recetario/botongraficotk>`__: Crear botones gráficos personalizados de 3 estados con TK.

* `Ventana Password </recetario/ventanapasswordvibra>`__: Crear una ventana de password que Vibra si la password es incorrecta.

* `Reloj Digital </recetario/relojdigital>`__: Crear un Reloj Digital simple, trucando un Label.

Emails
------

* `Gmail </recetario/gmailmail>`__ : Cómo enviar emails usando Gmail como SMTP

* `Email con Adjunto </recetario/emailconadjunto>`__ : Cómo enviar emails con adjuntos binarios

Creación de ejecutables para Windows
------------------------------------

* `Desde Linux </recetario/crearejecutablewindowsdesdelinux>`__ : Cómo crear ejecutables para Windows desde Linux con Wine.

* `En Windows </recetario/crearejecutablewindows>`__: Cómo crear ejecutables para Windows nativamente.

Hilos y concurrencia
--------------------

* `Comunicar Threads Con Queue </recetario/comunicarthreadsconqueue>`__: ejemplo sobre cómo comunicar y sincronizar threads usando colas

* `Multiprocessing y threading </recetario/MultiprocessingYThreading>`__: ejemplo simple de cómo las apis de threading y multiprocessing son intercambiables.

Web
---

* `Servidor Simple </recetario/comolevantarunservidorhttpsimple>`__: Ejemplo sobre cómo levantar un servidor http que sirva el contenido de un directorio local

* `Servidor Multithread </recetario/comolevantarunservidorhttpmultithread>`__: Ejemplo sobre cómo levantar un servidor http que sirva el contenido de un directorio local manejando los requests con threads

Xml
---

* `Xml a Diccionario </recetario/xmladiccionario>`__: este ejemplo muestra cómo convertir un string xml en un conjunto de diccionarios y listas anidadas, también provee de dos clases que permiten acceder a los diccionarios y listas como si fueran objetos.

* `SimpleXmlElement </recetario/simplexmlelement>`__: ejemplo de manejo de xml por elementos simples (simil php), permite leer y/o crear xml accediendo a los tags como si fueran atributos de un objeto.

Pdf
---

* `Generación de Facturas en PDF </recetario/facturapyfpdf>`__: Ejemplo de cómo generar una factura gráficamente en PDF utilizando PyFpdf

* `Modificación de Estilos en rst2pdf </recetario/estilosrst2pdf>`__: Explicación de Roberto Alsina, sobre cómo modificar los estilos de diseño en rst2pdf

Dbf
---

* `Leer y modificar Archivos .DBF </recetario/dbfpy>`__: Ejemplo de cómo leer y modificar bases de datos en formato DBF

Windows
-------

* `Servidor Interfase C.O.M. </recetario/servidorcom>`__: Ejemplo de cómo exponer objetos python a otros lenguajes (VB, VFP, etc.) vía interfase COM

* `Llamar a librerías nativas con ctypes </recetario/winbatt>`__: Ejemplo de cómo usar ctypes para llamar a bibliotecas nativas usando estructuras C.

Python Internals
----------------

* `Locals De Una Función Que Lanzó Una Excepción </recetario/localsdeunafuncionquelanzounaexcepcion>`__: ejemplo de cómo obtener las variables locales a la función que lanzó una excepción

* `Psyco Speed Up </recetario/psycospeedup>`__: Como acelerar las aplicaciones con Psyco, si esta presente.

* `Mapeando Memoria </recetario/mapeandomemoria>`__: Cómo generar un mapa de la memoria con heapy

Numpy, Scipy, Matplotlib
------------------------

* `Histograma </recetario/histograma>`__: Ejemplo sencillo de uso de la función *hist*

Administración de Sistemas Operativos
-------------------------------------

* `Listar procesos </recetario/listarprocesos>`__: cómo listar procesos multiplataforma

* `Chequear Interfaces Internet Linux </recetario/chequearinterfacesinternetlinux>`__

* `Xdg-Sudo </recetario/xdg-sudo>`__: El sudo Gráfico Universal, para Escritorios GTK/QT/whatever, inspirado en *xdg-open* de Linux.

* `Chequeo de Paquetes, APT, Linux </recetario/chequeo_de_paquetes_apt_linux>`__: Chequear si un Programa está instalado, o no, y si existe en Linux.

Internet
--------

* `Revisar conexion </recetario/revisarconexion>`__: revisar si estamos conectados a internet conexión.

* `Obtener Bytes transferidos </recetario/obtenerbytestransferidos>`__: obtener la cantidad de datos transferidos en Bytes.

* `Ip publica </recetario/ippublica>`__ : obtener la  dirección ip pública usando 3 líneas de Python.

* `Obtener ubicación geográfica </recetario/obtenerubicaciongeografica>`__: obtener datos de la ubicación geográfica (Geo-Location) usando Python-Geoip.

Misceláneo
----------

* `Matrix </recetario/matrixpythontoy>`__: Efecto "The Matrix" en línea de comandos, ideal CLI Screen Saver / Screen Lock.

* `Saber si libreria está instalada </recetario/sabersinlibreriaestainstalada>`__: Saber si N Libreria está instalada sin ingresar al intérprete de Python.

* `Python version check </recetario/pythonversioncheck>`__: Chequea la versión de Python, y sale o imprime error en función de eso.

* `Root check </recetario/rootcheck>`__: Comprobar si somos root y actuar en función de eso, orientado a Linux.

* `Como bajar todos los buffers al disco </recetario/comobajartodoslosbuffersaldisco>`__: Best Practice para un programa en Linux para cerrarse.

* `Progressbar y urllib2 </recetario/progressbarurllib2>`__: Cómo descargar algo de internet y mostrar una barrita de progreso.

* `Chequear distro versión </recetario/checkdistroversion>`__: Chequea la versión de la Distribución Linux y actuar en función de eso.

* `Alarma precaria </recetario/alarmaprecaria>`__: Alarma mínima y básica de línea de comandos.

* `Keyboard leds demo </recetario/keyboardledsdemo>`__: Cómo controlar los Leds del Teclado con Python.

* `Notificar dispositivos usb </recetario/notificardispositivosusb>`__ : Cómo detectar y notificar dispositivos USB en Linux.

Python en Apache OpenOffice / LibreOffice
-----------------------------------------

* `Hola Mundo </recetario/pyuno/holamundo>`__

* `Mi primer macro </recetario/pyuno/miprimermacro>`__

Crypto
------

* `Blowfish con Blowfishpy </recetario/crypto/blowfishconblowfishpy>`__: como encriptar usando el modulo blowfish.py

Divertidos
----------

* `Nado sincronizado </recetario/fun/nadosincronizado>`__: bailarín de nado sincronizado en tu consola!

* `Nado sincronizado disco </recetario/fun/nadosincronizadodisco>`__: bailarín de nado sincronizado en tu consola con luces de colores!

* `Mini space invaders </recetario/fun/minispaceinvaders>`__: Un mini space invaders usando caracteres.

