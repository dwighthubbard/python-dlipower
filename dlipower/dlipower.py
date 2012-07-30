#!/usr/bin/python
"""
###############################################################
Digital Loggers Web Power Switch management
###############################################################
 Description: This is both a module and a script

              The module provides a python class named
              powerswitch that allows managing the web power
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
"""
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

# Python built in modules
import os
import sys
import time
import optparse
import base64
import json
import urllib2

# External modules
import BeautifulSoup

# Global settings
TIMEOUT=30
CYCLETIME=3
CONFIG_DEFAULTS={'timeout':TIMEOUT,'cycletime':CYCLETIME,'userid':'admin','password':'4321','hostname':'192.168.0.100'}
CONFIG_FILE=os.path.expanduser('~/.dlipower.conf')

class powerswitch:
    """ Powerswitch class to manage the Digital Loggers Web power switch """
    def __init__(self,userid=None,password=None,hostname=None,timeout=None,cycletime=None):
        CONFIG=self.load_configuration()
        if userid:
            self.userid=userid
        else:
            self.userid=CONFIG['userid']
        if password:
            self.password=password
        else:
            self.password=CONFIG['password']
        if hostname:
            self.hostname=hostname
        else:
            self.hostname=CONFIG['hostname']
        if timeout:
            self.timeout=float(timeout)
        else:
            self.timeout=CONFIG['timeout']
        if cycletime:
            self.cycletime=float(cycletime)
        else:
            self.cycletime=CONFIG['cycletime']
        self._is_admin=True
    def load_configuration(self):
        """ Return a configuration dictionary """
        if os.path.isfile(CONFIG_FILE):
            fh=open(CONFIG_FILE,'r')
            try:
              CONFIG=json.load(fh)
            except ValueError:
              # Failed
              return CONFIG_DEFAULTS
            fh.close()
            return CONFIG
        return CONFIG_DEFAULTS
    def save_configuration(self):
        """ Update the configuration file with the object's settings """
        # Get the configuration from the config file or set to the defaults
        CONFIG=self.load_configuration()
            
        # Overwrite the objects configuration over the existing config values
        CONFIG['userid']=self.userid
        CONFIG['password']=self.password
        CONFIG['hostname']=self.hostname
        CONFIG['timeout']=self.timeout
        
        # Write it to disk
        fh=open(CONFIG_FILE,'w')
        # Make sure the file perms are correct before we write data
        # that can include the password into it.
        os.fchmod(fh.fileno(),0o0600)
        if fh:
            json.dump(CONFIG,fh,sort_keys=True, indent=4)
            fh.close()
        else:
            return True
        return False
    def verify(self):
        """ Verify we can reach the switch, returns true if ok """
        return self.geturl()
    def geturl(self,url='index.htm') :
        """ Get a URL from the userid/password protected powerswitch page 
            Return None on failure
        """
        request = urllib2.Request("http://%s/%s" % (self.hostname,url))
        base64string = base64.encodestring('%s:%s' % (self.userid, self.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        try:
            result = urllib2.urlopen(request,timeout=self.timeout).read()
        except urllib2.URLError:
            return None
        #except timeout:
        #    return None
        return result
    def determine_outlet(self,outlet=None):
        """ Get the correct outlet number from the outlet passed in, this
            allows specifying the outlet by the name and making sure the
            returned outlet is an int 
        """
        outlets=self.statuslist()
        if outlet and outlets and type(outlet) is str:
            for plug in outlets:
                if plug[1].strip() == outlet.strip():
                    return int(plug[0])
        return int(outlet)
    def get_outlet_name(self,outlet=0):
        """ Return the name of the outlet """
        outlet=self.determine_outlet(outlet)
        outlets=self.statuslist()
        if outlets and outlet:
            for plug in outlets:
                if int(plug[0]) == outlet:
                    return plug[1]
        return 'Unknown'
    def off(self,outlet=0):
        """ Turn off a power to an outlet 
            False = Success
            True = Fail
        """
        self.geturl(url= 'outlet?%d=OFF' % self.determine_outlet(outlet))
        return self.status(outlet) != 'OFF'
    def on(self,outlet=0):
        """ Turn on power to an outlet 
            False = Success
            True = Fail
        """
        self.geturl(url= 'outlet?%d=ON' % self.determine_outlet(outlet))
        return self.status(outlet) != 'ON'
    def cycle(self,outlet=0):
        """ Cycle power to an outlet 
            False = Power off Success
            True = Power off Fail
            Note, does not return any status info about the power on part of the operation by design
        """        
        if self.off(outlet):
          return True
        time.sleep(self.cycletime)
        self.on(outlet)
        return False
    def statuslist(self):
        """ Return the status of all outlets in a list, 
        each item will contain 3 items plugnumber, hostname and state  """
        outlets=[]
        url=self.geturl('index.htm')
        if not url:
            return None
        soup=BeautifulSoup.BeautifulSoup(url)
        # Get the root of the table containing the port status info
        try:
            root=soup.findAll('td',text='1')[0].parent.parent.parent
        except IndexError:
            # Finding the root of the table with the outlet info failed
            # try again assuming we're seeing the table for a user
            # account insteaed of the admin account (tables are different)
            try:
              self._is_admin=False
              root=soup.findAll('th',text='#')[0].parent.parent.parent
            except IndexError:
              return None
        for temp in root.findAll('tr'):
            columns=temp.findAll('td')
            if len(columns) == 5:
                plugnumber=columns[0].string
                hostname=columns[1].string
                state=columns[2].find('font').string.upper()
                outlets.append([int(plugnumber),hostname,state])
        return outlets
    def printstatus(self):
        """ Print the status off all the outlets as a table to stdout """
        if not self.statuslist():
            print("Unable to communicate to the Web power switch at %s" % self.hostname)
            return None
        print('Outlet\t%-15.15s\tState' % 'Hostname')
        for item in self.statuslist():
            print('%d\t%-15.15s\t%s' % (item[0],item[1],item[2]))
        return
    def status(self,outlet=1):
        """ Return the status of an outlet, returned value will be one of: ON, OFF, Unknown """
        outlet=self.determine_outlet(outlet)
        outlets=self.statuslist()
        if outlets and outlet:
            for plug in outlets:
                if plug[0] == outlet:
                    return plug[2]
        return 'Unknown'

if __name__ == "__main__":
    usage = "usage: %prog [options] [status|on|off|cycle|get_outlet_name] [arg]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--hostname',dest='hostname',default=None,help="hostname/ip of the power switch (default %default)")
    parser.add_option('--timeout',dest='timeout',default=None,help="Timeout for value for power switch communication (default %default)")
    parser.add_option('--cycletime',dest='cycletime',default=None,type=int,help="Delay betwween off/on states for power cycle operations (default %default)")
    parser.add_option('--user',    dest='user',    default=None        ,help="userid to connect with (default %default)"         )
    parser.add_option('--password',dest='password',default=None         ,help="password (default %default)"                       )
    parser.add_option('--save_settings',dest='save_settings',default=False,action='store_true',help='Save the settings to the configuration file')
    parser.add_option("--quiet",dest="quiet",default=False,action="store_true",help="Be quiet, don't print error messages only return error return codes (default False)")
    (options, args) = parser.parse_args()

    switch=powerswitch(userid=options.user,password=options.password,hostname=options.hostname,timeout=options.timeout,cycletime=options.cycletime)
    if options.save_settings:
        switch.save_configuration()
    if len(args):
        if len(args) == 2:
            if args[0].lower() in ['on','poweron']:
                rc=switch.on(args[1])
                if rc and not options.quiet:
                  print >> sys.stderr,"Power on operation failed"
                sys.exit(rc)
            elif args[0].lower() in ['off','poweroff']:
                rc=switch.off(args[1])
                if rc and not options.quiet:
                  print >> sys.stderr,"Power off operation failed"
            elif args[0].lower() in ['cycle']:
                sys.exit(switch.cycle(args[1]))
            elif args[0].lower() in ['status']:
                print(switch.status(args[1]))
            elif args[0].lower() in ['get_name','getname','get_outlet_name','getoutletname']:
                print(switch.get_outlet_name(args[1]))
            else:
                print("Unknown argument %s" % args[0])
    else:
        switch.printstatus()
