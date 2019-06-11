
**.. raw:: html
Rendering of reStructured text is not possible, please install Docutils.**



::

   Idea: Editor de ebooks online y colaborativo
   ================================================

   Motivación
   ----------

   Aunque no "apocalípticamente" como alguno preveían, la lectura de libros electrónicos se
   hace cada más popular. Los lectores de libros electrónicos como el Kindle son cada vez más accesibles
   y a esto se le suman otros dispositivos que, si bien no pensados centralmente en la lectura,
   pueden funcionar como tales.

   No obstante, lo que importa es lo de adentro. Y lo de adentro no se consigue tan fácilmente, sobre todo
   en idioma español y que se lea dignamente.

   Las herramientas de conversión automatizada (como Calibre_) tienen muchas
   limitaciones y producen un código sucio que, en general,
   requieren trabajo de posprocesado manual (con herramientas como Sigil_)
   para obtener un maquetado correcto y, en definitiva, una lectura fluída y agradable.

   Pero el trabajo de "corrección" (o edición desde 0) es tedioso y muchas veces arduo para una sola persona.

   Por esto propongo realizar un editor de *ebooks*, online y colaborativo.


   Ideas
   -----



   - Sigil_ es una aplicación para la edición de ebooks, libre, multiplataforma y además funciona bien.
     Creo que lo usa bastante gente. Basicamente permite un modo de edición WYSIWYG, otro en modo fuente
     (que es, ni más ni menos, que html) y un manejo sencillo de la ToC.
     Creo que es un buen ejemplo para inspirarse.

   - Yo sé y tengo ganas de usar Django. ¿Les va?

   - Como se trata de "editar" (xhtml + css), necesitamos un editor. Para codigo Ace_ está
     `buenísimo <http://ajaxorg.github.com/ace/build/kitchen-sink.html>`_ ( y además
     existe como `widget de django <https://github.com/Celc/django-ace-editor>`_ ) pero 
     me parece que no tiene modo WYSIWYG para html. Quizas habrá que elegir alguno de
     `estos <http://www.djangopackages.com/grids/g/wysiwyg/>`_
          
   - lo de "colaborativo" no lo tengo claro. Se podrá hacer algo como google docs
     que permite la edición simultánea? A priori, podemos arrancar en modo "bloqueante"
     como hace moin moin.

     - por otro lado, yo (alecu) opino que es mejor no arrancar de algo bloqueante, sino partir de algo que ya tenga la colaboración metida adentro. Por ejemplo se le podría hacer un view de "ebook" a: https://github.com/Pita/etherpad-lite (a pesar de que es node.js)


   - En cualquier caso, parece necesario (o al menos util) tener un control de
     versiones sobre la edicion. Conozco reversion_ y apesta bastante ¿alguien conoce
     una alternativa?

     - si persistimos los "ebooks" como archivos (el epub descomprimido) y no a nivel bbdd,
       podemos usar un sistema de control de versiones conocido como mercurial o git. Si bien mercurial está hecho en python,
       los propios desarrolladores `no recomiendan usar la API interna <http://mercurial.selenic.com/wiki/MercurialApi>`_ sino
       `esta libreria <https://bitbucket.org/haard/hgapi>`_ que interactua con el CLI hg. Para git
       `dulwich_ <https://github.com/jelmer/dulwich>`_ parece muy piola

     - otra posibilidad: usar una base de datos documental (MongoDB , couchdb, cassandra? alguien tiene experiencia?)


   - Manejo de permisos, quien puede ver/editar ?

   - Input:

       - arrancar un ebook from scratch
       - subir/importar desde archivo local/online (convirtiendo, en caso necesario, usando calibre)
       - listado de urls parseadas con readability_  ¿se les ocurre alguna manera user-friendly de
         darle más posibilidades a esta opción? Por ejemplo, quiero armar un ebook con todas las
         contratapas de 2011 escritas por Juan Forn en Página/12.
       - Feeds RSS/Atom, con la posibilidad de solicitar "todo el contenido" aun en un feed
         con articulos incompletos


   - Ouput:

       - Creo que hay que manejarse en formato .epub (el estándar más extendido) y convertir desde ahí
         usando Calibre_.
       - enviar por email 
       - enviar al kindle  (simil anterior)
       - u1 / dropbox ?

   - Validación:

      - Sigil hizo y usa Flightcrew_, que parece lo mejorcito para validar el epub.
        El core es libreria C++ ¿se puede wrappear?  En cualquier caso,
        tambien tiene un cliente CLI que se puede usar via subprocess.
      - También usa HTMLTidy para *sanear* el html (de entrada/salida).
        Hay `wrapper <https://github.com/countergram/pytidylib/>`_

   - Filtros

      - calibre permite aplicar filtros basados en xpath en la conversión.
        Podemos permitir definirlos al usuario ? y a posteriori ?
      - Nunca entendí la sintaxis de xpath. Se podrá permitir manipular
        via pyquery_ ?
      - readability_ está buenísimo pero a veces falla. Ayudarlo
        a saber donde está el contenido?


   - UI:

     - No soy *muy* conocedor de estos menesteres pero creo que jquery-ui_ está bueno.
     - Les gusta `esto <http://layout.jquery-dev.net/demos/container_margins.html>`_ ?
     - Alguien maneja algun framework CSS ?
      

   Se te ocurre algo ? tus ideas son bienvenidas!

          

   .. _Calibre: http://calibre-ebook.com/
   .. _Sigil: http://code.google.com/p/sigil/
   .. _Ace: http://ajaxorg.github.com/ace/
   .. _reversion: https://github.com/etianen/django-reversion
   .. _readability: http://pypi.python.org/pypi/readability-lxml
   .. _pyquery: http://pypi.python.org/pypi/pyquery/
   .. _Flightcrew: http://code.google.com/p/flightcrew/
   .. _jquery-ui: http://jqueryui.com

