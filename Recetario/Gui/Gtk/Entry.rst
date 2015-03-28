#format rst
## page was renamed from Recetario/Gtk/Entry

GtkEntry
--------

crea una ventana con un label y un campo de texto y muestra el mensaje hola **nombre** con el valor ingresado en el entry.

`attachment:Entry.png`_

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
      </span><span class="line">        <span class="c"># un tamanio muy chico para que se expanda el minimo tamanio necesario</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;nombre&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">entry</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;entry&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># 5 pixeles de espacio entre el borde de la ventana y el primer</span>
      </span><span class="line">        <span class="c"># contenedor</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_border_width</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># 5 pixeles de espaciado entre cada widget</span>
      </span><span class="line">        <span class="n">hbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HBox</span><span class="p">(</span><span class="n">spacing</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
      </span><span class="line">        <span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">        <span class="n">hbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">hbox</span><span class="p">)</span>
      </span><span class="line">        <span class="n">hbox</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;delete-event&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_delete</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># conectamos la senial activate (el usuario presiona enter)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">entry</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;activate&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_entry_activate</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">window</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;llamado cuando se cierra la ventana&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_entry_activate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entry</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;llamada cuando se presiona enter en el entry, el primer elemento</span>
      </span><span class="line"><span class="sd">        de toda senial de gtk es el elemento que emite la senial, asi que no</span>
      </span><span class="line"><span class="sd">        necesitamos tener una referencia al elemento para interactuar con el&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">message</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_OK</span><span class="p">,</span>
      </span><span class="line">            <span class="n">message_format</span><span class="o">=</span><span class="s">&quot;hola &quot;</span> <span class="o">+</span> <span class="n">entry</span><span class="o">.</span><span class="n">get_text</span><span class="p">())</span>
      </span><span class="line">        <span class="n">message</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line">        <span class="n">message</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">hola</span> <span class="o">=</span> <span class="n">Ventana</span><span class="p">()</span>
      </span><span class="line">    <span class="n">hola</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

