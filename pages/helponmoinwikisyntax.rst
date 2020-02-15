
This page aims to introduce the most important elements of MoinMoin_'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you'll find links to the relative help pages. Please note that some of the features depend on your configuration.

Table of Contents
=================

::

   '''Contents''' (up to the 2nd level)
   <<TableOfContents(2)>>

**Contents** (up to the 2nd level) .. contents:: :depth: 2

Headings
========

**see:** HelpOnHeadlines_

::

   = heading 1st level =
   == heading 2nd level ==
   === heading 3rd level ===
   ==== heading 4th level ====
   ===== heading 5th level =====

heading 1st level
=================

heading 2nd level
-----------------

heading 3rd level
~~~~~~~~~~~~~~~~~

heading 4th level
:::::::::::::::::

heading 5th level
,,,,,,,,,,,,,,,,,

Text Formatting
===============

**see:** HelpOnFormatting_

::

    * ''emphasized (italics)''
    * '''boldface'''
    * '''''bold italics'''''
    * `monospace`
    * {{{source code}}}
    * __underline__
    * ,,sub,,script
    * ^super^script
    * ~-smaller-~
    * ~+larger+~
    * --(strike through)--

* *emphasized (italics)*

* **boldface**

* **bold italics**

* ``monospace``

* ``source code``

* :underline:`underline`

* :subscript:`sub`script

* :superscript:`super`script

* :small:`smaller`

* :big:`larger`

* :strike:`strike through`

Hyperlinks
==========

**see:** HelpOnLinking_

Internal Links
--------------

::

    * FrontPage
    * [[FrontPage]]
    * HelpOnEditing/SubPages
    * /SubPage
    * ../SiblingPage
    * [[FrontPage|named link]]
    * [[#anchorname]]
    * [[#anchorname|description]]
    * [[PageName#anchorname]]
    * [[PageName#anchorname|description]]
    * [[attachment:filename.txt]]

* FrontPage_

* FrontPage_

* `HelpOnEditing/SubPages`_

* `/SubPage`_

* `../SiblingPage`_

* `named link`_

* `#anchorname`_

* description_

* `PageName#anchorname`_

* `description <../PageName#anchorname>`__

*

External Links
--------------

::

    * http://moinmo.in/
    * [[http://moinmo.in/]]
    * [[http://moinmo.in/|MoinMoin Wiki]]
    * [[http://static.moinmo.in/logos/moinmoin.png]]
    * {{http://static.moinmo.in/logos/moinmoin.png}}
    * [[http://static.moinmo.in/logos/moinmoin.png|moinmoin.png]]
    * MeatBall:InterWiki
    * [[MeatBall:InterWiki|InterWiki page on MeatBall]]
    * [[file://///servername/share/full/path/to/file/filename%20with%20spaces.txt|link to file filename with spaces.txt]]
    * user@example.com

* http://moinmo.in/

* http://moinmo.in/

* `MoinMoin Wiki`_

* http://static.moinmo.in/logos/moinmoin.png

* http://static.moinmo.in/logos/moinmoin.png

* `moinmoin.png`_

* InterWiki_

* `InterWiki page on MeatBall`_

* `link to file filename with spaces.txt`_

* `user@example.com`_

Avoid or Limit Automatic Linking
--------------------------------

::

    * Wiki''''''Name
    * Wiki``Name
    * !WikiName
    * WikiName''''''s
    * WikiName``s
    * `http://www.example.com`
    * [[http://www.example.com/]]notlinked

* WikiName

* WikiName

* WikiName

* WikiName_s

* WikiName_s

* ``http://www.example.com``

* http://www.example.com/notlinked

Drawings
========

  `myexample.tdraw`_

Blockquotes and Indentations
============================

::

    indented text
     text indented to the 2nd level

  indented text

    text indented to the 2nd level

Lists
=====

**see:** HelpOnLists_

Unordered Lists
---------------

::

    * item 1

    * item 2 (preceding white space)
     * item 2.1
      * item 2.1.1
    * item 3
     . item 3.1 (bulletless)
    . item 4 (bulletless)
     * item 4.1
      . item 4.1.1 (bulletless)

* item 1

* item 2 (preceding white space)

  * item 2.1

    * item 2.1.1

* item 3

    item 3.1 (bulletless)

  item 4 (bulletless)

  * item 4.1

      item 4.1.1 (bulletless)

Ordered Lists
-------------

with Numbers
~~~~~~~~~~~~

::

    1. item 1
      1. item 1.1
      1. item 1.2
    1. item 2

1. item 1

   1. item 1.1

   #. item 1.2

#. item 2

with Roman Numbers
~~~~~~~~~~~~~~~~~~

::

    I. item 1
      i. item 1.1
      i. item 1.2
    I. item 2

I. item 1

   i. item 1.1

   #. item 1.2

#. item 2

with Letters
~~~~~~~~~~~~

::

    A. item A
      a. item A. a)
      a. item A. b)
    A. item B

A. item A

   a. item A. a)

   #. item A. b)

#. item B

Definition Lists
----------------

::

    term:: definition
    object::
    :: description 1
    :: description 2

term  definition

object
  description 1

  description 2

Horizontal Rules
================

**see:** HelpOnRules_

::

   ----
   -----
   ------
   -------
   --------
   ---------
   ----------

-------------------------



-------------------------



-------------------------



-------------------------



-------------------------



-------------------------



-------------------------



Tables
======

**see:** HelpOnTables_

Tables
------

::

   ||'''A'''||'''B'''||'''C'''||
   ||1      ||2      ||3      ||

[Table not converted]

Cell Width
----------

::

   ||minimal width ||<99%>maximal width ||

[Table not converted]

Spanning Rows and Columns
-------------------------

::

   ||<|2> cell spanning 2 rows ||cell in the 2nd column ||
   ||cell in the 2nd column of the 2nd row ||
   ||<-2> cell spanning 2 columns ||
   ||||use empty cells as a shorthand ||

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

Alignment of Cell Contents
--------------------------

::

   ||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||
   ||<)> right ||
   ||<(> left ||

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

Coloured Table Cells
--------------------

::

   ||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||
   ||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

HTML-like Options for Tables
----------------------------

::

   ||A ||<rowspan="2"> like <|2> ||
   ||<bgcolor="#00FF00"> like <#00FF00> ||
   ||<colspan="2"> like <-2>||

[Table not converted]

Macros and Variables
====================

Macros
------

**see:** HelpOnMacros_

* .. _anchorname:

   ``<<Anchor(anchorname)>>`` inserts a link anchor ``anchorname``

* ``<<BR>>`` inserts a hard line break

* ``<<FootNote(Note)>>`` inserts a footnote saying ``Note``

* ``<<Include(HelpOnMacros/Include)>>`` inserts the contents of the page ``HelpOnMacros/Include`` inline

* ``<<MailTo(user AT example DOT com)>>`` obfuscates the email address ``user@example.com`` to users not logged in

Variables
---------

**see:** HelpOnVariables_

* ``@````SIG````@`` inserts your login name and timestamp of modification

* ``@````TIME````@`` inserts date and time of modification

Smileys and Icons
=================

**see:** HelpOnSmileys_ `[[ShowSmileys]]`_

Parsers
=======

**see:** HelpOnParsers_

Verbatim Display
----------------

::

   {{{
   def hello():
       print "Hello World!"
   }}}

::

   def hello():
       print "Hello World!"

Syntax Highlighting
-------------------

::

   {{{#!code python
   def hello():
       print "Hello World!"
   }}}

::

   def hello():
       print "Hello World!"

Using the wiki parser with css classes
--------------------------------------

::

   {{{#!wiki red/solid
   This is wiki markup in a '''div''' with __css__ `class="red solid"`.
   }}}

This is wiki markup in a **div** with :underline:`css` ``class="red solid"``.

Admonitions
===========

**see:** HelpOnAdmonitions_

::

   {{{#!wiki caution
   '''Don't overuse admonitions'''

   Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.
   }}}

**Don't overuse admonitions**

Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.

Comments
========

**see:** HelpOnComments_

::

   Click on "Comments" in edit bar to toggle the /* comments */ visibility.

Click on "Comments" in edit bar to toggle the comments visibility.

::

   {{{#!wiki comment/dotted
   This is a wiki parser section with class "comment dotted" (see HelpOnParsers).

   Its visibility gets toggled the same way.
   }}}

This is a wiki parser section with class "comment dotted" (see HelpOnParsers_).

Its visibility gets toggled the same way.

.. ############################################################################





.. _FrontPage:


.. _#anchorname:
.. _description: HelpOnMoinWikiSyntax#anchorname


.. _MoinMoin Wiki: http://moinmo.in/

.. _moinmoin.png: http://static.moinmo.in/logos/moinmoin.png

.. _InterWiki:

.. _link to file filename with spaces.txt: file://///servername/share/full/path/to/file/filename%20with%20spaces.txt

.. _user@example.com: mailto:user@example.com


.. _myexample.tdraw: drawing:myexample.tdraw












.. role:: underline
   :class: underline



.. role:: subscript
   :class: subscript



.. role:: superscript
   :class: superscript



.. role:: small
   :class: small



.. role:: big
   :class: big



.. role:: underline
   :class: underline

