
GtkStatusIcon
-------------

Aplicación con ícono en el area de notificaciones.

Tiene un menú contextual (About/Quit) y con el botón izquierdo abre una ventana simple.

`trayapp.png </images/Recetario/Gui/Gtk/StatusIcon/trayapp.png>`_

::

    '''Mini ejemplo de system tray app.'''

    import gtk

    class TrayApp:

        def __init__(self):
            self.statusicon = gtk.StatusIcon()
            self.statusicon.set_from_stock(gtk.STOCK_INFO)
            self.statusicon.set_tooltip('StatusIcon Example')
            self.statusicon.connect('popup-menu', self.right_click_event)
            self.statusicon.connect('activate', self.left_click_event)

        def left_click_event(self, status_icon):
            # Para que solo abra una ventana
            if not getattr(self, 'window', None):
                self.label = gtk.Label('Hola pyar')
                self.window = gtk.Window()
                self.window.set_default_size(200, 200)
                self.window.set_title('Hello world')
                self.window.connect('delete_event', self.exit_window)
                self.window.add(self.label)
                self.window.show_all()

        def exit_window(self, widget, event, data=None):
            del self.window

        def right_click_event(self, status_icon, button, activate_time):
            menu = gtk.Menu()
            about = gtk.MenuItem('About')
            quit = gtk.MenuItem('Quit')
            about.connect('activate', self.show_about_dialog)
            quit.connect('activate', gtk.main_quit)
            menu.append(about)
            menu.append(quit)
            menu.show_all()
            menu.popup(None, None, gtk.status_icon_position_menu,
                       button, activate_time, self.statusicon)

        def show_about_dialog(self, widget):
                    about_dialog = gtk.AboutDialog()
                    about_dialog.set_destroy_with_parent(True)
                    about_dialog.set_name('StatusIcon Example')
                    about_dialog.set_version('1.0')
                    about_dialog.set_authors(['Name Lastname'])
                    about_dialog.run()
                    about_dialog.destroy()

        def main(self):
            gtk.main()

    if __name__ == '__main__':
        tray_app = TrayApp()
        tray_app.main()


Más info en http://www.learnpygtk.org/pygtktutorial/statusicon.html

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /categoryrecetas
