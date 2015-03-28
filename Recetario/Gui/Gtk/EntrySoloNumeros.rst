#format rst
## page was renamed from Recetario/Gtk/EntrySoloNumeros

GtkEntrySoloNumeros
===================

Este ejemplo muestra como permitir el ingreso de solo números en un gtk.Entry, a través de la señal insert-text_ de gtk.Editable (clase de la que hereda gtk.Entry) y usando el método stop_emission_ de gobject para vitar que la señal se propague y sea manejada por el handler por defecto para la señal (que es el que inserta el carácter en el widget)

`attachment:Only numbers.png`_

::

   .. raw:: html
      <span class="line"><span class="sd">&#39;&#39;&#39;ejemplo sobre solo dejar ingresar numeros en un campo de text</span>
      </span><span class="line"><span class="sd">tambien sirve para cadenas de texto pegadas en el entry con ctrl-v</span>
      </span><span class="line"><span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">re</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line">
      </span><span class="line"><span class="n">ONLY_NUMBERS</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;^[0-9]*$&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">on_insert_text</span><span class="p">(</span><span class="n">editable</span><span class="p">,</span> <span class="n">new_text</span><span class="p">,</span> <span class="n">new_text_length</span><span class="p">,</span> <span class="n">position</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;called when text is inserted on an entry&#39;&#39;&#39;</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">ONLY_NUMBERS</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">new_text</span><span class="p">)</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">        <span class="n">editable</span><span class="o">.</span><span class="n">stop_emission</span><span class="p">(</span><span class="s">&#39;insert-text&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">entry</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Entry</span><span class="p">()</span>
      </span><span class="line"><span class="n">entry</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;insert-text&#39;</span><span class="p">,</span> <span class="n">on_insert_text</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s">&#39;only numbers&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line"><span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

.. ############################################################################

.. _insert-text: http://library.gnome.org/devel/pygtk/stable/class-gtkeditable.html#signal-gtkeditable--insert-text

.. _stop_emission: http://library.gnome.org/devel/pygobject/stable/class-gobject.html#method-gobject--stop-emission

