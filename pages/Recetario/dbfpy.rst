
DbfPy
-----

Descripción
:::::::::::

Esta receta es un ejemplo de como acceder nativamente desde Python a bases de datos en formato DBF (dBase, Foxpro, Clipper, etc.), sin necesidad de ODBC u otras herramientas.

Utiliza DbfPy_. Para instalar la libreria, bajarla y descomprimirla con 7-Zip en el directorio de la aplicación o en site-packages (C:\python25\lib\site-packages o similar).

**Nota**: Para nuevos proyectos utilizar una base de datos relacional (ej. PostgreSQL o MySQL), o usar shelf para guardar objetos python facilmente.

Ejemplo:
::::::::

Ejemplo original traducido y ajustado:

::

    # -*- coding: iso-8859-1 -*-

    from dbfpy.dbf import Dbf, DbfRecord

    # abro el archivo country.dbf(viene como ejemplo dentro de la libreria)
    dbf1 = Dbf()
    dbf1.openFile('dbfpy/county.dbf', readOnly=0)
    dbf1.reportOn()
    print 'registros de ejemplo:'

    # recorro los registros:
    for registro in dbf1:
        # recorro los campos:
        for nombre_campo in dbf1.fieldNames():
            print '%s:\t %s' % (nombre_campo, registro[nombre_campo])
        print


    # agregar un registro (campos COUNTYNO, COUNTYNAME, COUNTYABBR)
    reg=DbfRecord(dbf1)
    reg['COUNTYNO']=116
    reg['COUNTYNAME']="Prueba"
    reg['COUNTYABBR']="PRUE"
    #reg['FECHA']=(2000,1,12)
    reg.store()


    # cierro el archivo
    dbf1.close()


Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _DbfPy: http://dbfpy.sourceforge.net/

.. _marianoreingart: /pages/marianoreingart.html
.. _categoryrecetas: /pages/categoryrecetas.html
