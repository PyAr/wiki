.. title: Votación PyCamp 2013


El resultado de la votación fue:

::

      84 Hotel Luz y Fuerza
      75 Hostal Colonial Serrano
      72 Verónica
      47 Villa Maristas Lujan
      24 Villa Maristas Mar del Plata

Estas fueron las votaciones en detalle:

::

   Facundo Batista
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Lujan
   Hotel Luz y Fuerza

   Daniel F. Moisset
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Sergio Schvezov
   Hotel Luz y Fuerza
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano

   Alejandro J. Cura
   Hostal Colonial Serrano
   Verónica
   Hotel Luz y Fuerza

   Emiliano Dalla Verde Marcozzi
   Hostal Colonial Serrano
   Hotel Luz y Fuerza
   Verónica

   Marcos Vanetta
   Villa Maristas Lujan
   Verónica
   Hotel Luz y Fuerza

   Natalia Bidart
   Hostal Colonial Serrano
   Hotel Luz y Fuerza
   Villa Maristas Lujan

   Juan Pedro Fisanotti
   Villa Maristas Lujan
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Erwin Feser
   Hostal Colonial Serrano
   Hotel Luz y Fuerza

   Juan A. Diaz
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano
   Hotel Luz y Fuerza

   Hernan Lozano
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Mar del Plata

   Agustin Henze
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Santiago Piccinini
   Villa Maristas Lujan
   Verónica

   Diego Sarmentero
   Hostal Colonial Serrano
   Verónica
   Hotel Luz y Fuerza

   Jairo Trad
   Verónica
   Villa Maristas Mar del Plata
   Hostal Colonial Serrano

   Pablo Mouzo
   Verónica
   Villa Maristas Lujan

   Federico M. Peretti
   Verónica
   Villa Maristas Lujan
   Villa Maristas Mar del Plata

   Matías Bordese
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Leandro Nahuel Roque Poblet
   Hotel Luz y Fuerza
   Villa Maristas Lujan
   Verónica

   Ricardo Kirkner
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica
   Villa Maristas Lujan

   Sanchez Héctor
   Verónica
   Villa Maristas Mar del Plata
   Villa Maristas Lujan

   Francisco Capdevila
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Villa Maristas Lujan

   Elías Andrawos
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Villa Maristas Lujan
   Villa Maristas Mar del Plata
   Verónica

   Felipe Lerena
   Hotel Luz y Fuerza
   Hostal Colonial Serrano
   Verónica

   Claudio Canepa
   Verónica
   Hotel Luz y Fuerza
   Villa Maristas Lujan

Las cuales se evaluaron con el siguiente script:

::

    # ¡Py3!

    import operator

    # this is the total number of possibilites open to vote
    TOP_SCORE = 5

    class ResultCalculator:
        """Calculate the voting result."""
        def __init__(self):
            self._count = {}

        def vote(self, block):
            """Feed the voting blocks."""
            # first line is a header, the rest are votes
            votes = block[1:]

            # score are descending
            for place, score in zip(votes, range(TOP_SCORE, 0, -1)):
                self._count[place] = self._count.get(place, 0) + score

        def print_result(self):
            """Show the result."""
            result = sorted(self._count.items(),
                            key=operator.itemgetter(1), reverse=True)
            for place, score in result:
                print("{:5d} {}".format(score, place))

    with open("voto_pycamp.txt", encoding="utf8") as fh:
        block = []
        rc = ResultCalculator()
        for line in fh:
            line = line.strip()
            if line:
                block.append(line)
            else:
                # empty line: block delimiter
                rc.vote(block)
                block = []
        rc.vote(block)

    print("Resultado:")
    rc.print_result()

