---------------------------------------
Depuración y defragmentación de memoria
---------------------------------------

.. class:: endnote

+---------------------------------------------------------+-------------------------------------------+
| .. image:: imgs/claudiofreire.jpg                       |**Author:** Claudio Freire                 |
|    :class: right foto                                   |                                           |
|                                                         |                                           |
+---------------------------------------------------------+-------------------------------------------+

.. raw:: pdf

    Spacer 0 1cm

Introducción
------------

Esta charla se planificó para darse en 20 minutos. Si no la pueden leer en 20 minutos, releer y releer
hasta que tome 20 minutos :-p

Bueno, en realidad el texto aquí presente está sólo ligeramente basado en la charla real. Soy de improvisar mucho en las
charlas, sólo tengo a las diapositivas como guía general de cómo va a progresar la charla, y este formato
no se adapta tan bien a la improvisación. Además que ni en pedo me acuerdo de las palabras exactas que usé ;)

Pero en serio... es un tema fumado, releer y releer hasta entender.

Cuando empecé a buscar tema para la charla, me decidí por la fragmentación de memoria porque antes yo creía
que era un mito. Ok, sí, puede suceder... pero ¿a alguien le sucede? ¿Es un problema? Qué ingénuo de mi parte
fue dudar de que ambas respuestas fuesen sí.

En la PyConAr 2010 (y aquí en este espacio ahora) no sólo tuve la oportunidad de transmitir alrededor de 4
meses de revolver las entrañas de python tratando de averiguar qué sucedía en mis aplicaciones (donde sufrí
de la fragmentación de memoria), sino que aprendí yo mismo que este problema es mucho más común de lo que esperaba.

Cuando comenzó la charla, pregunté: ¿alguien sabe lo que es la fragmentación de memoria?. Exactamente cero
personas levantaron la mano. Exactamente esa cantidad esperaba yo. Pero al final, varios se me acercaron
diciendo que lo mismo que me pasaba a mí (y yo describía, y describiré abajo) les estaba sucediendo.

Según mi estimación post-PyCon, un 10% de los presentes (asumo desarrolladores Python) sufren el problema, 
y a un 3% de ellos les trae problemas operativos serios. 
Así que el tema fue mucho más relevante de lo que yo esperaba.


¿Cómo administra memoria Python?
--------------------------------

Antes de ver qué es esto de la fragmentación, debemos estudiar algunos detalles internos de la administración
de memoria en Python.

¿Cómo dicen ustedes que administra la memoria Python? ¿Malloc? *(una función en C que reserva memoria para
quienes no saben C)*

Pues no. Python tiene requerimientos inusuales y muy específicos, si utilizara malloc para satisfacer todas sus
necesidades de memoria sería muy ineficiente. Python utiliza, en cambio, una serie de técnicas y estrategias
diseñadas para minimizar las llamadas a malloc, llamadas que son muy lentas para usar en el núcleo de la máquina
virtual de Python.

* Pools

  - Enteros

  - Flotantes

* Listas libres

  - Tuplas

  - Listas

  - Frames *(sí, los frames son objetos y hay que administrarlos también)*

* Arenas

Veamos de qué se tratan uno por uno

Pools
-----

No son piscinas.

Son arreglos, vectores de objetos del mismo tipo, que python utiliza comunmente para acelerar la creación y
destrucción de objetos muy comunes, como lo son los enteros y los números de coma flotante.

Cuando python necesita un objeto de estos no crea uno, crea muchos (tantos como entren en un bloque del pool),
y mantiene una lista enlazada de qué objetos tiene libres dentro de cada bloque:

.. figure:: imgs/pools.jpg
    :width: 50%
    :align: right
    :alt: Ejemplo de un pool de objetos
    
    Estructura de un pool de objetos

    En un pool, el campo **ob_type** (presente en todos los PyObject)
    se utiliza para enlazar los objetos libres. Cuando se necesita un
    objeto nuevo, se restaura el campo ob_type (trivial), y en general
    ya no hace falta más inicialización, por lo que es muy rápido.


En un pool de objetos, la creación y destrucción es muy rápida, y según el tipo de objeto, se puede
ahorrar un montón de inicialización (en el caso de enteros y números de coma flotante esto es muy cierto),
los objetos permanecen bien empaquetados en la memoria, todos juntitos, y en general todo funciona muy bien.

Listas libres
-------------

La idea de no tener que pedir memoria para crear o destruir objetos que son muy comunmente creados y destruidos
es algo que puede generalizarse desde los pools, a cualquier tipo de objeto (no sólo a objetos de un tipo particular),
incluso objetos de tamaño variable (donde tenerlos todos empaquetados en un arreglo o pool no es factible).

Cuando se hace esto, se tiene listas libres:

.. figure:: imgs/freelists.jpg
    :width: 50%
    :align: right
    :alt: Ejemplo de listas libres

    Estructura de una lista libres
    
    Las listas libres son muy parecidas a un pool, pero no se mantiene un arreglo de objetos, sino
    simplemente la lista enlazada de objetos libres. Cuando se destruye un objeto, se puede decidir
    ubicarlo en la lista libre en vez de efectivamente liberar la memoria, para poder aprovecharlo
    y reutilizarlo más tarde.

Esta idea de listas libres ahorra muchas llamadas a malloc, y es particularmente útil para cadenas, listas y tuplas,
que son objetos de tamaño variable muy intensamente utilizados en python y donde un pool no sería una idea práctica.
También son la razón principal por la cual Python es particularmente sensible a la fragmentación de memoria, ya vamos
a ver por qué.

Nótese que también los frames utilizan listas libres. Los frames son objetos, también de tamaño variable (pues necesitan
una pila, espacio temporal para las variables y objetos temporales que nuestro código genere), también muy intensamente
utilizados en python (se "crea" uno cada vez que se hace una llamada a una función). Las listas libres de frames son
una optimización muy importante (ahorran mucho tiempo de creación puesto que los frames son costosos de crear), pero también
contribuyen a la fragmentación de memoria (como toda lista libre).

Una cosa importante a recordar de las listas libres en Python es que la decisión de si destruir un objeto o
ubicarlo en la lista libre se hace al momento de dereferenciarlo (cuando su conteo de referencias llega a cero). Una vez
ahí, ahí permanece hasta que sea reutilizado. Python, para tomar esta decisión, tiene una serie de límites - X frames,
Y tuplas de tamaño 1, Z tuplas de tamaño 2, W cadenas, etc... (el límite suele ser 100 en cada caso)

Arenas
------

Ok... y el resto de los objetos. ¿Usan malloc?

Sí y no.

Usan arenas. Que no es de donde sale el vidrio, sino una mezcla entre pools, listas libres y malloc.

Para objetos pequeños, Python mantiene una *lista de pools* por cada tamaño concreto (recordemos que
los pools necesitan objetos del mismo tamaño pues son vectores). Cada pool tiene su lista libre, y cada
pool tieke 4Kb de tamaño. Esto toma el nombre de arena.

Para objetos grandes (más de 256 bytes), Python llama a malloc directamente.

Como los tamaños de objetos de python crecen de a 8 bytes (por su estructura), entonces hay exactamente 
32 arenas.

Todos los objetos de python se crean con este mecanismo de arenas, incluso los que usan listas libres.

Las arenas también introducen un problema de fragmentación interna, puesto que ningún bloque de la arena
puede ser liberado hasta que todos los objetos que viven en él sean liberados.


Fragmentación
-------------

Ahora, veamos lo que es la fragmentación de memoria:

.. figure:: imgs/memoria.jpg
    :width: 50%
    :align: right
    :alt: Mapa de memoria fragmentada
    
    Mapeo de una memoria fragmentada

    Si negro es espacio usado, y blanco es espacio libre,
    se puede ver aquí como hay mucho espeacio libre pero es inusable para objetos
    más allá de un determinado tamaño, por no ser espacio libre contiguo

Puesto simple, la fragmentación de memoria se produce cuando hay mucho espacio libre, pero no es contiguo.
Como en el mapa de memoria que se ve arriba, hay mucho espacio libre, pero es inusable para objetos grandes,
puesto que, a diferencia de un archivo que puede ser dividido en fragmentos en el disco, la memoria de un
objeto necesita ser contigua.

Así que, a diferencia de la fragmentación en un sistema de archivos, la fragmentación de memoria hace inusable
a la memoria. Si quisiera crear un objeto grande, digamos de unos megabytes, debería utilizar el espacio que
está hacia el final del mapa (o sea *extender la imagen virtual del proceso*). Esto efectivamente hace malloc
cuando se encuetra con esta situación.

El efecto inmediatamente visible es un uso ineficiente de la memoria disponible. Si mi programa necesita
2GB de memoria en teoría, podría estar pidiéndole 4GB al sistema operativo (porque tiene muchos pedacitos
reservados que no puede utilizar). Si tengo mucha mala suerte, esto podría hacer que mi sistema swapee.
Si tengo más mala suerte, thrashea, y se muere.


Veamos un ejemplo de código que fragmenta la memoria:

.. code-block:: Pycon

    >>> l = []
    >>> for i in xrange(1,100):
    ...   ll = [ " " * i * 16 for j in xrange(1000000 / i) ]
    ...   ll = ll[::2]
    ...   l.extend(ll)
    ...   print sum(map(len,l))
    ... 
    8000000
    16000000
    …
    792005616
    >>> 

Luego de esto, top nos dice::

    10467 claudiof  20   0 1676m 1.6g 1864 S    0 82.7   1:17.07 python

O sea, aunque según los cálculos el programa tenía que consumir 800M de memoria, efectivamente
consume 1.6G. El doble.

¿Por qué es esto?

Bueno, porque el ejemplo lo pensé específicamente para que cree un 50% de huecos inutilizables.
La memoria está fragmentada, pues, en un 50%.

Pero hay algo más grave. Si hago:

.. code-block:: Pycon

    >>> del l
    >>> del ll

Obtengo de top::

    10467 claudiof  20   0 1532m 1.5g 1864 S    0 75.6   1:17.96 python

Si repito el ejemplo de fragmentación, puedo comprobar que esos 1.5G están efectivamente libres para python::

    10467 claudiof  20   0 1676m 1.6g 1864 S    0 82.8   2:33.39 python

Pero si intento liberarlos (para el sistema operativo), no puedo.

¿WTF?


Enter Guppy
-----------

Guppy es un pecesito rojo comunmente encontrado en las peceras de todos lados. Esos pecesitos chiquitos, esos se llaman guppy.

Posta.

También es una biblioteca de extensión para Python que contiene un módulo, heapy, que me permite hacer diagnóstico de la memoria.

Posta.

.. figure:: imgs/guppy.jpg
    :width: 4cm
    :height: 3cm
    :align: left

    Guppy

Veamos un ejemplo de cómo usarlo:

.. code-block:: Pycon

    >>> from guppy import hpy
    >>> hp = hpy()
    >>> hp.heap()
    Partition of a set of 23778 objects. Total size = 1760692 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0  10642  45   696652  40    696652  40 str
        1   5432  23   196864  11    893516  51 tuple
        2    345   1   112968   6   1006484  57 dict (no owner)
        3   1546   7   105128   6   1111612  63 types.CodeType
        4     66   0   104592   6   1216204  69 dict of module
        5    174   1    93168   5   1309372  74 dict of type
        6    194   1    86040   5   1395412  79 type
        7   1472   6    82432   5   1477844  84 function
        8    124   1    67552   4   1545396  88 dict of class
        9   1027   4    36972   2   1582368  90 __builtin__.wrapper_descriptor

O sea, python (por el simple hecho de levantarlo) ya consume 1.7MB. En objetos python.
Heapy no cuenta lo que no son objetos python, así que lo que reporte heapy es todo memoria
utilizada directamente por objetos python.

Esto son cadenas, listas, diccionarios, arrays, pero **no** objetos mmap o memoria utilizada
por bibliotecas de extensión (ej: superficies SDL en pygame).

Diagnostiquemos ahora entonces:

.. code-block:: Pycon

    >>> l = []
    >>> for i in xrange(1,100):
    ...    … 

    >>> hp.heap()
    Partition of a set of 2612542 objects. Total size = 866405844 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0 2599386  99 854833304  99 854833304  99 str
        1    132   0 10516640   1 865349944 100 list
        2   5433   0   197064   0 865547008 100 tuple
        3    351   0   113784   0 865660792 100 dict (no owner)
        4   1547   0   105196   0 865765988 100 types.CodeType
        5     67   0   105112   0 865871100 100 dict of module
        6    174   0    93168   0 865964268 100 dict of type
        7    194   0    86040   0 866050308 100 type
        8   1472   0    82432   0 866132740 100 function
        9    124   0    67552   0 866200292 100 dict of class

Ok, como habíamos calculado, más o menos 800M (850M) en objetos python. Eso dice heapy.

.. code-block:: Pycon

    >>> del l
    >>> del ll
    >>> hp.heap()
    Partition of a set of 23844 objects. Total size = 1765236 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0  10690  45   698996  40    698996  40 str
        1   5433  23   197068  11    896064  51 tuple
        2    351   1   113784   6   1009848  57 dict (no owner)
        3   1547   6   105196   6   1115044  63 types.CodeType
        4     67   0   105112   6   1220156  69 dict of module
        5    174   1    93168   5   1313324  74 dict of type
        6    194   1    86040   5   1399364  79 type
        7   1472   6    82432   5   1481796  84 function
        8    124   1    67552   4   1549348  88 dict of class
        9   1027   4    36972   2   1586320  90 __builtin__.wrapper_descriptor

¿WTF?

Heapy nos dice que python ocupa de nuevo 1.7MB. Top sigue diciendo 1.6G. Yo le creo a top.

Sucede que de hecho, el resto es espacio “libre” (libre para python, no para el sistema operativo)

Haciendo un análisis diferencial, conseguiremos algo de perspectiva en el asunto:

.. code-block:: Pycon

    >>> from guppy import hpy
    >>> hp = hpy()
    >>> heap1 = hp.heap()
    >>> # experimento
    >>> heap2 = hp.heap()
    >>> cosas_nuevas = heap2 – heap1
    >>> del l, ll
    >>> basura = heap3 – heap1

Resulta en 3 snapshots del heap. *heap1*, como está al iniciar python. *heap2*, luego del experimento, y *heap3* luego de "liberar" todo,
y dos "diferenciales", *cosas_nuevas*, lo que hay en heap2 de nuevo (que no está en heap1), y *basura*, lo que hay en *heap3* que no está
en *heap1* (o sea, lo que no se liberó).

.. code-block:: Pycon

    >>> cosas_nuevas
    Partition of a set of 2588725 objects. Total size = 864642976 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0 2588706 100 854134668  99 854134668  99 str
        1      2   0 10506304   1 864640972 100 list
        2      6   0      816   0 864641788 100 dict (no owner)
        3      2   0      676   0 864642464 100 types.FrameType
        4      2   0      272   0 864642736 100 dict of guppy.etc.Glue.Owner
        5      1   0       68   0 864642804 100 types.CodeType
        6      2   0       64   0 864642868 100 guppy.etc.Glue.Owner
        7      2   0       64   0 864642932 100 tuple
        8      1   0       32   0 864642964 100 exceptions.KeyboardInterrupt
        9      1   0       12   0 864642976 100 int

Cabe preguntar: ¿Sólo 850M de cadenas? ¿Y los otros 800M para completar los 1.6G?

Bueno, sucede que la memoria se parece a un queso gruyere en este momento. Hay 800M en cadenas relativamente pequeñas, pero como en cada
paso yo liberaba la mitad de ellas (``ll = ll[::2]``), también tengo 800M de espacio libre inutilizable.Porque en cada paso, también,
necesito cadenas un poquito más grandes, y no se puede reutilizar los huecos.

A ver qué pasa al dereferenciar todo:

.. code-block:: Pycon

    >>> basura
    Partition of a set of 29 objects. Total size = 2520 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0      6  21      816  32       816  32 dict (no owner)
        1      2   7      748  30      1564  62 types.FrameType
        2     10  34      364  14      1928  77 str
        3      2   7      272  11      2200  87 dict of guppy.etc.Glue.Owner
        4      2   7       80   3      2280  90 __builtin__.weakref
        5      1   3       68   3      2348  93 types.CodeType
        6      2   7       64   3      2412  96 guppy.etc.Glue.Owner
        7      2   7       64   3      2476  98 tuple
        8      1   3       32   1      2508 100 exceptions.KeyboardInterrupt
        9      1   3       12   0      2520 100 int

¡Ahá!

¡Esto es importante!

Esos 29 objetos evitan que se pueda achicar el heap. Lo que me lleva...

Montón (heap)
-------------

...al heap.

Normalmente el heap se agranda y se achica.

.. figure:: imgs/heap.jpg
    :width: 50%
    :align: right
    :alt: Mapa de memoria fragmentada

    Ciclo de vida del montón

    El montón se expande y contrae, pero en cada ciclo puede quedar
    "basura", o capaz objetos útiles vivos, que impiden que se contraiga
    del todo. La memoria que queda en el medio no puede ser utilizada por
    otros procesos, sólo está libre para Python.

Como se ve en la figura, cada vez que se achica, no lo hace completamente.
A veces quedan objetos vivos en direcciones elevadas - como el montón no puede
fragmentarse (no se puede liberar un espacio del medio del montón, sólo puede
agrandarse o achicarse), esos objetos mantienen la memoria del medio reservada
para Python. Python puede reusarla, pero el resto del sistema operativo no.

Eso daña el caché de disco, daña otros procesos (capaz otros procesos Python,
en un webserver puede suceder que tengamos más de un worker corriendo python),
daña la performance general del sistema.

Adivinen quiénes tienen la costumbre de dejar objetos vivos en altas direcciones
de memoria...

...así es. Las listas libres. Acá, con guppy encontramos 29 objetos, probablemente
todos que están vivos gracias a alguna lista libre que los mantiene vivos. Vemos que
un par de ellos son Frames, como decía antes, los Frames causan este tipo de problemas.

Todos queremos saber cómo evitar estos problemas, así que:

Guppy tips
----------

* No dejar basura por el piso

  + Si se van a crear muchos objetos pequeños, crear los *persistentes* primero,
    y los *transientes* al final.

    - Compilar código (ej: usar eval o hacer imports) genera cadenas permanentes,
      llamadas *cadenas internadas*, así que compilar on-demand también es algo a evitar.

    - SQLAlchemy y muchas otras bibliotecas tienen cachés internos, investigar y estar
      al tanto de estas políticas.

  + Siempre que sea posible, preferir pocos objetos grandes a muchos objetos pequeños:

    - Listas de strings → strings separados por comas. O pipes. O enter. O lo que sea.

    - Listas de números → ``array.array`` o ``numpy.array``

* Barrer de vez en cuando

  + Si se mantienen caches con expiración, limpiar el caché regularmente para quitar elementos expirados

  + A veces se puede “desfragmentar” la memoria, reconstruyendo estructuras persistentes como los cachés

    **De hecho**, el garbage collector de java hace esto automáticamente, y muchos proyectos buscan implementar
    un garbage collector similar para Python, pero la API de extensión de Python, la Python/C, lo hace difícil
    al permitir punteros directos a los PyObject, estructuras que representan los objetos en python)*.


* El cambio es bueno

  + No crear estructuras eternas.

  + Los caches siempre expiran.

  + Los threads se renuevan.

* La casa es para vivirla, la oficina es para trabajar

  + Siempre que sea posible, realizar tareas intensivas en memoria en un subproceso, que al terminar libera la memoria y deja todo limpito y ordenado. 

  + El subproceso es la oficina, ahí se trabaja.

  + El proceso padre es mi casa, ahí se vive.


Links útiles
------------

* **Los slides**: http://python.org.ar/pyar/Charlas#Depuraci.2BAPM-n_y_defragmentaci.2BAPM-n_de_memoria_en_Python

* **Cómo mapear memoria**: http://python.org.ar/pyar/MapeandoMemoria

* **Heapy**: http://guppy-pe.sourceforge.net/

