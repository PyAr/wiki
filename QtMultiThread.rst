#format rst

Qt Multi Thread
===============

ejemplo de como manipular la interfaz grafica desde multiples threads.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="c">#qt_multithread.py</span>
      </span><span class="line">
      </span><span class="line"><span class="c">#Modificado de la versión original de Mariano Guerra para GTK ( http://python.org.ar/pyar/GtkMultiThread )</span>
      </span><span class="line"><span class="c">#Versión para Qt por Ernesto Savoretti</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyQt4</span> <span class="kn">import</span> <span class="n">QtCore</span><span class="p">,</span> <span class="n">QtGui</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">Queue</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">random</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">threading</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="n">TEXTS</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;eggs&#39;</span><span class="p">,</span> <span class="s">&#39;spam&#39;</span><span class="p">,</span> <span class="s">&#39;pyar&#39;</span><span class="p">,</span> <span class="s">&#39;gtk&#39;</span><span class="p">,</span> <span class="s">&#39;qt&#39;</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Molesto</span><span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;un thread que quiere molestar el main thread&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cola</span><span class="p">):</span>
      </span><span class="line">        <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setDaemon</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line"><span class="c">#        self.label = label # no usar en este thread!</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">cola</span> <span class="o">=</span> <span class="n">cola</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;metodo principal del thread, duerme un tiempo aleatorio y despues</span>
      </span><span class="line"><span class="sd">        pone algo en la cola para que el main thread lo haga&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">            <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span> <span class="o">*</span> <span class="mi">5</span><span class="p">)</span>
      </span><span class="line">            <span class="n">texto</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getName</span><span class="p">()</span> <span class="o">+</span> <span class="s">&#39; &#39;</span> <span class="o">+</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">TEXTS</span><span class="p">)</span>
      </span><span class="line">            <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">getName</span><span class="p">(),</span> <span class="s">&#39;escribiendo&#39;</span><span class="p">,</span> <span class="n">texto</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">cola</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">texto</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Ventana</span><span class="p">(</span><span class="n">QtGui</span><span class="o">.</span><span class="n">QWidget</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;ventana con un label, ninguna locura&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="n">QtGui</span><span class="o">.</span><span class="n">QWidget</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="mi">50</span><span class="p">,</span> <span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setWindowTitle</span><span class="p">(</span><span class="s">&#39;Qt con threads&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">layout</span> <span class="o">=</span> <span class="n">QtGui</span><span class="o">.</span><span class="n">QHBoxLayout</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">QtGui</span><span class="o">.</span><span class="n">QLabel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">layout</span><span class="o">.</span><span class="n">addWidget</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">setLayout</span><span class="p">(</span><span class="n">layout</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">cola</span> <span class="o">=</span> <span class="n">Queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hincha_b</span> <span class="o">=</span> <span class="n">Molesto</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cola</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">hincha_b</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span> <span class="o">=</span> <span class="n">QtCore</span><span class="o">.</span><span class="n">QTimer</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">setInterval</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">timeout</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">queue_manager</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">timer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">queue_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">                <span class="n">texto</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cola</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">True</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">)</span>
      </span><span class="line">                <span class="k">print</span> <span class="n">texto</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">label</span><span class="o">.</span><span class="n">setText</span><span class="p">(</span><span class="n">texto</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span> <span class="n">Queue</span><span class="o">.</span><span class="n">Empty</span><span class="p">:</span>
      </span><span class="line">            <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">app</span> <span class="o">=</span> <span class="n">QtGui</span><span class="o">.</span><span class="n">QApplication</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span>
      </span><span class="line">    <span class="n">w</span> <span class="o">=</span> <span class="n">Ventana</span><span class="p">()</span>
      </span><span class="line">    <span class="n">app</span><span class="o">.</span><span class="n">exec_</span><span class="p">()</span>
      </span>

