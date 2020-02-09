
ORMs
----

Que es?
~~~~~~~

El mapeo objeto-relacional (más conocido por su nombre en inglés, Object-Relational mapping, o sus siglas O/RM, ORM, y O/R mapping) es una técnica de programación para convertir datos entre el sistema de tipos utilizado en un lenguaje de programación orientado a objetos y el utilizado en una base de datos relacional, utilizando un motor de persistencia. En la práctica esto crea una base de datos orientada a objetos virtual, sobre la base de datos relacional. Esto posibilita el uso de las características propias de la orientación a objetos (básicamente herencia y polimorfismo). Hay paquetes comerciales y de uso libre disponibles que desarrollan el mapeo relacional de objetos, aunque algunos programadores prefieren crear sus propias herramientas ORM.

mas información en wikipedia_

Threads relacionados en PyAr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Que ORM python me recomiendan?`_

Alternativas
~~~~~~~~~~~~

Sqlalchemy
::::::::::

SQLAlchemy es el toolkit SQL python y mapeador objeto relacional que provee a desarrolladores con el poder completo y la flexibilidad de SQL.

Provee un conjunto completo de conocidos patrones de persistencia de nivel enterprise, diseniados para acceso a base de datos eficiente y de alta performance, adaptado en un lenguaje de dominio especifico simple y pitonico.

`Pagina del proyecto`_

Notas
,,,,,

  MarianoGuerra_: muy poderoso, pero a veces muy complejo para lograr cosas simples. A mi entender el mas mantenido y completo de todos los ORMs independientes de un framework.

SQLObject
:::::::::

SQLObject es un gestor objeto relacional que provee interfaces de objetos a tu base de datos con tablas como clases, filas como instancias y columnas como atributos.

SQLObject incluye un lenguaje de consultas basado en objetos Python que hace SQL mas abstracto, y provee independencia sustancial de la base de datos para aplicaciones.

`Pagina del proyecto <http://www.sqlobject.org/>`__

Elixir
::::::

Elixir es una capa declarativa sobre la librería SQLAlchemy, es una capa bastante fina, que provee la habilidad de crear simples clases en python que mapean directamente a tablas de una base de datos relacionales (este patrón es conocido como el patrón de disenio Active Record), proveyendo muchos de los beneficios de las bases de datos tradicionales sin perder la conveniencia de los objetos python.

Elixir tiene la intención de reemplazar la extensión ActiveMapper_ de SQLAlchemy, y el proyecto TurboEntity_ pero no intena reemplazar las características básicas de SQLAlchemy, en su lugar se enfoca en proveer una sintaxis mas simple para definir modelos de objetos cuando no necesitas la expresividad del mapeo manual de definiciones de SQLAlchemy.

`Pagina del proyecto <http://elixir.ematia.de/trac/wiki>`__

Notas
,,,,,

  MarianoGuerra_: una herramienta muy útil para facilitar el uso de SQLAlchemy, según tengo entendido no esta siendo activamente mantenido.

Peewee
::::::

* pequeño orm

* escrito en python

* provee una interfaz de consulta liviana sobre sql

* usa conceptos sql en las consultas, como joins y clausulas where

* soporta sqlite, mysql, postgresql

Documentacion_ `Pagina del proyecto <https://github.com/coleifer/peewee/>`__

Específicos de un framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django ORM
::::::::::

ORM del framework web de django.

Un modelo es la fuente única y definitiva de información sobre tus datos, contiene los campos esenciales y comportamientos de los datos que almacenas. Generalmente, cada modelo mapea a una tabla única en la base de datos.

`Documentación`_ `Mas documentación`_

Notas
,,,,,

  MarianoGuerra_: La mejor opción si vas a hacer una aplicación en django ya que provee buena integración con el resto de django, si elegís otra opción podes perder esta integración.

Web2py ORM
::::::::::

web2py incluye una capa de abstracción de base de datos (DAL), una API que mapea objetos python a objetos de la base de datos como queries, tablas, registros.

El DAL genera SQL dinámicamente en tiempo real usando el dialecto especifico de la base de datos, de manera que no tenes que escribir SQL o aprender diferentes dialectos (el termino SQL es usado genéricamente), y la aplicación sera portable entre distintos tipos de bases de datos.

Al momento de escribir esto las bases de datos soportadas son SQLite (que viene con python y por lo tanto web2py), PostgreSQL, MySQL, Oracle, MSSQL, FireBird_, DB2, Informix, Ingres y (parcialmente) Google App Engine (SQL y NoSQL).

Experimentalmente soporta mas bases de datos, visita el sitio web de web2py y la lista de correos para adaptadores mas recientes.

`Documentación <http://web2py.com/book/default/chapter/06>`__

.. ############################################################################

.. _wikipedia: https://es.wikipedia.org/wiki/Mapeo_objeto-relacional

.. _Que ORM python me recomiendan?: http://thread.gmane.org/gmane.org.user-groups.python.argentina/53971

.. _Pagina del proyecto: http://www.sqlalchemy.org/




.. _Documentacion: http://charlesleifer.com/docs/peewee/

.. _Documentación: https://docs.djangoproject.com/en/1.4/topics/db/

.. _Mas documentación: https://docs.djangoproject.com/en/1.4/#the-model-layer


.. _marianoguerra: /pages/marianoguerra.html
