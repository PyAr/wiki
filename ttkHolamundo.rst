#format rst

ttkHolaMundo
------------

Crea una ventana que muestra el famoso mensaje "Hola mundo".

`attachment:ttkHolamundo.png`_

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python3</span>
      </span><span class="line"><span class="c">#-*- coding:utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">tkinter</span> <span class="kn">as</span> <span class="nn">tk</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">tkinter</span> <span class="kn">import</span> <span class="n">ttk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">HolaMundoApp</span><span class="p">(</span><span class="n">ttk</span><span class="o">.</span><span class="n">Frame</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;Clase que define una ventana que muestra el &quot;Hola mundo&quot;&#39;&#39;&#39;</span>
      </span><span class="line">   
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">master</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="n">ttk</span><span class="o">.</span><span class="n">Frame</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">master</span><span class="p">)</span>
      </span><span class="line">       
      </span><span class="line">        <span class="c">#Creamos un label</span>
      </span><span class="line">        <span class="n">o</span> <span class="o">=</span> <span class="n">ttk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s">&#39;Hola PyAr!&#39;</span><span class="p">,</span> <span class="n">anchor</span><span class="o">=</span><span class="s">&#39;center&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="c">#Lo agregamos a la ventana.</span>
      </span><span class="line">        <span class="n">o</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s">&#39;both&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">        <span class="c">#Agregamos este frame a la ventana principal (Top level window)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s">&#39;both&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">       
      </span><span class="line">        <span class="c">#Configuramos la ventana principal</span>
      </span><span class="line">        <span class="n">top</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">winfo_toplevel</span><span class="p">()</span>
      </span><span class="line">        <span class="n">top</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&#39;Hola mundo&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">top</span><span class="o">.</span><span class="n">minsize</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>
      </span><span class="line">       
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">app</span> <span class="o">=</span> <span class="n">HolaMundoApp</span><span class="p">()</span>
      </span><span class="line">    <span class="n">app</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

