#format rst

Reverse (a.k.a. "esrever")
==========================

* Una humilde funcion para dar vuelta los caracteres usando Python, letras o numeros, ejemplo simple.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*- </span>
      </span><span class="line"><span class="k">def</span> <span class="nf">reverse</span><span class="p">(</span><span class="n">this</span><span class="p">):</span>
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">things</span><span class="p">)[::</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span> <span class="k">for</span> <span class="n">things</span> <span class="ow">in</span> <span class="n">this</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
      </span><span class="line"><span class="n">inputz</span> <span class="o">=</span> <span class="nb">raw_input</span><span class="p">()</span>
      </span><span class="line"><span class="k">print</span> <span class="n">reverse</span><span class="p">(</span><span class="n">inputz</span><span class="p">)</span>
      </span>

**Ejemplo:**

::

   juan@wind:~$ /usr/bin/env python reverse.py
   import antigravity
   tropmi ytivargitna

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

