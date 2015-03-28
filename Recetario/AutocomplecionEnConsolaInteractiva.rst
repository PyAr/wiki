
Autocomplecion en consola interactiva
=====================================

(donado por Anthony Lenton)

crear un archivo llamado .pythonrc (se llama asi pero podria llamarse de cualquier otra forma), que dice:

::

   .. raw:: html
      <span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">   <span class="k">try</span><span class="p">:</span>
      </span><span class="line">       <span class="kn">import</span> <span class="nn">readline</span>
      </span><span class="line">   <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
      </span><span class="line">       <span class="k">print</span> <span class="s">&quot;Module readline not available.&quot;</span>
      </span><span class="line">   <span class="k">else</span><span class="p">:</span>
      </span><span class="line">       <span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">       <span class="kn">import</span> <span class="nn">rlcompleter</span>
      </span><span class="line">       <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&quot;darwin&quot;</span><span class="p">:</span>
      </span><span class="line">          <span class="n">readline</span><span class="o">.</span><span class="n">parse_and_bind</span> <span class="p">(</span><span class="s">&quot;bind ^I rl_complete&quot;</span><span class="p">)</span>
      </span><span class="line">       <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="n">readline</span><span class="o">.</span><span class="n">parse_and_bind</span><span class="p">(</span><span class="s">&quot;tab: complete&quot;</span><span class="p">)</span>
      </span><span class="line">       <span class="k">del</span> <span class="n">readline</span>
      </span><span class="line">       <span class="k">del</span> <span class="n">rlcompleter</span>
      </span><span class="line">       <span class="k">del</span> <span class="n">sys</span>
      </span>

y en el environment se setea la variable:

::

   .. raw:: html
      <span class="line"><span class="nv">PYTHONSTARTUP</span><span class="o">=</span>/home/tuusuario/.pythonrc <span class="c">#(aca importa que sea igual al nombre del alchivo).</span>
      </span>

Lo que hace es darte Tab-completion en el interprete, cuando no se recuerda que metodos tiene mistring, en el interprete se hace:

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mistring</span><span class="o">.&lt;</span><span class="n">tab</span><span class="o">&gt;&lt;</span><span class="n">tab</span><span class="o">&gt;</span>
      </span>

y lista los metodos y atributos disponibles.

Otros interpretes ya lo hacen.  ipython es notable por tener todo esto y mucho mas, pero hay gente que no se acostumbra a usarlo todavia, y esto le pone Tab-completion al interprete comuncito de siempre.

OS X
::::

Aparentemente apple no distribuye OSX con soporte para readline de fabrica. Yo estoy seguro que hace tiempo instalé readline 6.1 y py25-readline.

-------------------------



  CategoryRecetas_

