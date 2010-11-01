= Progressbar y Urllib2 =
Este es un ejemplito de como descargar algo y a medida que se descarga, mostrar una barrita de progreso.

{{{
#!code python
from progressbar import ProgressBar, Percentage, Bar

def download_python():
    url = 'http://www.python.org/ftp/python/2.7/Python-2.7.tar.bz2'
    fname = url.split('/')[-1]
    u = urllib2.urlopen(url)
    file = open(fname, 'w')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Descargando: %s Bytes: %s" % (fname, file_size)
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=file_size).start()
    i = 0
    data = str()
    chunk = 10240
    while True:
        buffer = u.read(chunk)
        if buffer:
            data += buffer
            pbar.update(i)
            i += chunk
        else:
            break
    file.write(data)
    pbar.finish()
    file.close()
}}}
