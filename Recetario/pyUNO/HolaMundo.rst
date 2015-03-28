
Todo un clásico... un Hola Mundo desde pyUNO

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">uno</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">hola_mundo</span><span class="p">():</span>
      </span><span class="line">    <span class="n">msgbox</span><span class="p">(</span><span class="s">&#39;Hola Mundo en PyUNO&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">return</span>
      </span><span class="line">   
      </span><span class="line"><span class="k">def</span> <span class="nf">msgbox</span><span class="p">(</span><span class="n">message</span><span class="p">):</span>
      </span><span class="line">    <span class="n">ctx</span> <span class="o">=</span> <span class="n">uno</span><span class="o">.</span><span class="n">getComponentContext</span><span class="p">()</span>
      </span><span class="line">    <span class="n">sm</span> <span class="o">=</span> <span class="n">ctx</span><span class="o">.</span><span class="n">getServiceManager</span><span class="p">()</span>
      </span><span class="line">    <span class="n">toolkit</span> <span class="o">=</span> <span class="n">sm</span><span class="o">.</span><span class="n">createInstanceWithContext</span><span class="p">(</span><span class="s">&#39;com.sun.star.awt.Toolkit&#39;</span><span class="p">,</span> <span class="n">ctx</span><span class="p">)</span>
      </span><span class="line">    <span class="n">msg</span> <span class="o">=</span> <span class="n">toolkit</span><span class="o">.</span><span class="n">createMessageBox</span><span class="p">(</span>
      </span><span class="line">                                <span class="n">toolkit</span><span class="o">.</span><span class="n">getDesktopWindow</span><span class="p">(),</span>
      </span><span class="line">                                <span class="s">&#39;infobox&#39;</span><span class="p">,</span>
      </span><span class="line">                                <span class="mi">1</span><span class="p">,</span>
      </span><span class="line">                                <span class="s">&#39;UNOPython&#39;</span><span class="p">,</span>
      </span><span class="line">                                <span class="nb">str</span><span class="p">(</span><span class="n">message</span><span class="p">))</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">msg</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
      </span>

Para saber donde guardar esta macro, mira el wiki de Apache OpenOffice_: http://wiki.openoffice.org/wiki/ES/Manuales/GuiaAOO/TemasAvanzados/Macros/Python

Para ejecutar la macro, desde cualquier aplicación de Apache OpenOffice_, menú Herramientas -> Macros -> Ejecutar macros...

