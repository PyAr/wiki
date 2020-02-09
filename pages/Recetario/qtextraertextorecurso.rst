
Extraer un archivo de texto embebido en un recurso .qrc
-------------------------------------------------------

Ademas de poder embeber imágenes, la librería Qt (y por ende PyQt) también permite incluir otros elementos en su sistema de recursos. La función que se define a continuación permite leer los contenidos de un archivo de texto plano que se encuentre registrado en un archivo .qrc. Cabe agregar que antes de invocar a ``loadTextFileFromRc()`` hay que convertir el .qrc a módulo de Python con la herramienta pyrcc4 (por ejemplo, en una terminal de GNU/Linux: ``$ pyrcc4 -o resources.py resources.qrc``). Esto puede ser útil para incorporar al programa una hoja de estilo que se aplique a toda la aplicación.

::

    # -*- coding: utf-8 -*-


    from PyQt4 import QtCore

    # El siguiente import realizará el registro de los recursos a PyQt.
    import resources


    def loadTextFileFromRc(rcPath):
        u"""Extrae el contenido de un archivo de texto incluido en el sistema
        de recursos.
            
        Parámetros:
            rcPath: ruta absoluta del archivo dentro del recurso. Por ejemplo:
                ':/app/css/style.css'.
        """

        q_file = QtCore.QFile(rcPath)
        q_file.open(QtCore.QIODevice.ReadOnly)
        q_text_stream = QtCore.QTextStream(q_file)
        content =  q_text_stream.readAll()
        q_file.close()

        return content


    if __name__ == '__main__':
        print loadTextFileFromRc(':/ruta/al/recurso.txt')


-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas/index.html
