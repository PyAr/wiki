
Esta página tiene como objetivo darle soporte al desafío planteado en el primer número de la revista PET.

*The goal of this page is to help with the challenge of the first PET issue.*

Ranking
=======

De esta página los participantes pueden bajar un programa que les permite validar su prorgama antes de enviarlo.

*You can download a program to test your solution.*

Uso/*Use*:

::

    some@example~:$ ./pet1-test.sh pet1-ejemplo.py


 (pet1-test2 no tiene en cuenta el stderr/ *pet-test2 is like 1 but without stderr*)

Los caracteres se cuentan con / *Characters are counted with:*

::

    some@example:~$ wc -c pet1-ejemplo.py

.. csv-table::
    :header: chars,script name,feedback con pet1-test,feedback con bignum

    106,pet1-piranna.py,<#FF0000> Falla para 0 y 1,OK
    111,pet1-pych3m4.py,OK,OK
    111,pet1-jmansilla.py,OK,OK
    111,pet1-hdzos.py,OK,OK
    112,pet1-fisadev.py,OK,OK
    115,pet1-matiasg.py,OK,OK
    117,pet1-fpalm.py,OK,OK
    120,pet1-fheinz.py,OK,<#FF0000> Falla con los casos de prueba 1048576 y mayores
    118,pet1-nicoreba.py,OK,OK
    123,pet1-ismael.py,OK,OK
    128,pet1-cballard.py,OK,<#FF0000> Falla con los casos de prueba 1048576 y mayores
    132,pet1-darni.py,OK,OK
    140,pet1-ivoscc.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    141,pet1-cromeovl.py,OK,OK
    150,pet1-rarmas.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    152,pet1-pepecuis.py,OK,OK
    153,pet1-matiasbellone.py,OK,OK
    154,pet1-sergiogragera.py,<#FF0000> Falla con 1024,<#FF0000> Falla con 2204362183931003246689498147640480133808128
    159,pet1-shariff.py,OK,OK
    160,pet1-anguiam.py,<#FF0000> Texto extra en la entrada/salida,
    164,pet1-vegacom.py,<#FF0000> Falla con 0 y 1,
    165,pet1-tavotell.py,<#FF0000> Inclueye un \b en las salidas con ^,
    167,pet1-eordano.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    170,pet1-lechon.py,<#FF0000> Espacio en blanco al final de la salida,
    176,pet1-casoalonso.py,<#FF0000> Texto extra en la entrada/salida,
    181,pet1-sedivy.py,<#FF0000> EOFError,
    191,pet1-gedece.py,OK,OK
    191,pet1-listas.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    192,pet1-utn.py,<#FF0000> Espacio en blanco al final de la salida,
    193,pet1-anguiam.py,<#FF0000> Texto extra en la entrada/salida,
    201,pet1-sergiogragera.py,<#FF0000> Faltan espacios en blanco alrededor de \*,
    203,pet1-volpe.py,OK,OK
    203,pet1-hpmaxi.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    207,pet1-soy_zco.py,OK,OK
    210,pet1-mctpyt.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    211,pet1-tokland.py,OK,<#FF0000> Falla con los casos de prueba 4294967296 y mayores
    213,pet1-zalaka.py,<#FF0000> Falla con 1,
    249,pet1-ajzach.py,<#FF0000> IndexError,
    262,pet1-cdipietro.py,<#FF0000> Texto extra en la entrada/salida,
    263,pet1-lvidarte.py,OK,<#FF0000> No termina con valores mayores a 1048576
    325,pet1-radicaled.py,<#FF0000> Da salidas erroneas,
    344,pet1-fanaur.py,OK,OK
    336,pet1-wasuaje.py,OK,<#FF0000> Falla con  2204362183931003246689498147640480133808128
    393,pet1-camilotorresf.py,<#FF0000> Dos espacios en blanco entre los símbolos x,
    438,pet1-mr.py,<#FF0000> Falla para 0 y 1,OK
    449,pet1-ramonvillalongagomez.py,<#FF0000> Texto extra en la entrada/salida,
    482,pet1-marcolucio.py,<#FF0000> Espacios en blanco alrededor de ^,
    518,pet1-hpmaxi.py,<#FF0000> Texto extra en la entrada/salida,
    528,pet1-rodrigoolmo.py,<#FF0000> Texto extra en la entrada/salida,
    540,pet1-juanpablojuanpablo.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    625,pet1-abel.py,OK,<#FF0000> Falla con los casos de prueba 1073741824 y mayores
    749,pet1-dmlistapython.py,<#FF0000> Texto extra en la entrada/salida,
    977,pet1-wasuaje.py,<#FF0000> Texto extra en la entrada/salida,
    968,pet1-duducosmos.py,<#FF0000> No produce salida,
    1052,pet1-rodrigoolmo.py,<#FF0000> Texto extra en la entrada/salida y no funciona para 1024,
    1702,pet1-rigoni.py,<#FF0000> Texto extra en la entrada/salida,


Trampas copadas/Funny cheat
===========================

Escribir un enunciado es realmente difícil. Algunos abusándose de nuestra debilidad han enviado algunas entradas que se riñen con la moral y las buenas costumbres. De todas formas les damos un lugar destacado!

*Write a challenge is really difficult. Some of you have taken advantages of our weakness and sent us solutions that are not so legal.*

.. csv-table::
    :header: chars,script name,feedback con pet1-test,feedback con bignum

    55,darni,OK,OK
