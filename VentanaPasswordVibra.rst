#format rst

Ventana de Password que Vibra
=============================

* Crear una ventana para passwords que vibra si la password es incorrecta, el campo de texto oculta los caracteres en pantalla, la vibracion es configurable.

**Screenshot:**

`attachment:temp.jpg`_

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">random</span> <span class="kn">import</span> <span class="n">randint</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="c"># correct password is: password</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="n">Event</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
      </span><span class="line">    <span class="k">if</span> <span class="nb">hash</span><span class="p">(</span><span class="n">var</span><span class="o">.</span><span class="n">get</span><span class="p">())</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1767432613</span><span class="p">:</span>  <span class="c"># hash for password</span>
      </span><span class="line">        <span class="n">o</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">()</span>
      </span><span class="line">        <span class="n">l</span><span class="p">[</span><span class="s">&#39;text&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;Wrong Password:</span><span class="se">\n</span><span class="s">Attemp will be logged and reported.&#39;</span>
      </span><span class="line">        <span class="n">l</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">fg</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">times</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">50</span><span class="p">):</span>
      </span><span class="line">                 <span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">(</span><span class="s">&quot;+</span><span class="si">%d</span><span class="s">+</span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;+&quot;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span><span class="o">+</span><span class="n">randint</span><span class="p">(</span><span class="o">-</span><span class="mi">69</span><span class="p">,</span> <span class="mi">69</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;+&quot;</span><span class="p">)[</span><span class="mi">2</span><span class="p">])</span><span class="o">+</span><span class="n">randint</span><span class="p">(</span><span class="o">-</span><span class="mi">69</span><span class="p">,</span> <span class="mi">69</span><span class="p">)))</span>
      </span><span class="line">                 <span class="n">root</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
      </span><span class="line">                 <span class="n">sleep</span><span class="p">(</span><span class="o">.</span><span class="mo">05</span><span class="p">)</span>
      </span><span class="line">                 <span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">(</span><span class="n">o</span><span class="p">)</span>
      </span><span class="line">        <span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">(</span><span class="n">o</span><span class="p">)</span>       
      </span><span class="line">        <span class="n">root</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">l</span><span class="p">[</span><span class="s">&#39;text&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;OK: Connected to FBI Main Server...&#39;</span>
      </span><span class="line">        <span class="k">print</span> <span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">Connected to FBI Main Server...</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">l</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">fg</span><span class="o">=</span><span class="s">&#39;black&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">root</span><span class="o">.</span><span class="n">iconify</span><span class="p">()</span>
      </span><span class="line">        <span class="n">sleep</span><span class="p">(</span><span class="o">.</span><span class="mi">25</span><span class="p">)</span>
      </span><span class="line">        <span class="n">root</span><span class="o">.</span><span class="n">deiconify</span><span class="p">()</span>
      </span><span class="line">        <span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">()</span>
      </span><span class="line">    <span class="n">var</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c">#        </span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">resizable</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;FBI VPN Client&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">geometry</span><span class="p">(</span><span class="s">&quot;+800+350&quot;</span><span class="p">)</span>            
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">wm_attributes</span><span class="p">(</span><span class="s">&quot;-topmost&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">focus</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">bg</span><span class="o">=</span><span class="s">&#39;#F2F1F0&#39;</span><span class="p">,</span> <span class="n">cursor</span><span class="o">=</span><span class="s">&#39;hand2&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">var</span> <span class="o">=</span> <span class="n">StringVar</span><span class="p">()</span>
      </span><span class="line"><span class="n">l</span> <span class="o">=</span> <span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span> <span class="o">=</span> <span class="s">&quot;FBI Login: Please type your password...&quot;</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;ubuntu&#39;</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;#F2F1F0&#39;</span><span class="p">,</span> <span class="n">bd</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">relief</span><span class="o">=</span><span class="s">&#39;flat&#39;</span><span class="p">,</span> <span class="n">cursor</span><span class="o">=</span><span class="s">&#39;hand2&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">l</span><span class="o">.</span><span class="n">grid</span><span class="p">()</span>
      </span><span class="line"><span class="n">a</span> <span class="o">=</span> <span class="n">Entry</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="s">&#39;ubuntu&#39;</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="s">&#39;bold&#39;</span><span class="p">),</span> <span class="n">show</span> <span class="o">=</span> <span class="s">&#39;●&#39;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s">&#39;#D7DAED&#39;</span><span class="p">,</span> <span class="n">bd</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">relief</span><span class="o">=</span><span class="s">&#39;flat&#39;</span><span class="p">,</span> <span class="n">cursor</span><span class="o">=</span><span class="s">&#39;xterm&#39;</span><span class="p">,</span> <span class="n">highlightcolor</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">,</span> <span class="n">textvariable</span> <span class="o">=</span> <span class="n">var</span><span class="p">)</span>  <span class="c"># show = &#39;*&#39;</span>
      </span><span class="line"><span class="n">a</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="n">row</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">column</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">padx</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">pady</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span>
      </span><span class="line"><span class="n">a</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Return&gt;&quot;</span><span class="p">,</span> <span class="n">check</span><span class="p">)</span>
      </span><span class="line"><span class="n">a</span><span class="o">.</span><span class="n">focus</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

