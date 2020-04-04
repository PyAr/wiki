.. title: Iterar sobre pares

¿Como iterar por ejemplo la secuencia [1,2,3,4,5,6] para que cada item sea: (1,2), (3,4), (5,6)?

.. code-block:: pycon

    >>> seq = [1,2,3,4,5,6,7]
    >>> i = iter(seq)
    >>> for x in zip(i,i):
    ...     print x
    ...
    (1, 2)
    (3, 4)
    (5, 6)

