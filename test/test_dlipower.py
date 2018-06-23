from unittest import skip
from vcr_unittest import VCRTestCase
from dlipower import PowerSwitch, Outlet
from dlipower import DLIPowerException


class TestDLIPowerPro(VCRTestCase):
    switch_hostname = 'pro.digital-loggers.com'
    use_https = True
    userid = 'admin'
    password = '4321'

    def setUp(self):
        """ Set up the mock objects to do our unit tests """
        super(TestDLIPowerPro, self).setUp()
        self.p = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)

    def test__dlipower__statuslist(self):
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        result = switch.statuslist()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 8)

    def test__dlipower__status(self):
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        result = switch.status(1)
        self.assertIn(result, ['ON', 'OFF'])

    def test__powerswitch_user_password(self):
        r = PowerSwitch(userid=self.userid, password=self.password, hostname=self.switch_hostname, cycletime=10)
        self.assertEqual(r.userid, self.userid)
        self.assertEqual(r.password, self.password)
        self.assertEqual(r.hostname, self.switch_hostname)
        self.assertIsInstance(r.cycletime, float)
        self.assertEqual(r.cycletime, 10.0)

    def test_status(self):
        """ Test the status method of the PowerSwitch object """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch.off(1)
        status = switch.status(1)
        self.assertEqual(status, 'OFF')

    def test_off(self):
        """ Test the status method of the PowerSwitch object """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch.off(1)
        status = switch.status(1)
        self.assertEqual(status, 'OFF')

    def test_on(self):
        """ Test the status method of the PowerSwitch object """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch.on(1)
        status = switch.status(1)
        self.assertEqual(status, 'ON')

    def test_cycle(self):
        """ Test the status method of the PowerSwitch object """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch.cycle(1)
        status = switch.status(1)
        self.assertEqual(status, 'ON')

    def test_outlet(self):
        ol = Outlet(None, 1, state='OFF')
        self.assertEqual(ol.switch, None)
        self.assertEqual(ol.outlet_number, 1)
        self.assertEqual(ol.__str__(), '1:OFF')
        self.assertEqual(ol.__repr__(), "<dlipower_outlet '1:OFF'>")
        self.assertEqual(ol.state, 'OFF')

    def test_on_state_setter(self):
        """ Test the state setter to turn on an outlet """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch[0].state = "ON"
        status = switch.status(1)
        self.assertEqual(status, 'ON')

    def test_on_outlet(self):
        """ Test the state setter to turn on an outlet """
        self.p[0].on()
        status = self.p.status(1)
        self.assertEqual(status, 'ON')

    def test_off_state_setter(self):
        """ Test the state setter to turn off an outlet """
        switch = PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=self.use_https)
        switch[0].state = "OFF"
        status = switch.status(1)
        self.assertEqual(status, 'OFF')

    def test_powerswitch_repr(self):
        print(self.p.__repr__())
        self.assertIn('DLIPowerSwitch at ', self.p.__repr__())

    def test_powerswitch_repr_html(self):
        self.assertIn(
            '<tr><th colspan="3">DLI Web Powerswitch at ',
            self.p._repr_html_()
        )

    def test_powerswitch_verify(self):
        self.p.verify()

    def test_outlet_set_name(self):
        self.p[0].name='goober'
        self.assertEqual(self.p.get_outlet_name(1), 'goober')

    def test_determine_outlet(self):
        self.p[0].name='goober'
        self.assertEqual(self.p.determine_outlet('goober'), 1)

    def test__outlet__unicode__magic(self):
        outlet = self.p[0]
        result = outlet.__unicode__()
        self.assertEqual(result, '%s:%s' % (outlet.name, outlet.state))

    def test__outlet__str__magic(self):
        outlet = self.p[0]
        result = outlet.__str__()
        self.assertEqual(result, '%s:%s' % (outlet.name, outlet.state))

    @skip('Does not work with unittest')
    def test_command_on_outlets(self):
        for i in range(0, 5):
            self.p[i].off()
        self.p.command_on_outlets('ON', range(1,6))
        for i in range(0, 5):
            self.assertEqual(self.p[i].state, 'ON')


class TestDLIPowerProNoSSL(TestDLIPowerPro):
    use_https = False


class TestDLIPowerLPC(TestDLIPowerPro):
    switch_hostname = 'lpc.digital-loggers.com'
    use_https = False


class TestDLIPowerEPCR(TestDLIPowerPro):
    switch_hostname = 'epcr.digital-loggers.com'
    use_https = False


class TestDLIPowerMissing(VCRTestCase):
    switch_hostname = '127.1.0.99'
    userid = 'admin'
    password = '4321'

    new_episodes = 'new_episodes'

    def _get_vcr_kwargs(self):
        kwargs = super()._get_vcr_kwargs()
        kwargs['record_mode'] = 'new_episodes'
        return kwargs

    def test__missing__https(self):
        PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=True)

    def test__missing__http(self):
        PowerSwitch(hostname=self.switch_hostname, userid=self.userid, password=self.password, use_https=False)
