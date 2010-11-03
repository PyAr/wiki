= Modificación de Estilos en rst2pdf =
''(por '''Roberto Alsina''')''
<<TableOfContents>>

En el [[http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/styles.style|svn de rst2pdf]] se puede ver un archivo de ejemplo, que define todos los atributos posibles.

En '''rst2pdf''' un estilo (este es el estilo que se llama base) puede tener los siguientes atributos:

{{{
#!code yaml
base:
     parent: null
     fontName: stdFont
     fontSize: 10
     leading: 12
     leftIndent: 0
     rightIndent: 0
     firstLineIndent: 0
     alignment: TA_LEFT
     spaceBefore: 0
     spaceAfter: 0
     bulletFontName: stdFont
     bulletFontSize: 10
     bulletIndent: 0
     textColor: black
     backColor: null
     wordWrap: null
     borderWidth: 0
     borderPadding: 0
     borderColor: null
     borderRadius: null
     allowWidows: false
     allowOrphans: false
     hyphenation: false
     kerning: false
     underline: false
     strike: false
     commands: []
}}}

De estos hay que saber:

1) {{{commands}}} es solamente cuando se aplica a tablas, y a cosas que están hechas con tablas, por ejemplo listas.

2) {{{parent}}} es el nombre de otro estilo. Ese estilo se usa para todo lo que vos no definas. Por ejemplo,

{{{
#!code yaml
   bodytext:
     parent: normal
     spaceBefore: 6
     alignment: TA_JUSTIFY
     hyphenation: true
}}}

Quiere decir: este estilo es igualito a "normal" pero... el {{{spaceBefore}}} es 6, va justificado y usa guiones para cortar palabras.

Si vos queres definir un estilo que sea igual a bodytext pero verde:

{{{
#!code yaml
verde:
   parent: bodytext
   textColor: green
}}}

'''NdR:''' si no se le indica {{{parent}}} hereda de {{{base}}}

== Como Utilizarlo en un documento ==
O lo usas como clase para un objeto, por ejemplo para un parrafo:



{{{
#!code rst
.. class:: verde

Este texto es verde
}}}

O definis un rol y lo aplicas a un pedazo de texto:

{{{
#!code rst
.. role:: verde

La ultima palabra es de color :verde:`esmeralda`
}}}

Si queres cambiar como se ve alguna de las cosas que ya estan definidas, pisás el estilo como quieras. Si por ejemplo querés que el estilo "base" en tu documento sea de 8 puntos en vez de diez, te creas una hoja de estilo que tenga esto adentro:

{{{
#!code yaml
styles:
   base:
       fontSize: 8
}}}

( Esa hoja es la que se llama eightpoint y [[http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/eightpoint.style| ya viene con rst2pdf]] )

Como todos los demas estilos heredan de base, cambiando base cambian todos.

Cada estilo definido en la hoja por default se usa en alguna parte de un documento, o es un estilo "práctico" como "right" o "center" para aplicar.

== Enlaces ==
 * [[https://code.google.com/p/rst2pdf/ |Proyecto rst2pdf]]
 * [[http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/styles.style |Hoja de estilo completa]]
 * [[http://code.google.com/p/rst2pdf/source/browse/trunk/rst2pdf/styles/eightpoint.style |Hoja de estilo eightpoint]]
