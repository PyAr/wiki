== Temas propuestos para el PyCamp 2013 ==

Estas son propuestas, en el PyCamp el primer día se hace una votación para elegir a cuáles de estos proyectos o ideas vamos a dedicar tiempo (este procedimiento lo tenemos que terminar de definir).

=== SimpleAI ===

[[http://github.com/simpleai-team/simpleai|SimpleAI]] es una biblioteca bien ordenada y documentada para hacer inteligencia artificial con python, que implementa cosas del libro "Artificial Intelligence: a Modern Approach" (AIMA). Podríamos implementar algunas cosas que faltan, agregar más ejemplos educativos, o simplemente jugar con ideas locas :) Yo no tendría drama en dar una mini-charla introductoria, o hangout antes (fisa) 

''Propone: fisa''

=== Mejorar integración Vim+Python ===

vim permite escribir plugins en python, pero el sistema que tiene para hacerlo casi que da pena. Podríamos intentar crear algo mejor, construído por sobre lo que vim da 

''Propone: fisa''

=== NINJA-IDE ===

Trabajar en poder acercar mas a nuevos desarrolladores al codigo de ninja (http://ninja-ide.org) para crecer la comunidad de desarrolladores en Argentina (donde nacio este proyecto), y buscar de arreglar bugs, desarrollar alguna que otra feature y tirar ideas entre los presentes de cual podria ser el futuro de ninja y las features claves a tratar.

''Propone: Diego Sarmentero''

=== Documentor ===

Programa para generar un sitio de documentacion de un proyecto analizando la estructura de los archivos, docstrings, etc. Utilizando ast y nikola. 

''Propone: Diego Sarmentero''


=== Torneo Spacecraft ===

Al igual que el año pasado, unas peleitas de spacecraft no estaria nada mal (https://github.com/luciotorre/spacecraft) y podriamos hacer un evento especial de navecitas controladas por emotiv contra navecitas controladas por kinect.

''Propone: Lucio Torre''


=== TOMy ===

[[http://abuelodelanada.github.io/TOMy/|TOMy]] es un cliente de MySQL (Ahora también PostgreSQL... ponele) de consola que espero, algún día tenga más y mejores funcionalidades que el cliente oficial, el cual es un poco limitado. El desarrollo está recién iniciado y me quedan muchísimas cosas por implementar y mejorar. Entre ellas: Coloreado de sintaxis (se podrá?), soporte de SSL, autocompletado usando [[http://www.taniquetil.com.ar/plog/post/1/598|árboles]] (servirá para este caso?), etc

Seguramente surgirán muchas más cosas por hacer, pero en principio, las más importantes son:

 * Armar virtualenv
 * Repensar la estructura del proyecto. ¿Servirá usar una similar a la que [[http://www.taniquetil.com.ar/plog/post/1/610 |usa Facundo en Encuentro]]?
 * Refactorizar método connect (no me gusta ni un poco como está)
 * La conexión no se reconecta automaticamente
 * Agregar tiempo de ejecución de consultas
 * Armar tests unitarios
 * Y varias cosas más que anoté en: https://github.com/Abuelodelanada/TOMy/issues?state=open


''Propone: José Massón''


=== GalaxyTrucker ===

Existe un juego de tablero llamado [[https://en.wikipedia.org/wiki/Galaxy_Trucker|Galaxy Trucker]] que está muy muy bueno. Quiero ver de armar alguna versión equivalente en digital. La dinámica se puede resumir en: 1. Armás tu nave (con restricciones como tiempo limitado, cantidad máxima de partes, etc), 2. Sometés la nave a un stress-test estructural (se puede romper si no es suficientemente robusta), 3. Mandás la nave a misiones (en función del azar pueden pasar varias cosas, como recolectar dinero, o que se rompa la nave, por ejemplo), 4. Se obtiene un puntaje. Goto 1. 

''Propone: Ricardo Kirkner''

=== Kilink, el pastebin útil ===

La idea es ofrecer un "espacio de colaboración de corta vida".  Algo así como un pastebin dinámico, pero que al mismo tiempo sea fácil de usar. En definitiva, algo útil.  Los kilinks van a poder ser editables, y cada nueva edición será hija del kilink editado.  Habrá tener coloreado de código, como todos los pastebines, pero con dos grandes diferencias: detección y coloreado automático de tipo de texto, y edición coloreada. 

¿Por qué usar kilink?

 * Se puede usar anonimamente...
 * ...pero recuerda quien sos
 * Permite compartir un texto en pocos clicks
 * Se da cuenta del lenguaje
 * Es amigable a nivel de interfaz
 * Copia el texto directamente a tu clipboard
 * Se puede integrar el texto en donde quieras, por versión o siempre actualizado!

Más info en [[http://www.taniquetil.com.ar/plog/post/1/608|este post]]. 

''Propone: FacundoBatista''

=== LocoLander ===

La idea es tener un bot que automáticamente commitee a trunk un branch de cualquier proyecto que esté suscripto al servicio.

Lo que haría este bot es revisar cada tanto los proyectos registrados, y si encuentra branches listos para commitear, levantaría el entorno que corresponda (customizado para cada proyecto), mergearía ese branch con trunk, correría tests, etc, y si está todo bien, lo ''landearía''.

Más info en [[http://www.taniquetil.com.ar/plog/post/1/606|este post]].

''Propone: FacundoBatista''

=== CDPedia ===

La [[http://python.org.ar/pyar/Proyectos/CDPedia|CDPedia]] es un proyecto de Python Argentina que permite acceder a la información de la Wikipedia en castellano sin necesidad de una conexión a Internet. Se puede descargar libremente de la red y grabar a CDs, DVDs o memorias USB para repartirlos sin restricciones. La CDPedia funciona en cualquier computadora, ya sea que tenga Linux, MacOS o Windows como sistema operativo.

Me gustaría hacer foco en:

 * Un sistema de generación continua: tener un Jenkins en un server que vaya generando CDPedias una atrás de la otra.
 * Que la CDPedia funque en Android: debería ser fácil porque no necesitamos armar una interfaz, pero hay que empaquetarlo.
 * Generar la CDPedia en Guaraní: sería el segundo idioma que hacemos, y debería ser fácil porque es chiquita.

''Propone: FacundoBatista''

=== Encuentro ===

[[http://encuentro.taniquetil.com.ar/|Este]] es un simple programa que permite buscar, descargar y ver contenido del canal Encuentro, Paka Paka, BACUA, Educ.ar y otros. 

''Propone: FacundoBatista''

=== RestoPY ===

Django para restaurantes y bares (https://bitbucket.org/edvm/restopy/). Es un sistema simple que utiliza el admin de django para gestionar los productos que se venden, las bebidas, el stock, los empleados y sus horarios, las reservas, etc ... Faltan implementar módulos en la parte gestión e implementar las vistas del resto del sistema (las vistas que van a utilizar los mozos, el login, etc ).

''Propone: Emiliano Dalla Verde Marcozzi''

=== SAW / SQLAlchemy Wrapper ===

Es una librería que quiere simplificar el uso de SQLAlchemy ( http://www.youtube.com/watch?feature=player_embedded&v=-vdl3UGxWcA ). Estaría bueno serializar el schema de la base a JSON/YAML/WHATAVA, crear unittests (la librería puede que tenga muchos tests desactualizados), crear doc copada en PyPI, si serializaste el schema se puede implementar un 'diff' fácil para poder comparar schemas entre bases de datos). El repo por acá https://bitbucket.org/msa_team/sawrapper

''Propone: Emiliano Dalla Verde Marcozzi''

=== Midinect ===

Midinect es un generador de mensajes midi a partir de una kinect, el proyecto "arrancó" el pycamp del año pasado,
falta hacerle muchas cosas:
 * Reducir la latencia
 * Hacer un mejor uso de numpy
 * Crear una interface de configuracion (Probablemente con QT)
 * Empaquetar para Linux y Mac (si... windows + midi Sucks)
 
Las herramientas elegidas son Freenect y OpenCV, hacen falta mano de expertos en AI y procesamiento de imagenes en realtime.

''Propone: JoaquinSorianello''

=== Fugue ===

Fugue es una herramienta de calibracion optica y deteccion de actitud para proyectores, permitiendo hacer *Projection Mapping* con mucha precision. La interface está empezada en QT, y para la calibración se usa OpenCV y un solido de dimensiones conocidas.

Si alguien lleva un proyector, tambien podemos encarar la creaccion de algunas primitivas basicas para hacer projection mapping usando el canvas acelerado con OpenGL que tiene QT

''Propone: JoaquinSorianello''

=== Hackeando Cosas ===

Un espacio para traer arduinos, rasberrys, wimotes, kinects, camaras, smartphones y otros elementos "Hackeables" para hacer programación artistica.

''Propone: JoaquinSorianello''

=== ArmagretronJS ===

Implementar una version del Juego ArmagetronAD (furor de pycamp 2011) usando WebGL (y algo com three.js) + un servidor twisted para manejar la lógica del juego.

''Propone JoaquinSorianello''

=== RedPanal reloaded ("Github para músicos") ===

Plataforma para la creación colaborativa de proyectos musicales. Orientado a trabajos multipista.

 * proyectos multipista completos
 * cada músico trabaja en su propio DAW
 * construccion colectiva: licencias CC
 * busquedas: categorizaciones de audios y proyectos
 * federación de contenidos
   * sistema de torrents
   * los usuarios comparten espacio en disco y ancho de banda para hostear una porcion de los audios de toda la comunidad
 * cliente instalable en PC para sincronizacion de proyectos (aka, tortoiseMusical)
 * web merges/ pull requests (me gusta esa pista la integro a mi proyecto con un click)

''Propone SantiagoPiccinini''

=== Buscador de audio  ===

Me gusta escuchar radio y no me gustan las publicidades.
La idea es aprovechar el audio separador entre contenido y publicidad (el que dice 'comienza espacio publicitario'), para poder acortar el audio grabado de un streaming de radio.

El problema a resolver es: Dado un audio corto encontrar los momentos en los que aparece en un audio largo. Luego puede integrarse a audacity o ffmpeg para acortar.

Para esto se pueden usar distintas técnicas, en prinicpio se me ocurre:
 * En el dominio del tiempo haciendo un Filtro Adaptado ( http://en.wikipedia.org/wiki/Matched_filter )
 * En frecuencias utilizando algo del estilo de http://en.wikipedia.org/wiki/Mel-frequency_cepstrum

''Propone DiegoMascialino''

=== Trabajar en Shiva ===

Shiva ( https://github.com/tooxie/shiva-server ) es un proyecto para organizar tu música y exponer una api REST, y algunas cosas mas... lo comentaron en la lista hace unos meses.
Yo todavía no lo uso, pero me parece un buen momento para meterle mano.

Mejorar la parte de lyrics:
 * Agregarle algunos scrapers
 * Que sea unicode el manejo interno de las letras
 * Normalizar strings para búsquedas, ahora solo hace to_lower en cada scraper

 * Soporte para guardar la información en los tags de los archivo. Para poder agregarle la información obtenida a cada mp3, para visualizarla cuando se reproduce el archivo en un teléfono o ipod.

''Propone DiegoMascialino''

=== Beam: editor de texto por consola ===

La idea es hacer un editor de texto básico como el notepad pero por consola e inspirado en vim. De vim se toma la idea de tener varios modos/estados para interactuar, y lo de ser básico es para que sea muy customizable mediante plugins. Los plugins serían eggs instalables con pip y configurables en un settings.py (similar al .vimrc) que se puede versionar y compartir en un repo.
Tengo un archivo beam.py que ya cuenta con el modo comando y modo inserción y permite editar un archivo y guardarlo. Estoy usando la librería urwid hecha en python (y bastante pythonica) para el dibujado de la consola. Pero falta definir mejor la arquitectura del editor.
'''Propuesta:''' llegar a una version 0.1 que funcione(?), tenga las bases para integrarse con plugins y si queda tiempo, escribir algunos plugins.

''Propone HernanLozano''


=== Python en las escuelas con pilas-editor ===

Queremos acercar la posibilidad de aprender programación a los mas jóvenes de las escuelas:

http://www.pilas-editor.com.ar

Pero antes de comenzar a golpear puertas, la idea es mejorar el prototipo del editor online para programar videojuegos, mejorar el soporte para python y pilas en javascript.

El proyecto es todo un desafío técnico y creativo, una oportunidad copada de hacer algo 'heavy', pero factible: python completamente en el navegador, diseñar un IDE, videojuegos, tutoriales online etc...

''Propone: HugoRuscitti''

=== Taller sobre webapps AngularJS ===

Vamos a ver cómo construir webapps de manera práctica, usando un enfoque nuevo y simple.

Usaremos herramientas como angularjs (para la interacción con el usuario), Flask como proveedor de datos json, y socketio con d3 para lograr gráficas en tiempo real.

Pienso que puede ser un taller interesante para conversar sobre arquitecturas de aplicaciones web, encontrar una forma mas sencilla de hacer interacciones complejas y amigarnos con javascript (no es tan feo honestamente...)

 * [[http://angularjs.org/|web de angularjs]].
 * [[http://d3js.org/|web de d3]].

''Propone: HugoRuscitti''



===  Proyección de: Indie Game The Movie ===

La idea es ver juntos un documental sobre video juegos independientes, en donde muestran los desafíos, altibajos y visión del mundo de 4 desarrolladores admirables:

http://www.youtube.com/watch?v=5RjRb88XFL0

Para darse una idea de los tipos de juegos que se consideran indie ver:

http://www.youtube.com/watch?v=uqtSKkyJgFM

''Propone: HugoRuscitti''


=== Taller sobre como hacer un videjuego con pilas-engine ===

La propuesta es hacer un juego sencillo paso a paso, contar algunos 'trucos' en la construcción de un juego y algunos patrones de diseño bien prácticos para no volverse loco haciendo un juego (o no tan loco).

Comenzaríamos desde cero, no hace falta haber hecho juegos, vamos a hacer algo bien sencillo como lo siguiente:

http://www.youtube.com/watch?v=89giezKWgJE


''Propone: HugoRuscitti''

=== Juegos electromecánicos: POV Hexagon ===

Estoy buscando algún juego sencillo que pueda usar como pantalla una rueda de bicicleta con una hilera de leds, algo similar a: http://www.ladyada.net/make/spokepov/

Mi idea durante pycamp es armar la base de un clon de Super Hexagon que pueda funcionar en una raspberry pi teniendo como salida dicha pantalla.


''Propone: alecu''
