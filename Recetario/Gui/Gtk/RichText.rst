#format rst
## page was renamed from Recetario/Gtk/RichText

  == GtkRichText_ ==

Ejemplo sobre como mostrar texto con formato en un gtk.TextView_, se crea una clase que extiende gtk.TextBuffer_ para facilitar la inserción de texto con formato.

::

   .. raw:: html
      <span class="line"><span class="sd">&#39;&#39;&#39;a module that contains a class to insert rich text into a textview&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">gtk</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">pango</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">RichBuffer</span><span class="p">(</span><span class="n">gtk</span><span class="o">.</span><span class="n">TextBuffer</span><span class="p">):</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;a buffer that makes it easy to manipulate a gtk textview with </span>
      </span><span class="line"><span class="sd">    rich text&#39;&#39;&#39;</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;constructor&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">gtk</span><span class="o">.</span><span class="n">TextBuffer</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">colormap</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">colormap_get_system</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">fg_tags</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">bg_tags</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">font_tags</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">size_tags</span> <span class="o">=</span> <span class="p">{}</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">bold_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&quot;bold&quot;</span><span class="p">,</span> <span class="n">weight</span><span class="o">=</span><span class="n">pango</span><span class="o">.</span><span class="n">WEIGHT_BOLD</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">italic_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&quot;italic&quot;</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">pango</span><span class="o">.</span><span class="n">STYLE_ITALIC</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">underline_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&quot;underline&quot;</span><span class="p">,</span>
      </span><span class="line">            <span class="n">underline</span><span class="o">=</span><span class="n">pango</span><span class="o">.</span><span class="n">UNDERLINE_SINGLE</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">strike_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&quot;strike&quot;</span><span class="p">,</span> <span class="n">strikethrough</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">put_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">fg_color</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">bg_color</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
      </span><span class="line">        <span class="n">bold</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">italic</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">underline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">strike</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;insert text at the current position with the style defined by the </span>
      </span><span class="line"><span class="sd">        optional parameters&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_tags</span><span class="p">(</span><span class="n">fg_color</span><span class="p">,</span> <span class="n">bg_color</span><span class="p">,</span> <span class="n">font</span><span class="p">,</span> <span class="n">size</span><span class="p">,</span> <span class="n">bold</span><span class="p">,</span> <span class="n">italic</span><span class="p">,</span>
      </span><span class="line">            <span class="n">underline</span><span class="p">,</span> <span class="n">strike</span><span class="p">)</span>
      </span><span class="line">        <span class="n">iterator</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_iter_at_mark</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_insert</span><span class="p">())</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">_insert</span><span class="p">(</span><span class="n">iterator</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">tags</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterator</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">tags</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;insert text at the current position with the style defined by the </span>
      </span><span class="line"><span class="sd">        optional parameters&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">tags</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">insert_with_tags</span><span class="p">(</span><span class="n">iterator</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="o">*</span><span class="n">tags</span><span class="p">)</span>
      </span><span class="line">        <span class="k">else</span><span class="p">:</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">iterator</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_parse_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fg_color</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">bg_color</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
      </span><span class="line">        <span class="n">bold</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">italic</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">underline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">strike</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;parse the parameters and return a list of tags to apply that </span>
      </span><span class="line"><span class="sd">        format</span>
      </span><span class="line"><span class="sd">        &#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">tags</span> <span class="o">=</span> <span class="p">[]</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">fg_color</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_fg</span><span class="p">(</span><span class="n">fg_color</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">tag</span><span class="p">:</span>
      </span><span class="line">                <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">bg_color</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_bg</span><span class="p">(</span><span class="n">bg_color</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">tag</span><span class="p">:</span>
      </span><span class="line">                <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">font</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_font</span><span class="p">(</span><span class="n">font</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">tag</span><span class="p">:</span>
      </span><span class="line">                <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">size</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_size</span><span class="p">(</span><span class="n">size</span><span class="p">)</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">tag</span><span class="p">:</span>
      </span><span class="line">                <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">bold</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">bold_tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">italic</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">italic_tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">underline</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">underline_tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">if</span> <span class="n">strike</span><span class="p">:</span>
      </span><span class="line">            <span class="n">tags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">strike_tag</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">tags</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_parse_fg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;parse the foreground color and return a tag&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fg_tags</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fg_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="n">color</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">color_parse</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">colormap</span><span class="o">.</span><span class="n">alloc_color</span><span class="p">(</span><span class="n">color</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">None</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">color_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&#39;fg_&#39;</span> <span class="o">+</span> <span class="n">value</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">foreground_gdk</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">fg_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="n">color_tag</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">color_tag</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_parse_bg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;parse the background color and return a tag&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">bg_tags</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">bg_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">try</span><span class="p">:</span>
      </span><span class="line">            <span class="n">color</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">gdk</span><span class="o">.</span><span class="n">color_parse</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">colormap</span><span class="o">.</span><span class="n">alloc_color</span><span class="p">(</span><span class="n">color</span><span class="p">)</span>
      </span><span class="line">        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">None</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">color_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&#39;bg_&#39;</span> <span class="o">+</span> <span class="n">value</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">background_gdk</span><span class="o">=</span><span class="n">color</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">bg_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="n">color_tag</span>
      </span><span class="line">
      </span><span class="line">        <span class="k">return</span> <span class="n">color_tag</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_parse_font</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;parse the font and return a tag&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">font_tags</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">font_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">font_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&#39;font_&#39;</span> <span class="o">+</span> <span class="n">value</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="s">&#39;_&#39;</span><span class="p">),</span>
      </span><span class="line">            <span class="n">font</span><span class="o">=</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">font_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="n">font_tag</span>
      </span><span class="line">       
      </span><span class="line">        <span class="k">return</span> <span class="n">font_tag</span>
      </span><span class="line">
      </span><span class="line">    <span class="k">def</span> <span class="nf">_parse_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;parse the font size and return a tag&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="k">if</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">size_tags</span><span class="p">:</span>
      </span><span class="line">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">size_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span>
      </span><span class="line">
      </span><span class="line">        <span class="n">size_tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">create_tag</span><span class="p">(</span><span class="s">&#39;size_&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">),</span> <span class="n">size_points</span><span class="o">=</span><span class="n">value</span><span class="p">)</span>
      </span><span class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">size_tags</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="n">size_tag</span>
      </span><span class="line">        <span class="k">return</span> <span class="n">size_tag</span>
      </span><span class="line">
      </span><span class="line"><span class="k">def</span> <span class="nf">test</span><span class="p">():</span>
      </span><span class="line">    <span class="sd">&#39;&#39;&#39;do some tests with the buffer&#39;&#39;&#39;</span>
      </span><span class="line">    <span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="n">widget</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
      </span><span class="line">        <span class="sd">&#39;&#39;&#39;method called when the window is closed&#39;&#39;&#39;</span>
      </span><span class="line">        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line">    <span class="n">window</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">Window</span><span class="p">()</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">set_default_size</span><span class="p">(</span><span class="mi">640</span><span class="p">,</span> <span class="mi">480</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&#39;delete-event&#39;</span><span class="p">,</span> <span class="n">on_close</span><span class="p">)</span>
      </span><span class="line">    <span class="n">textview</span> <span class="o">=</span> <span class="n">gtk</span><span class="o">.</span><span class="n">TextView</span><span class="p">()</span>
      </span><span class="line">    <span class="n">buff</span> <span class="o">=</span> <span class="n">RichBuffer</span><span class="p">()</span>
      </span><span class="line">    <span class="n">textview</span><span class="o">.</span><span class="n">set_buffer</span><span class="p">(</span><span class="n">buff</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">textview</span><span class="p">)</span>
      </span><span class="line">    <span class="n">window</span><span class="o">.</span><span class="n">show_all</span><span class="p">()</span>
      </span><span class="line">    <span class="n">buff</span><span class="o">.</span><span class="n">put_text</span><span class="p">(</span><span class="s">&#39;buenas, como va? &#39;</span><span class="p">,</span> <span class="s">&#39;#CCCCCC&#39;</span><span class="p">,</span> <span class="s">&#39;#000000&#39;</span><span class="p">,</span> <span class="s">&#39;Arial&#39;</span><span class="p">,</span> <span class="mi">12</span><span class="p">)</span>
      </span><span class="line">    <span class="n">buff</span><span class="o">.</span><span class="n">put_text</span><span class="p">(</span><span class="s">&#39;esto es una prueba</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;#CC0000&#39;</span><span class="p">,</span> <span class="s">&#39;#AAAAAA&#39;</span><span class="p">,</span> <span class="s">&#39;Purisa&#39;</span><span class="p">,</span> <span class="mi">14</span><span class="p">)</span>
      </span><span class="line">    <span class="n">buff</span><span class="o">.</span><span class="n">put_text</span><span class="p">(</span><span class="s">&#39;un poco de formato</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;#00CC00&#39;</span><span class="p">,</span> <span class="s">&#39;#FFFFFF&#39;</span><span class="p">,</span> <span class="s">&#39;Andale Mono&#39;</span><span class="p">,</span>
      </span><span class="line">        <span class="mi">8</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">buff</span><span class="o">.</span><span class="n">put_text</span><span class="p">(</span><span class="s">&#39;un poco mas</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;#CCCCCC&#39;</span><span class="p">,</span> <span class="s">&#39;#0000CC&#39;</span><span class="p">,</span> <span class="s">&#39;Andale Mono&#39;</span><span class="p">,</span> <span class="mi">16</span><span class="p">,</span>
      </span><span class="line">        <span class="bp">False</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">False</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span>
      </span><span class="line">    <span class="n">gtk</span><span class="o">.</span><span class="n">main</span><span class="p">()</span>
      </span><span class="line">
      </span><span class="line"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
      </span><span class="line">    <span class="n">test</span><span class="p">()</span>
      </span>

`attachment:GtkRichText.png`_

mas info:

* http://pygtk.org/docs/pygtk/

* http://www.gtk.org/api/2.6/gtk/GtkTextTag.html

* http://pygtk.org/docs/pygtk/class-gtktextbuffer.html

