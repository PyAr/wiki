
aLetras
-------

Descripción
:::::::::::

*aLetras(numero)* es una función a la que se le pasa un valor númerico y regresa un string con el valor numérico convertido a letras.

Los valores que pueden ser convertidos pertenecen al rango *-999.999.999,99 : 999.999.999,99*. Si se proporciona una cadena fuera de rango, retorna el string "0".

Siempre se trabaja con 2 decimales (se redondean los valores suministrados)

Ejemplos:
:::::::::

::

    >>> aLetras(1234.56)
    ' MIL DOSCIENTOS TREINTA Y CUATRO CON CINCUENTA Y SEIS CENTAVOS'
    >>> aLetras(-240.99)
    'MENOS DOSCIENTOS CUARENTA CON NOVENTA Y NUEVE CENTAVOS'
    >>> aLetras(100)
    'CIEN'
    >>> aLetras(401201501.01)
    'CUATROCIENTOS UN MILLON DOSCIENTOS UN MIL QUINIENTOS UNO CON UN CENTAVOS'
    >>> aLetras(-0.76)
    'MENOS CERO CON SETENTA Y SEIS CENTAVOS'
    >>> aLetras(1000000000)
    '0'


Observaciones
:::::::::::::

La asignación y condicional en una línea -> numeros[1] = "UNO" if i == 2 else "UN" <- da problemas de sintaxis con versiones anteriores a Python 2.5.x

Puede reemplazarse con:

::

    if i == 2:
      numeros[1] = "UNO"
    else:
      numeros[1] = "UN"


Código:
:::::::

::

    #fuente: Recetario de PyAR, http://python.com.ar/moin/Recetario
    #autor: Cesar E Portela
    #date: 06-05-2008
    #version: 2
    #para Python: 2.5.x

    def aLetras(numero):

        numeros = {0:"CERO",2:"DOS",3:"TRES",4:"CUATRO",5:"CINCO",6:"SEIS",7:"SIETE",8:"OCHO",9:"NUEVE",
                    10:"DIEZ",11:"ONCE",12:"DOCE",13:"TRECE",14:"CATORCE",15:"QUINCE",16:"DIECISEIS",17:"DIECISIETE",
                    18:"DIECIOCHO",19:"DIECINUEVE",20:"VEINTE",30:"TREINTA",
                    40:"CUARENTA",50:"CINCUENTA",60:"SESENTA",70:"SETENTA",80:"OCHENTA",90:"NOVENTA",100:"CIEN",
                    500:"QUINIENTOS ",700:"SETECIENTOS ",900:"NOVECIENTOS "}

        if abs(numero) > 999999999.99 : #mil millones, esta funcion procesa el rango [-999.999.999,99; 999.999.999,99]
            return ("0", 0)
        elif numero < 0:
            cadena = "MENOS "
        else:
            cadena = ""

        #separo el numero entregado entre parte entera y sus decimales (tomando solo 2 y redondeando para arriba)
        entero = int(abs(numero))
        decimales = int((round(abs(numero), 2) + 0.001) * 100) % 100

        #la parte entera es separada en grupos de tres digitos
        grupo1 = int(entero / 1000000)
        grupo2 = int((int(entero) - int(grupo1)*1000000)/1000)
        grupo3 = int(entero % 1000)

        lista = [grupo1, grupo2, grupo3, decimales]

        if (grupo1 + grupo2 + grupo3) == 0:
            cadena += numeros[0]

        for i in xrange(4):
            unidad = lista[i] % 10
            decena = lista[i] % 100
            centena = (lista[i] / 100) % 10
            subcadena = ""

            numeros[1] = "UNO" if i == 2 else "UN"

            if i == 0: #grupo 1: el de los millones
                if decena == 1:
                    subcadena = " MILLON "
                elif lista[i] > 1:
                    subcadena = " MILLONES "
                else: #aqui se entra si lista[i] == 0 y en ese caso, no hay nada que procesar
                    continue #se sigue con la siguiente iteracion del bucle

            elif i == 1: #grupo2: el de los miles
                if lista[i] == 1:
                    cadena += " MIL "
                    continue #se pasa a la siguiente iteracion
                elif lista[i] > 1:
                    subcadena = " MIL "
                else: #aqui se entra si lista[i] == 0 y en ese caso, no hay nada que procesar
                    continue #se sigue con la siguiente iteracion del bucle

            elif i == 3 and lista[i] != 0: #grupo4: el de los centavos (decimales)
                cadena += " CON "
                subcadena = " CENTAVOS"

            if centena != 0:
                if centena == 1 and (unidad + decena) == 0:
                    cadena += numeros[100]
                    continue
                elif centena == 1:
                    cadena += "CIENTO "
                elif centena == 5:
                    cadena += numeros[500]
                elif centena == 7:
                    cadena += numeros[700]
                elif centena == 9:
                    cadena += numeros[900]
                else:
                    cadena += numeros[centena] + "CIENTOS "

            if decena != 0:
                if decena < 21:
                    cadena += numeros[decena]
                elif decena < 30:
                    cadena += "VENTI"+numeros[unidad]
                else:
                    cadena += numeros[(decena/10)*10]
                    if unidad > 0:
                        cadena += " Y "+numeros[unidad]

            cadena += subcadena

        return cadena


Autor / Autores:
::::::::::::::::

CesarPortela

.. ############################################################################


