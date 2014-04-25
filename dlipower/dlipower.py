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
from __future__ import print_function

__copyright__ = """
Copyright (c) 2009-2014, Dwight Hubbard
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
import time
import base64
import json
import sys
import urllib
#import urllib2
import multiprocessing
import logging
import socket
import six.moves.urllib.error
import six.moves.urllib.request as urllib2


# External modules
if sys.version > '3.0.0':
    from bs4 import BeautifulSoup
    from urllib.parse import quote
else:
    from BeautifulSoup import BeautifulSoup
    from urllib import quote

# Global settings
TIMEOUT = 20
RETRIES = 3
CYCLETIME = 3
CONFIG_DEFAULTS = {
    'timeout': TIMEOUT,
    'cycletime': CYCLETIME,
    'userid': 'admin',
    'password': '4321',
    'hostname': '192.168.0.100'
}
CONFIG_FILE = os.path.expanduser('~/.dlipower.conf')


def _call_it(params):
    """indirect caller for instance methods and multiprocessing"""
    instance, name, args = params
    kwargs = {}
    return getattr(instance, name)(*args, **kwargs)


class PowerSwitch:
    """ Powerswitch class to manage the Digital Loggers Web power switch """
    def __init__(self, userid=None, password=None, hostname=None, timeout=None,
                 cycletime=None, retries=None):
        """
        Class initializaton
        """
        if not retries:
            retries = RETRIES
        config = self.load_configuration()
        if retries:
            self.retries = retries
        if userid:
            self.userid = userid
        else:
            self.userid = config['userid']
        if password:
            self.password = password
        else:
            self.password = config['password']
        if hostname:
            self.hostname = hostname
        else:
            self.hostname = config['hostname']
        if timeout:
            self.timeout = float(timeout)
        else:
            self.timeout = config['timeout']
        if cycletime:
            self.cycletime = float(cycletime)
        else:
            self.cycletime = config['cycletime']
        self._is_admin = True

    def load_configuration(self):
        """ Return a configuration dictionary """
        if os.path.isfile(CONFIG_FILE):
            file_h = open(CONFIG_FILE, 'r')
            try:
                config = json.load(file_h)
            except ValueError:
                # Failed
                return CONFIG_DEFAULTS
            file_h.close()
            return config
        return CONFIG_DEFAULTS

    def save_configuration(self):
        """ Update the configuration file with the object's settings """
        # Get the configuration from the config file or set to the defaults
        config = self.load_configuration()

        # Overwrite the objects configuration over the existing config values
        config['userid'] = self.userid
        config['password'] = self.password
        config['hostname'] = self.hostname
        config['timeout'] = self.timeout

        # Write it to disk
        file_h = open(CONFIG_FILE, 'w')
        # Make sure the file perms are correct before we write data
        # that can include the password into it.
        os.fchmod(file_h.fileno(), 0o0600)
        if file_h:
            json.dump(config, file_h, sort_keys=True, indent=4)
            file_h.close()
        else:
            return True
        return False

    def verify(self):
        """ Verify we can reach the switch, returns true if ok """
        return self.geturl()

    def geturl(self, url='index.htm'):
        """ Get a URL from the userid/password protected powerswitch page
            Return None on failure
        """
        request = urllib2.Request("http://%s/%s" % (self.hostname, url))
        base64string = base64.encodestring(
            six.b(
                '%s:%s' % (
                    self.userid, self.password
                )
            )
        )[:-1]
        request.add_header("Authorization", "Basic %s" % base64string)
        result = None
        for i in range(0, self.retries):
            try:
                result = urllib2.urlopen(request, timeout=self.timeout).read()
            except socket.timeout:
                logging.debug('Socket timeout attempt %s, retrying', i)
                result = None
            except six.moves.urllib.error.URLError:
                return None
            if result:
                break
        return result

    def determine_outlet(self, outlet=None):
        """ Get the correct outlet number from the outlet passed in, this
            allows specifying the outlet by the name and making sure the
            returned outlet is an int
        """
        outlets = self.statuslist()
        if outlet and outlets and type(outlet) is str:
            for plug in outlets:
                if plug[1].strip() == outlet.strip():
                    return int(plug[0])
        return int(outlet)

    def get_outlet_name(self, outlet=0):
        """ Return the name of the outlet """
        outlet = self.determine_outlet(outlet)
        outlets = self.statuslist()
        if outlets and outlet:
            for plug in outlets:
                if int(plug[0]) == outlet:
                    return plug[1]
        return 'Unknown'

    def set_outlet_name(self, outlet=0, name="Unknown"):
        """ Set the name of an outlet """
        self.determine_outlet(outlet)
        self.geturl(
            url='unitnames.cgi?outname%s=%s' % (outlet, quote(name))
        )
        return self.get_outlet_name(outlet) == name

    def off(self, outlet=0):
        """ Turn off a power to an outlet
            False = Success
            True = Fail
        """
        self.geturl(url='outlet?%d=OFF' % self.determine_outlet(outlet))
        return self.status(outlet) != 'OFF'

    def on(self, outlet=0):
        """ Turn on power to an outlet
            False = Success
            True = Fail
        """
        self.geturl(url='outlet?%d=ON' % self.determine_outlet(outlet))
        return self.status(outlet) != 'ON'

    def cycle(self, outlet=0):
        """ Cycle power to an outlet
            False = Power off Success
            True = Power off Fail
            Note, does not return any status info about the power on part of
            the operation by design
        """
        if self.off(outlet):
            return True
        time.sleep(self.cycletime)
        self.on(outlet)
        return False

    def statuslist(self):
        """ Return the status of all outlets in a list,
        each item will contain 3 items plugnumber, hostname and state  """
        outlets = []
        url = self.geturl('index.htm')
        if not url:
            return None
        soup = BeautifulSoup(url)
        # Get the root of the table containing the port status info
        try:
            root = soup.findAll('td', text='1')[0].parent.parent.parent
        except IndexError:
            # Finding the root of the table with the outlet info failed
            # try again assuming we're seeing the table for a user
            # account insteaed of the admin account (tables are different)
            try:
                self._is_admin = False
                root = soup.findAll('th', text='#')[0].parent.parent.parent
            except IndexError:
                return None
        for temp in root.findAll('tr'):
            columns = temp.findAll('td')
            if len(columns) == 5:
                plugnumber = columns[0].string
                hostname = columns[1].string
                state = columns[2].find('font').string.upper()
                outlets.append([int(plugnumber), hostname, state])
        return outlets

    def printstatus(self):
        """ Print the status off all the outlets as a table to stdout """
        if not self.statuslist():
            print("Unable to communicate to the Web power switch at %s" %
                self.hostname)
            return None
        print('Outlet\t%-15.15s\tState' % 'Hostname')
        for item in self.statuslist():
            print('%d\t%-15.15s\t%s' % (item[0], item[1], item[2]))
        return

    def status(self, outlet=1):
        """
        Return the status of an outlet, returned value will be one of:
        ON, OFF, Unknown
        """
        outlet = self.determine_outlet(outlet)
        outlets = self.statuslist()
        if outlets and outlet:
            for plug in outlets:
                if plug[0] == outlet:
                    return plug[2]
        return 'Unknown'

    def command_on_outlets(self, command, outlets):
        """
        If a single outlet is passed, handle it as a single outlet and
        pass back the return code.  Otherwise run the operation on multiple
        outlets in parallel the return code will be failure if any operation
        fails.  Operations that return a string will return a list of strings.
        """
        if len(outlets) == 1:
            result = getattr(self, command)(outlets[0])
            if isinstance(result, bool):
                return result
            else:
                return [result]
        pool = multiprocessing.Pool(processes=len(outlets))
        result = [
            value for value in pool.imap(
                _call_it,
                [(self, command, (outlet, )) for outlet in outlets],
                chunksize=1
            )
        ]
        if isinstance(result[0], bool):
            for value in result:
                if value:
                    return True
            return result[0]
        return result


if __name__ == "__main__":
    pass
