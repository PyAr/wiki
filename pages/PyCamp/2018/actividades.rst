¿Buscando inspiración? Fijate también la página de `Ideas para programar`_

Uso de Eventol en PyAr y mejoras para el sistema
------------------------------------------------
Eventol es un proyecto libre que busca facilitar la administración y difusión de eventos relacionados con el software libre.
Ya tiene varios años de desarrollo, esta hecho en Django (con python3), se viene usando en FLISoL a nivel nacional hace 4 años y actualmente contamos con el apoyo de USLA para la infraestructura.
La idea principal es plantearlo como remplazo a las plataformas pagas para las distintas comunidades relacionadas con el software libre.
La propuesta para la pycamp es plantear su uso para los eventos de PyAr y agregarle las funcionalidades que le falten para ese fin.

Les dejo un par de links:

Github: https://github.com/eventoL/eventoL

Documentación: http://eventol.github.io/eventoL/#/

Instancia actual en USLA: https://eventol.flisol.org.ar/

Propone: FedeG


Un bot para telegram 
---------------------------------------------
Estuve laburando bastante para un bot de telegram que facilita un montón de cosas. Quizás podemos hacer uno para 
comunicar el canal de irc con el canal de telegram, que avise de eventos, que guarde un log de lo que se habla,
en fin muchas cosas que se pueden pensar. Si quieren ir viendo un poco del código de mi bot: https://github.com/eduzen/bot
 
Estaría bueno que ya vengan con python 3.6 instalado y un venv con python-telegram-bot

Propone: eduzen

Web PyAr
--------

Propongo trabajar en issues y features del sitio de PyAr.

Requirements: lo que haga falta para poner en marcha https://github.com/PyAr/pyarweb

Propone: Litox


fades
-----

Fixear algún bug o meter algún feature en fades (fades is a system that automatically handles the virtualenvs in the cases normally found when writing scripts and simple programs, and even helps to administer big projects).

El proyecto está `acá <https://github.com/PyAr/fades/>`_.

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



¿Chau lista de correo?
----------------------

Tenemos que hablar sobre la evolución de uno de las principales formas de comunicación dentro de PyAr. ¿Se quedó en el tiempo? ¿Sigue sirviendo? ¿Buscamos una solución nueva? ¿Mixta? ¿Qué queremos?

Propone: FacundoBatista

Mejorar Python
--------------
Podríamos invertir parte del tiempo en mejorar Python de las siguientes formas:

* Testeando las nuevas features de 3.7
* Resolviendo bugs reportados
* Incrementando el test coverage
* Mejorando documentación
* Implementando features con +1 en bugs.python.org.

Propone: Andrés Delfino

Administración AC
------------------

Hemos crecido bastante y tenemos varias opciones de pago y registro de socios.
La tarea manual es muy tediosa y nos atrasa bastante el laburo. Habría que hacer
que al menos los pagos recibidos por TodoPago y MercadoPago se imputen directamente
en la gDocs que tenemos o buscar alguna alternativa para que la gestión sea más simple.

Propone: LeCoVi (aka Leo Colombo Viña)

Front, the assistant bot
------------------------
A bot you talk to to add reminders, bookmark pages, things you need to search for later, movies you want to see, etc.

v0: records everything you say
v1: lets you tag stuff for easier searching, maybe add notifications
vN: a social del.icio.us like global repository of hand encoded bits of information that can do stuff for you

Propone: Lucio Torre

Direct Manipulation Collaborative Dataflow Notebooks
----------------------------------------------------

Hacer un website como si fuese un excel, hacer un notebook de python compartiendo en realtime el desarrollo, 
todo se recalcula cuando cambia un dato, y es una api REST::

        )
       (   
  -=====#


Propone: Lucio Torre


Escrutinio provisorio paralelo
------------------------------

La idea me surgió el año pasado, con las demoras que llevó la carga de telegramas en BA y cómo esas ineficiencias del sistema electoral actual se usan para impulsar el voto electrónico, con el que no estoy de acuerdo.

Hacer un programa que lea las actas electorales de conteo, a partir de fotos que podrían sacar los fiscales en las mesas de votación.

Según lo que estuve investigando y probando un poco, sería posible hacerlo combinando procesamiento de imágenes y algo de deep learning.

Utilizando OpenCV (o alguna otra librería) habría que detectar la grilla y aislar las celdas donde se escriben los números. Luego dada una celda habría que separar en dígitos y finalmente reconocer los dígitos con deeplearning (ya está hecho en https://github.com/JoelKronander/TensorFlask usando base MNIST).

Adicionalmente se podría laburar en el bot Telegram o alguna otra plataforma que reciba la data de los fiscales y en alguna interfaz de corrección colaborativa.

Llevo set de datos de 1000 actas electorales.

Propone: Guillo Narvaja


Mejorar la sección PyCamp de la Wiki.
-------------------------------------

Como todos sabemos (o están por saber) el PyCamp es genial!

Leyendo la wiki noté que por ahi no se termina de reflejar al 100% QUE es un PyCamp y  COMO se desarrolla. 
Además, la sección “Organizando un PyCamp” está vacía. Propongo ampliar la descripción, incluso hasta 
hacer un video! Y tratar de rescatar lo que había en “organizando un PyCamp” o volver a escribirlo actualizado.

Se podria hacer el último dia y pedir a las personas que vienen por primera vez que traten de contar 
su experiencia y cuan diferente fué de lo que se imaginaron.

Propone: Luri Silva


Eventes!
--------

Una django-app para pyarweb pensada primero desde la diversidad. 

Make pyar chat great again
--------------------------

La gente nueva esta usando Telegram. Pero los elders estan en el IRC. Hagamos un bridge irc<->telegram 

PyAr Infra as code
------------------

Estamos laburando con Tomás con traer la infra de PyAr a este siglo. (deploy automatizado, containers, hosting agnostico)

Sateye
------

Un proyecto arrancado pero que aún no está funcional, buscando reemplazar un grupo de herramientas bastante anticuadas y/o propietarias, para visualización y seguimiento de órbitas de satélites.

Hay bastante para hacer. Parte de la UI está avanzada, y el server que la levanta y va a exponer la data que la web app necesita. También parte de la visualización, usando Cesium para el globo terraqueo/mapa.
Falta generar la propagación de órbitas, plotearlas arriba del globo, administración de abms (satélites, estaciones terrenas, etc).

.. image:: https://i.imgur.com/bAcnBgC.png
   :height: 120px

Propone: fisa

Un Teclado para Ppysenteishon
-----------------------------

Pysenteishon te permite hoy controlar tus slides desde el celular de forma re simple. Pero a mi me gustaría que tenga otra cosa más: un touchpad y teclado, para poder usarlo por ejemplo para ver series tirado en un sillón.
Se le podría agregar un modo "pad y mouse", y pareciera que no es tan complicado.

Propone: fisa, pero no me hago cargo porque seguro voy a estar más con Sateye. Tiro la idea por si a alguien le interesa tomarla!

Pelear con espadas!
-------------------

Podemos aprender un poco las bases de artes marciales históricas europeas (específicamente, espada de dos manos), practicar, y pelear :)

.. image:: https://i.imgur.com/05g7DUW.jpg
   :height: 100px
   
Propone: fisa

UManoCOMPu
----------

Explorar, investigar, creanear e implementar ideas de formas no convencionales de interacción 
persona-computadora.

Ejemplos: 

* Joystick Vocal, en un juego de autos bajas los cambios haciendo el sonido del rebaje, etc
* Usar los acelerómetros del celu como input para una computadora

Propone: SAn

Juegos con micropython
----------------------

Traje varias placas que corren micropython, y algo de electrónica para conectarles. Quiero hacer una biblioteca que sea fácil de usar como PyGame para juegos electromecánicos, y algún juego usando eso.

Propone: alecu

Un bot que juegue Super Hexagon
-------------------------------

Hace muchos años que juego ese juego y nunca lo pude ganar. Me gustaría que al menos mi maquina lo haga, y en el camino poder aprender algunos rudimentos sobre computer visión. 

Propone: alecu

