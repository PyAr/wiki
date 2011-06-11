#acl AdminGroup:admin,read,write,delete,revert ToqueTones:read,write All:read 
## Las noticias se agregan acá. Mantener un orden cronológico descendente.
## Cuando el texto de la noticia es suficientemente amplio, crear una nueva página con el detalle de la noticia como una sub-página de ésta.
##
## Muchas veces en esta página escribimos los links de manera que queden más descriptivos (y no tan wikis),
## ya que esta info se ve en la página de inicio
##
## Los comentarios irss son interpretados por la macro que arma el feed de noticias. Deberían quedar fijos: el start inmediatamente
## después del link (junto con el tópico y la descripción del feed), y el stop al final de la página.
##
## Los comentarios ULTIMAS_{START|END} marcan el From/To para hacer el import en la página Inicio.
## El primero debería quedar fijo, inmediatamente antes de la primer fecha. El otro, es responsabilidad de quien
## edite esta página irlo "subiendo", de manera que la página inicial solo contenga las últimas noticias.
#language es
= Noticias =
## El link al RSS está deshabilitado porque tiene problemas con Python 2.3 :(
## ''Suscribite al feed de noticias haciendo click aquí:''  [[IRSS]]
##irss start
##irss topic PyAr - Python Argentina
##irss descr Últimas noticias
## ULTIMAS_START

==== 11/06/2011 ====

Se encuentra abierta la inscripción para el evento 
[[http://www.pyday.com.ar/catan2011 | PyDay Gonzalez Catán 2011: "Jornada de Programación en Python"]] 
a realizarse el sábado '''16 de Julio de 2011''' de '''9 a 19hs''' en el 
[[http://www.institutopascal.edu.ar/ | Instituto Superior Tecnológico Blaise Pascal]], 
que contará con Charlas Introductorias, Talleres Prácticos y espacios abiertos 
([[http://www.pyday.com.ar/catan2011/conference/schedule | ver Agenda]]).

Entrada libre y gratuita previa [[http://www.pyday.com.ar/catan2011/user/register | inscripción web]] (cupos limitados)
Se entregan certificados sin cargo.


==== 28/03/2011 ====

Se terminó el PyCamp 2011, los proyectos en los que trabajamos estan [[PyCamp/2011/ProyectosLaburados | acá]]

==== 13/03/2011 ====

Falta muy poco para el PyCamp 2011 ¿Que esperas para inscribirte? [[PyCamp/2011 |Mas info...]]

==== 10/02/2011 ====

Nos llega de Brasil una pésima noticia: falleció Dorneles Tremea, presidente de la Asociación de Python Brasil, y una gran persona. Más información [[http://associacao.python.org.br/associacao/imprensa/noticias/associacao-python-brasil-esta-em-luto|aquí]].

##irss stop
## ULTIMAS_END
== Anteriores ==
 * [[Noticias/2010 |Año 2010]]
 * [[Noticias/2009 |Año 2009]]
 * [[Noticias/2008 |Año 2008]]
 * [[Noticias/2007 |Año 2007]]
 * [[Noticias/2006 |Año 2006]]
 * [[Noticias/2005 |Año 2005]]
 * [[Noticias/2004 |Año 2004]]
