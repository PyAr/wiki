.. title: Progressbar y Urllib2


Este es un ejemplito de cómo descargar algo y a medida que se descarga, mostrar una barrita de progreso.

.. code-block:: python

    from progressbar import ProgressBar
    from progressbar import Percentage
    from progressbar import Bar


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
        chunk = 10240
        while True:
            buffer = u.read(chunk)
            if buffer:
                file.write(buffer)
                pbar.update(i)
                i += chunk
            else:
                break
        pbar.finish()
        file.close()

