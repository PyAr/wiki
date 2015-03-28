#format rst

Multiprocessing y Threading
---------------------------

en esta receta se muestra como hacer para correr algo en otro thread o proceso con pocos cambios y como lograr comunicacion entre ellos.

notar que el pid de quien lanza doer es distinto al que imprime doer

ejemplo con multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Process</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Queue</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Doer</span><span class="p">(</span><span class="n">Process</span><span class="p">):</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">queue</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="n">Process</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">queue</span> <span class="o">=</span> <span class="n">queue</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">state</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_do_on_start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;doint stuff on start&quot;</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;pid:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">        <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_on_end</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;doint stuff on end&quot;</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;pid:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">        <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_do_on_start</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">msg</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line">        <span class="k">while</span> <span class="n">msg</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">msg</span> <span class="o">!=</span> <span class="s">&quot;exit&quot;</span><span class="p">:</span>
      </span><span class="line">            <span class="c"># blocks here</span>
      </span><span class="line">            <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
      </span><span class="line">            <span class="k">print</span> <span class="s">&quot;handling message&quot;</span><span class="p">,</span> <span class="n">msg</span>
      </span><span class="line">
      </span><span class="line">            <span class="c"># do stuff here according to the message</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">msg</span> <span class="o">==</span> <span class="s">&quot;ping&quot;</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;pong&quot;</span>
      </span><span class="line">            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
      </span><span class="line">                <span class="n">action</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">msg</span>
      </span><span class="line">                <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="s">&quot;set-state&quot;</span><span class="p">:</span>
      </span><span class="line">                    <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">value</span>
      </span><span class="line">                    <span class="k">print</span> <span class="s">&quot;new state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">msg</span> <span class="o">!=</span> <span class="s">&quot;exit&quot;</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;unknown message&quot;</span><span class="p">,</span> <span class="n">msg</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_on_end</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">demo</span><span class="p">():</span>
      </span><span class="line">    <span class="n">queue</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;creating doer from process&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">    <span class="n">doer</span> <span class="o">=</span> <span class="n">Doer</span><span class="p">(</span><span class="n">queue</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>
      </span><span class="line">    <span class="n">doer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;ping&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;foo&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">((</span><span class="s">&quot;set-state&quot;</span><span class="p">,</span> <span class="s">&quot;hola!&quot;</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;exit&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">doer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">demo</span><span class="p">()</span>
      </span>

corriendolo tenemos el resultado

::

   $ python controlled.py
   creating doer from process 11784
   doint stuff on start
   state: 42
   pid: 11785

   handling message ping
   pong

   handling message foo
   unknown message foo

   handling message ('set-state', 'hola!')
   new state: hola!

   handling message exit

   doint stuff on end
   state: hola!
   pid: 11785

ejemplo con threading
~~~~~~~~~~~~~~~~~~~~~

para hacerlo andar con threading hay que solo cambiar de donde importamos las cosas, aquí esta la diferencia:

notar que el pid de quien lanza doer es igual al que imprime doer

::

   .. raw:: html
      <span class="line"><span class="gh">diff controlled.py controlledthread.py </span>
      </span><span class="line">4,5c4,5
      </span><span class="line">&lt; from multiprocessing import Process
      </span><span class="line">&lt; from multiprocessing import Queue
      </span><span class="line"><span class="gd">---</span>
      </span><span class="line">&gt; from threading import Thread as Process
      </span><span class="line">&gt; from Queue import Queue
      </span>

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">os</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">threading</span> <span class="kn">import</span> <span class="n">Thread</span> <span class="k">as</span> <span class="n">Process</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">Queue</span> <span class="kn">import</span> <span class="n">Queue</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Doer</span><span class="p">(</span><span class="n">Process</span><span class="p">):</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">queue</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="n">Process</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">queue</span> <span class="o">=</span> <span class="n">queue</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">state</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_do_on_start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;doint stuff on start&quot;</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;pid:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">        <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_on_end</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;doint stuff on end&quot;</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">        <span class="k">print</span> <span class="s">&quot;pid:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">        <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_do_on_start</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">msg</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line">        <span class="k">while</span> <span class="n">msg</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">msg</span> <span class="o">!=</span> <span class="s">&quot;exit&quot;</span><span class="p">:</span>
      </span><span class="line">            <span class="c"># blocks here</span>
      </span><span class="line">            <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
      </span><span class="line">            <span class="k">print</span> <span class="s">&quot;handling message&quot;</span><span class="p">,</span> <span class="n">msg</span>
      </span><span class="line">
      </span><span class="line">            <span class="c"># do stuff here according to the message</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">msg</span> <span class="o">==</span> <span class="s">&quot;ping&quot;</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;pong&quot;</span>
      </span><span class="line">            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
      </span><span class="line">                <span class="n">action</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">msg</span>
      </span><span class="line">                <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="s">&quot;set-state&quot;</span><span class="p">:</span>
      </span><span class="line">                    <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">value</span>
      </span><span class="line">                    <span class="k">print</span> <span class="s">&quot;new state:&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
      </span><span class="line">            <span class="k">elif</span> <span class="n">msg</span> <span class="o">!=</span> <span class="s">&quot;exit&quot;</span><span class="p">:</span>
      </span><span class="line">                <span class="k">print</span> <span class="s">&quot;unknown message&quot;</span><span class="p">,</span> <span class="n">msg</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">print</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_on_end</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">demo</span><span class="p">():</span>
      </span><span class="line">    <span class="n">queue</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;creating doer from process&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">()</span>
      </span><span class="line">    <span class="n">doer</span> <span class="o">=</span> <span class="n">Doer</span><span class="p">(</span><span class="n">queue</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>
      </span><span class="line">    <span class="n">doer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;ping&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;foo&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">((</span><span class="s">&quot;set-state&quot;</span><span class="p">,</span> <span class="s">&quot;hola!&quot;</span><span class="p">))</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="s">&quot;exit&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">doer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">demo</span><span class="p">()</span>
      </span>

::

   $ python controlledthread.py
   creating doer from process 11812
   doint stuff on start
   state: 42
   pid: 11812

   handling message ping
   pong

   handling message foo
   unknown message foo

   handling message ('set-state', 'hola!')
   new state: hola!

   handling message exit

   doint stuff on end
   state: hola!
   pid: 11812

