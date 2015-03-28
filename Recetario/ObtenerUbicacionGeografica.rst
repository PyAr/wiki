#format rst

Obtener Ubicacion Geografica
============================

* Como obtener distintos datos de la ubicacion Geografica, usando Python-Geoip, ejemplo simple.

**Requisitos:** Base de Datos de Geo-Location en la misma ubicacion que el programa, descargarla usando: 

::

   .. raw:: html
      <span class="line">wget --verbose http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
      </span>

**Nota:** *Depende de la conectividad con Internet usando direccion ip publica version 4, se desconoce el comportamiento con ip version 6.*

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*- </span>
      </span><span class="line"><span class="c"># </span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">urllib</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">GeoIP</span>
      </span><span class="line"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; ERROR: No PYTHON-GEOIP avaliable!!!. &quot;</span><span class="p">)</span> <span class="c"># que hacer si falla la importacion de la libreria</span>
      </span><span class="line">    <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># La base de datos GeoLiteCity.dat debe estar en la misma ubicacion que este programa</span>
      </span><span class="line"><span class="n">gi</span> <span class="o">=</span> <span class="n">GeoIP</span><span class="o">.</span><span class="n">open</span><span class="p">(</span>
      </span><span class="line"><span class="s">&quot;GeoLiteCity.dat&quot;</span><span class="p">,</span> <span class="n">GeoIP</span><span class="o">.</span><span class="n">GEOIP_INDEX_CACHE</span> <span class="o">|</span> <span class="n">GeoIP</span><span class="o">.</span><span class="n">GEOIP_CHECK_CACHE</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Obtiene la IP Publica</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="c"># esta URL puede ser reemplazada con otra que preste similar servicio</span>
      </span><span class="line">    <span class="n">ip</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span>
      </span><span class="line">    <span class="s">&#39;http://www.whatismyip.com/automation/n09230945.asp&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">ip</span>
      </span><span class="line"><span class="k">except</span><span class="p">:</span> <span class="c"># que hacer si falla la conectividad</span>
      </span><span class="line">    <span class="k">print</span> <span class="p">(</span><span class="s">&quot;ERROR: Network error!!!. &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Obtiene los datos de la DataBase usando la IP Publica</span>
      </span><span class="line"><span class="n">data</span> <span class="o">=</span> <span class="n">gi</span><span class="o">.</span><span class="n">record_by_name</span><span class="p">(</span><span class="n">ip</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Imprime los datos en la linea de comandos</span>
      </span><span class="line"><span class="k">print</span> <span class="n">data</span>
      </span>

**Ejemplo:**

::

   .. raw:: html
      <span class="line"><span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="nb">bin</span><span class="o">/</span><span class="n">env</span> <span class="n">python</span> <span class="n">geolocation</span><span class="o">.</span><span class="n">py</span>
      </span><span class="line"><span class="mf">190.17</span><span class="o">.</span><span class="mf">169.</span><span class="n">XXX</span>
      </span><span class="line"><span class="p">{</span><span class="s">&#39;city&#39;</span><span class="p">:</span> <span class="s">&#39;XXXXXX&#39;</span><span class="p">,</span> <span class="s">&#39;region_name&#39;</span><span class="p">:</span> <span class="s">&#39;Buenos Aires&#39;</span><span class="p">,</span> <span class="s">&#39;region&#39;</span><span class="p">:</span> <span class="s">&#39;01&#39;</span><span class="p">,</span> <span class="s">&#39;area_code&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&#39;time_zone&#39;</span><span class="p">:</span> <span class="s">&#39;America/Argentina/Buenos_Aires&#39;</span><span class="p">,</span> <span class="s">&#39;longitude&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mf">58.92079000071094</span><span class="p">,</span> <span class="s">&#39;metro_code&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&#39;country_code3&#39;</span><span class="p">:</span> <span class="s">&#39;ARG&#39;</span><span class="p">,</span> <span class="s">&#39;latitude&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mf">34.17680005629883</span><span class="p">,</span> <span class="s">&#39;postal_code&#39;</span><span class="p">:</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&#39;dma_code&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&#39;country_code&#39;</span><span class="p">:</span> <span class="s">&#39;AR&#39;</span><span class="p">,</span> <span class="s">&#39;country_name&#39;</span><span class="p">:</span> <span class="s">&#39;Argentina&#39;</span><span class="p">}</span>
      </span>

**Colaboracion:** *Si tenes conectividad con internet con ip version 6 NATIVA, puedes documentar tu experiencia aqui.*

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

