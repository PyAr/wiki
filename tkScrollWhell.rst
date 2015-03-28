#format rst

tkScrollWhell
-------------

Usando la rueda de Scroll del raton con TK. Ejemplo simple con un poco de imaginacion puede manejar mas cosas.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c">#-*- coding:utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="n">label</span> <span class="o">=</span> <span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s">&#39;Elija su Sexo usando la Rueda Scroll del Raton:&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">label</span><span class="o">.</span><span class="n">pack</span><span class="p">()</span>
      </span><span class="line"><span class="n">optionlist</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;Femenino&quot;</span><span class="p">,</span> <span class="s">&quot;Masculino&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">var</span> <span class="o">=</span> <span class="n">StringVar</span><span class="p">()</span>
      </span><span class="line"><span class="n">var</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">optionlist</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
      </span><span class="line"><span class="n">optmen</span> <span class="o">=</span> <span class="n">OptionMenu</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">var</span><span class="p">,</span> <span class="s">&quot;Femenino&quot;</span><span class="p">,</span> <span class="s">&quot;Masculino&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">mouse_wheel</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>  <span class="c"># responde a la rueda de scroll</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">num</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">or</span> <span class="n">event</span><span class="o">.</span><span class="n">delta</span> <span class="o">==</span> <span class="o">-</span><span class="mi">120</span><span class="p">:</span>  
      </span><span class="line">            <span class="n">var</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">optionlist</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">num</span> <span class="o">==</span> <span class="mi">4</span> <span class="ow">or</span> <span class="n">event</span><span class="o">.</span><span class="n">delta</span> <span class="o">==</span> <span class="mi">120</span><span class="p">:</span>
      </span><span class="line">            <span class="n">var</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">optionlist</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">optmen</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Button-4&gt;&quot;</span><span class="p">,</span> <span class="n">mouse_wheel</span><span class="p">)</span>
      </span><span class="line"><span class="n">optmen</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Button-5&gt;&quot;</span><span class="p">,</span> <span class="n">mouse_wheel</span><span class="p">)</span>
      </span><span class="line"><span class="n">optmen</span><span class="o">.</span><span class="n">pack</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

