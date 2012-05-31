#language es
#pragma section-numbers 2
= Recetario =
''Nuestro !CookBook, en vías desarrollo.'' A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un cheff experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

<<TableOfContents>>

----

== Configuracion del entorno python ==

=== Crear un entorno virtual y un esqueleto de proyecto ===

[[Recetario/CreandoUnNuevoProyectoPython]]: Receta para crear un entorno de trabajo y un esqueleto minimo para un nuevo proyecto Python

=== Mejorando el interprete python ===
[[Recetario/AutocomplecionEnConsolaInteractiva| Autocompletado en consola interactiva]]: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython.

== Estructuras de datos ==
=== IterarSobrePares ===
== Expresiones regulares ==
=== Extraer todos los mails de un texto ===
/ExtraerMails de un texto utilizando el módulo re.

== Formatos, datos, números y conversiones ==
=== aLetras ===
[[aLetras]] : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

=== Reverse ===
[[Reverse]] : Función que invierte los caracteres.

=== validar_cuit ===
/ValidarCuit : Función para validar un CUIT/CUIL estilo 00-00000000-0

=== digito_verificador_modulo10 ===
/CalcularDigitoVerificadorModuloDiez : Función para generar el dígito verificador módulo 10

=== Normalizar caracteres Unicode ===
Es bueno /NormalizarCaracteresUnicode para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe.

ObtenerSensacionTermica: Calcular la Sensacion Termica o Temperatura Aparente.

== Frameworks Web ==
=== Django ===
[[Django/TestFormularioConFileUpload]] :  un ejemplo de como probar un formulario que tiene un campo para subir un archivo.

[[Django/ObtenerClaseOriginalCuandoHayHerencia]] : Cuando usamos herencia de modelos, si `bar` y `baz` son subclases de `foo`, podemos hacer que `foo.objects.all()` devuelva instancias de `bar` o `baz` dependiendo de cómo creamos el objeto orignalmente.

=== Bottle ===

[[Recetario/Bottle/HolaMundo|Hola Mundo]] : una aplicacion minima que muestra el mensaje hola mundo.

[[Recetario/Bottle/Galeria|Mini Galeria de Imagenes]] : una aplicacion minima que muestra una Galeria de Imagenes Animada.

== Interfaces graficas ==
=== Gtk ===
[[/Gui/Gtk/HolaMundo]] : una ventana que muestra el mensaje hola mundo

[[/Gui/Gtk/HolaMundoOO]] : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

[[/Gui/Gtk/Entry]] : una ventana que solicita un valor y luego lo muestra en una ventana aparte

[[/Gui/Gtk/EntrySoloNumeros]]: un ejemplo de como permitir el ingreso de solo numeros en un gtk.Entry

[[/Gui/Gtk/HBox]] : ejemplo que muestra como organizar elementos continuos horizontalmente

[[/Gui/Gtk/VBox]] : ejemplo que muestra como organizar elementos continuos verticalmente

[[/Gui/Gtk/Grid]] : ejemplo que muestra como organizar elementos en forma de grilla

[[/Gui/Gtk/Button]] : ejemplo que muestra como crear botones de diversas maneras

[[/Gui/Gtk/ButtonBox]] : ejemplo que muestra como crear botones y agruparlos en un contenedor

[[/Gui/Gtk/AutoComplete]] : ejemplo que muestra como crear un campo de texto con auto complesion

[[/Gui/Gtk/Dialog]] : ejemplo para crear dialogos modales

[[/Gui/Gtk/FileChooser]] : ejemplo que permite al usuario seleccionar un archivo

[[/Gui/Gtk/Menu]] :  ejemplo que mustra como crear un menu con distintos items

[[/Gui/Gtk/TextArea]] : ejemplo sobre manipulacion basica de un area de texto con scroll

[[/Gui/Gtk/PrintNonGtk]] : ejemplo sobre como usar el dialogo de impresion de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

[[/Gui/Gtk/RichText]]: ejemplo sobre como insertar texto con formato basico a un textview

[[/Gui/Gtk/ConfirmClose]]: ejemplo sobre como solicitar confirmacion para el cierre de una ventana

[[/Gui/Gtk/MultiThread]]: ejemplo de como manipular la GUI desde múltiples threads sin usar locks (con colas)

[[/Gui/Gtk/MultiThread2]]: ejemplo de como manipular la GUI usando múltiples threads

[[/Gui/Gtk/Runner]] ejemplo de como correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk

[[/Gui/Gtk/FuncionRunner]] idem al anterior pero usando una funcion en lugar de un objeto

[[/Gui/Gtk/LabelConColor]]: ejemplo de como cambiar el color de un label sin usar pango markup

[[/Gui/Gtk/XMLRPCServer]] Servidor XMLRPC dentro de un hilo gtk

[[/Gui/Gtk/StockItems]]: ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre

[[/Gui/Gtk/WebkitEditor]]: ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

[[/Gui/Gtk/StatusIcon]]: ejemplo de aplicación con ícono en el system tray.

[[/Gui/Gtk/ErrorHandler]]: un ejemplo de capturar una excepción y mostrarla en un dialogo modal

[[/Gui/Gtk/ListView]]: un ejemplo de como mostrar elementos en una 

[[/Gui/Gtk/EmuladorTerminal]]: un ejemplo de como hacer una terminal visual al estilo gnome-terminal

=== Gtk + glade ===
GtkGladeHolaMundoOO : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

GtkGladeSignals : manejo basico de señales

=== Qt ===
QtMultiThread : ejemplo de como manipular la GUI usando múltiples threads sin usar locks (con colas)

/QtImprimirPagina: ejemplo de como imprimir una pagina web a pdf

/QtExtraerTextoRecurso : como extraer un archivo de texto embebido en el sistema de recursos de !PyQt

=== Pythoncard (wxPython) ===
PythonCard: Ejemplo de como hacer una aplicación de escritorio desde 0 (para principiantes)

=== Tkinter + ttk ===
[[ttkHolamundo]]: una ventana que muestra el mensaje hola mundo (usando Tk themed widgets).

[[tkWindowIcon]]: una ventana con icono (usando Tk).

[[tkButtonIcon]]: unos botones con iconos, ideal mini-toolbar (usando Tk).

[[tkScrollWhell]]: usando la rueda de Scroll del raton (usando Tk).

[[tkOnlineOfflineIcon]]: Icono de On Line u Off Line simple (usando Tk).

[[tkVersionPrint]]: Obtener la version de TK que se esta usando.

[[GTKonTK]]: Usar temas de GTK en Tk ''(Hack)''.

[[TKWizards]]: Crear un Wizard amigable de multiples paginas (siguiente, siguiente, ... terminar)

[[DisplayLCD7Segmentos]]: Crear un Widget de Canvas tipo Display LCD de 7 Segmentos.

[[BotonGraficoTK]]: Crear botones graficos personalizados de 3 estados con TK.

[[VentanaPasswordVibra]]: Crear una ventana de password que Vibra si la password es incorrecta.

[[RelojDigital]]: Crear un Reloj Digital simple, trucando un Label.

== Emails ==
=== GMail ===
/GmailMail : Cómo enviar emails usando Gmail como SMTP

=== Email con adjuntos ===
/EmailConAdjunto : Cómo enviar emails con adjuntos binarios

== Creación de ejecutables para Windows ==
=== Desde Linux ===
/CrearEjecutableWindowsDesdeLinux : Cómo crear ejecutables para Windows desde Linux con Wine.

=== En Windows ===
/CrearEjecutableWindows: Cómo crear ejecutables para Windows nativamente.

== Hilos y concurrencia ==
=== threads ===
ComunicarThreadsConQueue: ejemplo sobre como comunicar y sincronizar threads usando colas

== Web ==
=== HTTP servers ===
==== Servidor Simple ====
ComoLevantarUnServidorHttpSimple  Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local

==== Servidor Multithread ====
ComoLevantarUnServidorHttpMultithread  Ejemplo sobre como levantar un servidor http que sirva el contenido de un directorio local manejando los requests con threads

== Xml ==
=== Xml a Diccionario ===
[[XmlADiccionario]]: este ejemplo muestra como convertir un string xml en un conjunto de diccionarios y listas anidadas, también provee de dos clases que permiten acceder a los diccionarios y listas como si fueran objetos.

=== SimpleXmlElement ===
SimpleXmlElement: ejemplo de manejo de xml por elementos simples (simil php), permite leer y/o crear xml accediendo a los tags como si fueran atributos de un objeto.

== Pdf ==
=== Generación de Facturas en PDF ===
/FacturaPyFpdf: Ejemplo de como generar una factura gráficamente en PDF utilizando PyFpdf

=== Modificación de Estilos en rst2pdf ===
/EstilosRst2Pdf: Explicación de Roberto Alsina, sobre cómo modificar los estilos de diseño en rst2pdf

== Dbf ==
=== Leer y modificar Archivos .DBF ===
/DbfPy: Ejemplo de como leer y modificar bases de datos en formato DBF

== Windows ==
=== Servidor Interfase C.O.M. ===
/ServidorCom: Ejemplo de como exponer objetos python a otros lenguajes (VB, VFP, etc.) vía interfase COM

== Python Internals ==
LocalsDeUnaFuncionQueLanzoUnaExcepcion: ejemplo de como obtener las variables locales a la función que lanzo una excepion

PsycoSpeedUp: Como acelerar las aplicaciones con Psyco, si esta presente.

MapeandoMemoria: Cómo generar un mapa de la memoria con heapy

== Numpy, Scipy, Matplotlib ==
[[/Histograma]]: Ejemplo sencillo de uso de la función ''hist''

== Administracion de Sistemas Operativos ==
/ListarProcesos: como listar procesos multiplataforma

/ChequearInterfacesInternetLinux

[[Xdg-Sudo]]: El sudo Grafico Universal, para Escritorios GTK/QT/whatever, inspirado en ''xdg-open'' de Linux.

[[Chequeo de Paquetes, APT, Linux]]: Chequear si un Programa esta instalado, o no, y si existe en Linux.

== Internet ==
/RevisarConexion: revisar si estamos conectados a internet conexión.

/ObtenerBytesTransferidos: obtener la cantidad de datos transferidos en Bytes.

[[ipPublica]] : obtener la direccion ip publica usando 3 lineas de Python.

/ObtenerUbicacionGeografica: obtener datos de la ubicacion geografica (Geo-Location) usando Python-Geoip.

== Misceláneo ==
/MatrixPythonToy: Efecto "The Matrix" en linea de comandos, ideal CLI Screen Saver / Screen Lock.

/SaberSiNlibreriaEstaInstalada: Saber si N Libreria esta instalada sin ingresar al interprete de Python.

/PythonVersionCheck: Chequea la version de Python, y sale o imprime error en funcion de eso.

/RootCheck: Comprobar si somos root y actuar en funcion de eso, orientado a Linux.

/ComoBajarTodosLosBuffersAlDisco: Best Practice para un programa en Linux para cerrarse.

/ProgressbarUrllib2: Como descargar algo de internet y mostrar una barrita de progreso.

/CheckDistroVersion: Chequea la version de la Distribucion Linux y actuar en funcion de eso.

/AlarmaPrecaria: Alarma minima y basica de linea de comandos.

/KeyboardLedsDemo: Como controlar los Leds del Teclado con Python.

/NotificarDispositivosUsb : Como detectar y notificar dispocitivos USB en Linux.

== Python en Apache OpenOffice / LibreOffice ==

== Crypto ==

[[/Crypto/BlowfishConBlowfishpy]]: como encriptar usando el modulo blowfish.py

== Divertidos ==

[[/Fun/NadoSincronizado]]: bailarín de nado sincronizado en tu consola!

[[/Fun/NadoSincronizadoDisco]]: bailarín de nado sincronizado en tu consola con luces de colores!

----
CategoryRecetas
