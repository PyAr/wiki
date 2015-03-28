#format rst

Hola Mundo Bottle
=================

* Como hacer un hola mundo en Bottle_, ejemplo simple.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">route</span><span class="p">,</span> <span class="n">run</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39;Hola Mundo!&#39;</span>
      </span><span class="line"><span class="n">run</span><span class="p">()</span>
      </span>

**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python holamundo.py
   Bottle server starting up (using WSGIRefServer())...
   Listening on http://127.0.0.1:8080/
   Use Ctrl-C to quit.

   localhost.localdomain - - [18/Jul/2011 18:22:09] "GET / HTTP/1.1" 200 11
   localhost.localdomain - - [18/Jul/2011 18:22:09] "GET /favicon.ico HTTP/1.1" 404 687
   ^C
   juan@wind:~$

-------------------------

 

* Mejorando nuestro  hola mundo en Bottle_, ejemplo mas completo, ideal para Plantilla para una App nueva.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">route</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">run</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">redirect</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">debug</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">error</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">request</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">abort</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39;Hola Mundo!&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejemplo de uso de bottle.request para mostrar tu direccion ip</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/tuip&#39;</span><span class="p">)</span> <span class="c"># ingresando a esa URL devuelve tu IP</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">show_ip</span><span class="p">():</span>
      </span><span class="line">    <span class="n">ip</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;REMOTE_ADDR&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">ip</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejemplo de uso de bottle.error para el 404, la pagina no existe</span>
      </span><span class="line"><span class="nd">@error</span><span class="p">(</span><span class="mi">404</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">mistake404</span><span class="p">(</span><span class="n">code</span><span class="p">):</span> <span class="c"># Usando HTML directamente, de ejemplo.</span>
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39;&lt;title&gt;bottle app&lt;/title&gt;&lt;br&gt;&lt;b&gt;ERROR 404:la pagina no existe.&lt;/b&gt;&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejemplo de uso de bottle.abort para URL no permitida, error 401</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/restricted&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">restricted</span><span class="p">():</span>
      </span><span class="line">    <span class="n">abort</span><span class="p">(</span><span class="mi">401</span><span class="p">,</span> <span class="s">&#39;ERROR 401:URL no permitida.&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejemplo de Redireccion bottle.redirect de URL, por URL incorrecta</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/index.php&#39;</span><span class="p">)</span> <span class="c"># si va a index.php</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">wrong</span><span class="p">():</span>
      </span><span class="line">    <span class="n">redirect</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)</span> <span class="c"># enviarlo a &quot;/&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejecucion de Main</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
      </span><span class="line">    <span class="n">debug</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span><span class="c"># True para desarrollo, False para Produccion</span>
      </span><span class="line">    <span class="c">#</span>
      </span><span class="line">    <span class="c"># Por que es esto?: Puerto &lt;1024 requiere Privilegios elevados</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">geteuid</span><span class="p">()</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span> <span class="c"># root check</span>
      </span><span class="line">        <span class="n">run</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="s">&#39;0.0.0.0&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">reloader</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">run</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="s">&#39;127.0.0.1&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">8080</span><span class="p">,</span> <span class="n">reloader</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span><span class="o">==</span><span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">main</span><span class="p">()</span>
      </span>

*Nota: Hay mas Features en* Bottle_*, pero eso es suficiente para un Hola Mundo completo y didactico.*

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

.. ############################################################################

.. _Bottle: http://bottlepy.org

