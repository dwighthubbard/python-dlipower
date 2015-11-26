#!/usr/bin/env python
# Copyright (c) 2009-2015, Dwight Hubbard
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.


import logging
logging.basicConfig(level=logging.DEBUG)
import requests_mock
import unittest
import dlipower
import vcr


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
URLS = {
    'index.htm': OFF_HTML,
    'outlet?1=OFF': OFF_HTML,
    'outlet?1=ON': ON_HTML
}


class TestPowerswitch(unittest.TestCase):

    def setUp(self):
        """ Set up the mock objects to do our unit tests """
        self.p = dlipower.PowerSwitch(hostname='lpc.digital-loggers.com')

    def test_status(self):
        """ Test the status method of the PowerSwitch object """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/index.htm', text=OFF_HTML)
            status = self.p.status(1)
            print(status)
            self.assertEqual(status, 'OFF')

    def test_off(self):
        """ Test the status method of the PowerSwitch object """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=OFF', text=OFF_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=OFF_HTML)
            self.p.off(1)
            status = self.p.status(1)
            self.assertEqual(status, 'OFF')

    def test_on(self):
        """ Test the status method of the PowerSwitch object """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=ON', text=ON_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=ON_HTML)
            self.p.on(1)
            status = self.p.status(1)
            self.assertEqual(status, 'ON')

    def test_cycle(self):
        """ Test the status method of the PowerSwitch object """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=ON', text=ON_HTML)
            m.get('http://lpc.digital-loggers.com/outlet?1=OFF', text=OFF_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=ON_HTML)
            self.p.cycle(1)
            status = self.p.status(1)
            self.assertEqual(status, 'ON')

    def test_on_state_setter(self):
        """ Test the state setter to turn on an outlet """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=ON', text=ON_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=ON_HTML)
            self.p[0].state = "ON"
            status = self.p.status(1)
            self.assertEqual(status, 'ON')

    def test_on_outlet(self):
        """ Test the state setter to turn on an outlet """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=ON', text=ON_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=ON_HTML)
            self.p[0].on()
            status = self.p.status(1)
            self.assertEqual(status, 'ON')

    def test_off_state_setter(self):
        """ Test the state setter to turn off an outlet """
        with requests_mock.mock() as m:
            m.get('http://lpc.digital-loggers.com/outlet?1=OFF', text=OFF_HTML)
            m.get('http://lpc.digital-loggers.com/index.htm', text=OFF_HTML)
            self.p[0].state = "OFF"
            status = self.p.status(1)
            self.assertEqual(status, 'OFF')

    def test_powerswitch_user_password(self):
        r = dlipower.PowerSwitch(userid='foo', password='bar', hostname='goober.com', cycletime=10)
        self.assertEqual(r.userid, 'foo')
        self.assertEqual(r.password, 'bar')
        self.assertEqual(r.hostname, 'goober.com')
        self.assertIsInstance(r.cycletime, float)
        self.assertEqual(r.cycletime, 10.0)

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_powerswitch_repr(self):
        print(self.p.__repr__())
        self.assertIn('DLIPowerSwitch at lpc.digital-loggers.com', self.p.__repr__())

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_powerswitch_repr_html(self):
        self.assertIn(
            '<tr><th colspan="3">DLI Web Powerswitch at lpc.digital-loggers.com</th></tr>',
            self.p._repr_html_()
        )

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_powerswitch_verify(self):
        self.p.verify()

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_outlet_set_name(self):
        self.p[0].name='goober'
        self.assertEqual(self.p.get_outlet_name(1), 'goober')

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_determine_outlet(self):
        self.p[0].name='goober'
        self.assertEqual(self.p.determine_outlet('goober'), 1)

    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_cycle(self):
        self.p[0].off()
        self.p.cycle(1)
        self.assertEqual(self.p[0].state, 'ON')

    @unittest.skip
    @vcr.use_cassette(cassette_library_dir='test/fixtures')
    def test_command_on_outlets(self):
        for i in range(0, 5):
            self.p[i].off()
        self.p.command_on_outlets('ON', range(1,6))
        for i in range(0, 5):
            self.assertEqual(self.p[i].state, 'ON')

    def test_outlet(self):
        ol = dlipower.Outlet(None, 1, state='OFF')
        self.assertEqual(ol.switch, None)
        self.assertEqual(ol.outlet_number, 1)
        self.assertEqual(ol.__str__(), '1:OFF')
        self.assertEqual(ol.__repr__(), "<dlipower_outlet '1:OFF'>")
        self.assertEqual(ol.state, 'OFF')

    def tearDown(self):
        """ Clean up the Mock objects """
        pass

if __name__ == '__main__':
    unittest.main()
