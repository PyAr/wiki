
Otro ejemplo del uso de threads con gtk, compare con el `otro ejemplo`_ que utiliza colas

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">random</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">threading</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk.gdk</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="n">texts</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;eggs&#39;</span><span class="p">,</span> <span class="s">&#39;spam&#39;</span><span class="p">,</span> <span class="s">&#39;pyar&#39;</span><span class="p">,</span> <span class="s">&#39;gtk&#39;</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">molesto</span><span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;un thread que quiere molestar el main thread&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">):</span>
      </span><span class="line">        <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">label</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;metodo principal del thread, duerme un tiempo aleatorio y despues</span>
      </span><span class="line"><span class="sd">        cambia el Label&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">            <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span> <span class="o">*</span> <span class="mi">5</span><span class="p">)</span>
      </span><span class="line">            <span class="n">texto</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getName</span><span class="p">()</span> <span class="o">+</span> <span class="s">&#39; &#39;</span> <span class="o">+</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">texts</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">threads_enter</span><span class="p">()</span>
      </span><span class="line">            <span class="c"># zona critica de gtk</span>
      </span><span class="line">            <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">getName</span><span class="p">(),</span> <span class="s">&#39;escribiendo&#39;</span><span class="p">,</span> <span class="n">texto</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">texto</span><span class="p">)</span>
      </span><span class="line">            <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">threads_leave</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">ventana</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;ventana con un label, ninguna locura&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&#39;gtk con threads&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">threads_init</span><span class="p">()</span>
      </span><span class="line">    <span class="n">ventana</span> <span class="o">=</span> <span class="n">ventana</span><span class="p">()</span>
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">threads</span> <span class="o">=</span> <span class="p">[</span><span class="n">molesto</span><span class="p">(</span><span class="n">ventana</span><span class="o">.</span><span class="n">label</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)]</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="n">threads</span><span class="p">:</span>
      </span><span class="line">        <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

.. ############################################################################

.. _otro ejemplo: GtkMultiThread

