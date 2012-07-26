DESCRIPTION
This is a python module and a script to mange the 
Digital Loggers Web Power switch.
              
The module provides a python class named
powerswitch that allows managing the web power
switch from python programs.
When run as a script this acts as a command
line utility to manage the DLI Power switch.

SUPPORTED DEVICES
This module has been tested against the following 
Digital Loggers Power network power switches:
  WebPowerSwitch II
  WebPowerSwitch III
  WebPowerSwitch IV
  WebPowerSwitch V
  Ethernet Power Controller III

COMMAND LINE USAGE
$ dlipower.py --help
Usage: dlipower.py [options] [status|on|off|cycle|get_outlet_name] [arg]

Options:
  -h, --help            show this help message and exit
  --hostname=HOSTNAME   hostname/ip of the power switch (default none)
  --timeout=TIMEOUT     Timeout for value for power switch communication
                        (default 30 seconds)
  --cycletime=CYCLETIME
                        Delay between off/on states for power cycle
                        operations (default 1.5 seconds)
  --user=USER           userid to connect with (default admin)
  --password=PASSWORD   password (default 4321)
  --save_settings       Save the settings to the configuration file so they
                        don't have to be passed on the command line.
  
  arg Can be the outlet number or name of the power outlet to operate on.

Author: Dwight Hubbard

