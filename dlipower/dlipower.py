#!/usr/bin/python
import os,socket,time,re,BeautifulSoup,optparse, urllib2, base64, json
###############################################################
# Digital Loggers Web Power Switch management
###############################################################
# Description: This is both a module and a script
#              
#              The module provides a python class named
#              powerswitch that allows managing the web power
#              switch from python programs.
# 
#              When run as a script this acts as a command
#              line utilty to manage the DLI Power switch.
# Author: Dwight Hubbard d@dhub.me
# Copyright: This module may be used for any use personal
#            or commercial as long as the author and copyright
#            notice are included in full.
###############################################################

# Global settings
# Timeout in seconds
TIMEOUT=5
CYCLETIME=1.5
CONFIG_DEFAULTS={'timeout':TIMEOUT,'cycletime':CYCLETIME,'userid':'admin','password':'4321','hostname':'192.168.0.100'}
CONFIG_FILE=os.path.expanduser('~/.dlipower.conf')

class powerswitch:
    """ Manage the DLI Web power switch """
    def __init__(self,userid=None,password=None,hostname=None,timeout=None):
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
        os.fchmod(fh.fileno(),0600)
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
        """ Get a URL from the userid/password protected powerswitch page """
        request = urllib2.Request("http://%s/%s" % (self.hostname,url))
        base64string = base64.encodestring('%s:%s' % (self.userid, self.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        try:
            result = urllib2.urlopen(request,timeout=self.timeout).read()
        except urllib2.URLError,timeout:
            return None
        return result
    def off(self,outlet=0):
        """ Turn off a power to an outlet """
        self.geturl(url= 'outlet?%d=OFF' % outlet)
    def on(self,outlet=0):
        """ Turn on power to an outlet """
        self.geturl(url= 'outlet?%d=ON' % outlet)
    def cycle(self,outlet=0):
        """ Cycle power to an outlet """
        self.off(outlet)
        time.sleep(CYCLETIME)
        self.on(outlet)
    def statuslist(self):
        """ Return the status of all outlets in a list, 
        each item will contain 3 items plugnumber, hostname and state  """
        outlets=[]
        url=self.geturl('index.htm')
        if not url:
            return None
        soup=BeautifulSoup.BeautifulSoup(url)
        try:
            powertable=soup.findAll('table')[5]
        except IndexError:
            return None
        for temp in powertable.findAll('tr')[2:]:
            columns=temp.findAll('td')
            plugnumber=columns[0].string
            hostname=columns[1].string
            state=columns[2].find('font').string
            outlets.append([int(plugnumber),hostname,state])
        return outlets
    def printstatus(self):
        """ Print the status off all the outlets as a table to stdout """
        if not self.statuslist():
            print "Unable to communicte to the Web power switch at %s" % self.hostname
            return None
        print 'Outlet\t%-15.15s\tState' % 'Hostname'
        for item in self.statuslist():
            print '%d\t%-15.15s\t%s' % (item[0],item[1],item[2])
    def status(self,outlet=1):
        """ Return the status of an outlet, returned value will be one of: On, Off, Unknown """
        outlets=self.statuslist()
        if outlet:
            for plug in outlets:
                if plug[0] == outlet:
                    return plug[2]
        return 'Unknown'

if __name__ == "__main__":
    usage = "usage: %prog [options] [status|on|off|cycle] [arg]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--hostname',dest='hostname',default=None,help="hostname/ip of the power switch (default %default)")
    parser.add_option('--timeout',dest='timeout',default=None,help="Timeout for value for power switch communication (default %default)")
    parser.add_option('--user',    dest='user',    default=None        ,help="userid to connect with (default %default)"         )
    parser.add_option('--password',dest='password',default=None         ,help="password (default %default)"                       )
    parser.add_option('--save_settings',dest='save_settings',default=False,action='store_true',help='Save the settings to the configuration file')
    (options, args) = parser.parse_args()

    switch=powerswitch(userid=options.user,password=options.password,hostname=options.hostname,timeout=options.timeout)
    if options.save_settings:
        switch.save_configuration()
    if len(args):
        if len(args) == 2:
            if args[0].lower() in ['on','poweron']:
                switch.on(int(args[1]))
            if args[0].lower() in ['off','poweroff']:
                switch.off(int(args[1]))
            if args[0].lower() in ['cycle']:
                switch.cycle(int(args[1]))
            if args[0].lower() in ['status']:
                print switch.status(int(args[1]))
    else:
        switch.printstatus()