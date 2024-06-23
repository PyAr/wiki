.. title: ¿Un qué?


Antes que nada, ¿qué es un PyCamp? `Acá tenés una buena descripción y mucha info </pycamp/>`_.


Fechas:
-------

24, 25, 26 y  27 de Marzo de 2017 (Viernes -feriado-, sábado, domingo y lunes).

WiFi
-----

ASL1@pyar y ASL2@pyar.
password: pycamp2017
Mirror pipy: http://192.168.42.250/index.html


Qué llevo (sección en construcción):
------------------------------------

 - Zapatillas, prolongadores, proyector, access points que puedas aportar, todo eso suma.

 - Tu computadora (mejor si es portatil). Actualizala con toda la información, paquetes y datos que creas que podrías necesitar, cosa de no exigirle a la internet del lugar más de lo necesario

 - La hostería **sí provee** Todo lo que tiene que ver con sábanas, frazadas, toallas, así que no nos tenemos que preocupar (aclaro porque hubo PyCamps donde no fue así)



Sede: Baradero, Buenos Aires
-----------------------------

**Nombre del lugar:** Hogar German Frers (datos + Fotos en el link)

http://www.habitatyerra.com.ar/

**Donde está:**

 * Mapa: http://osm.org/go/Mnfczj2hF--?m=

 * distancias:

  * 580km Córdoba Capital (8 horas en colectivo)

  * 150km de Rosario (4:30 Hs en colectivo, para en todos lados. Tambien hay algunas trafics que tardan 2 horas)

  * 150km de Capital Federal (2:30 en colectivo)


**Contacto:** Laureano Silva. `mandame un mail <mailto:laureano.bara@gmail.com>`_

**Formas de llegar: 5 pycampitas**

* En auto: Es cómodo llegar, las rutas están bien, está a 2 horas desde capital y desde Rosario.

* En colectivo:

  *  La única empresa es Chevallier. Desde Retiro salen como 12 colectivos diarios. Desde Rosario sólo 2.
  *  Desde Córdoba hay que hacer transbordo en Rosario (ahí aprovechan y compran alfajores santafesinos).

  * Costo aproximado:

    * Córdoba -> Rosario: ida $460-$520
    * Rosario -> Baradero: ida $170
    * Retiro -> Baradero: ida ~$150


**Precio:** $2500

* Incluye:

  * comidas: desayuno(3), almuerzo(4), cena(3). El asado esta fuera de este presupuesto, lo haremos a la vaquita en el PyCamp.

  * internet: Tienen un servicio de ARNET y uno de un WISP local. planean poner un tercero.

**Detalles extras del alojamiento:**

3 Habitaciones privadas con baño privado (1 base triple / 1 base cuadruple / 1 base quintuple ).
10 Habitaciones séptuples tienen baño a compartir c/duchas c/agua caliente las 24hs. Incluyen ropa
de cama + el libre uso (Pileta, canchas, SUM, WIFI).
Para reservar nos piden abonar el 50% del total del alojamiento tomando como base 20 pax,
por lo que tenemos que juntar $24500 al menos 30 dias antes del evento (23 de febrero).
Por otro lado, para congelar ya la tarifa, se necesitaria el 70% del total ($34300)


Inscripciones:
--------------

`Manda un mail <mailto:pycamp@python.org.ar>`_.


Organizadores:
------------------------

Laureano Silva.

Facundo Batista.

Cualquier duda, tema, o lo que quieras preguntar, `mandanos un mail <mailto:pycamp@python.org.ar>`_


Proyectos Propuestos:
------------------------

Se van cargando aquí `</PyCamp/2017/actividades>`_


IRC y Mirror PyPI:
------------------------



IRC
====

Conectate con cualquier cliente de irc al server en 192.168.1.100, canal #pycamp


Mirror PyPI
=============

Agregá esto al final de tu archivo ``/etc/hosts``:

.. code::

    192.168.1.100 pypi.pycamp


Y agregá esto en tu archivo ``/home/tuuser/.pip/pip.conf``:

.. code::

    [global]
    index-url = http://pypi.pycamp/simple
    trusted-host = pypi.pycamp


astá! ahora podés hacer pip install y va a volar (a la velocidad de una raspi y nuestro wifi)
