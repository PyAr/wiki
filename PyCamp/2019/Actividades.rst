¿Buscando inspiración? Fijate también la página de `Ideas para programar`_

fades
-----

Fixear algún bug o meter algún feature en fades (fades is a system that automatically handles the virtualenvs in the cases normally found when writing scripts and simple programs, and even helps to administer big projects).

El proyecto está `acá <https://github.com/PyAr/fades/>`__.

Propone: FacundoBatista



Asoc Members
------------

Terminar de emprolijar algunas cosas del Sistema de Miembros de la Asociación Civil, y generar algunos listados y páginas para operar que estamos necesitando.

El proyecto está `acá <https://github.com/PyAr/asoc_members/>`__.

Propone: FacundoBatista

ESP32 - Micropython:
--------------------
.. image:: /wiki/PyCamp/2019/Actividades/attachment/activity.png

Hackear estos dispositivos, utilizando Micropython o su versión Loboris.

- El Proyecto (General): Hacer un framework MVC bajo MicroPython para configurar un ESP32 con propositos generales.

- Para Hackear (hardware): (2)ESP32, (2) Arduino, (1) Arduino Nano, Display touch con lector de tarjeta SD, Lector de Tarjeta SD, ESP-8266 con programador para armar, luces leds, Potenciometros, Display 16x2 I2C, Display 16x4 I2C, display de 7 segmentos 1 dígito, display de 7 segmentos 4 dígitos, relays etc...

- Material Bibliográfico: Programming with MicroPython (Nicholas H. Tollervey), MicroPython for ESP32 Development Workshop (Agus Kurniawan), Micropython for ESP32 Doc.

- Software: ampy, picocom (o terminal de puerto serie para conectarse con el esp)

Propone: @gsgerman

Intro a Python
--------------

Si hay personas nuevas en el lenguaje, me animo a dar una intro, adaptando al nivel que haga falta.

Propone: @fisadev

OpenLex
---------
Sistema para abogados y estudios jurídicos, hecho en web2py. Necesita una buena revisión, pasarlo a la versión nueva del framework, revisarlo, y quererlo un poquito

Más info ver `acá <https://github.com/marian-vignau/OpenLex/>`_ o bien unirse a `grupo Telegram <https://t.me/OpenLex_SL/>`_

Mirar resumen tutorial de las features en `video <https://youtu.be/GK1-XE2Nxdc/>`_

Propone: Marian

Sateye
------

Hace rato arranqué y después abandoné una aplicación para visualización de satélites y otras cosas en órbita.
Hay otras alternativas, pero todas me parecieron siempre re poco usables, por eso quería hacer algo mejor.
La idea es retomarla y sacar una primer versión andando publicable.

Propone: @fisadev

Espadas! (actividad recreativa)
-------------------------------

Llevo algunas espadas de práctica y equipo de protección, para el que quiera aprender cosas básicas de artes 
marciales históricas europeas (no se daban garrotasos a lo bruto, eso es verso de hollywood :p).

Propone: @fisadev

Grillo
------

Hoy hice Grillo, una herramienta que permite mandar datos de una máquina a otra re re fácil, usando micrófono 
y parlantes para transmitir y leer la data por audio. Tiene magias como esta:

.. code::

    maquina1> grillo listen
    maquina2> grillo clipboard

 
Y después de escuchar un ruido, máquina 1 tiene en su clipboard el contenido que tiene el clipboard de máquina 2.
Sirve para mandar textos y archivos también.

Peeeeeeeeeero, la lib que hace la comunicación por audio solo banca mandar mensajes de 32 bytes.
Durante el pycamp podríamos reemplazarla por otra que no se si es simple de usar, o pensar en algo que use 
muchos mensajes, coordinando la comunicación, etc.

Propone: @fisadev

Coding dojo rotativo rápido
---------------------------

Juego para divertirnos todos juntos mientras programamos algo sencillo. ¡No importa tu nivel de Python o programación! La idea es divertirse :)

Propone: FacundoBatista