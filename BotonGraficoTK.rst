#format rst

Boton Grafico TK
================

Crear un boton grafico personalizado, con 3 estados posibles *(Activado, con el Roedor Encima, Normal)*, usando TK.

`attachment:temp.jpg`_

*En la foto de pantalla se muestra el Ejemplo con el Raton Encima (Mouse Over)*

* **Requisitos:** Es necesario saber usar encoding en Base64, que NO es cubierto por esta Receta, disculpe.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c"># Esto es okbutton.py</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">Tkinter</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">OkButton</span><span class="p">(</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">Button</span><span class="p">):</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">master</span><span class="p">,</span> <span class="n">data</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
      </span><span class="line">            <span class="k">if</span> <span class="n">data</span><span class="p">:</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">onImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;onImage&#39;</span><span class="p">])</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">offImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;offImage&quot;</span><span class="p">])</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">activeImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;activeImage&quot;</span><span class="p">])</span>
      </span><span class="line">            <span class="k">else</span><span class="p">:</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">onImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="nb">file</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;onImage&#39;</span><span class="p">])</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">offImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="nb">file</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;offImage&quot;</span><span class="p">])</span>
      </span><span class="line">                <span class="bp">self</span><span class="o">.</span><span class="n">activeImage</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="nb">file</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;activeImage&quot;</span><span class="p">])</span>                   
      </span><span class="line">            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&#39;activeImage&#39;</span><span class="p">],</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;onImage&quot;</span><span class="p">],</span> <span class="n">kwargs</span><span class="p">[</span><span class="s">&quot;offImage&quot;</span><span class="p">]</span>
      </span><span class="line">            <span class="n">Tkinter</span><span class="o">.</span><span class="n">Widget</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">master</span><span class="p">,</span> <span class="s">&#39;button&#39;</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Enter&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouseOver</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Leave&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouseLeave</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouseClick</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s">&quot;&lt;ButtonRelease-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouseLeave</span><span class="p">)</span>
      </span><span class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">mouseLeave</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">mouseOver</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Event</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="p">[</span><span class="s">&quot;image&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">onImage</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">mouseLeave</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Event</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="p">[</span><span class="s">&quot;image&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">offImage</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">mouseClick</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">Event</span><span class="p">):</span>
      </span><span class="line">        <span class="bp">self</span><span class="p">[</span><span class="s">&quot;image&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">activeImage</span>
      </span><span class="line">
      </span><span class="line"><span class="n">oexitOff</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span><span class="se">\</span>
      </span><span class="line"><span class="s">R0lGODlhXgAiAOf/AAABAAYAAAQABgUCBw0ACBMACRQACxUBDBMCEgkGDBAEDBkCFBYEDhsDEBIH</span>
      </span><span class="line"><span class="s">DxwFERgHERwGEhsHFx8HGBUMEhoLEyEKGh8MFRcPFB4OGyINGycMHR0QFyMOHCQPHR0SHCUQHh4U</span>
      </span><span class="line"><span class="s">HiMTHysRISAVIC0SIiQVICkUIi4TIyYWIioVIy4UJCIYIi8UJScXIzEWJi4YJioaJjQYKSsbKDIZ</span>
      </span><span class="line"><span class="s">LSwcKTEbKi4eKjkdLjAgLDIhLjkfNDwgMDwiNzYlMj4jODwlNEAkNTgnND8lOjopNj8oN0MnN0Io</span>
      </span><span class="line"><span class="s">PUUoOUEqOT4tOkQtO0csQUYvPkguQ0suP0QwQ0ovRUkxQEswRk4xQkozQkY1QlIxSEw0Q04zSEg2</span>
      </span><span class="line"><span class="s">Q001RE42RVA1SlM1Rko4RVU3SFE5SFQ4Tkw7SFU5T1o4UFc7UVc8UVo8TlY+TVJATWA+VlNES1pC</span>
      </span><span class="line"><span class="s">UWJAWGNBWWRCWmBEWllHVWZEXGJGXFdLV2ZHWWlGXmpHYGVJX1pNWWFMVWtIYWBNW2hLYW1KYmBR</span>
      </span><span class="line"><span class="s">WG9MZF5SXnFOZmZTYXJPaG5RaGJWYnZSa2pXZXNVbG1YYXhUbXlVbm1aaGtcY25baXtXcHxYcXha</span>
      </span><span class="line"><span class="s">cXBda31Zcn9bdIZbdoFddn1fdohdeIRfeXNmcopfeoxgfI5ifollfntrcpBkgItmgHpteZJmgo1o</span>
      </span><span class="line"><span class="s">gpRohJZqhpFshZdrh5ltiZVviZhuj4N2god3f55xjZhzjZxylKBzj5t1j6F0kIx8hIt9ip13kaN2</span>
      </span><span class="line"><span class="s">kox+i6J3maV4lKZ5laR5m6J8lqZ7nZODi6t9mql+oKp/oZeHj62CpLCCn5uKkq+EprWDp7GGqLmG</span>
      </span><span class="line"><span class="s">q7SJq7uIrZ+Sn7aLrbeMrqWUnL+MsbmOsLuQsqiYn8GPs6SaoKmZoMSRtaycpMaTt8eUuKmgpsiV</span>
      </span><span class="line"><span class="s">ucOXucmWu8qXvMuYvc2av86bwLalrdCcwdGdwrSqsNOfxNSgxdWhxtaiyNekydilyrqwt9qmy9un</span>
      </span><span class="line"><span class="s">zMC2vMq5wcS7wdfN09rQ1tzS2OHX3ufd4+rg5u7k6vvw9/7//P///yH+EUNyZWF0ZWQgd2l0aCBH</span>
      </span><span class="line"><span class="s">SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQYAACBRIqXMiwocOHECM6JBCgoMWLFyVq3Mix</span>
      </span><span class="line"><span class="s">o0OMIAdGjNBBQoOTKFOqXMmypUuVEko2YPAwpMWIEGCoSSSojs+fQIMKHUq0aFBBjwTJ+XKiQU2b</span>
      </span><span class="line"><span class="s">ACAe8PAl1Lx8+fBp3cq1q9evYMN2zacv3z14nLSIOPAxpFQRerzd6+evrt27ePPq3cu3r79+9rbp</span>
      </span><span class="line"><span class="s">ado248OpbKTZ28evsePHkCNLnky5suN99qT1EZKBLUPDDzNoeWWuHr3TqFOrXs26tevXqOvJTocs</span>
      </span><span class="line"><span class="s">lJULhUU6PMAghqNi0rIJH068uPHjyJMrN47N2rNgiWLQ/ExwNwIGD24ccnXrlq7v4MP+ix9Pvrz5</span>
      </span><span class="line"><span class="s">8+C737L1ihQg6bkZHrje4IEEFVL6JHLkCBIlSpAEKOCABBZo4IEIEvgfJPwtkgghe4wBhAcMIOCZ</span>
      </span><span class="line"><span class="s">QropxNsCD0zQwQYl4FAEFFJQwUUYXGCh4oostujiizDG2OKJXFAhxRNLJAGEDSdY8MACDFyYkEAL</span>
      </span><span class="line"><span class="s">8daABBZ4gIIMOPyABBNRTJFFF1lcYeWVWGap5ZZcdpnllFNMEQUTSPywgwwoeGCBSUEuRGRCB3Do</span>
      </span><span class="line"><span class="s">YQk08HBEFGCcscYbc9zh55+ABirooHfEIYYZfRKqaKBzvLHGGWBEcQQPNJTQwQQ/XghAAHBiN8EG</span>
      </span><span class="line"><span class="s">KOBwxBRnwPFHIY1UYgkmm2yiyav+sMYq66ywekEAQRz8QSuscwBgQqyXmABADZZU0kghf8BxxhRH</span>
      </span><span class="line"><span class="s">4IDCBpi2WcBBBfDW4QYv8MAEGXMUIkknpaCyCiyy1GLuuegaokMNjKDrbi2zxCBQBT7kUBEAebx7</span>
      </span><span class="line"><span class="s">LiIAfICuDwBg0Aosq6BSSieSFDIHGUzw8AK0D7SJUAEILBATCtqecUcknahSCzDDHKPMMiQ3Y/LJ</span>
      </span><span class="line"><span class="s">ySQhkADDnOzyyVwIlMrJy7Qh88snbwJACidjAQAFwyyjzDHDAFOLKp1EcscZDaNQ0gIIaMihBSEy</span>
      </span><span class="line"><span class="s">cUYglpxSizDLODONNtpw083YZHejzQ0DDVP22t0YIxAtbEsBQAxsj53K3GOn8XP+NN1wA/Y0ziwz</span>
      </span><span class="line"><span class="s">TC2nWBII0ziU4OMCbBGAQAMTeECDEWTcYQkqviRDjTbfjENOOaCjI/roKguEy+ioo04HADmkLvo0</span>
      </span><span class="line"><span class="s">AkXjOjqxAHADOjZToA06oJdDzjjfaENNMr6gYskdZBhBgwcTNIAARdh1gPEUcERyii/LXPMNOeio</span>
      </span><span class="line"><span class="s">w8734IPvx0CghG8++DkAoMj533MAwCjs08J67uCcrw465HxzzTK+nBIJHFPggdMiVhGLdUAGRyjD</span>
      </span><span class="line"><span class="s">IDpRi2RorxzeA1884qGNNiQhHrkYiB0myMEOdpACAEiFBzkoBPWNMB64IMg3PBg+dZRDf8moRScG</span>
      </span><span class="line"><span class="s">UYYjyOBpAoFciKIAB0moYhj+1PhGOb43QiLI7F4+OOEJQcgKJRYBAIg4YQYFIJAQrPCE33shNYah</span>
      </span><span class="line"><span class="s">CknAIQqJa55AHmABFPSgC3fQxCyUoQ1yeI+D8oijPLZQEAegQ454zGMcawAAS+gxjiR43x95wbpv</span>
      </span><span class="line"><span class="s">sAAACdBGHjnIDnWQQxvKmIUm7tCFHqDARwIJgPSCQIZAfGIXzOgGOtgxQT2CoiDN+KMq4wAAJfzx</span>
      </span><span class="line"><span class="s">HAKpxiBZJw92qEwA3NDjBNmBjm4wYxefCAQZguC0ewGgAy/4QRkKIYpeROMboyxlHtFBkEyoUpXQ</span>
      </span><span class="line"><span class="s">iKUex0cCVRIyB3GMRxMA4IByLDIevPxGNHohikKU4Qcv6ABBBJDMZTbzmdH+jMcf9UbLa6oyZrrD</span>
      </span><span class="line"><span class="s">oykE8gtv9lMe8UhfDfQpx12iQ53sdCc8qUgQFXDSk6AUJSkZushhEIOj/swjO+QFgCYYIg8pEMgk</span>
      </span><span class="line"><span class="s">rvlNPJ5DAQCgAx4d6ktgCjMIKrjIGdO4xja+UZohDaoc2WGIgnwgF/5sKR6XIRBiIHSXjoSkJCnZ</span>
      </span><span class="line"><span class="s">A4wIgIc+BKIQiajErnrVg8uIRS208dWydjCL39hiF79I0YsoQIEMdKAQI8hVs9r1rmVt4QuvEcMZ</span>
      </span><span class="line"><span class="s">lgGmISGAG6yHPe1xj67sS6xiF8vYxt4vf/vrXyTccCuoAKAIl8vc5jr3udDN7rOgDa1oXde73wVv</span>
      </span><span class="line"><span class="s">eMWzxBMtOxACeEFrXPM3GtjEVrfa2va2uK2t37QBOMERzlasvYgL0FCJVoRsZCXDmXKXy9zmMpdk</span>
      </span><span class="line"><span class="s">QjuGMFpRCTS4ACoBAQA7</span>
      </span><span class="line"><span class="s">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="n">oexitOn</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span><span class="se">\</span>
      </span><span class="line"><span class="s">R0lGODlhXgAiAOf/AAABAAYAAAcAAAkBAA0ACBAAARUAARYAAxQACxkADB0ADRoBDRwAFB4ADyIA</span>
      </span><span class="line"><span class="s">ER8BECEAFSUAEiQAFiQAFygAGCUBFywAGSsAHS0AGiIEFyYEGSoDGi4CICgHGzAFIzIHJCwMHzUJ</span>
      </span><span class="line"><span class="s">JzsIKTYKJzwJKhYA/zAQIhsA/z4LLB8A/yIA/0ANLT0PKEcMMUEPL0kQMwQQ/0AUMTkYKk0TNkcV</span>
      </span><span class="line"><span class="s">NDwaLUwUO0QYNFAWOS4N/08XPlcVPFAYP0kcOVkXPkoeOjMR/1gZRFkaREwgPFobRTYT/0QkO04h</span>
      </span><span class="line"><span class="s">PlkZflgfRlEciEUoOV4fSVEkQEsT/0soO2YfTWEiTGQfYmghT04X/04rPk4c2mMkTmUjWWojUGwl</span>
      </span><span class="line"><span class="s">UkMg/2smWFEzRFMg/3ApVm8qXGImsVQ2R1Yj/3EsXlgk/3AnnWUk/30uX1o8TV8r53wwZGcn/30x</span>
      </span><span class="line"><span class="s">ZX4yZmE9UF4/UYAzZ20v0WEv/3QvzYI1amBCU4o1bYU4bG4w/3Q0yGRFV4w3b3Az/2ZHWI45cWxH</span>
      </span><span class="line"><span class="s">W5A7c3w0/2xJYoY22ZI9dYw/c25LY3BLXmdOXn43/2xNXpQ/d3BNZZRBfZdBeZZDf5pCh51Cgos7</span>
      </span><span class="line"><span class="s">/5pEfJI/x41AzYM//59EhKFEf41C6o5C/51KhqRIiKVJinRba5hD8JFE/6ZKi55H2KdMjJhF/5xG</span>
      </span><span class="line"><span class="s">83lfb6hLq55I56lOjp9J9qtQkKtQoqVK8q1Skq1Nx7RRlLJRmrZSlqZP77BRvrdTl6tP6rVUnLlW</span>
      </span><span class="line"><span class="s">mb1UsoVre7FU4bxYm8NXnr5anbtV2bdW37hZxsNapr1aw8JbrItwgcZcqMJeoYxygsJcv8ddqb1c</span>
      </span><span class="line"><span class="s">18heqsJd08VdzsVfwspgrMxgp8peys1irs9ksJJ7hctkyNBmss9lxJd8jNJotNlmttRnwddnu9Np</span>
      </span><span class="line"><span class="s">tdpnt9tpuNxquZeDkd1rup6KmaCMm6KOnaaPmKWQn6iToqqVpLKdrbWgsLumtcCvt8mxu8iywtPE</span>
      </span><span class="line"><span class="s">0tfFzdbI1drI0dzL0+LQ2OjX3+vZ4e7c5PDe5/nq+P3r8/78/////yH+EUNyZWF0ZWQgd2l0aCBH</span>
      </span><span class="line"><span class="s">SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQoIABBxIqXMiwocOHECM2LDBAQMGLGDFK3Mix</span>
      </span><span class="line"><span class="s">o0eHGUMOjLgAQoMEKFOqXMmypcuXKxuYTIDgociLBSAmANEl0Z40QIMKHUq0qNGjQ/f4TPOkQwKH</span>
      </span><span class="line"><span class="s">BW4KhIhAw5NT7+7ds8e1q9evYMOKHfv1Hr579dx9elKhZsObVDXAWUevn7+7ePPq3cu3r9+//vjJ</span>
      </span><span class="line"><span class="s">UwfHKciMVDOIKTcvn77HkCNLnky5suXLkPPNKwdHBgS3CzHmfMhgyS528OKpXs26tevXsGPLXg2v</span>
      </span><span class="line"><span class="s">drtxp5YwmHiRKohF2syhS0e8uPHjyJMrX868OLrn6cpZSwQCtMKCDxEgWGDCz65k4MP+ix9Pvrz5</span>
      </span><span class="line"><span class="s">8+jNG9t1yk71w1MZak+woMEGI28ADRp0qBGi/QAGKOCABBZo4ICINHLIfoD44ccbVdTQlnUJjSQf</span>
      </span><span class="line"><span class="s">fQ04UAEGI8TQww8/DNHEEUOUaOKJKKao4oosonhEE0OA2MMNN7DwwQYPLEDTWwBc2MADG3ogAgkt</span>
      </span><span class="line"><span class="s">0DDDDDjwoAMPTDbp5JNQRinllE8uicORNLSwgggeYFDBAydRGF9C2zUQJJEz7EAEE1BMkcWbcMYp</span>
      </span><span class="line"><span class="s">55x0ZiGFEkhgUeeec04BBRNE7DBDCyR0WUEDC1gHgAAKlbnhCCvYQMQVXJCBhhtxxIHHppx26umn</span>
      </span><span class="line"><span class="s">nlqhwqikmgEqp2GM6umoMMThBhr+ZHBxBRE2rDCCl4iCdhCZ9VXAgQgv7DAFGG3cEQgjkEgiSSaZ</span>
      </span><span class="line"><span class="s">cOLss87KAQQMekBrLSeSwEBqEUCQqsa1z9IxKrRFjBqJJJAwEsgdbYAxxQ4viMDBoYkmNEBOCCRg</span>
      </span><span class="line"><span class="s">JgbAEqHFGnw8wgkprLwSy8Gx2KLwwrKUOyoqC0e8MBWjWsJwGaNWIvHChIw68aitHPwKK6Rw8ggf</span>
      </span><span class="line"><span class="s">a2hBRLy47lgAvgs8wOELRHwRRyGcsBJLLr8Mg8wxxywj9NDFdDsqLEMnPXQto46i9DJOqADD00Jr</span>
      </span><span class="line"><span class="s">IrXQY4yqC9DIDPNLLrGowkkhcXyx8q051vRyvmZ6sMIOWsTBSCex9IJMM9FQQw3+Nnz3zbfDKqTi</span>
      </span><span class="line"><span class="s">9+B8s6ECEIRjQ8yowiRuyuHYYKyCMn3rHU0zyPQSSyeMxKHFDit4cChNBQiwnQMYkGDDFWsUQrcv</span>
      </span><span class="line"><span class="s">zey9zTbc1G577XOQesntvNvebR+91z7qJME/DoTk0PA+OzbUNOPL5oWscYUNJGDgQKIW6RuB20KA</span>
      </span><span class="line"><span class="s">wQcnsfgiDTa0h2O++c+UUUQ4rpDKxvnwxx/OqJvIb365fdi/CqkqTGN/ONzYBjak8TxO8AEMQghd</span>
      </span><span class="line"><span class="s">BE4iEH1RYAQzgEIbHKGKXjQDG984nzg2KA6HbWJbHAyhCDc4qlKMcIP4O+H++DeNEZ7vG9hoRi9U</span>
      </span><span class="line"><span class="s">4Yg2QGEGI6AAAwEQs9TxQAv+eJBELIZBjW2Yb4PkSCI5tsC/UWVDiVCMYhK7pQgpJnFUl7Di/oAw</span>
      </span><span class="line"><span class="s">DVI5I4obNN82qDGMWEgCD1rgQfVyNBAHcIAEO/gCHzqBi2VggxvhEIcUL9HEYFjxj4YrghWzMSpm</span>
      </span><span class="line"><span class="s">aPFw5PCGw54hRXEAEBvLwEUn+PCFHZCAAw4giBtXIAQyGIIUFrxjHqVISFJV8Y9WBEYhpZg7Ffxx</span>
      </span><span class="line"><span class="s">i0kMR9RUcA0wPlKGpDAEGRKISYNwgJOeBOUF8ahHKUoOCKhEJRNV8EUlflAFrnglImPZLSCEA4qO</span>
      </span><span class="line"><span class="s">5EYMe5HLXa6AAxYhyAXgKEc62pGYVgzHLW5xzWRasRvaUoET8sCGeAoClbDtVGIp2YDNR0ZykpUk</span>
      </span><span class="line"><span class="s">wQUwQoIfBnGIRTxiMd3JUCWGIw9NVMEqkplPJfJiVLcgRxjDMcYynjGNJMiIACI4wQpeMIMKPaFK</span>
      </span><span class="line"><span class="s">VypCXpRiFc9gqUxD+MJt0tCGMwgnRgjQve+Fb3zl+59Qh0rUohI1gAMs4AGFQICbDCAKrXtd7MhH</span>
      </span><span class="line"><span class="s">u+BZ9apYzapWl9e853UielEYgFQEsgK50c1ueNNb4tbK1ra61a2Ww5zmOBeHFYyVIATgAc50xjOf</span>
      </span><span class="line"><span class="s">AY1qgA2sYAf7NKAdo2tfC9vYeNDUu15EA0lwAyUKhrCEbeyymM2sZjNb2VeQghJuSIIGpBIQADs=</span>
      </span><span class="line"><span class="s">&#39;&#39;&#39;</span>
      </span><span class="line"><span class="n">oexitActive</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span><span class="se">\</span>
      </span><span class="line"><span class="s">R0lGODlhXgAiAOffAEpLSU1LT09LSlVKS05MT1BMSlRLUFlKUlRMUVpLUl5KU1tMU11LWFpNWVxN</span>
      </span><span class="line"><span class="s">VF5MWV1OVV9NWmBOW0lMtVJKtl9QV2FPXGJPXWRPWFNLt2BRWFpKsmNQXmhPX1tLs2ZRWmlQYFxM</span>
      </span><span class="line"><span class="s">tGVSYGpRYV1NtWZTYWtSYmRVXF5OtmdUYmRWXVdRtl9Pt2hVY1lRt21UZGlWZG5VZWpXZW9WZmhZ</span>
      </span><span class="line"><span class="s">YWFTtGtYZnBXZ2laYWJUtWxZZ25WgnFYaGpbYnJWfmNVtm1aaHJZaXNYdGlVsmRWt3ZYb3hYanNa</span>
      </span><span class="line"><span class="s">amxdZGpWs3lZa2tYonRba2tXtHpabG5fZnZdbW1ZtnxcbnNblHtddGtjaG9at3tbinFiaXRas3Jj</span>
      </span><span class="line"><span class="s">anVbtH1fdn9fcXdcqHNka3ZctX5gd3pennRlbH9heHtfn3VmbXhet4BieXFoboBfm4Fjen5fs3do</span>
      </span><span class="line"><span class="s">b39ftIJke3hpcIBgtYNlfHRrcX9jpHlqcYFhtoRmfXVscollfnprcoplf4hkm4tmgIZloYlnhYdj</span>
      </span><span class="line"><span class="s">s4Fls4xngYhktIJmtI1ogoplqXlwdolltY5pg4pmtoxnq4VotpBqhHtyeIpppY1orJFrhYFxeYlp</span>
      </span><span class="line"><span class="s">snxzeY5prZJshpRri5JrkYpqs49qrpNth5NrnphsiJRuiJNrqpltiZJumZVviZpuipZvlYF4fptv</span>
      </span><span class="line"><span class="s">i5lum5NvpppvnJ1wjJRwp5hwo4N6gJtxk55xjZ5wmJlxpIR7gZxxn59yjp9xmZ1yoKBzj550lp5z</span>
      </span><span class="line"><span class="s">oaF0kKFzm4d+hJ91l6J1kaJ0nIh/haF2mKN1naR3k6J3mYqBh6N4moyDiY2Eio6Fi4+GjJCHjZGI</span>
      </span><span class="line"><span class="s">jpWMkpaNk5iPlZySmJ2TmZ6UmqWboaacoqKfo6OgpKqhp6yjqa2kqqmnq6qorK6ssK+tsbWytv//</span>
      </span><span class="line"><span class="s">////////////////////////////////////////////////////////////////////////////</span>
      </span><span class="line"><span class="s">/////////////////////////////////////////////////////yH+EUNyZWF0ZWQgd2l0aCBH</span>
      </span><span class="line"><span class="s">SU1QACH5BAEKAP8ALAAAAABeACIAAAj+AAEIHEiQYIECAxIqXMiwocOHECM6PFiwokWLEjNq3MjR</span>
      </span><span class="line"><span class="s">4cWPAyMaSJDAgMmTKFOqXMmyZUqSJQ08BFlRZIUnc9Jo2cmzp8+fQIMK9ZkGTxosPSDI9EgTAEQD</span>
      </span><span class="line"><span class="s">C3pIgnbtmrWrWLNq3cq1q1et17Bdq/bsUI+STD8+XTCGGbVu3uLKnUu3rt27ePN64zZt2RilaWs+</span>
      </span><span class="line"><span class="s">HFkF2bRs2rYpXsy4sePHkCNL3qYt27RjY06gZYgRYoIepZpFk0a6tOnTqFOrXs36dDRnxRzhSBBY</span>
      </span><span class="line"><span class="s">4NMKeoAhU8a7t+/fwIMLH048eLJjvOZUWLqw4GCTGtqUakW9uvXr2LNr3859eylKZpb+B26Y0gGN</span>
      </span><span class="line"><span class="s">MXDS19FTp7379/Djy59PXz779OnbfEGi2WTDkAydBBMDGJQAgwwy6ACEDgw26OCDEEYo4YQRLoig</span>
      </span><span class="line"><span class="s">DC2k8IEEDMTEnEK2LSRgAgxEYAEHIKRgggkvtOjiizDGKOOMNNYIw4opgMDBBRF06CFnTilkEkkl</span>
      </span><span class="line"><span class="s">XgCCCTHcwMMRRjChxJNQRinllFQKsYMPRVCpJZVMGHEEDzfEYAIIPProH4gIJTQkiRZ0YMINRzhB</span>
      </span><span class="line"><span class="s">RRdhkIHGnWvkqeeefPap5xITBBpoBlf4qecUE4SwJxohTIACGWF0QYUTR9xgQgcWmMncQWqOlMAD</span>
      </span><span class="line"><span class="s">FowQgxFShLGGHHns0YcgrBbi6qv+rorBAgpqwGprIYKgMGgNLAjqxa2vijGBB7DWMEEGf/SxRx5y</span>
      </span><span class="line"><span class="s">rBGGFEbEMIIFD5B0ZpoCMhDqDU5wscYehTRiiSWeeCKKKKCkq+4mOQiKibrwqttEoH6o24kVgfIR</span>
      </span><span class="line"><span class="s">r7p0JKpuEhNQcEm54zZSyB5rcOHEDdN2eJKII2k7wg1QkCFHIZZ0AooqHL/i8cceu+KCoJyAbPIr</span>
      </span><span class="line"><span class="s">oQT6yMkAo3Cyx4Y46jG+FJDiMceqgNJJJIXIQQYUDGcaU0IFrBlBBzE4QUYeiWwyiiq03KILLr5U</span>
      </span><span class="line"><span class="s">bXXV7QYKydVcV73FBC507UsqgZ4i9iJg+0IzLFbjossttKgyyiaJ5EGGEzF0EIH+tQYcNCQDF5hw</span>
      </span><span class="line"><span class="s">BBdyJOIJ1LpU3UswjDfOOBiCAuL45I2PzAbljG8wASGYQwI2zbVM3kvVusTtSSJycHGECRc43DcA</span>
      </span><span class="line"><span class="s">Qx59gxRrFLKJKrdUHQwxw/Q+TCpW5DBMJYJu4fvxyA9DwQSMJN+7sWw477mgtjhPTDBV36LKJoWs</span>
      </span><span class="line"><span class="s">IcUNesck0EgKWCB4GHlEMgotvuw+DDHGxG9M1ogIWoP8+Ocf//KK6B9/u2zwH/EEFQJb6I931/MF</span>
      </span><span class="line"><span class="s">LUYRiTyEYXUWUEBJxkeiC7zACWsQxOESRwz45W9eggrYL/znv5HFgYSNCoQAJ8CCXDSKAqnwXwd9</span>
      </span><span class="line"><span class="s">oQtVeEIQa3DCC1o3QYGQiAP+MZDCGxIBile0bxj+C0QIJ7AKEvovCxP4gf9+EShWrJAFxghG1gyo</span>
      </span><span class="line"><span class="s">v2Fg7xWgSMQbpBADDnSIIJ8CIhXk0Ij1HXGKIbSDE/23ikDFQn+QCwEJiYdFYxDjBwHbRRext8BG</span>
      </span><span class="line"><span class="s">yIEKZayWQR6gRja6MRhI9B++WDhHEs4LhvgbRKA0sUdKxo8YvXKBB+XnRQWOwpCI5MADClAQBgBR</span>
      </span><span class="line"><span class="s">iEQ0IiRJSIxPfGKUlcRfMHQ1gSGcYQskCJQbnMhH/P1ieVvIXynBKEYymtEiFsSgBlXBQVzm8pp+</span>
      </span><span class="line"><span class="s">PMMSPZCJORYTf6gI1CfkN8Ma3jCHO7xIAc6XvkciEJvwjB8qJpGJGMaTlu+ZIyQDHbg6Vl6EALOr</span>
      </span><span class="line"><span class="s">3e1y1z7eOe+gCE2oQhfauwT6Qnvc894NCECTAgSBcIZDnOIwx9GOevSjIA3G6GhoOtRxIQj+bIoI</span>
      </span><span class="line"><span class="s">lta0p0VtamKLqUxnSlOaug1ucqOb3UTQlIIEIAYXy9jGOvayohr1qEg9Ks50xjM5xCAAPb1IA24Q</span>
      </span><span class="line"><span class="s">hj6Mq1zn2pdWt8rVrnb1XARrRB/CcIMGNCUgADs=</span>
      </span><span class="line"><span class="s">&#39;&#39;&#39;</span>
      </span>

* **Ejemplo:** *(es el de la foto)*.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*-</span>
      </span><span class="line"><span class="c"># License: GPLv3</span>
      </span><span class="line"><span class="c">#import this</span>
      </span><span class="line"><span class="k">try</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">from</span> <span class="nn">Tkinter</span> <span class="kn">import</span> <span class="o">*</span>  <span class="c"># Python2</span>
      </span><span class="line"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
      </span><span class="line">    <span class="kn">from</span> <span class="nn">tkinter</span> <span class="kn">import</span> <span class="o">*</span>  <span class="c"># Python3</span>
      </span><span class="line"><span class="c">################################################################</span>
      </span><span class="line"><span class="kn">from</span> <span class="nn">okbutton</span> <span class="kn">import</span> <span class="o">*</span>  <span class="c"># This is the file, from the example ^_^</span>
      </span><span class="line"><span class="c">################################################################</span>
      </span><span class="line"><span class="n">root</span> <span class="o">=</span> <span class="n">Tk</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&#39;Boton&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">focus</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">resizable</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">botoncito</span> <span class="o">=</span> <span class="n">OkButton</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">onImage</span> <span class="o">=</span> <span class="n">oexitOn</span><span class="p">,</span> <span class="n">offImage</span> <span class="o">=</span> <span class="n">oexitOff</span><span class="p">,</span> <span class="n">activeImage</span> <span class="o">=</span> <span class="n">oexitActive</span><span class="p">,</span> <span class="n">bd</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">relief</span><span class="o">=</span><span class="s">&#39;flat&#39;</span><span class="p">,</span> <span class="n">cursor</span><span class="o">=</span><span class="s">&#39;hand2&#39;</span><span class="p">,</span> <span class="n">command</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">destroy</span><span class="p">)</span>
      </span><span class="line"><span class="n">botoncito</span><span class="o">.</span><span class="n">pack</span><span class="p">()</span>
      </span><span class="line"><span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

