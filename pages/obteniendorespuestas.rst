
Obteniendo Respuestas
=====================

*por Mike Ash*

Traducido por Juan Pedro Fisanotti

**Nota del Traductor**

En el texto se utiliza varias veces la abreviación "RTFM!", que traducida significa "lee el maldito manual!"(Read The Fucking Manual!). Se deja sin traducir, porque se utiliza de esa manera en la jerga informática.

Doy vueltas por varios chats y foros relacionados a programadores y veo a mucha gente teniendo problemas para obtener respuestas. No reciben respuesta, obtienen respuestas pobres, o absorben mucho abuso verbal. Como persona realizando preguntas, hay algunas cosas simples que puedes hacer para mejorar tus chances de obtener buenas respuestas. Esta guía va a mostrarte diez cosas sencillas que puedes hacer para asegurarte de que tus preguntas son respondidas rápidamente y bien.

Si estás apurado, puedes saltear la introducción aburrida e ir directamente a la guía.

Por favor deja tus comentarios sobre este artículo `en el post del blog`_.

Otras personas han escrito articulos sobre este tema antes, pero ellos sufren algunos problemas. Mi objetivo es evitar esos problemas y hacer algo que sea directamente útil para ti, la persona con problemas, en lugar de algo que es principalmente útil para las personas que responden las preguntas.

`How To Ask Questions The Smart Way (Cómo Realizar Preguntas De Manera Inteligente)`_ es bastante condescendiente, especialmente si ya has sido insultado por alguien que te dijo que necesitas ayuda en realizar preguntas. Si te envían a una guía con un archivo sobre ``smart-questions`` (preguntas inteligentes), eso significa que esta persona piensa que tienes preguntas estúpidas, quien necesita eso?

`Help Vampires: A Spotter's Guide (Vampiros de Ayuda: Una Guía Para El Observador))`_ es buenísima, pero no está escrita desde el otro lado. Mientras que es muy buena para personas que dan vueltas y responden un montón de preguntas, y los ayuda a lidiar con los nombrados Vampiros, no es algo muy útil para una persona realizando preguntas.

Otra guía que acabo de descubrir es `Getting help on IRC (Obteniendo ayuda en IRC)`_. Es un compañero práctico, pero más orientado hacia lo escencial de la etiqueta de IRC y menos hacia las preguntas específicamente.

Y así te presento a *Getting Answers (Obteniendo Respuestas)*. El objetivo del artículo es obtener respuestas a tus preguntas, nada más y nada menos. Voy a ignorar completamente cosas aburridas como la manera adecuada de saludar a la gente o cúando leer el tópico. Esta guía te llevará por diez cosas básicas que puedes hacer para mejorar las chances de obtener respuestas, y mejorar la calidad de las respuestas que recibes. Obtener como respuesta un ``rtfm!`` es considerado un fracaso, no mejor que no haber recibido respuesta en absoluto, y obtener un consejo que resuelve tu problema es éxito. Todo lo demás es secundario a esto.

Vas a notar un sabor distintivo de IRC y Mac en la guía, pero las ideas deberían ser verdad para cualquier tema en cualquier contexto.

Chico Pregunta y Hombre Respuesta nos ayudarán ilustrando los principios en la guía. CP y HR tendrán conversaciones simuladas mostrando la manera correcta y equivocada de obtener buenas respuestas rápidamente. Las conversaciones son armadas, pero cada una de ellas está tomada directamente de situaciones que he visto.

Explica qué es lo que no funciona
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Puedes pensar que esto es obvio, pero no lo es. Muchas personas preguntan sobre técnicas generales o sobre algo que ellos sienten que es más simple y relacinado en lugar de simplemente decir qué es lo que está andando mal. Si piensas que es un problema con una técnica más general, pregunta eso también, pero siempre dile a la gente qué es lo que no te está funcionando.

Mala pregunta:

::

   CP: como compilo una aplicacion en 10.4 que funciona en 10.3?
   HR: configura el SKD como para: ...
   CP: hay alguna otra manera?
   HR: no entiendo lo que quieres decir
   CP: bueno, mi aplicación falla cuando la ejecuto en 10.3
   HR: ...

Buena pregunta:

::

   CP: my aplicación falla en 10.3 pero funciona bien en 10.4, cómo descubro el problema? es un problema de como configuré mi compilación?
   HR: tu configuración de compilación no debería importar, probablemente estás enlazando contra algo que no existe en 10.3. mira la salida de la Consola luego de la falla para ver qué es

Lo que está mal es, "mi aplicación falla cuando la ejecuto en 10.3", pero esto ni siquiera es mencionado hasta luego de varias rondas en el proceso de pregunta/respuesta, y luego de mucho tiempo desperdiciado en ambos lados. La explicación de Hombre Respuesta sobre los SDK era completamente innecesaria porque Chico Pregunta ya sabía sobre eso. Chico Pregunta perdió tiempo dirigiendo a Hombre Respuesta hacia un camino irrelevante en lugar de exponer su problema al inicio.

Exponiendo exactamente qué es lo que está mal inmediatamente, Chico Pregunta obtuvo instantaneamente una respuesta útil de Hombre Respuesta.

Provee todo por adelantado
~~~~~~~~~~~~~~~~~~~~~~~~~~

Haciendo que la gente tenga que pescar (buscar) información desperdicia tu tiempo. Da tanta información de fondo en tu pregunta original como puedas.

Mala pregunta:

::

   CP: cómo anexo a una cadena de texto? (n del t: "append")
   HR: utiliza stringByAppendingString:
   CP: bueno, pero no quiero crear un nuevo objeto
   HR: entonces utiliza NSMutableString y appendString
   CP: pero estoy utilizando C, no ObjC
   HR: argh, por qué no lo has dicho entonces? utiliza strcat
   CP: y si tengo un CFString?
   HR: gah! utiliza CFStringAppend
   CP: pero eso no funciona, yo necesito anexar un char *
   HR: que se pudra <se va> (n del t: "screw this")

Buena pregunta:

::

   CP: cómo anexo un char * a un CFString? Las cosas que estoy encontrando solo funcionan con CFMutableString
   HR: esa es tu única opción, vas a tener que crear una copia mutable, y luego utilizar CFStringAppendCString

No especificando tu pregunta lo suficiente no te ahorra ningún tiempo (de cualquier forma, vas a tener que decirlo todo enventualmente) y hace menos probable que la gente te responda, tanto ahora como en el futuro. Puede que tengas miedo de decir demasiado. No lo tengas. Es mucho mejor ser demasiado específico que muy poco específico, ya que es mucho más fácil para alguien ignorar los detalles extras que preguntarte por los faltantes. Cuando dudes, di "No estoy seguro de si esto es relevante, pero estoy haciendo..."

Postea tu código
~~~~~~~~~~~~~~~~

Esto no se aplica para grandes preguntas conceptuales, por supuesto, pero para todo lo demás es escencial. Nunca describas tu aproximación general a un problema sin postear el código detrás de esta, ya que el código es lo que cuenta, y traducir todo al español tiende a alterar las cosas dejándolas irreconocibles.

Mala pregunta:

::

   CP: cuando creo un NSString desde datos UTF-8 falla, por qué?
   HR: postea tu código
   CP: no creo que sea un problema con el código
   HR: que se pudra <se va> (n del t: "screw this")

Mala pregunta #2:

::

   CP: si creo una subclase de NSMatrix entonces no aparece nada en la pantalla, pero utilizando una NSMatrix limpia funciona, por qué?
   HR: cómo diablos podría yo saberlo?

Mala pregunta #3:

::

   CP: cuando creo un NSString desde datos UTF-8 falla, por qué?
   HR: postea tu código
   CP: no tengo el código conmigo, pero estoy haciendo algo como char *utf8str = ...; [utf8str stringWithUTF8String]
   HR: no puedes enviarle un mensaje a un char *, y no existe un método stringWithUTF8String sin parámetros, prueba ...
   ...al día siguiente...
   CP: encontré el problema, en realidad estaba utilizando stringWithCString:
   HR: aarrgghh!

Buena pregunta:

::

   CP: cuando creo un NSString desde datos UTF-8 utilizando char *utf8str = ...; [NSString stringWithCString:utf8str] falla, por qué?
   HR: porque stringWithCString: no espera UTF-8, utiliza stringWithUTF8String

Pedir código implica tiempo y esfuerzo, y tu puedes acelerar la respuesta proveyéndolo inmediatamente. Si no sabes si es relevante o no, postéalo de todas formas. Nunca cites o escribas de memoria. Incluso cuando lo hagas con las mejores intenciones, vas a introducir errores sutiles o evidentes en tu código, y la gente a la que le estás hablando va a resolver un problema completamente diferente al que en realidad tienes.

(En IRC, no olvides utilizar un pastebot. Pegar tu código directamente en el canal es considerado grosero si posee más de una linea más o menos.)

Has tu investigación de antemano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mientras que puede ser una buena idea comentarle a un amigo o dos acerca de un problema inmediatamente después de que se presenta, preguntarle a extraños debería ser uno de tus últimos recursos. Has todo lo que puedas para investigar el problema y solucionarlo por tu cuenta antes de hacer eso. Esto te ayudará a obtener una respuesta al permitirte plantear una pregunta mucho más informada. Cuanto más conozcas del tema, mejores son las chances de preguntar lo que necesitas.

Mala pregunta:

::

   CP: cómo creo un hilo?
   HR: rtfm!

Buena pregunta:

::

   CP: leí la documentación de NSThread, pero cómo puedo hacer que llame a un método con un parámetro int?
   HR: crea un nuevo método que reciba un NSNumber y simplemente llame al otro método con su intValue

En la primer versión, Chico Pregunta no obtuvo una respuesta muy útil. La repuesta de la segunda versión fue mucho más útil, porque Chico Pregunta leyó acerca del tema antes de realizar su pregunta. Chico Pregunta también realizó la movida inteligente de detallar lo que él había investigado. Es mucho menos probable que recibas un inútil ``rtfm!`` si le dices a los demás qué manuales específicos ya has leido.

Has tu investigación durante
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tu trabajo no termina una vez que has realizado la primer pregunta. Cuando te presenten una pieza de consejo que no te resulte familiar, investígala antes de preguntar acerta de ella. Incluso solo pegar el término desconocido en Google puede ayudar muchísimo.

Mala pregunta:

::

   CP: cómo puedo obtener el listado de un directorio?
   HR: utiliza NSFileManager
   CP: qué es NSFileManager?
   HR: rtfm!

Buena pregunta:

::

   CP: cómo puedo obtener el listado de un directorio?
   HR: utiliza NSFileManager
   ...CP busca NSFileManager en Google...
   CP: ok, gracias... se puede de alguna manera hacer que solo me devuelva los resultados cuyo nombre comienza con "tty"?
   HR: puedes obtener todos los resultados, y luego filtrarlos utilizando NSPredicate haciendo...

Investigando tus preguntas sucesivas tan bien como tu pregunta original te permitirá obtener respuestas más útiles.

Has tu investigación después
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apuesto a que lo veías venir. Después de haber recibido un consejo y partir, deberías hacer tanta investigación como puedas, antes de volver y preguntar acerca del consejo.

Mala pregunta:

::

   CP: cómo puedo obtener el listado de un directorio?
   HR: utiliza NSFileManager
   ...CP se va...más tarde:
   CP: cómo uso NSFileManager?
   HR: rtfm!

Buena pregunta:

::

   CP: cómo puedo obtener el listado de un directorio?
   HR: utiliza NSFileManager!
   ...CP se va...al día siguiente:
   CP: cuando uso NSFileManager para listar los contenidos de /, obtengo "Applications" en lugar del nombre traducido que veo en Finder, por qué hace esto y cómo puedo replicar el comportamiento de Finder?
   HR: los nombres localizados no existen en el sistema de archivos, pero puedes utilizar...

Como antes, haciendo tu investigación obtienes mejores respuestas.

No postees la misma pregunta repetidamente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esto se aplica especialmente a foros y listas de correo, pero también se aplica a IRC. A menos que tu problema sea altamente complicado, mucha gente va a poder ayudarte. Lo más probable es que alguna de esas personas haya visto tu pregunta la primera vez. Si nadie responde, has más investigación, intenta producir un pequeño caso de prueba o al menos reduce los límites del problema, y vuelve en un día o dos con más información.

Mala pregunta:

::

   CP: mi subclase NSMatrix modificada no se dibuja, ayuda?
   ...grillos...al día siguiente:
   CP: mi subclase NSMatrix modificada no se dibuja, ayuda?
   ...grillos...al día siguiente:
   CP: mi subclase NSMatrix modificada no se dibuja, ayuda?

Buena pregunta:

::

   CP: mi subclase NSMatrix modificada no se dibuja, ayuda?
   ...grillos...al día siguiente:
   CP: mi subclase NSMatrix modificada no se dibuja, creé un proyecto de prueba sencillo que exibe el comportamiento, pueden bajarlo en http://blah, alguien sabe lo que está sucediendo?
   HR: no sobreescribas drawRect:

Si nadie pudo responder tu pregunta la primera vez, probablemente no querrán responderla la segunda vez tampoco. Utiliza el tiempo que gastas esperando por una respuesta para trabajar en el problema tu mismo. Incluso si no tienes esperanzas de resolverlo, puedes producir algo y recolectar información que ayudará a otros a solucionarlo.

Sigue luego de obtener una respuesta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deberías siempre responder a las personas que te dan consejo, incluso cuando ya lo entiendes y funciona perfectamente, y no necesitas más información.

Mala pregunta:

::

   CP: mi programa falla con EXC_BAD_ACCESS cuando hago [obj release], qué es lo que sucede?
   HR: probablemente estás sobre-liberando, intenta utilizar NSZombieEnabled
   ...más tarde...
   CP: mi programa falla en una especie de callback de notificación, como puedo debuguear eso?
   HR: espera, ya has resuelto tu problema con [obj release]?
   ...más tarde...
   CP: mi prigrama me da un error diciendo que NSString no responde a setObject:forKey:, cómo debugueo eso?
   HR: que se pudra <se va> (n del t: "screw this")

Mejor pregunta:

::

   CP: mi programa falla con EXC_BAD_ACCESS cuando hago [obj release], qué es lo que sucede?
   HR: probablemente estás sobre-liberando, intenta utilizar NSZombieEnabled
   CP: ok, gracias
   ...más tarde...
   CP: encontré mi problema de sobre-liberación de antes, pero ahora mi programa falla en __CFXNotificationPost, cómo puedo debuguear eso?
   HR: asegúrate de quitarte a ti mismo como observador del NSNotificationCenter en tu método -dealloc
   CP: oops, gracias...más tarde...
   CP: ok, tengo arreglado el error de la notificación, pero ahora mi programa me da un error diciendo "-[NSCFString setObject:forKey:]: selector not recognized", cómo debugueo eso?
   HR: ello podría deberse a otro error de sobre-liberación, o solo a confusión de tipos donde tratas a un string como a un diccionario.
   CP: ok, voy a hecharle una mirada, gracias

A menos que te encuentres pagando por la ayuda (en cuyo caso probablemente puedes ignorar esta página por completo, y la persona a la que le estás pagando va a simplemente cobrar más), las personas que están respondiendo tus preguntas lo están haciendo gratuitamente. Como a una tierna mascota que se sienta cuando se lo ordenas, necesitas recompensarlos cuando hacen lo que tu quieres.

La segunda conversasión está titulada como "mejor" en lugar de "buena" debido a que probablemente viole la regla #2. Las respuestas básicas a estas preguntas deberían existir en la documentación conceptual, que puede entonces ser utilizada para realizar mejores preguntas y obtener mejores respuestas. Pero no pude pensar en un ejemplo mejor.

Para preguntas más complejas, menciona cómo finalmente lo has solucionado y qué consejo has seguido. Esto no solo otorga una poderosa recompensa a las personas que lo proveyeron, sino que también permite a otras personas aprender de tu ejemplo.

Trata a la lista como personas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Muchas conversasiones que he visto indican una sutil, enterrada creencia de que la lista o el chat es una especie de máquina de respuestas, y que la clave para obtener buenas respuestas es salir a la caza hasta que se encuentre el formato preciso requerido para la pregunta.

Mala pregunta:

::

   CP: como anexo a un NSString? (n del t: "append")
   HR: lee la documentación de NSString, busca "append"
   CP: soy nuevo con Cocoa y quiero anexar a un NSString, cómo hago eso?
   HR: hola? lee lo que he dicho arriba
   CP: estoy en 10.4.7 usando Xcode 2.3, no se mucho sobre Cocoa, cómo anexo a un NSString?
   HR: ...

Buena pregunta:

::

   CP: como anexo a un NSString? (n del t: "append")
   HR: lee la documentación de NSString, busca "append"
   CP: doh, lo siento, me olvidé de mencionar que quiero anexar un string C
   HR: en ese caso, crea un NSString desde el string C, luego anexa eso, o utiliza %s con stringByAppendingFormat:

Esto no es un juego, te encuentras hablandole a personas reales y vivas. Trátalas de la misma manera con la que tratarías a personas con las que hablas cara a cara, y obtendrás resultados mucho mejores.

Siempre considera la respuesta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A veces un verdadero idiota te responderá, y a veces te encontrarás con alguien inteligente que se encuentra en un mal día o que no ha leído correctamente tu pregunta. Sin embargo, la mayoría del tiempo estarás hablando con personas que conocen más acerca del tema en discusión que lo que tu conoces (recuerda que esa es la razón por la cual acudiste a ellos por ayuda en primer lugar). Por este motivo, vale la pena al menos considerar la posibilidad de que ellos saben de qué están hablando.

Mala pregunta:

::

   CP: cómo puedo mapear a memoria a un archivo utilizando Cocoa?
   HR: NSData
   CP: por favor lee mi pregunta nuevamente, quiero mapear a memoria a un archivo
   HR: ...

Mejor pregunta:

::

   CP: cómo puedo mapear a memoria a un archivo utilizando Cocoa?
   HR: NSData
   CP: huh? cómo se relaciona ello con mapear un archivo a memoria?
   HR: NSData posee inicializadores que te permiten crear uno mapeando a memoria un archivo.

Buena pregunta:

::

   CP: cómo puedo mapear a memoria a un archivo utilizando Cocoa?
   HR: NSData
   CP: <lee la documentación de NSData, encuentra el método correcto> lo tengo, gracias!

Si la respuesta de la otra persona realmente era correcta, entonces ganarás muchísimo tiempo si comienzas asumiendo que lo era. Si asumes que es errónea, o deberías esperar a que la otra persona te corrija, o si no tienes suerte ni siquiera se molestará en hacerlo y tu no obtendrás una respuesta. Incluso si la respuesta es errónea, tendrás más probabilidad de obtener una respuesta correcta si eres gentil al señalar lo erróneo.

Que tus soluciones sean rechazadas por la persona que realiza la pregunta es frustrante. Es menos probable que las personas frustradas respondan tus preguntas. Se bueno con ellos, y ellos serán buenos contigo.

**Nota para las listas de correo:** a diferencia de los medios efímeros como IRC, las listas de correo tipicamente son archivadas y se puede buscar en ellas. Cuando encuentras una solución, posteala! De esa manera, cuando olvides cómo habías hecho esto meses después y busques en la lista por una respuesta, podrás ver como lo habías resuelto antes.

Preguntas, comentarios, u otro feedback? Envía un e-mail al autor: ``mike EN mikeash PUNTO com``

.. ############################################################################


.. _en el post del blog: http://www.mikeash.com/blog/pivot/entry.php?id=21

.. _How To Ask Questions The Smart Way (Cómo Realizar Preguntas De Manera Inteligente): http://catb.org/esr/faqs/smart-questions.html

.. _`Help Vampires: A Spotter's Guide (Vampiros de Ayuda: Una Guía Para El Observador))`: http://www.slash7.com/pages/vampires

.. _Getting help on IRC (Obteniendo ayuda en IRC): http://workaround.org/getting-help-on-irc

