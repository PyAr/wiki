#format rst

Qt Imprimir Pagina Web a PDF
============================

ejemplo de como imprimir una pagina web a pdf

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyQt4.QtCore</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyQt4.QtGui</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyQt4.QtWebKit</span> <span class="kn">import</span> <span class="o">*</span>
      </span><span class="line">
      </span><span class="line"><span class="n">app</span> <span class="o">=</span> <span class="n">QApplication</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">web</span> <span class="o">=</span> <span class="n">QWebView</span><span class="p">()</span>
      </span><span class="line"> <span class="n">web</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">QUrl</span><span class="p">(</span><span class="s">&quot;http://www.google.com&quot;</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line"><span class="c">#web.show()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">printer</span> <span class="o">=</span> <span class="n">QPrinter</span><span class="p">()</span>
      </span><span class="line"><span class="n">printer</span><span class="o">.</span><span class="n">setPageSize</span><span class="p">(</span><span class="n">QPrinter</span><span class="o">.</span><span class="n">A4</span><span class="p">)</span>
      </span><span class="line"><span class="n">printer</span><span class="o">.</span><span class="n">setOutputFormat</span><span class="p">(</span><span class="n">QPrinter</span><span class="o">.</span><span class="n">PdfFormat</span><span class="p">)</span>
      </span><span class="line"><span class="n">printer</span><span class="o">.</span><span class="n">setOutputFileName</span><span class="p">(</span><span class="s">&quot;test.pdf&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">convertIt</span><span class="p">():</span>
      </span><span class="line">   <span class="n">web</span><span class="o">.</span><span class="n">print_</span><span class="p">(</span><span class="n">printer</span><span class="p">)</span>
      </span><span class="line">   <span class="k">print</span> <span class="s">&quot;Pdf generated&quot;</span>
      </span><span class="line">   <span class="n">QApplication</span><span class="o">.</span><span class="n">exit</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">QObject</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">web</span><span class="p">,</span> <span class="n">SIGNAL</span><span class="p">(</span><span class="s">&quot;loadFinished(bool)&quot;</span><span class="p">),</span> <span class="n">convertIt</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">app</span><span class="o">.</span><span class="n">exec_</span><span class="p">())</span>
      </span>

-------------------------



  CategoryRecetas_

