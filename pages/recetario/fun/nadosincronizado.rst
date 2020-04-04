.. title: Nado Sincronizado


un generador de nado sincronizado

`[[Video(http://marianoguerra.com.ar/random/nado.ogv)]]`_

.. code-block:: python

    import sys
    import time
    import random

    ARM = ['\\', '_', '/', ' ']

    def figure():
        fig = random.choice(ARM) + "o" + random.choice(ARM)
        sys.stdout.write(fig)
        sys.stdout.flush()

    def erase():
        sys.stdout.write("\b\b\b")
        sys.stdout.flush()

    def dance():
        while True:
            figure()
            time.sleep(0.5)
            erase()

    if __name__ == '__main__':
        dance()

