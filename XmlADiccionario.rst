#format rst

Xml a diccionario
-----------------

En este ejemplo se muestra como convertir un string a una estructura de diccionarios y listas anidadas usando expat, tambien se proveen dos clases que permiten manipular el resultado como su fueran objetos.

primero el codigo

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">xml.parsers.expat</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">XmlParser</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a class that parses a xml string an generates a nested </span>
      </span><span class="line"><span class="sd">    dict/list structure</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">parsers</span><span class="o">.</span><span class="n">expat</span><span class="o">.</span><span class="n">ParserCreate</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">buffer_text</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">stack</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">current</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">StartElementHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_element</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">EndElementHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">end_element</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">CharacterDataHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">char_data</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span><span class="o">.</span><span class="n">Parse</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">start_element</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">attrs</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;Start xml element handler&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">current</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">for</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span> <span class="ow">in</span> <span class="n">attrs</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">key</span><span class="p">)]</span> <span class="o">=</span> <span class="n">value</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">[</span><span class="s">&#39;tag&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">name</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">[</span><span class="s">&#39;childs&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">end_element</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;End xml element handler&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">stack</span><span class="p">):</span>
      </span><span class="line">            <span class="n">current</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
      </span><span class="line">            <span class="n">current</span><span class="p">[</span><span class="s">&#39;childs&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">current</span> <span class="o">=</span> <span class="n">current</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">char_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;Char xml element handler.</span>
      </span><span class="line"><span class="sd">        buffer_text is enabled, so this is the whole text element&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">current</span><span class="p">[</span><span class="s">&#39;childs&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">DictObj</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a class that allows to access a dict as an object</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="nb">dict</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__getattribute__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
      </span><span class="line">            <span class="n">obj</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="o">==</span> <span class="nb">dict</span><span class="p">:</span>
      </span><span class="line">                <span class="k">return</span> <span class="n">DictObj</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
      </span><span class="line">            <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="o">==</span> <span class="nb">list</span><span class="p">:</span>
      </span><span class="line">                <span class="k">return</span> <span class="n">ListObj</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
      </span><span class="line">           
      </span><span class="line">            <span class="k">return</span> <span class="n">obj</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">None</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">ListObj</span><span class="p">(</span><span class="nb">list</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a class that allows to access dicts inside a list as objects</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="nb">list</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">            <span class="k">raise</span> <span class="ne">IndexError</span><span class="p">(</span><span class="s">&#39;list index out of range&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">obj</span> <span class="o">=</span> <span class="nb">list</span><span class="o">.</span><span class="n">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="o">==</span> <span class="nb">dict</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">DictObj</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
      </span><span class="line">        <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="o">==</span> <span class="nb">list</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">ListObj</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">obj</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;iterate over the list&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">while</span> <span class="n">count</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">            <span class="k">yield</span> <span class="bp">self</span><span class="p">[</span><span class="n">count</span><span class="p">]</span>
      </span><span class="line">            <span class="n">count</span> <span class="o">+=</span> <span class="mi">1</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">raw_string</span><span class="p">(</span><span class="n">dct_</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;return a string containing just the string parts removing all the </span>
      </span><span class="line"><span class="sd">    xml stuff&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">helper</span><span class="p">(</span><span class="n">dct</span><span class="p">):</span>
      </span><span class="line">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">dct</span><span class="o">.</span><span class="n">childs</span><span class="p">:</span>
      </span><span class="line">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">child</span><span class="p">)</span> <span class="o">==</span> <span class="nb">str</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="n">child</span><span class="p">)</span> <span class="o">==</span> <span class="nb">unicode</span><span class="p">:</span>
      </span><span class="line">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">child</span><span class="p">))</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="n">result</span> <span class="o">=</span> <span class="n">result</span> <span class="o">+</span> <span class="n">helper</span><span class="p">(</span><span class="n">child</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">result</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">helper</span><span class="p">(</span><span class="n">dct_</span><span class="p">))</span>
      </span>

Simplemente creamos un objeto de tipo XmlParser_ pasandole el string y obtenemos el resultado parseado en la variable result.  Si no queremos andar preguntado si las llaves existen antes de accederlas para evitar excepciones podemos usar la clase DictObj_ que nos permite acceder a las llaves como si fueran atributos, las variables que no existan como llaves contendran None. Aca va un ejemplo en la consola interactiva

::

   .. raw:: html
      <span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">XmlParser</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">p</span> <span class="o">=</span> <span class="n">XmlParser</span><span class="o">.</span><span class="n">XmlParser</span><span class="p">(</span><span class="s">&#39;&lt;span&gt;&lt;a href=&quot;google.com&quot;&gt;go&lt;s&gt;o&lt;/s&gt;gle&lt;/a&gt; &lt;i&gt;test&lt;/i&gt; &lt;img src=&quot;foo.png&quot; alt=&quot;foo&quot;/&gt; &lt;u&gt;!&lt;/u&gt;&lt;s&gt;!&lt;/s&gt;&lt;/span&gt;&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">r</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span> <span class="o">=</span> <span class="n">XmlParser</span><span class="o">.</span><span class="n">DictObj</span><span class="p">(</span><span class="n">r</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span>
      </span><span class="line"><span class="go">{&#39;childs&#39;: [{&#39;childs&#39;: [u&#39;go&#39;, {&#39;childs&#39;: [u&#39;o&#39;], &#39;tag&#39;: u&#39;s&#39;}, u&#39;gle&#39;], &#39;href&#39;: u&#39;google.com&#39;, &#39;tag&#39;: u&#39;a&#39;}, u&#39; &#39;, {&#39;childs&#39;: [u&#39;test&#39;], &#39;tag&#39;: u&#39;i&#39;}, u&#39; &#39;, {&#39;childs&#39;: [], &#39;src&#39;: u&#39;foo.png&#39;, &#39;alt&#39;: u&#39;foo&#39;, &#39;tag&#39;: u&#39;img&#39;}, u&#39; &#39;, {&#39;childs&#39;: [u&#39;!&#39;], &#39;tag&#39;: u&#39;u&#39;}, {&#39;childs&#39;: [u&#39;!&#39;], &#39;tag&#39;: u&#39;s&#39;}], &#39;tag&#39;: u&#39;span&#39;}</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span><span class="o">.</span><span class="n">childs</span>
      </span><span class="line"><span class="go">[{&#39;childs&#39;: [u&#39;go&#39;, {&#39;childs&#39;: [u&#39;o&#39;], &#39;tag&#39;: u&#39;s&#39;}, u&#39;gle&#39;], &#39;href&#39;: u&#39;google.com&#39;, &#39;tag&#39;: u&#39;a&#39;}, u&#39; &#39;, {&#39;childs&#39;: [u&#39;test&#39;], &#39;tag&#39;: u&#39;i&#39;}, u&#39; &#39;, {&#39;childs&#39;: [], &#39;src&#39;: u&#39;foo.png&#39;, &#39;alt&#39;: u&#39;foo&#39;, &#39;tag&#39;: u&#39;img&#39;}, u&#39; &#39;, {&#39;childs&#39;: [u&#39;!&#39;], &#39;tag&#39;: u&#39;u&#39;}, {&#39;childs&#39;: [u&#39;!&#39;], &#39;tag&#39;: u&#39;s&#39;}]</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line"><span class="go">{&#39;childs&#39;: [u&#39;go&#39;, {&#39;childs&#39;: [u&#39;o&#39;], &#39;tag&#39;: u&#39;s&#39;}, u&#39;gle&#39;], &#39;href&#39;: u&#39;google.com&#39;, &#39;tag&#39;: u&#39;a&#39;}</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">tag</span>
      </span><span class="line"><span class="go">u&#39;a&#39;</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line"><span class="go">u&#39;go&#39;</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">d</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">childs</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">tag</span>
      </span><span class="line"><span class="go">u&#39;s&#39;</span>
      </span>

.. ############################################################################

.. _XmlParser: ../XmlParser

.. _DictObj: ../DictObj

