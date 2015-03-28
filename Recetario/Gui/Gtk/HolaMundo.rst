
GtkHolaMundo
------------

Crea y muestra una ventana que muestra el famoso mensaje hola mundo.

`Hola mundo.png </wiki/Recetario/Gui/Gtk/HolaMundo/attachment/582/Hola%20mundo.png>`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># se crea la ventana</span>
      </span><span class="line"><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="c"># seteamos el tamanio de la ventana</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span>
      </span><span class="line"><span class="c"># se crea la etiqueta que va a mostrar el mensaje</span>
      </span><span class="line"><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&quot;Hola pyar!&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># se setea el el titulo de la ventana</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&quot;hola mundo&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># agregamos el label a la ventana</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line"><span class="c"># mostramos la ventana y todo lo que contiene</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">on_window_close</span><span class="p">(</span><span class="n">window</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;este metodo es llamado cuando se aprieta la equis para cerrar la </span>
      </span><span class="line"><span class="sd">    ventana&#39;&#39;&#39;</span>
      </span><span class="line">    <span class="c"># cerramos el programa retornando 0 (exito)</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># conectamos la senial delete-event que es emitida cuando se presiona la</span>
      </span><span class="line"><span class="c"># equis en la ventana</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;delete-event&quot;</span><span class="p">,</span> <span class="n">on_window_close</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># llamamos al main loop para que muestre la ventana y</span>
      </span><span class="line"><span class="c"># procese los eventos</span>
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

