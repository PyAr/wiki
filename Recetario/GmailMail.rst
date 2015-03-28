#format rst

GmailMail
---------

Este script permite enviar emails a través de GMail. Los emails pueden tener texto plano, HTML y archivos adjuntos (todos opcionales).

**Nota:** :small:`el script lo escribí originalmente en inglés. Debería entenderse, pero pienso traducirlo cuando tenga algo más de tiempo.`

**Archivo:** GmailMail.py

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line">
      </span><span class="line"><span class="c"># requires Python &gt;= 2.5</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">smtplib</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.multipart</span> <span class="kn">import</span> <span class="n">MIMEMultipart</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.base</span> <span class="kn">import</span> <span class="n">MIMEBase</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.text</span> <span class="kn">import</span> <span class="n">MIMEText</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.audio</span> <span class="kn">import</span> <span class="n">MIMEAudio</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.mime.image</span> <span class="kn">import</span> <span class="n">MIMEImage</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">email.encoders</span> <span class="kn">import</span> <span class="n">encode_base64</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">mimetypes</span> <span class="kn">import</span> <span class="n">guess_type</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">os.path</span> <span class="kn">import</span> <span class="n">basename</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">GmailMail</span><span class="p">():</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">gmail_user</span><span class="p">,</span> <span class="n">gmail_pwd</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">        Prepares an instance with basic authentication</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">        &quot;&quot;&quot;</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">gmail_user</span> <span class="o">=</span> <span class="n">gmail_user</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">gmail_pwd</span> <span class="o">=</span> <span class="n">gmail_pwd</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">getAttachment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">charset</span><span class="o">=</span><span class="s">&#39;ASCII&#39;</span><span class="p">):</span>
      </span><span class="line">        <span class="n">contentType</span><span class="p">,</span> <span class="n">encoding</span> <span class="o">=</span> <span class="n">guess_type</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">contentType</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">            <span class="n">contentType</span> <span class="o">=</span> <span class="s">&#39;application/octet-stream&#39;</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">mainType</span><span class="p">,</span> <span class="n">subType</span> <span class="o">=</span> <span class="n">contentType</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
      </span><span class="line">        <span class="n">_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">mainType</span> <span class="o">==</span> <span class="s">&#39;text&#39;</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachment</span> <span class="o">=</span> <span class="n">MIMEText</span><span class="p">(</span><span class="n">_file</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="n">subType</span><span class="p">,</span> <span class="n">charset</span><span class="p">)</span>
      </span><span class="line">        <span class="k">elif</span> <span class="n">mainType</span> <span class="o">==</span> <span class="s">&#39;message&#39;</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachment</span> <span class="o">=</span> <span class="n">email</span><span class="o">.</span><span class="n">message_from_file</span><span class="p">(</span><span class="n">_file</span><span class="p">)</span>
      </span><span class="line">        <span class="k">elif</span> <span class="n">mainType</span> <span class="o">==</span> <span class="s">&#39;image&#39;</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachment</span> <span class="o">=</span> <span class="n">MIMEImage</span><span class="p">(</span><span class="n">_file</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="n">_subType</span><span class="o">=</span><span class="n">subType</span><span class="p">)</span>
      </span><span class="line">        <span class="k">elif</span> <span class="n">mainType</span> <span class="o">==</span> <span class="s">&#39;audio&#39;</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachment</span> <span class="o">=</span> <span class="n">MIMEAudio</span><span class="p">(</span><span class="n">_file</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="n">_subType</span><span class="o">=</span><span class="n">subType</span><span class="p">)</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachment</span> <span class="o">=</span> <span class="n">MIMEBase</span><span class="p">(</span><span class="n">mainType</span><span class="p">,</span> <span class="n">subType</span><span class="p">)</span>
      </span><span class="line">            <span class="n">attachment</span><span class="o">.</span><span class="n">set_payload</span><span class="p">(</span><span class="n">_file</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
      </span><span class="line">            <span class="n">encode_base64</span><span class="p">(</span><span class="n">attachment</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">attachment</span><span class="o">.</span><span class="n">add_header</span><span class="p">(</span><span class="s">&#39;Content-Disposition&#39;</span><span class="p">,</span> <span class="s">&#39;attachment&#39;</span><span class="p">,</span>
      </span><span class="line">            <span class="n">filename</span><span class="o">=</span><span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>
      </span><span class="line">       
      </span><span class="line">        <span class="k">return</span> <span class="n">attachment</span>
      </span><span class="line">       
      </span><span class="line">    <span class="k">def</span> <span class="nf">send</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">to</span><span class="p">,</span> <span class="n">subject</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s">u&quot;&quot;</span><span class="p">,</span> <span class="n">html</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">attachments</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">charset</span><span class="o">=</span><span class="s">&quot;iso-8859-15&quot;</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="sd">        Sends an email through Gmail using the authentication</span>
      </span><span class="line"><span class="sd">        given to this instance.</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">        If given, attachments must be a list of paths pointing</span>
      </span><span class="line"><span class="sd">        to the files we want to include.</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">        This script does not embed inline content (multipart/related)</span>
      </span><span class="line">
      </span><span class="line"><span class="sd">        &quot;&quot;&quot;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">charset</span> <span class="ow">in</span> <span class="p">[</span><span class="s">&#39;utf8&#39;</span><span class="p">,</span><span class="s">&#39;utf-8&#39;</span><span class="p">]:</span> <span class="c">#bug?</span>
      </span><span class="line">            <span class="kn">from</span> <span class="nn">email.charset</span> <span class="kn">import</span> <span class="n">add_charset</span><span class="p">,</span> <span class="n">SHORTEST</span>
      </span><span class="line">            <span class="n">add_charset</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">SHORTEST</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">):</span>
      </span><span class="line">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">charset</span><span class="p">,</span> <span class="s">&#39;replace&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">html</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">):</span>
      </span><span class="line">            <span class="n">html</span> <span class="o">=</span> <span class="n">html</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">charset</span><span class="p">,</span> <span class="s">&#39;replace&#39;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">attachments</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">            <span class="n">attachments</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">       
      </span><span class="line">        <span class="k">if</span> <span class="n">text</span><span class="p">:</span> <span class="n">plain_part</span> <span class="o">=</span> <span class="n">MIMEText</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="s">&#39;plain&#39;</span><span class="p">,</span> <span class="n">charset</span><span class="p">)</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">html</span><span class="p">:</span> <span class="n">html_part</span> <span class="o">=</span> <span class="n">MIMEText</span><span class="p">(</span><span class="n">html</span><span class="p">,</span> <span class="s">&#39;html&#39;</span><span class="p">,</span> <span class="n">charset</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">is_alternative</span> <span class="o">=</span> <span class="n">html</span> <span class="ow">and</span> <span class="n">text</span>
      </span><span class="line">        <span class="n">layers</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">attachments</span> <span class="ow">or</span> <span class="n">is_alternative</span><span class="p">:</span>
      </span><span class="line">            <span class="n">msg</span> <span class="o">=</span> <span class="n">MIMEMultipart</span><span class="p">()</span> <span class="c">#mixed</span>
      </span><span class="line">            <span class="n">msg</span><span class="o">.</span><span class="n">set_charset</span><span class="p">(</span><span class="n">charset</span><span class="p">)</span>
      </span><span class="line">            <span class="n">msg</span><span class="o">.</span><span class="n">preamble</span> <span class="o">=</span> <span class="s">&#39;This is a multi-part message in MIME format.&#39;</span>
      </span><span class="line">            <span class="n">msg</span><span class="o">.</span><span class="n">epilogue</span> <span class="o">=</span> <span class="s">&#39;&#39;</span>
      </span><span class="line">            <span class="n">layers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span>
      </span><span class="line">           
      </span><span class="line">            <span class="k">if</span> <span class="n">is_alternative</span><span class="p">:</span>
      </span><span class="line">                <span class="n">msgAlternative</span> <span class="o">=</span> <span class="n">MIMEMultipart</span><span class="p">(</span><span class="s">&#39;alternative&#39;</span><span class="p">)</span>
      </span><span class="line">                <span class="n">msg</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">msgAlternative</span><span class="p">)</span>
      </span><span class="line">                <span class="n">layers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msgAlternative</span><span class="p">)</span>
      </span><span class="line">           
      </span><span class="line">            <span class="k">if</span> <span class="n">text</span><span class="p">:</span>
      </span><span class="line">                <span class="n">layers</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">plain_part</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">html</span><span class="p">:</span>
      </span><span class="line">                <span class="n">layers</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="n">html_part</span><span class="p">)</span>
      </span><span class="line">           
      </span><span class="line">        <span class="k">elif</span> <span class="n">text</span><span class="p">:</span>
      </span><span class="line">            <span class="n">msg</span> <span class="o">=</span> <span class="n">plain_part</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span> <span class="c">#html only</span>
      </span><span class="line">            <span class="n">msg</span> <span class="o">=</span> <span class="n">html_part</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">attachments</span><span class="p">:</span>
      </span><span class="line">            <span class="n">msg</span><span class="o">.</span><span class="n">attach</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">getAttachment</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">charset</span><span class="p">))</span>
      </span><span class="line">       
      </span><span class="line">        <span class="n">msg</span><span class="p">[</span><span class="s">&#39;From&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gmail_user</span>
      </span><span class="line">        <span class="n">msg</span><span class="p">[</span><span class="s">&#39;To&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">to</span>
      </span><span class="line">        <span class="n">msg</span><span class="p">[</span><span class="s">&#39;Subject&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">subject</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">mailServer</span> <span class="o">=</span> <span class="n">smtplib</span><span class="o">.</span><span class="n">SMTP</span><span class="p">(</span><span class="s">&quot;smtp.gmail.com&quot;</span><span class="p">,</span> <span class="mi">587</span><span class="p">)</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">ehlo</span><span class="p">()</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">starttls</span><span class="p">()</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">ehlo</span><span class="p">()</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">gmail_user</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">gmail_pwd</span><span class="p">)</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">sendmail</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">gmail_user</span><span class="p">,</span> <span class="n">to</span><span class="p">,</span> <span class="n">msg</span><span class="o">.</span><span class="n">as_string</span><span class="p">())</span>
      </span><span class="line">        <span class="c"># Should be mailServer.quit(), but that crashes...</span>
      </span><span class="line">        <span class="n">mailServer</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
      </span>

Algunos tests (ejemplos, casos de uso):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Archivo:** GmailMail_tests.py

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">from</span> <span class="nn">GmailMail</span> <span class="kn">import</span> <span class="n">GmailMail</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">urlopen</span>
      </span><span class="line">
      </span><span class="line"><span class="n">text</span> <span class="o">=</span> <span class="s">u&quot;&quot;&quot;</span><span class="se">\</span>
      </span><span class="line"><span class="s">Éste es el contenido en modo texto plano</span>
      </span><span class="line"><span class="s">Tenemos acentos y eñes.</span>
      </span><span class="line">
      </span><span class="line"><span class="s">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="n">url</span> <span class="o">=</span> <span class="s">&quot;http://python.com.ar/moin&quot;</span>
      </span><span class="line"><span class="n">html</span> <span class="o">=</span> <span class="n">urlopen</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="n">user</span> <span class="o">=</span> <span class="s">&#39;XXXXXX@gmail.com&#39;</span> <span class="c"># mi usuario de GMail</span>
      </span><span class="line"><span class="n">pwd</span>  <span class="o">=</span> <span class="s">&#39;********&#39;</span>         <span class="c"># mi contraseña de GMail</span>
      </span><span class="line">
      </span><span class="line"><span class="n">m</span> <span class="o">=</span> <span class="n">GmailMail</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">pwd</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando texto plano solamente&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba de sólo texto&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando html solamente&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con sólo html&#39;</span><span class="p">,</span> <span class="n">html</span><span class="o">=</span><span class="n">html</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando texto plano y html (sin attachments)&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con texto plano y html (sin attachments)&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">html</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando texto plano y attachments&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con texto plano y attachments&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">attachments</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GmailMail.py&#39;</span><span class="p">])</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando html y attachments&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con html y attachments&#39;</span><span class="p">,</span> <span class="n">html</span><span class="o">=</span><span class="n">html</span><span class="p">,</span> <span class="n">attachments</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GmailMail.py&#39;</span><span class="p">])</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando attachments solamente&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con attachments solamente&#39;</span><span class="p">,</span> <span class="n">attachments</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GmailMail.py&#39;</span><span class="p">])</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;mandando todo&quot;</span>
      </span><span class="line"><span class="n">m</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="s">u&#39;prueba con todo&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">html</span><span class="p">,</span> <span class="n">attachments</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GmailMail.py&#39;</span><span class="p">])</span>
      </span>

Referencias (que recuerdo):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://docs.python.org/lib/module-email.html  

* http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/  

* http://mg.pov.lt/blog/unicode-emails-in-python.html  

* http://www.peterbe.com/plog/zope-html-emails  

-------------------------



  CategoryRecetas_

