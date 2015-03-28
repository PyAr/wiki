#format rst

aLetras
-------

Descripción
:::::::::::

*aLetras(numero)* es una función a la que se le pasa un valor númerico y regresa un string con el valor numérico convertido a letras.

Los valores que pueden ser convertidos pertenecen al rango *-999.999.999,99 : 999.999.999,99*. Si se proporciona una cadena fuera de rango, retorna el string "0".

Siempre se trabaja con 2 decimales (se redondean los valores suministrados)

Ejemplos:
:::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="mf">1234.56</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39; MIL DOSCIENTOS TREINTA Y CUATRO CON CINCUENTA Y SEIS CENTAVOS&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="o">-</span><span class="mf">240.99</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;MENOS DOSCIENTOS CUARENTA CON NOVENTA Y NUEVE CENTAVOS&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;CIEN&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="mf">401201501.01</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;CUATROCIENTOS UN MILLON DOSCIENTOS UN MIL QUINIENTOS UNO CON UN CENTAVOS&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="o">-</span><span class="mf">0.76</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;MENOS CERO CON SETENTA Y SEIS CENTAVOS&#39;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">aLetras</span><span class="p">(</span><span class="mi">1000000000</span><span class="p">)</span>
      </span><span class="line"><span class="s">&#39;0&#39;</span>
      </span>

Observaciones
:::::::::::::

La asignación y condicional en una línea -> numeros[1] = "UNO" if i == 2 else "UN" <- da problemas de sintaxis con versiones anteriores a Python 2.5.x

Puede reemplazarse con:

::

   .. raw:: html
      <span class="line"><span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
      </span><span class="line">  <span class="n">numeros</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;UNO&quot;</span>
      </span><span class="line"><span class="k">else</span><span class="p">:</span>
      </span><span class="line">  <span class="n">numeros</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;UN&quot;</span>
      </span>

Código:
:::::::

::

   .. raw:: html
      <span class="line"><span class="c">#fuente: Recetario de PyAR, http://python.com.ar/moin/Recetario</span>
      </span><span class="line"><span class="c">#autor: Cesar E Portela</span>
      </span><span class="line"><span class="c">#date: 06-05-2008</span>
      </span><span class="line"><span class="c">#version: 2</span>
      </span><span class="line"><span class="c">#para Python: 2.5.x</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">aLetras</span><span class="p">(</span><span class="n">numero</span><span class="p">):</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">numeros</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span><span class="s">&quot;CERO&quot;</span><span class="p">,</span><span class="mi">2</span><span class="p">:</span><span class="s">&quot;DOS&quot;</span><span class="p">,</span><span class="mi">3</span><span class="p">:</span><span class="s">&quot;TRES&quot;</span><span class="p">,</span><span class="mi">4</span><span class="p">:</span><span class="s">&quot;CUATRO&quot;</span><span class="p">,</span><span class="mi">5</span><span class="p">:</span><span class="s">&quot;CINCO&quot;</span><span class="p">,</span><span class="mi">6</span><span class="p">:</span><span class="s">&quot;SEIS&quot;</span><span class="p">,</span><span class="mi">7</span><span class="p">:</span><span class="s">&quot;SIETE&quot;</span><span class="p">,</span><span class="mi">8</span><span class="p">:</span><span class="s">&quot;OCHO&quot;</span><span class="p">,</span><span class="mi">9</span><span class="p">:</span><span class="s">&quot;NUEVE&quot;</span><span class="p">,</span>
      </span><span class="line">                <span class="mi">10</span><span class="p">:</span><span class="s">&quot;DIEZ&quot;</span><span class="p">,</span><span class="mi">11</span><span class="p">:</span><span class="s">&quot;ONCE&quot;</span><span class="p">,</span><span class="mi">12</span><span class="p">:</span><span class="s">&quot;DOCE&quot;</span><span class="p">,</span><span class="mi">13</span><span class="p">:</span><span class="s">&quot;TRECE&quot;</span><span class="p">,</span><span class="mi">14</span><span class="p">:</span><span class="s">&quot;CATORCE&quot;</span><span class="p">,</span><span class="mi">15</span><span class="p">:</span><span class="s">&quot;QUINCE&quot;</span><span class="p">,</span><span class="mi">16</span><span class="p">:</span><span class="s">&quot;DIECISEIS&quot;</span><span class="p">,</span><span class="mi">17</span><span class="p">:</span><span class="s">&quot;DIECISIETE&quot;</span><span class="p">,</span>
      </span><span class="line">                <span class="mi">18</span><span class="p">:</span><span class="s">&quot;DIECIOCHO&quot;</span><span class="p">,</span><span class="mi">19</span><span class="p">:</span><span class="s">&quot;DIECINUEVE&quot;</span><span class="p">,</span><span class="mi">20</span><span class="p">:</span><span class="s">&quot;VEINTE&quot;</span><span class="p">,</span><span class="mi">30</span><span class="p">:</span><span class="s">&quot;TREINTA&quot;</span><span class="p">,</span>
      </span><span class="line">                <span class="mi">40</span><span class="p">:</span><span class="s">&quot;CUARENTA&quot;</span><span class="p">,</span><span class="mi">50</span><span class="p">:</span><span class="s">&quot;CINCUENTA&quot;</span><span class="p">,</span><span class="mi">60</span><span class="p">:</span><span class="s">&quot;SESENTA&quot;</span><span class="p">,</span><span class="mi">70</span><span class="p">:</span><span class="s">&quot;SETENTA&quot;</span><span class="p">,</span><span class="mi">80</span><span class="p">:</span><span class="s">&quot;OCHENTA&quot;</span><span class="p">,</span><span class="mi">90</span><span class="p">:</span><span class="s">&quot;NOVENTA&quot;</span><span class="p">,</span><span class="mi">100</span><span class="p">:</span><span class="s">&quot;CIEN&quot;</span><span class="p">,</span>
      </span><span class="line">                <span class="mi">500</span><span class="p">:</span><span class="s">&quot;QUINIENTOS &quot;</span><span class="p">,</span><span class="mi">700</span><span class="p">:</span><span class="s">&quot;SETECIENTOS &quot;</span><span class="p">,</span><span class="mi">900</span><span class="p">:</span><span class="s">&quot;NOVECIENTOS &quot;</span><span class="p">}</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">if</span> <span class="nb">abs</span><span class="p">(</span><span class="n">numero</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">999999999.99</span> <span class="p">:</span> <span class="c">#mil millones, esta funcion procesa el rango [-999.999.999,99; 999.999.999,99]</span>
      </span><span class="line">        <span class="k">return</span> <span class="p">(</span><span class="s">&quot;0&quot;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
      </span><span class="line">    <span class="k">elif</span> <span class="n">numero</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">        <span class="n">cadena</span> <span class="o">=</span> <span class="s">&quot;MENOS &quot;</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">cadena</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
      </span><span class="line">
      </span><span class="line">    <span class="c">#separo el numero entregado entre parte entera y sus decimales (tomando solo 2 y redondeando para arriba)</span>
      </span><span class="line">    <span class="n">entero</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">numero</span><span class="p">))</span>
      </span><span class="line">    <span class="n">decimales</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="nb">round</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">numero</span><span class="p">),</span> <span class="mi">2</span><span class="p">)</span> <span class="o">+</span> <span class="mf">0.001</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span> <span class="o">%</span> <span class="mi">100</span>
      </span><span class="line">
      </span><span class="line">    <span class="c">#la parte entera es separada en grupos de tres digitos</span>
      </span><span class="line">    <span class="n">grupo1</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">entero</span> <span class="o">/</span> <span class="mi">1000000</span><span class="p">)</span>
      </span><span class="line">    <span class="n">grupo2</span> <span class="o">=</span> <span class="nb">int</span><span class="p">((</span><span class="nb">int</span><span class="p">(</span><span class="n">entero</span><span class="p">)</span> <span class="o">-</span> <span class="nb">int</span><span class="p">(</span><span class="n">grupo1</span><span class="p">)</span><span class="o">*</span><span class="mi">1000000</span><span class="p">)</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>
      </span><span class="line">    <span class="n">grupo3</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">entero</span> <span class="o">%</span> <span class="mi">1000</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">lista</span> <span class="o">=</span> <span class="p">[</span><span class="n">grupo1</span><span class="p">,</span> <span class="n">grupo2</span><span class="p">,</span> <span class="n">grupo3</span><span class="p">,</span> <span class="n">decimales</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">if</span> <span class="p">(</span><span class="n">grupo1</span> <span class="o">+</span> <span class="n">grupo2</span> <span class="o">+</span> <span class="n">grupo3</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">        <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">4</span><span class="p">):</span>
      </span><span class="line">        <span class="n">unidad</span> <span class="o">=</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">%</span> <span class="mi">10</span>
      </span><span class="line">        <span class="n">decena</span> <span class="o">=</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">%</span> <span class="mi">100</span>
      </span><span class="line">        <span class="n">centena</span> <span class="o">=</span> <span class="p">(</span><span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span> <span class="o">%</span> <span class="mi">10</span>
      </span><span class="line">        <span class="n">subcadena</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">numeros</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;UNO&quot;</span> <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">2</span> <span class="k">else</span> <span class="s">&quot;UN&quot;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c">#grupo 1: el de los millones</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">decena</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">                <span class="n">subcadena</span> <span class="o">=</span> <span class="s">&quot; MILLON &quot;</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">                <span class="n">subcadena</span> <span class="o">=</span> <span class="s">&quot; MILLONES &quot;</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span> <span class="c">#aqui se entra si lista[i] == 0 y en ese caso, no hay nada que procesar</span>
      </span><span class="line">                <span class="k">continue</span> <span class="c">#se sigue con la siguiente iteracion del bucle</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">elif</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span> <span class="c">#grupo2: el de los miles</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="s">&quot; MIL &quot;</span>
      </span><span class="line">                <span class="k">continue</span> <span class="c">#se pasa a la siguiente iteracion</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">                <span class="n">subcadena</span> <span class="o">=</span> <span class="s">&quot; MIL &quot;</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span> <span class="c">#aqui se entra si lista[i] == 0 y en ese caso, no hay nada que procesar</span>
      </span><span class="line">                <span class="k">continue</span> <span class="c">#se sigue con la siguiente iteracion del bucle</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">elif</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">3</span> <span class="ow">and</span> <span class="n">lista</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span> <span class="c">#grupo4: el de los centavos (decimales)</span>
      </span><span class="line">            <span class="n">cadena</span> <span class="o">+=</span> <span class="s">&quot; CON &quot;</span>
      </span><span class="line">            <span class="n">subcadena</span> <span class="o">=</span> <span class="s">&quot; CENTAVOS&quot;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">centena</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">centena</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="p">(</span><span class="n">unidad</span> <span class="o">+</span> <span class="n">decena</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="mi">100</span><span class="p">]</span>
      </span><span class="line">                <span class="k">continue</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">centena</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="s">&quot;CIENTO &quot;</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">centena</span> <span class="o">==</span> <span class="mi">5</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="mi">500</span><span class="p">]</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">centena</span> <span class="o">==</span> <span class="mi">7</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="mi">700</span><span class="p">]</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">centena</span> <span class="o">==</span> <span class="mi">9</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="mi">900</span><span class="p">]</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="n">centena</span><span class="p">]</span> <span class="o">+</span> <span class="s">&quot;CIENTOS &quot;</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">decena</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">decena</span> <span class="o">&lt;</span> <span class="mi">21</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[</span><span class="n">decena</span><span class="p">]</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">decena</span> <span class="o">&lt;</span> <span class="mi">30</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="s">&quot;VENTI&quot;</span><span class="o">+</span><span class="n">numeros</span><span class="p">[</span><span class="n">unidad</span><span class="p">]</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="n">cadena</span> <span class="o">+=</span> <span class="n">numeros</span><span class="p">[(</span><span class="n">decena</span><span class="o">/</span><span class="mi">10</span><span class="p">)</span><span class="o">*</span><span class="mi">10</span><span class="p">]</span>
      </span><span class="line">                <span class="k">if</span> <span class="n">unidad</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">cadena</span> <span class="o">+=</span> <span class="s">&quot; Y &quot;</span><span class="o">+</span><span class="n">numeros</span><span class="p">[</span><span class="n">unidad</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">cadena</span> <span class="o">+=</span> <span class="n">subcadena</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="n">cadena</span>
      </span>

Autor / Autores:
::::::::::::::::

CesarPortela_

.. ############################################################################

.. _CesarPortela: ../CesarPortela

