Digital Loggers Power Management Python Plugin
**********************************************
[![Build Status](https://travis-ci.org/dwighthubbard/python-dlipower.svg?branch=master)](https://travis-ci.org/dwighthubbard/python-dlipower)
[![Coverage Status](https://coveralls.io/repos/dwighthubbard/python-dlipower/badge.svg)](https://coveralls.io/r/dwighthubbard/python-dlipower)
[![Download Stats](https://pypip.in/download/dlipower/badge.svg)](https://pypi.python.org/pypi/dlipower/)
[![Version Stats](https://pypip.in/version/dlipower/badge.svg)](https://pypi.python.org/pypi/dlipower)
[![Python Version Stats](https://pypip.in/py_versions/dlipower/badge.svg)](https://pypi.python.org/pypi/dlipower/)
[![License Info](https://pypip.in/license/dlipower/badge.svg)](https://pypi.python.org/pypi/dlipower/)

DESCRIPTION
===========
This is a python module and a script to mange the 
Digital Loggers Web Power switch.
              
The module provides a python class named
PowerSwitch that allows managing the web power
switch from python programs.

When run as a script this acts as a command
line utility to manage the DLI Power switch.

SUPPORTED DEVICES
=================
This module has been tested against the following 
Digital Loggers Power network power switches:
* WebPowerSwitch II
* WebPowerSwitch III
* WebPowerSwitch IV
* WebPowerSwitch V
* Ethernet Power Controller III

COMMAND LINE USAGE
==================
The dlipower package provides two scripts.

dlipower script
---------------
This script provides a command line interface to the dli power switches.
```
Usage: dlipower [options] [status|on|off|cycle|get_outlet_name|set_outlet_name] [range] [newname]

Options:
  -h, --help            show this help message and exit
  --hostname=HOSTNAME   hostname/ip of the power switch (default none)
  --timeout=TIMEOUT     Timeout for value for power switch communication
                        (default none)
  --cycletime=CYCLETIME
                        Delay betwween off/on states for power cycle
                        operations (default none)
  --user=USER           userid to connect with (default none)
  --password=PASSWORD   password (default none)
  --save_settings       Save the settings to the configuration file
  --quiet               Suppress error output

Arguments:
  range - One or more ports seperated by commas
    Example: 
      1,3,5-9 (Refers to outlets 1,3,5,6,7,8,9)
  newname - The name to rename the outlet to```
```

fence_dli
---------
The fence_dli script is a linux cluster compatible stonith fencing script for
dlipower switches.


PYTHON USAGE
============
```python
from __future__ import print_function
import dlipower


print('Connecting to a DLI PowerSwitch at lpc.digital-loggers.com')
switch = dlipower.PowerSwitch(hostname="lpc.digital-loggers.com", userid="admin")

print('Turning off the first outlet')
switch[0].state = 'OFF'

print('The powerstate of the first outlet is currently', switch[0].state)

print('Renaming the first outlet as "Traffic light"')
switch[0].description = 'Traffic light'

print('The current status of the powerswitch is:')
print(switch)
```

```
Connecting to a DLI PowerSwitch at lpc.digital-loggers.com
Turning off the first outlet
The powerstate of the first outlet is currently OFF
Renaming the first outlet as "Traffic light"
The current status of the powerswitch is: 
DLIPowerSwitch at lpc.digital-loggers.com
Outlet	Hostname       	State
1	Traffic light  	OFF
2	killer robot   	ON
3	Buiten verlicti	ON
4	Meeting Room Li	OFF
5	Brocade LVM123 	ON
6	Shoretel ABC123	ON
7	Shortel 24V - T	ON
8	Shortel 24V - T	ON
```
