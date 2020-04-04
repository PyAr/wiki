.. title: GtkDialog


ejemplo para crear dialogos modales de distintos tipos con distintos botones



::

    import gtk
    import sys

    # por defecto crea un mensaje de informacion sin botones
    info = gtk.MessageDialog(message_format="informacion!")
    # tipo advertencia con un boton de ok
    warning = gtk.MessageDialog(type=gtk.MESSAGE_WARNING,
        buttons=gtk.BUTTONS_OK_CANCEL, message_format="advertencia..")
    # pregunta con botones si no
    question = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION,
        buttons=gtk.BUTTONS_YES_NO, message_format="pregunta?")
    # error con boton ok
    error = gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
        buttons=gtk.BUTTONS_OK, message_format="error!?!")

    # run bloquea hasta que se produzca un evento y devuelve el valor del evento
    if info.run() == gtk.RESPONSE_DELETE_EVENT:
        print "si, es la unica senial que puede emitir, ya que no tiene botones"
    # hay que esconder el dialogo
    info.hide()

    # almacenamos el valor de retorno en una variable para controlar varios valores
    response = warning.run()
    warning.hide()

    if response == gtk.RESPONSE_OK:
        print "advertencia respondio aceptar"
    elif response == gtk.RESPONSE_CANCEL:
        print "advertencia respondio cancel"

    response = question.run()

    if response == gtk.RESPONSE_YES:
        print "respondio si!"
    elif response == gtk.RESPONSE_NO:
        print "respondio no :("

    question.hide()

    if error.run() == gtk.RESPONSE_OK:
        print "error OK"

    error.hide()
    sys.exit(0)

    gtk.main()

