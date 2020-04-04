.. title: Codigo1

PRUEBA:

.. code-block:: python

    #!/usr/bin/env python

    import sqlite3

    # leo DB #dbfn = 'allseqs-AR.db' dbfn = '../AS/allseqs-AS.db' conn = sqlite3.connect(dbfn) c = conn.cursor() # CREATE TABLES c.execute("SELECT ctgID,read from ctgs") for row in c:

    ctg = row[0] lib = row[1].split('-')[0][-3:]

klkl

