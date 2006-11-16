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

En aquel entonces, el sitio era gratuito y ranqueaba alto en los resultados de los buscadores. El origen de este grupo es incierto, algunos creen que algún ocasional interesado la creó, otros suponen que Meetup creaba estos grupos artificialmente como  técnica de posicionamiento en buscadores ([http://es.wikipedia.org/wiki/Posicionamiento_en_buscadores SEO]). Lo cierto es que al poco tiempo de que [:PabloZiliani:Pablo Ziliani] se registrara, un cambio en el funcionamiento de Meetup terminó ofreciéndole a él el rol de "administrador del grupo", cargo que aceptó y que al poco tiempo derivó en la organización de la [:Eventos/Reuniones/Reunion01:primera reunión] del grupo en Buenos Aires, en septiembre de 2004.

=== ¿Qué pasó con el grupo de Meetup? ===
El grupo de Meetup no era (estrictamente hablando) nacional, sino de Buenos Aires. Por la estructura que tiene Meetup, los grupos se organizan en base a ciudades, no países. Por otro lado, durante 2005 Meetup volvió a cambiar su organización, y empezó a cobrar por el mantenimiento del grupo. Fue por eso que en aquel entonces se tomó la decisión de dejar de usarlo. PyAr había dejado de girar exclusivamente en torno a las reuniones (que es lo que enfatiza Meetup), y ya tenía nombre, sitio y [:ListaDeCorreo:lista de correo] propios.

=== ¿Cómo es la organización interna de PyAr? ===
Hoy, mientras la cantidad de miembros del grupo lo permite, tenemos una organización plana, en la que todos debatimos nuestras ideas e inquietudes, y cada uno trata de aportar en lo que puede.

=== ¿Cómo participar? ===
Suscribiéndote a la ListaDeCorreo, registrándote en el portal, asistiendo a cualquiera de nuetros ["Eventos"], aportando ideas. También tenemos un canal de IRC. El servidor es `irc.freenode.net`, y el nombre del canal es `#python-ar`. Si querés colaborar aportando contenido al Wiki, o ayudando en su mantenimiento, también es posible. Por favor, leé ["ContribuyendoAlWiki"].

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

== Sobre Python (el Lenguaje) ==
=== Cuales son las ventajas/desventajas de usar listas o tuplas? Y diccionarios? ===
La velocidad de las tuplas vs las listas, se discutió acá hace unos meses: http://grulic.org.ar/lurker/message/20051219.201756.60530154.en.html

Las ventajas o desventajas de usar una u otra dependen del uso que le vaya a dar. Al ser inmutables, las tuplas pueden usarse como índices para diccionarios, las listas no. Las tuplas tienen que recostruirse cada vez que necesitás "modificarlas", las listas no.

Con respecto a si hay realmente diferencia en cuanto a velocidad y tamaño en memoria, las listas y las tuplas deberían ser más rápidas de recorrer, mientras que los diccionarios fueron hechos para acceder rápidamente a ítems particulares.

Mas info en [http://www.python.org/doc/faq/es/general/#por-qu-hay-tipos-de-datos-tuplas-y-listas-separados FAQ General de Python]
