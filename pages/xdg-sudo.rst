
Xdg-Sudo
========

El sudo grafico universal para escritorios GTK/QT/loquesea, inspirado en el funcionamiento de xdg-open.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # Licence: GPLv3
    # xdg-sudo: Automatically choose "gksudo" or "kdesudo" 
    import os
    import sys
    #import antigravity
    import subprocess
    import re
    if os.geteuid()==0: # non-root check, because if you are root, all this is pointless
        sys.exit(" ERROR: Do not run as root...\n")
    else:
        print (" You are normal user... \n")
    # Prepare actual command to execute
    parameters = " ".join([re.escape(a) for a in sys.argv[1:]])
    # Test which tools exist
    kdesudo = os.path.exists('/usr/bin/kdesudo')
    gtksudo = os.path.exists('/usr/bin/gksudo')
    # If we have at least one of them, check which one to use.
    if kdesudo or gtksudo:
        if kdesudo and gtksudo:
            # Test if gnome runs
            process = subprocess.Popen("ps -ae | grep gnome-session", shell=True, stdout=subprocess.PIPE)
            process.wait()
            if len(process.communicate()[0])>0:
                useGnome = True
            else:
                useGnome = False
        elif kdesudo and (not gtksudo):
            useGnome = False
        elif (not kdesudo) and gtksudo:
            useGnome = True
        # really run it
        if useGnome:
            cmd = "gksudo "
        else:
            cmd = "kdesudo "
        # Run the actual program now
        os.system(cmd+parameters)
    else:
        # we dont have gksudo or kdesudo, OMFG!
        cmd = "xterm -e \"echo 'Neither \\\"gksudo\\\" nor \\\"kdesudo\\\" have been found on your machine. Thus, \\\"sudo\\\" is being used. Please leave this window open until the program has finished. Your are asked for your password below.'; sudo "+parameters+"; sleep 1\""
        os.system(cmd)


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

