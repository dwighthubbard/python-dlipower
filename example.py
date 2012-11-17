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

"""
Copyright (c) 2009, Dwight Hubbard
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
import time

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
  print("Can't talk to the switch")
  sys.exit(1)

# Print the current state of all the outlets
switch.printstatus()
  
# Power on outlet #8
switch.on(8)

# Get the state of outlet 8 is and print it
print('Outlet #8 is',switch.status(8))

# Wait a few seconds
time.sleep(5)

# Power outlet #8 back off
switch.off(8)

# Print the current state outlet 8 again
print('Outlet #8 is',switch.status(8))
