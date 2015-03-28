#format rst

Votación PyCamp 2013
--------------------

El resultado de la votación fue:

::

      84 Hotel Luz y Fuerza
      75 Hostal Colonial Serrano
      72 Verónica
      47 Villa Maristas Lujan
      24 Villa Maristas Mar del Plata

Estas fueron las votaciones en detalle:

::

   Facundo Batista
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Lujan
   Hotel Luz y Fuerza

   Daniel F. Moisset
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Sergio Schvezov
   Hotel Luz y Fuerza
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano

   Alejandro J. Cura
   Hostal Colonial Serrano
   Verónica
   Hotel Luz y Fuerza

   Emiliano Dalla Verde Marcozzi
   Hostal Colonial Serrano
   Hotel Luz y Fuerza
   Verónica

   Marcos Vanetta
   Villa Maristas Lujan
   Verónica
   Hotel Luz y Fuerza

   Natalia Bidart
   Hostal Colonial Serrano
   Hotel Luz y Fuerza
   Villa Maristas Lujan

   Juan Pedro Fisanotti
   Villa Maristas Lujan
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Erwin Feser
   Hostal Colonial Serrano
   Hotel Luz y Fuerza

   Juan A. Diaz
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano
   Hotel Luz y Fuerza

   Hernan Lozano
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Mar del Plata

   Agustin Henze
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Santiago Piccinini
   Villa Maristas Lujan
   Verónica

   Diego Sarmentero
   Hostal Colonial Serrano
   Verónica
   Hotel Luz y Fuerza

   Jairo Trad
   Verónica
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano

   Pablo Mouzo
   Verónica
   Villa Maristas Lujan

   Federico M. Peretti
   Verónica
   Villa Maristas Lujan
   Villa Maristas Mar del Plata

   Matías Bordese
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Leandro Nahuel Roque Poblet
   Hotel Luz y Fuerza
   Villa Maristas Lujan
   Verónica

   Ricardo Kirkner
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Lujan

   Sanchez Héctor
   Verónica
   Villa Maristas Mar del Plata
   Villa Maristas Lujan

   Francisco Capdevila
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Villa Maristas Lujan

   Elías Andrawos
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Villa Maristas Lujan
   Villa Maristas Mar del Plata
   Verónica

   Felipe Lerena
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Claudio Canepa
   Verónica
   Hotel Luz y Fuerza
   Villa Maristas Lujan

Las cuales se evaluaron con el siguiente script:

::

   .. raw:: html
      <span class="line"><span class="c"># ¡Py3!</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">operator</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># this is the total number of possibilites open to vote</span>
      </span><span class="line"><span class="n">TOP_SCORE</span> <span class="o">=</span> <span class="mi">5</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">ResultCalculator</span><span class="p">:</span>
      </span><span class="line">    <span class="sd">&quot;&quot;&quot;Calculate the voting result.&quot;&quot;&quot;</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_count</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">vote</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;Feed the voting blocks.&quot;&quot;&quot;</span>
      </span><span class="line">        <span class="c"># first line is a header, the rest are votes</span>
      </span><span class="line">        <span class="n">votes</span> <span class="o">=</span> <span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
      </span><span class="line">
      </span><span class="line">        <span class="c"># score are descending</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">place</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">votes</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="n">TOP_SCORE</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)):</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">_count</span><span class="p">[</span><span class="n">place</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_count</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">place</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="o">+</span> <span class="n">score</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">print_result</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;Show the result.&quot;&quot;&quot;</span>
      </span><span class="line">        <span class="n">result</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_count</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span>
      </span><span class="line">                        <span class="n">key</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">itemgetter</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">place</span><span class="p">,</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
      </span><span class="line">            <span class="k">print</span><span class="p">(</span><span class="s">&quot;{:5d} {}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">score</span><span class="p">,</span> <span class="n">place</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line"><span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;voto_pycamp.txt&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&quot;utf8&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
      </span><span class="line">    <span class="n">block</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">    <span class="n">rc</span> <span class="o">=</span> <span class="n">ResultCalculator</span><span class="p">()</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">fh</span><span class="p">:</span>
      </span><span class="line">        <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">line</span><span class="p">:</span>
      </span><span class="line">            <span class="n">block</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="c"># empty line: block delimiter</span>
      </span><span class="line">            <span class="n">rc</span><span class="o">.</span><span class="n">vote</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
      </span><span class="line">            <span class="n">block</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">    <span class="n">rc</span><span class="o">.</span><span class="n">vote</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span><span class="p">(</span><span class="s">&quot;Resultado:&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">rc</span><span class="o">.</span><span class="n">print_result</span><span class="p">()</span>
      </span>

