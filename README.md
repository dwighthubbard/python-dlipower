[![Build Status](https://cd.screwdriver.cd/pipelines/5669/badge?nocache=true)](https://cd.screwdriver.cd/pipelines/5669)
[![Package](https://img.shields.io/badge/package-pypi-blue.svg)](https://pypi.org/project/dlipower/)
[![Codestyle](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Documentation](https://readthedocs.org/projects/dlipower/badge/?version=latest)](http://dlipower.readthedocs.org/en/latest/)

---

# Digital Loggers Network Power Switch Python Module

This is a python module and a script to mange the 
Digital Loggers Web Power switch.
              
The module provides a python class named
PowerSwitch that allows managing the web power
switch from python programs.

When run as a script this acts as a command
line utility to manage the DLI Power switch.

# SUPPORTED DEVICES
This module has been tested against the following 
Digital Loggers Power network power switches:

* ProSwitch
* WebPowerSwitch II
* WebPowerSwitch III
* WebPowerSwitch IV
* WebPowerSwitch V
* Ethernet Power Controller III


# Example

```python
import dlipower

print('Connecting to a DLI PowerSwitch at lpc.digital-loggers.com')
switch = dlipower.PowerSwitch(hostname="lpc.digital-loggers.com", userid="admin")

print('Turning off the first outlet')
switch.off(1)

print('The powerstate of the first outlet is currently', switch[0].state)

print('Renaming the first outlet as "Traffic light"')
switch[0].name = 'Traffic light'

print('The current status of the powerswitch is:')
print(switch)
```

```console
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
