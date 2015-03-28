
Mini space invaders
-------------------

Un mini space invaders usando caracteres, la nave dispara a quemarropas en una lucha contra el bicho, nadie sabe cuanto durará esta cacería, que lo disfruten:

* La nave y el bicho se mueven solos de forma aleatoria.

* La nave dispara de forma aleatoria.

* Todo esta en un spanglish feo.

* Se podría agregar manejo de eventos de teclado para manejar la nave y los disparos. Alguna idea usando módulo estándar de python?

* En cuanto pueda pongo un videito.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">random</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="n">ROWS</span> <span class="o">=</span> <span class="mi">14</span>
      </span><span class="line"><span class="n">COLS</span> <span class="o">=</span> <span class="mi">16</span>
      </span><span class="line"><span class="n">BULLET</span> <span class="o">=</span> <span class="s">&#39;.&#39;</span>
      </span><span class="line"><span class="n">SHOTS</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line"><span class="n">SCREEN</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line"><span class="n">EMPTY</span> <span class="o">=</span> <span class="s">&#39; &#39;</span>
      </span><span class="line"><span class="n">EXPLOSION</span> <span class="o">=</span> <span class="s">&#39;#&#39;</span>
      </span><span class="line"><span class="n">SHIP</span> <span class="o">=</span> <span class="s">&#39;A&#39;</span>
      </span><span class="line"><span class="n">BUG</span> <span class="o">=</span> <span class="s">&#39;W&#39;</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="c"># Funciones del mundo</span>
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">crear_mapa</span><span class="p">():</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">ROWS</span><span class="p">):</span>
      </span><span class="line">        <span class="n">SCREEN</span><span class="o">.</span><span class="n">append</span><span class="p">([])</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">COLS</span><span class="p">):</span>
      </span><span class="line">            <span class="n">SCREEN</span><span class="p">[</span><span class="n">row</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">EMPTY</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">mostrar_mapa</span><span class="p">():</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">SCREEN</span><span class="p">:</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">row</span><span class="p">:</span>
      </span><span class="line">            <span class="k">print</span> <span class="n">col</span><span class="p">,</span>
      </span><span class="line">        <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">mover_disparos</span><span class="p">():</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">disparo</span> <span class="ow">in</span> <span class="n">SHOTS</span><span class="p">:</span>
      </span><span class="line">        <span class="n">SCREEN</span><span class="p">[</span><span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]][</span><span class="n">disparo</span><span class="p">[</span><span class="mi">1</span><span class="p">]]</span> <span class="o">=</span> <span class="n">EMPTY</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">SCREEN</span><span class="p">[</span><span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="mi">1</span><span class="p">][</span><span class="n">disparo</span><span class="p">[</span><span class="mi">1</span><span class="p">]]</span> <span class="o">==</span> <span class="n">BUG</span><span class="p">:</span>
      </span><span class="line">                <span class="n">SCREEN</span><span class="p">[</span><span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="mi">1</span><span class="p">][</span><span class="n">disparo</span><span class="p">[</span><span class="mi">1</span><span class="p">]]</span> <span class="o">=</span> <span class="n">EXPLOSION</span>
      </span><span class="line">                <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="n">SCREEN</span><span class="p">[</span><span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="mi">1</span><span class="p">][</span><span class="n">disparo</span><span class="p">[</span><span class="mi">1</span><span class="p">]]</span> <span class="o">=</span> <span class="n">BULLET</span>
      </span><span class="line">                <span class="n">SHOTS</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">disparo</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">disparo</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
      </span><span class="line">        <span class="n">SHOTS</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">disparo</span><span class="p">)</span>
      </span><span class="line">    <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">_mover_nave</span><span class="p">(</span><span class="n">direccion</span><span class="p">,</span> <span class="n">nave</span><span class="p">,</span> <span class="n">row</span><span class="p">):</span>
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">col</span> <span class="o">=</span> <span class="n">SCREEN</span><span class="p">[</span><span class="n">row</span><span class="p">]</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">nave</span><span class="p">)</span>
      </span><span class="line">    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
      </span><span class="line">            <span class="n">col</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="n">SCREEN</span><span class="p">[</span><span class="n">row</span><span class="p">][</span><span class="n">col</span><span class="p">]</span> <span class="o">=</span> <span class="n">EMPTY</span>
      </span><span class="line">    <span class="n">next_col</span> <span class="o">=</span> <span class="n">col</span> <span class="o">+</span> <span class="p">(</span><span class="mi">1</span> <span class="o">*</span> <span class="n">direccion</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">next_col</span> <span class="o">&gt;</span> <span class="mi">15</span><span class="p">:</span>
      </span><span class="line">        <span class="n">next_col</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="n">SCREEN</span><span class="p">[</span><span class="n">row</span><span class="p">][</span><span class="n">next_col</span><span class="p">]</span> <span class="o">=</span> <span class="n">nave</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">limpiar_pantalla</span><span class="p">():</span>
      </span><span class="line">    <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">([</span><span class="s">&#39;clear&#39;</span><span class="p">,</span> <span class="s">&#39;cls&#39;</span><span class="p">][</span><span class="n">os</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;nt&#39;</span><span class="p">])</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="c"># Funciones para la nave</span>
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">crear_nave</span><span class="p">():</span>
      </span><span class="line">    <span class="n">SCREEN</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">COLS</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)]</span> <span class="o">=</span> <span class="n">SHIP</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">mover_nave</span><span class="p">():</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">50</span><span class="p">:</span>
      </span><span class="line">        <span class="n">_mover_nave</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">SHIP</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">_mover_nave</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">SHIP</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">disparar</span><span class="p">():</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">70</span><span class="p">:</span>
      </span><span class="line">        <span class="n">col</span> <span class="o">=</span> <span class="n">SCREEN</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">SHIP</span><span class="p">)</span>
      </span><span class="line">        <span class="n">SCREEN</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">][</span><span class="n">col</span><span class="p">]</span> <span class="o">=</span> <span class="n">BULLET</span>
      </span><span class="line">        <span class="n">row</span> <span class="o">=</span> <span class="n">ROWS</span> <span class="o">-</span> <span class="mi">2</span>
      </span><span class="line">        <span class="n">SHOTS</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">row</span><span class="p">,</span> <span class="n">col</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="c"># Funciones para el bicho</span>
      </span><span class="line"><span class="c">###############################################################################</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">crear_bicho</span><span class="p">():</span>
      </span><span class="line">    <span class="n">SCREEN</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">COLS</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)]</span> <span class="o">=</span> <span class="n">BUG</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">mover_bicho</span><span class="p">():</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">50</span><span class="p">:</span>
      </span><span class="line">        <span class="n">_mover_nave</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">BUG</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">_mover_nave</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">BUG</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">jugar</span><span class="p">():</span>
      </span><span class="line">    <span class="n">crear_mapa</span><span class="p">()</span>
      </span><span class="line">    <span class="n">crear_nave</span><span class="p">()</span>
      </span><span class="line">    <span class="n">crear_bicho</span><span class="p">()</span>
      </span><span class="line">    <span class="k">while</span> <span class="n">mover_disparos</span><span class="p">():</span>
      </span><span class="line">        <span class="n">mover_bicho</span><span class="p">()</span>
      </span><span class="line">        <span class="n">disparar</span><span class="p">()</span>
      </span><span class="line">        <span class="n">mover_nave</span><span class="p">()</span>
      </span><span class="line">        <span class="n">mostrar_mapa</span><span class="p">()</span>
      </span><span class="line">        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.2</span><span class="p">)</span>
      </span><span class="line">        <span class="n">limpiar_pantalla</span><span class="p">()</span>
      </span><span class="line">    <span class="n">limpiar_pantalla</span><span class="p">()</span>
      </span><span class="line">    <span class="n">mostrar_mapa</span><span class="p">()</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;EL BICHO SE MURIO&quot;</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">jugar</span><span class="p">()</span>
      </span>

