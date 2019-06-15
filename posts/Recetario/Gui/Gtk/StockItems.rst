
Gtk stock items
===============

ejemplo que muestra todos los iconos stock de gtk con su respectivo nombre 

un screenshot:

`stock-gtk.png </wiki/Recetario/Gui/Gtk/StockItems/attachment/581/stock-gtk.png>`_

::

    '''modulo que muestra el uso de los stock icons en gtk'''
    import gtk

    def run():
        '''muestra una ventana con algunos elementos con stock icons'''
        ventana = gtk.Window()
        ventana.set_default_size(400, 400)

        box = gtk.VBox(spacing=4)

        for id in gtk.stock_list_ids():
            imagen = gtk.Image()
            imagen.set_from_stock(id, gtk.ICON_SIZE_BUTTON)

            etiqueta = gtk.Label("gtk.STOCK" + id[3:].replace("-", "_").upper())
            etiqueta.set_alignment(0.0, 0.5)

            caja = gtk.HBox()

            caja.pack_start(imagen, False)
            caja.pack_start(etiqueta)

            box.pack_start(caja)

        scroll = gtk.ScrolledWindow()
        scroll.add_with_viewport(box)
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        ventana.add(scroll)

        ventana.connect('delete-event', gtk.main_quit)
        ventana.show_all()
        gtk.main()


    if __name__ == '__main__':
        run()


-------------------------



  CategoryRecetas_

