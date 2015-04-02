
Interceptar Prints
------------------

Esto sirve para modificar los strings que se vayan a imprimir, por ejemplo para agregarles un timestamp o algo similar. En este ejemplo lo usamos para redefinir "2" y "4". Probado en Python 2 y Python 3.

::

    import sys

    class FakeStdout:
        def write(self, s):
            s = s.replace("2", "3")
            s = s.replace("4", "6")
            real_stdout.write(s)
        def flush(self):
            real_stdout.flush()

    real_stdout = sys.stdout
    sys.stdout = FakeStdout()


    print(2)
    print(2 + 2)

