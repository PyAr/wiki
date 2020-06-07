.. title: Compilarpython

Acá hay una breve explicación para compilar python desde su código fuente

Compilando Py3k
---------------

Para compilar primero tenemos que descargar las fuentes desde el repositorio. Para eso, debemos tener un cliente de subversion ("sudo aptitude install subversion" en linux basados en debian)

el comando que hay que correr es el siguiente

.. code-block:: console

    svn co http://svn.python.org/projects/python/branches/py3k/


luego debemos tener instalados los archivos de desarrollo para poder tener habilitados algunos módulos de Python; si no los instalamos, esos módulos no van a estar disponibles.

La lista con los nombres en linux basados en debian es:

* build-essential

* libsqlite3-dev

* libssl-dev

* zlib1g-dev

* libncurses5-dev

* libreadline5-dev

* libbz2-dev

* libgdbm-dev

* tk8.4-dev

* libdb-dev

Luego de instalar todas las librerías debemos correr los siguientes comandos:

.. code-block:: console

    cd py3k
    ./configure
    make
    sudo make install


Si todo salió bien, ahora podemos usar python 3.

Podemos probar corriendo el comando python3.0 en la consola:

.. code-block:: console

    mariano@mousehouse:~/Software/py3k$ python3.0
    Python 3.0rc1+ (py3k:66685, Sep 29 2008, 17:25:48)
    [GCC 4.2.3 (Ubuntu 4.2.3-2ubuntu7)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


Cada vez que queramos actualizar al código más nuevo en el repositorio, debemos hacer lo siguiente:

.. code-block:: console

    cd py3k
    svn up
    make
    sudo make install


Cómo armar un paquete DEB de Python
===================================

A veces es necesario armar un paquete para facilitar la instalación/desinstalación y pruebas en distintas máquinas.

Aquí un ejemplo de cómo hacerlo para Debian o Ubuntu (bajando py3k):

Bajamos y descomprimimos (en este caso, por SVN):

.. code-block:: console

    svn co http://svn.python.org/projects/python/branches/py3k py3k
    cd py3k


Configuramos y armamos el paquete:

.. code-block:: console

    ./configure --prefix=$HOME
    cat << EOF > description-pak
    Python 3.x provisional test package
    EOF
    checkinstall -y --pkgname=py3k --pkglicense=PL \
                 --maintainer=reingart@example.com \
                 --requires= \
                 --provides=py3k --pkgrelease=1 \
                 --pkgsource=http://www.python.org/download/ \
                 --install=no --reset-uids=yes \
                 -D make install


Luego, instalamos el paquete con:

.. code-block:: console

    dpkg -i py3k-1_i386.deb

