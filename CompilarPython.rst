= Como compilar python =

Acá hay una breve explicación para compilar python desde su código fuente

== Compilando Py3k ==

Para compilar primero tenemos descargar las fuentes desde el repositorio, para eso debemos tener un cliente de subversion ("sudo aptitude install subversion" en linux basados en debian)

el comando que hay que correr es el siguiente

{{{
svn co http://svn.python.org/projects/python/branches/py3k/
}}}

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

{{{
cd py3k
./configure
make
sudo make install
}}}

si todo salio en orden, ahora podemos usar python 3.

podemos probar corriendo el comando python3.0 en la consola

{{{
mariano@mousehouse:~/Software/py3k$ python3.0
Python 3.0rc1+ (py3k:66685, Sep 29 2008, 17:25:48) 
[GCC 4.2.3 (Ubuntu 4.2.3-2ubuntu7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
}}}

cada vez que queramos actualizar al código mas nuevo en el repositorio, debemos hacer lo siguiente

{{{
cd py3k
svn up
make
sudo make install
}}}
