.. title: Reunión 42 - 28 de Mayo de 2010 - Bar Dr Mason, Buenos Aires - 19:00


**Edición Pycentenario**

—¡Cuarenta y dos! —exclamó Loonquawl—. ¿Es eso todo lo que tienes que mostrar tras siete millones y medio de años de trabajo?

—Lo he comprobado muy minuciosamente —dijo el ordenador—, y ésa es casi definitivamente la respuesta. Creo que el problema, para ser sinceros, es que no habéis sabido nunca cuál es la pregunta.

  *"The Hitchhiker's Guide to the Galaxy", Douglas Adams*

Temario
~~~~~~~

* Conclusiones y comentarios sobre el `PyDay Rafaela 2010`_

* Propuesta de PyDay_ Buenos Aires 2010

* Internacionalización de Python (`traducción mensajes de excepción`_, ayuda incorporada y demás)

* Reservo slot para tema "off the record" (pero "on topic") [sb]

* *proponer más temas...*

Asistentes:
~~~~~~~~~~~

Por favor, si venís a la reunión, anotate en esta lista:

* MarianoReingart_

* TomasZulberti

* FacundoBatista_

* AlbertoPaparelli_?

* MarceloFernández

* JoaquinSorianello_ (Se me complico...)

* AngelVelasquez_?

* HugoRuscitti_?

* SebastianBassi_

* GabrielGenellina_ (ufa 😕 )

* DiegoMascialino

* FelipeLerena

* Roberto Alsina

* Pablo Zilani

* Matias Barrios (N)

* Felipe Batista (7 meses)

¿Dónde?
~~~~~~~

Aráoz 1199 (entre Av. Córdoba y Cabrera)

Reservamos el sótano del bar "Doctor Mason" de 19 a 22hs. Cuenta con Wi-Fi y pool.

Costo (opcional) aproximado por persona $30 para comer y tomar algo (modalidad "a la carta" individual)

.. raw:: html

  <iframe src="https://www.google.com/maps/d/embed?mid=1EPKMtOBA1Z5cLEE-keWo3267qwg&hl=en" width="640" height="480"></iframe>

Ver: `Doctor Mason`_

¿De qué se hablo?
~~~~~~~~~~~~~~~~~

Curso de Python en La Tribu

* La idea es dar cursos de Python en la tribu un día a la semana. Posiblemente empiece este año. La idea es dar un curso básico y avanzado en dos tracks el mismo día.

* ¿Es mejor enseñar python a programadores o a personas que no saben programar?

* Para los no programadores, habría que ver porque una persona así quiere aprender a programar. ¿En que trabajan?

* Estaría bueno enseñar algo practico (django, web2py, etc..) pero el problema es que estas cosas tienen muchos conceptos mas (sql, templates, etc..). La ventaja es que la web es algo que motiva a la persona a seguir el curso.

* La Tribu quiere hacer algo para la comunidad. No es para empresas.

PyDay_ Rafaela 2010

* Fue el sábado 08/05 en una universidad católica organizada por las personas de allá. En esa universidad hay dos materias en las que se usa Python

* Fueron 92 personas, y se quedaron todos hasta el final. La asistentes estuvieron muy interesados y los organizadores comentaron de volver a repetirlo el año que viene.

* Hay vídeos y las charlas también están subidas. Los vídeos: http://pydayrafaela.blip.tv/, y las charlas: http://www.pyday.com.ar/rafaela2010/

PyCon_ 2010

* Los slots para charlas son de 25 minutos, lo que permite hacer charlas especializadas (templates de django). Si la charla tiene que ser mas larga (introducción a python, django, web2py, etc...) se puede pedir un slot de una hora.

* Parece que en la facultad donde se organiza las aulas donde se dan las charlas están cerca y además, va a haber espacios abiertos para consultas.

* En los vídeos de PyDay_ Rafaela no se ven las diapositivas, asi que se hablo de que el disertante grabe su pantalla (gtkRecordMyDesktop) y el audio. Ver al disertante hablando no es tan importante como ver las diapositivas, y esto es algo que se puede hacer fácil.

PyDay_ Buenos Aires

* Surgió cuando la idea cuando estábamos volviendo del PyDay_ Raf. La idea es hacerla la primer semana de Septiembre, y de ser posible hacer 3 tracks: Básico, Talleres, Abierto (cosas de la comunidad: postgres, ubuntu) y avanzado.

* Se tiene un lugar, el Club de los Programadores en donde entran 60 personas en el aula mas grande. Tiene todo preparado también para los talleres. Hay que ver si se puede conseguir un lugar mas grande

* También surgió la idea de hacer un librito con diferentes tutoriales. Por ejemplo, meter el tutorial de django, web2py, wxPython, easy_install/virtualenv. Sin embargo, las hojas machete salen mucho mas barato, y la gente se los lleva.

* Falta conseguir sponsors. Tiene una lista de mails: ``pyday GUION baires EN googlegroups PUNTO com``

I18n Exceptions:

* La idea es internacionalizar los mensajes de excepciones que usa Python.

* Se mando una mail a python-ideas, y aunque tuvo un par de objeciones no hubo una que indique que no se puede hacer. En la wiki de pyar se escribió un borrador de un PEP.

* El problema con esto para los desarrolladores es cuando se reporta un bug, ya que el mensaje va puede estar en otro idioma que no sea el suyo (Chino). En postgres esto se soluciono metiéndole un código de error a cada mensaje. De todas formas, el programador puede saber que excepción fue lanzada ya que los mensajes los puede sacar el svn.

* Por default, debería leer el locale de la maquina.

.. ############################################################################

.. _PyDay Rafaela 2010: http://www.pyday.com.ar/rafaela2010

.. _traducción mensajes de excepción: /tracebackinternationalizationproposal

.. _Doctor Mason: http://www.doctormason.com.ar/

.. _pyday: /pyday
.. _marianoreingart: /marianoreingart
.. _albertopaparelli: /albertopaparelli
.. _joaquinsorianello: /joaquinsorianello
.. _angelvelasquez: /angelvelasquez
.. _hugoruscitti: /hugoruscitti
.. _sebastianbassi: /sebastianbassi
.. _gabrielgenellina: /gabrielgenellina
.. _facundobatista: /miembros/facundobatista
.. _pycon: /pycon
