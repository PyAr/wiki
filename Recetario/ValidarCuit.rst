#format rst

Validar CUIT
------------

Descripción
:::::::::::

*validar_cuit(cuit)* es una función a la que se le pasa un CUIT/CUIL (cadena '00-00000000-0') y devuelve True si el CUIT es válido (tiene la longitud y formato correcto, y su digito verificador esta ok).

El CUIT/CUIL es el código único de de identificación tributaria/laboral, que se le asigna a cada persona física o jurídica (sociedades) alcanzadas por el sistema impositivo argentino.

**Aclaración**: que el CUIT sea válido no quiere decir que la persona titular exista y esté habilitada por los organismos correspondientes.

Siempre se debe verificar la vigencia del CUIT en la página de la AFIP (Administración Federal de Ingresos Públicos). Por el momento es una página web, quizas en un futuro ofrezcan un servicio web para automatizar el proceso. Tambien es posible bajarse un padrón (archivo de texto plano), tarea para otra receta |:)|

Ejemplos:
:::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">validar_cuit</span><span class="p">(</span><span class="s">&quot;00-00000000-0&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="bp">True</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">validar_cuit</span><span class="p">(</span><span class="s">&quot;00-00000000-1&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="bp">False</span>
      </span>

Código:
:::::::

::

   .. raw:: html
      <span class="line"><span class="k">def</span> <span class="nf">validar_cuit</span><span class="p">(</span><span class="n">cuit</span><span class="p">):</span>
      </span><span class="line">    <span class="c"># validaciones minimas</span>
      </span><span class="line">    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">cuit</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">13</span> <span class="ow">or</span> <span class="n">cuit</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&quot;-&quot;</span> <span class="ow">or</span> <span class="n">cuit</span><span class="p">[</span><span class="mi">11</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&quot;-&quot;</span><span class="p">:</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">base</span> <span class="o">=</span> <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">cuit</span> <span class="o">=</span> <span class="n">cuit</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;-&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="c"># remuevo las barras</span>
      </span><span class="line">
      </span><span class="line">    <span class="c"># calculo el digito verificador:</span>
      </span><span class="line">    <span class="n">aux</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
      </span><span class="line">        <span class="n">aux</span> <span class="o">+=</span> <span class="nb">int</span><span class="p">(</span><span class="n">cuit</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="o">*</span> <span class="n">base</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">aux</span> <span class="o">=</span> <span class="mi">11</span> <span class="o">-</span> <span class="p">(</span><span class="n">aux</span> <span class="o">-</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">aux</span> <span class="o">/</span> <span class="mi">11</span><span class="p">)</span> <span class="o">*</span> <span class="mi">11</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">if</span> <span class="n">aux</span> <span class="o">==</span> <span class="mi">11</span><span class="p">:</span>
      </span><span class="line">        <span class="n">aux</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">aux</span> <span class="o">==</span> <span class="mi">10</span><span class="p">:</span>
      </span><span class="line">        <span class="n">aux</span> <span class="o">=</span> <span class="mi">9</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="n">aux</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">cuit</span><span class="p">[</span><span class="mi">10</span><span class="p">])</span>
      </span>

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

