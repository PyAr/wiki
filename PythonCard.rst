
PythonCard
==========

Introducción
------------

PythonCard es un conjunto de herramientas de construcción GUI para crear aplicaciones de escritorio multiplataforma en Windows, Mac OS X, y Linux, usando Python.

La motivación de PythonCard es "Las cosas simples deberían ser simples, y las complejas deberían ser posibles"

PythonCard es para vos si queres desarrollar aplicaciones gráficas de manera rápida y fácil con un mínimo esfuerzo y código. Es parecido a **Visual Basic Clásico**, con respecto a la creación visual de interfaces gráficas y programación por eventos.

PythonCard usa wxPython. Si estás familiarizado con wxPython, se puede ver a PythonCard como una manera simple de hacer programas wxPython con un gran conjunto de ejemplos y herramientas que se pueden copiar y mejorar para crear aplicaciones multiplataforma.

Como instalar PythonCard:
-------------------------

Linux (Debian y derivados)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pythoncard esta soportado en Etch, así que su instalación es bastante simple

::

   .. raw:: html
      <span class="line">apt-get install pythoncard
      </span>

Windows
~~~~~~~

* Bajar e instalar Python desde `www.python.org, Downloads, Windows Installer Python 2.5.2`_. 

* Bajar e instalar wxPython desde `wxPython.org, Binaries, win32 unicode`_. 

* Bajar e instalar PythonCard `pythoncard.sourceforge.net, Downloads, PythonCard 0.8.2 win32`_. 

Ejemplos
--------

Si todo se instaló correctamente, podemos probar los ejemplos que vienen con PythonCard, menú Inicio, PythonCard, Sample Launcher (o buscar el script en C:\Python25\Lib\site-packages\PythonCard\samples\samples.pyw o similar para la plataforma en que estemos). Debería aparecer la pantalla de ejemplos (ver `sitio de PythonCard`_). En ella se puede encontrar los programas de ejemplos en las siguientes categorías:

* **Bases de datos** (altas, bajas, modificaciones y consultas): addresses, companies, custdb, dbBrowser, flatfileDatabase, gadflyDatabase

* **Juegos**: tictactoe (ta-te-ti), turtle (tortuga = lenguaje logo), life (juego de la vida), reversi, sodoku

* **Gráficos**: doodle (mano alzada), spirograph (espirografía), lsystem (fractales Lindenmayer), hopalong (fractales)

* **Demostración del entorno**: proof, dialogs, minimal, minimalStandalone, noresource, pictureViewer, saveClipboardBitmap, simpleBrowser, simpleIEBrowser, samples, widgets 

* **Internet**: chat, jabberChat, pysshed, radioclient, SourceForgeTracker_, searchexplorer, stockprice, textRouter, webgrabber, webserver

* **Utilitarios**: conversions (ºC a ºF), redemo (expresiones regulares), rpn (calculadora de impuestos)

* **Varios**: mp3player, slideshow (presentaciones html), sounds (sonidos wab), textIndexer, worldclock

Si algo anda mal y no se muestra la pantalla de ejemplos, podemos probar lo siguiente para ver que esta fallando en una consola Python:

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">wx</span>
      </span><span class="line"><span class="n">wx</span><span class="o">.</span><span class="n">version</span><span class="p">()</span> <span class="c"># debería imprimir &#39;2.8.7.1 (msw-unicode)&#39; o similar</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">PythonCard</span> <span class="kn">import</span> <span class="n">model</span>
      </span><span class="line"><span class="n">rsrc</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;application&#39;</span><span class="p">:{</span><span class="s">&#39;type&#39;</span><span class="p">:</span><span class="s">&#39;Application&#39;</span><span class="p">,</span> <span class="s">&#39;name&#39;</span><span class="p">:</span><span class="s">&#39;Minimal&#39;</span><span class="p">,</span>
      </span><span class="line">    <span class="s">&#39;backgrounds&#39;</span><span class="p">:</span> <span class="p">[{</span><span class="s">&#39;type&#39;</span><span class="p">:</span><span class="s">&#39;Background&#39;</span><span class="p">,</span><span class="s">&#39;name&#39;</span><span class="p">:</span><span class="s">&#39;bgMin&#39;</span><span class="p">,</span>
      </span><span class="line">        <span class="s">&#39;title&#39;</span><span class="p">:</span><span class="s">&#39;Prueba&#39;</span><span class="p">,</span><span class="s">&#39;size&#39;</span><span class="p">:(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">100</span><span class="p">),</span><span class="s">&#39;components&#39;</span><span class="p">:</span> <span class="p">[]}]}</span> <span class="p">}</span>
      </span><span class="line">
      </span><span class="line"><span class="n">model</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">Background</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">rsrc</span><span class="p">)</span><span class="o">.</span><span class="n">MainLoop</span><span class="p">()</span>
      </span>

Debería aparecer una ventanita con título "Prueba".

Además, PythonCard dispone de características de depuración (depurar menú, loggeo, visor de mensajes, visor del espacio nombres, editor de propiedades, shell). Estas opciones se pueden activar al ejecutar los ejemplos para ver como funcionan.

Editor de Pantallas
-------------------

PythonCard viene con un editor de pantallas (resource/layout editor), se encuentra en el menu Inicio, PythonCard, Layout Editor (o buscar el script en C:\Python25\Lib\site-packages\PythonCard\tools\resourceEditor\layoutEditor.py o similar para la plataforma en que estemos). Debería aparecer la pantalla de edición (ver imágenes y más información en `sitio de PythonCard <http://pythoncard.sourceforge.net/resource_editor_overview.html>`__):

`pycard1.png </wiki/PythonCard/attachment/32/pycard1.png>`_

Ejemplo de como crear una aplicación de prueba (que tome una expresión/comando python ingresado por el usuario y devuelva su resultado):

* Ir al menú *File*, *New*, aparece un miniasistente para crear la aplicación

* Seleccionar "Standard Template with File/Exit Menu" (Plantilla estandard con menú File/Exit)

* Ingresar el nombre y ubicación de la aplicación, ej "Prueba" en el escritorio o carpeta personal. 

* Se Generará los siguientes archivos:

  * ``prueba.py``: programa python que contendrá el comportamiento a los eventos y demás funcionalidades

  * ``prueba.rsrc.py``: archivo python que define la interfaz gráfica

* Agregamos los componentes (ver el diseño de pantalla en la última sección):

  * Etiqueta: menú *Component*, *Static Text* (la seleccionamos y en la pantalla de propiedades cambiamos el *Label*: Comando)

  * Campo de Texto: menú *Component*, *Text Field* (la seleccionamos y movemos a continuación de la etiqueta, en las propiedades marcar *Vary*, cambiar *Name*: txtComando y *Text*: en blanco )

  * Área de Texto: menú *Component*, *Text Area* (lo seleccionamos, movemos a donde corresponda, en las propiedades marcar *Vary*, escribir en *Name*: txtResultados y en *Text*: en blanco)

  * Botón: menú *Component*, *Button* (lo seleccionamos, movemos a donde corresponda, en las propiedades marcar *Vary*, escribir en *Name*: btnEjecutar y en *Label*: Ejecutar )

* Agregamos un menu de ayuda:

  * Ir al menú *Edit*, *Menu Editor*:

    * Marcar *File*, presionar *New Menu Item*, y escribir en *Label*: Ayuda

    * Presionar *Ok* para aceptar

* Probamos que quede bien, yendo al menú *File*, *Run* (obviamente no va a hacer nada más que aparecer en la pantalla, sin ningún comportamiento)

* Grabamos con el menú *File*, *Save*

Editor de Código
----------------

PythonCard viene tambien con un editor de código, se encuentra en el menú Inicio, PythonCard, Code Editor (o buscar el script en C:\Python25\Lib\site-packages\PythonCard\tools\resourceEditor\codeEditor.py o similar para la plataforma en que estemos). También esta el *Tabbed Code Editor* que nos permite editar múltiples archivos y seleccionar los componentes y sus eventos. Debería aparecer la pantalla de edición de código (ver imágenes y más información en `sitio de PythonCard <http://pythoncard.sourceforge.net/tools/codeEditor.html>`__):

`pycard2.png </wiki/PythonCard/attachment/33/pycard2.png>`_

Continuando con el ejemplo de como crear una aplicación de prueba (ver sección anterior):

* Ir al menú *File*, *Open*, abrir el archivo ``prueba.py`` generado anteriormente

* Aparecerá el script genérico (plantilla) creado en la sección anterior, al que le falta agregar el comportamiento frente a los eventos (ver el código completo al final):

  * Agregar ``from PythonCard import dialog`` para poder utilizar los dialogos

  * Agregar el método on_btnEjecutar_mouseClick (evento click del mouse sobre el botón Ejecutar)

  * Agregar el método on_menuFileAyuda_select (evento selección del menú File | Ayuda)

* Para probar el código, ir al menú *File*, *Run*, debería aparecer la aplicación funcionando

* De no funcionar, se pueden cambiar las opciones de depuración en el menú *File*, *Run Options* o ejecutar con el interprete con la opción *Run with interpreter*

Código completo final del ejemplo:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">PythonCard</span> <span class="kn">import</span> <span class="n">model</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">PythonCard</span> <span class="kn">import</span> <span class="n">dialog</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">MyBackground</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">Background</span><span class="p">):</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_initialize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="c"># if you have any initialization</span>
      </span><span class="line">        <span class="c"># including sizer setup, do it here</span>
      </span><span class="line">        <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_btnEjecutar_mouseClick</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="n">comando</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="o">.</span><span class="n">txtComando</span><span class="o">.</span><span class="n">text</span>
      </span><span class="line">        <span class="n">resultado</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="nb">eval</span><span class="p">(</span><span class="n">comando</span><span class="p">))</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">components</span><span class="o">.</span><span class="n">txtResultados</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">resultado</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_menuFileAyuda_select</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="n">dialog</span><span class="o">.</span><span class="n">alertDialog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;Este programa de prueba ejecuta el comando ingresado por el usuario&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;Ayuda&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">app</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="n">MyBackground</span><span class="p">)</span>
      </span><span class="line">    <span class="n">app</span><span class="o">.</span><span class="n">MainLoop</span><span class="p">()</span>
      </span>

**Nota**: Por ser un ejemplo se obviaron temas de manejo de excepciones y cuestiones avanzadas. Se pueden descargar los archivos terminados:

* 

* 

Pantalla del ejemplo ejecutandose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`prueba.png </wiki/PythonCard/attachment/30/prueba.png>`_

.. ############################################################################

.. _www.python.org, Downloads, Windows Installer Python 2.5.2: http://www.python.org/ftp/python/2.5.2/python-2.5.2.msi

.. _wxPython.org, Binaries, win32 unicode: http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.7.1-py25.exe

.. _pythoncard.sourceforge.net, Downloads, PythonCard 0.8.2 win32: http://downloads.sourceforge.net/pythoncard/PythonCard-0.8.2.win32.exe

.. _sitio de PythonCard: http://pythoncard.sourceforge.net/samples/samples.html


