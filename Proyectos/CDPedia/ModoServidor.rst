
Correr CDPedia como Servidor
----------------------------

La CDPedia está preparada (desde su versión 0.8) para correr en modo servidor: la instalás en una máquina, y podés accederla desde muchas otras. 

¿Cómo se arma esto?

Si corres ``./cdpedia.py --help`` te muestra las opciones, pero básicamente hay 2 formas de montar un servidor. La más sencilla es utilizar el servidor web integrado con cdpedia y es la forma recomendada; la otra es usar un web server externo.

Usando el servidor integrado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Por ejemplo, para servir cdpedia en el puerto 80 en un hostname particular hacemos asi:

::

   sudo ./cdpedia.py --host=foo.bar.com.ar --port=80 --daemon

Obviamente el sudo es porque el 80 es un puerto privilegiado, sino directamente podemos poner lo siguiente para servir en una ip local y un puerto elevado.

::

   ./cdpedia.py --host=10.0.0.4 --port=8080 --daemon

Inclusive se puede configurar apache o el servidor que haya para que haga las veces de proxy reverso y asi servir todo en el 80.

Usando un server externo (Apache, nginx, etc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hay dos formas de hacer esto:

* proxy reverso (recomendado)

* WSGI

Proxy reverso
:::::::::::::

El servidor web externo o principal hace de proxy reverso hacia el servidor integrado de la cdpedia. 

cliente <-> apache <-> cdpedia --daemon

Ejemplos:

Correr la cdpedia con ./cdpedia.py --host=127.0.0.1 --port=8888 --daemon

y configurar el servidor de la siguiente forma

lighttpd:

::

   $HTTP["url"] =~ "^/cdpedia/" {
       proxy.server  = (
           "" => ( (
               "host" => "127.0.0.1",
               "port" => 8888
           ) )
       )
   }

apache:

::

       ProxyPass / http://127.0.0.1:8888/cdpedia/
       ProxyPassReverse / http://127.0.0.1:8888/cdpedia/

nginx:

::

   location /cdpedia {
     proxy_pass        http://127.0.0.1:8888;
   }

WSGI
::::

Esta opción implica no usar el servidor web integrado y en cambio servir utilizando el modulo WSGI del servidor web que se quiera (mod_wsgi para apache, etc). Aún no encontramos razones convincentes de por qué se preferiría esta opcion por sobre el servidor integrado.

Debería ser muy sencillo de hacer ya que la cdpedia es una aplicación WSGI, así que simplemente habria que escribir un achivo wsgi.py que importe la app de la cdpedia y decirle al servidor web que lea desde ahi.

Si optan por esta línea de trabajo, nos interesa mucho saber las razones! Manden mail por favor a `cdpedia@googlegroups.com`_ así les damos una mano y de paso generamos la documentación al respecto.

.. ############################################################################

.. _cdpedia@googlegroups.com: mailto:cdpedia@googlegroups.com

