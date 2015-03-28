#format rst
## page was renamed from Recetario/Gtk/XMLRPCServer

Servidor XMLRPC dentro de un hilo gtk

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">SimpleXMLRPCServer</span> <span class="kn">import</span> <span class="n">SimpleXMLRPCServer</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gobject</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">time</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">hello</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
      </span><span class="line">        <span class="n">dialog</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Dialog</span><span class="p">(</span><span class="s">&quot;Hello dialog&quot;</span><span class="p">,</span>
      </span><span class="line">                        <span class="bp">None</span><span class="p">,</span>
      </span><span class="line">                        <span class="n">gtk</span><span class="o">.</span><span class="n">DIALOG_MODAL</span> <span class="o">|</span> <span class="n">gtk</span><span class="o">.</span><span class="n">DIALOG_DESTROY_WITH_PARENT</span><span class="p">,</span>
      </span><span class="line">                        <span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_CANCEL</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_CANCEL</span><span class="p">,</span>
      </span><span class="line">                                <span class="n">gtk</span><span class="o">.</span><span class="n">STOCK_OK</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">RESPONSE_ACCEPT</span><span class="p">,)</span>
      </span><span class="line">                        <span class="p">)</span>
      </span><span class="line">        <span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Hello </span><span class="si">%s</span><span class="s">&#39;</span><span class="o">%</span><span class="n">name</span><span class="p">)</span>
      </span><span class="line">        <span class="n">dialog</span><span class="o">.</span><span class="n">vbox</span><span class="o">.</span><span class="n">pack_start</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line">        <span class="n">label</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">        <span class="n">response</span> <span class="o">=</span> <span class="n">dialog</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span><span class="line">        <span class="n">dialog</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">response</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">change_time</span><span class="p">(</span><span class="n">label</span><span class="p">):</span>
      </span><span class="line">        <span class="n">label</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()))</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">handle_request</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">condition</span><span class="p">,</span> <span class="n">webservice</span><span class="p">):</span>
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">                <span class="n">webservice</span><span class="o">.</span><span class="n">handle_request</span><span class="p">()</span>
      </span><span class="line">        <span class="k">except</span><span class="p">:</span>
      </span><span class="line">                <span class="k">pass</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="n">s</span> <span class="o">=</span> <span class="n">SimpleXMLRPCServer</span><span class="p">((</span><span class="s">&#39;localhost&#39;</span><span class="p">,</span><span class="mi">8080</span><span class="p">))</span>
      </span><span class="line"><span class="n">s</span><span class="o">.</span><span class="n">register_function</span><span class="p">(</span><span class="n">hello</span><span class="p">)</span>
      </span><span class="line"><span class="n">gobject</span><span class="o">.</span><span class="n">io_add_watch</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">gobject</span><span class="o">.</span><span class="n">IO_IN</span><span class="p">,</span>
      </span><span class="line">                     <span class="n">handle_request</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span>
      </span><span class="line"><span class="n">win</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line"><span class="n">win</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;destroy&#39;</span><span class="p">,</span> <span class="n">gtk</span><span class="o">.</span><span class="n">main_quit</span><span class="p">)</span>
      </span><span class="line"><span class="n">win</span><span class="o">.</span><span class="n">set_size_request</span><span class="p">(</span><span class="mi">300</span><span class="p">,</span><span class="mi">300</span><span class="p">)</span>
      </span><span class="line"><span class="n">label</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s">&#39;Main window&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">gobject</span><span class="o">.</span><span class="n">timeout_add</span><span class="p">(</span><span class="mi">100</span><span class="p">,</span> <span class="n">change_time</span><span class="p">,</span> <span class="n">label</span><span class="p">)</span>
      </span><span class="line"><span class="n">win</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
      </span><span class="line"><span class="n">win</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line"><span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span>

-------------------------



  CategoryRecetas_

