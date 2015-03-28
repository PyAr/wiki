#format rst

DbfPy
-----

Descripción
:::::::::::

Esta receta es un ejemplo de como acceder nativamente desde Python a bases de datos en formato DBF (dBase, Foxpro, Clipper, etc.), sin necesidad de ODBC u otras herramientas.

Utiliza DbfPy_. Para instalar la libreria, bajarla y descomprimirla con 7-Zip en el directorio de la aplicación o en site-packages (C:\python25\lib\site-packages o similar).

**Nota**: Para nuevos proyectos utilizar una base de datos relacional (ej. PostgreSQL o MySQL), o usar shelf para guardar objetos python facilmente.

Ejemplo:
::::::::

Ejemplo original traducido y ajustado:

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: iso-8859-1 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">dbfpy.dbf</span> <span class="kn">import</span> <span class="n">Dbf</span><span class="p">,</span> <span class="n">DbfRecord</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># abro el archivo country.dbf(viene como ejemplo dentro de la libreria)</span>
      </span><span class="line"><span class="n">dbf1</span> <span class="o">=</span> <span class="n">Dbf</span><span class="p">()</span>
      </span><span class="line"><span class="n">dbf1</span><span class="o">.</span><span class="n">openFile</span><span class="p">(</span><span class="s">&#39;dbfpy/county.dbf&#39;</span><span class="p">,</span> <span class="n">readOnly</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">dbf1</span><span class="o">.</span><span class="n">reportOn</span><span class="p">()</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&#39;registros de ejemplo:&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># recorro los registros:</span>
      </span><span class="line"><span class="k">for</span> <span class="n">registro</span> <span class="ow">in</span> <span class="n">dbf1</span><span class="p">:</span>
      </span><span class="line">    <span class="c"># recorro los campos:</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">nombre_campo</span> <span class="ow">in</span> <span class="n">dbf1</span><span class="o">.</span><span class="n">fieldNames</span><span class="p">():</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">:</span><span class="se">\t</span><span class="s"> </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">nombre_campo</span><span class="p">,</span> <span class="n">registro</span><span class="p">[</span><span class="n">nombre_campo</span><span class="p">])</span>
      </span><span class="line">    <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="c"># agregar un registro (campos COUNTYNO, COUNTYNAME, COUNTYABBR)</span>
      </span><span class="line"><span class="n">reg</span><span class="o">=</span><span class="n">DbfRecord</span><span class="p">(</span><span class="n">dbf1</span><span class="p">)</span>
      </span><span class="line"><span class="n">reg</span><span class="p">[</span><span class="s">&#39;COUNTYNO&#39;</span><span class="p">]</span><span class="o">=</span><span class="mi">116</span>
      </span><span class="line"><span class="n">reg</span><span class="p">[</span><span class="s">&#39;COUNTYNAME&#39;</span><span class="p">]</span><span class="o">=</span><span class="s">&quot;Prueba&quot;</span>
      </span><span class="line"><span class="n">reg</span><span class="p">[</span><span class="s">&#39;COUNTYABBR&#39;</span><span class="p">]</span><span class="o">=</span><span class="s">&quot;PRUE&quot;</span>
      </span><span class="line"><span class="c">#reg[&#39;FECHA&#39;]=(2000,1,12)</span>
      </span><span class="line"><span class="n">reg</span><span class="o">.</span><span class="n">store</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="c"># cierro el archivo</span>
      </span><span class="line"><span class="n">dbf1</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span>

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _DbfPy: http://dbfpy.sourceforge.net/

