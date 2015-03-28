#format rst

Factura con PyFPDF
------------------

Descripción
:::::::::::

Esta receta es un ejemplo sencillo de como generar una factura en PDF utilizando la libreria PyFpdf_ (port de FPDF_ para python).

Para más detalles sobre la libreria PyFpdf_ y bajar una versión actualizada y mejorada, ir a: `sito del proyecto`_ (incluye este ejemplo)

La factura incluye logo, recuadros, textos y código de barra entrelazado 2 de 5, en un formato aplicable en Argentina. Ver muestra adjunta: `attachment:factura.pdf`_factura.pdf`attachment:None`_

Este ejemplo esta harcodeado, en la vida real habría que abstraerlo en alguna especie de plantilla para facilitar su modificación.

Ejemplo:
::::::::

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: iso-8859-1 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyFPDF</span> <span class="kn">import</span> <span class="n">FPDF</span>
      </span><span class="line">
      </span><span class="line"><span class="n">pdf</span> <span class="o">=</span> <span class="n">FPDF</span><span class="p">()</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">AddPage</span><span class="p">()</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">13.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">105.0</span><span class="p">,</span> <span class="mf">8.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">22.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;C&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">75.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Comprobante de Ejemplo&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Rect</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">15.0</span><span class="p">,</span> <span class="mf">170.0</span><span class="p">,</span> <span class="mf">245.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Rect</span><span class="p">(</span><span class="mf">95.0</span><span class="p">,</span> <span class="mf">15.0</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span><span class="s">&#39;serpiente.png&#39;</span><span class="p">,</span> <span class="mf">20.0</span><span class="p">,</span> <span class="mf">17.0</span><span class="p">,</span> <span class="n">link</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">13.0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">13.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">16.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">95.0</span><span class="p">,</span> <span class="mf">18.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;C&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">10.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;X&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">8.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">105.0</span><span class="p">,</span> <span class="mf">21.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">4.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;C&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">75.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Original&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">7.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">95.0</span><span class="p">,</span> <span class="mf">21.5</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">4.5</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;C&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">10.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;COD.00&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">100.0</span><span class="p">,</span> <span class="mf">25.0</span><span class="p">,</span> <span class="mf">100.0</span><span class="p">,</span> <span class="mf">57.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">14.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">125.0</span><span class="p">,</span> <span class="mf">25.5</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.5</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">60.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;00000001&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">115.0</span><span class="p">,</span> <span class="mf">27.5</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.5</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">10.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;N</span><span class="se">\xba</span><span class="s">: &#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">32.5</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">98.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;EMPRESA&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">115.0</span><span class="p">,</span> <span class="mf">33.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">60.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Fecha:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">135.0</span><span class="p">,</span> <span class="mf">33.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">40.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;19/02/2009&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">57.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">57.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">59.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">13.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Sr.(s):&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">35.0</span><span class="p">,</span> <span class="mf">59.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">140.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Mariano Reingart&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">64.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">18.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Domicilio:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">35.0</span><span class="p">,</span> <span class="mf">64.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">125.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Siempreviva 12345&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">69.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">18.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Tel</span><span class="se">\xe9</span><span class="s">fono:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">35.0</span><span class="p">,</span> <span class="mf">69.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">80.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;+1-5555-5555&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">115.0</span><span class="p">,</span> <span class="mf">69.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">18.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Localidad:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">133.0</span><span class="p">,</span> <span class="mf">69.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">6.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">42.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Springfield&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">77.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">77.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">80.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">15.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;IVA:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">35.0</span><span class="p">,</span> <span class="mf">80.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">70.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Responsable&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">115.0</span><span class="p">,</span> <span class="mf">80.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;CUIT:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">135.0</span><span class="p">,</span> <span class="mf">80.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">40.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;10-12345678-9&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">88.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">88.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">17.0</span><span class="p">,</span> <span class="mf">90.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">48.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Fecha de Vencimiento Pago:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">65.0</span><span class="p">,</span> <span class="mf">90.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;23/07/1978&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">92.0</span><span class="p">,</span> <span class="mf">90.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">43.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Per</span><span class="se">\xed</span><span class="s">odo Facturado&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">125.0</span><span class="p">,</span> <span class="mf">90.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;01/01/2009&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">150.0</span><span class="p">,</span> <span class="mf">90.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;31/01/2009&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">95.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">95.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">155.0</span><span class="p">,</span> <span class="mf">95.0</span><span class="p">,</span> <span class="mf">155.0</span><span class="p">,</span> <span class="mf">230.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">20.0</span><span class="p">,</span> <span class="mf">97.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">125.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Descripci</span><span class="se">\xf3</span><span class="s">n&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">160.0</span><span class="p">,</span> <span class="mf">97.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Importe&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">102.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">102.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">20.0</span><span class="p">,</span> <span class="mf">103.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">125.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Esto es una prueba y no es v</span><span class="se">\xe1</span><span class="s">lido como factura&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">160.0</span><span class="p">,</span> <span class="mf">103.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">20.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;100,00&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Line</span><span class="p">(</span><span class="mf">15.0</span><span class="p">,</span> <span class="mf">230.0</span><span class="p">,</span> <span class="mf">185.0</span><span class="p">,</span> <span class="mf">230.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">20.0</span><span class="p">,</span> <span class="mf">233.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">95.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;CAE N</span><span class="se">\xba</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">45.0</span><span class="p">,</span> <span class="mf">233.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">30.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;01234567890&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">105.0</span><span class="p">,</span> <span class="mf">234.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">45.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;NETO GRAVADO:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">145.0</span><span class="p">,</span> <span class="mf">234.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">33.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;100,00&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">20.0</span><span class="p">,</span> <span class="mf">238.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">95.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Fecha Vto. CAE:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">55.0</span><span class="p">,</span> <span class="mf">238.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">5.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">30.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;19/02/2009&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">125.0</span><span class="p">,</span> <span class="mf">241.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">25.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;IVA 21%:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">145.0</span><span class="p">,</span> <span class="mf">241.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">33.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;21,00&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Interleaved2of5</span><span class="p">(</span><span class="s">&#39;012345678905&#39;</span><span class="p">,</span> <span class="mf">20.0</span><span class="p">,</span> <span class="mf">243.5</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">0.75</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;B&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">105.0</span><span class="p">,</span> <span class="mf">251.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">73.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;121,00&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">12.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">125.0</span><span class="p">,</span> <span class="mf">251.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">9.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;R&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">25.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;Total:&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetLineWidth</span><span class="p">(</span><span class="mf">0.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Rect</span><span class="p">(</span><span class="mf">155.0</span><span class="p">,</span> <span class="mf">252.0</span><span class="p">,</span> <span class="mf">25.0</span><span class="p">,</span> <span class="mf">7.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetFont</span><span class="p">(</span><span class="s">&#39;arial&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="mf">10.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">SetXY</span><span class="p">(</span><span class="mf">20.0</span><span class="p">,</span> <span class="mf">253.0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Cell</span><span class="p">(</span><span class="n">ln</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">h</span><span class="o">=</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="n">w</span><span class="o">=</span><span class="mf">120.0</span><span class="p">,</span> <span class="n">txt</span><span class="o">=</span><span class="s">&#39;012345678905&#39;</span><span class="p">,</span> <span class="n">border</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">pdf</span><span class="o">.</span><span class="n">Output</span><span class="p">(</span><span class="s">&#39;c:/factura.pdf&#39;</span><span class="p">,</span> <span class="s">&#39;F&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s">&quot;c:/factura.pdf&quot;</span><span class="p">)</span>
      </span>

::

   # -*- coding: iso-8859-1 -*-
   #Actualizado 24/08/2012
   import os
   from fpdf import FPDF

   pdf = FPDF()
   pdf.add_page(orientation='P')
   pdf.set_font('arial', '', 13.0)
   pdf.set_xy(105.0, 8.0)
   pdf.cell(ln=0, h=22.0, align='C', w=75.0, txt='Comprobante de Ejemplo', border=0)
   pdf.set_line_width(0.0)
   pdf.rect(15.0, 15.0, 170.0, 245.0)
   pdf.set_line_width(0.0)
   pdf.rect(95.0, 15.0, 10.0, 10.0)
   #descomentar para poner imagen de la serpiente
   #pdf.image('serpiente.png', 20.0, 17.0, link='', type='', w=13.0, h=13.0)
   pdf.set_font('arial', 'B', 16.0)
   pdf.set_xy(95.0, 18.0)
   pdf.cell(ln=0, h=2.0, align='C', w=10.0, txt='X', border=0)
   pdf.set_font('arial', '', 8.0)
   pdf.set_xy(105.0, 21.0)
   pdf.cell(ln=0, h=4.0, align='C', w=75.0, txt='Original', border=0)
   pdf.set_font('arial', 'B', 7.0)
   pdf.set_xy(95.0, 21.5)
   pdf.cell(ln=0, h=4.5, align='C', w=10.0, txt='COD.00', border=0)
   pdf.set_line_width(0.0)
   pdf.line(100.0, 25.0, 100.0, 57.0)
   pdf.set_font('arial', 'B', 14.0)
   pdf.set_xy(125.0, 25.5)
   pdf.cell(ln=0, h=9.5, align='L', w=60.0, txt='00000001', border=0)
   pdf.set_xy(115.0, 27.5)
   pdf.cell(ln=0, h=5.5, align='L', w=10.0, txt='N\xba: ', border=0)
   pdf.set_font('arial', 'B', 12.0)
   pdf.set_xy(17.0, 32.5)
   pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='EMPRESA', border=0)
   pdf.set_font('arial', '', 12.0)
   pdf.set_xy(115.0, 33.0)
   pdf.cell(ln=0, h=7.0, align='L', w=60.0, txt='Fecha:', border=0)
   pdf.set_xy(135.0, 33.0)
   pdf.cell(ln=0, h=7.0, align='L', w=40.0, txt='19/02/2009', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 57.0, 185.0, 57.0)
   pdf.set_font('arial', '', 10.0)
   pdf.set_xy(17.0, 59.0)
   pdf.cell(ln=0, h=6.0, align='L', w=13.0, txt='Sr.(s):', border=0)
   pdf.set_xy(35.0, 59.0)
   pdf.cell(ln=0, h=6.0, align='L', w=140.0, txt='Mariano Reingart', border=0)
   pdf.set_xy(17.0, 64.0)
   pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Domicilio:', border=0)
   pdf.set_xy(35.0, 64.0)
   pdf.cell(ln=0, h=6.0, align='L', w=125.0, txt='Siempreviva 12345', border=0)
   pdf.set_xy(17.0, 69.0)
   pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Tel\xe9fono:', border=0)
   pdf.set_xy(35.0, 69.0)
   pdf.cell(ln=0, h=6.0, align='L', w=80.0, txt='+1-5555-5555', border=0)
   pdf.set_xy(115.0, 69.0)
   pdf.cell(ln=0, h=6.0, align='L', w=18.0, txt='Localidad:', border=0)
   pdf.set_xy(133.0, 69.0)
   pdf.cell(ln=0, h=6.0, align='L', w=42.0, txt='Springfield', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 77.0, 185.0, 77.0)
   pdf.set_xy(17.0, 80.0)
   pdf.cell(ln=0, h=5.0, align='L', w=15.0, txt='IVA:', border=0)
   pdf.set_xy(35.0, 80.0)
   pdf.cell(ln=0, h=5.0, align='L', w=70.0, txt='Responsable', border=0)
   pdf.set_xy(115.0, 80.0)
   pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='CUIT:', border=0)
   pdf.set_xy(135.0, 80.0)
   pdf.cell(ln=0, h=5.0, align='L', w=40.0, txt='10-12345678-9', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 88.0, 185.0, 88.0)
   pdf.set_xy(17.0, 90.0)
   pdf.cell(ln=0, h=5.0, align='L', w=48.0, txt='Fecha de Vencimiento Pago:', border=0)
   pdf.set_xy(65.0, 90.0)
   pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='23/07/1978', border=0)
   pdf.set_xy(92.0, 90.0)
   pdf.cell(ln=0, h=5.0, align='L', w=43.0, txt='Per\xedodo Facturado', border=0)
   pdf.set_xy(125.0, 90.0)
   pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='01/01/2009', border=0)
   pdf.set_xy(150.0, 90.0)
   pdf.cell(ln=0, h=5.0, align='L', w=20.0, txt='31/01/2009', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 95.0, 185.0, 95.0)
   pdf.set_line_width(0.0)
   pdf.line(155.0, 95.0, 155.0, 230.0)
   pdf.set_xy(20.0, 97.0)
   pdf.cell(ln=0, h=5.0, align='L', w=125.0, txt='Descripci\xf3n', border=0)
   pdf.set_xy(160.0, 97.0)
   pdf.cell(ln=0, h=5.0, align='R', w=20.0, txt='Importe', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 102.0, 185.0, 102.0)
   pdf.set_xy(20.0, 103.0)
   pdf.cell(ln=0, h=7.0, align='L', w=125.0, txt='Esto es una prueba y no es v\xe1lido como factura', border=0)
   pdf.set_xy(160.0, 103.0)
   pdf.cell(ln=0, h=7.0, align='R', w=20.0, txt='100,00', border=0)
   pdf.set_line_width(0.0)
   pdf.line(15.0, 230.0, 185.0, 230.0)
   pdf.set_xy(20.0, 233.0)
   pdf.cell(ln=0, h=5.0, align='L', w=95.0, txt='CAE N\xba', border=0)
   pdf.set_xy(45.0, 233.0)
   pdf.cell(ln=0, h=5.0, align='L', w=30.0, txt='01234567890', border=0)
   pdf.set_font('arial', '', 12.0)
   pdf.set_xy(105.0, 234.0)
   pdf.cell(ln=0, h=9.0, align='R', w=45.0, txt='NETO GRAVADO:', border=0)
   pdf.set_font('arial', 'B', 12.0)
   pdf.set_xy(145.0, 234.0)
   pdf.cell(ln=0, h=9.0, align='R', w=33.0, txt='100,00', border=0)
   pdf.set_font('arial', '', 10.0)
   pdf.set_xy(20.0, 238.0)
   pdf.cell(ln=0, h=5.0, align='L', w=95.0, txt='Fecha Vto. CAE:', border=0)
   pdf.set_xy(55.0, 238.0)
   pdf.cell(ln=0, h=5.0, align='L', w=30.0, txt='19/02/2009', border=0)
   pdf.set_font('arial', '', 12.0)
   pdf.set_xy(125.0, 241.0)
   pdf.cell(ln=0, h=9.0, align='R', w=25.0, txt='IVA 21%:', border=0)
   pdf.set_font('arial', 'B', 12.0)
   pdf.set_xy(145.0, 241.0)
   pdf.cell(ln=0, h=9.0, align='R', w=33.0, txt='21,00', border=0)
   pdf.interleaved2of5('012345678905', 20.0, 243.5, w=0.75)
   pdf.set_font('arial', 'B', 12.0)
   pdf.set_xy(105.0, 251.0)
   pdf.cell(ln=0, h=9.0, align='R', w=73.0, txt='121,00', border=0)
   pdf.set_font('arial', '', 12.0)
   pdf.set_xy(125.0, 251.0)
   pdf.cell(ln=0, h=9.0, align='R', w=25.0, txt='Total:', border=0)
   pdf.set_line_width(0.0)
   pdf.rect(155.0, 252.0, 25.0, 7.0)
   pdf.set_font('arial', '', 10.0)
   pdf.set_xy(20.0, 253.0)
   pdf.cell(ln=0, h=7.0, align='L', w=120.0, txt='012345678905', border=0)
   pdf.output('/home/user/factura.pdf', 'F')

   os.system("/home/user/factura.pdf")

Autor / Autores:
::::::::::::::::

MarianoReingart_

Actualización
:::::::::::::

Mathesis

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _FPDF: http://www.fpdf.org

.. _sito del proyecto: http://www.nsis.com.ar/public/wiki/PyFpdf

