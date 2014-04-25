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
#!/usr/bin/env python
import dlipower

switch = dlipower.PowerSwitch(
    hostname="lpc.digital-loggers.com", userid="admin"
)

# Print the status of the outlets on the PowerSwitch
switch.printstatus()

# Turn off outlet one
switch.off(1)

# Print the status of outlet one
print switch.status(1)

# Turn on outlet 2
switch.on(2)

# Rename outlet 1
switch.set_outlet_name(1,'Traffic light')
```
