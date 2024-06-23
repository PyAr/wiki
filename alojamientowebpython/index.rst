.. title: Alojamiento para aplicaciones Web Python


**Última actualización: 2012-04-11**

Cuando pensamos crear u sitio o aplicación Web, o cuando ya lo hemos desarrollado y queremos pasar a la etapa de producción llegamos al punto en el cual necesitamos la infraestructura necesaria para mantener el mismo disponible para sus usuarios. Si no se dispone de un propio la opción es contratar el servicio

Invitamos a todos a mantener esta página actualizada, particularmente a quienes:

* Tienen experiencia con las distintas compañías que ofrecen este tipo de servicio

* Han consultado sobre este tema en la lista de correo de PyAR, han recibido ayuda y han llegado a una conclusión exitosa o a una experiencia negativa con un proveedor X. Es una buena forma de devolver a la comunidad y mantener el nivel técnico de la información que manejamos todos.

Ver también el `artículo en Wikipedia`_ que contiene más información general.

Alojamiento Web compartido (''shared hosting'')
-----------------------------------------------

Internacional
~~~~~~~~~~~~~

* Webfaction (http://www.webfaction.com/)

Sistemas Virtuales Privados (''Virtual Private System'' o VPS)
--------------------------------------------------------------

Sistemas gratuitos
------------------

¿?

Lista de verificación (''checklist'') para contratar un servicio
----------------------------------------------------------------

* ¿Qué método(s) de interfaz servidor Web <-> Aplicación web Python ha implementado?

  * WSGI

  * FastCGI

  * mod_python (no recomendado, este método se ha abandonado)

  * CGI (¡definitivamente no!)

* ¿Qué componentes y qué esquema técnico ha implementado/diseñado el proveedor?

    Servidor Web

  * Apache

  * Nginx

  * Nginx+Gunicorn

  * Lighttpd

  *

  * ...

    Otras partes

  * mod_wsgi

  * uWSGI

    También puede ser útil conocer:

  * Publicación de secciones dinámicas (aplicación web Python) y recursos estáticos (imágenes, hojas de estilo, código JavaScript_) con servidores separados.

  .. ############################################################################

  .. _artículo en Wikipedia: http://es.wikipedia.org/wiki/Alojamiento_web

  .. _JavaScript: ../JavaScript

