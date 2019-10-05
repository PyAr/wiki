
Resultados PyCamp 2009
~~~~~~~~~~~~~~~~~~~~~~

Esto es un resumen de lo que se trabajó durante este exitoso Campamento Python.

**Nota para los escritores, luego la sacamos:**

* *La idea es que todos los que participaron agreguen algo en lo que se hizo, a menos que ya se haya comentado.*

* *Fíjense que agregué todos los proyectos que teníamos anotados en el schedule, pero es sólo una guía general, siéntanse libres de agregar otras cosas que se hicieron o* sacar aquellos proyectos en los que al final no se hizo nada...

* *Estaría bueno que los champion de los distintos proyectos tomen la iniciativa... esta página es un buen ejemplo para repartir y valorizar el laburo que hacemos todos cada vez que nos reunimos...*

CD Pedia
--------

Se incorporaron muchos nuevos participantes al proyecto, los que probaron y arreglaron numerosos bugs. Se incorporó algo de funcionalidad, pero el mayor esfuerzo estuvo orientado a la optimización del índice existente, y pruebas de distintos motores de índices o bases de datos, para ver cual es la mejor opción para que el proyecto escale correspondientemente.

Este paso estaría lo suficientemente avanzado como para que empecemos a preocuparnos en qué articulos recortar (obviamente no podemos poner los 20 G de textos, casi un millón y medio de artículos...), lo cual va a repercutir directamente en ls imágenes a incorporar y, obviamente, el índice.

Más datos:

* Sitio del proyecto: http://code.google.com/p/cdpedia

* Lista de correo: http://groups.google.com/group/cdpedia

Bug day
-------

Hubieron dos cazas de bugs, una para Python y otra para Django. La primera no estuvo demasiado productiva (con la complicación de que no tenía acceso SSH, así que que yo haga un comit de algo no era una opción), pero luego de un extenso análisis de Humitos pudimos al menos cerrar un bug, 🙂

Se estuvo trabajando un rato bastante largo en la corrección de bugs de Django, de mi parte (Humitos), estuve viendo algunos bugs de documentación, falta de documentación y algunos errores en la misma. Otros, por su parte, estuvieron trabajando en bugs de código en sí. El resumen de los bugs en los que trabajamos se puede encontrar acá:

* `Tickets de pycamp2009`_

PythonCard
----------

Nos reunimos un par y vimos que uso le daba cada uno, comentamos cuales eran las complicaciones actuales (bugs, herramientas poco integradas, etc.) y como encarar un proyecto para mejorarlo. Seguramente creemos un trac en USLA para "revivir" esta herramienta.

PyConTech
---------

Aca también se incorporaron varios participantes nuevos, no solo desarrolladores sino testers y traductores, lo que estubo muy bueno y nos permitió avanzar y definir muchas cosas.

Por un lado, se encaró la parte de traducción y revisión de contenidos, y por otro la app de registración gratuita. Si bien no le dedicamos mucho tiempo, se avanzo bastante en ambos puntos.

Quedamos en seguir los temas por la lista de pyconar-admin.

Mejorar naushika
----------------

Cocos2d
-------

En términos generales, todo giró alrededor de crear un editor de mapas no tileados (es decir, donde los sprites puedan estar en posiciones arbitrarias y no necesariamente en un layout de grilla),  inspirado en el video acerca del editor de mapas del juego Aquaria [0]. Eventualmente, el editor pasará a formar parte de Cocos2d,  pero por el momento está aparte y no cuenta con un repositorio público.

* [0] http://blog.wolfire.com/2009/01/aquaria-design-tour/

Reply
-----

El primer día se intentó trabajar un poco en mejorar reply [0], proveyéndole soporte para la librería rl-glue [1], lo que habilitaría usar reply para crear agentes y entornos que luego puedan user compartidos (y reutilizados) sin necesidad de ser modificados. Esto también permitiría poder participar de competencias de Aprendizaje por Refuerzo, que usan rl-glue como interface entre los distintos agentes que compiten.

Sin embargo, como los que iban a participar de reply, también participaron en Cocos2d, este proyecto quedó sin hacerse.

* [0] http://reply.googlecode.com

* [1] http://glue.rl-community.org

Karma@pyar
----------

Se presento el proyecto mas formalmente y se discutió su utilidad.

Después un grupo empezó a pensar en la implementación.

Armamos un modelo del sistema. Estuvimos trabajando en los filtros del mismo para integrarlos, al menos para empezar, con mailman y postfix.

Lo que hicimos, y algunas cosas mas que fuimos agregando y todo, se encuentra en el trac del proyecto: http://trac.usla.org.ar/proyectos/pykarm

Sysadmining
-----------

Hubo una reunión el domingo por la tarde donde se comentó el estado de las migraciones y upgrades del wiki de PyAr_ y de la lista de correo.

Luego de la reunión, RamiroMorales_ consiguió finalizar el proceso de migración del wiki a una versión más nueva de Moin en una instalación local, a partir de un dump del moin que tenía un par de meses de antigüedad. Dave estuvo viendo de instalar pykarm en el server virtual de usla, instalando y configurando para esto un mailman. Se acordó hacer un sprint virtual de administración donde se terminen de hacer las migraciones pendientes.

acheckersgame
-------------

Mejoramos muchos aspectos de un videojuego de damas llamado acheckersgame. El primer día lo dedicamos a estudiar y analizar por completo el juego, ya que sumamos dos participantes nuevos al proyecto. Escribimos una documentación para programadores y refactorizamos muchos aspectos importantes.

El segundo y tercer día armamos el algoritmo para comer piezas, recorrer caminos y aplicar reglas del juego como 'estar obligado a comer' , y poder coronar. Otro cambios fueron, poder jugar con el teclado, y algunas funciones a modo de debug, como eliminar fichas y convertir fichas a damas. También mejoramos la interfaz y su interacción con el usuario, como animaciones y consejos para jugar.

El código completo del programa lo pueden obtener desde el repositorio de software [0] en google code.

* [0] http://code.google.com/p/acheckersgame/

PyCamp
------

PyCon2009
---------

.. ############################################################################

.. _Tickets de pycamp2009: http://code.djangoproject.com/query?status=new&status=assigned&status=reopened&status=closed&keywords=~pycamp2009&order=priority



.. _pyar: /pages/pyar
.. _ramiromorales: /pages/ramiromorales
