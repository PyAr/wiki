#format rst
## page was renamed from Recetario/Gtk/ConfirmClose

GtkConfirmClose
---------------

Ejemplo de como solicitar confirmación de cierre en una ventana

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">VentanaPrincipal</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;la ventana principal&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">300</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&#39;Ejemplo&#39;</span><span class="p">)</span>
      </span><span class="line">   
      </span><span class="line">        <span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;cerrame&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">label</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_close</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;metodo llamado cuando aprietan el boton cerrar&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">confirmar_cierre</span><span class="p">():</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">confirmar_cierre</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;muestra un dialogo que pregunta si esta seguro que</span>
      </span><span class="line"><span class="sd">        quiere cerrar, devuelve True si selecciona si&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">dialogo</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">MESSAGE_QUESTION</span><span class="p">,</span>
      </span><span class="line">            <span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_YES_NO</span><span class="p">,</span>
      </span><span class="line">            <span class="n">message_format</span><span class="o">=</span><span class="s">&quot;Esta seguro que desea salir?&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">response</span> <span class="o">=</span> <span class="n">dialogo</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line">        <span class="n">dialogo</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">response</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_YES</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">       
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">test</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;prueba la implementacion&#39;&#39;&#39;</span>
      </span><span class="line">    <span class="n">ventana</span> <span class="o">=</span> <span class="n">VentanaPrincipal</span><span class="p">()</span>
      </span><span class="line">    <span class="n">ventana</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">test</span><span class="p">()</span>
      </span>

