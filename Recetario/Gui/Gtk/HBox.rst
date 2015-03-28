#format rst
## page was renamed from Recetario/Gtk/HBox

GtkHBox
-------

ejemplo que muestra el uso de hbox (cajas horizontales) para ordenar elementos de forma horizontal

`attachment:hbox.png`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Ventana</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;clase que define una ventana que saluda&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor, se llama al constructor de la clase padre&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;hbox&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># creamos una caja horizontal que contiene elementos</span>
      </span><span class="line">        <span class="c"># de manera horizontal</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HBox</span><span class="p">()</span>
      </span><span class="line">        <span class="c"># agregamos tres elementos</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;uno&quot;</span><span class="p">))</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;dos&quot;</span><span class="p">))</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;tres&quot;</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hbox</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hbox</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;delete-event&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_delete</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">window</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;llamado cuando se cierra la ventana&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">ventana</span> <span class="o">=</span> <span class="n">Ventana</span><span class="p">()</span>
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

