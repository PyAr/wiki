Ejemplos del año pasado (2014) acá http://python.org.ar/wiki/PyCamp/2014/TemasPropuestos

Juegos, Realidad Virtual y otras cosas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El objetivo de esta actividad es tratar de armar algo utilizando Oculus, LeapMotion,
Kinect, Controles y patineta de Xbox, y cualquier cosa que pinte combinar para la idea
que se decida realizar junto a los interesados despues de algun brainstorming el primer
dia. Obviamente por los dispositivos a usar, el objetivo esta orientado a tratar de
crear algun juego o alguna experiencia particular. DISCLAIMER: No se va a usar Python,
sino C# utilizando el Engine de Unity3D. (Propone actividad: Gatox)

Tomador de notas grafico
~~~~~~~~~~~~~~~~~~~~~~~~

En general cuando tomo notas de algo (mayormente diseñando arquitecturas o planeando
roadmaps de features) tiendo a hacer grafos muy parecidos a mind maps, mi idea es hacer
un editor que me deje crear nodos, lineas, flechas y todo tipo de dato que se pueda
encodear en graficos con las menos palabras posibles. Voy a estar usando algun toolkit
graficoso porque no quiero widgets standard sino algo que este mas cerca de una hoja de
papel y una lapicera pero practico para el teclado. (Propone actividad: Perrito)

Redes Libres
~~~~~~~~~~~~
Simulador de redes mesh con protocolo BATMAN Adv.

https://github.com/dbritos/Network-mesh-emulator

Conocer y si es posible, colaborar con el proyecto de redes libres comunitarias.
(Propone actividad: Javier -> emperna a Nico Echaniz)

Tritcask
~~~~~~~~

Un key value store 100% python. Hay que hacerlo pip instalable, portar a python 3, hacer alguna doc, etcs...

https://github.com/verterok/tritcask

(propone: lucio)

SASI
~~~~~~~~
SASI es sigla de Sistema Autogestivo de Saneamiento Integral. 

Surge de un proyecto del que participo hace algún tiempo en conjunto con la Facultad de Ciencias Bioquimicas y Farmacéuticas 
de la Universidad Nacional de Rosario que consiste en hacer un relevamiento del acceso al agua potable en una villa de Rosario, Villa Banana [1].

La idea de hacer un sistema que permita gestionar las encuestas y las distintas actividades en el barrio y que además tenga la posibilidad de comunicarse con la gente del barrio, que en muchos casos no tiene posibilidades de hacerlo de forma directa. 
Con respecto a esto último una de las alternativas es un sistema que reciba smss mediante un modem gsm en un raspberry y los reporte al servidor. Esta parte está mas o menos avanzada.

Para los formularios de las encuestas podria utilizarse Open Data Kit [2]

Aparte de esto está la complicación de que el barrio no está mapeado, 
con lo cual también se estan haciendo actividades sobre mapeo comunitario y está la idea de georreferenciar las encuestas, ubicar centros de interés e ir incorporando todas las utilidades que tiene un GIS.

Aparte de esto me parece que es un proyecto que puede tener varias funcionalidades generales para cierto tipo de proyecto que requiera actividades en campo, encuestas y GIS. 
Se me ocurre que puede ser algo similar a Ushahidi [3], pero con otro objetivo, aunque con una dinámica similar.


[1] http://www.riepibito.com.ar

[2] https://opendatakit.org/

[3] http://www.ushahidi.com/

(propone: Bruno Geninatti)


SubHunter
~~~~~~~~~

App (cli y deskstop) para bajar subtitulos[0].Buscar en varios servers (wrappers), bajar uno de cada server para tener más de una opción.

Python 3.4, asyncio, UI no definida.

Usable en Touchandgo[1] (si touchandgo-devs quiere)

**Aprendiz friendly**

[0] https://github.com/matibarriento/subHunter

[1] https://github.com/touchandgo-devs/touchandgo

(propone: Matías Barriento)


Verificador de subtítulos
~~~~~~~~~~~~~~~~~~~~~~~~~

(empalmado con Sub Hunter ↑) La idea es verificar si un subtítulo matchea con el video... o mejor dicho, con el audio ;)  Lo básico es encontrar si en el momento del subtítulo hay alguien hablando, con eso uno ya se asegura que el subtítulo está sincronizado... [Propone: Facundo Batista]


Encuentro
~~~~~~~~~

Fixear algún bug o meter algún feature en `Encuentro <https://launchpad.net/encuentro>`_, que es un simple programa que permite buscar, descargar y ver contenido del canal Encuentro, Paka Paka, BACUA, Educ.ar y otros. [Propone: Facundo Batista]


fades
~~~~~

Fixear algún bug o meter algún feature en `fades <https://github.com/PyAr/fades>`_ (fades, "FAst DEpendencies for Scripts", is a system that automatically handles the virtualenvs in the simple cases normally found when writing scripts or simple programs). [Propone: Facundo Batista]


PyArWeb
~~~~~~~

Una manito para cerrar algunos de los 50~ issues que tenemos? en  `PyArWeb <https://github.com/PyAr/pyarweb>`_. La idea tambien es sumar personas via IRC así que estaría bueno hacerlo el Sábado o el Domingo [Propone: Ángel Velásquez]


Python Bug day
~~~~~~~~~~~~~~

La idea es trabajar un rato en Python en sí, cerrar algún bug del lenguaje propiamente dicho. Mucho código del lenguaje es en C, pero también hay mucho en Python mismo, y hay algunas cosas que son sencillas. [Propone: Facundo Batista]
