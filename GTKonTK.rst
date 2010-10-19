= GTK on TK =

Usar temas de GTK en las aplicaciones de TKinter, no requiere ttk, funciona en KDE.

'''Foto de Pantalla:''' 

De fondo Gedit en Ubuntu, usando el tema Ambiance, arriba una ventana con similar tema pero en TK, a su lado una ventana TK por defecto.

 ~-El codigo de este ejemplo esta mas abajo ''(la foto no esta editada, no hay truco, funciona en KDE, o inclusive lo he hecho funcionar sin GTK instalado)''.-~

{{attachment:gtk-on-tk-hack.jpg}}

'''El Codigo para hacer GTK on TK:'''

{{{
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
}}}

------

'''Ejemplo:'''

Descripcion: Crea 2 ventanas pequeñas iguales, una tratara de imitar el tema de GTK, la otra se mostrara como es por defecto.

~-''(el ejemplo funciona en Ubuntu, que es lo que yo uso, usa el codigo de arriba, lejos de estar bien hecho, pero sirve de ejemplo)''.-~

{{{
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
}}}

Comentario personal: 

''Es mas bonito que TTK  :)  Como sea, la idea es aprovechar que en Linux TODO es un archivo, la magia esta en parsear.''
