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


Digitalizador de tarjetas de presentación
-----------------------------------------

Fui a un evento de negocios y me vine con decenas de tarjetas personales. A todos ellos quedé en mandarles un folleto digital...

Quisiera sistematizar la extracción de datos de tarjetas personales. 
A partir de una foto de una tarjeta personal, extraer email, teléfono, nombre, puesto, etc.

Me parece lindo experimento para jugar con imágenes y texto (https://github.com/tesseract-ocr/tesseract).

Hay cosas que lo hacen, pero pagando:
http://www.enter.co/especiales/enterprise/cuatro-apps-para-dejar-de-coleccionar-tarjetas-de-presentacion/
https://www.merca20.com/3-apps-para-digitalizar-y-organizar-tarjetas-de-presentacion/

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