.. title: Manejo simple de xml (SimpleXMLElement)


En este ejemplo se muestra como convertir un string desde y hacia un objeto simple que representa el XML (código usado en `Factura Electronica`_)

::

    import xml.dom.minidom

    class SimpleXMLElement:
        "Clase para Manejo simple de XMLs (simil PHP)"
        def __init__(self, text = None, element = None, document = None):
            if text:
                self.__document = xml.dom.minidom.parseString(text)
                self.__element = self.__document.documentElement
            else:
                self.__element = element
                self.__document = document
        def addChild(self,tag,text=None):
            element = self.__document.createElement(tag)
            if text:
                element.appendChild(self.__document.createTextNode(str(text)))
            self.__element.appendChild(element)
        def asXML(self,filename=None):
            return self.__document.toxml('utf8')
        def __getattr__(self,tag):
            try:
                return SimpleXMLElement(
                    element=self.__element.getElementsByTagName(tag)[0],
                    document=self.__document)
            except:
                raise RuntimeError("Tag not found: %s" % tag)
        def __getitem__(self,item):
            return getattr(self,item)
        def __contains__( self, item):
            return self.__element.getElementsByTagName(item)
        def __unicode__(self):
            return self.__element.childNodes[0].data
        def __str__(self):
            return self.__element.childNodes[0].data.encode("utf8","ignore")
        def __repr__(self):
            return repr(self.__str__())
        def __int__(self):
            return int(self.__str__())
        def __float__(self):
            return float(self.__str__())


Simplemente creamos un objeto de tipo SimpleXmlElement pasandole el string y obtenemos el objeto parseado. Se puede:

* Acceder por item (como si fuera un dict)

* Acceder por atributo (como si fuera un objeto)

* Preguntar con ``in`` si un tag es hijo

* Al acceder se devuelven elementos xml, por lo que hay que convertirlos a ``str``, ``int``, ``float``, etc.

::

    >>> from simplexmlelement import SimpleXMLElement
    >>> span = SimpleXMLElement('<span><a href="google.com">google</a><prueba><i>1</i><float>1.5</float></prueba></span>')
    >>> print str(span.a)
    google
    >>> print float(span.prueba.i)
    1
    >>> print float(span.prueba.float)
    1.5


Faltaría:

* Acceder a los atributos de los tags (quizas por item simil diccionario o via ``attributes()`` y ``addAttribute()``)

* Soportar más de un tag hijo (implementar ``__iter__``)

.. ############################################################################

.. _Factura Electronica: http://www.nsis.com.ar/public/browser/pyafip/ws/php.py

