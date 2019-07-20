
TK Wizards
==========

Crea un Wizard amigable para actividades o previo de instalaciones, con multiples paginas, del tipo "siguiente, siguiente *(...)* Terminar"

Sacando todo el codigo necesario para generar el Wizard en si mismo, agregar nuevas paginas es simple.

Las paginas pueden contener cualquier widget, en este ejemplo solo se usa 1 label por cada una.

**Screenshot:**

  `temp.jpg </wiki/TKWizards/attachment/36/temp.jpg>`_

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    try:
        import Tkinter as tk  # Python2
    except ImportError:
        import tkinter as tk  # Python3

    class Wizard(tk.Toplevel):
        def __init__(self, npages, master=None):
            self.master = master
            self.pages = []
            self.current = 0
            tk.Toplevel.__init__(self)
            #self.overrideredirect() # saca el decorador de ventana
            self.protocol("WM_DELETE_WINDOW", self.onQuit)
            #self.attributes('-toolwindow', True) # ToolWindowz
            self.attributes('-topmost', True)
            if master:
                self.transient(self.master)
                self.lift(master)
            for page in range(npages):
                self.pages.append(tk.Frame(self))
            self.pages[0].pack(fill='both', expand=1)
            self.__wizard_buttons()

        def onQuit(self):
            pass # hace algo on quit

        def __wizard_buttons(self):
            for indx, frm in enumerate(self.pages):
                btnframe = tk.Frame(frm, bd=1, bg='#3C3B37')
                btnframe.pack(side='bottom', fill='x')
                nextbtn = tk.Button(btnframe, bd=0, bg='#F2F1F0', activebackground='#F58151', highlightcolor='red', cursor='hand2', text="Siguiente >>", width=10, command=self.__next_page)
                nextbtn.pack(side='right', anchor='e', padx=5, pady=5)
                if indx != 0:
                    prevbtn = tk.Button(btnframe, bd=0, bg='#F2F1F0', activebackground='#F58151', highlightcolor='red', cursor='hand2', text="<< Atras", width=10, command=self.__prev_page)
                    prevbtn.pack(side='right', anchor='e', padx=5, pady=5)
                    if indx == len(self.pages) - 1:
                        nextbtn.configure(text="Terminar", bd=0, bg='#F2F1F0', activebackground='#F58151', highlightcolor='red', cursor='hand2', command=self.close)

        def __next_page(self):
            if self.current == len(self.pages):
                return
            self.pages[self.current].pack_forget()
            self.current += 1
            self.pages[self.current].pack(fill='both', expand=1)

        def __prev_page(self):
            if self.current == 0:
                return
            self.pages[self.current].pack_forget()
            self.current -= 1
            self.pages[self.current].pack(fill='both', expand=1)

        def add_page_body(self, body):
            body.pack(side='top', fill='both', padx=6, pady=12)

        def page(self, page_num):
            try:
                page = self.pages[page_num]
            except KeyError("Pagina Invalida! : %s" % page_num):
                return 0
            return page

        def close(self):
            if self.validate():
                self.master.iconify()
                print (' TK Wizard finished... ')
                self.destroy()
                self.master.destroy() # remover?

        def validate(self):
            return 1 # hace algo

    if __name__ == "__main__":
        root = tk.Tk()
        root.title(' TK Wizards ')
        root.focus()
        wizard = Wizard(npages=3, master=root)
        wizard.minsize(400, 350)
        page0 = tk.Label(wizard.page(0), text='Pagina 1: ...Bienvenido al Wizard de TK !')
        page1 = tk.Label(wizard.page(1), text='Pagina 2: Acepta las condiciones de la WTFPL ?')
        page2 = tk.Label(wizard.page(2), text='Pagina 3: Felicitaciones, nada no se ha instalado correctamente.')
        wizard.add_page_body(page0)
        wizard.add_page_body(page1)
        wizard.add_page_body(page2)
        root.mainloop()

