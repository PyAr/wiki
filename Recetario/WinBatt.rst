#format rst

WinBatt (ctypes + powrprof.dll en win)
--------------------------------------

Descripción
:::::::::::

Esta receta es un ejemplo de como utilizar funciones nativas de las bibliotecas de Windows desde python (usando ctypes_).

Por ejemplo, en este caso se usa para consultar el estado de la batería (carga en Wh y tiempos estimados, consumo de energía en Watts, etc.) usando la función  CallNtPowerInformation_ de la biblioteca de windows PowrProf_.lib (PowrProf_.dll).  También se ilustra como usar estructuras de C en python para llamar a funciones externas.

Es necesario tener una versión de Python con ctypes y estar sobre windows.

Ejemplo:
::::::::

El ejemplo en Python (winbatt.py) registra un objeto python MiMiniInterpretePython_, exponiendo:

* carga la biblioteca ´powrprof.dll´

* define la constante SystemBatteryState_ (InformationLevel_) de POWER_INFORMATION_LEVEL 

* define la estructura SYSTEM_BATTERY_STATE_

* inicializa la estructura en blanco

* llama a la función CallNtPowerInformation_

* imprime los resultados

Archivo winbatt.py

::

   .. raw:: html
      <span class="line"><span class="c"># -*- coding: iso-8859-1 -*-</span>
      </span><span class="line">
      </span><span class="line"><span class="kn">import</span> <span class="nn">ctypes</span>
      </span><span class="line">
      </span><span class="line"><span class="n">l</span> <span class="o">=</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">cdll</span><span class="o">.</span><span class="n">LoadLibrary</span><span class="p">(</span><span class="s">&quot;powrprof&quot;</span><span class="p">)</span>
      </span><span class="line">
      </span><span class="line"><span class="n">SystemBatteryState</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c"># POWER_INFORMATION_LEVEL enum</span>
      </span><span class="line">
      </span><span class="line"><span class="k">class</span> <span class="nc">SYSTEM_BATTERY_STATE</span><span class="p">(</span><span class="n">ctypes</span><span class="o">.</span><span class="n">Structure</span><span class="p">):</span>
      </span><span class="line">    <span class="n">_fields_</span> <span class="o">=</span> <span class="p">[</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;AcOnLine&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_bool</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;BatteryPresent&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_bool</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;Charging&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_bool</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;Discharging&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_bool</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;Spare1&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_bool</span> <span class="o">*</span> <span class="mi">4</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;MaxCapacity&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;RemainingCapacity&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;Rate&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;EstimatedTime&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;DefaultAlert1&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">(</span><span class="s">&quot;DefaultAlert2&quot;</span><span class="p">,</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">c_long</span><span class="p">),</span>
      </span><span class="line">                <span class="p">]</span>
      </span><span class="line">
      </span><span class="line">
      </span><span class="line"><span class="n">sb</span> <span class="o">=</span> <span class="n">SYSTEM_BATTERY_STATE</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
      </span><span class="line"><span class="n">retval</span> <span class="o">=</span> <span class="n">l</span><span class="o">.</span><span class="n">CallNtPowerInformation</span><span class="p">(</span><span class="n">SystemBatteryState</span><span class="p">,</span>
      </span><span class="line">                                  <span class="bp">None</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span>
      </span><span class="line">                                  <span class="n">ctypes</span><span class="o">.</span><span class="n">addressof</span><span class="p">(</span><span class="n">sb</span><span class="p">),</span> <span class="n">ctypes</span><span class="o">.</span><span class="n">sizeof</span><span class="p">(</span><span class="n">sb</span><span class="p">))</span>
      </span><span class="line"><span class="k">assert</span> <span class="n">retval</span> <span class="o">==</span> <span class="mi">0</span>  <span class="c"># debe devolver 0 si no hay error</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;AcOnLine:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">AcOnLine</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;Charging:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">Charging</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;Discharging:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">Discharging</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;Capacity:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">MaxCapacity</span><span class="p">,</span> <span class="s">&quot;mWh max&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">RemainingCapacity</span><span class="p">,</span> <span class="s">&quot;mWh remaining&quot;</span><span class="p">,</span>
      </span><span class="line"><span class="k">print</span> <span class="n">sb</span><span class="o">.</span><span class="n">RemainingCapacity</span><span class="o">*</span><span class="mi">100</span><span class="o">/</span><span class="n">sb</span><span class="o">.</span><span class="n">MaxCapacity</span><span class="p">,</span> <span class="s">&quot;%&quot;</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;Rate:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">Rate</span> <span class="o">/</span> <span class="mf">1000.0</span><span class="p">,</span> <span class="s">&quot;W&quot;</span>
      </span><span class="line"><span class="k">print</span> <span class="s">&quot;Estimated Time:&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">EstimatedTime</span> <span class="o">/</span> <span class="mi">3600</span><span class="p">,</span> <span class="s">&quot;h&quot;</span><span class="p">,</span> <span class="n">sb</span><span class="o">.</span><span class="n">EstimatedTime</span> <span class="o">/</span> <span class="mi">60</span> <span class="o">%</span> <span class="mi">60</span><span class="p">,</span> <span class="s">&quot;min&quot;</span>
      </span>

Para usarlo se puede ejecutar desde línea de comando:

::

   C:\src>python winbatt.py
   AcOnLine: False
   Charging: False
   Discharging: True
   Capacity: 45140 mWh max 5417 mWh remaining 12 %
   Rate: -9.435 W
   Estimated Time: 0 h 34 min

Para Descargar Fuentes: `attachment:winbatt.py`_winbatt.py`attachment:None`_

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _ctypes: http://docs.python.org/2/library/ctypes.html

.. _CallNtPowerInformation: http://msdn.microsoft.com/en-us/library/windows/desktop/aa372675(v=vs.85).aspx

.. _SYSTEM_BATTERY_STATE: http://msdn.microsoft.com/en-us/library/windows/desktop/aa373212(v=vs.85).aspx

