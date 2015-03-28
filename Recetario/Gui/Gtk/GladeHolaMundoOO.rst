
GtkGladeHolaMundoOO
-------------------

ejemplo que carga la interfaz de un archivo .glade y lo muestra, el archivo .glade puede tener cualquier contenido mientras la ventana tenga el nombre "ventana"

gtk-glade-holamundo.glade
~~~~~~~~~~~~~~~~~~~~~~~~~

copiar el contenido siguiente a un archivo llamado **gtk-glade-holamundo.glade** el archivo fue editado con glade-3_.

::

   .. raw:: html
      <span class="line"><span class="cp">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;no&quot;?&gt;</span>
      </span><span class="line"><span class="cp">&lt;!DOCTYPE glade-interface SYSTEM &quot;glade-2.0.dtd&quot;&gt;</span>
      </span><span class="line"><span class="c">&lt;!--Generated with glade3 3.4.2 on Sat May 10 01:13:03 2008 --&gt;</span>
      </span><span class="line"><span class="nt">&lt;glade-interface&gt;</span>
      </span><span class="line">  <span class="nt">&lt;widget</span> <span class="na">class=</span><span class="s">&quot;GtkWindow&quot;</span> <span class="na">id=</span><span class="s">&quot;ventana&quot;</span><span class="nt">&gt;</span>
      </span><span class="line">    <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;title&quot;</span> <span class="na">translatable=</span><span class="s">&quot;yes&quot;</span><span class="nt">&gt;</span>hola mundo glade<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">    <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;window_position&quot;</span><span class="nt">&gt;</span>GTK_WIN_POS_CENTER<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">    <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;default_width&quot;</span><span class="nt">&gt;</span>200<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">    <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;default_height&quot;</span><span class="nt">&gt;</span>200<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">    <span class="nt">&lt;signal</span> <span class="na">name=</span><span class="s">&quot;delete_event&quot;</span> <span class="na">handler=</span><span class="s">&quot;on_ventana_delete_event&quot;</span><span class="nt">/&gt;</span>
      </span><span class="line">    <span class="nt">&lt;child&gt;</span>
      </span><span class="line">      <span class="nt">&lt;widget</span> <span class="na">class=</span><span class="s">&quot;GtkLabel&quot;</span> <span class="na">id=</span><span class="s">&quot;label&quot;</span><span class="nt">&gt;</span>
      </span><span class="line">        <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;visible&quot;</span><span class="nt">&gt;</span>True<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">        <span class="nt">&lt;property</span> <span class="na">name=</span><span class="s">&quot;label&quot;</span> <span class="na">translatable=</span><span class="s">&quot;yes&quot;</span><span class="nt">&gt;</span>hola pyar!<span class="nt">&lt;/property&gt;</span>
      </span><span class="line">      <span class="nt">&lt;/widget&gt;</span>
      </span><span class="line">    <span class="nt">&lt;/child&gt;</span>
      </span><span class="line">  <span class="nt">&lt;/widget&gt;</span>
      </span><span class="line"><span class="nt">&lt;/glade-interface&gt;</span>
      </span>

el codigo para el ejemplo es el siguiente

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk.glade</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">HolaMundo</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;clase que muestra un hola mundo desde un archivo glade&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">glade</span><span class="o">.</span><span class="n">XML</span><span class="p">(</span><span class="s">&quot;gtk-glade-holamundo.glade&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">signal_autoconnect</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="o">.</span><span class="n">get_widget</span><span class="p">(</span><span class="s">&quot;ventana&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_ventana_delete_event</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">window</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;callback llamado cuando se cierra la ventana&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">show</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;muestra la ventana principal&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">hola</span> <span class="o">=</span> <span class="n">HolaMundo</span><span class="p">()</span>
      </span><span class="line">    <span class="n">hola</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

.. ############################################################################

.. _glade-3: http://glade.gnome.org/

