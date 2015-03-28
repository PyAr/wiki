#format rst
## page was renamed from Recetario/Gtk/WebkitEditor

Gtk Webkit Editor
=================

ejemplo de como usar webkit para editar paginas HTML como si fuera un editor

para probarlo correlo, entra una direccion que empiece con http://, hace foco en alguna parte de la pagina y ponete a tipear como si fuera un editor de texto comun.

un ejemplo de su uso (tarea del autor encontrar los cambios |;)|

`attachment:webkit.png`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">webkit</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Editor</span><span class="p">(</span><span class="n">webkit</span><span class="o">.</span><span class="n">WebView</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a webkit editor&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="n">webkit</span><span class="o">.</span><span class="n">WebView</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_editable</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">EditorWindow</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;the editor window&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;webkit editor&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">800</span><span class="p">,</span> <span class="mi">600</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">entry</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">entry</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="s">&quot;http://webkit.org&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">entry</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;activate&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_entry_activate</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">editor</span> <span class="o">=</span> <span class="n">Editor</span><span class="p">()</span>
      </span><span class="line">        <span class="n">scroll</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ScrolledWindow</span><span class="p">()</span>
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">set_policy</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">POLICY_AUTOMATIC</span><span class="p">)</span>
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">set_shadow_type</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">SHADOW_IN</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">scroll</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">editor</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">vbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">()</span>
      </span><span class="line">        <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entry</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
      </span><span class="line">        <span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">scroll</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">vbox</span><span class="p">)</span>
      </span><span class="line">        <span class="n">vbox</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;load the given url in the editor and set it to editable&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">editor</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_on_entry_activate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entry</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;callback called when the user hits enter on the entry&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">entry</span><span class="o">.</span><span class="n">get_text</span><span class="p">())</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">window</span> <span class="o">=</span> <span class="n">EditorWindow</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">entry</span><span class="o">.</span><span class="n">activate</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

Tengan en cuenta que en Ubuntu inferior 10.04 python-webkit en gtk nececita SI o SI llamar a "gtk.gdk.threads_init()", si no tira error:

::

   GLib-ERROR **: The thread system is not yet initialized.
   aborting...
   Cancelado

Entonces deberan agregar un "gtk.gdk.threads_init()" antes de llamar a "EditorWindow_()", el final del codigo les quedara de la siguiente manera:

::

   .. raw:: html
      <span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">threads_init</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span> <span class="o">=</span> <span class="n">EditorWindow</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">entry</span><span class="o">.</span><span class="n">activate</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

