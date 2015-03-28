
Emulador de terminal con Gtk y VTE
==================================

un ejemplo de como hacer una terminal visual al estilo gnome-terminal 

`pyshell.png </wiki/Recetario/Gui/Gtk/EmuladorTerminal/attachment/590/pyshell.png>`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">vte</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;pyshell&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">scroll</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">ScrolledWindow</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">shell</span> <span class="o">=</span> <span class="n">vte</span><span class="o">.</span><span class="n">Terminal</span><span class="p">()</span>
      </span><span class="line"><span class="n">shell</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;child-exited&quot;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line"><span class="n">shell</span><span class="o">.</span><span class="n">fork_command</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">scroll</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">shell</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">scroll</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

