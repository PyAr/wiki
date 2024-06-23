.. title: GtkPrintNonGtk


Este ejemplo muestra como usar gtk para mostrar el diálogo de imprimir pero sin usar el main loop.

Es útil para aplicaciones no gtk que solo quieren usar el diálogo de impresión pero tienen otro main loop que no es el de gtk.

Explicación: Lo que hacemos después de mostrar el diálogo es procesar los eventos de gtk mientras haya eventos pendientes, luego seguimos en nuestra aplicación normalmente.

.. code-block:: python

    import gtk
    import time

    po = gtk.PrintOperation()
    pa = gtk.PRINT_OPERATION_ACTION_PRINT_DIALOG
    po.run(pa)

    while gtk.events_pending():
        gtk.main_iteration(True)

    print 'y seguimos como si nada'
    print 'esperamos 3 segundos'
    time.sleep(3)
    print 'chau'


.. image:: /images/Recetario/Gui/Gtk/PrintNonGtk/Imprimir.png

