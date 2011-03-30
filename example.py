#!/usr/bin/python
###############################################################
# Digital Loggers Web Power Switch management example
###############################################################
# Version: 0.01
# Description: Simple script to show how to use the DLI module
# Author: Dwight Hubbard d@dhub.me
# Copyright: This module may be used for any use personal
#            or commercial as long as the author and copyright
#            notice are included in full.
###############################################################
import sys,time

# The module needs to be in the python path.  So we'll add the
# current directory so we can find the dli module
sys.path.append('.')

#import the DLI module
import dlipower

# Global settings
# Change these to match the settings on the switch
SWITCHIP="192.168.0.100"
USER="admin"
PASSWORD="4321"

# Open (connect) to the power switch, if the
# parameters are not passed it defaults to the
# IP address, user and password the switch is 
# set with from the factory.  Only changed items
# actually need to be passed.
switch=dlipower.powerswitch(hostname=SWITCHIP,userid=USER,password=PASSWORD)

# Verify we can talk to the switch
if not switch.verify():
  print "Can't talk to the switch"
  sys.exit(1)

# Print the current state of all the outlets
switch.printstatus()
  
# Power on outlet #8
switch.on(8)

# Get the state of outlet 8 is and print it
print 'Outlet #8 is',switch.status(8)

# Wait a few seconds
time.sleep(5)

# Power outlet #8 back off
switch.off(8)

# Print the current state outlet 8 again
print 'Outlet #8 is',switch.status(8)
