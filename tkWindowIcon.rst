#format rst

tkWindowIcon
------------

Crea una ventana con Icono de ventana. Si es en Windows sacar el '@'+ de la ruta al icono. Los archivos se pueden pasar a .XBM con Gimp.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c">#-*- coding:utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="n">root</span><span class="o">.</span><span class="n">wm_iconbitmap</span><span class="p">(</span><span class="s">&#39;@&#39;</span><span class="o">+</span><span class="s">&#39;/usr/include/X11/bitmaps/icon&#39;</span><span class="p">)</span>  <span class="c"># Ruta al icono, formato .XBM</span>
      </span><span class="line"><span class="k">except</span> <span class="n">TclError</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; ERROR: Icon File not found... &quot;</span><span class="p">)</span> <span class="c"># imprime este mensaje si el icono no se encuentra</span>
      </span><span class="line">    <span class="k">print</span><span class="p">(</span><span class="s">&quot; &quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">pass</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

