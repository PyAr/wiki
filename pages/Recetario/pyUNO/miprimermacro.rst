
La siguiente macro, detecta el tipo de documento (Calc, Writer, Draw, Impress, etc) desde el cual se ejecuta.

::

    # -*- coding: utf-8 -*-
    import uno

    def quien_soy():
        doc = XSCRIPTCONTEXT.getDocument()
        msgbox(obtener_tipo(doc))
        return

    def obtener_tipo(doc):
        tipo = {'com.sun.star.sheet.SpreadsheetDocument': 'Calc',
                'com.sun.star.text.TextDocument': 'Writer',
                'com.sun.star.presentation.PresentationDocument': 'Impress',
                'com.sun.star.drawing.DrawingDocument': 'Draw',
                'com.sun.star.sdb.OfficeDatabaseDocument': 'Base',
                'com.sun.star.formula.FormulaProperties': 'Math',
                'com.sun.star.script.BasicIDE': 'Basic'}
        # iteramos entre los tipos de documentos
        for t in tipo:
            # validamos si soporta el servicio
            if doc.supportsService(t):
                # devolvemos el tipo de documento
                return 'Soy %s' % tipo[t]
        # si termina sin encontrar un tipo
        return 'No se que tipo soy'

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


Para saber donde guardar estas macros, mira el wiki de Apache OpenOffice_: http://wiki.openoffice.org/wiki/ES/Manuales/GuiaAOO/TemasAvanzados/Macros/Python

