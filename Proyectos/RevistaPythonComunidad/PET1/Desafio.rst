#acl JuanjoConti:read,write All:read
Esta página tiene como objetivo darle soporte al desafío planteado en el primer número de la revista PET.

Algunas aclaraciones al [[http://revista.python.org.ar/1/html/desafio.html|Enunciado original]]:

 * No se pueden usar programas externos o librerías que no estén en la stdlib.
 * En la cuenta de los caracteres se tienen en cuenta espacios en blanco,  tabulaciones y comentarios. Así que manden sus respuestas lo más cortas  posibles!
 * El número recibido es un entero >= 0.
 * Las  palabras 'entrada' y 'salida' no son parte de la entrada y salida  esperada para el programa (oscureció más de lo que aclaró)
 * La salida esperada para 0 es 0 y para 1 es 1.

= Ranking =
De esta página los participantes pueden bajar un programa que les permite validar su prorgama antes de enviarlo.

Uso: $ ./pet1-test.sh pet1-ejemplo.py

[[attachment:pet1-test|Descargar]] [[attachment:pet1-test2|Descargar]] (pet1-test2 no tiene en cuenta el stderr)

Los caracteres se cuentan con wc -c pet1-ejemplo.py

Notarán que renombré sus scripts usando su usario de mail o apellido. Si envían una nueva propuesta, háganlo usando este nombre de archivo. Los que no tengan el estado en OK, deben volver a enviar su script para que pueda ser elegible.
||'''chars''' ||<style="font-weight: bold;">script name ||'''feedback con pet1-test''' ||<style="font-weight: bold;">feedback con bignum ||
||111 ||pet1-pych3m4.py ||OK ||OK y ||
||111 ||pet1-jmansilla.py ||OK ||OK ||
||111 ||pet1-hdzos.py ||OK ||OK ||
||112 ||pet1-piranna.py ||Tiene un espacio de mas al principio de todas las salidas ||
||117 ||pet1-fpalm.py ||OK ||OK ||
||118 ||pet1-matiasg.py ||OK ||OK ||
||120 ||pet1-fheinz.py ||OK ||Falla con los casos de prueba 1048576 y mayores ||
||128 ||pet1-fisadev.py ||OK ||Tarda mucho tiempo en ejecutar con números grandes ||
||128 ||pet1-cballard.py ||OK ||Falla con los casos de prueba 1048576 y mayores ||
||129 ||pet1-nicoreba.py ||OK ||
||132 ||pet1-darni.py ||OK ||
||140 ||pet1-ivoscc.py ||OK ||
||150 ||pet1-rarmas.py ||OK ||
||153 ||pet1-matiasbellone.py ||OK ||
||154 ||pet1-sergiogragera.py ||Falla con 1024 ||
||159 ||pet1-shariff.py ||OK ||
||164 ||pet1-vegacom.py ||Falla con 1 ||
||167 ||pet1-eordano.py ||OK ||
||170 ||pet1-lechon.py ||Espacio en blanco al final de la salida ||
||176 ||pet1-casoalonso.py ||Texto extra en la entrada/salida ||
||181 ||pet1-sedivy.py ||EOFError ||
||189 ||pet1-tavotell.py ||OK ||
||191 ||pet1-listas.py ||OK ||
||191 ||pet1-listas.py ||OK ||
||201 ||pet1-sergiogragera.py ||Faltan espacios en blanco al rededor de * ||
||203 ||pet1-hpmaxi.py ||OK ||
||207 ||pet1-soy_zco.py ||OK ||
||210 ||pet1-mctpyt.py ||OK ||
||213 ||pet1-zalaka.py ||Falla con 1 ||
||228 ||pet1-volpe.py ||Texto extra en la entrada/salida ||
||230 ||pet1-volpe2.py ||Texto extra en la entrada/salida ||
||232 ||pet1-tokland.py ||OK ||
||249 ||pet1-ajzach.py ||IndexError ||
||262 ||pet1-cdipietro.py ||Texto extra en la entrada/salida ||
||325 ||pet1-cballard.py ||Falla para 0 ||
||325 ||pet1-radicaled.py ||Da salidas erroneas ||
||344 ||pet1-fanaur.py ||OK ||
||364 ||pet1-fanaur.py ||Texto extra en la entrada/salida ||
||349 ||pet1-lvidarte.py ||OK ||
||429 ||pet1-gedece.py ||No lee de la entrada estándar ||
||449 ||pet1-ramonvillalongagomez.py ||Texto extra en la entrada/salida ||
||482 ||pet1-marcolucio.py ||Espacios en blanco al rededor de ^ ||
||518 ||pet1-hpmaxi.py ||Texto extra en la entrada/salida ||
||528 ||pet1-rodrigoolmo.py ||Texto extra en la entrada/salida ||
||540 ||pet1-juanpablojuanpablo.py ||OK ||
||749 ||pet1-dmlistapython.py ||Texto extra en la entrada/salida ||
||968 ||pet1-duducosmos.py ||No produce salida ||
||1052 ||pet1-rodrigoolmo.py ||Texto extra en la entrada/salida y no funciona para 1024 ||
||1702 ||pet1-rigoni.py ||Texto extra en la entrada/salida ||




= Trampas copadas =
Escribir un enunciado es realmente difícil. Algunos abusándose de nuestra debilidad han enviado algunas entradas que se riñen con la moral y las buenas costumbres. De todas formas les damos un lugar destacado! Hasta ahora:
||*chars* ||*script name* ||*feedback con pet1-test* ||*feedback con bignum* ||
||55 ||darni ||OK ||OK ||
