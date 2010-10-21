#language es
#pragma section-numbers 2
= Recetario =
''Nuestro !CookBook, en vías desarrollo.'' A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un cheff experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

<<TableOfContents>>

----

== Configuracion del entorno python ==
=== Mejorando el interprete python ===
AutocomplecionEnConsolaInteractiva: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython.

== Estructuras de datos ==
=== IterarSobrePares ===
Cómo IterarSobrePares de una secuencia.

== Expresiones regulares ==
=== Extraer todos los mails de un texto ===
/ExtraerMails de un texto utilizando el módulo re.

== Formatos, datos, números y conversiones ==
=== aLetras ===
[[aLetras]] : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

=== validar_cuit ===
/ValidarCuit : Función para validar un CUIT/CUIL estilo 00-00000000-0

=== digito_verificador_modulo10 ===
/CalcularDigitoVerificadorModuloDiez : Función para generar el dígito verificador módulo 10

=== Normalizar caracteres Unicode ===
Es bueno /NormalizarCaracteresUnicode para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe.

== Frameworks Web ==
=== Django ===
[[Django/TestFormularioConFileUpload]] :  un ejemplo de como probar un formulario que tiene un campo para subir un archivo.

[[Django/ObtenerClaseOriginalCuandoHayHerencia]] : Cuando usamos herencia de modelos, si `bar` y `baz` son subclases de `foo`, podemos hacer que `foo.objects.all()` devuelva instancias de `bar` o `baz` dependiendo de cómo creamos el objeto orignalmente.

== Interfaces graficas ==
=== Gtk ===
GtkHolaMundo : una ventana que muestra el mensaje hola mundo

[[GtkHolaMundoOO]] : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

GtkEntry : una ventana que solicita un valor y luego lo muestra en una ventana aparte

GtkEntrySoloNumeros: un ejemplo de como permitir el ingreso de solo numeros en un gtk.Entry

[[GtkHBox]] : ejemplo que muestra como organizar elementos continuos horizontalmente

[[GtkVBox]] : ejemplo que muestra como organizar elementos continuos verticalmente

GtkGrid : ejemplo que muestra como organizar elementos en forma de grilla

GtkButton : ejemplo que muestra como crear botones de diversas maneras

GtkButtonBox : ejemplo que muestra como crear botones y agruparlos en un contenedor

GtkAutoComplete : ejemplo que muestra como crear un campo de texto con auto complesion

GtkDialog : ejemplo para crear dialogos modales

GtkFileChooser : ejemplo que permite al usuario seleccionar un archivo

GtkMenu :  ejemplo que mustra como crear un menu con distintos items

GtkTextArea : ejemplo sobre manipulacion basica de un area de texto con scroll

GtkPrintNonGtk : ejemplo sobre como usar el dialogo de impresion de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

GtkRichText: ejemplo sobre como insertar texto con formato basico a un textview

GtkConfirmClose: ejemplo sobre como solicitar confirmacion para el cierre de una ventana

GtkMultiThread: ejemplo de como manipular la GUI desde múltiples threads sin usar locks (con colas)

GtkMultiThread2: ejemplo de como manipular la GUI usando múltiples threads

GtkLabelConColor: ejemplo de como cambiar el color de un label sin usar pango markup

[[/GtkXMLRPCServer]] Servidor XMLRPC dentro de un hilo gtk

/GtkStockItems: ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre

/GtkWebkitEditor: ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

/GtkStatusIcon: ejemplo de aplicación con ícono en el system tray.

=== Gtk + glade ===
[[GtkGladeHolaMundoOO]] : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

GtkGladeSignals : manejo basico de señales

=== Qt ===
QtMultiThread : ejemplo de como manipular la GUI usando múltiples threads sin usar locks (con colas)

/QtImprimirPagina: ejemplo de como imprimir una pagina web a pdf

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

== Internet ==
/RevisarConexion: revisar si estamos conectados a internet conexión.

/ObtenerBytesTransferidos: obtener la cantidad de datos transferidos en Bytes.

== Misceláneo ==
/MatrixPythonToy: Efecto "The Matrix" en linea de comandos, ideal CLI Screen Saver / Screen Lock.

/SaberSiNlibreriaEstaInstalada: Saber si N Libreria esta instalada sin ingresar al interprete de Python.

/PythonVersionCheck: Chequea la version de Python, y sale o imprime error en funcion de eso.

/RootCheck: Comprobar si somos root y actuar en funcion de eso, orientado a Linux.

/CerrarCorrectamenteTuPrograma: Best Practice para un programa en Linux para cerrarse.
