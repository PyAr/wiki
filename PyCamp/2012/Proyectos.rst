= Proyectos en los que se trabajó durante el Pycamp 2012 =


== Nikola ==

Nikola es un generador de sitios estáticos con esteroides. Se le agregaron varias de las [[http://lateral.netmanagers.com.ar/tr/es/weblog/posts/nikola-ideas-for-pycamp.html|features propuestas]]: pipelines, mejora en las galerias de imágenes, listing de código, etc. 
Trabajaron Roberto Alsina, Hugo Ruscitti, Martín Gaitán

* repo: https://github.com/ralsina/nikola

* post: http://lateral.netmanagers.com.ar/tr/es/weblog/posts/pycamp-day-1.html

== Hazte libro ==

Una libreria que genera epubs a partir de una lista de urls. Trabajaron Gozalo Odiard y Martín Gaitán

* repo: https://github.com/nqnwebs/haztelibro


== Nuevo sitio de Pyar ==

ver ideas en [[NuevoSitio]]. 


== lai ==

Se agregaron algunas mejoras a la [[https://github.com/lvidarte/lai|versión original]] y empezó con la [[https://github.com/lvidarte/lai-u1db|versión con u1db]]. En ambas queda resolver el caso en que debe hacerce un merge.


== vim ==

- Usar el modo de edición de vim desde la línea de comandos (funciona en la consola de python):

{{{
    set -o vi # bash
    bindkey -v # zsh
}}}

  Agregarlo al .bashrc o .zshrc respec.
  También se puede setear creando un .inputrc (en bash)

{{{
    set editing-mode vi
    set keymap vi
}}}

   Hay muchas más opciones que se pueden setear (man 3 readline).
  
   Lista de comandos: [[http://www.catonmat.net/download/bash-vi-editing-mode-cheat-sheet.pdf|Bash vi editing mode cheat sheet]]
