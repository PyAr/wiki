Este es el repositorio de los contenidos de la Wiki de Python Argentina

| http://wiki.python.org.ar/


Podés editar los contenidos (incluso agregar páginas) y proponer un pull request, que se
sincronizará automáticamente con la wiki una vez que sea mezclado.

Pueden ver como colaborar en la página de `Cómo colaborar
<https://wiki.python.org.ar/colaborandoenelwiki>`__

Cómo buildear las páginas
=========================

El contenido de la wiki está escrito en `Markdown <https://es.wikipedia.org/wiki/Markdown>`__ o `reStructeredText <https://es.wikipedia.org/wiki/ReStructuredText>`__ y se 
transforma a `HTML` con `nikola <https://getnikola.com/>`__, un generador de sitios estáticos escrito en python.

.. code-block:: console

    pip install -U pip
    pip install -r requirements.txt

    nikola build
    nikola serve
