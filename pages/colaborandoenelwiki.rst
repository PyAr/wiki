.. title: Como colaborar en el Wiki de Pyar



.. contents::
    :local:

Introducción
------------

Existen varias maneras de contribuir con la wiki de Python Argentina:

- `reportando bugs <https://github.com/PyAr/wiki/issues>`__,
- revisando que esos bugs se encuentren vigentes,
- etc,


No importa como colaboran, siempre se tiene que seguir el `Codigo de
Conducta <https://ac.python.org.ar/#coc>`__

Reportanto Bugs
---------------

Cuando se reporte un bug, lo ideal sería que el mismo tenga:

- El link de donde se encuentra el error
- Una captura de pantalla de que es lo que está mal
- Un mensaje describiendo el error que se quiere cambiar


Proponiendo una mejora
----------------------

Hay dos formas de proponer mejoras:

- Hacer un cambio en una página puntual desde GitHub.
- Haciendo un Pull request

En cualquier caso, siempre es necesario que se creen una cuenta en
`GitHub <https://github.com/>`__

Sino saben mucho de reStructuredText, estos son algunos links que les pueden
ayudar:

- `Wikipedia reStructeredText <https://es.wikipedia.org/wiki/ReStructuredText>`__
- `rST Syntax <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`__
- `Create Documentation with RST, Sphinx, Sublime, and GitHub <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/>`__

Cambio puntual
++++++++++++++

Si estas viendo una pagina que esta mal, a la derecha del título
hay un link a Editar que los va a llevar al código fuente de todas
paginas


Una vez en la misma, pueden editarla desde el mismo Github,
y cuando commiten los cambios va a pedir crear un Pull request.

Cambios masivos
+++++++++++++++

Si tienen que hacer cambios masivos, por ahi usar la interfaz de
Github para editar todos los archivos es ineficiente.

En ese caso:

- Tienen que hacer un fork del proyecto
- Clonarse el fork
- Lean el README.rst para saber como configurar el entorno local
- Editar todos los cambios que crean necesarios
- Hacer un pull requests de su fork al proyecto oficial

Cosas a tener en cuenta
-----------------------

Cuando estas editando páginas rST, un par de cosas a tener en cuenta:

- Los archivos tienen que tener los nombres en minúscula y no tener tildes
  ni otros caracteres especiales
- Los archivos tienen que tener extensión ``.rst``
- Cuando tengan que poner una dirección de mail, no pongan la direccion del mail
  real, `foobar@example.com`, sino que usen palabras como `dot, at`. Por ejemplo:
  `foobar at example dot com`
