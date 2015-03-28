#format rst
## page was renamed from Recetario/Gtk/StockItems

Gtk stock items
===============

ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre 

un screenshot:

`attachment:stock-gtk.png`_

::

   .. raw:: html
      <span class="line"><span class="sd">&#39;&#39;&#39;modulo que muestra el uso de los stock icons en gtk&#39;&#39;&#39;</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">run</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;muestra una ventana con algunos elementos con stock icons&#39;&#39;&#39;</span>
      </span><span class="line">    <span class="n">ventana</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">400</span><span class="p">,</span> <span class="mi">400</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">box</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">(</span><span class="n">spacing</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">gtk</span><span class="o">.</span><span class="n">stock_list_ids</span><span class="p">():</span>
      </span><span class="line">        <span class="n">imagen</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Image</span><span class="p">()</span>
      </span><span class="line">        <span class="n">imagen</span><span class="o">.</span><span class="n">set_from_stock</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ICON_SIZE_BUTTON</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">etiqueta</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;gtk.STOCK&quot;</span> <span class="o">+</span> <span class="nb">id</span><span class="p">[</span><span class="mi">3</span><span class="p">:]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;-&quot;</span><span class="p">,</span> <span class="s">&quot;_&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">upper</span><span class="p">())</span>
      </span><span class="line">        <span class="n">etiqueta</span><span class="o">.</span><span class="n">set_alignment</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">caja</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HBox</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">caja</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">imagen</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">        <span class="n">caja</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">etiqueta</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">box</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">caja</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">scroll</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ScrolledWindow</span><span class="p">()</span>
      </span><span class="line">    <span class="n">scroll</span><span class="o">.</span><span class="n">add_with_viewport</span><span class="p">(</span><span class="n">box</span><span class="p">)</span>
      </span><span class="line">    <span class="n">scroll</span><span class="o">.</span><span class="n">set_policy</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">scroll</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">run</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

