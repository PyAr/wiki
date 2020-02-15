.. contents::

-------------------------



Sobre PyAr (el grupo de Usuarios)
---------------------------------

¿Quiénes somos?
~~~~~~~~~~~~~~~

Un `grupo de entusiastas de Python`_, que decidió aunar esfuerzos para crear una comunidad local como marco de referencia para la aplicación, difusión y mejora de este lenguaje.

¿Qué hacemos?
~~~~~~~~~~~~~

Organizamos reuniones_ donde debatimos ideas, mantenemos una ListaDeCorreo_ a través de la cual nos comunicamos, creamos y mantenemos este portal, el cual pretendemos que tenga contenido útil tanto para los miembros de PyAr_ como para toda aquella persona que se interese por Python. Hoy estamos abocados a lograr que el grupo se consolide, se sumen miembros, y se establezcan las bases para comenzar a generar aportes mas concretos.

¿Cómo surgió PyAr?
~~~~~~~~~~~~~~~~~~

Merced a búsquedas en Internet, algunas personas se fueron registrando en el `grupo de Python de Buenos Aires de Meetup`_.

A mediados del 2004, el sitio era gratuito y "ranqueaba" alto en los resultados de los buscadores. El origen de aquel grupo es incierto, algunos creen que algún ocasional interesado lo creó, otros suponen que Meetup creaba estos grupos artificialmente como técnica de posicionamiento en buscadores (SEO_). Lo único cierto es que un cambio en su funcionamiento (la aparición del rol de "Manager") ayudó a fomentar la organización y posterior concreción de la `primera reunión`_ del grupo en Buenos Aires, en septiembre de 2004.

¿Qué pasó con el grupo de Meetup?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El grupo de Meetup no era (estrictamente hablando) nacional, sino de Buenos Aires. Por la estructura que tiene Meetup, los grupos se organizan en base a ciudades, no países. Por otro lado, durante 2005 Meetup volvió a cambiar su funcionamiento y empezó a cobrar por el mantenimiento del grupo. Fue por ese motivo que en aquel entonces se tomó la decisión de dejar de usarlo. PyAr_ había dejado de girar exclusivamente en torno a las reuniones (que es lo que enfatiza Meetup), y ya tenía nombre, sitio y `lista de correo`_ propios.

¿Cómo es la organización interna de PyAr?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hoy, mientras la cantidad de miembros del grupo lo permite, tenemos una organización plana, en la que todos debatimos nuestras ideas e inquietudes, y cada uno trata de aportar en lo que puede.

¿Cómo participar?
~~~~~~~~~~~~~~~~~

Suscribiéndote a la ListaDeCorreo_, registrándote en el portal, asistiendo a cualquiera de nuetros Eventos_, aportando ideas. También tenemos un canal de IRC. El servidor es ``irc.freenode.net``, y el nombre del canal es ``#pyar``. Podés ingresar vía Web `aquí`_ o `aquí </irc>`__. Si querés colaborar aportando contenido al Wiki, o ayudando en su mantenimiento, también es posible. Por favor, leé ContribuyendoAlWiki_.

¿Cómo se organiza una reunión?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los pasos a seguir para organizar una reunión están documentados en `Eventos/Reuniones/ReleaseProcedure`_.

Quiero aprender Python. ¿Dónde consigo material?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En AprendiendoPython_, vamos recopilando algunos links y material que los miembros de PyAr_ fuimos leyendo, y que consideramos que puede serte útil a la hora de empezar a aprender o profundizar tus conocimientos sobre este lenguaje.

En el Recetario_ que estamos armando entre todos, podés encontrar código para resolver algunos problemas comunes.

Y también los MiniEjemplos_ son una forma de mostrar las capacidades del lenguaje.

¿Qué puedo esperar de PyAr en el futuro?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Qué el grupo crezca, se consolide y organice formalmente. Que podamos brindar aportes útiles a la sociedad, tales como una *Bolsa de Empleos* relacionados con Python. Que podamos asesorar a empresas en la utilización de Python. Que comencemos a organizar eventos y seminarios en universidades, foros y empresas. Que promovamos sprints periódicos en los que podamos desarrollar o mejorar productos de software. Que nos contactemos con otros grupos de usuarios de Latinoamérica, y coordinemos esfuerzos con ellos. .. _SPRINT:



¿Qué es un ''sprint''?
~~~~~~~~~~~~~~~~~~~~~~

Según la `Portland Pattern Repository's Wiki`_:

  *Desde comienzos de 2002 se han realizado varios eventos denominados 'sprint' alrededor del Lenguaje Python / Zope. Un sprint, bajo esta terminología, es una reunión de programadores interesados en trabajar en un determinado proyecto Open Source, con una duración de 3 a 5 días. Los sprints generalmente tienen una audiencia multinacional.*

*Normalmente una conferencia es precedida por un sprint (tanto es así que ahora cualquier conferencia respetable de Python es precedida por un sprint), pero los sprints también se dan por si solos. Uno o mas 'coaches' guían el proceso. Se dice que los sprints están inspirados por un concepto de XP (eXtreme Programming -- Programación Extrema).*

Probablemente los sprints de PyAr_ no duren 3 a 5 días, al menos al principio... ni contamos con tener una audiencia multinacional. Pero pensamos divertirnos, aprender, y hacer algo útil.

¿Como contribuyo al Wiki?
~~~~~~~~~~~~~~~~~~~~~~~~~

En la sección ContribuyendoAlWiki_ vas a encontrar todo (**todo** se refiere a dos cositas nomás) lo que necesitás para poder empezar a contribuir al wiki.

¿Cómo colaboro con ésta lista de preguntas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hay `otras preguntas todavía sin respuesta`_, similares a éstas, que son sobre temas que tratamos varias veces en la lista de correo, pero aun a nadie las pasó acá. Si estás interesado y tenés usuario en el wiki, adelante. Sinó, fijate como en la pregunta anterior.

¿Por que Python y PyAr son como son?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Que pregunta. Algunas respuestas pueden inferirse del PythonZen_

Sobre Python (el Lenguaje)
--------------------------

¿Cuales son las ventajas/desventajas de usar listas o tuplas? Y diccionarios?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La velocidad de las tuplas vs las listas, se discutió acá hace unos meses: http://grulic.org.ar/lurker/message/20051219.201756.60530154.en.html

Las ventajas o desventajas de usar una u otra dependen del uso que le vaya a dar. Al ser inmutables, las tuplas pueden usarse como índices para diccionarios, las listas no. Las tuplas tienen que reconstruirse cada vez que necesitás "modificarlas", las listas no.

Con respecto a si hay realmente diferencia en cuanto a velocidad y tamaño en memoria, las listas y las tuplas deberían ser más rápidas de recorrer, mientras que los diccionarios fueron hechos para acceder rápidamente a ítems particulares.

Mas info en `FAQ General de Python`_

¿Qué son las ''Excepciones''?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las excepciones (Exception) son un mecanismo que posee el lenguaje para informarnos de un error o advertencia. En la página MensajesExcepcionales_ creamos una guía con las excepciones más comunes, su traducción y posibles soluciones.

¿Cuales son los cambios en Python 3.0 (Python 3000) la nueva versión del lenguaje?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En la página Python3Mil_ se encuentra la información sobre Python 3k, cambios en el lenguaje, compatibilidad hacia atras, calendario aproximado.

¿Qué son las celdas?
~~~~~~~~~~~~~~~~~~~~

Las celdas son como cajones donde se guarda una variable para que pueda ser manipulada dentro de generadores, funciones y clases internos (closures).

Técnicamente hablando, las funciones internas, clases, expresiones generadoras y demás pueden tener "variables libres" (ver ejemplos). Esas variables libres son las celdas, y se rellenan con un valor como cualquier variable - el chiste es que varios pedazos de código pueden apuntar a la misma celda (y por lo tanto modificar la misma variable).

Ejemplo:

::

   def f(x):
      def g():
         return x + 1
      return g()
      # aquí "x" se incrementó, x no es local a 'g'
      # x es una celda en toda la función f
      # para que pueda ser accedida desde g y f a la vez

Otro

::

   def f(l):
      escala = sum(l)
      return set( x / escala for x in l )
      # escala es una celda porque "x / escala for x in l"
      # es una expresión generadora, y su única forma de
      # acceder a "escala" es a través de la celda

Es importante saber cuáles de nuestras variables son celdas y cuáles simplemente locales, porque la sintaxis de python nos prohibe borrar celdas, no así variables locales:

::

   def f(x):
      rv = set( [ i*x for i in xrange(10) ] )
      del x # bizarro pero ok
      return rv
   def g(x):
      rv = set( i*x for i in xrange(10) )
      del x # error de sintaxis, no se pueden borrar celdas
      return rv

Nótese que en *f*, x no es una celda porque ocurre en una expresión de lista por comprensión - que se parece, pero no es un generador.

¿qué son los ''fastlocals''?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La documentación de python sólo menciona un *scope lógico local*, el "local".  Tiene sentido, puesto que las variables son o locales, o globales, o celdas (ver pregunta anterior).

Las variables locales todos las conocemos:

::

   def f():
      x = 4 # x es local

Los parámetros de una función también son variables locales. Por ende, self, en una función de una instancia, es también una variable local.

Las variables globales todos las conocemos también:

::

   llamadas = 0

   def f():
      global llamadas # llamadas es global
      llamadas += 1

Las variables globales son *"locales al módulo"*. Dentro de otro módulo, habrá otras globales.

Las "más globales de las globales" serían las variables globales del módulo *"*:underline:`builtin`*"*, puesto que cuando un nombre no se encuentra ni entre las locales ni entre las globales del módulo, se busca en el módulo :underline:`builtin`.

Luego tenemos las celdas, que son usadas en los "closures", o funciones o clases anidadas. Véase la pregunta anterior para estas.

Hasta ahí tenemos todos los scopes **"lógicos"** de python.

Pero hay otro scope más, que es más vale *físico* (es un detalle de implementación).

Las variables globales se guardan en un diccionario, las "locales" a secas también, así que accederlas es lento.

Sucede que es muy sencillo para el compilador, en la mayoría de los casos, descubrir todas las variables locales que va a necesitar una función. Entonces, en esos casos, se preasigna un lugar a la variable en un array interno de CPython - el acceso a esas variables "locales rápidas" es... bueno, muy rápido pues.

Esas son **"fastlocals"**.

Casi todas las variables locales que se declaren van a ser rápidas. La única forma que conozco de generar variables locales lentas es con *import ** (en el scope local de una función, lo que es muy poco común), o especificando un diccionario de locales con *eval()*

La forma de "declarar" una variable de este tipo es simplemente asignandole un valor:

::

   def f(...):
      ...
      x = 5
      ...

Esto ya define a "x" como variable local rápida. Y ojo, **tiene ese status en todo el bloque.**

O sea que cosas como esta no van a funcionar:

::

   def f():
      if x != 3:
        ...
      ...
      x = 5

¿Por qué no? Porque x es local incluso cuando se accede en 'x != 3', y a esa altura, nunca fue asignada. Muchos pensarían que python va a ir a buscar una variable global llamda 'x' - nop... no es así. La simple asignación a x la define implícitamente como variable local y no global. Si queremos que sea global (y que la asignación cambie el valor de la variable global), hay que hacer:

::

   def f():
      global x
      if x != 3:
        ...
      ...
      x = 5

Sobre Python (el interprete)
----------------------------

¿Cuales son los interpretes que puedo usar?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las opciones disponibles son:

* La consola interactiva por defecto de python (viene con la instalacion, solo hay que escribir python)

* IDLE_

* ipython_

* `PyCrust/PyShell`_ (incluido en wxPython_)

¿Como puedo configurar mi interprete para que sea mas amigable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si estas usando el interprete interactivo por defecto de python, se recomienda leer los siguientes articulos:

* AutocomplecionEnConsolaInteractiva_: Explica como agregar autocomplecion de metodos y atributos con tab en la consola interactiva

* GuardarHistorialEnConsolaInteractiva_: Explica como guardar el historial de comandos entre sesiones en la consola interactiva.

* `recursos externos`_

Construyendo Aplicaciones
-------------------------

Usando Bases de Datos
~~~~~~~~~~~~~~~~~~~~~

Como conectarse a bases de datos y ejecutar consultas
:::::::::::::::::::::::::::::::::::::::::::::::::::::

La página DbApi_ contiene la información relativa al Acceso a Bases de Datos desde Python (Interface DB-API), sobre como conectarse (mysql, postgresql, etc.), ejecutar consultas, armar queries, escapear comillas, etc.

ORMs: Interfaces Objeto-Relacional
::::::::::::::::::::::::::::::::::

Acceder a bases de datos a traves de Db-Api es relativamente de bajo nivel. Se pueden utilizar Object-Relational-Mappers de mas alto nivel (similar a Hibernate en el mundo java). Los ORMS mas importantes para python son:

* SqlAlchemy_: Un mapeador que dice ser simple, eficiente y extensible

* SqlObject_

* Storm_: El nuevo mapeador de Canonical (Ubuntu)

Por el momento no hay ningún concenso en la lista sobre cual es mejor o peor.

También existen librerías para acceso de datos (similar al patron ActiveRecord_ o librerias DAO/ADO de otras plataformas) que permiten escribir consultas e interactuar con los datos más facilmente (incluso sin usar SQL), sin necesidad de definir un modelo de clases:

* DAL_: Capa de Abstracción de Base de Datos (Web2Py_)

PlPython: Python dentro de PostgreSQL
:::::::::::::::::::::::::::::::::::::

La página PlPython_ contiene un "tutorial" sobre como usar funciones Python dentro de la base de datos relacional PostgreSQL (tanto procedimientos almacenados como triggers/disparadores).

Programación de interfaces gráficas (toolkits)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La página InterfacesGraficas_ describe las diversas opciones disponibles en Python: wx, gtk, qt, etc., sus comparaciones, ventajas y desventajas y código de ejemplo.

En el Recetario_ hay ejemplos de como empezar a construir interfaces en python.

Programación WEB
~~~~~~~~~~~~~~~~

Interfaz WSGI
:::::::::::::

La página WSGI_ contiene información sobre la espeficiación para servidores web de python, comparación entre mod_python vs mod_wsgi vs servidores embebidos, performance, como usarlos y configurarlos, ejemplos.

Frameworks Webs
:::::::::::::::

Para construir aplicaciones web complejas en python se pueden usar alguno de los principales frameworks web:

* Django_: framework de alto nivel para desarrollo rapido y diseño claro y pragmático

* Turbogears_: el megaframework que combina CherryPy_, Kid, SQLObject y MochiKit_.

* Zope_: el "abuelo" de los frameworks web de python

* Pylons_: framework liviano que enfatiza flexibilidad y desarrollo rápido

* WebPy_: framework simple "todo-en-uno" sin dependencias

* web2py_: framework para desarrollos rápidos. De fácil aprendizaje y uso simple. Un ejecutable que contiene todo.

Herramientas webs
:::::::::::::::::

* Plone_: Completo sistema de manejo de contenidos (CMS)

* MoinMoin_: La Wiki hecha en Python (que es el que usamos actualmente en este nuestro sitio)

* Trac_: El sistema de gestión de proyectos hecho en python

IDEs
~~~~

* IDEs_: Comparación de entornos de desarrollo

* TablaComparativa_: Tabla comparativa de features de los IDEs

Python en la vida real
----------------------

Performance/Estabilidad de Python, ¿se la banca?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En ocasiones se pregunta a la lista si Python esta a la altura de las circunstancias, como se compara la velocidad/uso de memoria con VB, C, .NET, Java, etc. En la página RendimientoPythonVsJavaVsNet_ hay un resumen de los comentarios vertidos a la lista.

¿Que aplicaciones (conocidas) estan hechas en Python?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las siguientes aplicaciones se pueden ver/probar/evaluar para conocer el lenguaje y ver su capacidad/rendimiento:

* BitTorrent_ (original): programa para compartir archivos p2p (interfaz wx)

* ClamWin_: el antivirus libre, frontend de clamav (interfaz wx)

* OpenErp_ (ex TinyErp_): completo sistema de gestión empresarial en tres capas (interfaz gtk)

* Meld_: visor de diferencias (interfaz gtk)

* Trac_: sistema de gestión de proyectos (interfaz web)

En el ambito local:

* `Sistema Fierro`_: sistema de gestión para librerias y editoriales (interfaz wx)

* PyRece_: aplicativo libre para factura electrónica (interfaz wx mediante PythonCard_)

Nota: la lista no pretende ser completa, solo se presentan algunas de las aplicaciones más conocidas, relevantes y/o utilizadas por gran numero de personas.

¿Podrías nombrar sitios Web (conocidos) que estén hechos en Python?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si:

* YouTube (http://youtube.com) está `programado en Python`_. Es actualmente el segundo sitio de búsqueda en Internet luego de google.com.

* Reddit (http://reddit.com) está `programado en Python <http://brainsik.theory.org/.:./2009/why-reddit-uses-python>`__.

* FriendFeed (http://friendfeed.com) (adquidiro por Facebook en Agosto 2009) está `programado en Python <http://blog.friendfeed.com/2008/02/friendfeed-changelog-see-what-code-we.html>`__.

* La NASA `usa Python`_ en el *frontend* de su platforma de *cloud computing* NEBULA_.

Algunos sitios no tan conocidos pero que están hechos con Python y vale la pena ver:

* Kiosko.net (http://Kiosko.net) está hecho en Django.

* GooglePersonFinder_ (http://haiticrisis.appspot.com) se utilizó para el terremoto de Haití de 2010.

* PyConAr_ 2012 (http://ar.pycon.org/2012), un ejemplo de aplicación hecha en Web2py.

¿En que difieren Python y VisualBasic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La página VisualBasic_ detalla las similitudes y diferencias entre ambos lenguajes.

Preguntas surtidas
------------------

¿Hay alguna forma de saber la ruta (path) del archivo actual?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MarianoGuerra_ preguntó esto en este hilo: http://mx.grulic.org.ar/lurker/thread/20080719.055432.4df0ac40.es.html Esencialmente, el problema es saber la ruta absoluta del script python que se está ejecutando

La respuesta que le dio MartinBothiry_ es hacer:

::

   os.path.abspath(os.path.dirname(__file__))


¿Uso el modulo array o listas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SebastianBassi_ pregunto en este hilo: http://mx.grulic.org.ar/lurker/thread/20090803.144308.0aabeb1b.en.html

sobre en que casos convenia usar el modulo de la libreria estandar array por sobre una lista comun.

La respuesta de GabrielGenellina_ fue:

El array de la libreria estandar es un "chorizo" de elementos, todos del mismo tipo, pero tipos nativos (no objetos; por ejemplo "unsigned long integer"). Es unidimensional, y no tiene casi métodos. El array de Numpy también guarda tipos nativos, pero es multidimensional, y tiene un montón de métodos y operaciones definidos.

Extraer un elemento de un array es costoso, porque hay que crear el objeto Python que lo "envuelva", y lo mismo pasa al asignarle un valor a un elemento individual. Así que operar con arrays elemento-a-elemento en Python es mas lento que usar una lista estándar. Los arrays están pensados para usarlos desde código en C (o Numpy, que esta escrito en C); por ejemplo, un array.array("f") se puede pasar a una función en C declarada como "float x[]" o "float \*x".

Otra diferencia: array solo puede contener caracteres, números enteros nativos, o números de punto flotante; no objetos. Pero la representación en memoria es mucho mas compacta, cada elemento ocupa sólo lo necesario para guardar su valor y nada más (por ejemplo, 4 bytes para un float vs. 20 que se necesitan en una lista normal [16 para el objeto float de Python y 4 para el puntero en la lista], los tamaños son para Windows 32 bits).

Yo diria que conviene usar un array si:

* todos los elementos son homogeneos, de alguno de los tipos soportados.

y:

* vas a procesarlo en C porque te importa la velocidad

* o bien, estas corto de memoria y una lista normal no te entra (pero no te importa la velocidad)

A veces el "is" me dice una cosa y otras otra, ¿funciona mal?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"is" no falla, compara si dos objetos son el mismo (no si son iguales).

En algunos casos, ofrece resultado que a primera vista sorprenden...

::

   >>> a = 3
   >>> b = 3
   >>> a is b
   True

En este caso a apunta a un 3 en memoria, y b apunta al mismo 3 en memoria. Python no creó dos objetos "3", sino que usó el mismo para los nombres a y b.

::

   >>> a = 500
   >>> b = 500
   >>> a is b
   False

Aquí a apunta a un 500 en memoria, y b apunta a otro 500 en memoria. Python sí creó dos objetos "500".

La pregunta es... ¿por qué la diferencia de comportamiento? Python (ojo, ver abajo) precachea (o tiene internalizado) algunos enteros chicos, porque sabe que siempre se van a usar.

Lo mismo sucede con algunos strings muy cortitos.

Pero ojo, que esto sucede con versiones pasadas y actuales de CPython. Es un detalle de implementación, puede cambiar a futuro, y puede no darse en otras implementaciones de Python como Jython o IronPython_.

.. ############################################################################


.. _reuniones:

.. _ListaDeCorreo:

.. _grupo de Python de Buenos Aires de Meetup: http://python.meetup.com/cities/ar/buenos_aires/

.. _SEO: http://es.wikipedia.org/wiki/Posicionamiento_en_buscadores

.. _aquí: /irc

.. _Portland Pattern Repository's Wiki: http://c2.com/cgi/wiki?PythonSprint

.. _FAQ General de Python: http://www.python.org/doc/faq/es/general/#por-qu-hay-tipos-de-datos-tuplas-y-listas-separados

.. _IDLE: http://en.wikipedia.org/wiki/IDLE_(Python)

.. _ipython: http://ipython.scipy.org/moin/About

.. _PyCrust/PyShell: http://www.wxpython.org/py.php

.. _wxPython: http://www.wxpython.org/

.. _recursos externos: http://www.eseth.org/2008/pimp-pythonrc.html

.. _SqlAlchemy: http://www.sqlalchemy.org/

.. _SqlObject: http://sqlobject.org/

.. _Storm: http://storm.canonical.com/

.. _ActiveRecord: http://es.wikipedia.org/wiki/Patr%C3%B3n_ActiveRecord

.. _DAL: http://www.web2py.com.ar/examples/default/dal

.. _Django: http://www.djangoproject.com

.. _Turbogears: http://turbogears.org/

.. _Zope: http://www.zope.org

.. _Pylons: http://pylonshq.com

.. _WebPy: http://webpy.org

.. _web2py: http://www.web2py.com.ar/

.. _Plone: http://plone.org/

.. _MoinMoin: http://moinmo.in/

.. _Trac: http://trac.edgewall.org

.. _IDEs: http://python.org.ar/pyar/IDEs

.. _TablaComparativa: http://python.org.ar/pyar/TablaIDEs


.. _BitTorrent: http://www.bittorrent.com

.. _ClamWin: http://es.clamwin.com

.. _Odoo: http://www.odoo.com (ex **OpenErp**)


.. _Meld: http://meld.sourceforge.net

.. _Sistema Fierro: http://www.fierro-soft.com.ar

.. _PyRece: http://www.pyafipws.com.ar/pyrece


.. _programado en Python: http://vimeo.com/6461983

.. _usa Python: http://nebula.nasa.gov/services/

.. _NEBULA: http://nebula.nasa.gov/











.. role:: underline
   :class: underline

.. _pyar: /pyar
.. _eventos: /eventos
.. _contribuyendoalwiki: /contribuyendoalwiki
.. _aprendiendopython: /aprendiendopython
.. _recetario: /recetario
.. _miniejemplos: /miniejemplos
.. _pythonzen: /pythonzen
.. _mensajesexcepcionales: /mensajesexcepcionales
.. _python3mil: /python3mil
.. _autocomplecionenconsolainteractiva: /Recetario/autocomplecionenconsolainteractiva
.. _guardarhistorialenconsolainteractiva: /guardarhistorialenconsolainteractiva
.. _dbapi: /dbapi
.. _plpython: /plpython
.. _interfacesgraficas: /interfacesgraficas
.. _wsgi: /wsgi
.. _cherrypy: /cherrypy
.. _rendimientopythonvsjavavsnet: /rendimientopythonvsjavavsnet
.. _pythoncard: /pythoncard
.. _visualbasic: /visualbasic
.. _marianoguerra: /marianoguerra
.. _sebastianbassi: /sebastianbassi
.. _gabrielgenellina: /gabrielgenellina
