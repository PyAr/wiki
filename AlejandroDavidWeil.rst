##master-page:HomepageTemplate
#format wiki
== alejandro david weil ==
Email: mi nick en gmail.

Programo en Python desde, aproximadamente, el 2004.

Uno de mis pasatiempos (cuando tengo tiempo para pasar) es [http://imfish.sf.net/ IMFish] un cliente de mensajeria instantanea que se me ocurrio hacer luego de ver y usar [http://freshmeat.net/projects/wmfishtime/ WMFishTime]. Funciona con msn, jabber e icq. Sin embargo aun esta en version beta y es '''inusable''' (si uno no lee el readme, etc). La unica version compil, perdon, empaquetada, es medio vieja ya en comparacion con las cosas que hay en el cvs, sin embargo, la version del cvs no esta funcional en este momento.
Para el futuro, hay varios interrogantes/posibilidades:

 1. Sacar icq. (no encontre una lib que funcione bien completamente hecha en python, si alguien sabe de alguna o quiere hacerla, es bienvenido!, Una opcion seria ver la version de oscar que tiene [http://twistedmatrix.com/trac/ Twisted]. En principio no me gustaria incluir twisted como dependencia, pero quien sabe. De cualquier manera, creo que es mucho mejor soportar bien jabber y soporte basico de msn, esa me parece la prioridad. Cabe mencionar que la version beta disponible utiliza el cliente de icq [http://ysmv7.sourceforge.net/ YSM] hecho por Raddy.

 1. Decidir si seguir con Gtk (o Gnome). Gtk me gusta bastante, me gusta que tiene buen soporte de svg, y que tienen layers cercanos al X como para aprovechar en un futuro las extensiones de X para svg por ejemplo. Sin embargo, el problema para mi, es que no tiene soporte nativo en mac os x, y el proyecto que hay al respecto, por ahora, requiere la version tiger del mismo. Otra desventaja, es que si bien uno puede aprovechar layers cercanos al X para utilizar features especiales del mismo, eso puede ser una desventaja (debido a que no funcione) en m$ window$ y/o mac os x. Entonces la pregunta es, es posible hacer algo que intente exprimir bastantes features graficos y multiplataforma al mismo tiempo?  Una posibilidad al respecto seria utilizar [http://www.pygame.org PyGame], sin embargo, me gustaria no hacer todo absolutamente grafico, sino tener menues y ventanas de dialogo para algunas cosas, y eso lo veo aun medio verde. En fin.. se escuchan sugerencias.

 1. Hacer animaciones de los sprites. Eso ya esta en el cvs.


Para el soporte de msn, utilizo la [http://auriga.wearlab.de/~alb/msnlib/ msnlib] de Alberto Bertogli. Sin embargo, esta no poseia soporte de proxy http y yo estaba interesado en eso, asi que hice un patch para lograrlo. Para ello, arme una libreria de http ''a-la'' httplib, pero asincronica, [http://ahttplib.sf.net ahttplib]. Aunque funciona, no me parece que haya quedado muy prolija, y creo que en aquel momento no entendia bien (o al menos, ahora entiendo un poco mejor) asyncore (la libreria de red asyncronica (por ahora standard) de python. Asi que ultimamente me dedique un poco a emprolijarla.

 








----
 La página[wiki:PythonInfo:Audioincluye Audio] incluye varioas grabaciones de charlas acerca de python, es un link interesante.

----
 CategoryHomepage
