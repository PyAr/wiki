.. title: GnomeArt


este proyecto pretende remplazar el programa http://www.miketech.net/gnome-art/ pero programado en python, las tecnologias a usar son

* python

* pygtk

* subversion

Tareas
------

realizar interfaz con glade-3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aca se deben poner todas las ventanas, una descripcion de que hace y screenshots de cada una, luego cada uno puede agarrar una y hacerla en glade.

  Implementar los callbacks de los eventos, inicialmente se pueden hacer con dummies (que hagan prints como "abrir") para tener la infraestructura, luego cuando los modulos base esten andando se van a poder conectar ambos.

realizar modulo para interactuar con gnome-art
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se debe hacer un modulo para obtener la informacion de los themes, recomendable que sea con threads para no bloquear la interfaz, para ello se debera aprender a usar httplib, urllib, urllib2 o similar y threading, hay un ejemplo de threads y gtk aca GtkMultiThread y este es ejemplo ComunicarThreadsConQueue_.

Como ayuda se podria ver un poco el codigo de gnome-art, al menos para saber como interactua con el server.

Opcional: unittesting
~~~~~~~~~~~~~~~~~~~~~

Estaria bueno que aprendan a usar el modulo unittest http://docs.python.org/library/unittest.html y lo apliquen al proyecto

.. ############################################################################


.. _comunicarthreadsconqueue: /comunicarthreadsconqueue
