.. title: Gtk Auto Complete


ejemplo de campo de texto con auto complesion

::

    import gtk

    class Complete(gtk.Entry):
        '''a class to autocomplete'''

        def __init__(self, *words):
            gtk.Entry.__init__(self)
            self.completion = gtk.EntryCompletion()
            self.set_completion(self.completion)
            self.model = gtk.ListStore(str)
            self.completion.set_model(self.model)
            self.completion.set_text_column(0)

            for word in words:
                self.remember(word)

        def remember(self, value):
            '''add a value to the list of strings to suggest'''
            self.model.append([value])

    if __name__ == '__main__':
        window = gtk.Window()
        complete = Complete("python", "pyar", "span", "eggs")
        window.add(complete)
        window.connect('delete-event', gtk.main_quit)
        window.show_all()
        gtk.main()

