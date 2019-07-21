Introducción a Django
---------------------

.. image:: imgs/fisa.jpg 
    :align: center

La charla original se llamaba "Mini Introducción a Django", pero resultó que
la versión escrita no es tan "mini".

.. image:: imgs/django1.png
    :align: center

Bien, ¿qué es Django? En pocas palabras: es un framework de desarrollo web. Es
decir, un conjunto de bibliotecas y herramientas que nos van a permitir crear
sitios web.
Como ya se deben imaginar, está hecho en Python y por tanto también será Python
(con todas sus bondades) el lenguaje que utilicemos para crear nuestros sitios.

Django es software libre, con lo que tenemos acceso a su código fuente para 
aprender, entender, ayudar a mejorarlo, etc. Y además goza de una comunidad muy 
grande y activa, lo que ayuda a que se mantenga actualizado, se detecten y 
corrijan sus errores, tenga documentación actualizada y detallada, y algunas 
otras ventajas que después vamos a ver (spoiler: muchas aplicaciones útiles ya 
hechas!).

Además, es bueno saber que Django tiene una filosofía muy definida,
influenciada por el ambiente donde nació. Los creadores originales de Django 
trabajaban haciendo sitios para empresas de noticias, donde muchas veces se 
requerían cambios en cuestiones de días o horas. Y como se trataba de un grupo 
de desarrolladores "perfeccionistas", el desafío era llegar a las apretadas 
fechas de entrega pero escribiendo código de manera correcta, y no haciendo 
"chanchadas" para que las cosas salieran rápido.

De allí que se dice que Django es "el framework web para perfeccionistas con
fechas de entrega". Django espera facilitarnos la tarea de desarrollo, pero
ayudándonos a la vez a escribir buen código.

Y finalmente es un framework que intenta ser flexible, no interponiéndose entre 
el desarrollador y lo que quiere conseguir. Por ello es muy sencillo reemplazar
algunas partes que no nos gustan de Django, con otras que nos gusten o sirvan 
más.

Hecha la Introducción (y si no se aburrieron y dejaron ya de leer), vamos a
conocer a Django.

Lo primero importante a saber es cómo Django nos propone estructurar nuestros
sitios:

.. image:: imgs/django2.png
    :align: center

En Django vamos a tener Proyectos y Aplicaciones:


* Proyecto: va a contener la configuración general de nuestro sitio (cosas como la base de datos, email de los admins, etc.), y un conjunto de aplicaciones.
* Aplicaciones: van a ser las que tengan la funcionalidad en sí de nuestro sitio (por ejemplo, la lógica para encontrar la foto del perrito más votado de la semana).

Algo interesante es que Django nos alienta a que las aplicaciones sean lo más
desacopladas posibles, de forma de que una misma aplicación pueda reutilizarse
en más de un proyecto.

Django mismo ya nos trae muchas aplicaciones útiles para cosas comunes del
desarrollo web, como la autenticación de usuarios o la administración del
contenido del sitio. Y como Django tiene una comunidad muy grande (y humilde, 
como verán), también podemos encontrar muchas aplicaciones de terceros para 
reutilizar y modificar.

Hay aplicaciones que nos ayudan durante el desarrollo (para logging, debug, 
etc.), aplicaciones para agregar funcionalidad a nuestro sitio (tagging,
registración, etc.) y aplicaciones ya armadas que podemos poner directamente en
producción (como blogs, CMS, etc.).

.. image:: imgs/django3.png
    :align: center

Ahora bien, ¿cómo es una aplicación?

Para nuestras aplicaciones Django nos propone seguir la arquitectura MVC 
("Modelo-Vista-Controlador"). Para quienes no lo hayan escuchado antes, MVC no
es un invento de Django, sino una arquitectura bien difundida que nos propone
separar nuestras aplicaciones en tres partes:

* Los Modelos: la parte de nuestra aplicación que define la estructura de la base de datos y se encarga de la comunicación con ella.

* Las Vistas: la interfaz del usuario, con el código que elije qué datos pedirle o mostrarle en cada momento.

* Los Controladores: la parte de la aplicación que elije qué vistas ejecutar en respuesta a las acciones o peticiones del usuario.

Los modelos van a ser clases que representen las cosas que queremos almacenar
en la base de datos. Ejemplo: clase Cliente, clase Noticia, etc.

Las vistas van a ser funciones normales de Python, que van a devolver el 
contenido que debe ser entregado al usuario (página web, imágen, etc.). Ejemplo:
la vista "pagina_de_inicio".

Y para los controladores, nosotros sólo vamos a tener que definir qué función
(vista) debe ser llamada para cada url. Ejemplo: "cuando el usuario pida la url
http://misitio.com/inicio/, ejecutar la vista pagina_de_inicio".

Django se encarga en gran parte de los controladores, y nos provee de
herramientas para facilitarnos el desarrollo de las vistas y los modelos.

Vamos a hecharle una mirada a eso...

El paquete de Django trae...
----------------------------

.. image:: imgs/django4.png
    :align: center

La primer herramienta que nos da Django es un ORM (un "mapeador 
objeto-relacional"). El ORM va a ser el que nos permita interactuar con la base
de datos, y por lo tanto va a ser una de las dos cosas que más vamos a usar
comúnmente (así que presten atención, esto es como esos temas que seguro entran
en el examen).

Como nosotros programamos con orientación a objetos, lo que vamos a definir y 
usar son clases. Y como las bases de datos más comunes son relacionales, Django
se va a encargar de traducir nuestras operaciones sobre objetos, en sentencias
SQL que se van a ejecutar sobre tablas de la base de datos.

Por ejemplo: definimos nuestra clase Usuario, con varias propiedades (nombre,
dirección, email, etc.). Luego podemos hacer cosas como crear instancias de
Usuario, ingresar valores en sus propiedades, y decirle "che, guardate!", y
Django automágicamente va a armar una sentencia SQL de insert o update según
necesite, y la va a ejecutar en la base de datos.

[ya que estamos: la aplicación de autenticación que trae Django ya tiene una 
clase User que podemos aprovechar :)]

.. image:: imgs/django5.png
    :align: center

Ya podemos entonces escribir código que lea y guarde cosas en la base de datos,
pero eso al usuario no le sirve de mucho. Hay que mostrarle algo. Así que la
segunda herramienta que más vamos a utilizar es el sistema de plantillas. 

¿Qué es el sistema de plantillas? Es lo que nos va a permitir "injertar" 
nuestros datos dentro de plantillas html (o xml, o atom, ...) que nosotros
definamos.

Es decir, vamos a armar nuestro html que esperamos que el usuario vea en su
navegador, y dentro del html diremos cosas como "acá tiene que aparecer el
nombre del cliente actual".

El lenguaje de templates (plantillas) además nos permite poner un poco de
lógica básica al código html, como ciclos, condiciones, o incluso una especie
de herencia de plantillas.

.. image:: imgs/django6.png
    :align: center

Y hay un número de herramientas extras que también usaremos mucho en nuestros 
sitios al desarrollar con Django. Siempre es bueno conocerlas para no
andar "reinventando la rueda", ya que además se trata de herramientas que han
sido pulidas por las necesidades y uso de mucha gente.

Si algo huele a "esto lo debe hacer mucha gente", entonces es probable que
Django tenga alguna herramienta para facilitar la tarea. Si no la tiene,
también es probable que alguien la haya desarrollado como una aplicación. Y si
tampoco existe como aplicación, genial! ya descubriste algo con lo cual 
contribuir :)

.. image:: imgs/django7.png
    :align: center

Hasta ahora las herramientas que estuvimos viendo son cosas que utilizaremos
más que nada mientras programemos. Cosas que vamos a usar dentro de nuestro
código. Pero Django también trae algunas utilidades para facilitar algunas
tareas más allá de la codificación.

El servidor de desarrollo nos permitirá ejecutar nuestro sitio web desde el
entorno de desarrollo mismo, sin necesidad de configurar un servidor web para
ello ni estar haciendo deploys para probar cada cambio que hagamos.

La consola de Django nos permite ejecutar código en una consola interactiva de
Python, pero como si fuese nuestro sitio ejecutándose en el servidor. Podemos
usarla por ejemplo para interactuar con la base de datos pero con nuestros 
modelos.

Y el modo de debug, que nos permite ver muchísima información de los errores en
la ejecución del código de nuestro sitio. Teniendo el debug activado, frente
a un error podemos ver el código que lo generó, las variables que había en 
memoria en ese momento y sus valores, los parámetros GET y POST recibidos, la 
configuración actual del sitio, el stack trace de la excepción de Python, etc.
Para quienes han trabajado en desarrollo web, saben bien lo que esto vale, ya
que es algo que generalmente no poseemos.

.. image:: imgs/django8.png
    :align: center

Y como postre de esta lista de herramientas y utilidades, tenemos al Admin de
Django.

Django Admin es una aplicación que viene incorporada, y que nos ahorra una
cantidad impresionante de trabajo. Sí, ya se que suena medio fanático y
exagerado, pero es bastante realista lo que dije.

Recordemos que en nuestras aplicaciones podíamos definir modelos. Es decir,
clases que representaban las cosas que almacenábamos en la base de datos (clase
Usuario, clase Noticia, clase Comentario, etc.).

En los modelos ya definimos todo lo necesario para poder luego operar con esas
entidades en la base de datos, crear nuevas, buscar, guardar, modificar, etc.
Entonces, ¿qué nos falta para tener una aplicación que nos permita administrar 
el contenido de la base de datos? Las pantallas (páginas), lógicamente.

Bueno, el admin de django es precisamente eso. Simplemente le decimos algo
como "che, admin! mirá, acá yo dije que tenia clientes en la base de datos, ¿no
me mostrás un ABM de clientes?". Y el admin nos muestra un ABM de clientes. Así
de sencillo (si no lo creen, pueden ver el código en el tutorial de Django).

[ABM (o CRUD en inglés) es una aplicación que permita hacer Altas, Bajas y 
Modificaciones (Create, Read, Update, Delete, en inglés)]

Incluso podemos personalizar la manera en que esos ABM se muestran, con cosas
como mostrar filtros por los campos que queramos, decidir que columnas mostrar
en las listas, cómo mostrar los campos en la edición, etc.

Esta aplicación nos sirve a nosotros desarrolladores durante la creación del
sitio, para cargar contenido y ver "cómo iría quedando". También nos sirve luego
en producción, para los administradores o moderadores del sitio. Pero también 
le puede servir a nuestro usuario final, dependiendo del caso.

Cada vez que veo el admin, me da lástima recordar las horas que dediqué a 
programar ABMs que no eran ni un cuarto de lo configurables que son en Django :)

Haciendo funcionar las partes
-----------------------------

Bueno, ya recorrimos una cantidad interesante de las cosas que Django tiene. La
pregunta ahora es: ¿Cómo se engancha y funciona todo esto?

.. image:: imgs/django9.png
    :align: center

Es más simple de lo que parece:

1. El usuario pide una url ("quiero entrar a http://noticias.com/policiales, y
que sea rápido!")

2. Django se da cuenta de que para responder a esa url, tiene que llamar a una
función (una *vista* de ahora en más). Como se imaginan, la llama.

3. En nuestra vista (función "policiales" en el ejemplo), leemos todas las
noticias de la base de datos que tengan la categoría policial.

4. Finalmente nuestra vista le dice a Django que le devuelva al usuario un
template determinado (en este caso el html de la página de policiales),
pero utilizando dentro del template los datos que nosotros le pasamos.

Hasta aquí tenemos una idea global del funcionamiento y la manera de trabajar de 
Django, pero todo esto puede entenderse mucho mejor si lo vemos con código. Por
ese motivo es que les recomiendo ir al tutorial oficial de Django, que pueden
encontrar en http://docs.djangoproject.com/en/dev/intro/tutorial01/

En el tutorial pueden ver cómo construir una aplicación sencilla desde cero, y
con lo leído en este artículo, seguramente les será más sencillo entender lo que
vayan haciendo en su transcurso.

Y si no les es más sencillo, siempre tienen mi mail para quejarse :)

