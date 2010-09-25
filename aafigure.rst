## page was renamed from AaFigure
<<TableOfContents>>
= AaFigure Parser =

== Description ==
The aafigure project aims to convert ASCII art figures to images such as SVG, PNG, JPEG, PDF and more.

== Download & Release Notes ==
|| Download || Release Version || Moin Version || Release Notes ||
|| [[http://bazaar.launchpad.net/~aafigure-team/aafigure/trunk/annotate/98/examples/moinmoin/aafig.py|aafig.py]] || 0.3 || 1.8 || -- ||

The link above points to a certain revision of the file. It's also possible to get the bleeding edge version here: [[http://bazaar.launchpad.net/~aafigure-team/aafigure/trunk/annotate/head%3A/examples/moinmoin/aafig.py|aafig.py]]

== Installation ==
For general installation instructions, see [[ParserMarket/InstallingParsers]]. This parser requires the [[https://launchpad.net/aafigure|aafigure]] package. It can be downloaded from [[http://pypi.python.org/pypi/aafigure|PyPi]]

== Usage ==
The parser name is {{{aafig}}} and options are appended, separated with spaces.
Options that require a value take that after a {{{=}}} without any whitespace
between option and value.  Supported options are:

 * ``scale=<float>``
 * ``aspect=<float>``
 * ``textual``
 * ``proportional``
 * ``linewidth=<float>``
 * ``foreground=#rrggbb``
 * ``fill=#rrggbb``

There is no ``background`` as the SVG backend ignores that. And it is not possible
to pass generic options.

The images are generated and stored in MoinMoin's internal cache. So there is
no mess with attached files on the page. Each change on an image generates a
new cache entry so the cache may grow over time. However the files can be
deleted with no problem as they can be rebuilt when the page is viewed again
(the old files are not automatically deleted as they are still used when older
revision of a page is displayed).

== Example ==
ASCII Art figures can be inserted into a Moin WikiText page the following way::

{{{{
    {{{#!aafig scale=1.5 foreground=#ff1010
    DD --->
    }}}
}}}}

The following examples will be shown as text when the plugin is not installed and as image when it is installed.

Aspect
{{{#!aafig aspect=0.5 textual
 +---+    DDDD
 |   +--->DDDD
 +---+    DDDD
}}}

Lines and Arrows
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

Fills
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

== Copyright ==
(C) 2009 Chris Liechti

== License ==
This parser is released under the terms of the simplified BSD license.

= Discussion =
