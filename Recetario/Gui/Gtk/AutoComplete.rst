#format rst
## page was renamed from Recetario/Gtk/AutoComplete

Gtk Auto Complete
=================

ejemplo de campo de texto con auto complesion

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Complete</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a class to autocomplete&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">words</span><span class="p">):</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">completion</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">EntryCompletion</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">set_completion</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">completion</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">model</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ListStore</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">completion</span><span class="o">.</span><span class="n">set_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">completion</span><span class="o">.</span><span class="n">set_text_column</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">remember</span><span class="p">(</span><span class="n">word</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">remember</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;add a value to the list of strings to suggest&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">value</span><span class="p">])</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line">    <span class="n">complete</span> <span class="o">=</span> <span class="n">Complete</span><span class="p">(</span><span class="s">&quot;python&quot;</span><span class="p">,</span> <span class="s">&quot;pyar&quot;</span><span class="p">,</span> <span class="s">&quot;span&quot;</span><span class="p">,</span> <span class="s">&quot;eggs&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">complete</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

