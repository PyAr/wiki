#format rst

Como compilar python
====================

Acá hay una breve explicación para compilar python desde su código fuente

Compilando Py3k
---------------

Para compilar primero tenemos descargar las fuentes desde el repositorio, para eso debemos tener un cliente de subversion ("sudo aptitude install subversion" en linux basados en debian)

el comando que hay que correr es el siguiente

::

   .. raw:: html
      <span class="line">svn co http://svn.python.org/projects/python/branches/py3k/
      </span>

luego debemos tener instalados los archivos de desarrollo para poder tener habilitados algunos modulos de python, si no los instalamos, esos modulos no van a estar disponibles.

la lista con los nombres en linux basados en debian es:

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

luego de instalar todas las librerías debemos correr los siguientes comandos

::

   .. raw:: html
      <span class="line"><span class="go">cd py3k</span>
      </span><span class="line"><span class="go">./configure</span>
      </span><span class="line"><span class="go">make</span>
      </span><span class="line"><span class="go">sudo make install</span>
      </span>

si todo salio en orden, ahora podemos usar python 3.

podemos probar corriendo el comando python3.0 en la consola

::

   .. raw:: html
      <span class="line"><span class="go">mariano@mousehouse:~/Software/py3k$ python3.0</span>
      </span><span class="line"><span class="go">Python 3.0rc1+ (py3k:66685, Sep 29 2008, 17:25:48) </span>
      </span><span class="line"><span class="go">[GCC 4.2.3 (Ubuntu 4.2.3-2ubuntu7)] on linux2</span>
      </span><span class="line"><span class="go">Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span>
      </span>

cada vez que queramos actualizar al código mas nuevo en el repositorio, debemos hacer lo siguiente

::

   .. raw:: html
      <span class="line"><span class="go">cd py3k</span>
      </span><span class="line"><span class="go">svn up</span>
      </span><span class="line"><span class="go">make</span>
      </span><span class="line"><span class="go">sudo make install</span>
      </span>

Como armar un paquete DEB de Python
===================================

A veces es necesario armar un paquete para facilitar la instalación/desinstalación y pruebas en distintas máquinas.

Aquí un ejemplo de como hacerlo para Debian o Ubuntu (bajando py3k):

Bajamos y descomprimimos (en este caso, por SVN):

::

   .. raw:: html
      <span class="line"><span class="go">svn co http://svn.python.org/projects/python/branches/py3k py3k</span>
      </span><span class="line"><span class="go">cd py3k</span>
      </span>

Configuramos y armamos el paquete:

::

   .. raw:: html
      <span class="line">./configure --prefix<span class="o">=</span><span class="nv">$HOME</span>
      </span><span class="line">cat <span class="s">&lt;&lt; EOF &gt; description-pak</span>
      </span><span class="line"><span class="s">Python 3.x provisional test package</span>
      </span><span class="line"><span class="s">EOF</span>
      </span><span class="line">checkinstall -y --pkgname<span class="o">=</span>py3k --pkglicense<span class="o">=</span>PL <span class="se">\</span>
      </span><span class="line">             --maintainer<span class="o">=</span>reingart@example.com <span class="se">\</span>
      </span><span class="line">             --requires<span class="o">=</span> <span class="se">\</span>
      </span><span class="line">             --provides<span class="o">=</span>py3k --pkgrelease<span class="o">=</span>1 <span class="se">\</span>
      </span><span class="line">             --pkgsource<span class="o">=</span>http://www.python.org/download/ <span class="se">\</span>
      </span><span class="line">             --install<span class="o">=</span>no --reset-uids<span class="o">=</span>yes <span class="se">\</span>
      </span><span class="line">             -D make install
      </span>

Luego, instalamos el paquete con:

::

   .. raw:: html
      <span class="line"><span class="go">dpkg -i py3k-1_i386.deb</span>
      </span>

