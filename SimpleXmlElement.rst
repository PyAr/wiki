#format rst

Manejo simple de xml (SimpleXMLElement)
---------------------------------------

En este ejemplo se muestra como convertir un string desde y hacia un objeto simple que representa el XML (código usado en `Factura Electronica`_)

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">xml.dom.minidom</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">SimpleXMLElement</span><span class="p">:</span>
      </span><span class="line">    <span class="s">&quot;Clase para Manejo simple de XMLs (simil PHP)&quot;</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">element</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">document</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">text</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">__document</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">dom</span><span class="o">.</span><span class="n">minidom</span><span class="o">.</span><span class="n">parseString</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">__element</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__document</span><span class="o">.</span><span class="n">documentElement</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">__element</span> <span class="o">=</span> <span class="n">element</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">__document</span> <span class="o">=</span> <span class="n">document</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">addChild</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">tag</span><span class="p">,</span><span class="n">text</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="n">element</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__document</span><span class="o">.</span><span class="n">createElement</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">text</span><span class="p">:</span>
      </span><span class="line">            <span class="n">element</span><span class="o">.</span><span class="n">appendChild</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__document</span><span class="o">.</span><span class="n">createTextNode</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">text</span><span class="p">)))</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">__element</span><span class="o">.</span><span class="n">appendChild</span><span class="p">(</span><span class="n">element</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">asXML</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">filename</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__document</span><span class="o">.</span><span class="n">toxml</span><span class="p">(</span><span class="s">&#39;utf8&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">tag</span><span class="p">):</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">SimpleXMLElement</span><span class="p">(</span>
      </span><span class="line">                <span class="n">element</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">__element</span><span class="o">.</span><span class="n">getElementsByTagName</span><span class="p">(</span><span class="n">tag</span><span class="p">)[</span><span class="mi">0</span><span class="p">],</span>
      </span><span class="line">                <span class="n">document</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">__document</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span><span class="p">:</span>
      </span><span class="line">            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;Tag not found: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">tag</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">item</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">item</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__contains__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__element</span><span class="o">.</span><span class="n">getElementsByTagName</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__unicode__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__element</span><span class="o">.</span><span class="n">childNodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">data</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__element</span><span class="o">.</span><span class="n">childNodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;utf8&quot;</span><span class="p">,</span><span class="s">&quot;ignore&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__str__</span><span class="p">())</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__int__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__str__</span><span class="p">())</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__float__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">return</span> <span class="nb">float</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__str__</span><span class="p">())</span>
      </span>

Simplemente creamos un objeto de tipo SimpleXmlElement pasandole el string y obtenemos el objeto parseado. Se puede:

* Acceder por item (como si fuera un dict) 

* Acceder por atributo (como si fuera un objeto)

* Preguntar con ``in`` si un tag es hijo

* Al acceder se devuelven elementos xml, por lo que hay que convertirlos a ``str``, ``int``, ``float``, etc.

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="kn">from</span> <span class="nn">simplexmlelement</span> <span class="kn">import</span> <span class="n">SimpleXMLElement</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">span</span> <span class="o">=</span> <span class="n">SimpleXMLElement</span><span class="p">(</span><span class="s">&#39;&lt;span&gt;&lt;a href=&quot;google.com&quot;&gt;google&lt;/a&gt;&lt;prueba&gt;&lt;i&gt;1&lt;/i&gt;&lt;float&gt;1.5&lt;/float&gt;&lt;/prueba&gt;&lt;/span&gt;&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">a</span><span class="p">)</span>
      </span><span class="line"><span class="n">google</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="nb">float</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">prueba</span><span class="o">.</span><span class="n">i</span><span class="p">)</span>
      </span><span class="line"><span class="mi">1</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="nb">float</span><span class="p">(</span><span class="n">span</span><span class="o">.</span><span class="n">prueba</span><span class="o">.</span><span class="n">float</span><span class="p">)</span>
      </span><span class="line"><span class="mf">1.5</span>
      </span>

Faltaría:

* Acceder a los atributos de los tags (quizas por item simil diccionario o via ``attributes()`` y ``addAttribute()``)

* Soportar más de un tag hijo (implementar ``__iter__``)

.. ############################################################################

.. _Factura Electronica: http://www.nsis.com.ar/public/browser/pyafip/ws/php.py

