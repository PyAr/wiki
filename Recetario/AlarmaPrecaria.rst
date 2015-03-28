#format rst

Alarma Precaria
===============

Alarma mínima y básica de linea de comandos.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="n">not_executed</span> <span class="o">=</span> <span class="mi">1</span>
      </span><span class="line"><span class="k">while</span><span class="p">(</span><span class="n">not_executed</span><span class="p">):</span>
      </span><span class="line">    <span class="n">dt</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">localtime</span><span class="p">())</span>
      </span><span class="line">    <span class="n">hour</span> <span class="o">=</span> <span class="n">dt</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
      </span><span class="line">    <span class="n">minute</span> <span class="o">=</span> <span class="n">dt</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span>
      </span><span class="line">    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">hour</span> <span class="o">==</span> <span class="mi">8</span> <span class="ow">and</span> <span class="n">minute</span> <span class="o">==</span> <span class="mi">30</span><span class="p">:</span> <span class="c"># modificar hour y minute a la hora deseada</span>
      </span><span class="line">        <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&quot;xdg-open /home/user/ring.ogg&quot;</span><span class="p">)</span> <span class="c"># RingTone (?)</span>
      </span><span class="line">        <span class="n">not_executed</span> <span class="o">=</span> <span class="mi">0</span>
      </span>

Comentarios
-----------

Facundo
~~~~~~~

Hay un par de cambios triviales para hacerle: se puede reemplazar el not_executed por un break, no hace falta declarar el encoding, y usar localtime() como corresponde..

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="k">while</span><span class="p">(</span><span class="bp">True</span><span class="p">):</span>
      </span><span class="line">    <span class="n">dt</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">localtime</span><span class="p">()</span>
      </span><span class="line">    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">dt</span><span class="o">.</span><span class="n">tm_hour</span> <span class="o">==</span> <span class="mi">8</span> <span class="ow">and</span> <span class="n">dt</span><span class="o">.</span><span class="n">tm_min</span> <span class="o">==</span> <span class="mi">30</span><span class="p">:</span> <span class="c"># modificar hour y minute a la hora deseada</span>
      </span><span class="line">        <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&quot;xdg-open /home/user/ring.ogg&quot;</span><span class="p">)</span> <span class="c"># RingTone (?)</span>
      </span><span class="line">        <span class="k">break</span>
      </span>

... pero realmente está mal planteado la resolución: no hay que usar un while ahí:

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># modificar hour y minute a la hora deseada</span>
      </span><span class="line"><span class="n">HOUR</span> <span class="o">=</span> <span class="mi">8</span>
      </span><span class="line"><span class="n">MIN</span> <span class="o">=</span> <span class="mi">30</span>
      </span><span class="line">
      </span><span class="line"><span class="n">t</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">localtime</span><span class="p">()</span>
      </span><span class="line"><span class="n">nowhms</span> <span class="o">=</span> <span class="n">t</span><span class="o">.</span><span class="n">tm_hour</span> <span class="o">*</span> <span class="mi">3600</span> <span class="o">+</span> <span class="n">t</span><span class="o">.</span><span class="n">tm_min</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="n">t</span><span class="o">.</span><span class="n">tm_sec</span>
      </span><span class="line"><span class="n">alarm</span> <span class="o">=</span> <span class="n">HOUR</span> <span class="o">*</span> <span class="mi">3600</span> <span class="o">+</span> <span class="n">MIN</span> <span class="o">*</span> <span class="mi">60</span>
      </span><span class="line"><span class="n">delta</span> <span class="o">=</span> <span class="n">alarm</span> <span class="o">-</span> <span class="n">nowhms</span>
      </span><span class="line"><span class="k">if</span> <span class="n">delta</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
      </span><span class="line">    <span class="c"># tomorrow</span>
      </span><span class="line">    <span class="n">delta</span> <span class="o">+=</span> <span class="mi">3600</span> <span class="o">*</span> <span class="mi">24</span>
      </span><span class="line"><span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">delta</span><span class="p">)</span>
      </span><span class="line"><span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&quot;xdg-open /home/user/ring.ogg&quot;</span><span class="p">)</span> <span class="c"># RingTone (?)</span>
      </span>

DanielMoisset
~~~~~~~~~~~~~

Yo prefiero no scar cuentas de fecha a mano, y en vez que datetime haga el trabajo sucio. Sobre todo porque maneja mejor casos delicados (que pasa si pongo la alarma justo antes de un cambio a horario de verano?) sin tener que pensarlos

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">datetime</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># modificar hour y minute a la hora deseada</span>
      </span><span class="line">
      </span><span class="line"><span class="n">HOUR</span> <span class="o">=</span> <span class="mi">8</span>
      </span><span class="line"><span class="n">MIN</span> <span class="o">=</span> <span class="mi">30</span>
      </span><span class="line">
      </span><span class="line"><span class="n">now</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
      </span><span class="line"><span class="n">alarm</span> <span class="o">=</span> <span class="n">now</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">hour</span><span class="o">=</span><span class="n">HOUR</span><span class="p">,</span> <span class="n">minute</span><span class="o">=</span><span class="n">MIN</span><span class="p">)</span>
      </span><span class="line"><span class="k">if</span> <span class="n">alarm</span> <span class="o">&lt;</span> <span class="n">now</span><span class="p">:</span>
      </span><span class="line">    <span class="c"># Set the alarm tomorrow</span>
      </span><span class="line">    <span class="n">alarm</span> <span class="o">+=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line"><span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">((</span><span class="n">alarm</span><span class="o">-</span><span class="n">now</span><span class="p">)</span><span class="o">.</span><span class="n">seconds</span><span class="p">)</span>
      </span><span class="line"><span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&quot;xdg-open /home/user/ring.ogg&quot;</span><span class="p">)</span> <span class="c"># RingTone (?)</span>
      </span>

Juancarlospaco
~~~~~~~~~~~~~~

*Por lo menos en Linux se necesita el Shebang y declarar encoding, por que sino al usar "Vídeo-de-Música.ogv" de Ringtone traen problemas los acentos.*

-------------------------



A esta altura creo que es mas importante agregar el correcto coloreado de sintaxis y cuidar la ortografia, a discutir si poner o no el encoding y el shebang. La idea es que las recetas sean genericas, con ese encoding y ese shebang, no cubris todos los casos. Pej, copias y pegas, y tu editor guarda en latin1??

Si funciona con:

::

   .. raw:: html
      <span class="line">usuario@maquina: ~<span class="nv">$ </span>python receta.py
      </span>

Es mas que suficiente. -- JoaquinSorianello_ `[[DateTime(2010-11-08T10:56:40-0300)]]`_

-------------------------



-------------------------



  CategoryRecetas_

