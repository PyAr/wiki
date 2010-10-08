= tkVersionPrint =

Imprime la version de TK que se esta usando actualmente.
{{{
#!/usr/bin/env python
from Tkinter import *
root = Tk()
#
tkversion = root.tk.eval('info patchlevel')
print 'TK Version = '+tkversion
#
root.mainloop()
}}}

Ejemplo:
{{{
juan@maverick:~$ /usr/bin/env python test.py 
TK Version = 8.5.8
}}}
