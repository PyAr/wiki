#format rst

Obtener Sensacion Termica
=========================

* Como obtener la Sensacion Termica o Temperatura Aparente usando Python, ejemplo simple.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*- </span>
      </span><span class="line"><span class="c"># </span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">math</span>
      </span><span class="line">
      </span><span class="line"><span class="n">t</span><span class="o">=</span> <span class="mi">20</span> <span class="c"># Temperatura</span>
      </span><span class="line"><span class="n">v</span> <span class="o">=</span> <span class="mi">20</span> <span class="c"># Velocidad del Viento</span>
      </span><span class="line"><span class="n">st</span> <span class="o">=</span> <span class="mi">33</span> <span class="o">+</span> <span class="p">(</span><span class="n">t</span><span class="o">-</span> <span class="mi">33</span><span class="p">)</span><span class="o">*</span><span class="p">(</span><span class="mf">0.474</span> <span class="o">+</span> <span class="mf">0.454</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">((</span><span class="n">v</span><span class="p">))</span><span class="o">-</span><span class="mf">0.0454</span><span class="o">*</span><span class="n">v</span><span class="p">)</span>
      </span><span class="line"><span class="k">print</span> <span class="n">st</span>
      </span>

**Ejemplo:**

::

   .. raw:: html
      <span class="line"><span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="nb">bin</span><span class="o">/</span><span class="n">env</span> <span class="n">python</span> <span class="n">st</span><span class="o">.</span><span class="n">py</span>
      </span><span class="line"><span class="mf">12.24</span>
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

