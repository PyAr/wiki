.. title: Actividades

Estas son propuestas, en el PyCamp el primer día se hace una votación para elegir a cuáles de estos proyectos o ideas vamos a dedicar tiempo (este procedimiento lo tenemos que terminar de definir).


fades
-----

Fixear algún bug o meter algún feature en fades (fades is a system that automatically handles the virtualenvs in the cases normally found when writing scripts and simple programs, and even helps to administer big projects).

Propone: FacundoBatista


__init__
---------

La idea es hacer un taller de "como sumarte a un proyecto del pycamp" explicando python, debug, git, virtualenv, etc para que quien esta dando sus primeros pasos pueda integrarse facilmente.
Te recomiendo sumarte si recien arrancas.
Y si ya sabes todo esto, veni a dar una mano.

Requirements: python, git, virtualenv. Opcionales: ipython, ipdb, virtualenvwrapper, etc

Propone: Mati Barriento


Web PyAr
---------

Según entiendo, hay conflictos para actualizar el branch master del sitio web de PyAr. En develop hay features nuevos.
Propongo trabajar en equipo para destrabar eso.

Requirements: lo que haga falta para poner en marcha https://github.com/PyAr/pyarweb

Propone: Litox


Programación: Qué es esto?
--------------------------

Un tallercito para aprender a aprender a programar desde 0, o refrezcar las neuronas

Requirements: Lapiz y papel o compu y muchas ganas

Propone: DavidLitvak


Metaprogramación en Python
--------------------------

Un tallercito para aprender conceptos avanzados de programación, en particular, metaprogramación.
Para qué sirve? Cómo se usa? Situaciones reales donde esto sirve.

Requirements: Python 2.7+ o 3.x y algun editor de texto o IDE que prefieras

Propone: DavidLitvak


Mirror PyPI - Una mejor alternativa
-----------------------------------

Cada PyCamp traemos un mirror de PyPI completo, pero cada vez crece más en tamaño, la estructura interna de PyPI
varía y todos nos volvemos un poco más locos. Por lo tanto, estaría bueno armar una solución un poco mas robusta.
Similar a DevPI pero con un poco mas de configurabilidad y la posibilidad de hacer un buen warm-up via config.
El fín del proyecto, es poder meterlo en nuestra "valijita pycampera" y poder tenerlo disponible en cada PyCamp
por venir.

Requirements: A investigar

Propone: DavidLitvak, fisa, GiLgAmEzH

Resultado
.........

Hicimos fork del proyecto bandersnatch:
https://bitbucket.org/fisadev/bandersnatch-pycamp2017

Incorporamos la opción de hacer la descarga inicial de solo una lista de paquetes.
Porque bandersnatch se trae todo Pypi, incluídas versiones viejas de paquetes grandes, y
paquetes que nadie usa. La lista tiene un formato parecido a requirements.txt, con lo que
se puede restringir las versiones a descargar de los paquetes.

También incorporamos el cacheo de los paquetes a demanda. Con lo que si un usuario del proxy hace pip install
de un paquete no descargado (no en la lista inicial), se descarga y queda listo para el resto de los usuarios.

Moravec: Como encarar un proyecto ya realizado
----------------------------------------------

El proyecto se llama Moravec, es de la gente de ElGatoYLaCaja y el backend se encuentra en Python.
Para ver detalles del proyecto: https://elgatoylacaja.com.ar/moravec/ .
Código fuente: https://github.com/elgatoylacaja/Dennett.
Una de las razones de porque me uní al evento, es poder aprender lo suficiente para poder darles una mano a la gente que esta atrás de este proyecto, en especial a Jorge que lo esta haciendo de manera voluntaria.

Requirements: No tengo conocimientos de Python como para determinarlo, pero si alguien puede, le podría dar una mirada y ver que tan complejo es.

Propone: Mario


LabJM: Laboratorio online
-----------------------------------------------
La idea es automatizar procesos de cargado de resultados de análisis en un laboratorio bioquímico.

En principio está pensado para realizarse en django. Su complejidad no es para nada elevada.

Propone: agucurto


Recordium
---------

Recordium es una aplicación simple que ayuda que cuando estés alejado de la compu puedas recordarle cosa a tu futuro vos que va a estar en la compu.

Más data en `el proyecto <https://github.com/facundobatista/recordium>`_. Ver también allí cómo instalar las dependencias necesarias.

Mi idea es cerrar un par de (los pocos) issues que tiene el proyecto, que está casi casi "feature complete".

Propone: FacundoBatista


Linkode, el pastebin útil
-------------------------

La idea es ofrecer un "espacio de colaboración de corta vida".  Algo así como un pastebin dinámico, pero que al mismo tiempo sea fácil de usar.

¿Por qué usar Linkode?

* Se puede usar anonimamente...

* ...pero recuerda quien sos

* Permite compartir un texto en pocos clicks

* Se da cuenta del lenguaje

* Es amigable a nivel de interfaz

* Copia el texto directamente a tu clipboard

* Se puede integrar el texto en donde quieras, por versión o siempre actualizado!

El `servicio ya está online <http://linkode.org>`_. El `proyecto está acá <https://github.com/facundobatista/kilink>`_

Propone: FacundoBatista

EasyCamp - Analisis Funcional
-----------------------------


Ideemos una App de Django que nos ayude a organizar un PyCamp. La idea es hacer un relevamiento, ver que debería hacer la app (features) y cómo podemos hacerlo.

* Encuesta asado
* Qué datos pedimos? (formulario con datos obligatorios)
* Habitaciones
* Carpooling

Posibilidad de fusionarse/mezclarse/tocarse con la valijita del PyCamp

Proponen: MatiBarriento, LuriSilva

Juego de aventura gráfica con Pilas engine
------------------------------------------

Una capa encima de Pilas para definir personajes, habitaciones, diálogos, puzzles.

Propone: manuq

Discusión: encajonar apps de escritorio en linux, para qué y cómo
-----------------------------------------------------------------

Quien haya intentado distribuir una aplicación en linux sabrá lo jodido que es. Y los bugs que se reportan por diferencias entre distros, usuarios corriendo la app con dependencias en distintas versiones, etc.  Hay una movida (o dos) de mejorar esta situación, basada en containers.  La idea es discutirla(s).  Yo conozco Flatpak, si alguien conoce Snappy podríamos compararlas.

Propone: manuq

ChopPycamp:
-----------

Programar un juego donde un bot tiene que juntar cervezas.

propone: fisa

Verano/12 Epub
---------------

Compilar cuentos de Verano/12

Estuvimos trabajando, usando Scrapy para bajar obtener el contenido de los cuentos.

Luego con Jinja2 generamos un documento reStructuredText, y usamos la aplicación rst2epub2 para obtener el epub

Aca está el `repo <https://github.com/dmascialino/cuentos_verano12>`_

Propone: diegom.

Recopilador de programas de radio:
----------------------------------

Recopilar de internet programas de radio y tenerlos disponibles en una interfaz para escucharlos.

Una idea era publicarlo en un canal de Telegram, pero charlando con varios, decidimos estudiar los podcasts.
Estuvimos usando: `feedgen <https://github.com/lkiesow/python-feedgen>`_ para generar el podcast.

Tambien vimos http://podsync.net/ , queremos hacer algo parecido pero que se extraiga solo el audio.

Propone: diegom.

Jugar con RaspberryPi zero W:
-----------------------------

Jugar con una raspi Zero W.

Propone: dlitvak.

NNVisualizer:
-------------

Una lib para importar redes neuronales y visualizarlas en un notebook.

propone: rossanigo.

PyCampVotingManager:
--------------------

Una app para votar proyectos en un pycamp y asignarle slots.

propone: zoe

Template: Otro proyecto o software o actividad
----------------------------------------------

Como se llama, que hace?, en que beneficiaria? porque esta bueno?

Requirements: <Que estaría bueno tener instalado antes del evento>

Propone: <Quien propone la idea o empuja el proyecto>

