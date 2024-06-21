Este es el repositorio de los contenidos de la Wiki de Python Argentina

| http://wiki.python.org.ar/

Podés editar los contenidos (incluso agregar páginas) y proponer un pull request, que se
sincronizará automáticamente con la wiki una vez que sea mezclado.

Antes de clonar el repo, asegurate de tener instalado [Git LFS](https://git-lfs.github.com/)

Pueden ver como colaborar en la página de `Cómo colaborar
<https://github.com/PyAr/wiki/blob/nikola/pages/colaborandoenelwiki.rst>`__

Cómo buildear las páginas
=========================

.. code-block:: console

    pip install -U pip
    pip install -r requirements.txt

    nikola build
    nikola serve

Cómo buildear la imagen de docker
=================================

.. code-block:: console

     docker build --no-cache --tag tzulberti/wiki -f Dockerfile .


Se necesita el `--no-cache` para que la parte de clonar el repo de la
wiki no use un cache sino que se haga todo el tiempo.

Infraestructura
=================================

[Nuestro repo de github](https://github.com/PyAr/pyar_infra)

Si encontras algún problema por favor [reportalo acá](https://github.com/PyAr/pyar_infra/issues)