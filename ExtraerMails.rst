#format rst

Extraer direcciones de email de un texto
----------------------------------------

Código
::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="kn">import</span> <span class="nn">re</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mailsrch</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mailsrch</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">texto</span><span class="p">)</span>
      </span>

El código anterior devuelve una lista de strings, donde cada string es una dirección de email. El texto original puede contener basura como espcios, comas u otros caracteres.

Autor
:::::

JuanjoConti_

Fuente
::::::

http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

.. ############################################################################

.. _JuanjoConti: ../JuanjoConti

