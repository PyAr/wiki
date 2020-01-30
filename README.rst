Este es el repositorio de los contenidos de la Wiki de Python Argentina

| http://python.org.ar/wiki/

Podés editar los contenidos (incluso agregar páginas) y proponer un pull request, que se
sincronizará automáticamente con la wiki una vez que sea mezclado.

Antes de clonar el repo, asegurate de tener instalado [Git LFS][https://git-lfs.github.com/]

Como buildear las paginas
=========================

.. code-block:: console

    pip install nikola==8.0.2
    pip install Jinja2==2.10.1

    nikola build
    nikola serve
