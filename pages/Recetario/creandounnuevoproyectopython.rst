
Creando un nuevo proyecto Python
================================

Así que querés comenzar un nuevo proyecto usando Python? ¡Felicitaciones! ¿Querés que tenga la estructura recomendada para proyectos modernos? ¿queres que sea instalable fácilmente? ¿Querés que no se te arme lio de dependencias que colisionan con las de otros proyectos ? Bien, te propongo esta receta. 

Las herramientas
----------------

Virtualenv_ es una herramienta para aislar tu entorno de desarrollo python. Es muy pero muy útil para evitar conflictos entre las dependencias de tus distintos proyectos. 

virtualenvwrapper_ es un conjunto de extensiones que hacen la vida del usuario *virtualenv* aun más feliz, permitiendo crear y borrar entornos virtuales, asociarlos a un proyecto, automatizar tareas al activar o desactivar uno, etc. 

pip_ es la herramienta moderna, correcta y recomendada para administrar los paquetes python instalados en tu sistema/virtualenv. Es un reemplazo de *easy_install*

Distribute_ es la herramienta moderna y recomendada para distribuir tu paquete python. Es un fork de *setuptools* (que es, a su vez, una mejora sobre el módulo estándar *distutils*) 

Skeleton_ es una herramienta que define *plantillas* para iniciar proyecto, generando la estructura básica necesaria. Es similar a *PasteScript_* pero enfocado en esta tarea concreta, sin dependencias y compatible con Python 3.x 

La receta
---------

1. Instalá pip

::

       $ sudo curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

2. Instalá virtualenwrapper y skeleton

::

     $ sudo pip install virtualenwrapper
     $ sudo pip install git+git://github.com/stumitchell/skeleton.git#egg=skeleton

Notar que *skeleton* se está instalando desde un *fork* del proyecto original, que resuelve bugs de la versión original (aparentemente desmantenida)

3. Configurá virtualenvwrapper. 

::

     $ mkdir ~/.virtualenvs           # acá se van a guardar tus entornos virtuales
     $ mkdir ~/proyectos              # acá se van a guardar tus proyectos

Luego editá tu *~/.bashrc* agregando las siguientes líneas

::

  WORKON_HOME=$HOME/.virtualenvs
  PROJECT_HOME=$HOME/proyectos
  
  source /usr/local/bin/virtualenvwrapper.sh

y recargá tus cambios

::
  
  $ source ~/.bashrc

4. Inicializá tu proyecto. Por ejemplo el proyecto *zaraza*

::

  $ mkproject -t package zaraza

Se te solicitarán algunos datos (nombre del proyecto, autor, licencia, etc.) y ¡(casi) listo! Estarás trabajando en tu proyecto *zaraza*. Tu prompt se verá así: 

::

  (zaraza)tin@morocha:~/proyectos/zaraza$

¿Qué sucedió? Se creó un directorio *~/proyectos/zaraza* para tu proyecto, asociado a un virtualenv ubicado  en  *~/.virtualenvs /zaraza*.  skeleton automáticamente creó una estructura básica de paquete python  *~/proyectos/zaraza/src* incluyendo un *setup.py* basado en distribute. 

5. Instalá tu paquete en el virtualenv, para poder importarlo desde cualquier lado

::

  (zaraza) $ cd  ~/proyectos/zaraza/src
  (zaraza) $ pip install -e .

Esto agrega el directorio de desarrollo de tu proyecto al PYTHONPATH del virtualenv, de modo que puedes importar *zaraza* desde cualquier lado dentro del virtualenv (por ejemplo, cuando hagas una carpeta *src/test* al nivel de '/src/zaraza'

¿Y ahora?
---------

Cada vez que quieras trabajar en tu proyecto *zaraza* podes correr 

 

::

  $ workon zaraza

Para salir del virtualenv

 

::

  (zaraza) $ deactivate

Algunos tips más a modo de despedida
------------------------------------

Virtualenwrapper es totalmente hookeable y extensible. Esta receta propone usar *skeleton* (que funciona como plugin de `virtualenvwrapper.project`_)  para crear una estructura de paquete estándar básica, pero hay plugins para proyectos más específicos. Por ejemplo `virtualenwrapper.django`_

El comando usado en el paso 4 (*mkproject*) es un wrapper sobre el comando principal de virtualenvwrapper *mkvirtualenv*, que acepta muchos parámetros opcionales. Ejecutá *mkproject_help* o *mkvirtualenv --help* para saber más. 

Y ya sabés ...

http://python-distribute.org/pip_distribute.png

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Virtualenv: http://www.virtualenv.org

.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/

.. _pip: http://www.pip-installer.org

.. _Distribute: http://packages.python.org/distribute/

.. _Skeleton: https://github.com/stumitchell/skeleton

.. _virtualenvwrapper.project: http://www.doughellmann.com/projects/virtualenvwrapper.project/

.. _virtualenwrapper.django: http://www.doughellmann.com/projects/virtualenvwrapper.django/

.. _categoryrecetas: /pages/categoryrecetas.html
