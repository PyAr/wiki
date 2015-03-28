#format rst

Modificación de Estilos en rst2pdf
==================================

*(por* **Roberto Alsina***)* .. contents::

En el `svn de rst2pdf`_ se puede ver un archivo de ejemplo, que define todos los atributos posibles.

En **rst2pdf** un estilo (este es el estilo que se llama base) puede tener los siguientes atributos:

::

   .. raw:: html
      <span class="line"><span class="l-Scalar-Plain">base</span><span class="p-Indicator">:</span>
      </span><span class="line">     <span class="l-Scalar-Plain">parent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">null</span>
      </span><span class="line">     <span class="l-Scalar-Plain">fontName</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">stdFont</span>
      </span><span class="line">     <span class="l-Scalar-Plain">fontSize</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">10</span>
      </span><span class="line">     <span class="l-Scalar-Plain">leading</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">12</span>
      </span><span class="line">     <span class="l-Scalar-Plain">leftIndent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">rightIndent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">firstLineIndent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">alignment</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">TA_LEFT</span>
      </span><span class="line">     <span class="l-Scalar-Plain">spaceBefore</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">spaceAfter</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">bulletFontName</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">stdFont</span>
      </span><span class="line">     <span class="l-Scalar-Plain">bulletFontSize</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">10</span>
      </span><span class="line">     <span class="l-Scalar-Plain">bulletIndent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">textColor</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">black</span>
      </span><span class="line">     <span class="l-Scalar-Plain">backColor</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">null</span>
      </span><span class="line">     <span class="l-Scalar-Plain">wordWrap</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">null</span>
      </span><span class="line">     <span class="l-Scalar-Plain">borderWidth</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">borderPadding</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0</span>
      </span><span class="line">     <span class="l-Scalar-Plain">borderColor</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">null</span>
      </span><span class="line">     <span class="l-Scalar-Plain">borderRadius</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">null</span>
      </span><span class="line">     <span class="l-Scalar-Plain">allowWidows</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">allowOrphans</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">hyphenation</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">kerning</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">underline</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">strike</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">false</span>
      </span><span class="line">     <span class="l-Scalar-Plain">commands</span><span class="p-Indicator">:</span> <span class="p-Indicator">[]</span>
      </span>

De estos hay que saber:

1) ``commands`` es solamente cuando se aplica a tablas, y a cosas que están hechas con tablas, por ejemplo listas.

2) ``parent`` es el nombre de otro estilo. Ese estilo se usa para todo lo que vos no definas. Por ejemplo,

::

   .. raw:: html
      <span class="line">   <span class="l-Scalar-Plain">bodytext</span><span class="p-Indicator">:</span>
      </span><span class="line">     <span class="l-Scalar-Plain">parent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">normal</span>
      </span><span class="line">     <span class="l-Scalar-Plain">spaceBefore</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">6</span>
      </span><span class="line">     <span class="l-Scalar-Plain">alignment</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">TA_JUSTIFY</span>
      </span><span class="line">     <span class="l-Scalar-Plain">hyphenation</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">true</span>
      </span>

Quiere decir: este estilo es igualito a "normal" pero... el ``spaceBefore`` es 6, va justificado y usa guiones para cortar palabras.

Si vos queres definir un estilo que sea igual a bodytext pero verde:

::

   .. raw:: html
      <span class="line"><span class="l-Scalar-Plain">verde</span><span class="p-Indicator">:</span>
      </span><span class="line">   <span class="l-Scalar-Plain">parent</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">bodytext</span>
      </span><span class="line">   <span class="l-Scalar-Plain">textColor</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">green</span>
      </span>

**NdR:** si no se le indica ``parent`` hereda de ``base``

Como Utilizarlo en un documento
-------------------------------

O lo usas como clase para un objeto, por ejemplo para un parrafo:

::

   .. raw:: html
      <span class="line"><span class="p">..</span> <span class="ow">class</span><span class="p">::</span> <span class="k">verde</span>
      </span><span class="line">
      </span><span class="line">Este texto es verde
      </span>

O definis un rol y lo aplicas a un pedazo de texto:

::

   .. raw:: html
      <span class="line"><span class="p">..</span> <span class="ow">role</span><span class="p">::</span> <span class="k">verde</span>
      </span><span class="line">
      </span><span class="line">La ultima palabra es de color <span class="na">:verde:</span><span class="nv">`esmeralda`</span>
      </span>

Si queres cambiar como se ve alguna de las cosas que ya estan definidas, pisás el estilo como quieras. Si por ejemplo querés que el estilo "base" en tu documento sea de 8 puntos en vez de diez, te creas una hoja de estilo que tenga esto adentro:

::

   .. raw:: html
      <span class="line"><span class="l-Scalar-Plain">styles</span><span class="p-Indicator">:</span>
      </span><span class="line">   <span class="l-Scalar-Plain">base</span><span class="p-Indicator">:</span>
      </span><span class="line">       <span class="l-Scalar-Plain">fontSize</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">8</span>
      </span>

( Esa hoja es la que se llama eightpoint y `ya viene con rst2pdf`_ )

Como todos los demas estilos heredan de base, cambiando base cambian todos.

Cada estilo definido en la hoja por default se usa en alguna parte de un documento, o es un estilo "práctico" como "right" o "center" para aplicar.

Enlaces
-------

* `Proyecto rst2pdf`_

* `Hoja de estilo completa`_

* `Hoja de estilo eightpoint`_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _svn de rst2pdf:
.. _Hoja de estilo completa: http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/styles.style

.. _ya viene con rst2pdf:
.. _Hoja de estilo eightpoint: http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/eightpoint.style

.. _Proyecto rst2pdf: https://code.google.com/p/rst2pdf/

