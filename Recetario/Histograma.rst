#format rst
## page was renamed from recetario/Histograma

Cómo generar un histograma
==========================

Ejemplo super sencillo mostrado en la Tribu el 31/JUL/2010 sobre cómo usar matplotlib desde la consola.

Para mas información, revisar:

* Matplotlib_

* `Documentación de hist`_

::

   .. raw:: html
      <span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">matplotlib.pylab</span> <span class="kn">import</span> <span class="n">hist</span><span class="p">,</span> <span class="n">show</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">plata</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">plata</span><span class="o">.</span><span class="n">extend</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">50</span><span class="p">])</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">20</span><span class="p">]</span><span class="o">*</span><span class="mi">10</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">10</span><span class="p">]</span><span class="o">*</span><span class="mi">13</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">5</span><span class="p">]</span><span class="o">*</span><span class="mi">8</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">2</span><span class="p">]</span><span class="o">*</span><span class="mi">35</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="p">([</span><span class="mi">1</span><span class="p">]</span><span class="o">*</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">plata</span>
      </span><span class="line"><span class="go">[50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, </span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">hist</span><span class="p">(</span><span class="n">plata</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">100</span><span class="p">))</span>
      </span><span class="line"><span class="go">(array([ 0,  1, 35,  0,  0, 15,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,</span>
      </span><span class="line"><span class="go">        0,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,</span>
      </span><span class="line"><span class="go">        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,</span>
      </span><span class="line"><span class="go">        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,</span>
      </span><span class="line"><span class="go">        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,</span>
      </span><span class="line"><span class="go">        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]), array([   0.,  </span>
      </span><span class="line"><span class="go">          9.,   10.,   11.,   12.,   13.,   14.,   15.,   16.,   17.,</span>
      </span><span class="line"><span class="go">         18.,   19.,   20.,   21.,   22.,   23.,   24.,   25.,   26.,</span>
      </span><span class="line"><span class="go">         27.,   28.,   29.,   30.,   31.,   32.,   33.,   34.,   35.,</span>
      </span><span class="line"><span class="go">         36.,   37.,   38.,   39.,   40.,   41.,   42.,   43.,   44.,</span>
      </span><span class="line"><span class="go">         45.,   46.,   47.,   48.,   49.,   50.,   51.,   52.,   53.,</span>
      </span><span class="line"><span class="go">         54.,   55.,   56.,   57.,   58.,   59.,   60.,   61.,   62.,</span>
      </span><span class="line"><span class="go">         63.,   64.,   65.,   66.,   67.,   68.,   69.,   70.,   71.,</span>
      </span><span class="line"><span class="go">         72.,   73.,   74.,   75.,   76.,   77.,   78.,   79.,   80.,</span>
      </span><span class="line"><span class="go">         81.,   82.,   83.,   84.,   85.,   86.,   87.,   88.,   89.,</span>
      </span><span class="line"><span class="go">         90.,   91.,   92.,   93.,   94.,   95.,   96.,   97.,   98.,</span>
      </span><span class="line"><span class="go">         99.,  100.]), &lt;a list of 100 Patch objects&gt;)</span>
      </span><span class="line"><span class="gp">&gt;&gt;&gt; </span><span class="n">show</span><span class="p">()</span>
      </span>

`attachment:ej_tribu.jpg`_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Matplotlib: http://matplotlib.sourceforge.net/

.. _Documentación de hist: http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist

