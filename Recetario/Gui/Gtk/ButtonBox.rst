= ButtonBox =

este ejemplo muestra como usar un contenedor de botones para agregar botones y hacer que mantengan su tamanio óptimo y se distribuyan por la pantalla de manera homogénea.

{{{
#!code python
import gtk

window = gtk.Window()

vbox = gtk.VBox()

hbox1 = gtk.HButtonBox()
hbox1.pack_start(gtk.Button(stock=gtk.STOCK_OK))

hbox2 = gtk.HButtonBox()
hbox2.pack_start(gtk.Button(stock=gtk.STOCK_YES))
hbox2.pack_start(gtk.Button(stock=gtk.STOCK_NO))

vbox.pack_start(hbox1)
vbox.pack_start(hbox2)

window.add(vbox)
window.show_all()

window.connect('destroy', gtk.main_quit)

gtk.main()
}}}

== Mas Información ==

 * http://pygtk.org/docs/pygtk/class-gtkhbuttonbox.html
 * http://pygtk.org/docs/pygtk/class-gtkbuttonbox.html
 * http://pygtk.org/docs/pygtk/class-gtkbox.html
