#format rst

Chequeo de Paquetes con APT
===========================

* Como saber si un paquete esta instalado, o no, y si el mismo existe usando Python, ejemplo interactivo simple.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">apt</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">cache</span> <span class="o">=</span> <span class="n">apt</span><span class="o">.</span><span class="n">Cache</span><span class="p">()</span>
      </span><span class="line"><span class="n">cache</span><span class="o">.</span><span class="n">open</span><span class="p">()</span>
      </span><span class="line"><span class="n">program</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39; Cual es el nombre del programa?: &#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">if</span> <span class="n">program</span> <span class="ow">in</span> <span class="n">cache</span><span class="p">:</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">cache</span><span class="p">[</span><span class="n">program</span><span class="p">]</span><span class="o">.</span><span class="n">is_installed</span><span class="p">:</span>
      </span><span class="line">        <span class="k">print</span> <span class="p">(</span><span class="s">&#39; El programa esta instalado!</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="k">print</span> <span class="p">(</span><span class="s">&#39; El programa no esta instalado!</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="k">else</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="p">(</span><span class="s">&#39; Estas seguro del Nombre del programa?, el programa no existe!</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
      </span>

**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: python
    El programa esta instalado!
   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: monodevelop
    El programa no esta instalado!
   juan@wind:~$ /usr/bin/env python apt-app-check.py
    Cual es el nombre del programa?: hjklsdajflkdshjdskabnv         
    Estas seguro del Nombre del programa?, el programa no existe!
   juan@wind:~$

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

