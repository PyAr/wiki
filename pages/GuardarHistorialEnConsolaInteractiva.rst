
Guardar historial en consola interactiva
========================================

como guardar y recuperar el historial de las sesiones en la consola interactiva (donado por Matias Ribecky)

crear un archivo llamado .pythonrc (se llama asi pero podria llamarse de cualquier otra forma), que dice: 

::

   import os
   import sys
   import atexit

   history_path = os.path.expanduser("~/.pyhistory")

   def save_history():
       import readline
       readline.write_history_file(history_path)

   if os.path.exists(history_path):
       readline.read_history_file(history_path)

   atexit.register(save_history)

   del os, sys, atexit, readline, rlcompleter, save_history, history_path

y en el environment se setteada la variable

PYTHONSTARTUP=/home/tuusuario/.pythonrc (aca importa que sea igual al nombre del alchivo). 

