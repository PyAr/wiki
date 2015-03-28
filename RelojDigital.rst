#format rst

Reloj Digital
=============

* Crear un Reloj digital simple, empleando un Label de TK.

**Screenshot:**

`attachment:temp.jpg`_

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">focus</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;ǝɯıʇ uoɥʇʎd&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">cursor</span><span class="o">=</span><span class="s">&#39;watch&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">time1</span> <span class="o">=</span> <span class="s">&#39;&#39;</span>
      </span><span class="line"><span class="n">clock</span> <span class="o">=</span> <span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;ubuntu&#39;</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="s">&#39;bold&#39;</span><span class="p">),</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;#3C3B37&#39;</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s">&#39;white&#39;</span><span class="p">,</span> <span class="n">bd</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">clock</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="n">BOTH</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">tick</span><span class="p">():</span>
      </span><span class="line">    <span class="k">global</span> <span class="n">time1</span>
      </span><span class="line">    <span class="n">time2</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s">&#39;%H:%M:%S&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">time2</span> <span class="o">!=</span> <span class="n">time1</span><span class="p">:</span>
      </span><span class="line">        <span class="n">time1</span> <span class="o">=</span> <span class="n">time2</span>
      </span><span class="line">        <span class="n">clock</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">time2</span><span class="p">)</span>
      </span><span class="line">    <span class="n">clock</span><span class="o">.</span><span class="n">after</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="n">tick</span><span class="p">)</span>
      </span><span class="line"><span class="n">tick</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

