
Xml a diccionario
-----------------

En este ejemplo se muestra como convertir un string a una estructura de diccionarios y listas anidadas usando expat, tambien se proveen dos clases que permiten manipular el resultado como su fueran objetos.

primero el codigo

::

    import xml.parsers.expat

    class XmlParser(object):
        '''a class that parses a xml string an generates a nested 
        dict/list structure
        '''

        def __init__(self, text):
            '''constructor'''
            self.parser = xml.parsers.expat.ParserCreate()
            self.parser.buffer_text = True

            self.result = None
            self.stack = []
            self.current = None

            self.parser.StartElementHandler = self.start_element
            self.parser.EndElementHandler = self.end_element
            self.parser.CharacterDataHandler = self.char_data
            self.parser.Parse(text)

        def start_element(self, name, attrs):
            '''Start xml element handler'''
            if self.current != None:
                self.stack.append(self.current)

            self.current = {}

            for (key, value) in attrs.iteritems():
                self.current[str(key)] = value

            self.current['tag'] = name
            self.current['childs'] = []

        def end_element(self, name):
            '''End xml element handler'''
            if len(self.stack):
                current = self.stack.pop()
                current['childs'].append(self.current)
                self.current = current
            else:
                self.result = self.current

        def char_data(self, data):
            '''Char xml element handler.
            buffer_text is enabled, so this is the whole text element'''
            self.current['childs'].append(data)

    class DictObj(dict):
        '''a class that allows to access a dict as an object
        '''

        def __init__(self, kwargs):
            '''constructor'''
            dict.__init__(self, kwargs)

        def __getattribute__(self, name):
            if name in self:
                obj = self[name]

                if type(obj) == dict:
                    return DictObj(obj)
                elif type(obj) == list:
                    return ListObj(obj)

                return obj
            else:
                return None

    class ListObj(list):
        '''a class that allows to access dicts inside a list as objects
        '''

        def __init__(self, args):
            '''constructor'''
            list.__init__(self, args)

        def __getitem__(self, index):
            if index > len(self):
                raise IndexError('list index out of range')

            obj = list.__getitem__(self, index)

            if type(obj) == dict:
                return DictObj(obj)
            elif type(obj) == list:
                return ListObj(obj)

            return obj

        def __iter__(self):
            '''iterate over the list'''

            count = 0

            while count < len(self):
                yield self[count]
                count += 1

    def raw_string(dct_):
        '''return a string containing just the string parts removing all the 
        xml stuff'''

        def helper(dct):
            result = []

            for child in dct.childs:
                if type(child) == str or type(child) == unicode:
                    result.append(str(child))
                else:
                    result = result + helper(child)

            return result

        return ''.join(helper(dct_))


Simplemente creamos un objeto de tipo XmlParser_ pasandole el string y obtenemos el resultado parseado en la variable result.  Si no queremos andar preguntado si las llaves existen antes de accederlas para evitar excepciones podemos usar la clase DictObj_ que nos permite acceder a las llaves como si fueran atributos, las variables que no existan como llaves contendran None. Aca va un ejemplo en la consola interactiva

::

    >>> import XmlParser
    >>> p = XmlParser.XmlParser('<span><a href="google.com">go<s>o</s>gle</a> <i>test</i> <img src="foo.png" alt="foo"/> <u>!</u><s>!</s></span>')
    >>> r = p.result
    >>> d = XmlParser.DictObj(r)
    >>> d
    {'childs': [{'childs': [u'go', {'childs': [u'o'], 'tag': u's'}, u'gle'], 'href': u'google.com', 'tag': u'a'}, u' ', {'childs': [u'test'], 'tag': u'i'}, u' ', {'childs': [], 'src': u'foo.png', 'alt': u'foo', 'tag': u'img'}, u' ', {'childs': [u'!'], 'tag': u'u'}, {'childs': [u'!'], 'tag': u's'}], 'tag': u'span'}
    >>> d.childs
    [{'childs': [u'go', {'childs': [u'o'], 'tag': u's'}, u'gle'], 'href': u'google.com', 'tag': u'a'}, u' ', {'childs': [u'test'], 'tag': u'i'}, u' ', {'childs': [], 'src': u'foo.png', 'alt': u'foo', 'tag': u'img'}, u' ', {'childs': [u'!'], 'tag': u'u'}, {'childs': [u'!'], 'tag': u's'}]
    >>> d.childs[0]
    {'childs': [u'go', {'childs': [u'o'], 'tag': u's'}, u'gle'], 'href': u'google.com', 'tag': u'a'}
    >>> d.childs[0].tag
    u'a'
    >>> d.childs[0].childs[0]
    u'go'
    >>> d.childs[0].childs[1].tag
    u's'


.. ############################################################################



