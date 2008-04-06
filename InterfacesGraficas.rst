== Interfaces Gráficas (GUI) ==

Existen varias librerias que implementan interfaces gráficas de usuario (GUI) en python, las principales son:
 * Tkinker: Basada en las librerías gráficas TK/TCL, interface "de-facto" preinstalada con python.
 * WxPython: Basada en WxWidgets (una libreria multiplataforma C/C++), "bendecida" por GvR como la "más pitónica"
 * PyQT: basado en la libreria C++ QT (KDE)
 * PyGTK: basado en la libreria C GTK (GNOME)

=== Tabla comparativa ===

|| Caracteristica || Tkinker || WxPython ||  PyQT || PyGTK ||
|| Portabilidad || "Completa" (en donde funcione python) || Windows, Linux (GTK+/X11/Motif), Mac OS X || Windows, Linux, Mac OS X || Windows, Linux, Mac OS X (via servidor de X) ||
|| Diseñadores "Visual" || N/A || wxGlade/XRCed || Qt Designer || Glade ||
|| Formato XML || No || sí (XRC) || ?? || sí (c/libglade) ||
|| Otras facilidades || N/S N/C || soporte para imagenes (BMP, PNG, JPG, etc.), visualización e impresión de HTML, clipboard y drag and drop, ayuda en linea, gráficos vectorialse, OpenGL, programación en red, flujos,  multitarea, bases de datos, soporte ansi y unicode || sockets, hilos, Unicode, expresiones regulares, bases de datos SQL, SVG, OpenGL, XML || Pango (texto multilingual), Cairo (gráficos 2D), ATK (accesibilidad) ||
|| Tamaño aprox. (instalador windows desarrollo) || "0KB" (viene con Python) || 8.12MB || 15.6MB || 15.5MB ||

=== Ventajas y Desventajas ===

Yo empece usando WxPython (bind a python de WxWindows), que a diferencia de PyGTK (creo) y PyQT, no necesitan de instalar ninguna libreria extra en la pc destino, solo el paquete WxPython en tu maquina de desarrollo, despues podes distrubuir exe de windows con py2exe. 
Hasta ahora nunca tuve dramas con Wx, salvo cuando me puse a probar en Linux donde me esta dando errores, wxGtk es horrible... pero te el codigo, tal cual lo tengo corriendo en Windows corrio de una en Linux sin un cambio, salvo estos errores de Gtk que aun no se porque suceden... 
Tengo un par de libros, WxPython in Action y un manual de SPE, que junto con el manual de python es toda la doc. de referencia que necesitas para hacer programas GUI WxWindow.
