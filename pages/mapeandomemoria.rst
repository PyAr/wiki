.. title: Mapeando Memoria


Las funciones de abajo utilizan heapy_ para generar una descripción visual (en ascii) de la memoria, junto con otras estadísticas.

*heapStats* devuelve un diccionario pickleado, que es útil para guardarlo en un archivo para posterior análisis por ejemplo, o para ser transmitido por algún protocolo de red, como xmlrpc o http, puesto que suele utilizarse dentro de un demonio de servidor.

En los datos generados, *"byclodo"* significa que son datos agrupados por *CLass Or Dictionary Owner*, lo que suele decirnos con bastante precisión quién es el culpable de mantener vivos los objetos. *"byrcs"* significa que se agrupan los datos por *Referrer Classification Set*, que significa el "clodo" del referente, útil para detectar referencias cíclicas por ejemplo.

Finalmente, memmap tiene el mapa de la memoria, y el detalle por si se quiere generar mapas más detallados o con diferente visualización.

Probablemente para un uso concreto sea necesario extender memmap antes del memmap.sort(), agregando buffers específicos de la aplicación que no caigan dentro de lo consumido por python. Por ejemplo, los objetos mmap tienen asociados grandes pedazos de memoria que no aparecerían en el mapa, y si se usan mucho en la aplicación convendría incluirlos, o buffers significativos utilizados por bibliotecas de extensión.

Este código sólo funciona en CPython, puesto que utiliza el hecho de que id() devuelve la dirección en memoria de un objeto. Eso no es cierto en Jython, PyPy y muchas otras implementaciones.

::

    import cPickle
    from guppy import hpy as heapy
    _heapy = heapy()

    def report_memmap(mm):
        import re
        from bisect import bisect_left, bisect_right

        mxsz = max( s for a,s in mm )

        def usage(mn,mx,mxsz):
            rv = ' '
            for a,s in mm[bisect_left(mm,(mn-mxsz-16,0)):bisect_right(mm,(mx+1,0))]:
                if mn>=mx:
                    break
                s += a + 16 # add 16 bytes for malloc headers
                if s<=mn:
                    continue
                if a<mx:
                    rv = '-' # touched the range, at least fragmented
                if a>mn:
                    # cannot be fully used
                    break
                #used up to s
                mn=s
            if mx <= mn:
                rv = '*' # used in full
            return rv

        def bytes(x):
            if x < 1024:
                return '%db' % x
            elif x < 1024*1024:
                return '%.2fKb' % (x/1024.0)
            elif x < 1024*1024*1024:
                return '%.2fMb' % (x/1024.0/1024.0)
            else:
                return '%.2fGb' % (x/1024.0/1024.0/1024.0)

        def secsize(x):
            rv = 4096
            while (x/rv/80) > 40:
                rv *= 2
            return rv

        def report(mn,mx,ss):
            smxsz = max( s for a,s in mm[bisect_left(mm,(mn-mxsz-16,0)):bisect_right(mm,(mx+1,0))] )
            mp  = ''.join([ usage(i,i+ss,smxsz) for i in range(mn,mx,ss) ])
            rv  = '%s total, %s per sector\n' % (bytes(mx-mn), bytes(ss))
            rv += lre.sub('\\1\n',mp)
            rv += """
            Fragmentation: %.2f%%
            Fragmented sectors: %d
            Contiguous used sectors: %d
            Contiguous free sectors: %d
            """ % ( mp.count('-')*100.0/len(mp),
                    mp.count('-'),
                    mp.count('*'),
                    mp.count(' ') )
            return rv

        def domap(filterfn):
            if not any(filterfn(a) for a,s in mm):
                return 'empty'
            mn = min( a for a,s in mm if filterfn(a) )
            mx = max( a for a,s in mm if filterfn(a) )
            ss = secsize(mx-mn)
            mn = mn/ss*ss
            mx = mx/ss*ss+ss
            return report(mn,mx,ss)

        lre = re.compile('(.{80,80})')

        lomap = domap(lambda a: a <  0x80000000)
        medmap= domap(lambda a: a >= 0x80000000 and a < 0x100000000L)
        himap = domap(lambda a: a >= 0x100000000L)

        return lomap, medmap, himap


    def heapStats():
        global _debug_heap
        global _heapy

        import StringIO

        statdump = StringIO.StringIO()
        heap = _heapy.heap()

        try:
            heap.dump(statdump)
        except:
            # ignore exceptions dumping... shit happens
            pass

        statdumpu = StringIO.StringIO()
        heapu = _heapy.heapu()

        try:
            heapu.dump(statdumpu)
        except:
            # ignore exceptions dumping... shit happens
            pass

        statdumpbr = StringIO.StringIO()
        heapbr = heap.byrcs

        try:
            heapbr.dump(statdumpbr)
        except:
            # ignore exceptions dumping... shit happens
            pass

        refs = None
        try:
            refs = heap.stat
            refs.rows = list(refs.get_rows())
            refs.rows.sort(lambda x,y:-cmp(x.count,y.count))

            oc = _heapy.Size.classifier.get_cli().classify
            id_ = id
            str_ = str
            memmap = [ (id_(x),oc(x)) for x in heap.nodes ]
        except:
            # At least the rest will be useful
            memmap = []

        memmap.sort()

        # Generate lowres reports from the memmap in four areas, lo, med, hi and very hi.
        # memory (memory allocations tend to group themselves in those ranges,
        # one is probably memmapped heap, the other is simple allocations and
        # the medium one must be the stack). The very high area is the mmap'd area,
        # where most big arrays end up.
        lomap, medmap, himap = report_memmap(memmap)

        # Pickle the memmap, xmlrpclib doesn't like big integers
        memmap = cPickle.dumps(memmap)

        def srepr(x):
            try:
                return repr(x)
            except Exception,e:
                return 'ERROR: %s' (e,)

        rv = dict(
            byclodo = dict(
                reachable = map(srepr, [ heap, heap.more, heap.more.more ]),
                uncollectable = map(srepr, [ heapu, heapu.more, heapu.more.more ]),
                statdump = statdump.getvalue(),
                statdumpu = statdumpu.getvalue(),
                refs = srepr(refs)
            ),
            byrcs = dict(
                reachable = map(srepr, [ heapbr, heapbr.more, heapbr.more.more ]),
                statdump = statdumpbr.getvalue()
            ),
            memmap = dict(
                detail = memmap,
                lo = lomap,
                med = medmap,
                hi = himap
            )
        )

        # return a pickle dump, not by pure xmlrpc
        #   (xmlrpc is picky, doesn't support big ints)
        return cPickle.dumps(rv, 2)


.. ############################################################################

.. _heapy: http://guppy-pe.sourceforge.net/

