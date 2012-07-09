= Proyectos en los que se trabajó durante el Pycamp 2012 =


== Nikola ==

Nikola es un generador de sitios estáticos con esteroides. Se le agregaron varias de las [[http://lateral.netmanagers.com.ar/tr/es/weblog/posts/nikola-ideas-for-pycamp.html|features propuestas]]: pipelines, mejora en las galerias de imágenes, listing de código, temas de bootstrapwatch, etc. 
Trabajaron Roberto Alsina, Hugo Ruscitti, Martín Gaitán

* repo: https://github.com/ralsina/nikola

* post: http://lateral.netmanagers.com.ar/tr/es/weblog/posts/pycamp-day-1.html

== Hazte libro ==

Una libreria que genera epubs a partir de una lista de urls. Trabajaron Gozalo Odiard y Martín Gaitán

* repo: https://github.com/nqnwebs/haztelibro


== Nuevo sitio de Pyar ==

ver ideas en [[NuevoSitio]]. Agreguen las suyas. Contactar con Joac. 


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

== Spacecraft == 

Se mejoró el servidor y se hicieron muchos bots

== Python para Android ==

Lipe estuvo laburando con [[http://kivy.org|Kivy]] un framewrok crossplatform que compila python para android y escritorio. Hicieron "botonera"


== Nikola SaaS ==

Un servicio de blogs en la nube usando flask, celery, github y Nikola. Usando un post hook de nikola, el servicio se entera que se actualizaron los fuentes en gihub y actualiza el blog rende


== Guitarra de verdad usada como MIDI ==

Lucio y otros cumpas laburaron en un programita para detectar/aislar/filtrar notas de una guitarra eléctrica comun para usarla como guitarra para juegos estilo Guitar hero.

== Cdpedia ==

Se estuvo limpiando y laburando 


== OLPC =

http://ar.sugarlabs.org . Se estuvo mostrando e instalando (ahora es muhcos más facil en Ubuntu) el emulador para que se sumen colaboradores. 

== ORM for Json ==

Se agregaron soporte para YAML y puliendo cosas. Se [[http://pypi.python.org/pypi/Ojota|subió a PyPi]]

== Encuentro == 
Un 
Debido a que el contenido pasó al portal [[http://conectate.gov.ar]] se estuvo laburando en hacerlo andar y adapatando la UI a la nueva referencia. Se lanza nueva version en breve. 


== Jugnado con NLTK ==

Pablo celayes estuvo jugando con NLTK 


== Pilas en el navegador == 

Se estudió la la libreria Skulpt para poder utilizar la API de pilas en el navegador y hacerlo andar sobre HTML5. 

== 7 Wonders ==

Se mejoro la UI con bootstraps css . Se cargaron datos (cartas y demás cosas necesarias). Pronto se pushea y se sube par jugar 

== Nija IDE ==

Estudiando la nueva api de PyQT para pythonizar el código (no más Qstrings) 

== Otras actividades ==

- se jugó al futbol
- torneo de pingpong
- taller de malabares (un éxito! descubriendo talentos ocultos en los geeks)
- telescopio

== QML == 

J0hn estuvo mirando QML para armar interfaces "piolas" en un codigo rápido estilo json

== Kinect == 

Se estuvo jugando con el procesamiento de imágenes y el kinect (transparencia, detección de bordes de primer plano, etc) (Joac, Manuq, perrito) y para relevar mapas 3D de un espacio fisco (Lucio)

== generador de certificados SSL ==


== Plugins de lalita ==

Exportar eventos de lalita para usar "plugins" en procesos externos. 
