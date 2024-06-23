.. title: Autocomplecion en consola interactiva


(donado por Anthony Lenton)

Crear un archivo llamado .pythonrc (se llama así pero podría llamarse de cualquier otra forma), que dice:

.. code-block:: python

    if __name__ == "__main__":
       try:
           import readline
       except ImportError:
           print "Module readline not available."
       else:
           import sys
           import rlcompleter
           if sys.platform == "darwin":
              readline.parse_and_bind ("bind ^I rl_complete")
           else:
                readline.parse_and_bind("tab: complete")
           del readline
           del rlcompleter
           del sys


Y en el environment se setea la variable:

.. code-block:: bash

    PYTHONSTARTUP=/home/tuusuario/.pythonrc #(aca importa que sea igual al nombre del alchivo).


Lo que hace es darte Tab-completion en el interprete, cuando no se recuerda que métodos tiene mistring, en el intérprete se hace:

.. code-block:: pycon

    >>> mistring.<tab><tab>


Lista los métodos y atributos disponibles.

Otros intérpretes ya lo hacen.  ipython es notable por tener todo esto y mucho más, pero hay gente que no se acostumbra a usarlo todavia, y esto le pone Tab-completion al intérprete que es bastante común.

OS X
::::

Aparentemente apple no distribuye OSX con soporte para readline de fábrica. Yo estoy seguro que hace tiempo instalé readline 6.1 y py25-readline.

