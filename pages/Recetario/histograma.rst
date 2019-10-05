
Cómo generar un histograma
==========================

Ejemplo super sencillo mostrado en la Tribu el 31/JUL/2010 sobre cómo usar matplotlib desde la consola.

Para mas información, revisar:

* Matplotlib_

* `Documentación de hist`_

::

    >>> from matplotlib.pylab import hist, show
    >>> plata = []
    >>> a = plata.extend
    >>> a([50])
    >>> a([20]*10)
    >>> a([10]*13)
    >>> a([5]*8)
    >>> a([2]*35)
    >>> a([1]*1)
    >>> plata
    [50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    >>> hist(plata, 100, (0,100))
    (array([ 0,  1, 35,  0,  0, 15,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,
            0,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]), array([   0.,
              9.,   10.,   11.,   12.,   13.,   14.,   15.,   16.,   17.,
             18.,   19.,   20.,   21.,   22.,   23.,   24.,   25.,   26.,
             27.,   28.,   29.,   30.,   31.,   32.,   33.,   34.,   35.,
             36.,   37.,   38.,   39.,   40.,   41.,   42.,   43.,   44.,
             45.,   46.,   47.,   48.,   49.,   50.,   51.,   52.,   53.,
             54.,   55.,   56.,   57.,   58.,   59.,   60.,   61.,   62.,
             63.,   64.,   65.,   66.,   67.,   68.,   69.,   70.,   71.,
             72.,   73.,   74.,   75.,   76.,   77.,   78.,   79.,   80.,
             81.,   82.,   83.,   84.,   85.,   86.,   87.,   88.,   89.,
             90.,   91.,   92.,   93.,   94.,   95.,   96.,   97.,   98.,
             99.,  100.]), <a list of 100 Patch objects>)
    >>> show()


`ej_tribu.jpg </images/Recetario/Histograma/ej_tribu.jpg>`_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _Matplotlib: http://matplotlib.sourceforge.net/

.. _Documentación de hist: http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist

.. _categoryrecetas: /pages/categoryrecetas
