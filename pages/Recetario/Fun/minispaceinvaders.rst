.. title: Mini space invaders


Un mini space invaders usando caracteres, la nave dispara a quemarropas en una lucha contra el bicho, nadie sabe cuanto durará esta cacería, que lo disfruten:

* La nave y el bicho se mueven solos de forma aleatoria.

* La nave dispara de forma aleatoria.

* Todo esta en un spanglish feo.

* Se podría agregar manejo de eventos de teclado para manejar la nave y los disparos. Alguna idea usando módulo estándar de python?

* En cuanto pueda pongo un videito.

::

    import random
    import time
    import os


    ROWS = 14
    COLS = 16
    BULLET = '.'
    SHOTS = []
    SCREEN = []
    EMPTY = ' '
    EXPLOSION = '#'
    SHIP = 'A'
    BUG = 'W'


    ###############################################################################
    # Funciones del mundo
    ###############################################################################
    def crear_mapa():
        for row in range(0, ROWS):
            SCREEN.append([])
            for col in range(0, COLS):
                SCREEN[row].append(EMPTY)


    def mostrar_mapa():
        for row in SCREEN:
            for col in row:
                print col,
            print


    def mover_disparos():
        for disparo in SHOTS:
            SCREEN[disparo[0]][disparo[1]] = EMPTY
            if disparo[0] > 0:
                if SCREEN[disparo[0] - 1][disparo[1]] == BUG:
                    SCREEN[disparo[0] - 1][disparo[1]] = EXPLOSION
                    return False
                else:
                    SCREEN[disparo[0] - 1][disparo[1]] = BULLET
                    SHOTS.append((disparo[0] - 1, disparo[1]))
            SHOTS.remove(disparo)
        return True


    def _mover_nave(direccion, nave, row):
        try:
            col = SCREEN[row].index(nave)
        except ValueError:
                col = 0
        SCREEN[row][col] = EMPTY
        next_col = col + (1 * direccion)
        if next_col > 15:
            next_col = 0
        SCREEN[row][next_col] = nave


    def limpiar_pantalla():
        os.system(['clear', 'cls'][os.name == 'nt'])


    ###############################################################################
    # Funciones para la nave
    ###############################################################################
    def crear_nave():
        SCREEN[-1][random.randint(0, COLS - 1)] = SHIP


    def mover_nave():
        if random.randint(0, 100) > 50:
            _mover_nave(-1, SHIP, -1)
        else:
            _mover_nave(1, SHIP, -1)


    def disparar():
        if random.randint(0, 100) > 70:
            col = SCREEN[-1].index(SHIP)
            SCREEN[-2][col] = BULLET
            row = ROWS - 2
            SHOTS.append((row, col))


    ###############################################################################
    # Funciones para el bicho
    ###############################################################################
    def crear_bicho():
        SCREEN[0][random.randint(0, COLS - 1)] = BUG


    def mover_bicho():
        if random.randint(0, 100) > 50:
            _mover_nave(-1, BUG, 0)
        else:
            _mover_nave(1, BUG, 0)


    def jugar():
        crear_mapa()
        crear_nave()
        crear_bicho()
        while mover_disparos():
            mover_bicho()
            disparar()
            mover_nave()
            mostrar_mapa()
            time.sleep(0.2)
            limpiar_pantalla()
        limpiar_pantalla()
        mostrar_mapa()
        print "EL BICHO SE MURIO"


    if __name__ == '__main__':
        jugar()

