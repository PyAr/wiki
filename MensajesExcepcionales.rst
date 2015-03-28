#format rst

Mensajes Excepcionales
======================

  *"10. Los errores nunca deberían dejarse pasar silenciosamente."* PythonZen_

Esta página busca ser una guía para las personas que se estén iniciando en este maravilloso lenguaje y se encuentren con errores comunes y no sepan como solucionarlos.

La idea es presentar ejemplos de excepciones, su traducción al español y una posible solución en cada caso.

¿Que son las excepciones?
-------------------------

Las Excepciones (``Exceptions`` en inglés) son condiciones excepcionales que eleva el sistema operativo, el lenguaje, o nuestro mismo programa.

No necesariamente pueden ser un error, también existen advertencias que en general no interrumpen el flujo del programa.

¿Que son los tracebacks (trazas de rastreo)?
--------------------------------------------

Las trazas de rastreo (``Traceback`` en inglés) es la información que reúne el lenguaje para informarnos sobre una excepción que ha ocurrido.

Por ejemplo:

::

   .. raw:: html
      <span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;form.py&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">78</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line">    <span class="n">f</span> <span class="o">=</span> <span class="n">Form</span><span class="p">(</span><span class="s">&quot;factura.csv&quot;</span><span class="p">)</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;form.py&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">12</span><span class="p">,</span> <span class="ow">in</span> <span class="n">__init__</span>
      </span><span class="line">    <span class="k">for</span> <span class="n">linea</span> <span class="ow">in</span> <span class="nb">open</span><span class="p">(</span><span class="n">infile</span><span class="p">)</span><span class="o">.</span><span class="n">readlines</span><span class="p">():</span>
      </span><span class="line"><span class="ne">IOError</span><span class="p">:</span> <span class="p">[</span><span class="n">Errno</span> <span class="mi">2</span><span class="p">]</span> <span class="n">No</span> <span class="n">such</span> <span class="nb">file</span> <span class="ow">or</span> <span class="n">directory</span><span class="p">:</span> <span class="s">&#39;factura.csv&#39;</span>
      </span>

Se traduciría a:

::

   Traza de rastreo (llamada más reciente a lo último):
     Archivo "form.py", línea 78, en <módulo>
       f = Form("factura.csv")
     Archivo "form.py", línea 12, en __init__
       for linea in open(infile).readlines():
   IOError: [Errno 2] No existe el archivo o directorio: 'factura.csv'

Y nos dice que:

* Se produjo una excepción del tipo IOError con el mensaje "[Errno 2] No existe el archivo o directorio: 'factura.csv'"

* El problema surgió en la línea 12 de ``form.py`` (dentro de la función ``__init__``): ``for linea in open(infile).readlines():``

* Esta función fue llamada desde la línea 78 del mismo archivo (en el módulo, fuera de una función): ``f = Form("factura.csv")`` 

* y así sucesivamente (si tuvieramos más llamadas encadenadas, la lista sería más larga)

En este ejemplo, vemos que le estamos pasando un nombre de archivo que no existe ('factura.csv'), y para corregir el error deberíamos modificar la línea 78.

Aquí es donde se ve la utilidad de las trazas, a veces el error no es culpa de la línea en el que es producido, sino viene arrastrando un dato o condición inválida desde otro punto del programa.

Que el árbol no nos impida ver el bosque ... |:-)|

Errores comunes
---------------

Errores de Sangría (IdentationError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"7. La legibilidad cuenta."* PythonZen_

En Python es fundamental dejar sangría (espacio antes de las instrucciones), que identifica el bloque al que pertenece, ya que no usamos llaves o palabras clave para delimitar los bloques como en otros lenguajes. Si bien esto ayuda a escribir código más prolijo evitando errores de anidación, puede ser raro hasta que uno se acostumbra.

Generalmente, cada vez que abramos un bloque (con una sentencia que termina en : -dos puntos- ), debemos incrementar la sangría. Por ej:

::

   .. raw:: html
      <span class="line"><span class="k">def</span> <span class="nf">mayor</span><span class="p">(</span><span class="n">param1</span><span class="p">,</span> <span class="n">param2</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">param1</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;El valor es None=Nulo! :S&quot;</span>
      </span><span class="line">    <span class="k">elif</span> <span class="n">param1</span><span class="o">&gt;</span><span class="n">param2</span><span class="p">:</span>
      </span><span class="line">        <span class="k">print</span> <span class="n">param1</span><span class="p">,</span><span class="s">&quot;es mayor a&quot;</span><span class="p">,</span> <span class="n">param2</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;todo bien :)&quot;</span>
      </span><span class="line">    <span class="k">else</span><span class="p">:</span>
      </span><span class="line">        <span class="k">print</span> <span class="n">param1</span><span class="p">,</span><span class="s">&quot;es menor a&quot;</span><span class="p">,</span> <span class="n">param2</span>
      </span><span class="line">        <span class="k">return</span> <span class="s">&quot;todo mal :(&quot;</span>
      </span><span class="line">
      </span><span class="line"><span class="k">print</span> <span class="n">mayor</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
      </span>

Que puede pasar si no lo hacemos...

Error de Sangría: se esperaba un bloque con sangría
:::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">if</span> <span class="bp">True</span><span class="p">:</span>
      </span><span class="line"><span class="o">...</span> <span class="k">print</span> <span class="s">&quot;verdad!&quot;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">2</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;verdad!&quot;</span>
      </span><span class="line">        <span class="o">^</span>
      </span><span class="line"><span class="ne">IndentationError</span><span class="p">:</span> <span class="n">expected</span> <span class="n">an</span> <span class="n">indented</span> <span class="n">block</span>
      </span>

Aquí el ``print`` esta a la misma altura que el ``if`` (sin sangría), cuando deberíamos haber dejado el espacio correspondiente porque estamos abriendo un nuevo bloque con ``:``

Error de Sangría: sangría no esperada
:::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="s">&quot;hola&quot;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span>    <span class="k">print</span> <span class="s">&quot;chau&quot;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;chau&quot;</span>
      </span><span class="line">   <span class="o">^</span>
      </span><span class="line"><span class="ne">IndentationError</span><span class="p">:</span> <span class="n">unexpected</span> <span class="n">indent</span>
      </span>

Aquí el ``print "chau"`` *no* esta a la misma altura que el ``print "hola"``, como no abrimos un bloque con ``:``, no es necesario dejar espacio para la sangría.

Error de Sangría: la nueva sangría no coincide con ningún otro nivel exterior
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">def</span> <span class="nf">prueba</span><span class="p">():</span>
      </span><span class="line"><span class="o">...</span>     <span class="k">if</span> <span class="bp">False</span><span class="p">:</span>
      </span><span class="line"><span class="o">...</span>         <span class="k">pass</span>
      </span><span class="line"><span class="o">...</span>   <span class="k">print</span> <span class="s">&quot;...&quot;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">4</span>
      </span><span class="line">    <span class="k">print</span> <span class="s">&quot;...&quot;</span>
      </span><span class="line">             
      </span><span class="line"><span class="o">^</span>
      </span><span class="line"><span class="ne">IndentationError</span><span class="p">:</span> <span class="n">unindent</span> <span class="n">does</span> <span class="ow">not</span> <span class="n">match</span> <span class="nb">any</span> <span class="n">outer</span> <span class="n">indentation</span> <span class="n">level</span>
      </span>

Aquí el ``print "..."`` *no* esta a la misma altura que el ``if False`` ni que el ``pass`` ni que el ``def``, por lo que no se sabe a que bloque pertenece. Si cerramos el bloque del ``if`` debería estar a la misma altura que este, y si pertenece al bloque ``if``, debería estar dentro de este a la altura del ``pass``. Si el ``print`` no pertenece a la función, deberíamos ponerlo a la misma altura que el ``def``

Errores de Sintaxis (SyntaxError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"13. Debería haber una — y preferiblemente sólo una — manera obvia de hacerlo."* PythonZen_

La sintaxis, como en cualquier lenguaje, es fundamental para que Python entienda lo que estamos queriendole decir, ya que es estricto y se reusará a ejecutar cualquier código que no siga las reglas de sintáxis definidas (que por cierto, no son muchas), a saber:

* **Mayúsculas y Minúsculas, identificadores (nombres) y palabras clave**: empiezan con una letra, pueden continuar con letras (a..z o A..Z), dígitos (0..9) o guión bajo (_). Python reconoce la diferencia (es "case sensitive" o sensible a mayúsculas y minúsculas), por lo que ``Hola`` y ``hola`` son dos identificadores distintos! Se recomienda escribir:

  * Nombres de variable y módulos (archivos) en minúsculas con las palabras separadas por guión bajo ('_'), por ejemplo: ``mi_variable_x``

  * Nombres de clases en CamelCase_ (primer letra de cada palabra en mayúscula, luego minúsculas, sin separar por espacios), por ejemplo: ``MiClasePunto``

* **Palabras clave reservadas**: deben ser escritas tal cual, deben estar al principio de una linea y/o separadas con espacios y no pueden ser usadas como nombres de variables: and as assert break class continue def elif else except exec finally for global if import in is lambda or pass print raise return try with yield. 

  * Sentencias simples ``assert pass del print return yield raise break continue import global exec``: son comprendidos dentro de una línea lógica y varias sentencias simples pueden estar en una sola línea separadas por punto y coma

  * Sentencias compuestas ``if while for try with def class``: contienen (grupos de) otras sentencias; y de alguna manera afectan el control de la ejecución de los mismos. En general, abarcan múltiples líneas.

* **Literales**: los valores "constantes" pueden escribirse según su tipo:

  * Cadenas (strings): encerrados por comillas simples o dobles (sin diferencia), ej: ``"mi cadena"`` o ``'mi cadena'``

    * Unicode: se identifican con una u antes de la cadena, por ej: ``u"Mi texto en español"``

    * Raw (Crudo): se identifican con una r, son textos sin interpretar los escapes ("\"), por ej: ``r"c:\config.sys"``

    * Con triple comilla simple (``'''``) o triple comilla doble (``"""`` se encierran textos que se pueden extender varias líneas

  * Números: en general, solo números separados por el punto ("coma decimal"), ej: ``1234.567``

    * Prefijos: se utilizan para diferenciar la base en que está escrito el número:

      * Hexadecimales (base 16): 0x1234

      * Binarios (base 2): 0b01010101 (solo Python 2.6 o superior)

      * Octales (base 8): 0o666 (solo Python 2.6 o superior), 0666 (solo Python 2.6 o inferior)

    * Sufijos: se utlizan para denotar el tipo de número:

      * Largos: 123456789012345678901234567890L (long)

      * Imaginarios: 1234j

    * Notación científica: se indica con una e o E en el medio: ``1e100``, ``3.14e-10`` (no confundir con el número irracional, el exponente es en base 10)

* **Operadores**:

  * Unarios:  reciben un operando: ``~ -``, por ej la negación: ``-1``

  * Binarios: reciben dos operandos:

    * Aritméticos ``+ - * ** / // %``: para cálculos, por ej: ``1 + 2`` (sumar 1 y 2)

    * Relacionales ``< > <= >= == !=``: para comparaciones, por ej: ``a != b`` (¿a es diferente de b?)

    * A nivel de bit ``<< >> & | ^``: por ej. ``5>>6`` (

* **Delimitadores**: determinados caracteres indican determinadas acciones y funcionan como "separadores", cualquier otro uso (o su no utilización) no especificado a continuación generará un error:

  * Paréntesis (): definen tuplas "de elementos": ``(1,2,3,4)`` o permiten llamar a una función/crear una clase, ``mi_funcion(123)``

  * Corchetes []: definen listas "de elementos": ``["uno", "dos", "tres"]`` o permiten acceder por índice/clave a una colección: ``mi_lista[posición]``

  * Diccionarios {}: definen diccionarios (asociando un valor a una clave) por ej. ``{'clave':'valor'``} o conjuntos

  * Decorador @: aplican una función a una función o clase, por ej ``@requiere_acceso``

  * Coma ``,``: separa expresiones o elementos de una secuencia, por ej: ``1, 2, 3``

  * Dos puntos ``:``: inicia bloques (con o sin sangría), elementos en un diccionario o anotaciones en una función (Python3Mil_)

  * Igual ``=``: asigna una expresión a un nombre, por ej. ``mi_variable=5`` No confundir con igualdad: ``a==b`` También puede usarse la asignación aumentada, combinando un operador, por ej: ``a+=1`` (asigna el valor de ``a+1`` a ``a``)

  * Punto y coma ``;``: separa varias instrucciones en una misma línea, por ej. ``a=1; b=2; c=a+b``. *Sí, se puede como en C, pero tratar de no usar...*

* **Comentarios**: cualquier línea que empieze con numeral (#) es un comentario y será ignorada (independientemente de lo que tiene adentro y si tiene sangría o no)

* **Caracteres sin significado**: No usar el signo pesos ($) o el signo de interrogación (?) ya que no se utilizan en Python fuera de las cadenas y producirá un error.

Esperando no haberlo abrumado con el resumen de la sintaxis del lenguaje (los interesados pueden ver la especificación completa en http://docs.python.org/), veamos que pasa si no la respetamos:

Error de Sintaxis: sintaxis inválida
::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">If</span> <span class="n">a</span><span class="o">&gt;</span><span class="mi">1</span><span class="p">:</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="n">If</span> <span class="n">a</span><span class="o">&gt;</span><span class="mi">1</span><span class="p">:</span>
      </span><span class="line">       <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">syntax</span>
      </span>

Python respeta mayúsculas y minusculas, ``If`` no es el ``if`` que queremos usar. Tener cuidado sobre todo si venimos de lenguajes que son indiferentes a este tema (por. ej. Visual Basic)

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">secuencia</span> <span class="o">=</span> <span class="mi">1</span> <span class="mi">2</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="n">secuencia</span> <span class="o">=</span> <span class="mi">1</span> <span class="mi">2</span>
      </span><span class="line">                  <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">syntax</span>
      </span>

Debemos indicar un operador entre las expresiones o un delimitador entre los elementos.  En este caso nos falto la coma ``secuencia = 1, 2``

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">if</span> <span class="n">a</span><span class="o">==</span><span class="mi">1</span>
      </span><span class="line"><span class="o">...</span>    <span class="k">print</span> <span class="s">&quot;a es verdadero!&quot;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="k">if</span> <span class="n">a</span><span class="o">==</span><span class="mi">1</span>
      </span><span class="line">      
      </span><span class="line"><span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">syntax</span>
      </span>

Las sentencias compuestas, deben terminar con dos puntos (":") para indicar el nuevo bloque que afectan ``if a==1:``

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">while</span> <span class="n">a</span><span class="o">=</span><span class="mi">1</span><span class="p">:</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="k">while</span> <span class="n">a</span><span class="o">=</span><span class="mi">1</span><span class="p">:</span>
      </span><span class="line">           <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">syntax</span>
      </span>

La asignación no se puede usar en una expresión (comparación), por ej., para evitar los errores clásicos en C ``while(v=1)...`` donde nos asignaba ``1`` a ``v`` en vez de comparar si ``v`` era igual a ``1``. En este caso, usar el operador de comparación ``while a==1:``

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">def</span> <span class="nf">a</span><span class="p">:</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="k">def</span> <span class="nf">a</span><span class="p">:</span>
      </span><span class="line">         <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">syntax</span>
      </span>

Por más que no tengamos parámetros en nuestra función, los paréntesis son obligatorios. Sería: ``def a():``

Error de Sintaxis: FinDeLinea mientras se buscaba una cadena "simple"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="s">&#39;abc&quot;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="s">&#39;abc&quot;</span>
      </span><span class="line">        <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">EOL</span> <span class="k">while</span> <span class="n">scanning</span> <span class="n">single</span><span class="o">-</span><span class="n">quoted</span> <span class="n">string</span>
      </span>

Las cadenas simples (de una sola línea) deben empezar y terminar en la misma línea y con el mismo caracter, comillas (") o tilde (').

Error de Sintaxis: FinDeArchivo mientras se buscaba una cadena de "múltiples líneas"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="s">&quot;&quot;&quot;</span>
      </span><span class="line"><span class="s">... mucho </span>
      </span><span class="line"><span class="s">... texto</span>
      </span><span class="line"><span class="s">...</span>
      </span><span class="line"><span class="s">SyntaxError: EOF while scanning triple-quoted string</span>
      </span>

Las cadenas de múltiples líneas, deben empezar con triple comilla o tilde, y terminar con lo mismo. Aquí faltó cerrar la cadena con ``"""`` Nota: el error es simulado, es difícil que suceda en el intérprete, pero si ocurre en un archivo)

Error de Sintaxis: no es posible asignar a un operador
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">numero</span><span class="o">+</span><span class="n">antiguo</span><span class="o">=</span><span class="mi">1</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">can</span><span class="s">&#39;t assign to operator (&lt;input&gt;, line 1)</span>
      </span>

El nombre de la variable es inválido, sería: ``numero_mas_antiguo=1``

Error de Sintaxis: "token" inválido
:::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="mo">08</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line">    <span class="k">print</span> <span class="mo">08</span>
      </span><span class="line">           <span class="o">^</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">token</span>
      </span>

El compilador de Python es muy estricto, y si no recibe el símbolo/componente léxico correcto ("token") nos emitirá estos errores. En este caso, se debe a que los numeros que comienzan con 0 es un caso especial de notación octal (base 8), por lo que solo acepta números del 0 al 7. Para corregir el error, eliminar el 0 que precede al número ``print 8``

Errores de Nombres (NameError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"2. Explícito es mejor que implícito."* PythonZen_

Si bien Python es dinámico y no tenemos que declarar las variables y funciones al principio de nuestro programa, estas deben existir (estar definidas o "inicializadas") antes de poder usarlas.

O sea, previamente debimos haberle asignado un valor a una variable (con ``=``), definido una función con ``def`` o clase con ``class``. Tener en cuenta que Python justamente es dinámico, y si el interprete no pasa por la linea de la definición, no se define, por más que este el código en el archivo.

En otros lenguajes, si la variable no esta definida, a veces toma un valor arbitrario (nulo, 0 o cadena vacia) o queda declarada sin inicializar (tomando cualquier valor que esté en la memoria), con los consiguientes errores que esto puede ocasionar. Para prevenir esto, en Python es necesario explicitamente definir ("inicializar") la variable con un valor inicial.

Error de Nombre: el nombre 'variable' no está definido
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">saludo</span><span class="o">=</span><span class="s">&quot;Hola&quot;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">print</span> <span class="n">Saludo</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">NameError</span><span class="p">:</span> <span class="n">name</span> <span class="s">&#39;Saludo&#39;</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">defined</span>
      </span>

Estamos queriendo usar un nombre (identificador) de algo que no existe. En este caso la variable ``Saludo`` no está inicializada, ya que el nombre de variable correcta es ``saludo`` (notar la diferencia de mayúsculas y minúsculas que comentamos en la sección anterior)

Error de Nombre: el nombre global 'variable' no está definido
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">def</span> <span class="nf">mi_func</span><span class="p">():</span>
      </span><span class="line"><span class="o">...</span>     <span class="k">print</span> <span class="n">variable</span>
      </span><span class="line"><span class="o">...</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mi_func</span><span class="p">()</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">2</span><span class="p">,</span> <span class="ow">in</span> <span class="n">mi_func</span>
      </span><span class="line"><span class="ne">NameError</span><span class="p">:</span> <span class="k">global</span> <span class="n">name</span> <span class="s">&#39;variable&#39;</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">defined</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span>
      </span>

Similar al anterior, estamos queriendo usar una variable que no definimos previamente (ahora dentro de una función). O definimos la variable globalmente (fuera de la función), o localmente (dentro de la función).

Error de no vinculación local: la variable local 'xxx' fue referenciada antes de asignarla
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">variable</span> <span class="o">=</span> <span class="mi">1</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">def</span> <span class="nf">mi_func</span><span class="p">():</span>
      </span><span class="line"><span class="o">...</span>     <span class="k">print</span> <span class="n">variable</span>
      </span><span class="line"><span class="o">...</span>     <span class="n">variable</span> <span class="o">=</span> <span class="n">variable</span> <span class="o">+</span> <span class="mi">1</span>
      </span><span class="line"><span class="o">...</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mi_func</span><span class="p">()</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">2</span><span class="p">,</span> <span class="ow">in</span> <span class="n">mi_func</span>
      </span><span class="line"><span class="ne">UnboundLocalError</span><span class="p">:</span> <span class="n">local</span> <span class="n">variable</span> <span class="s">&#39;variable&#39;</span> <span class="n">referenced</span> <span class="n">before</span> <span class="n">assignment</span>
      </span>

Una variación del anterior, pero en este caso, debemos usar la sentencia ``global variable`` dentro de la función, ya que, sinó, al asignarle un valor dentro de la función, se convierte automáticamente en una variable local, por más que exista globalmente (y da error si la asignación no está al principio de la función antes de usar la variable):

::

   .. raw:: html
      <span class="line"><span class="n">variable</span> <span class="o">=</span> <span class="mi">1</span>
      </span><span class="line"><span class="k">def</span> <span class="nf">mi_func</span><span class="p">():</span>
      </span><span class="line">    <span class="k">global</span> <span class="n">variable</span>
      </span><span class="line">    <span class="k">print</span> <span class="n">variable</span>
      </span><span class="line">    <span class="n">variable</span> <span class="o">=</span> <span class="n">variable</span> <span class="o">+</span> <span class="mi">1</span>
      </span>

Errores de Tipos (TypeError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *"12. Cuando te enfrentes a la ambigüedad, rechaza la tentación de adivinar."* PythonZen_

Si si, Python es fuertemente tipado, en general no hará mágia con nuestros datos para convertirlos de un tipo a otro, si no se lo pedimos explícitamente.

No como en otros lenguajes, que cambiarían el tipo de una variable silenciosamente dependiendo del contexto (que puede ser ambiguo, por ej. ¿convertir a ``float`` o ``int``?) con el consiguiente arrastre de un error difícil de solucionar.

Error de Tipo: tipo de operando no soportado para +: 'int' y 'str'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">a</span> <span class="o">=</span> <span class="mi">5</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">b</span> <span class="o">=</span> <span class="s">&quot;10&quot;</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">a</span><span class="o">+</span><span class="n">b</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="n">unsupported</span> <span class="n">operand</span> <span class="nb">type</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="o">+</span><span class="p">:</span> <span class="s">&#39;int&#39;</span> <span class="ow">and</span> <span class="s">&#39;str&#39;</span>
      </span>

Típico, en algunos lenguajes esto puede resultar "510" o 15 (dependiendo como entienda el contexto, el órden de los operandos, etc.) ya que hacen una conversión de tipos implícita.

En Python, gentilmente nos avisa que, explicitamente debemos convertir el número a cadena (``str(a)+b`` que resulta en "510") o la cadena en número (``a+int(b) que resulta en 15``.

Error de Tipo: se requiere un entero
::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">fecha</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">(</span><span class="s">&#39;2010&#39;</span><span class="p">,</span><span class="s">&#39;05&#39;</span><span class="p">,</span><span class="s">&#39;10&#39;</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="n">an</span> <span class="n">integer</span> <span class="ow">is</span> <span class="n">required</span>
      </span>

Algunas funciones validan los parámetros de entrada, en este caso ``datetime.date`` solicita enteros.  Sería ``datetime.date(int('2010'),int('05'),int('10'))``

Error de Tipo: el objeto 'NoneType' no es iterable
::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">secuencia</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">secuencia</span><span class="p">:</span>
      </span><span class="line"><span class="o">...</span>     <span class="k">pass</span>
      </span><span class="line"><span class="o">...</span>    
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="s">&#39;NoneType&#39;</span> <span class="nb">object</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">iterable</span>
      </span>

Para iterar (recorrer uno a uno los elementos de una secuencia o colección), por ej. en un ``for``, es necesario que esta sea realmente una secuencia o iterable (tuplas, listas, diccionario, conjunto, etc.)  

Funciones
~~~~~~~~~

Podemos tener errores de tipo o de sintaxis respecto a las funciones, por ejemplo:

Error de Tipo: objeto 'int' no es llamable
::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">a</span><span class="o">=</span><span class="mi">1</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">a</span> <span class="p">(</span><span class="mi">1</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="s">&#39;int&#39;</span> <span class="nb">object</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">callable</span>
      </span>

Estamos queriendo llamar a una variable que tiene un entero, cosa que no se puede (no es una "función llamable"). Seguramente, o la variable no debería haber sido un entero, o en vez de llamarla deberíamos aplicar algún operador o método sobre ella.

Error de Tipo: función() toma al menos un argumento (0 dados)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mayor</span><span class="p">()</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="n">mayor</span><span class="p">()</span> <span class="n">takes</span> <span class="n">at</span> <span class="n">least</span> <span class="mi">1</span> <span class="n">argument</span> <span class="p">(</span><span class="mi">0</span> <span class="n">given</span><span class="p">)</span>
      </span>

Al definir la función, dijimos que tenía dos parámetros (``param1`` y ``param2=0``). Salvo que el parámetro tenga un valor por defecto (en el caso de param2 es 0), debemos pasarlo al llamar a la función. Revisar...

Error de Tipo: función() toma como mucho 2 argumentos (3 dados)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mayor</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="n">mayor</span><span class="p">()</span> <span class="n">takes</span> <span class="n">at</span> <span class="n">most</span> <span class="mi">2</span> <span class="n">arguments</span> <span class="p">(</span><span class="mi">3</span> <span class="n">given</span><span class="p">)</span>
      </span>

Similar al anterior, pero le pasamos más parámetros de los que necesita la función.  Revisar...

Error de Tipo: función() tuvo un argumento por nombre inesperado 'paramx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mayor</span><span class="p">(</span><span class="n">param3</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">TypeError</span><span class="p">:</span> <span class="n">mayor</span><span class="p">()</span> <span class="n">got</span> <span class="n">an</span> <span class="n">unexpected</span> <span class="n">keyword</span> <span class="n">argument</span> <span class="s">&#39;param3&#39;</span>
      </span>

Idem al anterior, tratamos de pasarle un parámetro (esta vez por nombre), que tampoco esta definido en la misma. Revisar....

Error de Sintáxis: argumento por posición luego de argumento por nombre
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">mayor</span><span class="p">(</span><span class="n">param2</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span>
      </span><span class="line"><span class="ne">SyntaxError</span><span class="p">:</span> <span class="n">non</span><span class="o">-</span><span class="n">keyword</span> <span class="n">arg</span> <span class="n">after</span> <span class="n">keyword</span> <span class="n">arg</span> <span class="p">(</span><span class="o">&lt;</span><span class="nb">input</span><span class="o">&gt;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">)</span>
      </span>

Los parámetros por posición se pasan antes que los parámetros por nombre: ``mayor(3,param2=5)``

Errores de Valores (ValueError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

De manera similar a los errores de tipos, cuando pasemos un dato que no se puede convertir o es inválido, Python nos mostrará estos mensajes:

Error de Valor: literal inválido para int() con base 10: 'xxxx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">int</span><span class="p">(</span><span class="s">&quot;10ab&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">literal</span> <span class="k">for</span> <span class="nb">int</span><span class="p">()</span> <span class="k">with</span> <span class="n">base</span> <span class="mi">10</span><span class="p">:</span> <span class="s">&#39;10ab&#39;</span>
      </span>

En este caso '10ab', salvo que las letras sean un error te escritura, estamos intentando convertir un valor hexadecimal (base 16) a entero, sin especificarlo, por lo que intenta base 10 por defecto. Lo correcto sería ``int("10ab",16)``

Igualmente siempre es conveniente capturar este tipo de errores, para validar que el dato a convertir es realmente un número, y sinó, tomar una medida adecuada.

Error de Valor: literal inválido para float() con base 10: 'xxxx'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">float</span><span class="p">(</span><span class="s">&quot;10,50&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">invalid</span> <span class="n">literal</span> <span class="k">for</span> <span class="nb">float</span><span class="p">():</span> <span class="mi">10</span><span class="p">,</span><span class="mi">50</span>
      </span>

Lo mismo que el anterior, pero con la salvedad que para python debemos indicar los decimales con el punto (.) y no la coma (,). Podríamos convertirlo facilmente: ``float("10,50".replace(",",".")``

Error de Valor: el día esta fuera de rango para el mes
::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">fecha</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">2010</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">day</span> <span class="ow">is</span> <span class="n">out</span> <span class="n">of</span> <span class="nb">range</span> <span class="k">for</span> <span class="n">month</span>
      </span>

Estamos intentando pasar un valor a la función en el parámetro que no corresponde: ``datetime.date(año, mes, día)`` Sería ``fecha = datetime.date(2010,5,10)``

Error de Valor: demasiados valores para desempaquetar
:::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">,</span><span class="n">c</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">too</span> <span class="n">many</span> <span class="n">values</span> <span class="n">to</span> <span class="n">unpack</span>
      </span>

En Python, podemos asignar varios elementos a una lista de destinos, pero la cantidad de destinos y de elementos a asignar deben coincidir.  En este caso, ``a=1``, ``b=2``, ``c=3`` y al cuarto elemento ya no hay a que asignarlo.  Podríamos agregar un destino más: ``a,b,c,d = (1,2,3,4)`` o sacar un elemento a asignar de la expresión: ``a,b,c = (1,2,3)``.

Error de Valor: necesita más de 2 valores para desempaquetar
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="n">z</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">need</span> <span class="n">more</span> <span class="n">than</span> <span class="mi">2</span> <span class="n">values</span> <span class="n">to</span> <span class="n">unpack</span>
      </span>

Caso inverso al anterior, nos falta un elemento en la expresión de asignación (o nos sobra un destino). Posible solución: sacamos un destino ``x,y = 1, 2`` o agregamos un elemento: ``x,y,< = 1, 2 ,3``

Error de Valor: caracter de escape \x inválido
::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;C:\xaraza.txt&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">invalid</span> \<span class="n">x</span> <span class="n">escape</span>
      </span>

En los strings (cadenas), ciertos caracteres tienen un significado especial. Es el caso de la barra invertida ("\"), que identifica que lo que sigue definie un caractér especial ("\n" para el salto de linea, "\xfe" para el caracter cuyo código hexadecimal es FE, etc.) Si queremos una barra invertida (por ejemplo, en un directorio de windows), debemos usar strings crudos (raws): r"C:\xaraza.txt" o doble barra invertida: "C:\\xaraza.txt"

Errores de Atributos (AttributeError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Practicamente todo en Python es un objeto, y estos objetos tienen métodos y "propiedades" (ambos denominados atributos). Si intentamos acceder a un atributo que no pertenece al objeto, se producirá uno de los siguientes errores:

Error de Atributo: el objeto 'NoneType' no tiene el atributo 'split'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">fecha</span> <span class="o">=</span> <span class="bp">None</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">fecha</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;/&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">AttributeError</span><span class="p">:</span> <span class="s">&#39;NoneType&#39;</span> <span class="nb">object</span> <span class="n">has</span> <span class="n">no</span> <span class="n">attribute</span> <span class="s">&#39;split&#39;</span>
      </span>

En este caso estamos queriendo invocar a un método ``split`` que no esta definido para este tipo de objeto (aquí ``None``, pero podría ser cualquier otro). Seguramente la variable fecha debería ser otra cosa, o nos equivocamos de método a invocar.

Error de Atributo: el objeto 'modulo' no tiene el atributo 'next'
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="kn">import</span> <span class="nn">csv</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">csv</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">AttributeError</span><span class="p">:</span> <span class="s">&#39;module&#39;</span> <span class="nb">object</span> <span class="n">has</span> <span class="n">no</span> <span class="n">attribute</span> <span class="s">&#39;next&#39;</span>
      </span>

Similar al anterior, pero en este caso estamos importando un módulo ``csv`` que no tiene la función ``next``}. En este caso particular, ``next`` es un método de la instancia de ``csv_reader``, no del módulo.

Errores de Índice (IndexError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error de Índice: el índice de lista esta fuera de rango
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">l</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="n">l</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;stdin&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">IndexError</span><span class="p">:</span> <span class="nb">list</span> <span class="n">index</span> <span class="n">out</span> <span class="n">of</span> <span class="nb">range</span>
      </span>

En este caso, la lista tiene 3 elementos, y se acceden desde la posición 0 hasta la 3 (como en C), lo correcto sería ``l[2]`` para el tercer elemento.

Errores de Clave (KeyError)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los diccionarios se acceden por clave asociativa, si la clave no existe, se producirá un error:

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;clave&#39;</span><span class="p">:</span> <span class="s">&#39;valor&#39;</span><span class="p">}</span>
      </span><span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="s">&#39;clave2&#39;</span><span class="p">]</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">KeyError</span><span class="p">:</span> <span class="s">&#39;clave2&#39;</span>
      </span>

En este caso, podríamos acceder al valor de correcto usando ``dict['clave']`` que sí existe, o pedir ``dict.get('clave2')`` que si la clave no existe, devolverá ``None`` y no producirá una excepción.

Otros Errores
~~~~~~~~~~~~~

Los errores del sistema operativo y bibliotecas relacionadas también se expresan como excepciones:

IOError: [Errno 2] No existe el archivo o directorio: 'C:\\saraza'
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;C:\saraza&quot;</span><span class="p">)</span>
      </span><span class="line"><span class="n">Traceback</span> <span class="p">(</span><span class="n">most</span> <span class="n">recent</span> <span class="n">call</span> <span class="n">last</span><span class="p">):</span>
      </span><span class="line">  <span class="n">File</span> <span class="s">&quot;&lt;input&gt;&quot;</span><span class="p">,</span> <span class="n">line</span> <span class="mi">1</span><span class="p">,</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">module</span><span class="o">&gt;</span>
      </span><span class="line"><span class="ne">IOError</span><span class="p">:</span> <span class="p">[</span><span class="n">Errno</span> <span class="mi">2</span><span class="p">]</span> <span class="n">No</span> <span class="n">such</span> <span class="nb">file</span> <span class="ow">or</span> <span class="n">directory</span><span class="p">:</span> <span class="s">&#39;C:</span><span class="se">\\</span><span class="s">saraza&#39;</span>
      </span>

El archivo solicitado no existe, si queremos crearlo deberíamos pasarle un segundo parámetro que lo especifique: ``open("saraza","a")`` o ``open("saraza","w")``

Advertencias
~~~~~~~~~~~~

Como comentabamos, hay Excepciones que no son errores, sino advertencias.  Se usan para avisarnos sobre algún cambio en el lenguaje o código potencialmente incorrecto o perjudicial:

Advertencia de "Deprecación": el módulo md5 esta desaconsejado; use en su lugar haslib
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::

   .. raw:: html
      <span class="line"><span class="o">&gt;&gt;&gt;</span> <span class="kn">import</span> <span class="nn">md5</span>
      </span><span class="line"><span class="n">__main__</span><span class="p">:</span><span class="mi">1</span><span class="p">:</span> <span class="ne">DeprecationWarning</span><span class="p">:</span> <span class="n">the</span> <span class="n">md5</span> <span class="n">module</span> <span class="ow">is</span> <span class="n">deprecated</span><span class="p">;</span> <span class="n">use</span> <span class="n">hashlib</span> <span class="n">instead</span>
      </span>

En esta versión de Python, el módulo md5 existe por compatibilidad hacia atrás.  En versiones posteriores podría no existir más. Se recomienda revisar la recomendación que nos da Python: el módulo hashlib.

.. ############################################################################

.. _PythonZen: ../PythonZen

.. _CamelCase: ../CamelCase

.. _Python3Mil: ../Python3Mil

