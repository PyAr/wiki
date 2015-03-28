#format rst

Como Levantar Un Servidor Http Multithread
==========================================

este ejemplo muestra como levantar un servidor web en python sirviendo el contenido del directorio actual utilizando threads para manejar las solicitudes.

para usar simplemente hay que llamar a este modulo desde la linea de comando, si se llamara test.py entonces correr "python test.py"

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">SocketServer</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">BaseHTTPServer</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">SimpleHTTPServer</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">Server</span><span class="p">(</span><span class="n">SocketServer</span><span class="o">.</span><span class="n">ThreadingMixIn</span><span class="p">,</span> <span class="n">BaseHTTPServer</span><span class="o">.</span><span class="n">HTTPServer</span><span class="p">):</span>
      </span><span class="line">    <span class="k">pass</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">SimpleHTTPServer</span><span class="o">.</span><span class="n">test</span><span class="p">(</span><span class="n">ServerClass</span><span class="o">=</span><span class="n">Server</span><span class="p">)</span>
      </span>

