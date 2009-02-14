#language es
#pragma section-numbers 2
= Preguntas Frecuentes =
[[TableOfContents]]
----
== Sobre PyAr (el grupo de Usuarios) ==
=== ¿Quiénes somos? ===
Un grupo de entusiastas de Python, que decidió aunar esfuerzos para crear una comunidad local como marco de referencia para la aplicación, difusión y mejora de este lenguaje.

=== ¿Qué hacemos? ===
Organizamos reuniones donde debatimos ideas, mantenemos una ListaDeCorreo a través de la cual nos comunicamos, creamos y mantenemos este portal, el cual pretendemos que tenga contenido útil tanto para los miembros de PyAr como para toda aquella persona que se interese por Python. Hoy estamos abocados a lograr que el grupo se consolide, se sumen miembros, y se establezcan las bases para comenzar a generar aportes mas concretos.

=== ¿Cómo surgió PyAr? ===
Merced a búsquedas en Internet, algunas personas se fueron registrando en el [http://python.meetup.com/cities/ar/buenos_aires/ grupo de Python de Buenos Aires de Meetup].

A mediados del 2004, el sitio era gratuito y "ranqueaba" alto en los resultados de los buscadores. El origen de aquel grupo es incierto, algunos creen que algún ocasional interesado lo creó, otros suponen que Meetup creaba estos grupos artificialmente como técnica de posicionamiento en buscadores ([http://es.wikipedia.org/wiki/Posicionamiento_en_buscadores SEO]). Lo único cierto es que un cambio en su funcionamiento (la aparición del rol de "Manager") ayudó a fomentar la organización y posterior concreción de la [:Eventos/Reuniones/Reunion01:primera reunión] del grupo en Buenos Aires, en septiembre de 2004.

=== ¿Qué pasó con el grupo de Meetup? ===
El grupo de Meetup no era (estrictamente hablando) nacional, sino de Buenos Aires. Por la estructura que tiene Meetup, los grupos se organizan en base a ciudades, no países. Por otro lado, durante 2005 Meetup volvió a cambiar su funcionamiento y empezó a cobrar por el mantenimiento del grupo. Fue por ese motivo que en aquel entonces se tomó la decisión de dejar de usarlo. PyAr había dejado de girar exclusivamente en torno a las reuniones (que es lo que enfatiza Meetup), y ya tenía nombre, sitio y [:ListaDeCorreo:lista de correo] propios.

=== ¿Cómo es la organización interna de PyAr? ===
Hoy, mientras la cantidad de miembros del grupo lo permite, tenemos una organización plana, en la que todos debatimos nuestras ideas e inquietudes, y cada uno trata de aportar en lo que puede.

=== ¿Cómo participar? ===
Suscribiéndote a la ListaDeCorreo, registrándote en el portal, asistiendo a cualquiera de nuetros ["Eventos"], aportando ideas. También tenemos un canal de IRC. El servidor es `irc.freenode.net`, y el nombre del canal es `#pyar`. Si querés colaborar aportando contenido al Wiki, o ayudando en su mantenimiento, también es posible. Por favor, leé ["ContribuyendoAlWiki"].

=== ¿Cómo se organiza una reunión? ===
Los pasos a seguir para organizar una reunión están documentados en ["Eventos/Reuniones/ReleaseProcedure"].

=== Quiero aprender Python. ¿Dónde consigo material? ===
En AprendiendoPython, vamos recopilando algunos links y material que los miembros de PyAr fuimos leyendo, y que consideramos que puede serte útil a la hora de empezar a aprender o profundizar tus conocimientos sobre este lenguaje.

=== ¿Qué puedo esperar de PyAr en el futuro? ===
Qué el grupo crezca, se consolide y organice formalmente. Que podamos brindar aportes útiles a la sociedad, tales como una ''Bolsa de Empleos'' relacionados con Python. Que podamos asesorar a empresas en la utilización de Python. Que comencemos a organizar eventos y seminarios en universidades, foros y empresas. Que promovamos sprints periódicos en los que podamos desarrollar o mejorar productos de software. Que nos contactemos con otros grupos de usuarios de Latinoamérica, y coordinemos esfuerzos con ellos. [[Anchor(SPRINT)]]

=== ¿Qué es un ''sprint''? ===
Según la [http://c2.com/cgi/wiki?PythonSprint Portland Pattern Repository's Wiki]:

 ''Desde comienzos de 2002 se han realizado varios eventos denominados 'sprint' alrededor del Lenguaje Python / Zope. Un sprint, bajo esta terminología, es una reunión de programadores interesados en trabajar en un determinado proyecto Open Source, con una duración de 3 a 5 días. Los sprints generalmente tienen una audiencia multinacional.''
''Normalmente una conferencia es precedida por un sprint (tanto es así que ahora cualquier conferencia respetable de Python es precedida por un sprint), pero los sprints también se dan por si solos. Uno o mas 'coaches' guían el proceso. Se dice que los sprints están inspirados por un concepto de XP (eXtreme Programming -- Programación Extrema).''

Probablemente los sprints de PyAr no duren 3 a 5 días, al menos al principio... ni contamos con tener una audiencia multinacional. Pero pensamos divertirnos, aprender, y hacer algo útil.

=== ¿Qué es el ''Hip Bar''? ===
El Hip Bar es el pub donde organizamos la mayoría de los encuentros en Capital Federal. Durante mucho tiempo, estuvimos creídos que el lugar se llamaba ''Hip Hop''... si encontrás en el portal o en la lista referencias a ese lugar, tené en cuenta que se trata del mismo pub. Para mayor información (dirección, fotos), tenemos una página dedicada al HipBar.

=== ¿Como contribuyo al Wiki? ===
En la sección ContribuyendoAlWiki vas a encontrar todo ('''todo''' se refiere a dos cositas nomás) lo que necesitás para poder empezar a contribuir al wiki.

=== ¿Cómo colaboro con ésta lista de preguntas? ===

Hay [:PreguntasSinRespuesta:otras preguntas todavía sin respuesta], similares a éstas, que son sobre temas que tratamos varias veces en la lista de correo, pero aun a nadie las pasó acá. Si estás interesado y tenés usuario en el wiki, adelante. Sinó, fijate como en la pregunta anterior.

== Sobre Python (el Lenguaje) ==
=== ¿Cuales son las ventajas/desventajas de usar listas o tuplas? Y diccionarios? ===
La velocidad de las tuplas vs las listas, se discutió acá hace unos meses: http://grulic.org.ar/lurker/message/20051219.201756.60530154.en.html

Las ventajas o desventajas de usar una u otra dependen del uso que le vaya a dar. Al ser inmutables, las tuplas pueden usarse como índices para diccionarios, las listas no. Las tuplas tienen que recostruirse cada vez que necesitás "modificarlas", las listas no.

Con respecto a si hay realmente diferencia en cuanto a velocidad y tamaño en memoria, las listas y las tuplas deberían ser más rápidas de recorrer, mientras que los diccionarios fueron hechos para acceder rápidamente a ítems particulares.

Mas info en [http://www.python.org/doc/faq/es/general/#por-qu-hay-tipos-de-datos-tuplas-y-listas-separados FAQ General de Python]

=== ¿Cuales son los cambios en Python 3.0 (Python 3000) la nueva versión del lenguaje? ===

En la página Python3Mil se encuentra la información sobre Python 3k, cambios en el lenguaje, compatibilidad hacia atras, calendario aproximado. 

== Sobre Python (el interprete) ==
=== ¿Cuales son los interpretes que puedo usar? ===

Las opciones disponibles son:
 * La consola interactiva por defecto de python (viene con la instalacion, solo hay que escribir python)
 * [http://en.wikipedia.org/wiki/IDLE_(Python) IDLE]
 * [http://ipython.scipy.org/moin/About ipython]
 * [http://www.wxpython.org/py.php PyCrust/PyShell] (incluido en [http://www.wxpython.org/ wxPython])

=== ¿Como puedo configurar mi interprete para que sea mas amigable? ===

Si estas usando el interprete interactivo por defecto de python, se recomienda leer los siguientes articulos:
 * AutocomplecionEnConsolaInteractiva: Explica como agregar autocomplecion de metodos y atributos con tab en la consola interactiva
 * GuardarHistorialEnConsolaInteractiva: Explica como guardar el historial de comandos entre sesiones en la consola interactiva.
 * [http://www.eseth.org/2008/pimp-pythonrc.html recursos externos]

== Construyendo Aplicaciones ==

=== Usando Bases de Datos ===

==== Como conectarse a bases de datos y ejecutar consultas ====

La página DbApi contiene la información relativa al Acceso a Bases de Datos desde Python (Interface DB-API), sobre como conectarse (mysql, postgresql, etc.), ejecutar consultas, armar queries, escapear comillas, etc.

==== ORMs: Interfaces Objeto-Relacional ====

Acceder a bases de datos a traves de Db-Api es relativamente de bajo nivel. Se pueden utilizar Object-Relational-Mappers de mas alto nivel (similar a Hibernate en el mundo java).
Los ORMS mas importantes para python son:
 * [http://www.sqlalchemy.org/ SqlAlchemy]: Un mapeador que dice ser simple, eficiente y extensible
 * [http://sqlobject.org/ SqlObject]
 * [http://storm.canonical.com/ Storm]: El nuevo mapeador de Canonical (Ubuntu)

Por el momento no hay ningún concenso en la lista sobre cual es mejor o peor.

=== Programación de interfaces gráficas (toolkits) ===

La página InterfacesGraficas describe las diversas opciones disponibles en Python: wx, gtk, qt, etc., sus comparaciones, ventajas y desventajas y código de ejemplo. 

En el [Recetario] hay ejemplos de como empezar a construir interfaces en python.

=== Programación WEB ===

==== Interfaz WSGI ====
La página ["WSGI"] contiene información sobre la espeficiación para servidores web de python, comparación entre mod_python vs mod_wsgi vs servidores embebidos, performance, como usarlos y configurarlos, ejemplos.

==== Frameworks Webs ====

Para construir aplicaciones web complejas en python se pueden usar alguno de los principales frameworks web:
 * [http://www.djangoproject.com Django]: framework de alto nivel para desarrollo rapido y diseño claro y pragmático
 * [http://turbogears.org/ Turbogears]: el megaframework que combina CherryPy, Kid, SQLObject y MochiKit.
 * [http://www.zope.org Zope]: el "abuelo" de los frameworks web de python
 * [http://pylonshq.com Pylons]: framework liviano que enfatiza flexibilidad y desarrollo rápido
 * [http://webpy.org WebPy]: framework simple "todo-en-uno" sin dependencias
 * [http://mdp.cti.depaul.edu/ web2py]: framework para desarrollos rápidos. De uso simple. Un ejecutable que contiene todo.

==== Herramientas webs ====
 * [http://plone.org/ Plone]: Completo sistema de manejo de contenidos (CMS)
 * [http://moinmo.in/ MoinMoin]: La Wiki hecha en python
 * [http://trac.edgewall.org Trac]: El sistema de gestión de proyectos hecho en python

== Python en la vida real ==

=== Performance/Estabilidad de Python, ¿se la banca? ===

En ocasiones se pregunta a la lista si Python esta a la altura de las circunstancias, como se compara la velocidad/uso de memoria con VB, C, .NET, Java, etc. En la página RendimientoPythonVsJavaVsNet hay un resumen de los comentarios vertidos a la lista.

=== ¿Que aplicaciones (conocidas) estan hechas en python? ===

Las siguientes aplicaciones se pueden ver/probar/evaluar para conocer el lenguaje y ver su capacidad/rendimiento: 
 * [http://www.bittorrent.com BitTorrent] (original): programa para compartir archivos p2p (interfaz wx)
 * [http://es.clamwin.com ClamWin]: el antivirus libre, frontend de clamav (interfaz wx)
 * [http://www.openerp.com OpenErp] (ex TinyErp): completo sistema de gestión empresarial en tres capas (interfaz gtk)
 * [http://meld.sourceforge.net Meld]: visor de diferencias (interfaz gtk)
 * [http://trac.edgewall.org Trac]: sistema de gestión de proyectos (interfaz web)

En el ambito local:
 * [http://www.fierro-soft.com.ar Sistema Fierro]: sistema de gestión para librerias y editoriales (interfaz wx)

Nota: la lista no pretende ser completa, solo se presentan algunas de las aplicaciones más conocidas, relevantes y/o utilizadas por gran numero de personas.

== Preguntas surtidas ==

=== ¿Hay alguna forma de saber la ruta (path) del archivo actual? ===

MarianoGuerra preguntó esto en este hilo: http://mx.grulic.org.ar/lurker/thread/20080719.055432.4df0ac40.es.html
Esencialmente, el problema es saber la ruta absoluta del script python que se está ejecutando

La respuesta que le dio MartinBothiry es hacer:

{{{
  os.path.abspath(os.path.dirname(__file__)) 
}}}
