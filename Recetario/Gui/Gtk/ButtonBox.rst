#format rst

ButtonBox
=========

este ejemplo muestra como usar un contenedor de botones para agregar botones y hacer que mantengan su tamanio óptimo y se distribuyan por la pantalla de manera homogénea.

`attachment:buttonbox-demo.png`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;button box demo&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">vbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox1</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HButtonBox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox1</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">stock</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_OK</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">build_bbox</span><span class="p">():</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;build a hbox fill it with example buttons and return it&quot;&quot;&quot;</span>
      </span><span class="line">        <span class="n">hbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HButtonBox</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">stock</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_YES</span><span class="p">))</span>
      </span><span class="line">        <span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">stock</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_NO</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">hbox</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox2</span> <span class="o">=</span> <span class="n">build_bbox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox2</span><span class="o">.</span><span class="n">set_layout</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONBOX_SPREAD</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox3</span> <span class="o">=</span> <span class="n">build_bbox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox3</span><span class="o">.</span><span class="n">set_layout</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONBOX_EDGE</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox4</span> <span class="o">=</span> <span class="n">build_bbox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox4</span><span class="o">.</span><span class="n">set_layout</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONBOX_START</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox5</span> <span class="o">=</span> <span class="n">build_bbox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox5</span><span class="o">.</span><span class="n">set_layout</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONBOX_END</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">hbox6</span> <span class="o">=</span> <span class="n">build_bbox</span><span class="p">()</span>
      </span><span class="line"><span class="n">hbox6</span><span class="o">.</span><span class="n">set_layout</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONBOX_END</span><span class="p">)</span>
      </span><span class="line"><span class="n">help_button</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">stock</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_HELP</span><span class="p">)</span>
      </span><span class="line"><span class="n">hbox6</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">help_button</span><span class="p">)</span>
      </span><span class="line"><span class="n">hbox6</span><span class="o">.</span><span class="n">set_child_secondary</span><span class="p">(</span><span class="n">help_button</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox1</span><span class="p">)</span>
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox2</span><span class="p">)</span>
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox3</span><span class="p">)</span>
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox4</span><span class="p">)</span>
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox5</span><span class="p">)</span>
      </span><span class="line"><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">hbox6</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">vbox</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;destroy&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

Mas Información
---------------

* http://pygtk.org/docs/pygtk/class-gtkhbuttonbox.html

* http://pygtk.org/docs/pygtk/class-gtkbuttonbox.html

* http://pygtk.org/docs/pygtk/class-gtkbox.html

