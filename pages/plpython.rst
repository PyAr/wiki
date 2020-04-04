.. title: Pl/Python: Python dentro de PostgreSQL


El lenguaje procedural plpython permite escribir funciones python para la base de datos relacional PostgreSQL.

Como se puede acceder a todas las funciones de python, no debe usarse para usuarios no confiados, por eso se lo llama plpythonu (u=untrusted).

Para más información ver `Sitio del Grupo de Usuarios de PostgreSQL Argentina`_, sección PlPython_

Funciones ("Procedimientos almacenados")
----------------------------------------

El cuerpo de una funcion plpythonu es simplemente un script de Python.  Cuando la función es llamada, sus argumentos son pasados como elementos de una lista ``args``; los argumentos por nombre son pasados como variables ordinarias.  El resultado es devuelto de la manera usual, con un ``return`` o un ``yield`` (en el caso que devuelvan un conjunto de resultados)

Los valores ``NULL`` de PostgreSQL equivalen a ``None`` en Python.

Está disponible el diccionario ``SD`` para almacenar datos entre cada llamada a función, y el diccionario globar ``GD`` para usar desde todas las funciones.

**Nota**: PostgreSQL 8.1 no soporta argumentos por nombre, recibir valores compuestos, devolver listas/tuplas o usar generadores.

Ejemplo simple
~~~~~~~~~~~~~~

Calcular el valor máximo entre dos enteros, descartando valores nulos:

.. code-block:: sql

   CREATE FUNCTION pymax (a integer, b integer)
     RETURNS integer
   AS $$
     if (a is None) or (b is None):
       return None
     if a > b:
       return a
     return b
   $$ LANGUAGE plpythonu;

   -- invoco la función:
   SELECT pymax(2, 3);
   -- devuelve 3

Recibir tipos compuestos
~~~~~~~~~~~~~~~~~~~~~~~~

Las funciones plpython pueden recibir tipos compuestos (ej.registros de tablas) como diccionarios:

.. code-block:: sql

   CREATE TABLE empleado (
     nombre TEXT,
     salario INTEGER,
     edad INTEGER
   );

   CREATE FUNCTION sueldo_alto (e empleado)
     RETURNS boolean
   AS $$
     if e["salario"] > 200000:
       return True
     if (e["edad"] < 30) and (e["salario"] > 100000):
       return True
     return False
   $$ LANGUAGE plpythonu;

Devolver tipos compuestos
~~~~~~~~~~~~~~~~~~~~~~~~~

Los tipos compuestos pueden ser devueltos como secuencias (tuplas o listas), diccionarios u objetos. En este ejemplo se devuelve un tipo compuesto representando una persona:

.. code-block:: sql

   CREATE TYPE persona AS (
     nombre   TEXT,
     apellido TEXT
   );

   CREATE FUNCTION crear_persona (nombre TEXT, apellido TEXT)
     RETURNS persona
   AS $$
     return [ nombre, apellido ]
     # o como tupla: return ( nombre, apellido )
     # o como diccionario: return { "nombre": nombre, "apellido": apellido }
   $$ LANGUAGE plpythonu;

   CREATE FUNCTION crear_persona (nombre TEXT, persona TEXT)
     RETURNS persona
   AS $$
     class Persona:
       def __init__ (self, n, a):
         self.nombre = n
         self.apellido = a
     return Persona(nombre, apellido)
   $$ LANGUAGE plpythonu;

Devolver múltiples tipos escalares o compuestos (''set-of'')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se puede devolver múltiples valores (usando listas/tuplas, iteradores o generadores).  En este ejemplo se devuelven varios saludos:

.. code-block:: sql

   CREATE TYPE saludo AS (
     mensaje TEXT, -- hola
     a_quien TEXT  -- mundo
   );

   CREATE FUNCTION saludar (mensaje TEXT)
     RETURNS SETOF saludo
   AS $$
     # devolver una tupla conteniendo lista de tipos compuestos
     # todas las otras combinaciones son posibles
     return ( [ mensaje, "Mundo" ], [ mensaje, "PostgreSQL" ], [ mensaje, "PL/Python" ] )
   $$ LANGUAGE plpythonu;

   CREATE FUNCTION saludar_generador (mensaje TEXT)
     RETURNS SETOF saludo
   AS $$
     for a_quien in [ "Mundo", "PostgreSQL", "PL/Python" ]:
       yield ( mensaje, a_quien )
   $$ LANGUAGE plpythonu;

Disparadores (Triggers)
-----------------------

Cuando una función plpython es usada en un disparador, el diccionario ``TD`` contiene:

* ``TD["new"]``: valores nuevos de la fila afectada (diccionario)

* ``TD["old"]``: valores viejos de la fila afectada (diccionario)

* ``TD["event"]``: tipo de evento "INSERT", "UPDATE", "DELETE", o "UNKNOWN"

* ``TD["when"]``: momento en que se ejecutó: "BEFORE" (antes del commit), "AFTER" (despues del commit), o "UNKNOWN"

* ``TD["level"]``: nivel al que se ejecutó: "ROW" (por fila), "STATEMENT" (por sentencia), o "UNKNOWN"

* ``TD["name"]``: nombre del disparador

* ``TD["table_name"]``: nombre de la tabla en que se disparó

* ``TD["table_schema"]``: esquema en el que se disparó

* ``TD["relid"]``: OID de la tabla que disparó

* Si el comando ``CREATE TRIGGER`` incluyó argumentos, estos estarán disponibles en  la lista ``TD["args"]``

Si ``TD["when"]`` es BEFORE, se puede devolver ``None`` or "OK" para indicar que la fila no se modificó, "SKIP" para abortar el evento, o "MODIFY" para indicar que hemos modificado la fila.

Acceso a la base de datos
-------------------------

Automaticamente se importa un módulo llamado ``plpy``.

Generar mensajes y lanzar errores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este módulo incluye funciones de ``plpy.debug(msg)``, ``plpy.log(msg)``, ``plpy.info(msg)``, ``plpy.notice(msg)``, ``plpy.warning(msg)``, ``plpy.error(msg)``, y ``plpy.fatal(msg)``

``plpy.error`` y ``plpy.fatal`` en realidad disparan una excepción python, si no se controla, se propaga y causa que la transacción se aborte. Equivalente a llamar ``raise plpy.ERROR(msg)`` y ``raise plpy.FATAL(msg)``, respectivamente

Las otras funciones solo generan mensajes en los distintos niveles de prioridad.

Preparar y ejecutar consultas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adicionalmente, el módulo ``plpy`` provee dos funciones: ``execute`` y ``prepare``.

Llamar a ``plpy.execute(query, limit)`` con una consulta (query: string) y un límite de registros opcional (limit),  permite ejecutar la consulta y devuelve los resultados en un objeto que emula una lista de diccionarios, pudiendo acceder por número de fila y nombre de columna. Tiene tres métodos adicionales: ``nrows`` que devuelve el número de filas, y ``status``.

Ejemplo:

.. code-block:: python

   rv = plpy.execute("SELECT * FROM mi_tabla", 5)
   for fila in rv:
      print fila['columna']

La función ``plpy.prepare(query,[parameter_types])``, prepara el plan de ejecución para una consulta, se le pasa la consulta como string y la lista de tipos de parámetros:

.. code-block:: python

   plan = plpy.prepare("SELECT apellido FROM usuario WHERE nombre = $1 AND casado = $2 ", [ "text", "boolean" ])

``text`` y ``boolean`` son los tipos de la variables que se pasara como parámetros ($1 y $2).

Despues de preparar la sentencia, usar la función ``plpy.execute`` para ejecutarla:

.. code-block:: python

   rv = plpy.execute(plan, [ "Mariano", True ], 5)

Se pasa el plan como primer argumento, los parámetros como segundo (en este caso, busca nombre="Mariano" y si esta casado). El límite (tercer argumento) es opcional.

Al preparar un plan, este se almacena para usarlo posteriormente. Para usarlo eficazmente entre llamada y llamada, se debe usar un diccionario de almacenamiento persistente (``SD`` o ``GD``) para guardarlo:

.. code-block:: sql

   CREATE FUNCTION usar_plan_guardado() RETURNS trigger AS $$
       if SD.has_key("plan"):
           plan = SD["plan"] # está el plan, lo reutilizo
       else:
           # no esta el plan, lo creo y almaceno en el diccionario persistente
           plan = plpy.prepare("SELECT 1")
           SD["plan"] = plan
       # continua la función...
   $$ LANGUAGE plpythonu;

.. ############################################################################

.. _Sitio del Grupo de Usuarios de PostgreSQL Argentina: http://www.arpug.com.ar/

.. _PlPython: http://www.arpug.com.ar/trac/wiki/PlPython

