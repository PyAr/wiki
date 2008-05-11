= PythonCard =

== Introducción ==

PythonCard es un conjunto de herramientas de construcción GUI para crear aplicaciones de escritorio multiplataforma en Windows, Mac OS X,  y Linux, usando Python.

La motivación de PythonCard es "Las cosas simples deberían ser simples, y las complejas deberían ser posibles"

PythonCard es para vos si queres desarrollar aplicacioens gráficas de manera rápida y facil con un mínimo esfuerzo y código.

PythonCard usa wxPython. Si estás familizarizado con wxPython, se puede ver a PythonCard como una manera simple de hacer programas wxPython con un gran conjunto de ejemplos y herramientas que se pueden copiar y mejorar para crear aplicaciones multiplataforma.

== Como instalar PythonCard: ==

=== Linux (Debian y derivados) ===
Pythoncard esta soportado en Etch, asique su instalación es bastante simple
{{{
apt-get install pythoncard
}}}

 
 
=== Windows ===
 * Bajar e instalar Python desde [http://www.python.org/ftp/python/2.5.2/python-2.5.2.msi www.python.org | Downloads | Windows Installer Python 2.5.2]. 
 * Bajar e instalar wxPython desde [http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.7.1-py25.exe wxPython.org | Binaries | win32 unicode]. 
 * Bajar e instalar PythonCard [http://downloads.sourceforge.net/pythoncard/PythonCard-0.8.2.win32.exe pythoncard.sourceforge.net | Downloads | PythonCard 0.8.2 win32]. 

== Confirmar que funciona ==
Si todo se instaló correctamente, podemos probar los ejemplos que vienen con PythonCard, menu Inicio, PythonCard, Samples (o buscar el script en C:\Python25\Lib\site-packages\PythonCard\samples\samples.pyw o similar)

Si algo anda mal, podemos probar lo siguiente para ver que esta fallando en una consola Python:
{{{
import wx
wx.version() # debería imprimir '2.8.7.1 (msw-unicode)' o similar

from PythonCard import model
rsrc = {'application':{'type':'Application', 'name':'Minimal',
    'backgrounds': [{'type':'Background','name':'bgMin','title':'Ejemplo','size':(200, 100),'components': []}]} }

class Minimal(model.Background): pass

app = model.Application(Minimal, None, rsrc); app.MainLoop()

}}}

Debería aparecer una ventanita con título "Ejemplo".
