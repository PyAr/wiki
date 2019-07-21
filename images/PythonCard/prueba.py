#!/usr/bin/python

"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""

from PythonCard import model
from PythonCard import dialog

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass

    def on_btnEjecutar_mouseClick(self, event):
        comando = self.components.txtComando.text
        resultado = str(eval(comando))
        self.components.txtResultados.text = resultado

    def on_menuFileAyuda_select(self, event):
        dialog.alertDialog(self, 
            'Este programa de prueba ejecuta el comando ingresado por el usuario', 
            'Ayuda')

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
