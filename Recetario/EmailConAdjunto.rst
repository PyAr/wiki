#format rst

Email con Adjunto
-----------------

Descripción
:::::::::::

Esta receta es un ejemplo sencillo de como enviar un email, con una parte de texto y otra binaria (adjunto)

Ejemplo:
::::::::

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: iso-8859-1 -*-</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.text</span> <span class="kn">import</span> <span class="n">MIMEText</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.application</span> <span class="kn">import</span> <span class="n">MIMEApplication</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.multipart</span> <span class="kn">import</span> <span class="n">MIMEMultipart</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">smtplib</span> <span class="kn">import</span> <span class="n">SMTP</span>
      </span><span class="line">
      </span><span class="line"><span class="n">msg</span> <span class="o">=</span> <span class="n">MIMEMultipart</span><span class="p">()</span>
      </span><span class="line"><span class="n">msg</span><span class="p">[</span><span class="s">&#39;Subject&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;Esto es una prueba&#39;</span>
      </span><span class="line"><span class="n">msg</span><span class="p">[</span><span class="s">&#39;From&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;yo@example.com&#39;</span>
      </span><span class="line"><span class="n">msg</span><span class="p">[</span><span class="s">&#39;Reply-to&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;responder-aca@example.com&#39;</span>
      </span><span class="line"><span class="n">msg</span><span class="p">[</span><span class="s">&#39;To&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;vos@example.com&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Esto es lo que se ve si uno no tiene un lector de mails como la gente:</span>
      </span><span class="line"><span class="n">msg</span><span class="o">.</span><span class="n">preamble</span> <span class="o">=</span> <span class="s">&#39;Mensaje de multiples partes.</span><span class="se">\n</span><span class="s">&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Esta es la parte textual:</span>
      </span><span class="line"><span class="n">part</span> <span class="o">=</span> <span class="n">MIMEText</span><span class="p">(</span><span class="s">&quot;Hola, te paso un archivo interesante&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">msg</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Esta es la parte binaria (puede ser cualquier extensión):</span>
      </span><span class="line"><span class="n">part</span> <span class="o">=</span> <span class="n">MIMEApplication</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="s">&quot;factura.pdf&quot;</span><span class="p">,</span><span class="s">&quot;rb&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
      </span><span class="line"><span class="n">part</span><span class="o">.</span><span class="n">add_header</span><span class="p">(</span><span class="s">&#39;Content-Disposition&#39;</span><span class="p">,</span> <span class="s">&#39;attachment&#39;</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s">&quot;factura.pdf&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">msg</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">part</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Se pueden seguir agregando partes (texto, imágenes, datos binarios, etc.)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Crear una instancia del servidor para envio de correo (hacerlo una sola vez)</span>
      </span><span class="line"><span class="n">smtp</span> <span class="o">=</span> <span class="n">SMTP</span><span class="p">(</span><span class="s">&quot;smtp.example.com&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c"># Iniciar sesión en el servidor (si es necesario):</span>
      </span><span class="line"><span class="n">smtp</span><span class="o">.</span><span class="n">ehlo</span><span class="p">()</span>
      </span><span class="line"><span class="n">smtp</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="s">&quot;yo@example.com&quot;</span><span class="p">,</span> <span class="s">&quot;mipassword&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># Enviar el mail (o los mails)</span>
      </span><span class="line"><span class="n">smtp</span><span class="o">.</span><span class="n">sendmail</span><span class="p">(</span><span class="n">msg</span><span class="p">[</span><span class="s">&#39;From&#39;</span><span class="p">],</span> <span class="n">msg</span><span class="p">[</span><span class="s">&#39;To&#39;</span><span class="p">],</span> <span class="n">msg</span><span class="o">.</span><span class="n">as_string</span><span class="p">())</span>
      </span>

Autor / Autores:
::::::::::::::::

MarianoReingart_

