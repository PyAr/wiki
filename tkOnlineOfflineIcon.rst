#format rst

tkOnLineOffLineIcon
-------------------

Crea un icono que cambia de estado segun si se esta o no conectado a Internet. Notar que se pueden cambiar mas propiedades del boton que las que este simpl ejemplo cambia.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c">#-*- coding:utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">socket</span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="c"># Comprobador de conexion a Internet</span>
      </span><span class="line"><span class="n">inet</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">bitmap</span><span class="o">=</span><span class="s">&#39;info&#39;</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s">&#39;green&#39;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;white&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">inet</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">pady</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">padx</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="s">&#39;google.com&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">c</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">create_connection</span><span class="p">((</span><span class="s">&#39;google.com&#39;</span><span class="p">,</span> <span class="mi">80</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
      </span><span class="line">    <span class="n">m</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="s">&#39;google.com&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">m</span>  <span class="c"># imprime la ip de google.com para pruebas</span>
      </span><span class="line">    <span class="n">c</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line"><span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">gaierror</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="p">(</span><span class="s">&quot; ERROR: DNS Error... &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">inet</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">bitmap</span><span class="o">=</span><span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;black&#39;</span><span class="p">)</span> <span class="c"># cambia a un icono de error</span>
      </span><span class="line"><span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="p">(</span><span class="s">&quot; ERROR: Connection error... &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">inet</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">bitmap</span><span class="o">=</span><span class="s">&#39;error&#39;</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;black&#39;</span><span class="p">)</span> <span class="c"># cambia a un icono de error</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

