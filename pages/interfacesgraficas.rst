
Interfaces Gráficas (GUI)
-------------------------

**Advertencia**: Esta página esta basada (en parte) en opiniones y experiencias personales de distintas personas. YMMV

Existen varias librerias que implementan interfaces gráficas de usuario (GUI) en python, las principales son:

* Tkinter: Basada en las librerías gráficas TCL/TK, interface "de-facto" (`#1`_) preinstalada con python, es la generalmente recomendada para proyectos triviales y/o de aprendizaje.

* WxPython_: Basada en WxWidgets_ (una libreria multiplataforma C/C++), "bendecida" (`#2`_) como la "más pitónica" por GvR (creador de Python), y sería la interface por defecto si no hubiese existido TK en primer lugar.

* PyQT: basado en la libreria C++ QT (KDE)

* PyGTK: basado en la libreria C GTK (GNOME)

Tabla comparativa
~~~~~~~~~~~~~~~~~

[Table not converted]

Características comunes
~~~~~~~~~~~~~~~~~~~~~~~

* Tamaño aprox. (instalador windows desarrollo): 15MB (excepto tkinter que viene preinstalado)

* Huella en memoria (footprint) de hello-word en windows: aproximadamente 20MB, excepto tkinter que es la mitad

Ventajas y Desventajas
~~~~~~~~~~~~~~~~~~~~~~

Tkinter
:::::::

* Ventajas:

  * Preinstalado con python en casi todas las plataformas

  * Relativamente simple y fácil de aprender (recomendado para "aprendices")

  * Documentación completa

* Desventajas:

  * Pocos elementos gráficos (sin listados, arboles, etc.)

  * Limitado control del comportamiento de la interface (recomendado para proyectos "triviales")

  * Lento (dibuja cada botón, etiqueta, menú, etc.) **

  * Apariencia "extraña" (no se parece a las aplicaciones nativas) **

Nota \**: cabe aclarar que las ultimas versiones de TCL/TK mejoran varios de estos puntos, dibujando con las funciones nativas de la plataforma, lo que acelera y mejora la apariencia.

WxPython
::::::::

* Ventajas:

  * Completo conjunto de elementos gráficos (listados, arboles, grillas, etc.)

  * Flexible control del comportamiento de la interface

  * Rápido y de Apariencia nativa (diseñado para utilizar funciones nativas de cada plataforma)

  * "Baterias Incluidas": más de 12 librerias y utilitarios complementarios (ver comparación)

  * Independencia: no esta orientado a ningún entorno, ni QT ni GTK, hay una capa mas que agrega un grado de libertad adicional

  * No se cierra en el mínimo denominador común; soporta las características comunes de Windows, y las emula en Linux/Mac OS cuando no se pueden hacer nativamente (y viceversa).

  * Es mas "pitónico", por ej. espacio de nombres mas claro, sin referencias a C/C++, etc.

  * Permite separar completamente el diseño de la interface en XML del código python (XRC)

  * Es fácil armar componentes personalizados, tanto que incorpora widgets que no están en wxWidgets mismo, ya que están escritos en Python (AGW_).

  * Documentación completa y ejemplos extensivos.

  * Su lista oficial de usuarios (wxpython-users_) es *muy* activa y amigable, donde participan los desarrolladores principales del proyecto.

* Desventajas:

  * No viene preinstalado con python, se debe instalar un paquete (wxPython en Windows y Mac OS,  wxWidgets+wxPython en Linux, aunque en este último caso está generalmente está fácilmente disponible en los repositorios).

  * Relativamente mas complejo de aprender

  * Al tener un desarrollo bastante rápido y sostenido, se liberan versiones frecuentemente, lo que en la práctica le confiere cierto nivel de "volatilidad" y problemas de compatibilidad si se deben mantener varias versiones de wx para el mismo código.

  * Es una capa más sobre el toolkit gráfico que se usa debajo (ej: GTK).

  * Las características emuladas de otras plataformas no siempre se ven bien.

  * Hacer interfaces multiplataformas que se vean bien requiere conocimiento del toolkit subyacente (win32, gtk).

  * En proyectos medianos/grandes, puede ser inestable y dificil de debuggear: en windows es muy facil segfaultear si se pasan parámetros incorrectos.

PyQt
::::

* Ventajas:

  * Completo conjunto de elementos gráficos (listados, arboles, grillas, etc.)

  * Flexible y potente control del comportamiento de la interface.  Posee un mecanismo de conexión de señales y eventos simple. Se puede definir los eventos más sencillos en diseñaodr de GUI's (ej: al pulsar este botón, borrar este campo de texto) y en el código python, definir las acciones más avanzadas.

  * Rápido y de Apariencia nativa (las últimas versiones utilizan funciones nativas en windows)

  * Se puede separar el diseño de la interface, pero usa un "compilador" pyuic para crear las clases python.

  * Arquitectura opcional para Modelo/Vista para las tablas, listas y árboles.

* Desventajas:

  * No viene preinstalado con python, se debe instalar por separado

  * Relativamente mas complejo de aprender

  * No del todo "pitónico". En ocasiones emerge la implentación en C++ subyacente, teniendo que hacer casts entre tipos de datos, etc. El prefijo Qt/Q (QtGUI, QWidget, QAplicattion) hace el código menos "pitónico"

  * No hay mucha documentación específica a python, ya que es lenguaje en si no es demasiado considerado

PyGTK
:::::

* Ventajas:

  * Completo conjunto de elementos gráficos (listados, arboles, grillas, etc.)

  * Flexible y potente control del comportamiento de la interface

  * Enlace con PyOrbit_ para programar aplicaciones en GNOME

  * Es estable, y los mensajes de error son correctos.

* Desventajas:

  * No viene preinstalado con python, se debe instalar por separado

  * Relativamente mas complejo de aprender

  * Relativamente lento en Windows (dibuja cada botón, etiqueta, menú, etc.) lo que le da una Apariecia "extraña" (aunque es parecido a windows)

  * En windows, es la librería que tiene mas dependencias y se instalan por separado.

  * Aparentemente tiene la documentación mas precaria de todos

Hello World
~~~~~~~~~~~

**Nota**: para poder comparar, los ejemplos crean una aplicación, ventana y botón, con un evento.

Hay mas ejemplos en el `Recetario#Interfaces_graficas`_

TkInter
:::::::

::

   from Tkinter import *

   class App:
       def __init__(self, master):
           frame = Frame(master)
           frame.pack()
           self.hi_there = Button(frame, text="Hola", command=self.say_hi)
           self.hi_there.pack(side=LEFT)
       def say_hi(self):
           print "hola todo el mundo!"

   root = Tk()
   app = App(root)
   root.mainloop()

WxPython
::::::::

::

   import wx
   class MyFrame(wx.Frame):
       def __init__(self, parent, title):
           wx.Frame.__init__(self, parent, -1, title )
           btn = wx.Button(self, -1, "Hola")
           self.Bind(wx.EVT_BUTTON, self.say_hello, btn)

       def say_hello(self,*arg):
           print "hola todo el mundo!"

   class MyApp(wx.App):
       def OnInit(self):
           frame = MyFrame(None, "Simple wxPython App")
           frame.Show(True)
           return True
   MyApp().MainLoop()

PyQt
::::

::

   from PyQt4 import QtCore, QtGui
   import sys

   class MiVentana(QtGui.QWidget):
       def __init__(self, padre = None):
           super(MiVentana, self).__init__(padre)
           self.button = QtGui.QPushButton("Hola",self)
           self.connect(self.button, QtCore.SIGNAL("clicked()"), self.say_hello)
           self.show()
       def say_hello(self,**kwargs):
           print "hola mundo!"

   app = QtGui.QApplication(sys.argv)
   v = MiVentana()
   app.exec_()

PyGTK
:::::

::

   import pygtk
   pygtk.require('2.0')
   import gtk

   class HelloWorld:
       def __init__(self):
           self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
           self.button = gtk.Button("Hello World")
           self.button.connect("clicked", self.say_hello, None)
           self.window.add(self.button)
           self.button.show()
           self.window.show()

       def main(self):
           gtk.main()

       def say_hello(self, widget, data=None):
           print "Hello World"


   hello = HelloWorld()
   hello.main()

(sin testear)

Referencias
~~~~~~~~~~~

* .. _1:

   http://wiki.python.org/moin/TkInter

* .. _2:

   http://wxpython.org/quotes.php

* http://www.riverbankcomputing.co.uk/pyqt/index.php

* http://live.gnome.org/PyGTK

* http://mail.python.org/pipermail/python-list/2001-December/116978.html

* http://wiki.wxpython.org/ComparingWxPythonAndPyQt

* http://www.wxwidgets.org/about/feature2.htm

* Lista de PyAr_

.. ############################################################################

.. _#1: /pages/interfacesgraficas#1



.. _#2: /pages/interfacesgraficas#2

.. _wxFormBuilder: http://wxformbuilder.org



.. _PySide: http://www.pyside.org

.. _AGW: http://xoomer.virgilio.it/infinity77/main/freeware.html

.. _wxpython-users: http://groups.google.com/group/wxpython-users




.. _pyar: /pages/pyar
