
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

Ahora podemos `atrapar al asesino`_ sin recurrir a Perl!!

La expresión regular que sigue es del proyecto django_. 

::

   .. raw:: html
      <span class="line"><span class="n">email_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span>
      </span><span class="line">            <span class="s">r&quot;(^[-!#$%&amp;&#39;*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&amp;&#39;*+/=?^_`{}|~0-9A-Z]+)*&quot;</span>  <span class="c"># dot-atom</span>
      </span><span class="line">            <span class="s">r&#39;|^&quot;([\001-\010\013\014\016-\037!#-\[\]-\177]|</span><span class="se">\\</span><span class="s">[\001-011\013\014\016-\177])*&quot;&#39;</span> <span class="c"># quoted-string</span>
      </span><span class="line">            <span class="s">r&#39;)@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">IGNORECASE</span><span class="p">)</span>  <span class="c"># domain</span>
      </span>

Se puede utilizar en la receta de Juanjo arriba.

Autor
:::::

JuanjoConti_

Fuente
::::::

http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _atrapar al asesino: http://xkcd.com/208/

.. _django: http://code.djangoproject.com/browser/django/trunk/django/core/validators.py#L116

