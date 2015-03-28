#format rst

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

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: iso-8859-1 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">MiMiniInterpretePython</span><span class="p">:</span>
      </span><span class="line">    <span class="n">_public_methods_</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;Evaluar&#39;</span><span class="p">]</span>    <span class="c"># Métodos a exportar por el servidor COM</span>
      </span><span class="line">    <span class="n">_public_attrs_</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;Version&#39;</span><span class="p">]</span>      <span class="c"># Atributos a exportar por el servidor COM</span>
      </span><span class="line">    <span class="n">_readonly_attrs_</span> <span class="o">=</span> <span class="n">_public_attrs_</span> <span class="c"># Atributos de solo lectura</span>
      </span><span class="line">    <span class="n">_reg_progid_</span> <span class="o">=</span> <span class="s">&quot;MiMiniInterpretePython&quot;</span>   <span class="c"># Nombre para Crear el Objeto COM</span>
      </span><span class="line">    <span class="c"># NUNCA copiar el siguiente ID </span>
      </span><span class="line">    <span class="c"># Usar &quot;print pythoncom.CreateGuid()&quot; para crear uno nuevo</span>
      </span><span class="line">    <span class="n">_reg_clsid_</span> <span class="o">=</span> <span class="s">&quot;{ECDDA31C-2999-4C77-9778-DDF75FBF81FC}&quot;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="c"># constructor, setear atributos:</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">Version</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span>
      </span><span class="line">   
      </span><span class="line">    <span class="k">def</span> <span class="nf">Evaluar</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">expresion</span><span class="p">):</span>
      </span><span class="line">        <span class="s">&quot;Evalua una expresión python y devuelve su resultado&quot;</span>
      </span><span class="line">        <span class="k">return</span> <span class="nb">eval</span><span class="p">(</span><span class="n">expresion</span><span class="p">)</span>
      </span><span class="line">   
      </span><span class="line">
      </span><span class="line"><span class="c"># Agregar código para que si este script es ejecutado por linea de comando,</span>
      </span><span class="line"><span class="c"># por Python.exe, se auto-registre</span>
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span><span class="o">==</span><span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">win32com.server.register</span>
      </span><span class="line">    <span class="n">win32com</span><span class="o">.</span><span class="n">server</span><span class="o">.</span><span class="n">register</span><span class="o">.</span><span class="n">UseCommandLine</span><span class="p">(</span><span class="n">MiMiniInterpretePython</span><span class="p">)</span>
      </span>

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

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">distutils.core</span> <span class="kn">import</span> <span class="n">setup</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">py2exe</span>
      </span><span class="line">
      </span><span class="line"><span class="n">setup</span><span class="p">(</span> <span class="n">name</span> <span class="o">=</span> <span class="s">&quot;MiServidorCOM&quot;</span><span class="p">,</span>
      </span><span class="line">    <span class="n">com_server</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;miservidorcom&quot;</span><span class="p">],</span>
      </span><span class="line">       <span class="p">)</span>
      </span>

Ejecutar Py2Exe_ para crear el EXE, DLL y demás archivos de distribución (carpeta dist):

::

   python setup.py py2exe

Luego, registrar el servidor COM por línea de comando:

::

   miservidorcom.exe --register

o

::

   regsvr32 miservidorcom.dll

Para Descargar Fuentes: `attachment:ejemplo.zip`_ejemplo.zip`attachment:None`_

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _COM: http://es.wikipedia.org/wiki/Component_Object_Model

.. _Extensiones Win32: http://starship.python.net/crew/mhammond/win32/Downloads.html

.. _Bibliografia: http://oreilly.com/catalog/pythonwin32/chapter/ch12.html

.. _CrearEjecutableWindows: ../CrearEjecutableWindows

