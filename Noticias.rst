#acl AdminGroup:admin,read,write,delete,revert ReadWriteGroup:read,write All:read 
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

==== 02/09/2012 ====

El 15 de septiembre se llevará a cabo el encuentro '''Nea Extends''' en Formosa.

El '''Nea Extends''' es un evento llevado adelante por programadores independientes, que desean dar a conocer las bondades, ventajas, y herramientas disponibles para los diferentes lenguajes de programación utilizados actualmente. Cómo aprovecharlos y cómo convertirlos en fuente de trabajo a través de la experiencia vivida por cada uno. 

Para conocer a los disertantes, más información sobre el evento e inscripción: [[http://neaextends.net/|Página oficial de NeaExtends]]. 


==== 31/08/2012 ====

Desde el 25 de agosto se puso para su descarga '''Python 3.3.0 RC1'''. La lista de novedades es muy amplia, e incluye desde entornos virtuales soportados en el core, paquete namespaces y algunas mejoras para facilitar el pasaje de 2.x a 3.x

Los enlaces importantes son:
 * [[http://docs.python.org/dev/whatsnew/3.3.html|Listado con las novedades]]. 
 * [[http://www.python.org/download/releases/3.3.0/|Enlace para descargarlo]].
 
==== 31/08/2012 ====
El día 15 de Septiembre se llevará a cabo un PyDay en Córdoba, enteraté más del evento accediendo a [[http://www.pydaycba.com.ar/|PyDay 2012 Córdoba]].

El [[http://www.pydaycba.com.ar/schedule|programa de charlas]] se encuentra disponible. La [[http://www.pydaycba.com.ar/register|inscripción]] es libre y gratuita!

==== 07/05/2012 ====

Python Argentina se enorgullece de anunciar que está abierto el período de recepción de propuestas para [[http://ar.pycon.org/2012|PyCon Argentina 2012]], con fecha límite '''30 de Junio de 2012'''. Más información e instrucciones para envío, [[http://ar.pycon.org/2012/conference/proposals|aquí]].

##irss stop
## ULTIMAS_END
== Anteriores ==
 * [[Noticias/2011 |Año 2011]]
 * [[Noticias/2010 |Año 2010]]
 * [[Noticias/2009 |Año 2009]]
 * [[Noticias/2008 |Año 2008]]
 * [[Noticias/2007 |Año 2007]]
 * [[Noticias/2006 |Año 2006]]
 * [[Noticias/2005 |Año 2005]]
 * [[Noticias/2004 |Año 2004]]
