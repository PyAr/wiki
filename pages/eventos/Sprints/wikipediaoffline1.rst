
El sábado 3 de Junio de 2006, al finalizar las Jornadas de Python de Santa Fé se invitó a los participantes a un sprint informal que se organizó en uno de los bares de la ciudad con wi-fi. Y nos juntamos cerca de 20 personas (no todos con máquinas, creo que eran unas 7 notebooks).

El tema propuesto fue investigar y programar una `Wikipedia Offline`_: meter en un cd todo el contenido que se pueda de la wikipedia en español para distribuir a alumnos y escuelas que tengan al menos una pc pero no tengan acceso a internet.

Y mientras bajaba el dump en castellano empezamos a organizar las tareas.

Un grupo se encargó de armar un script para borrar del dump todas las páginas que no fueran indispensables: dado que las paginas en castellano de la wikipedia (sin imagenes) ocupan descomprimidas más de 2gb, se decidió borrar las páginas de los usuarios, los comentarios sobre los artículos, y otras páginas miscelaneas que no son los artículos en sí.

Otro grupo se encargó de investigar diversos formatos y algoritmos de compresión, para optimizar por un lado el tamaño de los textos, para dejar lugar para incorporar luego las imágenes, y por otro lado optimizar el tiempo de acceso en PCs que tengan más de un par de años.

Y otro grupo se encargó de armar un ejecutable que contiene un mini servidor web y que levanta un browser apuntado a sí mismo. Este grupo también armó un script que genera un índice a partir de un archivo comprimido, permitiendo la búsqueda de artículos.

Con la colaboración de todos los participantes se llegó a armar un prototipo que funciona y resulta muy prometedor. Fluyeron las ideas para extenderlo y distribuirlo. Fue una experiencia muy interesante, enriquecedora y sobre todo: útil.

.. ############################################################################

.. _Wikipedia Offline: https://opensvn.csie.org/traccgi/PyAr/wiki/WikipediaOffline

