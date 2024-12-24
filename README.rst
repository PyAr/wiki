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

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1 # en PowerShell
    . .venv\bin\activate # en Bash

.. code-block:: console

    .venv> python -m pip install -U pip
    .venv> python -m pip install -r requirements.txt

.. code-block:: console

    .venv> nikola build
    .venv> nikola serve
