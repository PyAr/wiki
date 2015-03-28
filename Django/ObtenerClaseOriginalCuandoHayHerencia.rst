#format rst

Si usamos herencia normal de modelos (no abstracta), se vuelve difícil obtener el objeto original de la base de datos cuando sólo tenemos una referencia a un ancestro (esto pasa a menudo cuando tenemos relaciones a un modelo que fue derivado). Este cacho de código define una clase abstracta ``SubclassedModel``, cuyos descendientes tienen en ``objects`` un Manager por defecto que devuelve directamente objetos de la clase con la que fueron creados.

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">django.db</span> <span class="kn">import</span> <span class="n">models</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">django.db.models.query</span> <span class="kn">import</span> <span class="n">QuerySet</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">django.contrib.contenttypes.models</span> <span class="kn">import</span> <span class="n">ContentType</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">_as_original_class</span><span class="p">(</span><span class="n">inst</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">    Returns the instance that corresponds to `inst`</span>
      </span><span class="line"><span class="sd">    in its original class.</span>
      </span><span class="line"><span class="sd">    &quot;&quot;&quot;</span>
      </span><span class="line">    <span class="n">model</span> <span class="o">=</span> <span class="n">inst</span><span class="o">.</span><span class="n">content_type</span><span class="o">.</span><span class="n">model_class</span><span class="p">()</span>
      </span><span class="line">    <span class="k">if</span> <span class="p">(</span><span class="n">model</span> <span class="o">==</span> <span class="n">inst</span><span class="o">.</span><span class="n">__class__</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">inst</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">model</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">inst</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">OriginalClassQuerySet</span><span class="p">(</span><span class="n">QuerySet</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">    A QuerySet that returns original classes.</span>
      </span><span class="line"><span class="sd">    &quot;&quot;&quot;</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">k</span><span class="p">):</span>
      </span><span class="line">        <span class="n">result</span> <span class="o">=</span> <span class="nb">super</span><span class="p">(</span><span class="n">OriginalClassQuerySet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__getitem__</span><span class="p">(</span><span class="n">k</span><span class="p">)</span>
      </span><span class="line">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">_as_original_class</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">result</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="nb">super</span><span class="p">(</span><span class="n">OriginalClassQuerySet</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__iter__</span><span class="p">():</span>
      </span><span class="line">            <span class="k">yield</span> <span class="n">_as_original_class</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">OriginalClassManager</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">Manager</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">    A Manager that fetches original classes.</span>
      </span><span class="line"><span class="sd">    &quot;&quot;&quot;</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">get_query_set</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">OriginalClassQuerySet</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">SubclassedModel</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span>
      </span><span class="line">    <span class="n">content_type</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">ForeignKey</span><span class="p">(</span><span class="n">ContentType</span><span class="p">,</span> <span class="n">editable</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">null</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">objects</span> <span class="o">=</span> <span class="n">OriginalClassManager</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">class</span> <span class="nc">Meta</span><span class="p">:</span>
      </span><span class="line">        <span class="n">abstract</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">save</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span><span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_type</span><span class="p">):</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">content_type</span> <span class="o">=</span> \
      </span><span class="line">                <span class="n">ContentType</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get_for_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">)</span>
      </span><span class="line">            <span class="nb">super</span><span class="p">(</span><span class="n">SubclassedModel</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
      </span>

Para usarlo, supongamos el siguente ``models.py`` en la app ``example``:

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">django.db</span> <span class="kn">import</span> <span class="n">models</span>
      </span><span class="line"><span class="kn">from</span> <span class="err">&lt;</span><span class="nn">el</span><span class="err"> </span><span class="nn">m</span><span class="err">ó</span><span class="nn">dulo</span><span class="err"> </span><span class="nn">de</span><span class="err"> </span><span class="nn">arriba</span><span class="err">&gt;</span> <span class="kn">import</span> <span class="n">SubclassedModel</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Foo</span><span class="p">(</span><span class="n">SubclassedModel</span><span class="p">):</span>
      </span><span class="line">    <span class="p">[</span><span class="o">...</span><span class="p">]</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;A Foo&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Bar</span><span class="p">(</span><span class="n">Foo</span><span class="p">):</span>
      </span><span class="line">    <span class="p">[</span><span class="o">...</span><span class="p">]</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;A Bar&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Baz</span><span class="p">(</span><span class="n">Foo</span><span class="p">):</span>
      </span><span class="line">    <span class="p">[</span><span class="o">...</span><span class="p">]</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;A Baz&quot;</span>
      </span>

Entonces:

::

   .. raw:: html
      <span class="line"><span class="go">$ django-admin.py shell --settings=&lt;nombre del proyecto&gt;.settings</span>
      </span><span class="line"><span class="go">Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56) </span>
      </span><span class="line"><span class="go">[GCC 4.4.3] on linux2</span>
      </span><span class="line"><span class="go">Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.</span>
      </span><span class="line"><span class="go">(InteractiveConsole)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">example</span> <span class="kn">import</span> <span class="n">models</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">bar_instance</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">Bar</span><span class="p">([</span><span class="o">...</span><span class="p">])</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">bar_instance</span><span class="o">.</span><span class="n">save</span><span class="p">()</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">baz_instance</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">Baz</span><span class="p">([</span><span class="o">...</span><span class="p">])</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">baz_instance</span><span class="o">.</span><span class="n">save</span><span class="p">()</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">foo_instance</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">Foo</span><span class="p">([</span><span class="o">...</span><span class="p">])</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">foo_instance</span><span class="o">.</span><span class="n">save</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">l</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">Foo</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">l</span>
      </span><span class="line"><span class="go">[&lt;A Bar&gt;, &lt;A Baz&gt;, &lt;A Foo&gt;]</span>
      </span>

OJO: este mecanismo deshabilita el feature de Django según el cual un modelo no tiene un Manager por defecto cuando tiene cualquier Manager explícito. Se me ocurre que eso puede romper algo en subclases de ``SubclassedModel`` si uno no lo tiene en cuenta.

