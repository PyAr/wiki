#format rst

Obtener ip Publica
==================

* Como obtener la ip Publica, usando Python, ejemplo simple.

**Nota:** *Que tengas direccion ip publica no implica que tengas conectividad.*

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*- </span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">urllib</span>
      </span><span class="line"><span class="n">ip</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="s">&#39;http://automation.whatismyip.com/n09230945.asp&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> <span class="c"># esta URL puede ser reemplazada con otra que preste similar servicio</span>
      </span><span class="line"><span class="k">print</span> <span class="n">ip</span>
      </span>

**Ejemplo:**

::

   sudo /usr/bin/env python getip.py
   190.139.27.XXX

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

