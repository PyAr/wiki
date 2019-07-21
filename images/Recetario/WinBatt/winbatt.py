#!code python
# -*- coding: iso-8859-1 -*-

"Example to query battery status (under MS Windows)"

__author__ = "Mariano Reingart <reingart@gmail.com>"
__licence__ = "simple all-permissive license (GNU)"

# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
 
import ctypes

# Documentation:
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa372675(v=vs.85).aspx
# http://msdn.microsoft.com/en-us/library/windows/desktop/aa373212(v=vs.85).aspx

# load powrprof.dll (l will be the python "binding")
powrprof = ctypes.cdll.LoadLibrary("powrprof")

# POWER_INFORMATION_LEVEL enum (incomplete):
SystemBatteryState = 5

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


def get_system_battery_state(sb):
    "Call oiwrprof.CallNtPowerInformation to get SystemBatteryState"
    # return 0 on sucess, updates sb SYSTEM_BATTERY_STATE struct
    return powrprof.CallNtPowerInformation(
                SystemBatteryState,    # InformationLevel
                None, 0,               # lpInputBuffer, nInputBufferSize
                ctypes.addressof(sb),  # lpOutputBuffer [out]
                ctypes.sizeof(sb),     # nOutputBufferSize
                )


# Usage example:
if __name__=='__main__':
    # initialize system battery struct:
    sb = SYSTEM_BATTERY_STATE(0)
    # call CallNtPowerInformation
    retval = get_system_battery_state(sb)
    # raise exception if retval != 0 (WinError!)
    assert retval == 0
    # display useful information:
    print "AcOnLine:", sb.AcOnLine
    print "Charging:", sb.Charging
    print "Discharging:", sb.Discharging
    print "Capacity:", sb.MaxCapacity, "mWh max", 
    print sb.RemainingCapacity, "mWh remaining", 
    print sb.RemainingCapacity*100/sb.MaxCapacity, "%"
    # note: negative rate means discharging!
    print "Rate:", sb.Rate / 1000.0, "W"
    # note: negative elapsed time means charging!
    print "Estimated Time:", sb.EstimatedTime / 3600, "h", 
    print sb.EstimatedTime / 60 % 60, "min"
