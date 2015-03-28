#format rst

Escribe acerca de Recetario/Crypto/BlowfishConBlowfishpy aquí.

::

   ➜  ~  mkdir crypto_example
   ➜  ~  cd crypto_example
   ➜  crypto_example  wget http://www.seanet.com/\~bugbee/crypto/blowfish/blowfish.py3
   ➜  crypto_example  mv blowfish.py3 blowfish.py 

con este codigo

::

   .. raw:: html
      <span class="line"><span class="kn">import</span> <span class="nn">blowfish</span>
      </span><span class="line">
      </span><span class="line"><span class="n">b</span> <span class="o">=</span> <span class="n">blowfish</span><span class="o">.</span><span class="n">Blowfish</span><span class="p">(</span><span class="s">&quot;secreto aca&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">mensaje</span> <span class="o">=</span> <span class="s">&quot;hola!...&quot;</span>
      </span><span class="line"><span class="n">cifrado</span> <span class="o">=</span> <span class="n">b</span><span class="o">.</span><span class="n">encipher_block</span><span class="p">(</span><span class="n">mensaje</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mensaje </span><span class="si">%s</span><span class="s"> cifrado es </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">mensaje</span><span class="p">,</span> <span class="n">cifrado</span><span class="p">)</span>
      </span>

salida:

::

   mensaje hola!... cifrado es 0@�WE

nota: el mensaje a cifrar parece que tiene que tener un largo de 8 (no se mucho de blowfish :D)

