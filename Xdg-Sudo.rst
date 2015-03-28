#format rst

Xdg-Sudo
========

El sudo grafico universal para escritorios GTK/QT/loquesea, inspirado en el funcionamiento de xdg-open.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c"># Licence: GPLv3</span>
      </span><span class="line"><span class="c"># xdg-sudo: Automatically choose &quot;gksudo&quot; or &quot;kdesudo&quot; </span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="c">#import antigravity</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">subprocess</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">re</span>
      </span><span class="line"><span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">geteuid</span><span class="p">()</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span> <span class="c"># non-root check, because if you are root, all this is pointless</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="s">&quot; ERROR: Do not run as root...</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="k">else</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="p">(</span><span class="s">&quot; You are normal user... </span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># Prepare actual command to execute</span>
      </span><span class="line"><span class="n">parameters</span> <span class="o">=</span> <span class="s">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">re</span><span class="o">.</span><span class="n">escape</span><span class="p">(</span><span class="n">a</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]])</span>
      </span><span class="line"><span class="c"># Test which tools exist</span>
      </span><span class="line"><span class="n">kdesudo</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s">&#39;/usr/bin/kdesudo&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">gtksudo</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s">&#39;/usr/bin/gksudo&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># If we have at least one of them, check which one to use.</span>
      </span><span class="line"><span class="k">if</span> <span class="n">kdesudo</span> <span class="ow">or</span> <span class="n">gtksudo</span><span class="p">:</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">kdesudo</span> <span class="ow">and</span> <span class="n">gtksudo</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># Test if gnome runs</span>
      </span><span class="line">        <span class="n">process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span><span class="s">&quot;ps -ae | grep gnome-session&quot;</span><span class="p">,</span> <span class="n">shell</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span>
      </span><span class="line">        <span class="n">process</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span>
      </span><span class="line">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">process</span><span class="o">.</span><span class="n">communicate</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span>
      </span><span class="line">            <span class="n">useGnome</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="n">useGnome</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">    <span class="k">elif</span> <span class="n">kdesudo</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">gtksudo</span><span class="p">):</span>
      </span><span class="line">        <span class="n">useGnome</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">    <span class="k">elif</span> <span class="p">(</span><span class="ow">not</span> <span class="n">kdesudo</span><span class="p">)</span> <span class="ow">and</span> <span class="n">gtksudo</span><span class="p">:</span>
      </span><span class="line">        <span class="n">useGnome</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">    <span class="c"># really run it</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">useGnome</span><span class="p">:</span>
      </span><span class="line">        <span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;gksudo &quot;</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;kdesudo &quot;</span>
      </span><span class="line">    <span class="c"># Run the actual program now</span>
      </span><span class="line">    <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="n">cmd</span><span class="o">+</span><span class="n">parameters</span><span class="p">)</span>
      </span><span class="line"><span class="k">else</span><span class="p">:</span>
      </span><span class="line">    <span class="c"># we dont have gksudo or kdesudo, OMFG!</span>
      </span><span class="line">    <span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;xterm -e </span><span class="se">\&quot;</span><span class="s">echo &#39;Neither </span><span class="se">\\\&quot;</span><span class="s">gksudo</span><span class="se">\\\&quot;</span><span class="s"> nor </span><span class="se">\\\&quot;</span><span class="s">kdesudo</span><span class="se">\\\&quot;</span><span class="s"> have been found on your machine. Thus, </span><span class="se">\\\&quot;</span><span class="s">sudo</span><span class="se">\\\&quot;</span><span class="s"> is being used. Please leave this window open until the program has finished. Your are asked for your password below.&#39;; sudo &quot;</span><span class="o">+</span><span class="n">parameters</span><span class="o">+</span><span class="s">&quot;; sleep 1</span><span class="se">\&quot;</span><span class="s">&quot;</span>
      </span><span class="line">    <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span> 
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

