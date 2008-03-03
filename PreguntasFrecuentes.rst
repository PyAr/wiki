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


== Usando Bases de Datos ==
=== ¿Cómo me conecto a una base de datos con MySQL? ===
Este es un ejemplo basico de como hacerlo con MySQL:
{{{
>>> import MySQLdb
>>> db = MySQLdb.connect(host="localhost", user="root",
... passwd="mypassword", db="PythonU")
}}}
Una vez establecida la conexion, hay que crear un "cursor". Un cursor
es una estructura de control que se usa para recorrer (y eventualmente
procesar) los records de un result set.

El metodo para crear el cursor se llama, originalmente, cursor():
{{{
>>> cursor = db.cursor()
}}}
Ya tenemos la conexion establecida y el cursor creado, es hora de
ejecutar algunos comandos SQL:
{{{
>>> cursor.execute("SELECT * FROM Students")
5L
}}}
El metodo execute se usa para ejecutar comandos SQL. Note que no hace
falta agregar el ';' (punto y coma) al final del comando. Ahora es
cuestion de recorrer el objeto cursor.

Para obtener un solo elemento, usamos fetchone():
{{{
>>> cursor.fetchone()
(1L, 'Joe', 'Campbell', datetime.date(2006, 2, 10), 'N')

>>> cursor.fetchall()
((1L, 'Joe', 'Campbell', datetime.date(2006, 2, 10), 'N'),
(2L, 'Joe', 'Doe', datetime.date(2004, 2, 16), 'N'),
(3L, 'Rick', 'Hunter', datetime.date(2005, 3, 20), 'N'),
(4L, 'Laura', 'Ingalls', datetime.date(2001, 3, 15), 'Y'),
(5L, 'Virginia', 'Gonzalez', datetime.date(2003, 4, 2), 'N'))
}}}
Cual metodo usar dependera de la cantidad de datos que tengamos, la
memoria disponible en la PC y sobre todo, de como querramos hacerlo.
Si estamos trabajando con datasets limitados, no habra problema con el
uso de fetchall(), pero si la base de datos es lo suficientemente
grande como para entrar en memoria, se podria implementar una
estrategia como la que se encuentra aca:
{{{
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root",passwd="secret", db="PythonU")
cursor = db.cursor()
recs=cursor.execute("SELECT * FROM Students")
for x in range(recs):
   print cursor.fetchone()
}}}
O directamente:
{{{
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root",passwd="secret", db="PythonU")
cursor = db.cursor()
cursor.execute("SELECT * FROM Students")
for row in cursor:
   print row
}}}
(Sebastian Bassi)

=== ¿Cómo me conecto a una base de datos con PostgreSQL? ===

Otro ejemplo basico de como hacerlo con PostgreSQL (similar al de MySQL). 
Se usó el esquema: {{{CREATE TABLE estudiante ( nombre varchar,  apellido varchar,  fecha date,  booleano bool,  legajo serial PRIMARY KEY);}}}
Antes que nada se debe instalar el conector ([http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo para unix y windows]).


Primero importar el conector y crear la conexión a la base de datos:
{{{
>>> import psycopg2, psycopg2.extras
>>> conn = psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')
}}}


Luego crear un cursor para obtener los datos y ejecutar consulta:
{{{
>>> cur = conn.cursor()
>>> cur.execute("SELECT * FROM estudiante")
>>> rows=cur.fetchall()
>>> print rows

[['Joe', 'Capbell', datetime.date(2006, 2, 10), False, 1], ['Joe', 'Doe', datetime.date(2004, 2, 16), False, 2], ['Rick', 'Hunter', datetime.date(2005, 3, 20), False, 3], ['Laura', 'Ingalls', datetime.date(2001, 3, 15), True, 4], ['Virginia', 'Gonzalez', datetime.date(2003, 4, 2), False, 5]]
}}}


Algo más pitónico es crear el cursor simil diccionario (en vez de una lista de valores):
{{{
>>> cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)   
>>> cur.execute("SELECT * FROM estudiante")
>>> for row in cur: # itero sober cada fila
>>>    # row es un diccionario, con las claves = nombres de campos
>>>    print "Nombre y Apellido: %s, %s " % (row['nombre'],row['apellido'])
    
Nombre y Apellido: Joe, Capbell 
Nombre y Apellido: Joe, Doe 
Nombre y Apellido: Rick, Hunter 
Nombre y Apellido: Laura, Ingalls 
Nombre y Apellido: Virginia, Gonzalez 
}}}


'''Nota:''' esto es propio del conector psycopg2. Igualmente otros conectores tambien lo soportan o se puede imitar (leyendo el atributo description del cursor que tiene la información de los campos):
{{{
>>> print cur.description
(('nombre', 1043, 8, -1, None, None, None), ('apellido', 1043, 8, -1, None, None, None), ('fecha', 1082, 10, 4, None, None, None), ('booleano', 16, 1, 1, None, None, None), ('legajo', 23, 1, 4, None, None, None))
}}}
