Guardar el siguiente código en **mymacros.py** en:

* Apache OpenOffice: ``/home/USER/.openoffice/4/user/Scripts/python/mymacros.py``

* LibreOffice: ``/home/USER/.config/libreoffice/4/user/Scripts/python/mymacros.py``

Código
::::::

::

	import uno

	def HolaMundoWriter():
      	doc = XSCRIPTCONTEXT.getDocument()
      	text = doc.Text
      	text.String = 'Hola Mundo Python Writer!!'
      	return

  	def HolaMundoCalc():
      	doc = XSCRIPTCONTEXT.getDocument()
      	cell = doc.getSheets().getByIndex(0).getCellRangeByName('A1')
      	cell.setString('Hola Mundo Python Calc!!')
      	return

* Abrir AOO o LibO, menú Herramientas -> Macros -> Ejecutar Macro...