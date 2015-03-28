#format rst

Test Formulario Con File Upload en Django
=========================================

un ejemplo de como probar un formulario que tiene un campo para subir un archivo 

::

   .. raw:: html
      <span class="line"><span class="kn">from</span> <span class="nn">django.test.client</span> <span class="kn">import</span> <span class="n">Client</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">django.core.files.uploadedfile</span> <span class="kn">import</span> <span class="n">SimpleUploadedFile</span>
      </span><span class="line">
      </span><span class="line"><span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">()</span>
      </span><span class="line"><span class="n">client</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="o">=</span><span class="n">password</span><span class="p">)</span>
      </span><span class="line"><span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;campo1&#39;</span><span class="p">:</span> <span class="s">&#39;valor1&#39;</span><span class="p">,</span>
      </span><span class="line">        <span class="s">&#39;campo2&#39;</span><span class="p">:</span> <span class="s">&#39;valor2&#39;</span><span class="p">,</span>
      </span><span class="line">        <span class="s">&#39;archivo&#39;</span><span class="p">:</span> <span class="n">SimpleUploadedFile</span><span class="p">(</span><span class="s">&#39;nombre_de_archivo&#39;</span><span class="p">,</span><span class="s">&#39;contenido de archivo&#39;</span><span class="p">),</span>
      </span><span class="line"><span class="p">}</span>
      </span><span class="line">
      </span><span class="line"><span class="n">response</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="s">&#39;/path/al/form&#39;</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
      </span><span class="line"><span class="k">assert</span> <span class="n">response</span><span class="o">.</span><span class="n">status_code</span> <span class="o">==</span> <span class="mi">200</span>
      </span>

