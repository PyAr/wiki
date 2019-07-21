"""
This classes are the basics for an content based matching system
Based on: "Matching Events in a Content-Based Subscription System"
link, somewhere, later.

Supported datatypes (for now):
    - int
    - float
    - str

Aca usamos el hecho que float < int < str
Si ponemos decimal, deberia entrar en algun lado del orden.

"""

import sets, random

class MatchNode:
    def __init__(self, tail = None):
        if tail:
            self.empty = True
            self.dontcare = tail
        else:
            self.empty = True
            self.dontcare = None            
        self.test = None
        self.results = {}
        
        self.leaves = sets.Set()
        self.params = ()
        self.attribute = (None, None)
        
    def __repr__(self):
        return "<"+str(self.test)+":"+str(self.params)+"/"+str(self.attribute)+">"
    
    def match(self, event, verbose = 0, counter=None):
        if verbose:
            print "Entering:", self
            print "Event:", event
            
        if not self.test:
            if verbose: print "Just leaves"
            return self.leaves
        
        while event and event[0][0] < self.attribute:
            event = event[1:]
        if verbose and event:
            print ">evt left>",event
          
            
        
        if not event:
            if verbose: print "no event left"
            if self.dontcare:
                if verbose: print "go dontcare"
                return self.dontcare.match(event, verbose, counter)
            return self.leaves
            
        subs = sets.Set()
        if event[0][0] == self.attribute:
            if verbose: print "doing test", self.attribute, self.test, self.params
            if counter: counter()
            res = self.test(event[0], self.attribute, self.params)
            if verbose: print "res", res
            for result in res:
                if self.results.has_key(result):
                    subs = subs.union(self.results[result].match(event, verbose, counter))

        if self.dontcare:
            if verbose: print "go dontcare"
            subs = subs.union(self.dontcare.match( event, verbose, counter ))

        return subs

    def subscribe(self, sub, sid):
        # primero vemos si ya no queda nada de la subscripcion
        # en ese caso, si esto es una hoja, ponemos todo en la hoja.
        # si este nodo no es una hoja, lo mando por dontcare
        if not sub:
            # we only have to add matches
            if self.empty or self.leaves:
                self.leaves.add( sid )
                self.empty = False
            else:
                if not self.dontcare:
                    self.dontcare = MatchNode()
                self.dontcare = self.dontcare.subscribe(sub, sid)
            return self
                
        # spliteo los atributos
        tipo, atrib, prueba, param, res = sub[0]
        
        # si el nodo esta vacio, lo seteo para que consuma la primer condicion
        if self.empty:
            self.set_test(tipo, atrib, prueba, param)
            self.empty = False
            self.add_result(res, sub[1:], sid)
            return self
        
        # mientras que si esto es una hoja y aun quedan condiciones
        # creo un nodo que le doy como como este tail, y le subscribo la condicion
        # como el nodo va a estar empty, entraria por el caso de arriba
        # el tail se agrega en dontcare
        if self.leaves:
            n = MatchNode(tail = self)
            return n.subscribe(sub, sid)
        
        # esta comparacion  determina el orden en que deben hacerse las pruebas.
        
        mine = (self.attribute)+(self.test,self.params)
        other = (tipo, atrib, prueba, param)
        
        if  mine == other:
            self.add_result(res, sub[1:], sid)
            return self
        elif mine < other:
            if self.dontcare:
                self.dontcare = self.dontcare.subscribe(sub, sid)
            else:
                self.dontcare = MatchNode().subscribe(sub, sid)
            return self
        
        n = MatchNode(tail = self)
        return n.subscribe(sub, sid)
            
    def add_result(self, res, sub, sid):
        if self.results.has_key(res):
            n = self.results[res]
            n = n.subscribe(sub, sid)
            self.results[res] = n
        else:
            self.results[res] = MatchNode()
            self.results[res] = self.results[res].subscribe(sub, sid)
            
    def set_test(self, tipo, atrib, prueba, param):
        self.test = prueba
        self.params = param 
        self.attribute = (tipo, atrib)


    def dump(self, prefix = "", depth = 0):
        
        if self.empty:
            print "   "*depth,            
            print "EMPTY"
        elif self.leaves:
            print "   "*depth,            
            print prefix,":"
            for x in self.leaves:
                print "   "*(depth+1),"->",
                print x
        else:
            print "   "*depth,
            if prefix: print str(prefix)+":",
            print self.attribute, self.test, self.params
            #print self.results.keys()
            for x in self.results.keys():
                self.results[x].dump(prefix=x, depth=depth+1)
            if self.dontcare:
                self.dontcare.dump(prefix="-*dontcare*-", depth=depth+1)
        

class Matcher:
    debug = 1
    
    def __init__(self):
        self.tree = MatchNode()
        if self.debug:
            self.subs = []
    def match(self, event, verbose=0, counter=None):
        event = list(event)
        event.sort()
        return self.tree.match(event, verbose, counter)

    def subscribe(self, sub, sid):
        # sub should be anything
        # for now we require sub to be a conjunction of predicates
        # should sub be something else, we can transform it to CNF and
        # make a new subscription for term. later.
        # for now, we even assume its ordered
        if self.debug:
            self.subs.append( (sub, sid) )
        sub = list(sub)
        sub.sort()
        self.tree = self.tree.subscribe( sub, sid ) 
    
    def dump(self):
        self.tree.dump()

    def naive_match(self, event, counter=None):
        sids = sets.Set()
        for sub, sid in self.subs:
            if naive_test(sub, event, counter=counter):
                sids.add( sid )
        
    def test(self, event):
        if not self.debug:
            raise Exception("La clase no esta en modo debug")
        sids = self.naive_match(self, event)
        csid = self.match( event )
        if csid != sids:
            print "Testeo por red", csid
            print "Testeo Naive", sids
            for sub, sid in self.subs:
                print "  testing sub", sid 
                naive_test(sub, event, verbose=1)
            
            print "EVENT:"
            for ev in event:
                print "       ", ev
            for s in self.subs:
                print "---->"
                for q in s:
                    print "        ", q
            self.dump()
            import code
            code.interact(local=locals())
            raise Exception("fallo la prueba")
# Un predicado es una tupla:
#   (tipo, atributo, prueba, parametros, resultado)
#   tipo: el tipo (int, str, float) del atributo
#   atributo: el nombre (str) del atributo a evaluar
#   prueba: la funcion que evalua la condicion
#   parametros: parametros extra para la funcion
#   resultado: el resultado que debe dar la evaluacion para que sea valido

def evaluate(evt, attr, params):
    return [evt[1]]

def compare_attr(evt, attr, params):
    res = []
    val = params[0]
    other = evt[1]

    if val != other:
        res.append("NEQ")
    if val >= other:
        res.append("LEQ")
    if val <= other:
        res.append("GEQ")       
    if val > other:
        res.append("LT")
    if val < other:
        res.append("GT")
    return res

def EQ(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
        
    return (t, name, evaluate, (), value)

def NEQ(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
    return (t, name, compare_attr, (value,), "NEQ")

def GT(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
    return (t, name, compare_attr, (value,), "GT")

def LT(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
    return (t, name, compare_attr, (value,), "LT")

def LEQ(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
    return (t, name, compare_attr, (value,), "LEQ")

def GEQ(name, value):
    t = type(value)
    if not t in (float, int, str):
        raise TypeError("Attributes/values type must be in (float, str, int)")
    if type(name) != str:
        raise TypeError("Attribute names must be str")
    return (t, name, compare_attr, (value,), "GEQ")

def naive_test(sub, event, verbose = 0, counter=None):
    # tomo cada condicion de la subscripcion
    for s_tipo, s_attr, s_eval, s_param, s_res in sub:
        # con check verifico si se evaluo la condicion
        # si no se evaluo, se considera qeu no se cumple
        # es decir, altura > 10 implica que tiene altura.
        check = 0
        # tomo cada relacion del evento
        for (tipo, attr), valor in event:
            # si es tipo es correcto y el nombre tambien, lo evaluo
            if s_tipo == tipo and s_attr == attr:
                # si la prueba falla, las condiciones no se cumplen, return 0
                if verbose: print tipo, attr, s_res, s_eval( ((tipo, attr),valor) , s_attr , s_param )
                if counter: counter()
                if not s_res in s_eval( ((tipo, attr),valor) , s_attr , s_param ):
                    return 0
                # si llegamos aca es que la prueba se aplico y fue exitosa
                check = 1
                break
        # si la prueba no se aplico
        if check == 0:
            return 0
    # todas las pruebas se aplicaron y fueron exitosas
    return 1
                
def random_relation():
    return random.choice([EQ, NEQ, GT, LT, GEQ, LEQ])

def random_sub():
    # cuantos preds
    sub = []
    intvals = range(10)
    strvals = range(10)
    for x in range(random.randint(1,4)):
        # elijo el tipo, int, str o float / we dont use float with equal
        t = random.choice([1,2])
        if t == 1: # int
            # elijo el nombre
            vn = random.choice(intvals)
            intvals.remove(vn)
            nombre = "intval"+str(vn)
            # elijo el valor
            valor = random.randint(1,10)
            r = random_relation()
            sub.append( r(nombre, valor) ) 
        if t == 2: # string
            # elijo el nombre
            vn = random.choice(strvals)
            strvals.remove(vn)
            nombre = "strval"+str(vn)
            # elijo el valor
            valor = random.randint(1,10)
            r = random_relation()
            sub.append( r(nombre, valor) )            
    return sub
        
def random_event():
    # cuantos preds
    intvals = range(10)
    strvals = range(10)
    evt = []
    for x in range(random.randint(1,7)):
        # elijo el tipo, int, str o float / we dont use float with equal
        t = random.choice([1,2])
        if t == 1: # int
            vn = random.choice(intvals)
            intvals.remove(vn)
            # elijo el nombre
            nombre = "intval"+str(vn)
            # elijo el valor
            valor = random.randint(1,10)
            evt.append( ((int, nombre), valor) ) 
        if t == 2: # string
            vn = random.choice(strvals)
            strvals.remove(vn)
            # elijo el nombre
            nombre = "strval"+str(vn)
            # elijo el valor
            valor = random.randint(1,10)
            evt.append( ((str, nombre), valor) )            
    return evt
    

def test_random():
    print "*"*80
    for x in range(300):
        m = Matcher()
        for y in range(10):
            m.subscribe( random_sub(), y )
        for z in range(200):
            m.test( random_event() )

class Counter:
    def __init__(self):
        self.count = 0
        
    def __call__(self):
        self.count += 1
        
if __name__ == "__main__":
    #test_random()
    import sys, time
    # vamos a hacer pruebas de 1 a mil subscripciones
    for x in range(1, 1000, 10):
        m = Matcher()
        
        # hacemos x subscripciones
        for s in range(x):
            m.subscribe( random_sub(), x )
        # contamos las evaluaciones en 5 mil eventos
        
        # primero por red
        cr = Counter()
        trs = time.time()
        for z in range(5000):
            m.match(random_event(), counter=cr)
        tr = time.time() - trs
            
        # despues por naive
        cn = Counter()
        tns = time.time()
        for z in range(5000):
            m.naive_match(random_event(), counter=cn)
        tn = time.time() - tns
        
        print cr.count, tr, cn.count, tn 
        print >>sys.stderr, "-"*50
        print >>sys.stderr, x, "of", 1000
        print >>sys.stderr, "   Naive:"
        print >>sys.stderr, "       ", cn.count, "evaluations"
        print >>sys.stderr, "       ", tn, "seconds"        
        print >>sys.stderr, "   Network:"
        print >>sys.stderr, "       ", cr.count, "evaluations"
        print >>sys.stderr, "       ", tr, "seconds"                