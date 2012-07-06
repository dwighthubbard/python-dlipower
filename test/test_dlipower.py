#!/usr/bin/env python
import unittest
import urllib
import urllib2
import StringIO
import os
import sys
sys.path.insert(0,'../dlipower')
import dlipower

__author__ = 'dhubbard'

OFF_HTML="""<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">

<META HTTP-EQUIV="Refresh" CONTENT="60">
<title>Outlet Control  - Home Theater</title>
<script language="JavaScript">
<!--
function reg() {
window.open('http://www.digital-loggers.com/register.html?SN=0000331011');
}
//-->
</script>
</head>
<!-- state=fe lock=00 -->

<body alink="#0000FF" vlink="#0000FF">
<FONT FACE="Arial, Helvetica, Sans-Serif">
<table width="100%" cellspacing=0 cellpadding=0>
<tr>
<td valign=top width="17%" height="100%">

    <!-- menu -->
    <table width="100%" height="100%" align=center border=0 cellspacing=1 cellpadding=0>
    <tr><td valign=top bgcolor="#F4F4F4">
    <table width="100%" cellpadding=1 cellspacing=5>

    <tr><td align=center>

    <table><tr><td><a href="http://www.digital-loggers.com/8.html"><img src=logo.gif width=195 height=65 border=0 alt="Digital Loggers, Inc"></a></td>

    <td><b><font size=-1>Ethernet Power Controller</font></b></td></tr></table>
    <hr>
    </td></tr>



<tr><td nowrap><b><a href="/index.htm">Outlet Control</a></b></td></tr>
<tr><td nowrap><b><a href="/admin.htm">Setup</a></b></td></tr>
<tr><td nowrap><b><a href="/script.htm">Scripting</a></b></td></tr>



<tr><td nowrap><b><a href="/rtc.htm">Date/Time</a></b></td></tr>

<tr><td nowrap><b><a href="/ap.htm">AutoPing</a></b></td></tr>
<tr><td nowrap><b><a href="/syslog.htm">System Log</a></b></td></tr>
<tr><td nowrap><b><a href="/logout">Logout</a></b></td></tr>
<tr><td nowrap><b><a href="/help/">Help</a></b></td></tr>

<tr><td><hr></td></tr>


<tr><td><b><a href="http://www.digital-loggers.com/5.html">Manual</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/6.html">FAQ</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/7.html">Product Information</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/8.html">Digital Logger Inc.</a></b></td></tr>


    </table>
    </td></tr>


    <tr><td valign=bottom height="100%" bgcolor="#F4F4F4">
    <small>Version 1.6.0 (Jun 22 2012 / 21:56:21) 8AA39795-EE789B21</small>
    </td></tr>
    <tr><td valign=bottom height="100%" bgcolor="#F4F4F4">
    <small>S/N:0000331011</small>
    </td></tr>

    </table>
    <!-- /menu -->

</td>
<td valign=top width="83%">

    <!-- heading table -->
    <table width="100%" align=center border=0 cellspacing=1 cellpadding=3>

        <tr>
        <th bgcolor="#DDDDFF" align=left>
        Controller: Home Theater
        </th>
        </tr>

        <tr bgcolor="#FFFFFF" align=left>
        <td>
        Fri Jul  6 07:08:51 2012 <!-- 1162615s up -->
        </td>
        </tr>

    </table>
    <!-- /heading table -->

    <br>

    <!-- individual control table -->
    <table width="100%" align=center border=0 cellspacing=1 cellpadding=3>

        <tr>
        <td bgcolor="#DDDDFF" colspan=5 align=left>
        Individual Control
        </td>
        </tr>

        <!-- heading rows -->
        <tr bgcolor="#DDDDDD">
        <th>#</th>
        <th align=left>Name</th>
        <th align=left>State</th>
        <th align=left colspan=2>Action</th>
        </tr>
        <!-- /heading rows -->




<tr bgcolor="#F4F4F4"><td align=center>1</td>
<td>Lights</td><td>
<b><font color=red>OFF</font></b></td><td>
<a  href=outlet?1=ON>Switch ON</a>
</td><td>
<!-- <a  href=outlet?1=CCL>Cycle</a> -->
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>2</td>
<td>Microwave</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 2 [Microwave] OFF. Continue?')" href=outlet?2=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 2 [Microwave]. Continue?')" href=outlet?2=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>3</td>
<td>NETHD</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 3 [NETHD] OFF. Continue?')" href=outlet?3=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 3 [NETHD]. Continue?')" href=outlet?3=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>4</td>
<td>WDTV</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 4 [WDTV] OFF. Continue?')" href=outlet?4=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 4 [WDTV]. Continue?')" href=outlet?4=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>5</td>
<td>PS3</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 5 [PS3] OFF. Continue?')" href=outlet?5=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 5 [PS3]. Continue?')" href=outlet?5=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>6</td>
<td>Popcorn Popper</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 6 [Popcorn Popper] OFF. Continue?')" href=outlet?6=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 6 [Popcorn Popper]. Continue?')" href=outlet?6=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>7</td>
<td>ITACH</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 7 [ITACH] OFF. Continue?')" href=outlet?7=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 7 [ITACH]. Continue?')" href=outlet?7=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>8</td>
<td>Life Support</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 8 [Life Support] OFF. Continue?')" href=outlet?8=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 8 [Life Support]. Continue?')" href=outlet?8=CCL>Cycle</a>
</td></tr>


    </table>
    <!-- /individual control table -->

    <br>

<table width="100%" align=center border=0 cellspacing=1 cellpadding=3>
<tr><td bgcolor="#DDDDFF" align=left>Master Control</td></tr>

<tr><td bgcolor="#F4F4F4" align=left><a onclick="return confirm('You are going to switch all Outlets OFF. Continue?')" href=outlet?a=OFF>All Outlets OFF</a></td></tr>
<tr><td bgcolor="#F4F4F4" align=left><a href=outlet?a=ON>All Outlets ON</a></td></tr>
<tr><td bgcolor="#F4F4F4" align=left><a onclick="return confirm('You are going to cycle all Outlets. Continue?')" href=outlet?a=CCL>Cycle all Outlets</a></td></tr>
<tr><td align=center>Sequence delay: 15 sec.</td></tr>

</table>


</td>
</tr>
</table>

</body>
</html>"""

ON_HTML="""<html>
<head>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">

<META HTTP-EQUIV="Refresh" CONTENT="60">
<title>Outlet Control  - Home Theater</title>
<script language="JavaScript">
<!--
function reg() {
window.open('http://www.digital-loggers.com/register.html?SN=0000331011');
}
//-->
</script>
</head>
<!-- state=ff lock=00 -->

<body alink="#0000FF" vlink="#0000FF">
<FONT FACE="Arial, Helvetica, Sans-Serif">
<table width="100%" cellspacing=0 cellpadding=0>
<tr>
<td valign=top width="17%" height="100%">

    <!-- menu -->
    <table width="100%" height="100%" align=center border=0 cellspacing=1 cellpadding=0>
    <tr><td valign=top bgcolor="#F4F4F4">
    <table width="100%" cellpadding=1 cellspacing=5>

    <tr><td align=center>

    <table><tr><td><a href="http://www.digital-loggers.com/8.html"><img src=logo.gif width=195 height=65 border=0 alt="Digital Loggers, Inc"></a></td>

    <td><b><font size=-1>Ethernet Power Controller</font></b></td></tr></table>
    <hr>
    </td></tr>



<tr><td nowrap><b><a href="/index.htm">Outlet Control</a></b></td></tr>
<tr><td nowrap><b><a href="/admin.htm">Setup</a></b></td></tr>
<tr><td nowrap><b><a href="/script.htm">Scripting</a></b></td></tr>



<tr><td nowrap><b><a href="/rtc.htm">Date/Time</a></b></td></tr>

<tr><td nowrap><b><a href="/ap.htm">AutoPing</a></b></td></tr>
<tr><td nowrap><b><a href="/syslog.htm">System Log</a></b></td></tr>
<tr><td nowrap><b><a href="/logout">Logout</a></b></td></tr>
<tr><td nowrap><b><a href="/help/">Help</a></b></td></tr>

<tr><td><hr></td></tr>


<tr><td><b><a href="http://www.digital-loggers.com/5.html">Manual</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/6.html">FAQ</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/7.html">Product Information</a></b></td></tr>

<tr><td><b><a href="http://www.digital-loggers.com/8.html">Digital Logger Inc.</a></b></td></tr>


    </table>
    </td></tr>


    <tr><td valign=bottom height="100%" bgcolor="#F4F4F4">
    <small>Version 1.6.0 (Jun 22 2012 / 21:56:21) 8AA39795-EE789B21</small>
    </td></tr>
    <tr><td valign=bottom height="100%" bgcolor="#F4F4F4">
    <small>S/N:0000331011</small>
    </td></tr>

    </table>
    <!-- /menu -->

</td>
<td valign=top width="83%">

    <!-- heading table -->
    <table width="100%" align=center border=0 cellspacing=1 cellpadding=3>

        <tr>
        <th bgcolor="#DDDDFF" align=left>
        Controller: Home Theater
        </th>
        </tr>

        <tr bgcolor="#FFFFFF" align=left>
        <td>
        Fri Jul  6 08:52:58 2012 <!-- 1168862s up -->
        </td>
        </tr>

    </table>
    <!-- /heading table -->

    <br>

    <!-- individual control table -->
    <table width="100%" align=center border=0 cellspacing=1 cellpadding=3>

        <tr>
        <td bgcolor="#DDDDFF" colspan=5 align=left>
        Individual Control
        </td>
        </tr>

        <!-- heading rows -->
        <tr bgcolor="#DDDDDD">
        <th>#</th>
        <th align=left>Name</th>
        <th align=left>State</th>
        <th align=left colspan=2>Action</th>
        </tr>
        <!-- /heading rows -->




<tr bgcolor="#F4F4F4"><td align=center>1</td>
<td>Lights</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 1 [Lights] OFF. Continue?')" href=outlet?1=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 1 [Lights]. Continue?')" href=outlet?1=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>2</td>
<td>Microwave</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 2 [Microwave] OFF. Continue?')" href=outlet?2=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 2 [Microwave]. Continue?')" href=outlet?2=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>3</td>
<td>NETHD</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 3 [NETHD] OFF. Continue?')" href=outlet?3=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 3 [NETHD]. Continue?')" href=outlet?3=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>4</td>
<td>WDTV</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 4 [WDTV] OFF. Continue?')" href=outlet?4=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 4 [WDTV]. Continue?')" href=outlet?4=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>5</td>
<td>PS3</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 5 [PS3] OFF. Continue?')" href=outlet?5=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 5 [PS3]. Continue?')" href=outlet?5=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>6</td>
<td>Popcorn Popper</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 6 [Popcorn Popper] OFF. Continue?')" href=outlet?6=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 6 [Popcorn Popper]. Continue?')" href=outlet?6=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>7</td>
<td>ITACH</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 7 [ITACH] OFF. Continue?')" href=outlet?7=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 7 [ITACH]. Continue?')" href=outlet?7=CCL>Cycle</a>
</td></tr>


<tr bgcolor="#F4F4F4"><td align=center>8</td>
<td>Life Support</td><td>
<b><font color=green>ON</font></b></td><td>
<a onclick="return confirm('You are going to switch Outlet 8 [Life Support] OFF. Continue?')" href=outlet?8=OFF>Switch OFF</a>
</td><td>
<a onclick="return confirm('You are going to cycle Outlet 8 [Life Support]. Continue?')" href=outlet?8=CCL>Cycle</a>
</td></tr>


    </table>
    <!-- /individual control table -->

    <br>

<table width="100%" align=center border=0 cellspacing=1 cellpadding=3>
<tr><td bgcolor="#DDDDFF" align=left>Master Control</td></tr>

<tr><td bgcolor="#F4F4F4" align=left><a onclick="return confirm('You are going to switch all Outlets OFF. Continue?')" href=outlet?a=OFF>All Outlets OFF</a></td></tr>
<tr><td bgcolor="#F4F4F4" align=left><a href=outlet?a=ON>All Outlets ON</a></td></tr>
<tr><td bgcolor="#F4F4F4" align=left><a onclick="return confirm('You are going to cycle all Outlets. Continue?')" href=outlet?a=CCL>Cycle all Outlets</a></td></tr>
<tr><td align=center>Sequence delay: 15 sec.</td></tr>

</table>


</td>
</tr>
</table>

</body>
</html>
"""
URLS={'index.htm':OFF_HTML,'outlet?1=OFF':OFF_HTML,'outlet?1=ON':ON_HTML}

def mock_response(req):
    url= req.get_full_url().split('/')[-1]
    if url in URLS.keys():
        resp = urllib2.addinfourl(StringIO.StringIO(URLS[url]), "mock message", req.get_full_url())
        resp.code = 200
        resp.msg = "OK"
        return resp

class MyHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        return mock_response(req)

class TestPowerswitch(unittest.TestCase):
    def setUp(self):
        """ Set up the mock objects to do our unit tests """
        my_opener = urllib2.build_opener(MyHTTPHandler)
        urllib2.install_opener(my_opener)
        self.p=dlipower.powerswitch(hostname='http://lpc.digital-loggers.com')

    def test_status(self):
        """ Test the status method of the powerswitch object """
        URLS['index.htm']=OFF_HTML
        status=self.p.status(1)
        self.assertEqual(status, 'OFF')

    def test_off(self):
        """ Test the status method of the powerswitch object """
        self.p.off(1)
        URLS['index.htm']=OFF_HTML
        status=self.p.status(1)
        self.assertEqual(status, 'OFF')

    def test_on(self):
        """ Test the status method of the powerswitch object """
        self.p.on(1)
        URLS['index.htm']=ON_HTML
        status=self.p.status(1)
        self.assertEqual(status, 'ON')

def tearDown(self):
        """ Clean up the Mock objects """
        pass

if __name__ == '__main__':
    unittest.main()