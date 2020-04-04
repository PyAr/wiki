.. title: Holamundo

Todo un clásico... un Hola Mundo desde pyUNO

::

    # -*- coding: utf-8 -*-
    import uno

    def hola_mundo():
        msgbox('Hola Mundo en PyUNO')
        return

    def msgbox(message):
        ctx = uno.getComponentContext()
        sm = ctx.getServiceManager()
        toolkit = sm.createInstanceWithContext('com.sun.star.awt.Toolkit', ctx)
        msg = toolkit.createMessageBox(
                                    toolkit.getDesktopWindow(),
                                    'infobox',
                                    1,
                                    'UNOPython',
                                    str(message))
        return msg.execute()


Para saber donde guardar esta macro, mira el wiki de Apache OpenOffice: http://wiki.openoffice.org/wiki/ES/Manuales/GuiaAOO/TemasAvanzados/Macros/Python

Para ejecutar la macro, desde cualquier aplicación de Apache OpenOffice, menú Herramientas -> Macros -> Ejecutar macros...

