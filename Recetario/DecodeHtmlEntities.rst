#format rst

Decodificar entities de HTML
============================

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">re</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">htmlentitydefs</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">unescape</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&quot;UTF-8&quot;</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">    Removes HTML or XML character references and entities from a text string.</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">    @param text The HTML (or XML) source text.</span>
      </span><span class="line"><span class="sd">    @return The unescaped text as a Unicode.</span>
      </span><span class="line"><span class="sd">    &quot;&quot;&quot;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">fixup</span><span class="p">(</span><span class="n">m</span><span class="p">):</span>
      </span><span class="line">        <span class="n">text</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">text</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;&amp;#&quot;</span><span class="p">:</span>
      </span><span class="line">            <span class="c"># character reference</span>
      </span><span class="line">            <span class="k">try</span><span class="p">:</span>
      </span><span class="line">                <span class="k">if</span> <span class="n">text</span><span class="p">[:</span><span class="mi">3</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;&amp;#x&quot;</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">text</span> <span class="o">=</span> <span class="nb">unichr</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">text</span><span class="p">[</span><span class="mi">3</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="mi">16</span><span class="p">))</span>
      </span><span class="line">                <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">text</span> <span class="o">=</span> <span class="nb">unichr</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">text</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]))</span>
      </span><span class="line">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
      </span><span class="line">                <span class="k">pass</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="c"># named entity</span>
      </span><span class="line">            <span class="k">try</span><span class="p">:</span>
      </span><span class="line">                <span class="n">text</span> <span class="o">=</span> <span class="nb">unichr</span><span class="p">(</span><span class="n">htmlentitydefs</span><span class="o">.</span><span class="n">name2codepoint</span><span class="p">[</span><span class="n">text</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]])</span>
      </span><span class="line">            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
      </span><span class="line">                <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">text</span>
      </span><span class="line">
      </span><span class="line">    <span class="c"># Decode string as needed</span>
      </span><span class="line">    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="k">else</span> <span class="n">text</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">text</span> <span class="ow">and</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&quot;&amp;#?\w+;&quot;</span><span class="p">,</span> <span class="n">fixup</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
      </span>

Gracias Martin Conte Mac Donell! |;)|

-------------------------



  CategoryRecetas_

