#format rst

¿Como iterar por ejemplo la secuencia [1,2,3,4,5,6] para que cada item sea: (1,2), (3,4), (5,6)?

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">seq</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="mi">7</span><span class="p">]</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">i</span> <span class="o">=</span> <span class="nb">iter</span><span class="p">(</span><span class="n">seq</span><span class="p">)</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">i</span><span class="p">):</span>
      </span><span class="line"><span class="o">...</span>     <span class="k">print</span> <span class="n">x</span>
      </span><span class="line"><span class="o">...</span>
      </span><span class="line"><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
      </span><span class="line"><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
      </span><span class="line"><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">)</span>
      </span>

