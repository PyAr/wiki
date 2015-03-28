#format rst

Keyboard Leds Demo
==================

* Como controlar los 3 Leds del Teclado usando Python, ejemplo simple, requiere Privilegios elevados en el equipo.

**Nota:** *Si tu teclado es a Baterias (Bluetooth, Wireless), el uso intensivo de este Script reducira la duracion de las mismas.*

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">fcntl</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line">
      </span><span class="line"><span class="n">KDSETLED</span> <span class="o">=</span> <span class="mh">0x4B32</span>
      </span><span class="line"><span class="n">SCR_LED</span>  <span class="o">=</span> <span class="mh">0x01</span>
      </span><span class="line"><span class="n">NUM_LED</span>  <span class="o">=</span> <span class="mh">0x02</span>
      </span><span class="line"><span class="n">CAP_LED</span>  <span class="o">=</span> <span class="mh">0x04</span>
      </span><span class="line">
      </span><span class="line"><span class="n">console_fd</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s">&#39;/dev/console&#39;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">O_NOCTTY</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">all_on</span> <span class="o">=</span> <span class="n">SCR_LED</span> <span class="o">|</span> <span class="n">NUM_LED</span> <span class="o">|</span> <span class="n">CAP_LED</span>
      </span><span class="line"><span class="n">all_off</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">
      </span><span class="line"><span class="k">while</span> <span class="mi">1</span><span class="p">:</span>
      </span><span class="line">    <span class="n">fcntl</span><span class="o">.</span><span class="n">ioctl</span><span class="p">(</span><span class="n">console_fd</span><span class="p">,</span> <span class="n">KDSETLED</span><span class="p">,</span> <span class="n">all_on</span><span class="p">)</span>
      </span><span class="line">    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span> <span class="c"># Aca se cambia el tiempo, o podria realizar una funcion mas compleja</span>
      </span><span class="line">    <span class="n">fcntl</span><span class="o">.</span><span class="n">ioctl</span><span class="p">(</span><span class="n">console_fd</span><span class="p">,</span> <span class="n">KDSETLED</span><span class="p">,</span> <span class="n">all_off</span><span class="p">)</span>
      </span><span class="line">    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span> <span class="c"># Here changes the Timming, or something more complex</span>
      </span>

**Ejemplo:**

::

   sudo /usr/bin/env python keyboardleds.py

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

-------------------------



  CategoryRecetas_

