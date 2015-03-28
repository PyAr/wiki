#format rst

Locals De Una Funcion Que Lanzo Una Excepcion
=============================================

ejemplo de como obtener las variables locales a la función que lanzo una excepion.

En realidad son los locals de la funcion llamada.

Lo uso para pasarle los locals de la funcion a un template de django desde un decorador.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">inspect</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">fun</span><span class="p">():</span>
      </span><span class="line">    <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="s">&quot;dos&quot;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;hi!&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="n">fun</span><span class="p">()</span>
      </span><span class="line"><span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">error</span><span class="p">:</span>
      </span><span class="line">    <span class="n">fun_frame</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">trace</span><span class="p">()[</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;locals in fun: &quot;</span><span class="p">,</span> <span class="n">fun_frame</span><span class="o">.</span><span class="n">f_locals</span>
      </span><span class="line">    <span class="k">del</span> <span class="n">fun_frame</span>
      </span>

