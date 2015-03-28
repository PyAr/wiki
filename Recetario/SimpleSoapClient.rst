#format rst

SimpleSoapClient
----------------

Descripción
:::::::::::

En este ejemplo se muestra utilizar servicios webs de manera simple (código usado en `Factura Electronica`_)

Utiliza SimpleXmlElement_ y SimpleSoapClient_, manejando de manera simple el protocolo SOAP y XML.

**Nota**: Ver otras librerias más avanzadas.

Ejemplo: Feriados (Ministerio del Interior)
:::::::::::::::::::::::::::::::::::::::::::

Ver: http://www.mininterior.gov.ar/servicios/wsferiados.asp

::

   .. raw:: html
      <span class="line">    <span class="c"># Demo &amp; Test: Feriados (Ministerio del Interior):</span>
      </span><span class="line">    <span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timedelta</span>
      </span><span class="line">    <span class="n">client</span> <span class="o">=</span> <span class="n">SoapClient</span><span class="p">(</span>
      </span><span class="line">        <span class="n">location</span> <span class="o">=</span> <span class="s">&quot;http://webservices.mininterior.gov.ar/Feriados/Service.svc&quot;</span><span class="p">,</span>
      </span><span class="line">        <span class="n">action</span> <span class="o">=</span> <span class="s">&#39;http://tempuri.org/IMyService/&#39;</span><span class="p">,</span> <span class="c"># SOAPAction</span>
      </span><span class="line">        <span class="n">namespace</span> <span class="o">=</span> <span class="s">&quot;http://tempuri.org/FeriadoDS.xsd&quot;</span><span class="p">,</span>
      </span><span class="line">        <span class="n">trace</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">dt1</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">today</span><span class="p">()</span> <span class="o">-</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>
      </span><span class="line">    <span class="n">dt2</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">today</span><span class="p">()</span> <span class="o">+</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>
      </span><span class="line">    <span class="n">feriadosXML</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">FeriadosEntreFechasAsXml</span><span class="p">(</span><span class="n">dt1</span><span class="o">=</span><span class="n">dt1</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(),</span> <span class="n">dt2</span><span class="o">=</span><span class="n">dt2</span><span class="o">.</span><span class="n">isoformat</span><span class="p">());</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">feriadosXML</span>
      </span>

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Factura Electronica: http://www.nsis.com.ar/public/browser/pyafip/ws/php.py

