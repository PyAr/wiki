#format rst
## page was renamed from Recetario/Gtk/PrintNonGtk

GtkPrintNonGtk
==============

Este ejemplo muestra como usar gtk para mostrar el dialogo de imprimir pero sin usar el main loop.

  Es útil para aplicaciones no gtk que solo quieren usar el dialogo de impresión pero tienen otro main loop que no es el de gtk.

explicación: lo que hacemos después de mostrar el dialogo es procesar los eventos de gtk mientras haya eventos pendientes, luego seguimos en nuestra aplicación normalmente.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line">
      </span><span class="line"><span class="n">po</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">PrintOperation</span><span class="p">()</span>
      </span><span class="line"><span class="n">pa</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">PRINT_OPERATION_ACTION_PRINT_DIALOG</span>
      </span><span class="line"><span class="n">po</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">pa</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">while</span> <span class="n">gtk</span><span class="o">.</span><span class="n">events_pending</span><span class="p">():</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main_iteration</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&#39;y seguimos como si nada&#39;</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&#39;esperamos 3 segundos&#39;</span>
      </span><span class="line"><span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&#39;chau&#39;</span>
      </span>

`attachment:Imprimir.png`_

