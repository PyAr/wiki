.. title: GtkRichText


Ejemplo sobre cómo mostrar texto con formato en un gtk.TextView, se crea una clase que extiende gtk.TextBuffer para facilitar la inserción de texto con formato.

.. code-block:: python

    '''a module that contains a class to insert rich text into a textview'''

    import gtk
    import pango

    class RichBuffer(gtk.TextBuffer):
        '''a buffer that makes it easy to manipulate a gtk textview with
        rich text'''

        def __init__(self):
            '''constructor'''
            gtk.TextBuffer.__init__(self)

            self.colormap = gtk.gdk.colormap_get_system()

            self.fg_tags = {}
            self.bg_tags = {}
            self.font_tags = {}
            self.size_tags = {}
            self.bold_tag = self.create_tag("bold", weight=pango.WEIGHT_BOLD)
            self.italic_tag = self.create_tag("italic", style=pango.STYLE_ITALIC)
            self.underline_tag = self.create_tag("underline",
                underline=pango.UNDERLINE_SINGLE)
            self.strike_tag = self.create_tag("strike", strikethrough=True)

        def put_text(self, text, fg_color=None, bg_color=None, font=None, size=None,
            bold=False, italic=False, underline=False, strike=False):
            '''insert text at the current position with the style defined by the
            optional parameters'''
            tags = self._parse_tags(fg_color, bg_color, font, size, bold, italic,
                underline, strike)
            iterator = self.get_iter_at_mark(self.get_insert())
            self._insert(iterator, text, tags)

        def _insert(self, iterator, text, tags=None):
            '''insert text at the current position with the style defined by the
            optional parameters'''
            if tags is not None:
                self.insert_with_tags(iterator, text, *tags)
            else:
                self.insert(iterator, text)

        def _parse_tags(self, fg_color=None, bg_color=None, font=None, size=None,
            bold=False, italic=False, underline=False, strike=False):
            '''parse the parameters and return a list of tags to apply that
            format
            '''
            tags = []

            if fg_color:
                tag = self._parse_fg(fg_color)
                if tag:
                    tags.append(tag)

            if bg_color:
                tag = self._parse_bg(bg_color)
                if tag:
                    tags.append(tag)

            if font:
                tag = self._parse_font(font)
                if tag:
                    tags.append(tag)

            if size:
                tag = self._parse_size(size)
                if tag:
                    tags.append(tag)

            if bold:
                tags.append(self.bold_tag)

            if italic:
                tags.append(self.italic_tag)

            if underline:
                tags.append(self.underline_tag)

            if strike:
                tags.append(self.strike_tag)

            return tags

        def _parse_fg(self, value):
            '''parse the foreground color and return a tag'''
            if value in self.fg_tags:
                return self.fg_tags[value]

            try:
                color = gtk.gdk.color_parse(value)
                self.colormap.alloc_color(color)
            except ValueError:
                return None

            color_tag = self.create_tag('fg_' + value[1:], foreground_gdk=color)
            self.fg_tags[value] = color_tag

            return color_tag

        def _parse_bg(self, value):
            '''parse the background color and return a tag'''
            if value in self.bg_tags:
                return self.bg_tags[value]

            try:
                color = gtk.gdk.color_parse(value)
                self.colormap.alloc_color(color)
            except ValueError:
                return None

            color_tag = self.create_tag('bg_' + value[1:], background_gdk=color)
            self.bg_tags[value] = color_tag

            return color_tag

        def _parse_font(self, value):
            '''parse the font and return a tag'''
            if value in self.font_tags:
                return self.font_tags[value]

            font_tag = self.create_tag('font_' + value.replace(' ', '_'),
                font=value)
            self.font_tags[value] = font_tag

            return font_tag

        def _parse_size(self, value):
            '''parse the font size and return a tag'''
            if value in self.size_tags:
                return self.size_tags[value]

            size_tag = self.create_tag('size_' + str(value), size_points=value)
            self.size_tags[value] = size_tag
            return size_tag

    def test():
        '''do some tests with the buffer'''
        import sys
        def on_close(widget, event):
            '''method called when the window is closed'''
            sys.exit(0)

        window = gtk.Window()
        window.set_default_size(640, 480)
        window.connect('delete-event', on_close)
        textview = gtk.TextView()
        buff = RichBuffer()
        textview.set_buffer(buff)
        window.add(textview)
        window.show_all()
        buff.put_text('buenas, como va? ', '#CCCCCC', '#000000', 'Arial', 12)
        buff.put_text('esto es una prueba\n', '#CC0000', '#AAAAAA', 'Purisa', 14)
        buff.put_text('un poco de formato\n', '#00CC00', '#FFFFFF', 'Andale Mono',
            8, True, True, True, True)
        buff.put_text('un poco mas\n', '#CCCCCC', '#0000CC', 'Andale Mono', 16,
            False, True, False, True)
        gtk.main()

    if __name__ == '__main__':
        test()


.. image:: /images/Recetario/Gui/Gtk/RichText/GtkRichText.png

Más información:

* http://pygtk.org/docs/pygtk/

* http://www.gtk.org/api/2.6/gtk/GtkTextTag.html

* http://pygtk.org/docs/pygtk/class-gtktextbuffer.html

