.. title: GtkRunner


ejemplo de como correr funciones que demoran sin bloquear la ui y obtener los resultados en el thread de gtk

lo que tienen que reusar es la clase GtkRunner_

simplemente la llaman pasandole:

* callback función o método que va a ser llamado en el main thread una vez que la función que demora termine

* func: función a llamar

* de 0 a n argumentos posicionales que serán pasados a func en la llamada

* de 0 a n argumentos nombrados que serán pasados a func en la llamada

func(\*args, \*\*kwargs) sera llamada en un thread aparte el cual sera monitoreado periódicamente por su finalizacion, una vez terminado llamara a callback pasandole una tupla cuyo primer elemento es True si la función termino con éxito y False si la función lanzo una excepción. El segundo elemento de la tupla es el valor retornado por la función si tuvo éxito o la excepción lanzada en caso que haya fallado.

obviamente en la función esa no pueden correr código relacionado con gtk

::

    '''example of a generic class to run a given function in a thread and call a
    callback in the main thread with the result of the function'''

    import gtk
    import glib
    import time
    import Queue
    import urllib
    import threading

    class GtkRunner(threading.Thread):
        '''run *func* in a thread with *args* and *kwargs* as arguments, when
        finished call callback with a two item tuple containing a boolean as first
        item informing if the function returned correctly and the returned value or
        the exception thrown as second item
        '''

        def __init__(self, callback, func, *args, **kwargs):
            threading.Thread.__init__(self)
            self.setDaemon(True)

            self.callback = callback
            self.func = func
            self.args = args
            self.kwargs = kwargs

            self.result = Queue.Queue()

            self.start()
            glib.timeout_add_seconds(1, self.check)

        def run(self):
            '''
            main function of the thread, run func with args and kwargs
            and get the result, call callback with the (True, result)

            if an exception is thrown call callback with (False, exception)
            '''
            try:
                result = (True, self.func(*self.args, **self.kwargs))
            except Exception, ex:
                result = (False, ex)

            self.result.put(result)

        def check(self):
            '''
            check if func finished
            '''
            try:
                result = self.result.get(False, 0.1)
            except Queue.Empty:
                return True

            self.callback(result)
            return False


    def main():
        '''
        main function called when the module is run from the command line
        '''

        def return_slow(result, sleep=5):
            '''
            a demo function that returns result slowly
            '''
            time.sleep(sleep)
            return result

        def fail_slow(message, sleep=5):
            '''
            a demo function that raises an exception slowly
            '''
            time.sleep(sleep)
            raise Exception(message)

        def load_site(url):
            '''
            a demo function that loads the content of a url
            '''
            return urllib.urlopen(url).read()

        class Display(gtk.Window):
            '''
            a window to display some content that loads slowly
            '''

            def __init__(self, text, func, *args, **kwargs):
                gtk.Window.__init__(self)
                self.set_default_size(400, 300)
                self.set_title("display")
                self.set_border_width(2)

                self.func = func
                self.args = args
                self.kwargs = kwargs

                vbox = gtk.VBox(spacing=2)
                scroll = gtk.ScrolledWindow()
                self.text = gtk.TextView()
                self.text.get_buffer().set_text(text)

                scroll.add(self.text)

                vbox.pack_start(scroll, True, True)

                self.loading = gtk.ProgressBar()
                self.is_loading = False

                vbox.pack_start(self.loading, False)

                buttons = gtk.HButtonBox()
                self.run = gtk.Button(stock=gtk.STOCK_EXECUTE)
                self.run.connect('clicked', self._on_run_clicked)
                buttons.pack_start(self.run)

                vbox.pack_start(buttons, False)

                self.add(vbox)

                vbox.show_all()
                self.loading.hide()
                self.connect("delete-event", gtk.main_quit)

            def _on_run_clicked(self, button):
                self.set_loading()
                GtkRunner(self._on_result_ready, self.func, *self.args,
                        **self.kwargs)

            def set_loading(self, is_loading=True):
                '''
                set the window to the loading state
                '''
                self.is_loading = is_loading
                self.run.set_sensitive(not is_loading)

                if is_loading:
                    self.loading.show()
                    glib.timeout_add(500, self._make_progress_bar_go_crazy)
                else:
                    self.loading.hide()

            def _on_result_ready(self, result):
                status, value = result
                self.set_loading(False)

                if status:
                    content = str(value)
                else:
                    content = "exception running function: %s" % str(value)

                self.text.get_buffer().set_text(content)

            def _make_progress_bar_go_crazy(self):
                if self.is_loading:
                    self.loading.pulse()

                return self.is_loading

        gtk.gdk.threads_init()
        Display("show text after some seconds", return_slow, "I load slowly").show()
        Display("raise an exception after some seconds", fail_slow,
                "I fail slowly").show()
        Display("load the content of website", load_site,
                "http://marianoguerra.com.ar").show()
        gtk.main()

    if __name__ == '__main__':
        main()

