#acl Known:read,write All:read
#language es
= Reunión 34 - Miércoles 03/12/2008 - Bar "El Imaginario Cultural", Buenos Aires - 19:30hs =

Bienvenidos a todos a la minuta de la reunión número 34 de Pyar!
Debajo encontrarán respuestas para algunas preguntas que tal vez ronden sus mentes, si las mismas no cuadran con lo que uds. percibieron, háganmelo saber y sincronizamos pensamientos...
Ojalá la disfruten!

== ¿Tomaron lista? ==

''' Los asistentes en orden de relevamiento y/o llegada: '''
|| Mauro NN (aka "LavaLaMano") (1st Time) ||
|| TomasZulberti ||
|| SebastianMaceda ||
|| AlejandroJCura (aka "Alecu") ||
|| LeitoMonk ||
|| NubIs ||
|| RicardoKirkner (aka "Sr. Presidente")||
|| MarceloFernández ||
|| GabrielBrunacci (1st Time) ||
|| HectorSanchez (aka "Karucha") ||
|| LucasDevescovi (aka "LucasMetal") <-- It's me!! ||
|| MarianoReingart ||
|| MarianoDraghi (aka "cHagHi") ||
|| GonzaloLarralde (1st Time) ||
|| RicardoAraoz (1st Time) ||
|| SebastianBassi ||
|| AlejandroDavidWeil (aka "Tenuki") ||
|| ManuelMuradas (aka "Dieresys") (1st Time) ||
|| PabloZiliani (aka "PabloZ") ||
|| DiegoMascialino (1st Time)||
|| RobertoAlsina ||
|| FacundoBatista ||

''' Los desertores (los que se anotaron y no aparecieron :( ): '''
|| EzequielChan ||
|| RenzoCarbonara (aka "k0001") ||
|| AlbertoPaparelli ||
|| NicoEchaniz ||

== ¿Dónde ocurrió el hecho? ==

Esta parte de la historia arrancó tristemente, pero tuvo final feliz :).

Resulta que nos reunimos en el bar [http://www.imaginariocultural.com.ar/ El Imaginario Cultural], Bulnes y Guardia Vieja, Almagro, Ciudad de Buenos Aires, a las 19:00hs aprox. Esperamos en la vereda hasta que la masa de gente leudó, y entonces nos metimos al bar. Ahí surgió una extraña conversación con la mesera, algo tipo:
 * - PyAr: Somos muchos ¿Podemos poner las mesas en forma de L?
 * - Mesera: No.
 * - PyAr: ok. ¿Nos podrás bajar un poquito la música en este sector?
 * - Mesera: No.
 * - PyAr: mmm, ok. ¿Podemos ir al patio entonces?
 * - Mesera: No. No se puede armar una mesa tan grande en el patio.
 * - PyAr: Nos podemos ir a la m... también, no?
 * - Mesera: Esto es todo lo que puedo ofrecerte.
 
Y después de elegir una cerveza X y tomar una cerveza Y porque era lo único que tenían, esperamos un rato al resto de la gente, e indignados nos ubicamos nuevamente en la vereda. Ahí, gracias a Mariano "La hormiga exploradora" Reingart, caíamos a las 21hs aprox. en una pizzería llamada "Pachi", ubicada en [http://www.openstreetmap.org/?lat=-34.60065&lon=-58.42047&zoom=15&layers=B000FTF Guardia Vieja y Medrano], donde nos quedamos el resto de la noche atendidos realmente muy bien!!

Faltaría agradecer a GonzaloLarralde, cuyo mail enviado al partir de "El Imaginario Cultural" le permitió a DiegoMascialino llegar al nuevo bar! 

== ¿De qué se habló? ==

''' [http://www.nsis.com.ar/public/wiki/PyReplicaEs PyReplica] y experiencia del [http://www.postgres-arg.org/ 1º PgDay en BsAs]  '''

MarianoReingart nos contó sobre el primer PostgresDay en Argentina. El mismo se llevó a cabo en la Asociación de Programadores de Congreso, el 22 de Noviembre del corriente. Parece que salió muy bien ya que vino gente de Brasil, Venezuela y USA, y si bien eran 30 personas nada más, para una primera reunión es un número más que interesante!
Mariano ayudó en la organización y también dió una de las cuatro charlas, la referida a [http://www.nsis.com.ar/public/wiki/PyReplicaEs PyReplica], que según la definición de su wiki:

''"PyReplica es un replicador asincrónico maestro-esclavo simple para PostgreSQL basado en Python, usando un disparador maestro en plpython, señales, secuencias, y un script cliente en python (influenciado por slony & londiste, pero mucho más simple y fácil)."''

También nos repartió pins! :)

''' Python y los Servicios Web de [http://www.nsis.com.ar/public/wiki/FacturaElectronica Factura Electrónica] (AFIP), interfases con otros lenguajes, SIAP libre... ([http://www.nsis.com.ar/public/wiki/PyAfip PyAfip]) '''

Luego MarianoReingart paso a explicar la problemática de las grandes empresas, que al ser autoimpresoras de sus facturas deben solicitar por Internet la autorización de emisión pertinente (CAE: Código de Autorización Electrónica) a la AFIP, mediante un WebService o la Web directamente, como se explica [http://www.afip.gov.ar/eFactura/ aquí]. 
Con el paso del tiempo más y más rubros están siendo obligados a adoptar esta forma de operación, por eso para poder realizar esto desde programas escritos en Python, MarianoReingart y MarceloAlaniz desarrollaron [http://www.nsis.com.ar/public/wiki/PyAfipWs PyAfipWs], que según su wiki:

''"PyAfipWs es una interface COM (automatización) a los Servicios Web de la AFIP (web services de autenticación y factura electrónica), utiliza software libre desarrollado en Python y funciona con cualquier lenguaje compatible que pueda crear objetos COM en Windows (Visual Basic, ASP, Fox Pro, Delphi, .Net, Java, etc.)."''

Creo muy piola el hecho de poder, mediante esta interfase, emitir facturas electrónicas desde programas desarrollados en lenguajes viejos.

También se charlo sobre el trabajo en conjunto con MarianoMara para el desarrollo de [http://www.nsis.com.ar/public/wiki/SiaPy SiaPy], que es un prototipo (multiplataforma :) ) de un sistema similar al [http://www.afip.gov.ar/genericos/emisorasGarantias/siap_main.asp SIAP] de la AFIP: un software para generar declaraciones juradas, que sólo corre en Windows :( .

Finalmente Mariano mencionó la interesante posibilidad de donar el código fuente de PyAfipWs a la comunidad de Pyar y que los ingresos se utilicen en pos de expandir Python el la Argentina. Grande Mariano! Veremos que pasa...

''' Organizando PyCon Argentina 2009 '''

Durante la [http://www.python.com.ar/moin/Eventos/Reuniones/Reunion29 última reunión de PyAr en Santa Fé] se anunció, y durante la vuelta del viaje algunos participaron de un brainstorming, para dar vida a PyCon Argentina 2009! Sí!! la versión con choriceada y dulce de leche de [http://www.python.org/community/pycon/ PyCon].

FacundoBatista mencionó los temas críticos y aquellos urgentes para la organización de la misma, los interesados en colaborar puede registrarse en la [http://trac.usla.org.ar/proyectos/pycon-ar/login Wiki de PyCon Argentina].

'''Temas Críticos'''

 * Difusión
 * Apoyo y Sponsors
 * Disertantes
 * Manejo de charlas y disertantes: Alojamiento de gente del exterior, seguridad, etc.
 * Elección de fecha: No pisarse con otros eventos (ej: WikiMedia, PyCon Brasil, Regionales de SL, PostgresDay)
 * Infraestructura: Sitio Web, etc.
 * Edificio: Varios temas (ej: Ver si hay enchufes en las aulas, etc.).
 * Durante la conferencia: Varios temas (ej: alquiler de handies, registración, etc.).
 
'''Temas Urgentes'''
 
  * Lista de Correo: Crear y avisar para que se suscriban todos los interesados.
  * Roles de Asistencia: Repartición de Tareas (mediante la Wiki).
  * Comité de Selección de Charlas: Grupo de personas que definan las reglas para seleccionar charlas (ej: Lightning Talks, etc.)
  * Colaboración en el día de la conferencia: Gente a cargo de los alargues, aulas, pisos, cel. de los disertantes, etc.).
  * Estructura Organizativa General: Ver si es una estructura plana, o jerarquizada, etc.
  * Fecha y duración de la conferencia: 2 o 3 días, Qué días? (ej: Jueves, Viernes y Sábado, o Viernes, Sábado y Domingo)
  * Cantidad de gente esperada: Gente de Santa Fé, Córdoba. Organización de viajes desde el interior para abaratar costos de personas del interior, etc.
  * Tracks, Gente y Charlas: 
    * Encontrar equilibrio entre charlas de Django, Turbogears, Newbies, etc. 
    * Cuantos medios días queremos darle a cada tema? 
    * Qué temas? 
    * Cuantos tracks disponibles (2 tracks vs. 4 tracks, según cuanta gente esperamos)? 
    * Cuantas charlas tenemos?   
  * Capital Requerido: Cálculo de presupuesto (sponsors, infraestructura, se cobrará entrada?, etc.).
  * Habrá sprints?

''' Sorteo de una remera Slashdot (aniversario 10 años) '''

Hacia el final de la reunión, gracias a una donación de SebastianBassi y mediante complejos algoritmos matemáticos, ejecutados en diversos dispositivos de alta tecnología como notebooks, iPhones, zapatófonos, iPods, relojes cucú, etc. se obtuvo un simple número de dos cifras. El mismo fue utilizado como índice para acceder a un array de nombres, en cuya posición número 13 alojaba el string "GonzaloLarralde"!!! Felicitaciones Gonzalo por la hermosa remera!

''' The End '''

Como pudimos; algunos con sus sistemas al 100%, algunos arruinados rippeando Dvds en una XT, otros en piloto automático, pero todos toditos, tuvimos que partir, sip, snif snif :(.
Después de una noche en donde desfilaron muchas cervezas, acompañadas de muchas pizzas, y donde la amistad le empató al bit, con una gran sonrisa en nuestras caras todos nos dimos un gran abrazo y partimos hacía nuestros bunkers informáticos (que algunos llaman "hogar").

Espero que todos la hayan pasado igual de bien que yo asistiendo a la reunión, y que se hayan divertido leyendo la minuta tanto como yo escribiéndola!!

Abrazos para todos!!!!!!!!



 
 
 
 
 
