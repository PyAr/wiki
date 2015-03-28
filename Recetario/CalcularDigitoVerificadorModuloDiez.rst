#format rst

Cálculo de Dígito Verificador Módulo 10
---------------------------------------

Descripción
:::::::::::

*digito_verificador_modulo10* es una función a la que se le pasa un código (ej. cadena '01234567890') y devuelve el dígito verificador a agregar correspondiente a la verificación módulo 10.

Esta verificación se usa en códigos de barra, por ej. en las facturas en el sistema impositivo argentino, donde se consigna el CUIT del emisor, CAI/CAE, número de factura, etc. 

Para más información, ver `Resolución General 1702 de la AFIP`_.

Ejemplo:
::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">digito_verificador_modulo10</span><span class="p">(</span><span class="s">&quot;01234567890&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;5&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">digito_verificador_modulo10</span><span class="p">(</span><span class="s">&#39;111111111112233334444444444444455555555&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;3&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">digito_verificador_modulo10</span><span class="p">(</span><span class="s">&#39;123456789012345678901234567890123456789&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;0&#39;</span>
      </span>

Código:
:::::::

::

   .. raw:: html
      <span class="line"><span class="k">def</span> <span class="nf">digito_verificador_modulo10</span><span class="p">(</span><span class="n">codigo</span><span class="p">):</span>
      </span><span class="line">    <span class="s">&quot;Rutina para el cálculo del dígito verificador &#39;módulo 10&#39;&quot;</span>
      </span><span class="line">    <span class="c"># Ver RG 1702 AFIP</span>
      </span><span class="line">    <span class="c"># Etapa 1: comenzar desde la izquierda, sumar todos los caracteres ubicados en las posiciones impares.</span>
      </span><span class="line">    <span class="n">etapa1</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="nb">int</span><span class="p">(</span><span class="n">c</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span><span class="n">c</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">codigo</span><span class="p">)</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">i</span><span class="o">%</span><span class="mi">2</span><span class="p">])</span>
      </span><span class="line">    <span class="c"># Etapa 2: multiplicar la suma obtenida en la etapa 1 por el número 3</span>
      </span><span class="line">    <span class="n">etapa2</span> <span class="o">=</span> <span class="n">etapa1</span> <span class="o">*</span> <span class="mi">3</span>
      </span><span class="line">    <span class="c"># Etapa 3: comenzar desde la izquierda, sumar todos los caracteres que están ubicados en las posiciones pares.</span>
      </span><span class="line">    <span class="n">etapa3</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="nb">int</span><span class="p">(</span><span class="n">c</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span><span class="n">c</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">codigo</span><span class="p">)</span> <span class="k">if</span> <span class="n">i</span><span class="o">%</span><span class="mi">2</span><span class="p">])</span>
      </span><span class="line">    <span class="c"># Etapa 4: sumar los resultados obtenidos en las etapas 2 y 3.</span>
      </span><span class="line">    <span class="n">etapa4</span> <span class="o">=</span> <span class="n">etapa2</span> <span class="o">+</span> <span class="n">etapa3</span>
      </span><span class="line">    <span class="c"># Etapa 5: buscar el menor número que sumado al resultado obtenido en la etapa 4 dé un número múltiplo de 10. </span>
      </span><span class="line">    <span class="c"># Este será el valor del dígito verificador del módulo 10.</span>
      </span><span class="line">    <span class="n">digito</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">-</span> <span class="p">(</span><span class="n">etapa4</span> <span class="o">-</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">etapa4</span> <span class="o">/</span> <span class="mi">10</span><span class="p">)</span> <span class="o">*</span> <span class="mi">10</span><span class="p">))</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">digito</span> <span class="o">==</span> <span class="mi">10</span><span class="p">:</span>
      </span><span class="line">        <span class="n">digito</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">    <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">digito</span><span class="p">)</span>
      </span>

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Resolución General 1702 de la AFIP: http://www.afip.gov.ar/afip/resol170204.html

