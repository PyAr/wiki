#format rst
## page was renamed from Recetario/Gtk/LabelConColor

Gtk Label Con Color
===================

ejemplo de como cambiar el color de un label sin usar pango markup 

observaciones, si se comenta label.realize() el color que se imprime no es el que seteamos si no el por defecto.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;label&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line"><span class="n">label</span><span class="o">.</span><span class="n">modify_fg</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">STATE_NORMAL</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">color_parse</span><span class="p">(</span><span class="s">&#39;#f00&#39;</span><span class="p">))</span>
      </span><span class="line"><span class="n">label</span><span class="o">.</span><span class="n">realize</span><span class="p">()</span>
      </span><span class="line"><span class="k">print</span> <span class="n">label</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">fg</span><span class="p">[</span><span class="n">gtk</span><span class="o">.</span><span class="n">STATE_NORMAL</span><span class="p">]</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

