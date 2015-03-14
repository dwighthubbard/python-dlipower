COMMAND LINE USAGE
******************
The dlipower package provides two scripts.

dlipower script
===============
This script provides a command line interface to the dli power switches.

.. code-block:: bash

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


fence_dli
=========
The fence_dli script is a linux cluster compatible stonith fencing script for
dlipower switches.
