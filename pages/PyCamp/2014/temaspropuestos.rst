
Temas propuestos para el PyCamp 2014
------------------------------------

Estas son propuestas, en el PyCamp_ el primer día se hace una votación para elegir a cuáles de estos proyectos o ideas vamos a dedicar tiempo (este procedimiento lo tenemos que terminar de definir).

Linkode, el pastebin útil
~~~~~~~~~~~~~~~~~~~~~~~~~

La idea es ofrecer un "espacio de colaboración de corta vida".  Algo así como un pastebin dinámico, pero que al mismo tiempo sea fácil de usar.

¿Por qué usar Linkode?

* Se puede usar anonimamente...

* ...pero recuerda quien sos

* Permite compartir un texto en pocos clicks

* Se da cuenta del lenguaje

* Es amigable a nivel de interfaz

* Copia el texto directamente a tu clipboard

* Se puede integrar el texto en donde quieras, por versión o siempre actualizado!

Más info en `este post`_. El `servicio ya está online`_.

*Propone:* FacundoBatista_

Encuentro
~~~~~~~~~

Este_ es un simple programa que permite buscar, descargar y ver contenido del canal Encuentro, Paka Paka, BACUA, Educ.ar y otros.

*Propone:* FacundoBatista_

NINJA-IDE
~~~~~~~~~

NINJA-IDE_ es un Entorno de Desarrollo Integrado hecho en Python y para Python. El PyCamp_ pasado se comenzó una reescritura de todo el IDE para implementar una nueva arquitectura, esa nueva arquitectura ya se encuentra instalada en el IDE, y ha traído muchas mejoras de performance y facilidad a la hora de incorporar nuevas features o hacer que las actuales sean mas extensibles.

En este PyCamp_ pensamos estar trabajando en algunas de las nuevas features y dejar funcionando el soporte de Plugins acorde a la nueva arquitectura que facilita mucho el desarrollo y da mas opciones. Aquellos interesados en desarrollar plugins o features mismas del IDE pueden participar y aprender en simultaneo ambas cosas ya que la API utilizada para ambas tareas es la misma.

*Propone:* DiegoSarmentero_

CodeTranslator
~~~~~~~~~~~~~~

CodeTranslator_ es una simple aplicación que busca permitir la traducción de código fuente o APIs de una librería para que la misma pueda ser utilizada en distintos idiomas (Español, Ingles, etc). La idea surge principalmente basada en Pilas, cuya API es en español, pero es una gran herramienta de enseñanza para programar que podría ser utilizada por distintas personas que hablen distintos idiomas, y la idea de esta aplicación es poder permitir eso.

Pequeña demo muy básica: http://youtu.be/wKxqTgC8Z7Q

*Propone:* DiegoSarmentero_

PyConference
~~~~~~~~~~~~

PyConference_ es una aplicación para administración de eventos. Si bien está pensada para tener features generales que puedan aplicarse a (casi) cualquier meetup, conferencia, hackaton, etc., surgió como una iniciativa para facilitar la creación y administración de eventos de PyAr_ (PyDay_, PyConAr_, etc.), ofreciendo hosting gratuito, personalización de estilos fácil de usar, sistema de votación de charlas para los organizadores, perfil y administrador de charlas para disertantes, entre otras.

*Propone: Filly*

Mint for argentina
~~~~~~~~~~~~~~~~~~

https://www.mint.com/ es una aplicación de contabilidad personal, el feature mas interesante es que se conecta con tu cuenta de banco y puede analizar tus gastos para recomendarte formas de ahorrar mas. Por ahora es imposible atarse a la cuenta de banco pero la idea es hackear una aplicación como mint que ¿lea tu resumen de cuenta? y pueda ayudarte a gastar menos (o al menos que diga en que gastas mucho). Es un proyecto que tengo en la cabeza hace un tiempo y quizás a alguien mas le interesa.

*Propone:* SebastianAlvarez_

Preciosa, Precios de Argentina
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preciosa_ es una plataforma web con clientes para teléfonos móviles que funciona como una base de datos colaborativa (actualizable por los usuarios) para relevar precios de productos de supermercados. Con esa información es posible informar a los consumidores dónde se consigue el mejor precio de un producto, las mejores ofertas (relativas al precio promedio en la ciudad) en un comercio particular, y muchas más. Hay muchas tareas_ para realizar que implican desde scrapping de datos, geolocalización y cálculos estadísticos hasta la implementación de MVC en la aplicación HTML5 para móviles.

*Propone:* MartinGaitan_

Muerte a Moin Moin // django-waliki ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Semanas antes del PyCamp_ se organizó un grupo espontáneo encabezado por Emiliano para renovar el `sitio web`_ de Python Argentina. Hasta ahora, los alcances de esa renovación no incluyen modificar el sistema actual (esta wiki!) sino *complementarlo* con distintas "apps" de Django y un nuevo diseño gráfico para la portada.

El *engine* wiki con el que funciona el sitio actual es MoinMoin_, que, además de tener una apareciencia por  default bastante fea (un poco suavizada por la customización del encabezado) tiene un *markup* ad hoc bastante complicado, muy baja usabilidad, código fuente complejo y documentación escasa.

Propongo **migrar** la wiki actual a una aplicación wiki basada en Django, integrada al *look & feel* del nuevo sitio y motorizada por el mismo framework. Esto incluye: a) usuarios b) estructura de URL y contenido de todas las páginas (preferentente convirtiendo markup) c) historial de modificaciones de todas las páginas d) multimedia y otros contenidos

La aplicación wiki "pluggable" pada Django más desarrollada y mantenida es Django-wiki_ que utiliza el markup Markdown y persiste el contenido (y las revisiones) de la base de datos. Una alternativa es evaluar el desarrollo de una app ad hoc para Django inspirada en Waliki_, que mantenga el contenido en formato de archivos y utilice como sistema de control de cambios Git

*Propone:* MartinGaitan_

En la búsqueda del testrunner soñado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Propuse una lista de características que debería tener un test runner ideal; la idea es discutir eso, ver si hay que cambiar algo, y trabajar para lograrlo (no haciendo algo desde cero, sino muy probablemente realizando modificaciones o armando un plugin a algo que ya exista).

La lista de características y más explicación del tema, `en mi blog`_.

*Propone:* FacundoBatista_

Charla + actividad grupal: Key signing party
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes del PyCamp:
:::::::::::::::::

* Crear tu keypair, usar los algoritmo RSA y SHA2, se sugiere usar un tamaño de 4096 bits

* Imprimir varias etiquetas conteniendo información sobre tu keypair. Por ejemplo, múltlples copias por página de la salida del siguiente comando

::

   gpg -v --fingerprint <ID de tu keypair>

o usando la utilidad gpg-key2ps del paquete *signing-party* (Debian/Ubuntu)

* llevar al PyCamp_ algun identificación: DNI, DU, pasaporte, tarjeta verde. Un documento en el cual se vea tu nombre y tu foto.

Durante y depués de la keysigning party:
::::::::::::::::::::::::::::::::::::::::

Ver el material enlazado mas abajo.

Ver:

* http://keyring.debian.org/creating-key.html

* http://ekaia.org/blog/2009/05/10/creating-new-gpgkey/

* https://wiki.debian.org/Keysigning

* http://pgp-tools.alioth.debian.org/

* https://help.ubuntu.com/community/GnuPrivacyGuardHowto

*Propone:* RamiroMorales_

Clínica de migración a Py3k
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La idea es migrar código a Python 3.

Puede ser un proyecto que tengas y quieras migrar, o una biblioteca que necesites y que haya que migrar, o incluso una biblioteca que sepamos que hay que migrar...

No importa qué, el tema es migrar código, y hacerlo entre varios así aprendemos y nos sacamos las dudas en el momento.

*Propone:* FacundoBatista_

Granjita de robots twitteros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alguna vez quisiste tener 20mil seguidores en twitter y que todos tus chistes sean trending topic?

*Propone:* LucioTorre_

FlapPy Bot
~~~~~~~~~~

La idea sería armar un robot que pueda jugar al flappy bird (o alguna de sus numerosas copias). Algo parecido a `ésto`_. Según dicen lo armaron en sólo 4 días (son chinos, va a estar difícil, pero hay que ganarles). Yo tengo para poner tablet, disco (es muuy viejo), webcam (no graba con la re calidad), trípode.

*Propone:* FedericoMie_

pbt - Python Building Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una charla relampago en la ultima Pycon MarianoGuerra_ propuso implementar una herramienta que colabore en simplificar el desarrollo en python. Despues de varios vinos en el asado final se propuso construir pbt(Se lee pebete) se armo un repo, y mariano construyo un esqueleto que es este_ la idea de trabajarlo en la pycamp es darle funcionalidades basicas como para tener una version "usable" del mismo.

*Propone:* JairoTrad_

Traducción del video: Inventing on Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Motivación:**

Bret Victor dio una charla impresionante dirigida a programadores y artistas. Por suerte esa charla está filmada con buena calidad y subtítulos "srt" en inglés.

* http://vimeo.com/36579366

**Propuesta:**

Mi intensión es que podamos dedicar unas horas a traducir los subtítulos de la charla. Pienso que así podemos compartir con muchos programadores de habla hispana las ideas de Bret y que se puedan inspirar con tremenda charla.

*Propone:* HugoRuscitti_

Hacer la aplicación ciclo-fondos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Motivación:**

Quisiera crear una aplicación que cambie automáticamente los fondos de pantalla del escritorio, digamos cada 30 minutos.

La aplicación que podríamos tomar de inspiración es "simpledesktop":

* http://simpledesktops.com/app/mac/

**Propuesta:**

La idea es hacer una app que coloque un ícono en el systray del sistema con un temporizador. Esa app podría hablar con un webservice que tenga un grupo grande de fondos de pantalla (¿scrapeados de algún lado?). Ese webservice también lo podríamos crear nosotros, me lo imagino como una API rest 🙂

*Propone:* HugoRuscitti_

Experimentar con Live-coding y programación reactiva
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Motivación:**

Siguiendo con las ideas de Bret, quisiera implementar live-coding en pilas-engine: Que los chicos puedan visualizar el código completo de un juego y hacer cambios en vivo, visualizando inmediatamente el resultado del cambio.

Algo así:

* https://s3.amazonaws.com/worrydream.com/LearnableProgramming/Movies/Vocab13.mp4

* http://worrydream.com/LearnableProgramming/

Pero me doy cuenta que es bien difícil y no encuentro la solución al enigma, siento que si lo conversamos en equipo y codeamos unos prototipos podemos encontrarle la vuelta.

**Propuesta:**

Investigar y charlar sobre instrumentación de código (bah, creo que viene por el lado de instrumentación, no se...). También leer un poco sobre algunas apps que lo implementan, como el editor brackets y google-chrome (que podrían darnos la posta sobre el tema) y hacer algún prototipo sobre pilas, pygame o cualquier otra cosa ...

*Propone:* HugoRuscitti_

Procesamiento distribuido en múltiples GPUses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La idea es hacer una librería que abstraiga el procesamiento distribuido de varios streams de datos. Esta será la base de cualquier modelo que corra en el mini cluster del GERSolar (Grupo de Estudio de la Radiación Solar). En una primera instancia el mini cluster contará con un par de GPUs (OpenCL) distribuidas en algunos nodos. factopy_ es el repo donde hice algún bosquejo.

* Rediseñar/Diseñar/Pulir y/o implementar la parte del backend (tal vez utilizar Pyro4_).

* Aunque se encuentre enfocada en el mini cluster, estaría bueno que posea la flexibilidad suficiente para poder ser utilizada por un mini cluster de raspberrypies.

Propone: EloyColell_

Descarga de imágenes satelitales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La intención es automatizar la descarga de imágenes satelitales del satélite GOES-13 desde el `sitio web del NOAA (National Oceanic and Atmospheric Administration)`_. El repositorio se llama solar_radiation_model_.

* Adaptar la automatización de la descarga desde el NOAA para que se realice utilizando factopy_. Para realizar la descarga de la imágen satelital primero es necesario completar una solicitud en el sitio web, luego hay que esperar una notificación por correo electrónico, y luego recién proseguir con la descarga desde el servidor FTP.

* Estaría bueno que la descarga pueda realizarse con una raspberrypi + dísco externo.

Propone: EloyColell_

Competencia de algoritmos para 2048
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se me ocurre hacer un competencia alrededor del juego 2048_ y ver quien puede hacer:

* El que lo resuelva mas rapido (cpu y moves)

* El que lo resuelva con menos codigo

* La estrategia mas interesante

* etc?

Propone: Lucio Torre

Juego cooperativo de zombies por consola
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similar a challenges que tuvimos en pyconar y a juegos que jugamos en otros pycamps (spacecraft), llevo Zombsole, un juego cooperativo de zombies por consola.

Cada uno programa su bot, pero la idea es formar equipos y ganarle al juego en los varios modos cooperativos: escape, exterminio, refugio. Y si se juntan y programan sus bots de forma que se "entiendan" y complementen, mejor todavía! (hay mecanismos para que se comuniquen).

Un dato extra: usa Docker para aislar a los procesos de los jugadores, cosa de que no hagan trampas del tipo "con este hack los zombies no me atacan porque patcheo la lógica del mundo", etc. Si a alguien le interesa intentar romper eso, también está interesante, jeje.

El repo con una parte está acá: https://github.com/fisadev/zombsole

Pero me falta cerrarlo y poner un poco de doc. En estos días lo voy a estar terminando, aunque seguro van a aparecer ideas para mejorarlo mientras estemos en pycamp.

propone: fisa (JuanFisanotti_)

La maquina de hacer dinero :)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyalgotrade_ + bitcoin y ver que se aprende!

propone: LucioTorre_

WeFree la interné en el teléfono
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es una aplicacion para android y un servicio para compartir claves wifi y así conectarte a todos los AP's de la ciudad que quieras. La comunidad te conecta. (tambien conocido como el grán bypass a las telefónicas,  el roaming de la muerte, y otros)

propone: GeraRicharte_

Nueva web de PyAr
~~~~~~~~~~~~~~~~~

Web hecha con Django que va a ser el nuevo sitio de PyAr_, se trabajó en muchísimas partes y se avanzó en:

* Frontend, tenemos banner re bonito. Fix de colores / tamanios de letras y muchas cosas gráficas

* Aplicación de Jobs mejorada

* Aplicación de News mejorada

* Aplicación de Proyectos de PyAr_

* Aplicación de adoptar un newbie

* Aplicación de FAQs

* Mejora del cliente embebido de IRC

* Agregado de tags en app de jobs y news para filtrar

* Muchas cosas más que ahora se me escapen

Pilas
~~~~~

* Implementación de plugins para pilas

* Configurar pilas con archivo yaml

.. ############################################################################

.. _este post: http://www.taniquetil.com.ar/plog/post/1/608

.. _servicio ya está online: http://linkode.org

.. _Este: http://encuentro.taniquetil.com.ar/

.. _NINJA-IDE: http://ninja-ide.org/

.. _CodeTranslator: https://github.com/diegosarmentero/CodeTranslator/

.. _PyConference: https://github.com/PyConference/PyConference

.. _Preciosa:
.. _tareas: https://github.com/mgaitan/preciosa/

.. _sitio web: https://github.com/samuelbustamante/pyarweb

.. _MoinMoin: http://moinmo.in/

.. _Django-wiki: http://django-wiki.readthedocs.org

.. _Waliki: https://github.com/mgaitan/waliki/

.. _en mi blog: http://www.taniquetil.com.ar/plog/post/1/642

.. _ésto: https://www.youtube.com/watch?v=kHkMaWZFePI

.. _este: https://github.com/pebete/pbt

.. _factopy: https://github.com/ecolell/factopy

.. _Pyro4: http://pythonhosted.org/Pyro4/intro.html

.. _sitio web del NOAA (National Oceanic and Atmospheric Administration): http://www.nsof.class.noaa.gov/saa/products/search?datatype_family=GVAR_IMG

.. _solar_radiation_model: https://github.com/ecolell/solar_radiation_model

.. _2048: http://gabrielecirulli.github.io/2048/

.. _pyalgotrade: http://gbeced.github.io/pyalgotrade/

.. _diegosarmentero: /pages/diegosarmentero
.. _pyar: /pages/pyar
.. _pyday: /pages/pyday
.. _ramiromorales: /pages/ramiromorales
.. _luciotorre: /pages/luciotorre
.. _marianoguerra: /pages/marianoguerra
.. _hugoruscitti: /pages/hugoruscitti
.. _eloycolell: /pages/eloycolell
.. _pycamp: /pages/pycamp
.. _juanfisanotti: /pages/juanfisanotti
