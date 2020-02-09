
Proyectos en los que se trabajó durante el Pycamp 2012
======================================================

Kivy
----

Se estuvo jugando con el framework kivy: http://kivy.org/ , que permite hacer aplicaciones para Android , programando en python  en nuestro entorno de trabajo habitual, y luego genera un APK compilando nuestro proyecto.

Se instaló el entorno de desarrollo, probaron varios ejemplos, se subieron a distintos dispositivos con distintas versiones de Android, y hasta se hizo una botonera pastillera:

Participantes: FelipeLerena_, HectorSanchez_, Mave, EzequielChan_ 

link apk: http://www.felipelerena.com.ar/static/BotoneraPastillera-1.0-debug.apk 

Nikola
------

Nikola es un generador de sitios estáticos con esteroides. Se le agregaron varias de las `features propuestas`_: pipelines, mejora en las galerias de imágenes, listing de código, temas de bootstrapwatch, etc.  Trabajaron Roberto Alsina, Hugo Ruscitti, Martín Gaitán

* repo: https://github.com/ralsina/nikola

* post: http://lateral.netmanagers.com.ar/tr/es/weblog/posts/pycamp-day-1.html

Hazte libro
-----------

Una libreria que genera epubs a partir de una lista de urls. Trabajaron Gozalo Odiard y Martín Gaitán

* repo: https://github.com/nqnwebs/haztelibro

Nota: En la charla acerca de generar ebooks colaborativamente, comenté acerca de un proyecto que hace algo similar, pueden verlo aqui: http://www.sourcefabric.org/en/booktype

Nuevo sitio de Pyar
-------------------

ver ideas en NuevoSitio_. Agreguen las suyas. Contactar con Joac. 

lai
---

Se agregaron algunas mejoras a la `versión original`_ y empezó con la `versión con u1db`_. En ambas queda resolver el caso en que debe hacerce un merge.

vim
---

- Usar el modo de edición de vim desde la línea de comandos (funciona en la consola de python):

::

       set -o vi # bash
       bindkey -v # zsh

  Agregarlo al .bashrc o .zshrc respec. También se puede setear creando un .inputrc (en bash)

::

       set editing-mode vi
       set keymap vi

  Hay muchas más opciones que se pueden setear (man 3 readline).

  Lista de comandos: `Bash vi editing mode cheat sheet`_

También vimos muchos plugins y cosas interesantes para agregarle a vim y que sea un mejor entorno de desarrollo con python. La mayoría está en https://github.com/fisadev/fisa-vim-config . Descubrimos que dos no andaban, uno ya está corregido (el que todavía no anda es el debugger, pero ya está identificado el problema). Y surgió la idea de meter el autocompletado de ninja ide en vim (como plugin). La gente de ninja va a separar la lógica del autocompletado como proyecto aparte, y nosotros vamos a meterlo en vim.

Spacecraft
----------

Se mejoró el servidor y se hicieron muchos bots

Nikola SaaS
-----------

Un servicio de blogs en la nube usando flask, celery, github y Nikola. Usando un post hook de nikola, el servicio se entera que se actualizaron los fuentes en gihub y actualiza el blog rende

Guitarra de verdad usada como MIDI
----------------------------------

Lucio y otros cumpas laburaron en un programita para detectar/aislar/filtrar notas de una guitarra eléctrica comun para usarla como guitarra para juegos estilo Guitar hero.

Cdpedia
-------

Se corrigieron algunos bugs y se terminó de emprolijar todo lo necesario para generar un nuevo dump.

OLPC
----

http://ar.sugarlabs.org . Se estuvo mostrando e instalando (ahora es mucho más facil en Ubuntu) el emulador para que se sumen colaboradores. 

ORM for Json
------------

Se agregaron soporte para YAML y puliendo cosas. Se `subió a PyPi`_

Encuentro
---------

Debido a que el contenido pasó al portal Conectate_ se estuvo laburando en terminar hacerlo andar y adapatando la UI a la nueva referencia. Se lanza nueva version en breve. 

Jugando con NLTK
----------------

Pablo celayes estuvo jugando con NLTK. 

Pilas en el navegador
---------------------

Se estudió la la libreria Skulpt para poder utilizar la API de pilas en el navegador y hacerlo andar sobre HTML5.

https://github.com/hugoruscitti/pilasweb

7 Wonders
---------

Una implementación en django de un juego de mesa, https://github.com/dmoisset/evolve

Se mejoro la UI con bootstraps css. Se cargaron datos (cartas y demás cosas necesarias). Se corrigieron algunos bugs. Se subió un embrión de API REST para poder hacer otras interfaces.

Pronto se pushea y se sube para jugar 

NINJA-IDE
---------

Se migro el código de NINJA-IDE a la API2 de PyQt_, se resolvieron bugs (uno bastante critico: thx perrito), se identificaron nuevas features y mejoras para hacer. Y se sumo gente para trabajar en algunos Plugins. Tambien se mostraron algunas de las caracteristicas y features que consideramos valiosas de ninja y se mostro un pantallaso de que hacer para ponerser a jugar con el codigo de ninja.

Otras actividades
-----------------

- se jugó al futbol - torneo de pingpong - taller de malabares (un éxito! descubriendo talentos ocultos en los geeks) - telescopio

QML
---

J0hn y Gatox estuvieron mirando QML para armar interfaces "piolas" en un codigo rápido estilo json. Se vieron varios ejemplos de QML de aca: http://doc.qt.nokia.com/4.7-snapshot/qdeclarativeexamples.html Y se empezo un proyectito muy chico para jugar un poco con como se hacen las cosas en QML: https://github.com/diegosarmentero/python_qml

Kinect
------

Se estuvo jugando con el procesamiento de imágenes y el kinect (transparencia, detección de bordes de primer plano, etc) (Joac, Manuq, perrito) y para relevar mapas 3D de un espacio fisco (Lucio)

generador de certificados SSL
-----------------------------

Plugins de lalita
-----------------

Exportar eventos de lalita para usar "plugins" en procesos externos. 

MOVErónica
----------

Siguiendo el concepto de MOVE (Modelo, Operacion, Vistas y Eventos) y usando mongomodels_ y Juggernaut_ para nuestros modelos con eventos, hicimos una aplicación de demo que actualiza una pagina estática desde cualquier cliente python que conozca los modelos sin realizar ningún tipo de request. El código se puede ver en MOVEapp_ 

Documentator
------------

En el viaje de vuelta hablando con x-ip, ralsina y gatox, surgio la idea de usar un parte del codigo de ninja que saca la estructura del archivo, con los docstrings de cada clase y funcion, para que genere cierta informacion html, combinarlo con graphviz para los diagramas de clase y navegabilidad, y proveer la documentacion de un proyecto con Nikola SaaS

cocos
-----

Yamila le hizo un background animado bastante copado a Enjuewemela

El feature de un render fallback para particulas cuando no hay soporte de gl point sprites adquirio forma definitiva y llego a trunk

Una miniutilidad para editar visualmente caminos (secuencia de puntos) fue explorada a nivel de minima funcionalidad; se puede incorporar a cualquier app cocos porque esta autocontenida en un layer. Falta generalizar algunas cosas.

.. ############################################################################

.. _features propuestas: http://lateral.netmanagers.com.ar/tr/es/weblog/posts/nikola-ideas-for-pycamp.html

.. _versión original: https://github.com/lvidarte/lai

.. _versión con u1db: https://github.com/lvidarte/lai-u1db

.. _Bash vi editing mode cheat sheet: http://www.catonmat.net/download/bash-vi-editing-mode-cheat-sheet.pdf

.. _subió a PyPi: http://pypi.python.org/pypi/Ojota

.. _Conectate: http://conectate.gov.ar

.. _mongomodels: http://github.com/dlitvakb/mongomodels

.. _Juggernaut: http://github.com/maccman/juggernaut

.. _MOVEapp: http://github.com/dlitvakb/moveapp

.. _hectorsanchez: /pages/hectorsanchez.html
.. _nuevositio: /pages/nuevositio.html
.. _pyqt: /pages/CharlasAbiertas2010/pyqt.html
