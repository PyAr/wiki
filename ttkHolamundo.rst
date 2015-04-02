
ttkHolaMundo
------------

Crea una ventana que muestra el famoso mensaje "Hola mundo".

`ttkHolamundo.png </wiki/ttkHolamundo/attachment/121/ttkHolamundo.png>`_

::

    #!/usr/bin/env python3
    #-*- coding:utf-8 -*-

    import tkinter as tk
    from tkinter import ttk

    class HolaMundoApp(ttk.Frame):
        '''Clase que define una ventana que muestra el "Hola mundo"'''

        def __init__(self, master=None):
            ttk.Frame.__init__(self, master)

            #Creamos un label
            o = ttk.Label(self, text='Hola PyAr!', anchor='center')
            #Lo agregamos a la ventana.
            o.pack(fill='both', expand=True)
            #Agregamos este frame a la ventana principal (Top level window)
            self.pack(fill='both', expand=True)

            #Configuramos la ventana principal
            top = self.winfo_toplevel()
            top.title('Hola mundo')
            top.minsize(width=300, height=200)


    if __name__ == '__main__':
        app = HolaMundoApp()
        app.mainloop()

