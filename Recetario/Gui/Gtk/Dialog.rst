#format rst
## page was renamed from Recetario/Gtk/Dialog

GtkDialog
---------

ejemplo para crear dialogos modales de distintos tipos con distintos botones

`attachment:dialog1.png`_ `attachment:dialog2.png`_ `attachment:dialog3.png`_ `attachment:dialog4.png`_

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># por defecto crea un mensaje de informacion sin botones</span>
      </span><span class="line"><span class="n">info</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="n">message_format</span><span class="o">=</span><span class="s">&quot;informacion!&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># tipo advertencia con un boton de ok</span>
      </span><span class="line"><span class="n">warning</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">MESSAGE_WARNING</span><span class="p">,</span>
      </span><span class="line">    <span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_OK_CANCEL</span><span class="p">,</span> <span class="n">message_format</span><span class="o">=</span><span class="s">&quot;advertencia..&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># pregunta con botones si no</span>
      </span><span class="line"><span class="n">question</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">MESSAGE_QUESTION</span><span class="p">,</span>
      </span><span class="line">    <span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_YES_NO</span><span class="p">,</span> <span class="n">message_format</span><span class="o">=</span><span class="s">&quot;pregunta?&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># error con boton ok</span>
      </span><span class="line"><span class="n">error</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">MessageDialog</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">MESSAGE_ERROR</span><span class="p">,</span>
      </span><span class="line">    <span class="n">buttons</span><span class="o">=</span><span class="n">gtk</span><span class="o">.</span><span class="n">BUTTONS_OK</span><span class="p">,</span> <span class="n">message_format</span><span class="o">=</span><span class="s">&quot;error!?!&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># run bloquea hasta que se produzca un evento y devuelve el valor del evento</span>
      </span><span class="line"><span class="k">if</span> <span class="n">info</span><span class="o">.</span><span class="n">run</span><span class="p">()</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_DELETE_EVENT</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;si, es la unica senial que puede emitir, ya que no tiene botones&quot;</span>
      </span><span class="line"><span class="c"># hay que esconder el dialogo</span>
      </span><span class="line"><span class="n">info</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># almacenamos el valor de retorno en una variable para controlar varios valores</span>
      </span><span class="line"><span class="n">response</span> <span class="o">=</span> <span class="n">warning</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line"><span class="n">warning</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">response</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_OK</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;advertencia respondio aceptar&quot;</span>
      </span><span class="line"><span class="k">elif</span> <span class="n">response</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_CANCEL</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;advertencia respondio cancel&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="n">response</span> <span class="o">=</span> <span class="n">question</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">response</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_YES</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;respondio si!&quot;</span>
      </span><span class="line"><span class="k">elif</span> <span class="n">response</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_NO</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;respondio no :(&quot;</span>
      </span><span class="line">   
      </span><span class="line"><span class="n">question</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">error</span><span class="o">.</span><span class="n">run</span><span class="p">()</span> <span class="o">==</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_OK</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;error OK&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="n">error</span><span class="o">.</span><span class="n">hide</span><span class="p">()</span>
      </span><span class="line"><span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

