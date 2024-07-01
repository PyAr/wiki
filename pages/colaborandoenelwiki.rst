.. title: Cómo colaborar en el Wiki de Pyar



.. contents::
    :local:

Introducción
------------

Existen varias maneras de contribuir con la wiki de Python Argentina:

- `reportando bugs <https://github.com/PyAr/wiki/issues>`__
- revisando que esos bugs se encuentren vigentes
- etc


No importa como colaboran, siempre se tiene que seguir el `Código de
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
- Haciendo un Pull Request (PR)

En cualquier caso, siempre es necesario que se creen una cuenta en
`GitHub <https://github.com/>`_


Los contenidos de la wiki pueden ser escritos en `Markdown <https://es.wikipedia.org/wiki/Markdown>`__ o en `reStructeredText`.
`Markdown` es muy sencillo de aprender y utilizar pero tiene una sintaxis limitada a diferencia de `reStructeredText` que permite una mayor configurabilidad.

Si no saben mucho de reStructuredText, estos son algunos links que les pueden
ayudar:

- `Wikipedia reStructeredText <https://es.wikipedia.org/wiki/ReStructuredText>`__
- `rST Syntax <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`__
- `Create Documentation with RST, Sphinx, Sublime, and GitHub <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/>`__

Cambio puntual
++++++++++++++

Si estás viendo una página que está mal, a la derecha del título
hay un link a *Editar* que los va a llevar al código fuente de todas
páginas


Una vez en la misma, pueden editarla desde el mismo Github,
y cuando commiten los cambios va a pedir crear un PR.

Cambios masivos
+++++++++++++++

Si tienen que hacer cambios masivos, por ahí usar la interfaz de
Github para editar todos los archivos es ineficiente.

En ese caso:

- Tienen que hacer un fork del proyecto
- Clonarse el fork
- Lean el `README.rst <https://github.com/PyAr/wiki/blob/nikola/README.rst>`_ para saber como configurar el entorno local
- Editar todos los cambios que crean necesarios
- Hacer un PR de su fork al proyecto oficial

Cosas a tener en cuenta
-----------------------

Cuando estás editando páginas rST, un par de cosas a tener en cuenta:

- Los nombres de los archivos tienen estar en minúscula y no tener tildes
  ni otros caracteres especiales
- Los archivos tienen que tener extensión ``.rst``
- Cuando tengan que poner una dirección de mail, no pongan la dirección del mail
  real, `foobar@example.com`, sino que usen palabras como `dot, at`. Por ejemplo:
  `foobar at example dot com`
