=== Python for PalmOS ===

Here you can get the latests (only) release of this half baked port of python to palmOS.

img src="screenshot.bmp" /!\ FIXME!!!


==== Release Notes ====

Some months ago i did a port of the Python2.3.2 interpreter to PalmOS. I didnt port any C module or created modules for PalmOS API's. But you can run an interpreter and use stdin/stdout from a form.

There is also a tool to freeze scripts and use the interpreter as a pseudo-shared library.

While talking with FacundoBatista while in a PyAr meeting (python-argentina, http://www.python.org/ar ) he told me that there is some interest in this platform.

So, ive made an initial release that has no documentation on how to use it or compile it (it requires codewarrior). If there is any interest on this, please let me know so we can work on getting this as a real port.

As usual, this is just a proof of concept and is ugly in many ways. (in Palm, code segments must be less than 64K, so some files had to be split and rearranged  ).

If anyone want to check this out, heres the url: http://pyar.decode.com.ar/Members/ltorre/PythonPalm


==== Downloads ====

 * [http://www.movilogic.com/python/Python-2.3.2.zip Click here to download the source]

 * [http://pyar.decode.com.ar/Members/ltorre/MLPYD.prc Click here to download the sample prc] /!\ FIXME!!!

thanks to [http://pippy.sourceforge.net pippy] and Jeff Collins for inspiration and ideas.


==== Contact ====

You can contact me at {{{lucio from movilogic slash com}}}, replacing slash with dot and from with at, add 22 and find the prime factors.
