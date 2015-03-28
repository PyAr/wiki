
Extraer un archivo de texto embebido en un recurso .qrc
-------------------------------------------------------

Ademas de poder embeber imágenes, la librería Qt (y por ende PyQt) también permite incluir otros elementos en su sistema de recursos. La función que se define a continuación permite leer los contenidos de un archivo de texto plano que se encuentre registrado en un archivo .qrc. Cabe agregar que antes de invocar a ``loadTextFileFromRc()`` hay que convertir el .qrc a módulo de Python con la herramienta pyrcc4 (por ejemplo, en una terminal de GNU/Linux: ``$ pyrcc4 -o resources.py resources.qrc``). Esto puede ser útil para incorporar al programa una hoja de estilo que se aplique a toda la aplicación.

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">PyQt4</span> <span class="kn">import</span> <span class="n">QtCore</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># El siguiente import realizará el registro de los recursos a PyQt.</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">resources</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">loadTextFileFromRc</span><span class="p">(</span><span class="n">rcPath</span><span class="p">):</span>
      </span><span class="line">    <span class="s">u&quot;&quot;&quot;Extrae el contenido de un archivo de texto incluido en el sistema</span>
      </span><span class="line"><span class="s">    de recursos.</span>
      </span><span class="line"><span class="s">        </span>
      </span><span class="line"><span class="s">    Parámetros:</span>
      </span><span class="line"><span class="s">        rcPath: ruta absoluta del archivo dentro del recurso. Por ejemplo:</span>
      </span><span class="line"><span class="s">            &#39;:/app/css/style.css&#39;.</span>
      </span><span class="line"><span class="s">    &quot;&quot;&quot;</span>
      </span><span class="line">   
      </span><span class="line">    <span class="n">q_file</span> <span class="o">=</span> <span class="n">QtCore</span><span class="o">.</span><span class="n">QFile</span><span class="p">(</span><span class="n">rcPath</span><span class="p">)</span>
      </span><span class="line">    <span class="n">q_file</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">QtCore</span><span class="o">.</span><span class="n">QIODevice</span><span class="o">.</span><span class="n">ReadOnly</span><span class="p">)</span>
      </span><span class="line">    <span class="n">q_text_stream</span> <span class="o">=</span> <span class="n">QtCore</span><span class="o">.</span><span class="n">QTextStream</span><span class="p">(</span><span class="n">q_file</span><span class="p">)</span>
      </span><span class="line">    <span class="n">content</span> <span class="o">=</span>  <span class="n">q_text_stream</span><span class="o">.</span><span class="n">readAll</span><span class="p">()</span>
      </span><span class="line">    <span class="n">q_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">   
      </span><span class="line">    <span class="k">return</span> <span class="n">content</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">loadTextFileFromRc</span><span class="p">(</span><span class="s">&#39;:/ruta/al/recurso.txt&#39;</span><span class="p">)</span>
      </span>

-------------------------



  CategoryRecetas_

