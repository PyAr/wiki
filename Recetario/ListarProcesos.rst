
Listar Procesos
===============

Esta receta muestra una forma de listar procesos en python que soporta múltiples sistemas operativos

En el ejemplo se muestra como listar información sobre los procesos corriendo bajo el usuario "root"

Hace falta instalar la libreria psutil_, disponible en aqui_. Hay paquetes para Debian_ y Ubuntu_, python-psutil.

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">psutil</span>
      </span><span class="line">
      </span><span class="line"><span class="k">for</span> <span class="n">pid</span> <span class="ow">in</span> <span class="n">psutil</span><span class="o">.</span><span class="n">get_pid_list</span><span class="p">():</span>
      </span><span class="line">    <span class="n">proc</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">Process</span><span class="p">(</span><span class="n">pid</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">if</span> <span class="n">proc</span><span class="o">.</span><span class="n">username</span> <span class="o">!=</span> <span class="s">&quot;root&quot;</span><span class="p">:</span>
      </span><span class="line">        <span class="k">continue</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">print</span> <span class="n">proc</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">cmdline</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">pid</span>
      </span>

En la versión 0.3 de psutil el Ejemplo puede quedar como:

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">psutil</span>
      </span><span class="line">
      </span><span class="line"><span class="k">for</span> <span class="n">proc</span> <span class="ow">in</span> <span class="n">psutil</span><span class="o">.</span><span class="n">get_process_list</span><span class="p">():</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">proc</span><span class="o">.</span><span class="n">username</span> <span class="o">!=</span> <span class="s">&quot;root&quot;</span><span class="p">:</span>
      </span><span class="line">        <span class="k">continue</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">proc</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">cmdline</span><span class="p">,</span> <span class="n">proc</span><span class="o">.</span><span class="n">pid</span>
      </span>

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _psutil:
.. _aqui: http://code.google.com/p/psutil/

.. _Debian: http://packages.debian.org/python-psutil

.. _Ubuntu: http://packages.ubuntu.com/python-psutil

