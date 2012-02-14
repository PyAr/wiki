El nivel de la ensalada que se arma en la cabeza a la hora de entender Unicode hace que el tema deba explicarse una y otra vez, que se deban escribir ad infinitum posts, mails, dar chiquicientas charlas en conferencia  y tal. En un intento de darle fin (si, jua!) a semejante derroche de recursos es que escribimos esta página.

Bienvenido a La Última Página Acerca De Unicode Y Cómo Se Usa (O «cómo aprendí a dejar de preocuparme y odiar los encodings»).

Resulta que las tontas de las computadoras sólo saben pensar en función de números. Esto es todo un problema al momento de almacenar y manipular otras cosas, como los textos. Afortunadamente es posible hacer una relación entre números y cosas. 

Entonces, desde los tiempos inmemoriables las computadoras han representado los símbolos que nosotros usamos en la escritura con múmeros. Inicialmente esta asociación era evidente, pero últimamente (digamos, en los últimos 50+ años, o sea, casi toda la historia de la computación) las computadoras nos han estado engañando, pues al presentarnos resultados impresos no nos dan los números que usan internamente, sino que con la ayuda de pantallas, impresoras y otras cosillas por ahí (termiales Braille, por ejemplo), nos han estado devolviendo los símbolos a los que estamos acostumbrados: letras, dígitos, putuación y otros. Este mapeo entre símbolos y números se llama Encoding.

Todo estaría de maravillas sino fuera que Encodings hay millones. Estos mapeos fueron establecidos casi independientemente en muchas empresas y países del mundo, cada uno prácticamente con el suyo. Piensen por ejemplo en los idiomas que no usan ni siquiera como base al alfabeto latín. Así es que terminamos con cientos de Encodings llamados `'latin1'`, `'utf-8'`, `'cp-1250'` y cosas más esotéricas.

Para resolver este problema es que se inventó Unicode (cualquier semejanza con http://xkcd.com/927/ es un error de concepto; ahora explico porqué). Unicode '''no''' es un encoding, aunque se asemeja mucho. Unicode es una serie de tablas que

Ver también:

 * [[Recetario/NormalizarCaracteresUnicode]]

----
 CategoryRecetas
