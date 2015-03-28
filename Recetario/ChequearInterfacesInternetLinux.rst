
Si te esta pasa que necesitas saber porque placa de red tenes internet en Gnu/Linux con Python ? bueno, por ahi esto te sirve |:)|

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">socket</span>
      </span><span class="line">
      </span><span class="line"><span class="n">DEBUG</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">list_net_devices</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Lista todas las placas de red.</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            Lista con diccionarios, cada diccionario de la lista tiene</span>
      </span><span class="line"><span class="sd">            como key el nombre de la iface asignada y los valores del </span>
      </span><span class="line"><span class="sd">            diccionario son los datos correspondiente a la interfaz de red</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="n">fh</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&#39;/proc/net/dev&#39;</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">lines</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span>
      </span><span class="line">    <span class="n">fh</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">ifaces</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
      </span><span class="line">        <span class="k">if</span> <span class="s">&#39;:&#39;</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span>
      </span><span class="line">            <span class="n">iface_name</span><span class="p">,</span> <span class="n">iface_data</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span>
      </span><span class="line">            <span class="n">new_iface</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">            <span class="c"># limpiamos iface_data ...</span>
      </span><span class="line">            <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">iface_data</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">):</span>
      </span><span class="line">                <span class="k">if</span> <span class="n">item</span> <span class="o">!=</span> <span class="s">&#39;&#39;</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
      </span><span class="line">            <span class="n">new_iface</span><span class="p">[</span><span class="n">iface_name</span><span class="o">.</span><span class="n">strip</span><span class="p">()]</span> <span class="o">=</span> <span class="n">data</span>
      </span><span class="line">            <span class="n">ifaces</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">new_iface</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="n">ifaces</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">info_net_device</span><span class="p">(</span><span class="n">device</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Devuelve informacion de un dispositivo de red en particular</span>
      </span><span class="line"><span class="sd">        Argumentos:</span>
      </span><span class="line"><span class="sd">            device(str)</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            Diccionario siendo la clave el device solicitado y</span>
      </span><span class="line"><span class="sd">            los datos como values.</span>
      </span><span class="line"><span class="sd">            None en caso de no encontrarse el dispositivo de red.</span>
      </span><span class="line"><span class="sd">        Funciones:</span>
      </span><span class="line"><span class="sd">            list_net_devices</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;el device debe ser un string, obtuve </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">repr</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">devices</span> <span class="o">=</span> <span class="n">list_net_devices</span><span class="p">()</span>
      </span><span class="line">    <span class="n">info_iface</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">iface</span> <span class="ow">in</span> <span class="n">devices</span><span class="p">:</span>
      </span><span class="line">        <span class="n">kw</span> <span class="o">=</span> <span class="n">iface</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">kw</span> <span class="o">==</span> <span class="n">device</span><span class="p">:</span>
      </span><span class="line">            <span class="n">info_iface</span><span class="p">[</span><span class="n">kw</span><span class="p">]</span> <span class="o">=</span> <span class="n">iface</span><span class="p">[</span><span class="n">kw</span><span class="p">]</span>
      </span><span class="line">            <span class="k">return</span> <span class="n">info_iface</span>
      </span><span class="line">    <span class="k">return</span> <span class="bp">None</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">route_net_devices</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Devuelve las rutas asignadas a los dispositivos de red</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            Diccionario siendo la clave el dispositivo de red y su</span>
      </span><span class="line"><span class="sd">            value la ip de la ruta por defecto como string.</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="n">fh</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&#39;/proc/net/route&#39;</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">lines</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span>
      </span><span class="line">    <span class="n">fh</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">    <span class="n">devices</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;Iface&#39;</span><span class="p">:</span>
      </span><span class="line">            <span class="n">iface</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line">            <span class="n">hexgw</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)[</span><span class="mi">2</span><span class="p">]</span>
      </span><span class="line">            <span class="n">gw</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">hexgw</span><span class="p">[</span><span class="mi">6</span><span class="p">:</span><span class="mi">8</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span>
      </span><span class="line">                                  <span class="nb">int</span><span class="p">(</span><span class="n">hexgw</span><span class="p">[</span><span class="mi">4</span><span class="p">:</span><span class="mi">6</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span>
      </span><span class="line">                                  <span class="nb">int</span><span class="p">(</span><span class="n">hexgw</span><span class="p">[</span><span class="mi">2</span><span class="p">:</span><span class="mi">4</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span>
      </span><span class="line">                                  <span class="nb">int</span><span class="p">(</span><span class="n">hexgw</span><span class="p">[:</span><span class="mi">2</span><span class="p">],</span> <span class="mi">16</span><span class="p">),</span>
      </span><span class="line">                                  <span class="p">)</span>
      </span><span class="line">            <span class="n">devices</span><span class="p">[</span><span class="n">iface</span><span class="p">]</span> <span class="o">=</span> <span class="n">gw</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">devices</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">ip_port_open</span><span class="p">(</span><span class="n">ip</span><span class="p">,</span><span class="n">port</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Chequea si un puerto en una ip dada se encuentra abierto o no.</span>
      </span><span class="line"><span class="sd">        Argumentos:</span>
      </span><span class="line"><span class="sd">            ip(str)</span>
      </span><span class="line"><span class="sd">            port(int)</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            True(bool), si el puerto en la ip dada esta abierto</span>
      </span><span class="line"><span class="sd">            False(bool), si el puerto en la ip dada no esta abierto</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ip</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;la ip debe ser un string, obtuve </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">repr</span><span class="p">(</span><span class="n">ip</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;el puerto debe ser un int, obtuve </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">repr</span><span class="p">(</span><span class="n">port</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">s</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">)</span>
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">s</span><span class="o">.</span><span class="n">connect</span><span class="p">((</span><span class="n">ip</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">port</span><span class="p">)))</span>
      </span><span class="line">        <span class="n">s</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">    <span class="k">except</span><span class="p">:</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">host_port_open</span><span class="p">(</span><span class="n">hostname</span><span class="p">,</span> <span class="n">port</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Chequea si un puerto en un host dado se encuentra abierto o no.</span>
      </span><span class="line"><span class="sd">        Argumentos:</span>
      </span><span class="line"><span class="sd">            hostname(str)</span>
      </span><span class="line"><span class="sd">            port(int)</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            True(bool), si el puerto en el hostname dado esta abierto</span>
      </span><span class="line"><span class="sd">            False(bool), si el puerto en el hostname dado no esta abierto</span>
      </span><span class="line"><span class="sd">        Funciones:</span>
      </span><span class="line"><span class="sd">            ip_port_open</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">hostname</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;el hostname debe ser un string, obtuve </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">repr</span><span class="p">(</span><span class="n">hostname</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;el puerto debe ser un int, obtuve </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">repr</span><span class="p">(</span><span class="n">port</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">ip</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="n">hostname</span><span class="p">)</span>
      </span><span class="line">    <span class="k">return</span> <span class="n">ip_port_open</span><span class="p">(</span><span class="n">ip</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">dns_working</span><span class="p">(</span><span class="n">domain</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Chequea si podemos resolver un dominio, por lo tanto, si funcionan los DNS</span>
      </span><span class="line"><span class="sd">    Argumentos:</span>
      </span><span class="line"><span class="sd">        domain(str)</span>
      </span><span class="line"><span class="sd">    Retorna:</span>
      </span><span class="line"><span class="sd">        True(bool) en caso de poder resolver el dominio</span>
      </span><span class="line"><span class="sd">        False(bool) en caso de no poder resolver el dominio</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">domain</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;el domain debe ser un string&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">True</span>
      </span><span class="line">    <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
      </span><span class="line">        <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">gateway_recheable</span><span class="p">(</span><span class="n">dest_addr</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">inet</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="sd">    Chequea si tenemos conexion contra el gateway pasado como parametro.</span>
      </span><span class="line"><span class="sd">    Si el gateway bloquea los paquetes icmp, este metodo no funciona.</span>
      </span><span class="line"><span class="sd">        Argumentos:</span>
      </span><span class="line"><span class="sd">            gateway(str)</span>
      </span><span class="line"><span class="sd">        Retorna:</span>
      </span><span class="line"><span class="sd">            True(bool) si el gateway es recheable</span>
      </span><span class="line"><span class="sd">            False(bool) si el gateways no es recheable</span>
      </span><span class="line"><span class="sd">    &#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dest_addr</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
      </span><span class="line">        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;gateway debe ser una ip como string&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">create_sockets</span><span class="p">(</span><span class="n">ttl</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">        Sockets necesarios para el traceroute, enviamos por udp y</span>
      </span><span class="line"><span class="sd">        recibimos por icmp. Al usar icmp, precisamos permisos de super</span>
      </span><span class="line"><span class="sd">        administrador.</span>
      </span><span class="line"><span class="sd">            Argumentos:</span>
      </span><span class="line"><span class="sd">                ttl(int) TimeToLive, campo que se setea en el paquete</span>
      </span><span class="line"><span class="sd">                y cual se decrementa en 1 a medida que pasa por cada</span>
      </span><span class="line"><span class="sd">                host / router</span>
      </span><span class="line"><span class="sd">            Retorna:</span>
      </span><span class="line"><span class="sd">                recv_socket, socket icmp en el que se escuchan datos</span>
      </span><span class="line"><span class="sd">                send_socket, socket udp por el cual se envian datos</span>
      </span><span class="line"><span class="sd">            Funciones:</span>
      </span><span class="line"><span class="sd">                dns_working</span>
      </span><span class="line"><span class="sd">        &quot;&quot;&quot;</span>
      </span><span class="line">        <span class="n">icmp</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">getprotobyname</span><span class="p">(</span><span class="s">&#39;icmp&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">udp</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">getprotobyname</span><span class="p">(</span><span class="s">&#39;udp&#39;</span><span class="p">)</span>
      </span><span class="line">        <span class="n">timeout</span> <span class="o">=</span> <span class="mi">2</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">recv_socket</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_RAW</span><span class="p">,</span> <span class="n">icmp</span><span class="p">)</span>
      </span><span class="line">        <span class="n">recv_socket</span><span class="o">.</span><span class="n">settimeout</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
      </span><span class="line">        <span class="n">send_socket</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_DGRAM</span><span class="p">,</span> <span class="n">udp</span><span class="p">)</span>
      </span><span class="line">        <span class="n">send_socket</span><span class="o">.</span><span class="n">setsockopt</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">SOL_IP</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">IP_TTL</span><span class="p">,</span> <span class="n">ttl</span><span class="p">)</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">recv_socket</span><span class="p">,</span> <span class="n">send_socket</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">ttl</span> <span class="o">=</span> <span class="mi">1</span>
      </span><span class="line">    <span class="n">port</span> <span class="o">=</span> <span class="mi">33434</span>
      </span><span class="line">    <span class="n">recheable</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">    <span class="n">remote_host</span> <span class="o">=</span> <span class="s">&#39;google.com&#39;</span>    <span class="c"># host usado para comprobar internet</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">try</span><span class="p">:</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">dest_addr</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">            <span class="n">recv_socket</span><span class="p">,</span> <span class="n">send_socket</span> <span class="o">=</span> <span class="n">create_sockets</span><span class="p">(</span><span class="n">ttl</span><span class="p">)</span>
      </span><span class="line">            <span class="n">recv_socket</span><span class="o">.</span><span class="n">bind</span><span class="p">((</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">port</span><span class="p">))</span>
      </span><span class="line">            <span class="n">send_socket</span><span class="o">.</span><span class="n">sendto</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="p">(</span><span class="n">dest_addr</span><span class="p">,</span> <span class="n">port</span><span class="p">))</span>
      </span><span class="line">            <span class="n">_</span><span class="p">,</span> <span class="n">curr_addr</span> <span class="o">=</span> <span class="n">recv_socket</span><span class="o">.</span><span class="n">recvfrom</span><span class="p">(</span><span class="mi">512</span><span class="p">)</span>
      </span><span class="line">            <span class="n">curr_addr</span> <span class="o">=</span> <span class="n">curr_addr</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line">            <span class="n">send_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">            <span class="n">recv_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">curr_addr</span> <span class="o">==</span> <span class="n">dest_addr</span><span class="p">:</span>
      </span><span class="line">                <span class="n">recheable</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">inet</span> <span class="ow">is</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">            <span class="n">max_hops</span> <span class="o">=</span> <span class="mi">30</span>
      </span><span class="line">            <span class="n">max_hops_failures</span> <span class="o">=</span> <span class="mi">20</span>
      </span><span class="line">            <span class="n">failures</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">            <span class="n">accerted_hops</span> <span class="o">=</span> <span class="mi">0</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">if</span> <span class="ow">not</span> <span class="n">dns_working</span><span class="p">(</span><span class="n">remote_host</span><span class="p">):</span>
      </span><span class="line">                <span class="k">return</span> <span class="bp">False</span>
      </span><span class="line">            <span class="n">dest_addr</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">gethostbyname</span><span class="p">(</span><span class="n">remote_host</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">            <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line">                <span class="n">recv_socket</span><span class="p">,</span> <span class="n">send_socket</span> <span class="o">=</span> <span class="n">create_sockets</span><span class="p">(</span><span class="n">ttl</span><span class="p">)</span>
      </span><span class="line">                <span class="n">recv_socket</span><span class="o">.</span><span class="n">bind</span><span class="p">((</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">port</span><span class="p">))</span>
      </span><span class="line">                <span class="n">send_socket</span><span class="o">.</span><span class="n">sendto</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="p">(</span><span class="n">remote_host</span><span class="p">,</span> <span class="n">port</span><span class="p">))</span>
      </span><span class="line">                <span class="k">try</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">_</span><span class="p">,</span> <span class="n">curr_addr</span> <span class="o">=</span> <span class="n">recv_socket</span><span class="o">.</span><span class="n">recvfrom</span><span class="p">(</span><span class="mi">512</span><span class="p">)</span>
      </span><span class="line">                    <span class="n">curr_addr</span> <span class="o">=</span> <span class="n">curr_addr</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
      </span><span class="line">                    <span class="k">if</span> <span class="n">curr_addr</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">                        <span class="n">accerted_hops</span> <span class="o">+=</span> <span class="mi">1</span>
      </span><span class="line">                        <span class="k">if</span> <span class="n">curr_addr</span> <span class="o">==</span> <span class="n">dest_addr</span><span class="p">:</span>
      </span><span class="line">                            <span class="n">recheable</span> <span class="o">=</span> <span class="bp">True</span>
      </span><span class="line">                            <span class="n">send_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">                            <span class="n">recv_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">                            <span class="k">break</span>
      </span><span class="line">                    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                        <span class="n">failures</span> <span class="o">+=</span> <span class="mi">1</span>
      </span><span class="line">
      </span><span class="line">                <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">ex</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">failures</span> <span class="o">+=</span> <span class="mi">1</span>
      </span><span class="line">
      </span><span class="line">                <span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span>
      </span><span class="line">                    <span class="k">print</span> <span class="s">&#39;ttl: </span><span class="si">%s</span><span class="s"> chost: </span><span class="si">%s</span><span class="s"> rhost: </span><span class="si">%s</span><span class="s"> failures: </span><span class="si">%s</span><span class="s"> accerts: </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ttl</span><span class="p">,</span>
      </span><span class="line">                                                                                    <span class="n">curr_addr</span><span class="p">,</span>
      </span><span class="line">                                                                                    <span class="n">dest_addr</span><span class="p">,</span>
      </span><span class="line">                                                                                    <span class="n">failures</span><span class="p">,</span>
      </span><span class="line">                                                                                    <span class="n">accerted_hops</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">                <span class="n">ttl</span> <span class="o">+=</span> <span class="mi">1</span>
      </span><span class="line">                <span class="n">send_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">                <span class="n">recv_socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">                <span class="k">if</span> <span class="n">failures</span> <span class="o">&gt;=</span> <span class="n">max_hops_failures</span><span class="p">:</span>
      </span><span class="line">                    <span class="n">recheable</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">                    <span class="k">break</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">ex</span><span class="p">:</span>
      </span><span class="line">        <span class="n">recheable</span> <span class="o">=</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">return</span> <span class="n">recheable</span>
      </span>

Ejemplitos de como se usa:

::

   .. raw:: html
      <span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">8</span><span class="p">]:</span> <span class="c"># chequeamos conexion contra la db</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">9</span><span class="p">]:</span> <span class="n">host_port_open</span><span class="p">(</span><span class="s">&#39;gondor.airtrack.ovz&#39;</span><span class="p">,</span> <span class="mi">3306</span><span class="p">)</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">9</span><span class="p">]:</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">10</span><span class="p">]:</span> <span class="c"># http de googl ...</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">11</span><span class="p">]:</span> <span class="n">host_port_open</span><span class="p">(</span><span class="s">&#39;www.google.com&#39;</span><span class="p">,</span> <span class="mi">80</span><span class="p">)</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">11</span><span class="p">]:</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">12</span><span class="p">]:</span> <span class="n">host_port_open</span><span class="p">(</span><span class="s">&#39;www.google.com&#39;</span><span class="p">,</span> <span class="mi">81</span><span class="p">)</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">12</span><span class="p">]:</span> <span class="bp">False</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">15</span><span class="p">]:</span> <span class="c"># pedimos el gateway de la eth1 ...</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">16</span><span class="p">]:</span> <span class="n">route_net_devices</span><span class="p">()</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">16</span><span class="p">]:</span> <span class="p">{</span><span class="s">&#39;eth1&#39;</span><span class="p">:</span> <span class="s">&#39;192.168.1.1&#39;</span><span class="p">,</span> <span class="s">&#39;eth2&#39;</span><span class="p">:</span> <span class="s">&#39;0.0.0.0&#39;</span><span class="p">,</span> <span class="s">&#39;lo&#39;</span><span class="p">:</span> <span class="s">&#39;0.0.0.0&#39;</span><span class="p">}</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">17</span><span class="p">]:</span> <span class="c"># aha ... ahora veamos si tenemos conexion contra ese gw ...</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">18</span><span class="p">]:</span> <span class="n">gateway_recheable</span><span class="p">(</span><span class="n">route_net_devices</span><span class="p">()[</span><span class="s">&#39;eth1&#39;</span><span class="p">])</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">18</span><span class="p">]:</span> <span class="bp">True</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">19</span><span class="p">]:</span> <span class="c"># y nos da internet ese gw ? ...</span>
      </span><span class="line">
      </span><span class="line"><span class="n">In</span> <span class="p">[</span><span class="mi">20</span><span class="p">]:</span> <span class="n">gateway_recheable</span><span class="p">(</span><span class="n">route_net_devices</span><span class="p">()[</span><span class="s">&#39;eth1&#39;</span><span class="p">],</span> <span class="n">inet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">1</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">1.1</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">0</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">1</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">2</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">1.1</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">1</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">1</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">3</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">1.1</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">2</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">1</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">4</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">1.1</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">3</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">1</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">5</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">1.1</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">4</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">1</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">6</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">200.89</span><span class="o">.</span><span class="mf">165.213</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">4</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">2</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">7</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">200.89</span><span class="o">.</span><span class="mf">165.194</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">4</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">3</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">8</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">200.89</span><span class="o">.</span><span class="mf">165.194</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">5</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">3</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">9</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">200.89</span><span class="o">.</span><span class="mf">165.194</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">6</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">3</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">10</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">200.49</span><span class="o">.</span><span class="mf">159.254</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">6</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">4</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">11</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">251.28</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">6</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">5</span>
      </span><span class="line"><span class="n">ttl</span><span class="p">:</span> <span class="mi">12</span> <span class="n">chost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">251.6</span> <span class="n">rhost</span><span class="p">:</span> <span class="mf">209.85</span><span class="o">.</span><span class="mf">195.104</span> <span class="n">failures</span><span class="p">:</span> <span class="mi">6</span> <span class="n">accerts</span><span class="p">:</span> <span class="mi">6</span>
      </span><span class="line"><span class="n">Out</span><span class="p">[</span><span class="mi">20</span><span class="p">]:</span> <span class="bp">True</span>
      </span>

-------------------------



  CategoryRecetas_

