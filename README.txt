Description
This is a python module and a script to mange the 
Digital Loggers Web Power switch.
              
The module provides a python class named
powerswitch that allows managing the web power
switch from python programs.
When run as a script this acts as a command
line utilty to manage the DLI Power switch.

Command line usage
$ dlipower.py --help
Usage: dlipower.py [options] [status|on|off|cycle|get_outlet_name] [arg]

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
  
  arg Can be the outlet number or name of the power outlet to operate on.

Author: Dwight Hubbard

