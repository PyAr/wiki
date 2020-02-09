
Servidor Interfase COM
----------------------

Descripción
:::::::::::

Esta receta es un ejemplo de como crear un Servidor COM_ para poder exponer nuestros objetos Python y así accederlos desde otros lenguajes (Visual Basic, Visual Fox Pro, PHP, Java, .NET, etc.)

Esto nos permite utilizar las características de Python facilmente desde otros entornos, posibilitando extender o adaptar código ya desarrollado en otros lenguajes.

Es necesario instalar `Extensiones Win32`_ (ver Bibliografia_)

Ejemplo:
::::::::

El ejemplo en Python (miservidorcom.py) registra un objeto python MiMiniInterpretePython_, exponiendo:

* Atributo Version: almacena la versión del interprete

* Método Evaluar: evalua la expresión python recibida y devuelve su resultado

Archivo miservidorcom.py

::

    # -*- coding: iso-8859-1 -*-

    import sys

    class MiMiniInterpretePython:
        _public_methods_ = ['Evaluar']    # Métodos a exportar por el servidor COM
        _public_attrs_ = ['Version']      # Atributos a exportar por el servidor COM
        _readonly_attrs_ = _public_attrs_ # Atributos de solo lectura
        _reg_progid_ = "MiMiniInterpretePython"   # Nombre para Crear el Objeto COM
        # NUNCA copiar el siguiente ID 
        # Usar "print pythoncom.CreateGuid()" para crear uno nuevo
        _reg_clsid_ = "{ECDDA31C-2999-4C77-9778-DDF75FBF81FC}"

        def __init__(self):
            # constructor, setear atributos:
            self.Version = sys.version

        def Evaluar(self, expresion):
            "Evalua una expresión python y devuelve su resultado"
            return eval(expresion)


    # Agregar código para que si este script es ejecutado por linea de comando,
    # por Python.exe, se auto-registre
    if __name__=='__main__':
        import win32com.server.register
        win32com.server.register.UseCommandLine(MiMiniInterpretePython)


Para poder usarlo desde otros lenguajes, registrar el servidor COM ejecutando desde línea de comando:

::

   python miservidorcom.py --register

El siguiente ejemplo en Visual Basic (modulo1.bas) crea el objeto COM ("instanciando" MiMiniInterpretePython_) y muestra el atributo (Version), y luego solicita expresiones para evaluar en python.

Archivo modulo1.bas:

::

   Sub Main()

       ' Creo el objeto Python exportado por el Servidor COM:
       Set ObjetoPython = CreateObject("MiMiniInterpretePython")
      
       ' Obtengo un atributo del objeto python:
       Version = ObjetoPython.Version
       MsgBox Version, , "Versión de Python:"

       Do
           Expresion = InputBox("Ingrese una expresión python para ser evaluada", "Ejemplo COM", "1+2")
           If Expresion = "" Then Exit Sub
           ' Llamo al método del objeto python:
           Resultado = ObjetoPython.Evaluar(Expresion)
           MsgBox Resultado, , "Resultado:"
       Loop
     
   End Sub

Ejemplo en Visual Fox Pro:

::

   * instancio el objeto python via COM:
   ObjetoPython = CREATEOBJECT("MiMiniInterpretePython")

   * muestro el atributo versión:
   version = ObjetoPython.Version
   MESSAGEBOX("Versión de Python: " + version, 0)

   * muestro el resultado de evaluar una expresión llamando al método vía COM:
   expresion = "' '.join(['hola','mundo'])"
   resultado = ObjetoPython.Evaluar(expresion)
   MESSAGEBOX(resultado, 0)

Para generar una DLL o EXE y poder distribuir el servidor com sin necesidad de tener instalado Python, usar Py2Exe_ con el siguiente script de directivas de instalación (ver CrearEjecutableWindows_):

::

    from distutils.core import setup
    import py2exe

    setup( name = "MiServidorCOM",
        com_server = ["miservidorcom"],
           )


Ejecutar Py2Exe_ para crear el EXE, DLL y demás archivos de distribución (carpeta dist):

::

   python setup.py py2exe

Luego, registrar el servidor COM por línea de comando:

::

   miservidorcom.exe --register

o

::

   regsvr32 miservidorcom.dll

Para Descargar Fuentes: 

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _COM: http://es.wikipedia.org/wiki/Component_Object_Model

.. _Extensiones Win32: http://starship.python.net/crew/mhammond/win32/Downloads.html

.. _Bibliografia: http://oreilly.com/catalog/pythonwin32/chapter/ch12.html


.. _py2exe: /pages/py2exe/index.html
.. _marianoreingart: /pages/marianoreingart/index.html
.. _categoryrecetas: /pages/categoryrecetas/index.html
