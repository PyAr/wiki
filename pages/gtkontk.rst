
GTK on TK
=========

.. role:: small
   :class: small


Usar temas de GTK en las aplicaciones de TKinter, no requiere ttk, funciona en KDE.

**Foto de Pantalla:**

De fondo Gedit en Ubuntu, usando el tema Ambiance, arriba una ventana con similar tema pero en TK, a su lado una ventana TK por defecto.

  :small:`El codigo de este ejemplo esta mas abajo` *(la foto no esta editada, no hay truco, funciona en KDE, o inclusive lo he hecho funcionar sin GTK instalado)*:small:`.`

`gtk-on-tk-hack.jpg </images/GTKonTK/gtk-on-tk-hack.jpg>`_

**El Codigo para hacer GTK on TK:**

::

    #
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    #   colour.py
    #
    import os
    import sys
    import gtk
    try:
        import gconf
        NOGCONF = False
    except:
        NOGCONF = True

    __all__ = ["_get_color_scheme", "_get_color_scheme_list", "get_color_scheme_item", "string_to_gdkColour", "string_to_rgba", "get_Gtk_Theme_Name", "get_Gtk_Theme_Path"]

    def _get_color_scheme():
        gtkSet = gtk.settings_get_default()
        return gtkSet.get_property('gtk-color-scheme')

    def _get_color_scheme_list():
        gtkSch = _get_color_scheme()
        itemList = []
        for line in gtkSch.splitlines():
            itemList.append(line.split(":")[0])
        return itemList

    def get_color_scheme_item(colorName):
        gtkSch = _get_color_scheme()
        findLine = gtkSch[gtkSch.find(colorName):].splitlines()[0]
        c = findLine.replace(colorName+":", "").strip()
        #print colorName, "=", c
        c = c.replace("#", "")
        if len(c) == 12:
            #4 chars, r g b
            rgba = [c[0:4], c[4:8], c[8:12], ""]
        colourFound = '#'
        for set in rgba:
           colourFound = "".join([colourFound, set[:2].upper()])
        if len(colourFound) == 0:
            raise error
            return None
        else:
            return colourFound

    def incHex(c, times=1):
        import string
        c = c.replace("#", "")
        c = c.upper()
        hexString = '0123456789ABCDEF'
        if times > 0:
            if times > 16: times = 16
            hexString = hexString[times:]
            hexString = hexString.ljust(16, 'F')
        else:
            if times < -16: times = -16
            hexString = hexString[:times]
            hexString = hexString.rjust(16, '0')
        trans = string.maketrans('0123456789ABCDEF', hexString)
        ic = c.translate(trans)
        ic = "".join(['#', ic])
        return ic

    def string_to_gdkColor(c):
        if c[0] != '#': c = "".join(['#',c])
        while len(c) not in [4, 7, 10, 13]:
            c = c[0:len(c)-1]
        return gtk.gdk.color_parse(c)

    def rgba_to_string(r, g, b, a=None):
        if (a==None):
            a = 1
        hr, hg, hb, ha = [hex(min(int(n*255), 255))[2:] for n in(r, g, b, a)]
        hList = ['#']
        for n in (hr, hg, hb, ha):
            #print n
            hList.append(n.rjust(2, '0').upper())
        hr = hr.rjust(2, '0')
        hg = hg.rjust(2, '0')
        hb = hb.rjust(2, '0')
        ha = ha.rjust(2, '0')
        return "".join(hList)

    def string_to_rgb(c):
        r, g, b, a = (string_to_rgba(c))
        return r, g, b

    def string_to_rgba(c):
        c = c.replace("#", "")
        if len(c) == 12:
            #4 chars, r g b
            r, g, b = (c[0:4], c[4:8], c[8:12])
            r, g, b = [int(n, 16)/65535.0 for n in(r, g, b)]
            a = 1
        elif len(c) == 8:
            #2 chars, r g b a
            r, g, b, a = (c[0:2], c[2:4], c[4:6], c[6:8])
            r, g, b, a = [int(n, 16)/255.0 for n in(r, g, b, a)]
        elif len(c) == 6:
            #2 chars, r g b
            r, g, b = (c[0:2], c[2:4], c[4:6])
            r, g, b = [int(n, 16)/255.0 for n in(r, g, b)]
            a = 1
        return r, g, b, a

    def get_Gtk_Theme_Name():
        if NOGCONF:
            try:
                gtkrc = open(os.path.expanduser('~/.gtkrc-2.0'))
            except:
                gtkrc = open(os.path.expanduser('~/.gtkrc-2.0-kde4'))
            for line in gtkrc:
                if 'include' in line:
                    themePath = line.split("\"")[1]
                    gtkTheme = themePath.split("/")[-3]
        else:
            client = gconf.client_get_default()
            gtkTheme = client.get_string('/desktop/gnome/interface/gtk_theme')
        return gtkTheme

    def get_Gtk_Theme_Path(gtkTheme=None):
        if gtkTheme == None:
            gtkTheme = get_Gtk_Theme_Name()
        localThemePath = "".join(["~/.themes/", gtkTheme, "/gtk-2.0/gtkrc"])
        localThemePath = os.path.expanduser(localThemePath)
        globalThemePath = "".join(["/usr/share/themes/", gtkTheme, "/gtk-2.0/gtkrc"])
        if os.path.exists(localThemePath):
            ThemePath = localThemePath
        elif os.path.exists(globalThemePath):
            ThemePath = globalThemePath
        else:
            ThemePath = None

        if ThemePath:
            return ThemePath
        else:
            raise NameError

    if __name__ == "__main__":
        import random
        print "COLOUR TEST HARNESS"
        print get_Gtk_Theme_Name()
        print _get_color_scheme()
        colourList = ['030A16FF', '#090E1BDD', '#9595b0b0dbdb', '1414f3f3a8a8']
        colourList.append(get_color_scheme_item(_get_color_scheme_list()[random.randint(0, len(_get_color_scheme_list())-1)]))
        for cc in colourList:
            break
            print "Colour String ", cc
            print "gdkColour     ", string_to_gdkColor(cc)
            print "rgba          ", zip(string_to_rgba(cc))
        print "rgba to string", rgba_to_string(0, 0.5, 1, 0.3)
        print "inc ", incHex(rgba_to_string(0, 0.5, 1, 0.3))
        print get_color_scheme_item('selected_bg_color')


-------------------------



**Ejemplo:**

Descripcion: Crea 2 ventanas pequeñas iguales, una tratara de imitar el tema de GTK, la otra se mostrara como es por defecto.

*(el ejemplo funciona en Ubuntu, que es lo que yo uso, usa el codigo de arriba, lejos de estar bien hecho, pero sirve de ejemplo)*:small:`.`

::

    #
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    #import this
    #import antigravity
    import colour  # <-------Aca esta la magia
    import tkFont
    from Tkinter import *
    #
    root = Tk()
    root.title('GTK Themes on TK: Demo')
    root.wm_attributes("-alpha", 1)
    root.focus()
    root.resizable(0, 0)
    # Muestra informacion
    print " GTK-On-TK Theme Hack:"
    print " I will try to mimic: "+colour.get_Gtk_Theme_Name()+" GTK Theme"
    print " By Parsing the file: "+colour.get_Gtk_Theme_Path()
    print " This is not perfect, if you are on KDE install QTCurve... "
    # Menubar con GTK
    menubar = Menu(root, bd=0, relief=FLAT, fg=str(colour.get_color_scheme_item('base_color')), bg=str(colour.get_color_scheme_item('text_color')), activebackground=str(colour.get_color_scheme_item('selected_bg_color')), activeforeground=str(colour.get_color_scheme_item('text_color')))
    filemenu = Menu(menubar, tearoff=0, bd=0, relief=FLAT, fg=str(colour.get_color_scheme_item('base_color')), bg=str(colour.get_color_scheme_item('text_color')), activebackground=str(colour.get_color_scheme_item('selected_bg_color')), activeforeground=str(colour.get_color_scheme_item('text_color')))
    filemenu.add_command(label="Nuevo", state='disabled')
    filemenu.add_separator()
    filemenu.add_command(label="Cerrar ✗", command= lambda: root.destroy())
    menubar.add_cascade(label="Archivo", menu=filemenu)
    root.config(menu=menubar)
    # GUI con GTK
    root.config(bg=str(colour.get_color_scheme_item('base_color')))
    labl1 = Label(root, text="Soy una ventana con Tema GTK", font=("Times", 12, 'bold'), bd=0, relief=FLAT, bg=str(colour.get_color_scheme_item('base_color')), fg=str(colour.get_color_scheme_item('text_color')), activebackground=str(colour.get_color_scheme_item('selected_bg_color')), activeforeground=str(colour.get_color_scheme_item('text_color')))
    labl1.pack(side=TOP, expand='YES', fill='x', pady=10, padx=20)
    button = Button(root, text="Soy Linda!", fg=str(colour.get_color_scheme_item('text_color')), bd=0, relief=FLAT, bg=str(colour.get_color_scheme_item('base_color')),  activebackground=str(colour.get_color_scheme_item('selected_bg_color')), activeforeground=str(colour.get_color_scheme_item('text_color')))
    button.pack(side=BOTTOM, pady=10, padx=10)
    # la misma GUI pero como es por defecto
    toplevel = Toplevel()
    menubarz = Menu(toplevel)
    filemenuz = Menu(toplevel, tearoff=0)
    filemenuz.add_command(label="Nuevo", state='disabled')
    filemenuz.add_separator()
    filemenuz.add_command(label="Cerrar ✗", command= lambda: root.destroy())
    menubarz.add_cascade(label="Archivo", menu=filemenuz)
    toplevel.config(menu=menubarz)
    labl2 = Label(toplevel, text="Soy una ventana SIN Tema GTK")
    labl2.pack(side=TOP, expand='YES', fill='x', pady=10, padx=20)
    button2 = Button(toplevel, text="Soy Fea!")
    button2.pack(side=BOTTOM, pady=10, padx=10)
    # Le pongo fuente de Ubuntu (se puede omitir)
    menubar.config(font=("ubuntu", 10, "normal", "roman") )
    labl1.config(font=("ubuntu", 10, "bold", "roman") )
    filemenu.config(font=("ubuntu", 10, "normal", "roman") )
    button.config(font=("ubuntu", 10, "bold", "roman") )
    #
    root.mainloop()


Comentario personal:

*Es mas bonito que TTK  🙂  Como sea, la idea es aprovechar que en Linux TODO es un archivo, la magia esta en parsear.*

Comentarios
-----------

Alejandro Autalan
~~~~~~~~~~~~~~~~~

Me gusto esta idea de usar los temas de gtk en tkinter. Pero tener que especificar el estilo de cada widget es un poco tedioso :). Asi que a continuación va una variante de la receta.

Ventajas:

* No es necesario especificar el estilo de cada widget al crearlos.

Desventajas:

* Requiere PyGtk_.

* No funciona con ttk.

Probado con python 2.6 y PyGtk_ 2.17

::

    # -*- coding: utf-8 -*-

    #
    # colour.py
    #

    __all__ = ['apply_gtk_theme']

    import tkFont as tkfont

    HAS_GTK = False
    try:
        import gtk
        HAS_GTK = True
    except:
        pass

    def _get_color_scheme():
        gtkSet = gtk.settings_get_default()
        return gtkSet.get_property('gtk-color-scheme')

    def get_color_scheme_item(colorName):
        gtkSch = _get_color_scheme()
        findLine = ''
        for l in gtkSch.splitlines():
            if l.startswith(colorName):
                findLine = l
                break
        c = findLine.replace(colorName+":", "").strip()
        c = c.replace("#", "")
        rgba = []
        if len(c) == 12:
            rgba = [c[0:4], c[4:8], c[8:12], ""]
        colourFound = '#'
        for set in rgba:
           colourFound = "".join([colourFound, set[:2].upper()])
        if len(colourFound) == 0:
            raise error
            return None
        else:
            return colourFound


    tk_fonts = {}
    tk_font_families= None

    def get_tk_font(font_desc):
        """Crea una fuente tk"""

        global tk_font_families
        global tk_fonts

        if tk_font_families is None:
            tk_font_families = tkfont.families()
        font = None
        if font_desc in tk_fonts:
            font = tk_fonts[font_desc]
        else:
            family = 'Helvetica'
            for x in tk_font_families:
                if x in font_desc:
                    family = x
            s = font_desc.split()
            size = s[-1]
            lower = font_desc.lower()
            weight = 'normal'
            slant = 'roman'
            if 'bold' in lower:
                weight = 'bold'
            if 'italic' in lower:
                slant='italic'
            #print '%s, %s, %s, %s' % (family, weight, slant, size)
            f = tkfont.Font(family=family, size=size, weight=weight, slant=slant )
            tk_fonts[font_desc]= font = f
        return font


    #gtk_states = [gtk.STATE_NORMAL, gtk.STATE_PRELIGHT, gtk.STATE_ACTIVE, gtk.STATE_SELECTED, gtk.STATE_INSENSITIVE]

    def get_tk_styles():
        """Toma los estilos de Gtk y los "traduce" a estilos tk."""
        tk_styles = {}

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkLabel>*', '<GtkLabel>', gtk.Label)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': str(style.bg[gtk.STATE_NORMAL]),
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Label'] = label = c
        tk_styles['Message'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkEntry>*', 'GtkEntry', gtk.Entry)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': get_color_scheme_item('base_color'),
            'selectForeground': str(style.text[gtk.STATE_SELECTED]),
            'selectBackground': str(style.bg[gtk.STATE_SELECTED]),
            'activeForeground': str(style.bg[gtk.STATE_NORMAL]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Entry'] = c
        tk_styles['Text'] = c
        tk_styles['Spinbox'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkMenuBar>*', 'GtkMenuBar', gtk.MenuBar)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': str(style.bg[gtk.STATE_NORMAL]),
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Menu'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkButton>*', 'GtkButton', gtk.Button)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': str(style.bg[gtk.STATE_NORMAL]),
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Button'] = c
        tk_styles['OptionMenu'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkCheck>*', 'GtkCheck', gtk.CheckButton)
        c = {
            'foreground': label['foreground'],
            'background': label['background'],
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'selectColor': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Checkbutton'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkRadio>*', 'GtkRadio', gtk.RadioButton)
        c = {
            'foreground': label['foreground'],
            'background': label['background'],
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'selectColor': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Radiobutton'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkList>*', 'GtkList', gtk.List)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': str(style.bg[gtk.STATE_NORMAL]),
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'selectForeground': str(style.text[gtk.STATE_SELECTED]),
            'selectBackground': str(style.bg[gtk.STATE_SELECTED]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Listbox'] = c

        style = gtk.rc_get_style_by_paths(gtk.settings_get_default(),
            '*<GtkScrollbar>*', 'GtkScrollbar', gtk.Scrollbar)
        c = {
            'foreground': str(style.text[gtk.STATE_NORMAL]),
            'background': str(style.bg[gtk.STATE_NORMAL]),
            'activeForeground': str(style.text[gtk.STATE_SELECTED]),
            'activeBackground': str(style.bg[gtk.STATE_SELECTED]),
            'troughColor': str(style.bg[gtk.STATE_ACTIVE]),
            'font': get_tk_font(str(style.font_desc)),
        }
        tk_styles['Scrollbar'] = c
        tk_styles['Scale'] = c

        return tk_styles


    def apply_gtk_theme_real(w):
        tk_style = get_tk_styles()
        bg_color = get_color_scheme_item('bg_color')
        selected_bg_color = get_color_scheme_item('selected_bg_color')
        patterns = (
            ('*Frame*background', bg_color),

            ('*Menu*foreground', tk_style['Menu']['foreground']),
            ('*Menu*background', tk_style['Menu']['background']),
            ('*Menu*activeBackground', tk_style['Menu']['activeBackground']),
            ('*Menu*activeForeground', tk_style['Menu']['activeForeground']),
            ('*Menu*font', tk_style['Menu']['font']),
            ('*Menu*highlightBackground', bg_color),
            ('*Menu*highlightColor', selected_bg_color),

            ('*Button*foreground', tk_style['Button']['foreground']),
            ('*Button*background', tk_style['Button']['background']),
            ('*Button*activeBackground', tk_style['Button']['activeBackground']),
            ('*Button*activeForeground', tk_style['Button']['activeForeground']),
            ('*Button*font', tk_style['Button']['font']),
            ('*Button*highlightBackground', bg_color),
            ('*Button*highlightColor', selected_bg_color),

            ('*Label*foreground', tk_style['Label']['foreground']),
            ('*Label*background', tk_style['Label']['background']),
            ('*Label*activeBackground', tk_style['Label']['activeBackground']),
            ('*Label*activeForeground', tk_style['Label']['activeForeground']),
            ('*Label*font', tk_style['Label']['font']),
            ('*Label*highlightBackground', bg_color),
            ('*Label*highlightColor', selected_bg_color),

            ('*Message*foreground', tk_style['Message']['foreground']),
            ('*Message*background', tk_style['Message']['background']),
            ('*Message*activeBackground', tk_style['Message']['activeBackground']),
            ('*Message*activeForeground', tk_style['Message']['activeForeground']),
            ('*Message*font', tk_style['Message']['font']),
            ('*Message*highlightBackground', bg_color),
            ('*Message*highlightColor', selected_bg_color),

            ('*Checkbutton*foreground', tk_style['Checkbutton']['foreground']),
            ('*Checkbutton*background', tk_style['Checkbutton']['background']),
            ('*Checkbutton*activeBackground', tk_style['Checkbutton']['activeBackground']),
            ('*Checkbutton*activeForeground', tk_style['Checkbutton']['activeForeground']),
            ('*Checkbutton*selectColor', tk_style['Checkbutton']['selectColor']),
            ('*Checkbutton*font', tk_style['Checkbutton']['font']),
            ('*Checkbutton*highlightBackground', bg_color),
            ('*Checkbutton*highlightColor', selected_bg_color),

            ('*Radiobutton*foreground', tk_style['Radiobutton']['foreground']),
            ('*Radiobutton*background', tk_style['Radiobutton']['background']),
            ('*Radiobutton*activeBackground', tk_style['Radiobutton']['activeBackground']),
            ('*Radiobutton*activeForeground', tk_style['Radiobutton']['activeForeground']),
            ('*Radiobutton*selectColor', tk_style['Radiobutton']['selectColor']),
            ('*Radiobutton*font', tk_style['Radiobutton']['font']),
            ('*Radiobutton*highlightBackground', bg_color),
            ('*Radiobutton*highlightColor', selected_bg_color),

            ('*Entry*foreground', tk_style['Entry']['foreground']),
            ('*Entry*background', tk_style['Entry']['background']),
            ('*Entry*selectForeground', tk_style['Entry']['selectForeground']),
            ('*Entry*selectBackground', tk_style['Entry']['selectBackground']),
            ('*Entry*font', tk_style['Entry']['font']),
            ('*Entry*highlightBackground', bg_color),
            ('*Entry*highlightColor', selected_bg_color),
            ('*Entry*insertBackground', tk_style['Entry']['foreground']),

            ('*Text*foreground', tk_style['Text']['foreground']),
            ('*Text*background', tk_style['Text']['background']),
            ('*Text*selectForeground', tk_style['Text']['selectForeground']),
            ('*Text*selectBackground', tk_style['Text']['selectBackground']),
            ('*Text*font', tk_style['Text']['font']),
            ('*Text*highlightBackground', bg_color),
            ('*Text*highlightColor', selected_bg_color),
            ('*Text*insertBackground', tk_style['Text']['foreground']),

            ('*Spinbox*foreground', tk_style['Spinbox']['foreground']),
            ('*Spinbox*background', tk_style['Spinbox']['background']),
            ('*Spinbox*selectForeground', tk_style['Spinbox']['selectForeground']),
            ('*Spinbox*selectBackground', tk_style['Spinbox']['selectBackground']),
            ('*Spinbox*font', tk_style['Spinbox']['font']),
            ('*Spinbox*highlightBackground', bg_color),
            ('*Spinbox*highlightColor', selected_bg_color),
            ('*Spinbox*insertBackground', tk_style['Spinbox']['foreground']),

            ('*Menubutton.foreground', tk_style['OptionMenu']['foreground']),
            ('*Menubutton.background', tk_style['OptionMenu']['background']),
            ('*Menubutton.activeBackground', tk_style['OptionMenu']['activeBackground']),
            ('*Menubutton.activeForeground', tk_style['OptionMenu']['activeForeground']),
            ('*Menubutton.font', tk_style['OptionMenu']['font']),
            ('*Menubutton*highlightBackground', tk_style['OptionMenu']['background']),
            ('*Menubutton*highlightColor', tk_style['OptionMenu']['activeForeground']),

            ('*Listbox*foreground', tk_style['Listbox']['foreground']),
            ('*Listbox*background', tk_style['Listbox']['background']),
            ('*Listbox*activeBackground', tk_style['Listbox']['activeBackground']),
            ('*Listbox*activeForeground', tk_style['Listbox']['activeForeground']),
            ('*Listbox*selectBackground', tk_style['Listbox']['selectBackground']),
            ('*Listbox*selectForeground', tk_style['Listbox']['selectForeground']),
            ('*Listbox*font', tk_style['Listbox']['font']),
            ('*Listbox*highlightBackground', bg_color),
            ('*Listbox*highlightColor', selected_bg_color),

            ('*Scrollbar*foreground', tk_style['Scrollbar']['foreground']),
            ('*Scrollbar*background', tk_style['Scrollbar']['background']),
            ('*Scrollbar*activeBackground', tk_style['Scrollbar']['activeBackground']),
            ('*Scrollbar*activeForeground', tk_style['Scrollbar']['activeForeground']),
            ('*Scrollbar*troughColor', tk_style['Scrollbar']['troughColor']),
            ('*Scrollbar*highlightBackground', bg_color),
            ('*Scrollbar*highlightColor', selected_bg_color),

            ('*Scale*foreground', tk_style['Scale']['foreground']),
            ('*Scale*background', tk_style['Scale']['background']),
            ('*Scale*activeBackground', tk_style['Scale']['activeBackground']),
            ('*Scale*activeForeground', tk_style['Scale']['activeForeground']),
            ('*Scale*troughColor', tk_style['Scale']['troughColor']),
            ('*Scale*font', tk_style['Scale']['font']),
            ('*Scale*highlightBackground', bg_color),
            ('*Scale*highlightColor', selected_bg_color),
        )
        #w.option_add('pattern',value, priority)
        for p, v in patterns:
            w.option_add(p, v)

    def apply_gtk_theme_noop(w):
        #No gtk installed
        pass

    apply_gtk_theme = apply_gtk_theme_noop
    if HAS_GTK:
        apply_gtk_theme = apply_gtk_theme_real


**Ejemplo:**

Descripcion: Crea 2 ventanas pequeñas iguales, una tratara de imitar el tema de GTK, la otra se mostrara como es por defecto.

::

    #!/usr/bin/env python2
    #-*- coding:utf-8 -*-

    #
    # test.py
    #

    import Tkinter as tk
    import colour

    class GtkOnTkApp(tk.Frame):
        '''Gtk on tk test"'''

        def __entry_scrollHandler(self, *L):
            op, howMany = L[0], L[1]
            if op == "scroll":
                units = L[2]
                self.entry.xview_scroll ( howMany, units )
            elif op == "moveto":
                self.entry.xview_moveto ( howMany )


        def __init__(self, master, title):
            tk.Frame.__init__(self, master)
            root = self.winfo_toplevel()

            o = tk.Label(self, text="Label: " + title)
            o.pack(side='top', pady=2)

            o = tk.Button(self, text="Button")
            o.pack(side='top', pady=2)

            self.entry = o = tk.Entry(self)
            o.insert('end', 'Entry + Scrollbar ' * 10)
            o.pack(side='top', pady=2)

            o = tk.Scrollbar(self,orient='horizontal', command=self.__entry_scrollHandler)
            o.pack(side='top', fill='x', pady=2)
            self.entry.configure(xscrollcommand=o.set)

            o = tk.Spinbox(self, from_=0, to=50)
            o.pack(side='top', pady=2)

            opciones = ('OptionMenu', 'Opcion2', 'Opcion3')
            self.ovar = tk.StringVar()
            self.ovar.set(opciones[0])
            o = tk.OptionMenu(self, self.ovar, *opciones)
            o.pack(side='top', pady=2)

            self.items = tk.StringVar()
            self.items.set('Listbox Item2 Item3')
            o = tk.Listbox(self, listvariable=self.items, height=3)
            o.pack(side='top', fill='x', pady=2)

            o = tk.Checkbutton(self,text='Checkbutton')
            o.pack(side='top', pady=2)

            self.rbar = tk.IntVar()
            self.rbar.set(0)
            o = tk.Radiobutton(self,text='Radiobutton1', value=0, variable=self.rbar)
            o.pack(side='top', pady=2)
            o = tk.Radiobutton(self,text='Radiobutton2', value=1, variable=self.rbar)
            o.pack(side='top', pady=2)

            o = tk.Scale(self,label='Scale', orient='horizontal')
            o.pack(side='top', fill='x', pady=2)

            o = tk.Message(self, text='Message widget')
            o.pack(side='top', fill='x', pady=2)

            o = tk.Text(self, height=4)
            o.insert('0.0', 'Text widget ' * 20)
            o.pack(side='top', pady=2)

            self.pack(expand=True, fill='both')

            # Menubar
            menubar = tk.Menu(root)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo", state='disabled')
            filemenu.add_command(label="Menuitem 2")
            filemenu.add_command(label="Menuitem 3")
            filemenu.add_separator()
            filemenu.add_command(label="Cerrar ✗", command= lambda: root.destroy())
            menubar.add_cascade(label="Archivo", menu=filemenu)
            root.config(menu=menubar)
            root.title(title)


    if __name__ == '__main__':
        root = tk.Tk()
        # Creamos una ventana sin estilos
        app1 = GtkOnTkApp(tk.Toplevel(), 'Ventana sin tema Gtk')

        # Definimos los estilos gtk. Despues de la llamada a apply_gtk_theme
        # los widgets que se crean posen "estilo" gtk:
        colour.apply_gtk_theme(root)
        #Creamos ventana con estilos
        app2 = GtkOnTkApp(root, 'Ventana con tema Gtk')
        root.mainloop()


Capturas:

`gtkontk01.png </images/GTKonTK/gtkontk01.png>`_

`gtkontk02.png </images/GTKonTK/gtkontk02.png>`_

.. ############################################################################




.. _base: /Proyectos/RevistaPythonComunidad/base
