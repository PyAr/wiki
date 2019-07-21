PyAfipWs: facilitando, extendiendo y liberando los Servicios Web de AFIP (Factura Electrónica y otros)
=============================================================================================================

Introducción
-------------------

PyAfipWs es una interface de software libre a los Servicios Web de la AFIP, desarrollado en Python.

Nació por el 2008 de un intercambio de mails en la lista de PyAr!, cuando con el Señor Marcelo Alaniz, consultando sobre unos problemas con Python y webservices, fuimos armando una librería que se adaptara a los requerimientos y ambientes de AFIP (que dicho sea de paso, son bastantes variados y ninguna herramienta en python funcionaba del todo)

La interfase fue "inspirada" en los ejemplos oficiales de la AFIP para PHP, ya que eran los más simples de entender y más cercanos a un lenguaje como Python. 
Había ejemplos para Java pero estaban incompletos (tienen algunas dificultades con el tema dependencias e incompatibilidades con XML/SOAP) y en .NET (que estaban más completos pero solo para Windows). 
Igualmente, para nuestro gusto, estos dos ejemplos eran bastante difíciles de seguir, generan código ("artefactos"), etc. etc.

Adicionalmente, de PHP nos inspiramos en algunas bibliotecas de manejo simple de XML y SOAP, que luego dieron lugar a su contraparte en python por parecernos sencillas e intuitivas.

Inicialmente la desarrollamos para los web services de autenticación (firma digital y demás) y factura electrónica, pero con el correr del tiempo fuimos agregando otros servicios de AFIP, como bienes de capital - bono fiscal electrónico,  facturas de exportación,  código de trazabilidad de granos, depositario fiel y los nuevos servcios para mercado interno.

El proyecto ha madurado y algunas librerías que desarrollamos o adaptamos han sido liberadas separadamente:
 * `PySimpleSoap <http://pysimplesoap.googlecode.com/>`_: para manejo simple y completo de webservices
 * `PyFPDF <http://pyfpdf.googlecode.com/>`_: para generación de PDF de manera más fácil y fluida.

Ambas han sido integradas a `web2py <http://www.web2py.com>`_ para tener un marco de trabajo completo para desarrollar aplicaciones web de gestión.

Factura electrónica en Python:
---------------------------------------------

A modo de ejemplo, vamos a mostrar un como autorizar una factura electrónica en pocas líneas.

Primero se debe solicitar un ticket de acceso (utilizando un certificado y clave privada tramitadas previamente), que nos permitirá posteriormente utilizar el servicio web de factura electrónica:

.. code-block:: python

    from pyafip.ws import wsaa
  
    # crear ticket acceso, firmarlo y llamar al ws
    tra = wsaa.create_tra()
    cms = wsaa.sign_tra(tra,"homo.crt","homo.key")
    ta_xml = call_wsaa(cms, wsaa.WSAAURL)

Detrás de escena se usa M2Crypto (que es el enlace de OpenSSL para encriptación en Python), necesario para firmar la solicitud de acceso en XML.

Del ticket de acceso extraemos el Token y Sign (usando SimpleXMLElement para analizar y convertir el XML en una estructura de objetos y datos python), que contienen los códigos de seguridad requeridos en los otros webservices:

.. code-block:: python

    # procesar el xml
    ta = SimpleXMLElement(ta_xml)  
    token = str(ta.credentials.token)
    sign = str(ta.credentials.sign)

Una vez obtenida la autenticación para acceder a los servicios web, vamos a proceder a solicitar autorización para emitir una factura electrónica. 

Para ello creamos una conexión con el servidor y llamamos remotamente al procedimiento de autorización: 

.. code-block:: python

    from pyafip.ws import wsfe
  
    # crear cliente SOAP 
    client = wsfe.SoapClient(wsfe.WSFEURL, 
          action = wsfe.SOAP_ACTION, 
          namespace = wsfe.SOAP_NS) 

    # autorizar factura electronica (obtener CAE)
    res = wsfe.aut(client, token, sign,
       CUIT =20234567393, tipo_cbte=1, punto_vta=1,
       cbt_desde=1, cbt_hasta=1,
       tipo_doc=80, nro_doc=23111111113, 
       imp_total=121, imp_neto=100, impto_liq=21)
  
    print res['cae'], res['motivo']

Si todo funciona bien, esto nos devolverá el CAE (Código de Autorización Electrónico), necesario para confeccionar la factura electrónica.

Aquí termina el tema de los webservices en python, para la generación de la factura (por ej. en PDF), envio por correo y demás, ver PyRece a continuación.

Lenguajes legados
-----------------------------

Más alla de las aplicaciones en Python, esta biblioteca es compatible con lenguajes como Visual Basic, ASP, Fox Pro, Cobol, Delphi, Genexus, PowerBuilder, PHP, .Net, Java, ABAP (SAP), etc. y cualquier lenguaje/aplicación que pueda crear objetos  `COM (automatización) <http://es.wikipedia.org/wiki/Component_Object_Model>`_  en Windows (por ej. Excel o Access). 

Esto se logra facilmente utilizando PythonCOM (parte de las extensiones win32), envolviendo una clase común de python para que pueda ser expuesta a otras aplicaciones, definiendo los métodos y atributos públicos, el nombre expuesto y demás, por ej:

.. code-block:: python

  class WSAA:
      "Interfase para el WebService de Autenticación y Autorización"
      _public_methods_ = ['CreateTRA', 'SignTRA', 'CallWSAA']
      _public_attrs_ = ['Token', 'Sign', 'Version', 'XmlResponse']
      _readonly_attrs_ = _public_attrs_
      _reg_progid_ = "WSAA"
      _reg_clsid_ = "{6268820C-8900-4AE9-8A2D-F0A1EBD4CAC5}"
    
Una vez registrado la interfaz, se la puede llamar desde cualquier otra aplicacción con esta tecnología, por ej, en Visual Basic sería:

.. code-block:: vb

    Set WSAA = CreateObject("WSAA") 
    tra = WSAA.CreateTRA() 
    cms = WSAA.SignTRA(tra, "homo.crt", "homo.key")  
    ta = WSAA.CallWSAA(cms, url)
  
    Set WSFE = CreateObject("WSFE") 
    WSFE.Token = WSAA.Token  ' setear token y sign de wsaa
    WSFE.Sign = WSAA.Sign 
    WSFE.Cuit = "3000000000" ' CUIT del emisor
 
    ok = WSFE.Conectar(url) 
 
    cae = WSFE.Aut(id, presta_serv, tipo_doc, ... 
               imp_tot_conc, imp_neto, impto_liq, ...)

En nuestro caso fue muy útil y posibilitó a muchas aplicaciones contemplar estas nuevas funcionalidades (webservices, encriptación, etc.) con modificaciones menores, que de otro modo hubieran sido muy difíciles o imposibles.


Archivos de Texto y Línea de Comandos
---------------------------------------------------------------

Si bien la interfaz COM es muy útil para aplicaciones relativamente modernas, todavía hay lenguajes o entornos de muy difícil acceso, donde prácticamente la única forma de interoperabilidad son los archivos de texto.

Viendo que lenguajes como Cobol manejan archivos con campos de longitud fija (y esto ya era soportado por el aplicativo RECE de SIAP), tomamos ese camino, que con Python fue bastante directo.

La interfaz incluye herramientas como RECE.PY y RECEX.PY que por línea de comandos reciben y procesan los archivos de entrada, guardano los resultados en archivos de salida.
Esto es controlado con un archivo de configuración (RECE.INI) que utiliza define las URL, certificados y rutas a utilizar.

PyRece: ¿SIAP libre?
-------------------------------------

La historia no termina aquí, ya que viendo algunas dificultades del Aplicativo RECE o los servicios en linea para hacer facturas electrónicas (funcionalidad limitada, demoras o complejidades, etc., sobre todo para los contribuyentes que no poseen sistema de gestión), desarrollamos un aplicativo visual (de "escritorio") para facilitar y extender las posibilidades brindadas por AFIP:

.. image:: http://www.sistemasagiles.com.ar/trac/raw-attachment/wiki/PyRece/pantalla.png
   :align: center

La interfaz del usuario es una pantalla simple pero contempla:

* Lectura de planilla de calculo CSV (en vez de archivo de ancho fijo)
* Autenticación y Autorización on-line en el momento
* Generación del PDF personalizable (textos, logos, lineas, etc.) con la imagen de la factura 
* Envio por mail del PDF a los clientes (con un breve mensaje configurable)

Todas estas funciones no están disponibles (en su conjunto) en el aplicativo o sitio web de AFIP (algunas pueden realizarse con limitaciones, pero no de una forma totalmente ágil y transparente).

Esta aplicación a su vez demuestra que PyRece es una posibilidad concreta de desarrollarlo con Python un Sistema Integrado de APlicaciones (SIAP) de software libre, en este caso como alternativa al aplicativo RECE de factura electrónica, pero hay otros casos donde se podría hacer lo mismo si los servicios web estuvieran disponibles (por ej., IVA para DD.JJ., SICOSS para seguridad social., etc.).

FE.py
------------

Por último, hemos desarrollado una herramienta que unifica los distintos webservices (factura electrónica nacional, exportación, bienes de capital, etc.) e integra todo lo expuesto anteriormente, utilizando una base de datos para almacenar e intercambiar la información, generando las facturas en PDF, pudiéndolas cargar desde y hacia archivos de texto, envío por email o FTP, entre otras cuestiones.

En general utiliza PostgreSQL, pero también se puede usar otras bases de datos (PyODBC o SqLite). 

El Proyecto
-------------------

Cerrando el artículo, incluimos algunos comentarios sobre como se desarrollo el proyecto.

Un tema resuelto fue el modelo de negocios, sobre todo conociendo que hay otras alternativas cerradas y decidimos mantenernos en el camino del software libre, encontrar la combinación justa para poder competir no fue un tema menor.

Para los personas que no conocen Python y desean evaluar la interfaz, ponemos a disposición un instalador para demostración totalmente funcional en homologación (testing). Ofrecemos un soporte comercial pago para los que necesiten realizar consultas, soliciten corrección ajustes y deseen tener acceso al instalador para producción y actualizaciones futuras que liberemos.

Todo el código fuente esta publicado en el repositorio de `GoogleCode <http://pyafipws.googlecode.com>`_ bajo la licencia GPL3, con los respectivos scripts e instructivos de instalación.

El resultado creemos que ha sido bastante satisfactorio, posibilitando extender y mantener el proyecto financieramente, contribuyendo al software libre y a la comunidad con herramientas alternativas y superadoras, y empezando a crear una grupo de desarrolladores interesados en el tema.

La interfaz tiene miles de descargadas desde el sitio del proyecto, y muchas empresas y compañías importantes nos han contratado el soporte comercial.

Esto no ha sido totalmente sin contratiempos ni esfuerzos, por lo que para finalizar van algunos comentarios y recomendaciones:

* Los instaladores y paquetes fueron fundamentales para que las personas puedan evaluar los productos, sobre todo en tecnologías no tan difundidas como Python, y principalmente para Windows, que ha sido el mayor mercado para esta interfaz.
* La documentación y ejemplos fueron otro punto importante, y por experiencia es un tema donde se debe profundizar constantemente, aún en los casos que parezca que es suficiente (incluimos preguntas frecuentes, recortes de código, aclaraciones importantes, etc.). 
* Los cursos de capacitación y talleres son muy productivos (hemos realizado 2 en en la `ACP <https://groups.google.com/group/pyafipws/web/curso-en-la-acp?hl=es>`_, a quienes agradecemos), permiten extenderse un poco más sobre el tema y conocer a los interesados.
* Para la difusión nos han ayudado mucho blogs, noticias, eventos de software libre, etc. A medida que el proyecto fue apareciendo en los buscadores fue creciendo su popularidad y utilidad real para los usuarios.
* El soporte comunitario en nuestro caso no ha sido efectivo, la lista de correo y los sistemas de tickets/issues no se usaron mucho, tampoco ha habido muchas  contribuciones y revisiones al código fuente, quizás por el carácter sensible y/o particular del tema (amén que la filosofía del software libre todavía no ha sido muy bien transmitida en algunos ambientes).

Esperamos que este artículo haya servido de una visión general sobre el tema, cualquier información adicional la pueden encontrar en las siguientes direcciones:

* Sitio del proyecto: `www.pyafipws.com.ar <http://www.pyafipws.com.ar>`_ 
* Grupo de Noticias: `groups.google.com.ar/group/pyafipws <http://groups.google.com.ar/group/pyafipws>`_
* Soporte comercial y documentación: `www.sistemasagiles.com.ar/trac/wiki/PyAfipWs <http://www.sistemasagiles.com.ar/trac/wiki/PyAfipWs>`_
* Minisitio AFIP factura electrónica: `www.afip.gov.ar/fe <www.afip.gov.ar/fe>`_
