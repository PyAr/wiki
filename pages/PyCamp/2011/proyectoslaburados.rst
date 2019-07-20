
PyCamp 2011: Proyectos en los que laburamos
===========================================

Esta es una lista de los proyectos sobre los que trabajamos durante el PyCamp_ y que fueron presentados durante el cierre del mismo.

Geoarcade
---------

* geoarcade_: Con el objetivo de introducir a nuevos en Django, aprender algo de spatial databases y jugar con HTML5, CSS3 y la base de datos de open street map, nació este pequeño proyecto. El proyecto es un localizador de Fichines o Arcades. Cualquier usuario se registra y puede agregar un nuevo fichín marcando su posición exacta en el mapa. Pronto estará deployado en algún lugar.

pilasnet
--------

Junté el reactor de twisted con el bucle de pygame de pilas, y levanté un twisted.manhole para que mucha gente pueda entrar a la instancia de pilas por ssh. Gracias a Juanjo Conti por su blogpost con una receta para usar manhole pude hacer todo esto en 15 minutos antes de las presentaciones del fin de PyCamp_. Ahora le mandé a Hugo un diff para que si le gusta lo pueda emprolijar un poco e integrar a pilas.

Grafo wiki PyAr
---------------

Estuvimos trabajando en un grafo navegable de los enlaces entre paginas del wiki. Respecto  la version anterior en graphviz que se puede ver `acá`_, utilizamos unas libs en javascript llamadas `The jit`_ que genera unas animaciones muy bonitas. Nos falta levantar la aplicacion en la VM de pyar.

faldatouch
----------

#Fixme Completar

zodbbrowser
-----------

#Fixme Completar

pep8fy
------

Pep8fy_ fue una idea de RobertoAlsina_ y como su nombre lo indica, es un pep8ficador de código. La popular herramienta `pep8.py`_ se limita a ejercer el poder acusador de decirte que tu código no pasa la PEP8. En cambio, Pep8fy aspira a hacer esta tarea automáticamente.  La arquitectura es muy simple: con el modulo tokenizer se obtiene una lista de tokens del módulo a pep8ficar que se manipulan mediante una serie de filtros (uno para cada regla definida en la PEP8) y al final se regenera el código con la lista de tokens alterados.  Se lograron algunos filtros, pero es un trabajo en desarrollo. 

modulo video pilas
------------------

Perrito integró opencv a pilas, y creó dos nuevos actores, uno para tener un video en la pantalla de pilas o otro para poder observar la webcam dentro de pilas. El resultado estúvo buenisimo, los videos pueden rotar, escalar o incluso rebotar cómo una pelota...

i18n pilas
----------

Achuni creó una implementación para que pilas pueda traducirse a varios idiomas, modificó el comportamiento builtin de la sentencia "import" para que se reconstruya dinámicamente un alias de pilas en otro idioma. En medio hay un diccionario que define la traducción para cada cadena.

peewee
------

MarianoGarcia_, EmilianoDallaVerdeMarcozzi_, MarcosVanetta_ y MateoBengualid_ se dedicaron a darle soporte para MySQL a  PeeWee_. PeeWee_ es un ORM liviano ( un solo archivo ) ahora con soporte para Sqlite, MySQL y Postgresql.

Port de Twisted a Python 3
--------------------------

Facundo B siguió con un branch que tenía de antes, lo terminó y ya está en trunk. Nueces arrancó un branch desde cero, el cual desembocó en muchos tickets con sendos parches, los cuales entraron ya a trunk. Muy productivo!

CDPedia
-------

Viejos y nuevos contribuyentes al hermoso y noble proyecto CDPedia_ estuvimos laburando en algunas tareas para obtener la version 0.7 . A partir de los cambios realizados, se empaquetará un nuevo DVD de CDPedia para presentar a Educ.ar que tiene firme interés en enviar copias de esta enciclopedia a todas las escuelas del pais. 

Algunos cambios importantes fueron el empaquetado de imágenes en bloques, que permite un aprovechamiento importante en el espacio utilizado. Tambien se creó un generador de "bogus" al vuelo. (la imágen que se muestra cuando la imágen original no está en el CD) que suprime el problema de la variedad de tamaños y la posibilidad de que se vean feos por forzar las dimensiones. . Algunas funciones fueron mejoradas:o la obtención de un artículo al azar ahora se realiza mediante una redirección http que cambia la URL (antes cambiaba el contenido aleatoriamente, pero la url se mantenia en \al_azar). Por último, retoques de CSS y plantillas. 

Bug days
--------

Se hizo un bugday de Python y de Django, de forma presencial y virtual. Con respecto a Python se trabajó en un sólo ticket, pero varias personas aprendieron a conocer un poco las fuentes y el workflow de desarrollo; se charló mucho acerca de Mercurial, y cómo usarlo mejor para el proyecto (en sintonía con la larguísima discusión sobre el mismo tema en la lista python-dev). En Django se trabajó un poco más, sobre cinco tickets, logrando integrar a un desarrollador nuevo al workflow de Django.

Luisito (el enano)
------------------

SAn estuvo reescribiendo luisito_ basado en una nueva estrategia charlada con Alecu y RAlsina. Alecu le dio una mano gigante para entender mejor dónde convenia pararse dentro de twisted.web.proxy. También se escribieron algunos casos de prueba y Facu B le tiro unos tips a SAn de cómo convenía implementarlos.

-------------------------

 CategoryPyCamp_

.. ############################################################################

.. _geoarcade: https://launchpad.net/geoarcade

.. _acá: http://python.org.ar/moin_static/pyar/grafo_5.svg

.. _The jit: http://thejit.org

.. _Pep8fy: https://bitbucket.org/edvm/pep8fy

.. _pep8.py: http://pypi.python.org/pypi/pep8

.. _PeeWee: https://github.com/coleifer/peewee

.. _CDPedia: http://code.google.com/p/cdpedia/

.. _luisito: http://bitbucket.org/san/luisito

.. _marianogarcia: /pages/marianogarcia
.. _emilianodallaverdemarcozzi: /pages/emilianodallaverdemarcozzi
.. _marcosvanetta: /pages/marcosvanetta
.. _categorypycamp: /pages/categorypycamp
