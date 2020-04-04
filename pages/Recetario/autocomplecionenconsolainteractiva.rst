.. title: Autocomplecion en consola interactiva


(donado por Anthony Lenton)

crear un archivo llamado .pythonrc (se llama asi pero podria llamarse de cualquier otra forma), que dice:

::

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


y en el environment se setea la variable:

::

    PYTHONSTARTUP=/home/tuusuario/.pythonrc #(aca importa que sea igual al nombre del alchivo).


Lo que hace es darte Tab-completion en el interprete, cuando no se recuerda que metodos tiene mistring, en el interprete se hace:

::

    >>> mistring.<tab><tab>


y lista los metodos y atributos disponibles.

Otros interpretes ya lo hacen.  ipython es notable por tener todo esto y mucho mas, pero hay gente que no se acostumbra a usarlo todavia, y esto le pone Tab-completion al interprete comuncito de siempre.

OS X
::::

Aparentemente apple no distribuye OSX con soporte para readline de fabrica. Yo estoy seguro que hace tiempo instalé readline 6.1 y py25-readline.

