#format rst

La siguiente macro, detecta el tipo de documento (Calc, Writer, Draw, Impress, etc) desde el cual se ejecuta.

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">uno</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">quien_soy</span><span class="p">():</span>
      </span><span class="line">    <span class="n">doc</span> <span class="o">=</span> <span class="n">XSCRIPTCONTEXT</span><span class="o">.</span><span class="n">getDocument</span><span class="p">()</span>
      </span><span class="line">    <span class="n">msgbox</span><span class="p">(</span><span class="n">obtener_tipo</span><span class="p">(</span><span class="n">doc</span><span class="p">))</span>
      </span><span class="line">    <span class="k">return</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">obtener_tipo</span><span class="p">(</span><span class="n">doc</span><span class="p">):</span>
      </span><span class="line">    <span class="n">tipo</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;com.sun.star.sheet.SpreadsheetDocument&#39;</span><span class="p">:</span> <span class="s">&#39;Calc&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.text.TextDocument&#39;</span><span class="p">:</span> <span class="s">&#39;Writer&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.presentation.PresentationDocument&#39;</span><span class="p">:</span> <span class="s">&#39;Impress&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.drawing.DrawingDocument&#39;</span><span class="p">:</span> <span class="s">&#39;Draw&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.sdb.OfficeDatabaseDocument&#39;</span><span class="p">:</span> <span class="s">&#39;Base&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.formula.FormulaProperties&#39;</span><span class="p">:</span> <span class="s">&#39;Math&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="s">&#39;com.sun.star.script.BasicIDE&#39;</span><span class="p">:</span> <span class="s">&#39;Basic&#39;</span><span class="p">}</span>
      </span><span class="line">    <span class="c"># iteramos entre los tipos de documentos</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tipo</span><span class="p">:</span>
      </span><span class="line">        <span class="c"># validamos si soporta el servicio</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">doc</span><span class="o">.</span><span class="n">supportsService</span><span class="p">(</span><span class="n">t</span><span class="p">):</span>
      </span><span class="line">            <span class="c"># devolvemos el tipo de documento</span>
      </span><span class="line">            <span class="k">return</span> <span class="s">&#39;Soy </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">tipo</span><span class="p">[</span><span class="n">t</span><span class="p">]</span>
      </span><span class="line">    <span class="c"># si termina sin encontrar un tipo</span>
      </span><span class="line">    <span class="k">return</span> <span class="s">&#39;No se que tipo soy&#39;</span>
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

Para saber donde guardar estas macros, mira el wiki de Apache OpenOffice_: http://wiki.openoffice.org/wiki/ES/Manuales/GuiaAOO/TemasAvanzados/Macros/Python

