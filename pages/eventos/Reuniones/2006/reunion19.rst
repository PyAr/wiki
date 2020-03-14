
Reunión 19, "La internacional" - 10/11/2006 - La Casa del Queso - A la salida de CaFeCONF
=========================================================================================

¿Dónde?
~~~~~~~

`La Casa del Queso`_, Av. Corrientes 3587, entre Billinghurst y Sánchez de Bustamante, Cap. Fed. Estaríamos, en la parte del primer piso.

**¿Cuando?** A la salida de CafeConf_, o sea, de 19:30hs (gmt-3), aproximadamente, en adelante.

La reunion internacional despues de cafeconf estuvo buenisima, porque vinieron Anna Ravenscroft y Alex Martelli, ademas de que hubo gente de todo PyAr_.

Rompimos nuevamente el record de asistencia, asi fue. (segun disposición en la mesa, usen la imaginacion que no tengo scanner)

.. csv-table::

    Roberto Allende,Tabla con Fiambre,None
    Santiago Peresón (yaco),"Jarra de birra, centro de operaciones federal",Carlos Navarro
    Mariano Draghi (chaghi),Una Panera,Kaufmann Manuel
    Carlos G. Alvarez,Un jugo de naranja y una birra,JohnLenton
    NubIs,Una tabla de quesos que eligio alex,Alex Martelli
    Alecu,Los condimentos para la tabla de quesos,Anna Ravenscroft
    Juan Colome (joksnet),<-este es re joven (este es facundo->),FacundoBatista
    Tenuki,Una jarrota de birra y Unos vinos,LucioTorre
    Guillermo González,otra panera,PabloZiliani
    Tom H. Hiplam ?,Tabla con fiambre bis,Matt Dorn
    None,Ricardo Kirkner,el vacío a la derecha de Ricardo

Fuimos a 'La Casa del queso' (aun no supero la decepción, yo me esperaba algo como esto http://www.thescreamonline.com/strange/strange2-1/index.html). Que manera de haber quesos. Al ser tantos en la reunión, se hablo de todo en distintos grupos, asi que solo voy a poner las perlitas de Alex y Anna que es lo que nos da mas rating.

De que hablo Alex:

En cuanto a Map, Reduce and Filter: No le gustan porque te hacen enfocar unicamente en la reduccion, el mapeo o el filtro, en vez de pensar en la transformacion que se le hace a una lista por completo. Puede llegar a perdonar map en algun caso, pero en general que desaparezcan no le molesta, ya que prefiere usar generator comprehensions. (y quien no :P)

Refiriendose a twisted: No usan twisted en google, pero seguro por una cuestion politica, twisted usa el mismo concepto que la solucion que usan actualmente en google, que esta escrita en c++ para los curiosos.

En cuanto a los lenguajes en Google: En google usan muchos lenguajes, siempre investigan tecnologias nuevas entonces hacen pruebas piloto con muchos lenguajes, y la idea en general es que si consiguen un buen programador que programa en algun lenguaje (asi sea java), lo dejan que labure en lo que le gusta. En particular los sectores que lidera alex usan mas bien c++ y python. Prefieren C++ para cuando necesitan un manejo puntual de la memoria. En java no pueden, en python hasta ahi, por eso lo hacen en c++. En los volumenes de google, con clusters de clusters de servidores, lo que se ahorran en memoria es bastante dinero, y en cierto modo tambien es mas ecologico :P. Quien lo hubiera dicho, el ahorro de memoria es bueno para el medio ambiente.

En cuanto a su trabajo en google: El puesto de Alex en Google es 'Uber Technical Lead' (alto nombre, son grosos en google, hasta tienen tarjetitas con relieve), Basicamente se encarga de organizar a otros lideres y obviamente Codear. Un 75% de su tiempo lo pasa programando. Es muy bueno que estando en un cargo alto se encargue de estar en el campo de batalla, la experiencia que tienen en google, es que un técnico que se hace manager y pierde contacto con el dia a dia, se atrofia como técnico. El sector de alex se encarga de mantener los servidores funcionando correctamente todo el tiempo. Ya sea una conexion caida, un router que funciona mal, un disco que pincha, etc. Para eso hacen parches al kernel para que muestre mas informacion en /proc, y muchos scripts para recopilar esa informacion de cada maquina de los clusters de clusters que tienen. Tratan siempre de contribuir lo mas posible las mejoras que hacen.

Alex en cuanto a base de datos: Si, google usa MySql_, pero el hubiera preferido Postgres, muchas decisiones se tomaron antes de que entre a trabajar ahi.

De que habla Anna: Con Anna no pude hablar mucho, pero lo poco que hablamos fue divertidisimo. Actualmente esta trabajando en su tesis acerca de aprendizaje de computadoras, nos conto de un par de anecdotas graciosas, situaciones que se dan cuando estas en una clase de programacion en c++ siendo tan avocadamente pythonista. Por ejemplo, una vez un profesor pregunta 'Como ordenan una lista', a lo que Anna contesta: "List.sort", despues les mostraron distintos algoritmos para ordenar en c++. Pero segun ella, conociendo a Tim Peters, que trabaja hace muchisimo en algoritmos de ordenamiento, para que querria implementar ella su propio algoritmo en vez de usar el de Tim que esta disponible facilmente en python :). Es un claro ejemplo de alguien que aprecia como python te deja preocuparte de hacer lo que tenes que hacer en vez de pelearte con el lenguaje que estas usando.

Eso fue mas o menos todo, llegado el momento cada uno taza taza se fue a su casa alguno seguro a caraza, ojala no los haya atacado la inseguridad a los que iban en subte para el lado de constitucion porque se pone denso a esa hora. Gracias por estar a todos los que estuvieron, y los que no pudieron venir, la proxima sera!

saludos.

.. ############################################################################

.. _La Casa del Queso: http://www.lacasadelqueso.com.ar/

.. _pyar: /pyar
