#language es
#pragma section-numbers 2
= Recetario =
''Nuestro !CookBook, en vías desarrollo.'' A este lugar uno recurre cada vez que se encuentra en la cocina de Python, cuchillo en mano y se da cuenta que a sus ingredientes le faltan el toque de un cheff experto. Nuestra especialidad son las recetas autóctonas. ¿Platos magistrales que fallan al sazonar con acentos y eñes? ¿números que saben mal si no son previamente fritos en castellano? ¡Siga leyendo!

<<TableOfContents>>
----

== Configuracion del entorno python ==
=== Mejorando el interprete python ===
AutocomplecionEnConsolaInteractiva: tip sobre como agregar autocompleción con tab en la consola interactiva imitando el comportamiento ipython.

== Formatos, datos, números y conversiones ==
=== aLetras ===
[[aLetras]] : Función que al recibir un número lo convierte a letras. Regresa su forma por extensión (ejemplo: 123 -> "CIENTO VEINTITRES")

=== validar_cuit ===
/ValidarCuit : Función para validar un CUIT/CUIL estilo 00-00000000-0

=== digito_verificador_modulo10 ===
/CalcularDigitoVerificadorModuloDiez : Función para generar el dígito verificador módulo 10

=== Normalizar caracteres Unicode ===
Es bueno /NormalizarCaracteresUnicode para hacer búsquedas en strings sin que se tengan en cuenta los caracteres latinos, como los acentos y la eñe.

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

GtkDialog : ejemplo para crear dialogos modales

GtkFileChooser : ejemplo que permite al usuario seleccionar un archivo

GtkMenu :  ejemplo que mustra como crear un menu con distintos items

GtkTextArea : ejemplo sobre manipulacion basica de un area de texto con scroll

GtkPrintNonGtk : ejemplo sobre como usar el dialogo de impresion de gtk en aplicaciones no gtk (que no usan el main loop de gtk)

[[GtkRichText]]: ejemplo sobre como insertar texto con formato basico a un textview

[[GtkConfirmClose]]: ejemplo sobre como solicitar confirmacion para el cierre de una ventana

[[GtkMultiThread]]: ejemplo de como manipular la api desde múltiples threads sin usar locks (con colas)

[[GtkMultiThread2]]: ejemplo de como manipular la api desde múltiples threads

=== Gtk + glade ===
[[GtkGladeHolaMundoOO]] : una ventana que muestra el mensaje hola mundo programado utilizando orientacion a objetos

GtkGladeSignals : manejo basico de señales

=== Pythoncard (wxPython) ===

PythonCard: Ejemplo de como hacer una aplicación de escritorio desde 0 (para principiantes)

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
