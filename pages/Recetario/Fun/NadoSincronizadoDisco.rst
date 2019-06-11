
Nado Sincronizado
-----------------

un generador de nado sincronizado con luces de colores usando colorama (sudo pip install colorama)

::

    import sys
    import time
    import random
    from colorama import init, Fore
    ARM = ['\\', '_', '/', ' ']

    def figure():
        color = Fore.__dict__[random.choice(['BLACK', 'BLUE', 'CYAN',
            'GREEN', 'MAGENTA', 'RED', 'RESET', 'WHITE', 'YELLOW'])]
        fig = color + random.choice(ARM) + "o" + random.choice(ARM)
        sys.stdout.write(fig)
        sys.stdout.flush()

    def erase():
        sys.stdout.write("\b\b\b")
        sys.stdout.flush()

    def dance():
        init()
        while True:
            figure()
            time.sleep(0.5)
            erase()

    if __name__ == '__main__':
        dance()

