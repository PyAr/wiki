
Detectar y Notificar Dispositivos USB
=====================================

* Como Detectar y Notificar Dispositivos USB, usando Python, en Linux, ejemplo simple.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- 
    import glib
    import gudev
    import pynotify
    import sys
    #
    def callback(client, action, device, user_data):
        device_vendor = device.get_property("ID_VENDOR_ENC")
        device_model = device.get_property("ID_MODEL_ENC")
        if action == "add":
            n = pynotify.Notification("USB Device Added", "%s %s is now connected "
                                      "to your system" % (device_vendor,
                                      device_model))
            n.show()
        elif action == "remove":
            n = pynotify.Notification("USB Device Removed", "%s %s has been "
                                      "disconnected from your system" %
                                      (device_vendor, device_model))
            n.show()
    #
    if not pynotify.init("USB Device Notifier"):
        sys.exit("Couldn't connect to the notification daemon!")
    #
    client = gudev.Client(["usb/usb_device"])
    client.connect("uevent", callback, None)
    #
    loop = glib.MainLoop()
    loop.run()


*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

-------------------------



  CategoryRecetas_

.. _categoryrecetas: /pages/categoryrecetas
