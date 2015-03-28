
GtkRunner
=========

ejemplo de como correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk 

lo que tienen que reusar es la clase GtkRunner_

simplemente la llaman pasandole:

* callback función o método que va a ser llamado en el main thread una vez que la función que demora termine

* func: función a llamar

* de 0 a n argumentos posicionales que serán pasados a func en la llamada

* de 0 a n argumentos nombrados que serán pasados a func en la llamada

func(*args, **kwargs) sera llamada en un thread aparte el cual sera monitoreado periódicamente por su finalizacion, una vez terminado llamara a callback pasandole una tupla cuyo primer elemento es True si la función termino con éxito y False si la función lanzo una excepción. El segundo elemento de la tupla es el valor retornado por la función si tuvo éxito o la excepción lanzada en caso que haya fallado.

obviamente en la función esa no pueden correr código relacionado con gtk

::

   .. raw:: html
      <span class="line"><span class="sd">&#39;&#39;&#39;example of a generic class to run a given function in a thread and call a</span>
      </span><span class="line"><span class="sd">callback in the main thread with the result of the function&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">glib</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">Queue</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">urllib</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">threading</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">GtkRunner</span><span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;run *func* in a thread with *args* and *kwargs* as arguments, when</span>
      </span><span class="line"><span class="sd">    finished call callback with a two item tuple containing a boolean as first</span>
      </span><span class="line"><span class="sd">    item informing if the function returned correctly and the returned value or</span>
      </span><span class="line"><span class="sd">    the exception thrown as second item</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">        <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">callback</span> <span class="o">=</span> <span class="n">callback</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">func</span> <span class="o">=</span> <span class="n">func</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">Queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">        <span class="n">glib</span><span class="o">.</span><span class="n">timeout_add_seconds</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">check</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        main function of the thread, run func with args and kwargs</span>
      </span><span class="line"><span class="sd">        and get the result, call callback with the (True, result)</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">        if an exception is thrown call callback with (False, exception)</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">))</span>
      </span><span class="line">        <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">ex</span><span class="p">:</span>
      </span><span class="line">            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="bp">False</span><span class="p">,</span> <span class="n">ex</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        check if func finished</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">False</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span> <span class="n">Queue</span><span class="o">.</span><span class="n">Empty</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">callback</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    main function called when the module is run from the command line</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">return_slow</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">sleep</span><span class="o">=</span><span class="mi">5</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        a demo function that returns result slowly</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep</span><span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">result</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">fail_slow</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">sleep</span><span class="o">=</span><span class="mi">5</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        a demo function that raises an exception slowly</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep</span><span class="p">)</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">load_site</span><span class="p">(</span><span class="n">url</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        a demo function that loads the content of a url</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">urllib</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">class</span> <span class="nc">Display</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">        a window to display some content that loads slowly</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">            <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">400</span><span class="p">,</span> <span class="mi">300</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;display&quot;</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">set_border_width</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">func</span> <span class="o">=</span> <span class="n">func</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">vbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">(</span><span class="n">spacing</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
      </span><span class="line">            <span class="n">scroll</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ScrolledWindow</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TextView</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">get_buffer</span><span class="p">()</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">scroll</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">scroll</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">loading</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ProgressBar</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">is_loading</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">loading</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">buttons</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">HButtonBox</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">run</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">stock</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_EXECUTE</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;clicked&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_run_clicked</span><span class="p">)</span>
      </span><span class="line">            <span class="n">buttons</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">buttons</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">vbox</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">vbox</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">loading</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;delete-event&quot;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">_on_run_clicked</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">button</span><span class="p">):</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">set_loading</span><span class="p">()</span>
      </span><span class="line">            <span class="n">GtkRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_result_ready</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span>
      </span><span class="line">                    <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">set_loading</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_loading</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span>
      </span><span class="line">            <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">            set the window to the loading state</span>
      </span><span class="line"><span class="sd">            &#39;&#39;&#39;</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">is_loading</span> <span class="o">=</span> <span class="n">is_loading</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="o">.</span><span class="n">set_sensitive</span><span class="p">(</span><span class="ow">not</span> <span class="n">is_loading</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">if</span> <span class="n">is_loading</span><span class="p">:</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">loading</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">                <span class="n">glib</span><span class="o">.</span><span class="n">timeout_add</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_make_progress_bar_go_crazy</span><span class="p">)</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">loading</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">_on_result_ready</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
      </span><span class="line">            <span class="n">status</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">set_loading</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">if</span> <span class="n">status</span><span class="p">:</span>
      </span><span class="line">                <span class="n">content</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="n">content</span> <span class="o">=</span> <span class="s">&quot;exception running function: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">get_buffer</span><span class="p">()</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">_make_progress_bar_go_crazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_loading</span><span class="p">:</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">loading</span><span class="o">.</span><span class="n">pulse</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_loading</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">threads_init</span><span class="p">()</span>
      </span><span class="line">    <span class="n">Display</span><span class="p">(</span><span class="s">&quot;show text after some seconds&quot;</span><span class="p">,</span> <span class="n">return_slow</span><span class="p">,</span> <span class="s">&quot;I load slowly&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">Display</span><span class="p">(</span><span class="s">&quot;raise an exception after some seconds&quot;</span><span class="p">,</span> <span class="n">fail_slow</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&quot;I fail slowly&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">Display</span><span class="p">(</span><span class="s">&quot;load the content of website&quot;</span><span class="p">,</span> <span class="n">load_site</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&quot;http://marianoguerra.com.ar&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">main</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

