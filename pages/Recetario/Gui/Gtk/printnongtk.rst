
GtkPrintNonGtk
==============

Este ejemplo muestra como usar gtk para mostrar el dialogo de imprimir pero sin usar el main loop.

  Es útil para aplicaciones no gtk que solo quieren usar el dialogo de impresión pero tienen otro main loop que no es el de gtk.

explicación: lo que hacemos después de mostrar el dialogo es procesar los eventos de gtk mientras haya eventos pendientes, luego seguimos en nuestra aplicación normalmente.

::

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


`Imprimir.png </images/Recetario/Gui/Gtk/PrintNonGtk/Imprimir.png>`_

