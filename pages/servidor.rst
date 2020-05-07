.. title: Migración a Debian Wheezy


`2013-06-06T09:28:29-0300`

Servicios
---------

* Apache 2.2.22

* Postfix 2.9.6

* Mailman 2.1.15

Migración de la Moin
--------------------

* Funcionando sobre mod-wsgi, bajo el usuario www-pyar

* Sobre Python2.6 por los sitios de pycon (supongo que algún error de

    sintaxis)

* Sed rule sobre moin_static182 to moin_static

* Reconstrucción del cache

Migración de los sitios pycon
-----------------------------

* Funcionando sobre mod-wsgi, bajo el usuario www-pycon

* Sobre Python2.6 porque sobre Python2.7 no levantaba, supongo que algún error de sintaxis.

* El sitio de 2012 estaba desactivado (SUSPEND_SERVICE = True en applications/2012/models/0.py)

* Reconstrucción de todas las apps.

Migración de las listas (Mailman)
---------------------------------

* Regeneración de los archivos de cada lista y se fixearon permisos.

* Bastante out of the box, gracias a las tools que trae mailman y a la ayuda

    de dererk.

To improve
----------

* Usar Python2.7 para mod-wsgi, para esto hay que chequear las applicaciones

    pycon que corren sobre web2py.

* Utilizar web2py del OS (python-web2py), esto facilita actualizaciones

    futuras, actualizaciones de seguridad, etc.

* Theme de pyar:

  * Tiene hardcodeados los paths a static_moin

  * Versiones de jquery incrustadas en el theme (debería usar la del OS)

