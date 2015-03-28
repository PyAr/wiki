#format rst

La cuestión
-----------

Al efectuar búsquedas en Internet, estamos acostumbrados a que no se distinga entre mayúsculas y minúsculas, y que se ignoren los acentos de las palabras. Para hacer esto en Python, antes que nada necesitamos una función que convierta los strings a la forma especificada. Una que haga lo siguiente:

::

   >>> normalizar_string(u'Mónica Viñao')
   'monica vinao'

Usando unicodedata.normalize
----------------------------

Unicode define equivalencias entre caracteres, o secuencias de caracteres, de los distintos estándares (ver http://en.wikipedia.org/wiki/Unicode_equivalence). Y define formas normales a las que podemos llevar un texto. Entonces podemos lograr la transformación que queremos haciendo una normalización. Los caracteres se descomponen, ignorando la parte que no es ASCII:

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">unicodedata</span> <span class="kn">import</span> <span class="n">normalize</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">normalizar_string</span><span class="p">(</span><span class="n">unicode_string</span><span class="p">):</span>
      </span><span class="line">    <span class="s">u&quot;&quot;&quot;Retorna unicode_string normalizado para efectuar una búsqueda.</span>
      </span><span class="line">
      </span><span class="line"><span class="s">    &gt;&gt;&gt; normalizar_string(u&#39;Mónica Viñao&#39;)</span>
      </span><span class="line"><span class="s">    &#39;monica vinao&#39;</span>
      </span><span class="line"><span class="s">    </span>
      </span><span class="line"><span class="s">    &quot;&quot;&quot;</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">normalize</span><span class="p">(</span><span class="s">&#39;NFKD&#39;</span><span class="p">,</span> <span class="n">unicode_string</span><span class="p">)</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;ASCII&#39;</span><span class="p">,</span> <span class="s">&#39;ignore&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">doctest</span>
      </span><span class="line">    <span class="n">doctest</span><span class="o">.</span><span class="n">testmod</span><span class="p">()</span>
      </span>

¡Gracias a Martin Conte Mac Donell!

-------------------------



  CategoryRecetas_

