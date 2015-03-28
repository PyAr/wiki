#format rst

PsycoSpeedUp
------------

Acelera las aplicaciones en Python (JIT), disponible para 32bit.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c">#-*- coding:utf-8 -*-</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">psyco</span>  <span class="c"># Speed Up :)</span>
      </span><span class="line">    <span class="n">psyco</span><span class="o">.</span><span class="n">full</span><span class="p">()</span>
      </span><span class="line"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; No PYTHON-PSYCO avaliable, this application will run slower... &quot;</span><span class="p">)</span> <span class="c"># imprime este mensaje si Psyco no esta disponible</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">pass</span>
      </span><span class="line"><span class="c"># la aplicacion continuara funcionando si psyco no esta disponible, asi mismo continuara si es 64bit</span>
      </span><span class="line"><span class="c">########################## imports goes here</span>
      </span><span class="line"><span class="c"># from foo import bar</span>
      </span>

