#format rst

Gtk Browser Con Web Inspector
-----------------------------

esta receta va mas alla del "navegador en python en N lineas" (donde N < 30)

en este caso vemos como agregar el web inspector para inspeccionar y debuggear la pagina que estamos viendo

el resultado al principio es algo asi:

`attachment:brser1.png`_

luego de hacer click derecho en la pagina y hacer click en "Inspect Element" tenemos algo asi:

`attachment:brser2.png`_

el codigo:

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">webkit</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Browser</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">):</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">view</span> <span class="o">=</span> <span class="n">webkit</span><span class="o">.</span><span class="n">WebView</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&#39;Browser&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">scroll</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ScrolledWindow</span><span class="p">()</span>
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">set_policy</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">)</span>
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">set_shadow_type</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">SHADOW_IN</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">view</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">vbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">entry</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span>
      </span><span class="line">        <span class="n">entry</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_url_changed</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">:</span>
      </span><span class="line">            <span class="n">entry</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">entry</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">        <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">scroll</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">panels</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VPaned</span><span class="p">()</span>
      </span><span class="line">        <span class="n">panels</span><span class="o">.</span><span class="n">add1</span><span class="p">(</span><span class="n">vbox</span><span class="p">)</span>
      </span><span class="line">        <span class="n">panels</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">settings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">view</span><span class="o">.</span><span class="n">get_settings</span><span class="p">()</span>
      </span><span class="line">        <span class="n">settings</span><span class="o">.</span><span class="n">set_property</span><span class="p">(</span><span class="s">&quot;enable-developer-extras&quot;</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">def</span> <span class="nf">activate_inspector</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
      </span><span class="line">            <span class="n">view</span> <span class="o">=</span> <span class="n">webkit</span><span class="o">.</span><span class="n">WebView</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">            <span class="n">panels</span><span class="o">.</span><span class="n">add2</span><span class="p">(</span><span class="n">view</span><span class="p">)</span>
      </span><span class="line">            <span class="n">panels</span><span class="o">.</span><span class="n">set_position</span><span class="p">(</span><span class="n">panels</span><span class="o">.</span><span class="n">get_allocation</span><span class="p">()</span><span class="o">.</span><span class="n">height</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
      </span><span class="line">            <span class="n">view</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">return</span> <span class="n">view</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">inspector</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">view</span><span class="o">.</span><span class="n">get_web_inspector</span><span class="p">()</span>
      </span><span class="line">        <span class="n">inspector</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;inspect-web-view&quot;</span><span class="p">,</span> <span class="n">activate_inspector</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">panels</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="k">lambda</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">open</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="ow">not</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;http://&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">url</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;https://&#39;</span><span class="p">):</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="s">&#39;http://&#39;</span> <span class="o">+</span> <span class="n">url</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">view</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_on_url_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entry</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;called when the url changes&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">url</span> <span class="o">=</span> <span class="n">entry</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">browser</span> <span class="o">=</span> <span class="n">Browser</span><span class="p">(</span><span class="s">&#39;www.google.com/search?q=python%20argentina&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">browser</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

