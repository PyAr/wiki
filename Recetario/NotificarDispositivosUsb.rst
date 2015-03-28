
Detectar y Notificar Dispositivos USB
=====================================

* Como Detectar y Notificar Dispositivos USB, usando Python, en Linux, ejemplo simple.

::

   .. raw:: html
      <span class="line"><span class="c">#!/usr/bin/env python</span>
      </span><span class="line"><span class="c"># -*- coding: utf-8 -*- </span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">glib</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">gudev</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">pynotify</span>
      </span><span class="line"><span class="kn">import</span> <span class="nn">sys</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">callback</span><span class="p">(</span><span class="n">client</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">device</span><span class="p">,</span> <span class="n">user_data</span><span class="p">):</span>
      </span><span class="line">    <span class="n">device_vendor</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">get_property</span><span class="p">(</span><span class="s">&quot;ID_VENDOR_ENC&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="n">device_model</span> <span class="o">=</span> <span class="n">device</span><span class="o">.</span><span class="n">get_property</span><span class="p">(</span><span class="s">&quot;ID_MODEL_ENC&quot;</span><span class="p">)</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="s">&quot;add&quot;</span><span class="p">:</span>
      </span><span class="line">        <span class="n">n</span> <span class="o">=</span> <span class="n">pynotify</span><span class="o">.</span><span class="n">Notification</span><span class="p">(</span><span class="s">&quot;USB Device Added&quot;</span><span class="p">,</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s"> is now connected &quot;</span>
      </span><span class="line">                                  <span class="s">&quot;to your system&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">device_vendor</span><span class="p">,</span>
      </span><span class="line">                                  <span class="n">device_model</span><span class="p">))</span>
      </span><span class="line">        <span class="n">n</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line">    <span class="k">elif</span> <span class="n">action</span> <span class="o">==</span> <span class="s">&quot;remove&quot;</span><span class="p">:</span>
      </span><span class="line">        <span class="n">n</span> <span class="o">=</span> <span class="n">pynotify</span><span class="o">.</span><span class="n">Notification</span><span class="p">(</span><span class="s">&quot;USB Device Removed&quot;</span><span class="p">,</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s"> has been &quot;</span>
      </span><span class="line">                                  <span class="s">&quot;disconnected from your system&quot;</span> <span class="o">%</span>
      </span><span class="line">                                  <span class="p">(</span><span class="n">device_vendor</span><span class="p">,</span> <span class="n">device_model</span><span class="p">))</span>
      </span><span class="line">        <span class="n">n</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="k">if</span> <span class="ow">not</span> <span class="n">pynotify</span><span class="o">.</span><span class="n">init</span><span class="p">(</span><span class="s">&quot;USB Device Notifier&quot;</span><span class="p">):</span>
      </span><span class="line">    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="s">&quot;Couldn&#39;t connect to the notification daemon!&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">client</span> <span class="o">=</span> <span class="n">gudev</span><span class="o">.</span><span class="n">Client</span><span class="p">([</span><span class="s">&quot;usb/usb_device&quot;</span><span class="p">])</span>
      </span><span class="line"><span class="n">client</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;uevent&quot;</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
      </span><span class="line"><span class="c">#</span>
      </span><span class="line"><span class="n">loop</span> <span class="o">=</span> <span class="n">glib</span><span class="o">.</span><span class="n">MainLoop</span><span class="p">()</span>
      </span><span class="line"><span class="n">loop</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
      </span>

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

-------------------------



  CategoryRecetas_

