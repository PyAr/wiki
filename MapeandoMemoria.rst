#format rst

Mapeando Memoria
================

Las funciones de abajo utilizan heapy_ para generar una descripción visual (en ascii) de la memoria, junto con otras estadísticas.

*heapStats* devuelve un diccionario pickleado, que es útil para guardarlo en un archivo para posterior análisis por ejemplo, o para ser transmitido por algún protocolo de red, como xmlrpc o http, puesto que suele utilizarse dentro de un demonio de servidor.

En los datos generados, *"byclodo"* significa que son datos agrupados por *CLass Or Dictionary Owner*, lo que suele decirnos con bastante precisión quién es el culpable de mantener vivos los objetos. *"byrcs"* significa que se agrupan los datos por *Referrer Classification Set*, que significa el "clodo" del referente, útil para detectar referencias cíclicas por ejemplo.

Finalmente, memmap tiene el mapa de la memoria, y el detalle por si se quiere generar mapas más detallados o con diferente visualización.

Probablemente para un uso concreto sea necesario extender memmap antes del memmap.sort(), agregando buffers específicos de la aplicación que no caigan dentro de lo consumido por python. Por ejemplo, los objetos mmap tienen asociados grandes pedazos de memoria que no aparecerían en el mapa, y si se usan mucho en la aplicación convendría incluirlos, o buffers significativos utilizados por bibliotecas de extensión.

Este código sólo funciona en CPython, puesto que utiliza el hecho de que id() devuelve la dirección en memoria de un objeto. Eso no es cierto en Jython, PyPy y muchas otras implementaciones.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">cPickle</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">guppy</span> <span class="kn">import</span> <span class="n">hpy</span> <span class="k">as</span> <span class="n">heapy</span>
      </span><span class="line"><span class="n">_heapy</span> <span class="o">=</span> <span class="n">heapy</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">report_memmap</span><span class="p">(</span><span class="n">mm</span><span class="p">):</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">re</span>
      </span><span class="line">    <span class="kn">from</span> <span class="nn">bisect</span> <span class="kn">import</span> <span class="n">bisect_left</span><span class="p">,</span> <span class="n">bisect_right</span>
      </span><span class="line">   
      </span><span class="line">    <span class="n">mxsz</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span> <span class="n">s</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span> <span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">usage</span><span class="p">(</span><span class="n">mn</span><span class="p">,</span><span class="n">mx</span><span class="p">,</span><span class="n">mxsz</span><span class="p">):</span>
      </span><span class="line">        <span class="n">rv</span> <span class="o">=</span> <span class="s">&#39; &#39;</span>
      </span><span class="line">        <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span><span class="p">[</span><span class="n">bisect_left</span><span class="p">(</span><span class="n">mm</span><span class="p">,(</span><span class="n">mn</span><span class="o">-</span><span class="n">mxsz</span><span class="o">-</span><span class="mi">16</span><span class="p">,</span><span class="mi">0</span><span class="p">)):</span><span class="n">bisect_right</span><span class="p">(</span><span class="n">mm</span><span class="p">,(</span><span class="n">mx</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">))]:</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">mn</span><span class="o">&gt;=</span><span class="n">mx</span><span class="p">:</span>
      </span><span class="line">                <span class="k">break</span>
      </span><span class="line">            <span class="n">s</span> <span class="o">+=</span> <span class="n">a</span> <span class="o">+</span> <span class="mi">16</span> <span class="c"># add 16 bytes for malloc headers</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">s</span><span class="o">&lt;=</span><span class="n">mn</span><span class="p">:</span>
      </span><span class="line">                <span class="k">continue</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">a</span><span class="o">&lt;</span><span class="n">mx</span><span class="p">:</span>
      </span><span class="line">                <span class="n">rv</span> <span class="o">=</span> <span class="s">&#39;-&#39;</span> <span class="c"># touched the range, at least fragmented</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">a</span><span class="o">&gt;</span><span class="n">mn</span><span class="p">:</span>
      </span><span class="line">                <span class="c"># cannot be fully used</span>
      </span><span class="line">                <span class="k">break</span>
      </span><span class="line">            <span class="c">#used up to s</span>
      </span><span class="line">            <span class="n">mn</span><span class="o">=</span><span class="n">s</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">mx</span> <span class="o">&lt;=</span> <span class="n">mn</span><span class="p">:</span>
      </span><span class="line">            <span class="n">rv</span> <span class="o">=</span> <span class="s">&#39;*&#39;</span> <span class="c"># used in full</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">rv</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">bytes</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">1024</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;</span><span class="si">%d</span><span class="s">b&#39;</span> <span class="o">%</span> <span class="n">x</span>
      </span><span class="line">        <span class="k">elif</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">1024</span><span class="o">*</span><span class="mi">1024</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;</span><span class="si">%.2f</span><span class="s">Kb&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">x</span><span class="o">/</span><span class="mf">1024.0</span><span class="p">)</span>
      </span><span class="line">        <span class="k">elif</span> <span class="n">x</span> <span class="o">&lt;</span> <span class="mi">1024</span><span class="o">*</span><span class="mi">1024</span><span class="o">*</span><span class="mi">1024</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;</span><span class="si">%.2f</span><span class="s">Mb&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">x</span><span class="o">/</span><span class="mf">1024.0</span><span class="o">/</span><span class="mf">1024.0</span><span class="p">)</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;</span><span class="si">%.2f</span><span class="s">Gb&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">x</span><span class="o">/</span><span class="mf">1024.0</span><span class="o">/</span><span class="mf">1024.0</span><span class="o">/</span><span class="mf">1024.0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">secsize</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
      </span><span class="line">        <span class="n">rv</span> <span class="o">=</span> <span class="mi">4096</span>
      </span><span class="line">        <span class="k">while</span> <span class="p">(</span><span class="n">x</span><span class="o">/</span><span class="n">rv</span><span class="o">/</span><span class="mi">80</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">40</span><span class="p">:</span>
      </span><span class="line">            <span class="n">rv</span> <span class="o">*=</span> <span class="mi">2</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">rv</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">report</span><span class="p">(</span><span class="n">mn</span><span class="p">,</span><span class="n">mx</span><span class="p">,</span><span class="n">ss</span><span class="p">):</span>
      </span><span class="line">        <span class="n">smxsz</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span> <span class="n">s</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span><span class="p">[</span><span class="n">bisect_left</span><span class="p">(</span><span class="n">mm</span><span class="p">,(</span><span class="n">mn</span><span class="o">-</span><span class="n">mxsz</span><span class="o">-</span><span class="mi">16</span><span class="p">,</span><span class="mi">0</span><span class="p">)):</span><span class="n">bisect_right</span><span class="p">(</span><span class="n">mm</span><span class="p">,(</span><span class="n">mx</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">))]</span> <span class="p">)</span>
      </span><span class="line">        <span class="n">mp</span>  <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span> <span class="n">usage</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">i</span><span class="o">+</span><span class="n">ss</span><span class="p">,</span><span class="n">smxsz</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">mn</span><span class="p">,</span><span class="n">mx</span><span class="p">,</span><span class="n">ss</span><span class="p">)</span> <span class="p">])</span>
      </span><span class="line">        <span class="n">rv</span>  <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> total, </span><span class="si">%s</span><span class="s"> per sector</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">mx</span><span class="o">-</span><span class="n">mn</span><span class="p">),</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">ss</span><span class="p">))</span>
      </span><span class="line">        <span class="n">rv</span> <span class="o">+=</span> <span class="n">lre</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\\</span><span class="s">1</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span><span class="n">mp</span><span class="p">)</span>
      </span><span class="line">        <span class="n">rv</span> <span class="o">+=</span> <span class="s">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="s">        Fragmentation: </span><span class="si">%.2f%%</span><span class="s"></span>
      </span><span class="line"><span class="s">        Fragmented sectors: </span><span class="si">%d</span><span class="s"></span>
      </span><span class="line"><span class="s">        Contiguous used sectors: </span><span class="si">%d</span><span class="s"></span>
      </span><span class="line"><span class="s">        Contiguous free sectors: </span><span class="si">%d</span><span class="s"></span>
      </span><span class="line"><span class="s">        &quot;&quot;&quot;</span> <span class="o">%</span> <span class="p">(</span> <span class="n">mp</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">)</span><span class="o">*</span><span class="mf">100.0</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">mp</span><span class="p">),</span>
      </span><span class="line">                <span class="n">mp</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="p">),</span>
      </span><span class="line">                <span class="n">mp</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;*&#39;</span><span class="p">),</span>
      </span><span class="line">                <span class="n">mp</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)</span> <span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">rv</span>
      </span><span class="line">   
      </span><span class="line">    <span class="k">def</span> <span class="nf">domap</span><span class="p">(</span><span class="n">filterfn</span><span class="p">):</span>
      </span><span class="line">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">(</span><span class="n">filterfn</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span><span class="p">):</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;empty&#39;</span>
      </span><span class="line">        <span class="n">mn</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span> <span class="n">a</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span> <span class="k">if</span> <span class="n">filterfn</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="p">)</span>
      </span><span class="line">        <span class="n">mx</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span> <span class="n">a</span> <span class="k">for</span> <span class="n">a</span><span class="p">,</span><span class="n">s</span> <span class="ow">in</span> <span class="n">mm</span> <span class="k">if</span> <span class="n">filterfn</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="p">)</span>
      </span><span class="line">        <span class="n">ss</span> <span class="o">=</span> <span class="n">secsize</span><span class="p">(</span><span class="n">mx</span><span class="o">-</span><span class="n">mn</span><span class="p">)</span>
      </span><span class="line">        <span class="n">mn</span> <span class="o">=</span> <span class="n">mn</span><span class="o">/</span><span class="n">ss</span><span class="o">*</span><span class="n">ss</span>
      </span><span class="line">        <span class="n">mx</span> <span class="o">=</span> <span class="n">mx</span><span class="o">/</span><span class="n">ss</span><span class="o">*</span><span class="n">ss</span><span class="o">+</span><span class="n">ss</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">report</span><span class="p">(</span><span class="n">mn</span><span class="p">,</span><span class="n">mx</span><span class="p">,</span><span class="n">ss</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">lre</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;(.{80,80})&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">lomap</span> <span class="o">=</span> <span class="n">domap</span><span class="p">(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">:</span> <span class="n">a</span> <span class="o">&lt;</span>  <span class="mh">0x80000000</span><span class="p">)</span>
      </span><span class="line">    <span class="n">medmap</span><span class="o">=</span> <span class="n">domap</span><span class="p">(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">:</span> <span class="n">a</span> <span class="o">&gt;=</span> <span class="mh">0x80000000</span> <span class="ow">and</span> <span class="n">a</span> <span class="o">&lt;</span> <span class="mh">0x100000000</span><span class="n">L</span><span class="p">)</span>
      </span><span class="line">    <span class="n">himap</span> <span class="o">=</span> <span class="n">domap</span><span class="p">(</span><span class="k">lambda</span> <span class="n">a</span><span class="p">:</span> <span class="n">a</span> <span class="o">&gt;=</span> <span class="mh">0x100000000</span><span class="n">L</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="n">lomap</span><span class="p">,</span> <span class="n">medmap</span><span class="p">,</span> <span class="n">himap</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">heapStats</span><span class="p">():</span>
      </span><span class="line">    <span class="k">global</span> <span class="n">_debug_heap</span>
      </span><span class="line">    <span class="k">global</span> <span class="n">_heapy</span>
      </span><span class="line">
      </span><span class="line">    <span class="kn">import</span> <span class="nn">StringIO</span>
      </span><span class="line">   
      </span><span class="line">    <span class="n">statdump</span> <span class="o">=</span> <span class="n">StringIO</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
      </span><span class="line">    <span class="n">heap</span> <span class="o">=</span> <span class="n">_heapy</span><span class="o">.</span><span class="n">heap</span><span class="p">()</span>
      </span><span class="line">   
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">heap</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">statdump</span><span class="p">)</span>
      </span><span class="line">    <span class="k">except</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># ignore exceptions dumping... shit happens</span>
      </span><span class="line">        <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">statdumpu</span> <span class="o">=</span> <span class="n">StringIO</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
      </span><span class="line">    <span class="n">heapu</span> <span class="o">=</span> <span class="n">_heapy</span><span class="o">.</span><span class="n">heapu</span><span class="p">()</span>
      </span><span class="line">       
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">heapu</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">statdumpu</span><span class="p">)</span>
      </span><span class="line">    <span class="k">except</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># ignore exceptions dumping... shit happens</span>
      </span><span class="line">        <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">statdumpbr</span> <span class="o">=</span> <span class="n">StringIO</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
      </span><span class="line">    <span class="n">heapbr</span> <span class="o">=</span> <span class="n">heap</span><span class="o">.</span><span class="n">byrcs</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">heapbr</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">statdumpbr</span><span class="p">)</span>
      </span><span class="line">    <span class="k">except</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># ignore exceptions dumping... shit happens</span>
      </span><span class="line">        <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">refs</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">refs</span> <span class="o">=</span> <span class="n">heap</span><span class="o">.</span><span class="n">stat</span>
      </span><span class="line">        <span class="n">refs</span><span class="o">.</span><span class="n">rows</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">refs</span><span class="o">.</span><span class="n">get_rows</span><span class="p">())</span>
      </span><span class="line">        <span class="n">refs</span><span class="o">.</span><span class="n">rows</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">:</span><span class="o">-</span><span class="nb">cmp</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">count</span><span class="p">,</span><span class="n">y</span><span class="o">.</span><span class="n">count</span><span class="p">))</span>
      </span><span class="line">       
      </span><span class="line">        <span class="n">oc</span> <span class="o">=</span> <span class="n">_heapy</span><span class="o">.</span><span class="n">Size</span><span class="o">.</span><span class="n">classifier</span><span class="o">.</span><span class="n">get_cli</span><span class="p">()</span><span class="o">.</span><span class="n">classify</span>
      </span><span class="line">        <span class="n">id_</span> <span class="o">=</span> <span class="nb">id</span>
      </span><span class="line">        <span class="n">str_</span> <span class="o">=</span> <span class="nb">str</span>
      </span><span class="line">        <span class="n">memmap</span> <span class="o">=</span> <span class="p">[</span> <span class="p">(</span><span class="n">id_</span><span class="p">(</span><span class="n">x</span><span class="p">),</span><span class="n">oc</span><span class="p">(</span><span class="n">x</span><span class="p">))</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">heap</span><span class="o">.</span><span class="n">nodes</span> <span class="p">]</span>
      </span><span class="line">    <span class="k">except</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># At least the rest will be useful</span>
      </span><span class="line">        <span class="n">memmap</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">   
      </span><span class="line">    <span class="n">memmap</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
      </span><span class="line">   
      </span><span class="line">    <span class="c"># Generate lowres reports from the memmap in four areas, lo, med, hi and very hi.</span>
      </span><span class="line">    <span class="c"># memory (memory allocations tend to group themselves in those ranges,</span>
      </span><span class="line">    <span class="c"># one is probably memmapped heap, the other is simple allocations and</span>
      </span><span class="line">    <span class="c"># the medium one must be the stack). The very high area is the mmap&#39;d area,</span>
      </span><span class="line">    <span class="c"># where most big arrays end up.</span>
      </span><span class="line">    <span class="n">lomap</span><span class="p">,</span> <span class="n">medmap</span><span class="p">,</span> <span class="n">himap</span> <span class="o">=</span> <span class="n">report_memmap</span><span class="p">(</span><span class="n">memmap</span><span class="p">)</span>
      </span><span class="line">   
      </span><span class="line">    <span class="c"># Pickle the memmap, xmlrpclib doesn&#39;t like big integers</span>
      </span><span class="line">    <span class="n">memmap</span> <span class="o">=</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">memmap</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">srepr</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="nb">repr</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">e</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;ERROR: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="p">(</span><span class="n">e</span><span class="p">,)</span>
      </span><span class="line">   
      </span><span class="line">    <span class="n">rv</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
      </span><span class="line">        <span class="n">byclodo</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
      </span><span class="line">            <span class="n">reachable</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">srepr</span><span class="p">,</span> <span class="p">[</span> <span class="n">heap</span><span class="p">,</span> <span class="n">heap</span><span class="o">.</span><span class="n">more</span><span class="p">,</span> <span class="n">heap</span><span class="o">.</span><span class="n">more</span><span class="o">.</span><span class="n">more</span> <span class="p">]),</span>
      </span><span class="line">            <span class="n">uncollectable</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">srepr</span><span class="p">,</span> <span class="p">[</span> <span class="n">heapu</span><span class="p">,</span> <span class="n">heapu</span><span class="o">.</span><span class="n">more</span><span class="p">,</span> <span class="n">heapu</span><span class="o">.</span><span class="n">more</span><span class="o">.</span><span class="n">more</span> <span class="p">]),</span>
      </span><span class="line">            <span class="n">statdump</span> <span class="o">=</span> <span class="n">statdump</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(),</span>
      </span><span class="line">            <span class="n">statdumpu</span> <span class="o">=</span> <span class="n">statdumpu</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(),</span>
      </span><span class="line">            <span class="n">refs</span> <span class="o">=</span> <span class="n">srepr</span><span class="p">(</span><span class="n">refs</span><span class="p">)</span>
      </span><span class="line">        <span class="p">),</span>
      </span><span class="line">        <span class="n">byrcs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
      </span><span class="line">            <span class="n">reachable</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">srepr</span><span class="p">,</span> <span class="p">[</span> <span class="n">heapbr</span><span class="p">,</span> <span class="n">heapbr</span><span class="o">.</span><span class="n">more</span><span class="p">,</span> <span class="n">heapbr</span><span class="o">.</span><span class="n">more</span><span class="o">.</span><span class="n">more</span> <span class="p">]),</span>
      </span><span class="line">            <span class="n">statdump</span> <span class="o">=</span> <span class="n">statdumpbr</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span>
      </span><span class="line">        <span class="p">),</span>
      </span><span class="line">        <span class="n">memmap</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
      </span><span class="line">            <span class="n">detail</span> <span class="o">=</span> <span class="n">memmap</span><span class="p">,</span>
      </span><span class="line">            <span class="n">lo</span> <span class="o">=</span> <span class="n">lomap</span><span class="p">,</span>
      </span><span class="line">            <span class="n">med</span> <span class="o">=</span> <span class="n">medmap</span><span class="p">,</span>
      </span><span class="line">            <span class="n">hi</span> <span class="o">=</span> <span class="n">himap</span>
      </span><span class="line">        <span class="p">)</span>
      </span><span class="line">    <span class="p">)</span>
      </span><span class="line">   
      </span><span class="line">    <span class="c"># return a pickle dump, not by pure xmlrpc</span>
      </span><span class="line">    <span class="c">#   (xmlrpc is picky, doesn&#39;t support big ints)</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">rv</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
      </span>

.. ############################################################################

.. _heapy: http://guppy-pe.sourceforge.net/

