.. title: GtkGladeHolaMundoOO


ejemplo que carga la interfaz de un archivo .glade y lo muestra, el archivo .glade puede tener cualquier contenido mientras la ventana tenga el nombre "ventana"

gtk-glade-holamundo.glade
~~~~~~~~~~~~~~~~~~~~~~~~~

copiar el contenido siguiente a un archivo llamado **gtk-glade-holamundo.glade** el archivo fue editado con glade-3_.

::

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE glade-interface SYSTEM "glade-2.0.dtd">
    <!--Generated with glade3 3.4.2 on Sat May 10 01:13:03 2008 -->
    <glade-interface>
      <widget class="GtkWindow" id="ventana">
        <property name="title" translatable="yes">hola mundo glade</property>
        <property name="window_position">GTK_WIN_POS_CENTER</property>
        <property name="default_width">200</property>
        <property name="default_height">200</property>
        <signal name="delete_event" handler="on_ventana_delete_event"/>
        <child>
          <widget class="GtkLabel" id="label">
            <property name="visible">True</property>
            <property name="label" translatable="yes">hola pyar!</property>
          </widget>
        </child>
      </widget>
    </glade-interface>


el codigo para el ejemplo es el siguiente

::

    import gtk
    import sys
    import gtk.glade

    class HolaMundo(object):
        '''clase que muestra un hola mundo desde un archivo glade'''

        def __init__(self):
            '''constructor'''
            self.tree = gtk.glade.XML("gtk-glade-holamundo.glade")
            self.tree.signal_autoconnect(self)
            self.window = self.tree.get_widget("ventana")

        def on_ventana_delete_event(self, window, event):
            '''callback llamado cuando se cierra la ventana'''
            sys.exit(0)

        def show(self):
            '''muestra la ventana principal'''
            self.window.show_all()

    if __name__ == "__main__":
        hola = HolaMundo()
        hola.show()
        gtk.main()


.. ############################################################################

.. _glade-3: http://glade.gnome.org/

