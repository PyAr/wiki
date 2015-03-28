
GtkErrorHandler
===============

Si aplicamos el decorador error_handler a una función, cuando lance una excepción, vamos a obtener un dialogo modal mostrandomos el traceback.  Recomiendo usarlo solo para debug o versiones beta, un usuario no debería ver el traceback crudo.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">error_handler</span><span class="p">(</span><span class="n">function</span><span class="p">):</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">out</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
      </span><span class="line">       
      </span><span class="line">        <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
      </span><span class="line">            <span class="k">raise</span> <span class="ne">KeyboardInterrupt</span>
      </span><span class="line">       
      </span><span class="line">        <span class="k">except</span><span class="p">:</span>
      </span><span class="line">            <span class="kn">from</span> <span class="nn">traceback</span> <span class="kn">import</span> <span class="n">format_exc</span>
      </span><span class="line">            <span class="n">error</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span>
      </span><span class="line">                <span class="nb">type</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">MESSAGE_ERROR</span><span class="p">,</span>
      </span><span class="line">                <span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_OK</span><span class="p">,</span>
      </span><span class="line">                <span class="n">message_format</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">format_exc</span><span class="p">())</span>
      </span><span class="line">                <span class="p">)</span>
      </span><span class="line">            <span class="n">error</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;Something went wrong!&quot;</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">error</span><span class="o">.</span><span class="n">run</span><span class="p">()</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_OK</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;Error OK&quot;</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;Error closed&quot;</span>
      </span><span class="line">            <span class="n">error</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">out</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Gui</span><span class="p">:</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span><span class="mi">200</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;Simple PyGTK example&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">vbox</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">VBox</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">button</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="s">&quot;Click me!&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">button</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">vbox</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">button</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;clicked&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_clicked</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;destroy&quot;</span><span class="p">,</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">())</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">window</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="nd">@error_handler</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_clicked</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">widget</span><span class="p">):</span>
      </span><span class="line">       <span class="k">raise</span> <span class="ne">IndexError</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">app</span> <span class="o">=</span> <span class="n">Gui</span><span class="p">()</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

