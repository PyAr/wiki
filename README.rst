Este es el repositorio de los contenidos de la Wiki de Python Argentina

| http://wiki.python.org.ar/

Podés editar los contenidos (incluso agregar páginas) y proponer un pull request, que se
sincronizará automáticamente con la wiki una vez que sea mezclado.

Antes de clonar el repo, asegurate de tener instalado [Git LFS][https://git-lfs.github.com/]

Pueden ver como colaborar en la pagina de `Como colaborar
<https://github.com/PyAr/wiki/blob/nikola/pages/colaborandoenelwiki.rst>`__

Como buildear las paginas
=========================

.. code-block:: console

    pip install -U pip
    pip install -r requirements.txt

    nikola build
    nikola serve
