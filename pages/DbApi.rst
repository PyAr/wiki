
Acceso a Bases de Datos desde Python: Interfaz DB-API
-----------------------------------------------------

.. contents::

En python, el acceso a bases de datos esta estandarizado por la especificación Database API (DB-API), actualmente en la versión 2.0 (`PEP 249: Python Database API Specification v2.0`_)

Gracias a esto, se puede acceder a cualquier base de datos utlizando la misma interfaz (ya sea un motor remoto, local, ODBC, etc.). Se puede comparar con DAO, ADO, ADO.NET en el mundo Microsoft, o a JDBC en el mundo Java.

O sea, el mismo codigo se podría llegar a usar para cualquier base de datos, tomando siempre los recaudos necesarios (lenguaje SQL estándard, estilo de parametros soportado, etc.)

Por ello, el manejo de bases de datos en python siempre sigue estos pasos:

1. Importar el conector 

#. Conectarse a la base de datos (función connect del módulo conector)

#. Abrir un Cursor (método cursor de la conexión)

#. Ejecutar una consulta (método execute del cursor)

#. Obtener los datos (método fetch o iterar sobre el cursor)

#. Cerrar el cursor (método close del cursor)

-------------------------



¿Cómo me conecto a una base de datos con MySQL?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este es un ejemplo basico de como hacerlo con MySQL:

::

   >>> import MySQLdb
   >>> db = MySQLdb.connect(host="localhost", user="root",
   ... passwd="mypassword", db="PythonU")

Una vez establecida la conexion, hay que crear un "cursor". Un cursor es una estructura de control que se usa para recorrer (y eventualmente procesar) los records de un result set.

El metodo para crear el cursor se llama, originalmente, cursor():

::

   >>> cursor = db.cursor()

Ya tenemos la conexion establecida y el cursor creado, es hora de ejecutar algunos comandos SQL:

::

   >>> cursor.execute("SELECT * FROM Students")
   5L

El metodo execute se usa para ejecutar comandos SQL. Note que no hace falta agregar el ';' (punto y coma) al final del comando. Ahora es cuestion de recorrer el objeto cursor.

Para obtener un solo elemento, usamos fetchone():

::

   >>> cursor.fetchone()
   (1L, 'Joe', 'Campbell', datetime.date(2006, 2, 10), 'N')

   >>> cursor.fetchall()
   ((1L, 'Joe', 'Campbell', datetime.date(2006, 2, 10), 'N'),
   (2L, 'Joe', 'Doe', datetime.date(2004, 2, 16), 'N'),
   (3L, 'Rick', 'Hunter', datetime.date(2005, 3, 20), 'N'),
   (4L, 'Laura', 'Ingalls', datetime.date(2001, 3, 15), 'Y'),
   (5L, 'Virginia', 'Gonzalez', datetime.date(2003, 4, 2), 'N'))

Cual metodo usar dependera de la cantidad de datos que tengamos, la memoria disponible en la PC y sobre todo, de como querramos hacerlo. Si estamos trabajando con datasets limitados, no habra problema con el uso de fetchall(), pero si la base de datos es lo suficientemente grande como para entrar en memoria, se podria implementar una estrategia como la que se encuentra aca:

::

   import MySQLdb
   db = MySQLdb.connect(host="localhost", user="root",passwd="secret", db="PythonU")
   cursor = db.cursor()
   recs=cursor.execute("SELECT * FROM Students")
   for x in range(recs):
      print cursor.fetchone()

O directamente:

::

   import MySQLdb
   db = MySQLdb.connect(host="localhost", user="root",passwd="secret", db="PythonU")
   cursor = db.cursor()
   cursor.execute("SELECT * FROM Students")
   for row in cursor:
      print row

(Sebastian Bassi)

-------------------------



¿Cómo me conecto a una base de datos con PostgreSQL?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Otro ejemplo basico de como hacerlo con PostgreSQL (similar al de MySQL).  Se usó el esquema: ``CREATE TABLE estudiante ( nombre varchar,  apellido varchar,  fecha date,  booleano bool,  legajo serial PRIMARY KEY);`` Antes que nada se debe instalar el conector (`para unix y windows`_).

Primero importar el conector y crear la conexión a la base de datos:

::

   >>> import psycopg2, psycopg2.extras
   >>> conn = psycopg2.connect(database='test',user='postgres',password='pass', host='localhost')

Luego crear un cursor para obtener los datos y ejecutar consulta:

::

   >>> cur = conn.cursor()
   >>> cur.execute("SELECT * FROM estudiante")
   >>> rows=cur.fetchall()
   >>> print rows

   [['Joe', 'Capbell', datetime.date(2006, 2, 10), False, 1], ['Joe', 'Doe', datetime.date(2004, 2, 16), False, 2], ['Rick', 'Hunter', datetime.date(2005, 3, 20), False, 3], ['Laura', 'Ingalls', datetime.date(2001, 3, 15), True, 4], ['Virginia', 'Gonzalez', datetime.date(2003, 4, 2), False, 5]]

Algo más pitónico es crear el cursor simil diccionario (en vez de una lista de valores):

::

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

**Nota:** esto es propio del conector psycopg2. Igualmente otros conectores tambien lo soportan o se puede imitar (leyendo el atributo description del cursor que tiene la información de los campos):

::

   >>> print cur.description
   (('nombre', 1043, 8, -1, None, None, None), ('apellido', 1043, 8, -1, None, None, None), ('fecha', 1082, 10, 4, None, None, None), ('booleano', 16, 1, 1, None, None, None), ('legajo', 23, 1, 4, None, None, None))

-------------------------



Parámetros
~~~~~~~~~~

**Pregunta:** Hola chicos. Estoy con un inconveniente que no puedo solventar. Tengo una funcion de python que genera unos querystrings para postgres.

Mi problema empieza cuando, por ejemplo hay uno de esos apellidos que tienen ', Ej: D'agostino

como resultado me queda el string (ejemplo)

::

   'insert into personas (apellido) values ("D'agostino")'

**Respuesta:**

Lo que tendrías que hacer es que postgres te escapee automaticamente los valores, usando los parámetros de db-api (segúndo argumento del metodo execute del cursor):

::

     cur = conn.cursor()
     cur.execute("insert into personas (apellido) values (%s)" , ["D'agostino"])

Así, automáticamente postgres sabe, según el tipo de datos del parámetro, en este caso un string = "D'agostino", como escapear y formatear el sql para que no de error.

Además, esto es mas seguro frente a ataques por "inyección de sql", porque el formateo es automático, en vez de usar directamente el operador % sobre el query y pasarselo cocinado a la base.

Para hacerlo más robusto, podrías usar diccionario con los parametros (es más seguro en el caso que tengas varios parámetros, para evitar errores):

::

     cur.execute("insert into personas (apellido) values (%(apellido)s)" , {"apellido":"D'agostino"})

Igualmente, esto dependerá de las capacidades de cada conector (consultar variable paramstyle del módulo conector), pudiendo utilizarse los siguientes estilos de parametros:

* 'qmark': Signo de interrogación, ej. '...WHERE name=?'

* 'numeric': Numerico, posicional, ej. '...WHERE name=:1'

* 'named': por Nombre, ej. '...WHERE name=:name'

* 'format': Formato ANSI C, ej. '...WHERE name=%s'

* 'pyformat': Formato Python, ej. '...WHERE name=%(name)s'

.. ############################################################################

.. _`PEP 249: Python Database API Specification v2.0`: http://www.python.org/dev/peps/pep-0249/

.. _para unix y windows: http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo

