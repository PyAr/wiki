
WinBatt (ctypes + powrprof.dll en win)
--------------------------------------

Descripción
:::::::::::

Esta receta es un ejemplo de como utilizar funciones nativas de las bibliotecas de Windows desde python (usando ctypes_).

Por ejemplo, en este caso se usa para consultar el estado de la batería (carga en Wh y tiempos estimados, consumo de energía en Watts, etc.) usando la función  CallNtPowerInformation_ de la biblioteca de windows PowrProf_.lib (PowrProf_.dll).  También se ilustra como usar estructuras de C en python para llamar a funciones externas.

Es necesario tener una versión de Python con ctypes y estar sobre windows.

Ejemplo:
::::::::

El ejemplo en Python (winbatt.py) registra un objeto python MiMiniInterpretePython_, exponiendo:

* carga la biblioteca ´powrprof.dll´

* define la constante SystemBatteryState_ (InformationLevel_) de POWER_INFORMATION_LEVEL

* define la estructura SYSTEM_BATTERY_STATE_

* inicializa la estructura en blanco

* llama a la función CallNtPowerInformation_

* imprime los resultados

Archivo winbatt.py

::

    # -*- coding: iso-8859-1 -*-

    import ctypes

    l = ctypes.cdll.LoadLibrary("powrprof")

    SystemBatteryState = 5  # POWER_INFORMATION_LEVEL enum

    class SYSTEM_BATTERY_STATE(ctypes.Structure):
        _fields_ = [
                    ("AcOnLine", ctypes.c_bool),
                    ("BatteryPresent", ctypes.c_bool),
                    ("Charging", ctypes.c_bool),
                    ("Discharging", ctypes.c_bool),
                    ("Spare1", ctypes.c_bool * 4),
                    ("MaxCapacity", ctypes.c_long),
                    ("RemainingCapacity", ctypes.c_long),
                    ("Rate", ctypes.c_long),
                    ("EstimatedTime", ctypes.c_long),
                    ("DefaultAlert1", ctypes.c_long),
                    ("DefaultAlert2", ctypes.c_long),
                    ]


    sb = SYSTEM_BATTERY_STATE(0)
    retval = l.CallNtPowerInformation(SystemBatteryState,
                                      None, 0,
                                      ctypes.addressof(sb), ctypes.sizeof(sb))
    assert retval == 0  # debe devolver 0 si no hay error
    print "AcOnLine:", sb.AcOnLine
    print "Charging:", sb.Charging
    print "Discharging:", sb.Discharging
    print "Capacity:", sb.MaxCapacity, "mWh max", sb.RemainingCapacity, "mWh remaining",
    print sb.RemainingCapacity*100/sb.MaxCapacity, "%"
    print "Rate:", sb.Rate / 1000.0, "W"
    print "Estimated Time:", sb.EstimatedTime / 3600, "h", sb.EstimatedTime / 60 % 60, "min"


Para usarlo se puede ejecutar desde línea de comando:

::

   C:\src>python winbatt.py
   AcOnLine: False
   Charging: False
   Discharging: True
   Capacity: 45140 mWh max 5417 mWh remaining 12 %
   Rate: -9.435 W
   Estimated Time: 0 h 34 min

Para Descargar Fuentes:

Autor / Autores:
::::::::::::::::

MarianoReingart_

-------------------------



  CategoryRecetas_

.. ############################################################################

.. _ctypes: http://docs.python.org/2/library/ctypes.html

.. _CallNtPowerInformation: http://msdn.microsoft.com/en-us/library/windows/desktop/aa372675(v=vs.85).aspx

.. _SYSTEM_BATTERY_STATE: http://msdn.microsoft.com/en-us/library/windows/desktop/aa373212(v=vs.85).aspx

.. _marianoreingart: /marianoreingart
.. _categoryrecetas: /categoryrecetas
