#format rst

Interceptar Prints
------------------

Esto sirve para modificar los strings que se vayan a imprimir, por ejemplo para agregarles un timestamp o algo similar. En este ejemplo lo usamos para redefinir "2" y "4". Probado en Python 2 y Python 3.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">FakeStdout</span><span class="p">:</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span>
      </span><span class="line">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;2&quot;</span><span class="p">,</span> <span class="s">&quot;3&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;4&quot;</span><span class="p">,</span> <span class="s">&quot;6&quot;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">real_stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="n">real_stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">real_stdout</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span>
      </span><span class="line"><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="n">FakeStdout</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">print</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
      </span><span class="line"><span class="k">print</span><span class="p">(</span><span class="mi">2</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span>
      </span>

