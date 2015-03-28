#format rst
## page was renamed from Recetario/Gtk/StatusIcon

GtkStatusIcon
-------------

Aplicación con ícono en el area de notificaciones.

Tiene un menú contextual (About/Quit) y con el botón izquierdo abre una ventana simple.

`attachment:trayapp.png`_

::

   .. raw:: html
      <span class="line"><span class="sd">&#39;&#39;&#39;Mini ejemplo de system tray app.&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">TrayApp</span><span class="p">:</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">StatusIcon</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span><span class="o">.</span><span class="n">set_from_stock</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_INFO</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span><span class="o">.</span><span class="n">set_tooltip</span><span class="p">(</span><span class="s">&#39;StatusIcon Example&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;popup-menu&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">right_click_event</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">left_click_event</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">left_click_event</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">status_icon</span><span class="p">):</span>
      </span><span class="line">        <span class="c"># Para que solo abra una ventana</span>
      </span><span class="line">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;window&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">):</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Hola pyar&#39;</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&#39;Hello world&#39;</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete_event&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">exit_window</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">exit_window</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">,</span> <span class="n">event</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">window</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">right_click_event</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">status_icon</span><span class="p">,</span> <span class="n">button</span><span class="p">,</span> <span class="n">activate_time</span><span class="p">):</span>
      </span><span class="line">        <span class="n">menu</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Menu</span><span class="p">()</span>
      </span><span class="line">        <span class="n">about</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MenuItem</span><span class="p">(</span><span class="s">&#39;About&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">quit</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MenuItem</span><span class="p">(</span><span class="s">&#39;Quit&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">about</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">show_about_dialog</span><span class="p">)</span>
      </span><span class="line">        <span class="n">quit</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line">        <span class="n">menu</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">about</span><span class="p">)</span>
      </span><span class="line">        <span class="n">menu</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">quit</span><span class="p">)</span>
      </span><span class="line">        <span class="n">menu</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">        <span class="n">menu</span><span class="o">.</span><span class="n">popup</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">status_icon_position_menu</span><span class="p">,</span>
      </span><span class="line">                   <span class="n">button</span><span class="p">,</span> <span class="n">activate_time</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">statusicon</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">show_about_dialog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">):</span>
      </span><span class="line">                <span class="n">about_dialog</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">AboutDialog</span><span class="p">()</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">set_destroy_with_parent</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">set_name</span><span class="p">(</span><span class="s">&#39;StatusIcon Example&#39;</span><span class="p">)</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">set_version</span><span class="p">(</span><span class="s">&#39;1.0&#39;</span><span class="p">)</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">set_authors</span><span class="p">([</span><span class="s">&#39;Name Lastname&#39;</span><span class="p">])</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line">                <span class="n">about_dialog</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">tray_app</span> <span class="o">=</span> <span class="n">TrayApp</span><span class="p">()</span>
      </span><span class="line">    <span class="n">tray_app</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

Más info en http://www.learnpygtk.org/pygtktutorial/statusicon.html

-------------------------



  CategoryRecetas_

