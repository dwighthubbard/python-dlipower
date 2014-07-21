[![Build Status](https://travis-ci.org/dwighthubbard/python-dlipower.svg?branch=master)](https://travis-ci.org/dwighthubbard/python-dlipower)

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

NAME
----
    dlipower

FILE
----
    dlipower/dlipower.py

DESCRIPTION
-----------
```
    ###############################################################
    Digital Loggers Web Power Switch management
    ###############################################################
     Description: This is both a module and a script
    
                  The module provides a python class named
                  PowerSwitch that allows managing the web power
                  switch from python programs.
    
                  When run as a script this acts as a command
                  line utility to manage the DLI Power switch.
    
                  This module has been tested against the following 
                  Digital Loggers Power network power switches:
                    WebPowerSwitch II
                    WebPowerSwitch III
                    WebPowerSwitch IV
                    WebPowerSwitch V
                    Ethernet Power Controller III
                  
     Author: Dwight Hubbard d@dhub.me
```

CLASSES
=======

    PowerSwitch
    -----------
    
    class PowerSwitch
     |  Powerswitch class to manage the Digital Loggers Web power switch
     |  
     |  Methods defined here:
     |  
     |  __init__(self, userid=None, password=None, hostname=None, timeout=None, cycletime=None)
     |  
     |  command_on_outlets(self, command, outlets)
     |      If a single outlet is passed, handle it as a single outlet and 
     |      pass back the return code.  Otherwise run the operation on multiple
     |      outlets in parallel the return code will be failure if any operation
     |      fails.  Operations that return a string will return a list of strings.
     |  
     |  cycle(self, outlet=0)
     |      Cycle power to an outlet 
     |      False = Power off Success
     |      True = Power off Fail
     |      Note, does not return any status info about the power on part of the operation by design
     |  
     |  determine_outlet(self, outlet=None)
     |      Get the correct outlet number from the outlet passed in, this
     |      allows specifying the outlet by the name and making sure the
     |      returned outlet is an int
     |  
     |  get_outlet_name(self, outlet=0)
     |      Return the name of the outlet
     |  
     |  geturl(self, url='index.htm')
     |      Get a URL from the userid/password protected PowerSwitch page 
     |      Return None on failure
     |  
     |  load_configuration(self)
     |      Return a configuration dictionary
     |  
     |  off(self, outlet=0)
     |      Turn off a power to an outlet 
     |      False = Success
     |      True = Fail
     |  
     |  on(self, outlet=0)
     |      Turn on power to an outlet 
     |      False = Success
     |      True = Fail
     |  
     |  printstatus(self)
     |      Print the status off all the outlets as a table to stdout
     |  
     |  save_configuration(self)
     |      Update the configuration file with the object's settings
     |  
     |  set_outlet_name(self, outlet=0, name='Unknown')
     |      Set the name of an outlet
     |  
     |  status(self, outlet=1)
     |      Return the status of an outlet, returned value will be one of: ON, OFF, Unknown
     |  
     |  statuslist(self)
     |      Return the status of all outlets in a list, 
     |      each item will contain 3 items plugnumber, hostname and state
     |  
     |  verify(self)
     |      Verify we can reach the switch, returns true if ok

    DATA
        CONFIG_DEFAULTS = {'cycletime': 3, 'hostname': '192.168.0.100', 'passw...
        CONFIG_FILE = '~/.dlipower.conf'
        CYCLETIME = 3
        TIMEOUT = 30


Example
=======
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
