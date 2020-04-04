.. title: AaFigure Parser


.. todo:: Sacar esto de moin-moin y poner lo que corresponda

Uso
~~~

El nombre del parser es {{{aafig}}}  y las opciones se agregan separadas por espacios.
Las opciones que requieren valores los toman luego del {{{=}]] sin ningún espacio entre la opción y el valor.

 * ``scale=<float>``
 * ``aspect=<float>``
 * ``textual``
 * ``proportional``
 * ``linewidth=<float>``
 * ``foreground=#rrggbb``
 * ``fill=#rrggbb``

Las imagenes se generan y son almacenadas en el cache interno de MoinMoin. No hay confusión con los archivos adjuntos en la página. Cada cambio en la imagen genera una nueva entrada en el cache, por lo que este puede creer con el tiempo. Sin embargo los archivos pueden ser borrados sin ningun problema, ya que son regenerados cuando la pagina es vista nuevamente. (los viejos archivos no son borrados automaticamente porque se utilizan cuando se muestran las anteriores revisiones de la página).

Ejemplos
~~~~~~~~

Las figuras de ASCII Art se pueden insertar en una pagina WikiText de la siguiente manera:


::

    {{{{
        {{{#!aafig scale=1.5 foreground=#ff1010
        DD --->
        }}}
    }}}}

Aspecto
~~~~~~~


::

    {{{{
        {{{#!aafig aspect=0.5 textual
        +---+    DDDD
        |   +--->DDDD
        +---+    DDDD
        }}}
    }}}}
    {{{#!aafig aspect=0.5 textual
    +---+    DDDD
    |   +--->DDDD
    +---+    DDDD
    }}}

Lineas y Flechas
~~~~~~~~~~~~~~~~

::

    {{{{
    {{{#!aafig
    ---- |         ___  ~~~|
        | --  ___|        |    ===
                            ~~~

                                        +
        |  -  +   |  -  +   |  -  +   /               -
        /  /  /   /  /  /   /  /  /   /     --     |/| /    +
        |  |  |   +  +  +   -  -  -   /     /  \        -   \|/  |\
                                    +     +    +          +-+-+ | +
        |  |  |   +  +  +   -  -  -   \     \  /        -   /|\  |/
        \  \  \   \  \  \   \  \  \   \     --     |\| \    +
        |  -  +   |  -  +   |  -  +   \               -
                                        +

        --->   | | | | | |
        ---<   | | | | | |
        ---o   ^ V v o O #
        ---O
        ---#
    }}}
    }}}}
    {{{#!aafig
    ---- |         ___  ~~~|
        | --  ___|        |    ===
                            ~~~

                                        +
        |  -  +   |  -  +   |  -  +   /               -
        /  /  /   /  /  /   /  /  /   /     --     |/| /    +
        |  |  |   +  +  +   -  -  -   /     /  \        -   \|/  |\
                                    +     +    +          +-+-+ | +
        |  |  |   +  +  +   -  -  -   \     \  /        -   /|\  |/
        \  \  \   \  \  \   \  \  \   \     --     |\| \    +
        |  -  +   |  -  +   |  -  +   \               -
                                        +

        --->   | | | | | |
        ---<   | | | | | |
        ---o   ^ V v o O #
        ---O
        ---#
    }}}

Rellenos
~~~~~~~~

::

    {{{{
    {{{#!aafig aspect=1
        A   B   C   D   E   F   G   H   I   J   K   L   M
        AA  BB  CC  DD  EE  FF  GG  HH  II  JJ  KK  LL  MM
        AA  BB  CC  DD  EE  FF  GG  HH  II  JJ  KK  LL  MM

        aa  bb  cc  dd  ee  ff  gg  hh  ii  jj  kk  ll  mm
        aa  bb  cc  dd  ee  ff  gg  hh  ii  jj  kk  ll  mm

        N   O   P   Q   R   S   T   U   V   W   X   Y   Z
        NN  OO  PP  QQ  RR  SS  TT  UU  VV  WW  XX  YY  ZZ
        NN  OO  PP  QQ  RR  SS  TT  UU  VV  WW  XX  YY  ZZ

        nn  oo  pp  qq  rr  ss  tt  uu  vv  ww  xx  yy  zz
        nn  oo  pp  qq  rr  ss  tt  uu  vv  ww  xx  yy  zz
    }}}
    }}}}
    {{{#!aafig aspect=1
        A   B   C   D   E   F   G   H   I   J   K   L   M
        AA  BB  CC  DD  EE  FF  GG  HH  II  JJ  KK  LL  MM
        AA  BB  CC  DD  EE  FF  GG  HH  II  JJ  KK  LL  MM

        aa  bb  cc  dd  ee  ff  gg  hh  ii  jj  kk  ll  mm
        aa  bb  cc  dd  ee  ff  gg  hh  ii  jj  kk  ll  mm

        N   O   P   Q   R   S   T   U   V   W   X   Y   Z
        NN  OO  PP  QQ  RR  SS  TT  UU  VV  WW  XX  YY  ZZ
        NN  OO  PP  QQ  RR  SS  TT  UU  VV  WW  XX  YY  ZZ

        nn  oo  pp  qq  rr  ss  tt  uu  vv  ww  xx  yy  zz
        nn  oo  pp  qq  rr  ss  tt  uu  vv  ww  xx  yy  zz
    }}}
