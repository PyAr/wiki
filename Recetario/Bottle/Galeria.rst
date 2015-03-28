#format rst

Mini Galeria de Imagenes Bottle
===============================

* Como hacer una Mini Galeria de Imagenes en Bottle_, ejemplo basado en el Hola Mundo.

Usa Bottle_ para servir 1 pagina incrustada en la propia aplicacion, la misma desplega HTML, CSS y Js.

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
      </span><span class="line"><span class="n">GALLERY</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="s">&lt;!DOCTYPE HTML&gt;</span>
      </span><span class="line"><span class="s">&lt;html&gt;</span>
      </span><span class="line"><span class="s">  &lt;head&gt;</span>
      </span><span class="line"><span class="s">    &lt;title&gt;PYTHON-BOTTLE DEMO&lt;/title&gt;</span>
      </span><span class="line"><span class="s">    &lt;link rel=&quot;shortcut icon&quot; href=&quot;http://python.org.ar/images/pyar.ico&quot; type=&quot;image/x-icon&quot;/&gt;</span>
      </span><span class="line"><span class="s">    &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;chrome=1&quot;&gt;</span>
      </span><span class="line"><span class="s">    &lt;META NAME=&quot;ROBOTS&quot; CONTENT=&quot;NOINDEX, NOFOLLOW&quot;&gt;</span>
      </span><span class="line"><span class="s">    &lt;style type=&quot;text/css&quot;&gt; body { background-color: black; } &lt;/style&gt;</span>
      </span><span class="line"><span class="s">&lt;script language=&quot;JavaScript&quot;&gt;</span>
      </span><span class="line"><span class="s">&lt;!--</span>
      </span><span class="line"><span class="s">if (document.images) {</span>
      </span><span class="line"><span class="s">    demo1 = new Image();</span>
      </span><span class="line"><span class="s">    demo1.src = &quot;http://www.gstatic.com/webp/gallery/5.webp&quot;;</span>
      </span><span class="line"><span class="s">    demo2 = new Image();</span>
      </span><span class="line"><span class="s">    demo2.src = &quot;http://www.gstatic.com/webp/gallery/2.webp&quot;;</span>
      </span><span class="line"><span class="s">    demo3 = new Image();</span>
      </span><span class="line"><span class="s">    demo3.src = &quot;http://www.gstatic.com/webp/gallery/3.webp&quot;;</span>
      </span><span class="line"><span class="s">    demo4 = new Image();</span>
      </span><span class="line"><span class="s">    demo4.src = &quot;http://www.gstatic.com/webp/gallery/4.webp&quot;;</span>
      </span><span class="line"><span class="s">}</span>
      </span><span class="line"><span class="s">function timeimgs(numb) {  // Reusable timer</span>
      </span><span class="line"><span class="s">    thetimer = setTimeout(&quot;imgturn(&#39;&quot; +numb+ &quot;&#39;)&quot;, 1000);</span>
      </span><span class="line"><span class="s">}</span>
      </span><span class="line"><span class="s">function imgturn(numb) {</span>
      </span><span class="line"><span class="s">    if (document.images) {</span>
      </span><span class="line"><span class="s">        if (numb == &quot;4&quot;) {         </span>
      </span><span class="line"><span class="s">            document[&quot;demo&quot;].src = eval(&quot;demo4.src&quot;);</span>
      </span><span class="line"><span class="s">            timeimgs(&#39;1&#39;);</span>
      </span><span class="line"><span class="s">        }</span>
      </span><span class="line"><span class="s">    else {</span>
      </span><span class="line"><span class="s">        document[&quot;demo&quot;].src = eval(&quot;demo&quot; + numb + &quot;.src&quot;);</span>
      </span><span class="line"><span class="s">        timeimgs(numb = ++numb);</span>
      </span><span class="line"><span class="s">        }</span>
      </span><span class="line"><span class="s">    }</span>
      </span><span class="line"><span class="s">}</span>
      </span><span class="line"><span class="s">// --&gt;</span>
      </span><span class="line"><span class="s">&lt;/script&gt;</span>
      </span><span class="line"><span class="s">&lt;/head&gt;</span>
      </span><span class="line"><span class="s">&lt;body onload=&quot;timeimgs(&#39;1&#39;);&quot;&gt;</span>
      </span><span class="line"><span class="s">&lt;div align=&quot;center&quot;&gt;</span>
      </span><span class="line"><span class="s">    &lt;img src=&quot;http://www.gstatic.com/webp/gallery/1.webp&quot; name=&quot;demo&quot; width=&quot;1024&quot; height=&quot;768&quot; alt=&quot;demo&quot; title=&quot;PYTHON-BOTTLE DEMO&quot;&gt;</span>
      </span><span class="line"><span class="s">&lt;/div&gt;</span>
      </span><span class="line"><span class="s">&lt;/body&gt;</span>
      </span><span class="line"><span class="s">&lt;/html&gt;</span>
      </span><span class="line"><span class="s">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">GALLERY</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Ejemplo de uso de bottle.request para mostrar tu direccion ip</span>
      </span><span class="line"><span class="nd">@route</span><span class="p">(</span><span class="s">&#39;/tu_ip&#39;</span><span class="p">)</span> <span class="c"># ingresando a esa URL devuelve tu IP</span>
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

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

.. ############################################################################

.. _Bottle: http://bottlepy.org

