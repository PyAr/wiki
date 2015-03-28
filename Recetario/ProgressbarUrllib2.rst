#format rst

Progressbar y Urllib2
=====================

Este es un ejemplito de como descargar algo y a medida que se descarga, mostrar una barrita de progreso.

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">progressbar</span> <span class="kn">import</span> <span class="n">ProgressBar</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">progressbar</span> <span class="kn">import</span> <span class="n">Percentage</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">progressbar</span> <span class="kn">import</span> <span class="n">Bar</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">download_python</span><span class="p">():</span>
      </span><span class="line">    <span class="n">url</span> <span class="o">=</span> <span class="s">&#39;http://www.python.org/ftp/python/2.7/Python-2.7.tar.bz2&#39;</span>
      </span><span class="line">    <span class="n">fname</span> <span class="o">=</span> <span class="n">url</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
      </span><span class="line">    <span class="n">u</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
      </span><span class="line">    <span class="nb">file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">fname</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">meta</span> <span class="o">=</span> <span class="n">u</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
      </span><span class="line">    <span class="n">file_size</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">meta</span><span class="o">.</span><span class="n">getheaders</span><span class="p">(</span><span class="s">&quot;Content-Length&quot;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;Descargando: </span><span class="si">%s</span><span class="s"> Bytes: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">fname</span><span class="p">,</span> <span class="n">file_size</span><span class="p">)</span>
      </span><span class="line">    <span class="n">pbar</span> <span class="o">=</span> <span class="n">ProgressBar</span><span class="p">(</span><span class="n">widgets</span><span class="o">=</span><span class="p">[</span><span class="n">Percentage</span><span class="p">(),</span> <span class="n">Bar</span><span class="p">()],</span> <span class="n">maxval</span><span class="o">=</span><span class="n">file_size</span><span class="p">)</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">    <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="n">chunk</span> <span class="o">=</span> <span class="mi">10240</span>
      </span><span class="line">    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">        <span class="nb">buffer</span> <span class="o">=</span> <span class="n">u</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
      </span><span class="line">        <span class="k">if</span> <span class="nb">buffer</span><span class="p">:</span>
      </span><span class="line">            <span class="nb">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">buffer</span><span class="p">)</span>
      </span><span class="line">            <span class="n">pbar</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
      </span><span class="line">            <span class="n">i</span> <span class="o">+=</span> <span class="n">chunk</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="k">break</span>
      </span><span class="line">    <span class="n">pbar</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>
      </span><span class="line">    <span class="nb">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

