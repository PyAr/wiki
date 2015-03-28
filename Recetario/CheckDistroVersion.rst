
CheckDistroVersion
==================

Chequea la versión de la Distribución Linux, y actúa en función de eso. Utiliza el módulo platform_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">platform</span>
      </span><span class="line">
      </span><span class="line"><span class="n">osInfo</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;Ubuntu&#39;</span><span class="p">,</span> <span class="s">&#39;10.10&#39;</span><span class="p">,</span> <span class="s">&#39;maverick&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">sysInfo</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">linux_distribution</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">osInfo</span> <span class="o">==</span> <span class="n">sysInfo</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; OK &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="c"># Aca va que hacer si esta OK</span>
      </span><span class="line"><span class="k">else</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; ERROR &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="c"># Aca va que hacer si la version no es correcta</span>
      </span>

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _platform: http://www.python.org/doc//current/library/platform.html

