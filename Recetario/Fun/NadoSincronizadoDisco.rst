#format rst

Nado Sincronizado
-----------------

un generador de nado sincronizado con luces de colores usando colorama (sudo pip install colorama)

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">random</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">colorama</span> <span class="kn">import</span> <span class="n">init</span><span class="p">,</span> <span class="n">Fore</span>
      </span><span class="line"><span class="n">ARM</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;</span><span class="se">\\</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;_&#39;</span><span class="p">,</span> <span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">figure</span><span class="p">():</span>
      </span><span class="line">    <span class="n">color</span> <span class="o">=</span> <span class="n">Fore</span><span class="o">.</span><span class="n">__dict__</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">([</span><span class="s">&#39;BLACK&#39;</span><span class="p">,</span> <span class="s">&#39;BLUE&#39;</span><span class="p">,</span> <span class="s">&#39;CYAN&#39;</span><span class="p">,</span>
      </span><span class="line">        <span class="s">&#39;GREEN&#39;</span><span class="p">,</span> <span class="s">&#39;MAGENTA&#39;</span><span class="p">,</span> <span class="s">&#39;RED&#39;</span><span class="p">,</span> <span class="s">&#39;RESET&#39;</span><span class="p">,</span> <span class="s">&#39;WHITE&#39;</span><span class="p">,</span> <span class="s">&#39;YELLOW&#39;</span><span class="p">])]</span>
      </span><span class="line">    <span class="n">fig</span> <span class="o">=</span> <span class="n">color</span> <span class="o">+</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">ARM</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;o&quot;</span> <span class="o">+</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">ARM</span><span class="p">)</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">fig</span><span class="p">)</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">erase</span><span class="p">():</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\b\b\b</span><span class="s">&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">dance</span><span class="p">():</span>
      </span><span class="line">    <span class="n">init</span><span class="p">()</span>
      </span><span class="line">    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">        <span class="n">figure</span><span class="p">()</span>
      </span><span class="line">        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.5</span><span class="p">)</span>
      </span><span class="line">        <span class="n">erase</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">dance</span><span class="p">()</span>
      </span>

