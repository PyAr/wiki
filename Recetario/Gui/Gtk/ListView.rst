#format rst

Gtk ListView
------------

`attachment:gtklistexample.png`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gobject</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">GtkListExample</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;clase que representa una ventana con una lista&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">640</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">480</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s">&quot;gtk list example&quot;</span><span class="p">,</span>
      </span><span class="line">            <span class="n">on_exit</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="c"># llamamos al constructor de la clase padre</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># establecemos el tamanio</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># establecemos el titulo</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># creamos el modelo de cada fila</span>
      </span><span class="line">        <span class="c"># el modelo y la vista se crean separadamente y se relacionan despues</span>
      </span><span class="line">        <span class="c"># https://es.wikipedia.org/wiki/Modelo_Vista_Controlador</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ListStore</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bool</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># creamos el widget que va a mostrar la lista y le pasamos el modelo</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TreeView</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># creamos los objetos que van a renderizar los atributos</span>
      </span><span class="line">        <span class="n">textrenderer</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">CellRendererText</span><span class="p">()</span>
      </span><span class="line">        <span class="c"># seteamos una propiedad</span>
      </span><span class="line">        <span class="n">textrenderer</span><span class="o">.</span><span class="n">set_property</span><span class="p">(</span><span class="s">&quot;xalign&quot;</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># un renderer para renderizar booleanos como checkbox</span>
      </span><span class="line">        <span class="n">boolrenderer</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">CellRendererToggle</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># creamos las columnas de la lista</span>
      </span><span class="line">        <span class="c"># no necesariamente todos los elementos del modelo se deben mostrar</span>
      </span><span class="line">        <span class="c"># tampoco es necesario que se muestren en el orden del modelo, por</span>
      </span><span class="line">        <span class="c"># eso creamos las columnas para decirle que elementos del modelo</span>
      </span><span class="line">        <span class="c"># mostrar y como mostrarlos</span>
      </span><span class="line">        <span class="n">column1</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TreeViewColumn</span><span class="p">(</span><span class="s">&quot;nombre&quot;</span><span class="p">,</span> <span class="n">textrenderer</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">        <span class="n">column1</span><span class="o">.</span><span class="n">set_expand</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">column2</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TreeViewColumn</span><span class="p">(</span><span class="s">&quot;edad&quot;</span><span class="p">,</span> <span class="n">textrenderer</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line">        <span class="n">column2</span><span class="o">.</span><span class="n">set_expand</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">column3</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TreeViewColumn</span><span class="p">(</span><span class="s">&quot;algo&quot;</span><span class="p">,</span> <span class="n">boolrenderer</span><span class="p">,</span> <span class="n">active</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
      </span><span class="line">        <span class="n">column3</span><span class="o">.</span><span class="n">set_expand</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># agregamos las columnas</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append_column</span><span class="p">(</span><span class="n">column1</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append_column</span><span class="p">(</span><span class="n">column2</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append_column</span><span class="p">(</span><span class="n">column3</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># agregamos la lista a la ventana</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span>
      </span><span class="line">        <span class="c"># mostramos el widget</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">        <span class="c"># conectamos un manejador para cuando aprieten cerrar</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">on_exit</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">number</span><span class="p">,</span> <span class="n">boolean</span><span class="p">):</span>
      </span><span class="line">        <span class="c"># agregamos una fila al modelo</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">string</span><span class="p">,</span> <span class="n">number</span><span class="p">,</span> <span class="n">boolean</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">window</span> <span class="o">=</span> <span class="n">GtkListExample</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="s">&quot;bob&quot;</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="s">&quot;patricio&quot;</span><span class="p">,</span> <span class="mi">24</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="s">&quot;arenita&quot;</span><span class="p">,</span> <span class="mi">27</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

