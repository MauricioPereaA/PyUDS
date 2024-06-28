
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test, tools, pn_dict
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, random

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            step_delay=0.001,
            writeTestResults=True,
            excel_tab='Network Supervision'
        )

        #== Device Under Test - Settings ==#
        self.protected_message = list(pn_dict[device_under_test]['protected_messages'].keys())[0]
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']
        self.msgSupTimeout=pn_dict[device_under_test]['protected_messages'][self.protected_message]['SupervisionTimeout']

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001_1(self, name='wait +5 seconds and Clear DTCs'):
        time.sleep(1)
        test.preconditions(
            step_info=info(),
            #ignition_switch=['ACC','RUN']
        )
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_001_2(self, name='read DTCs 1 - NO DTCs SET'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )

    def test_002_1(self, name='stop message + read DTCs 2 - NO DTCs SET'):
        test.preconditions(
            step_info=info()
        )
        
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        #Read DTCs before supervision timeout
        test.canoe.set_envVariable(envReadingPeriod=self.msgSupTimeout/2)

        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
        time.sleep(self.msgSupTimeout/2000)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')

    def test_002_2(self, name='wait +5 seconds and read DTCs 3 - Lost Comm DTC is set'):
        test.preconditions(
            step_info=info()
        )
        time.sleep(7)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 2F'%self.DTC
            }
        )

    def test_003_1(self, name='return Message transmission + 5 seconds delay + Clear DTCs'):
        test.preconditions(
            step_info=info()
        )
        test.canoe.set_envVariable(**dict({self.protected_message:0}))
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_003_2(self, name='read DTCs 4 - NO DTCs SET'):
        time.sleep(5)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )

    def test_004(self, name='power down + 1 minute delay + stop message + power up + 4 seconds + read DTCs 5 10 times - NO DTCs SET'):
        test.preconditions(
            step_info=info()
        )
        # Power Supply - Turn OFF
        test.power_supply.output(False)
        print(__name__, 'Waiting 60 seconds while power supply is down')
        for i in reversed(range(60)): # This is just a countdown from 59 to 0 (60s = 1 min)
            print(i, end='  ', flush=True)
            time.sleep(1)

        # Disable Supervised Message tranmission to set Lost Communication DTC
        test.canoe.set_envVariable(**dict({self.protected_message:1}))

        # Power Supply - Turn ON + re-send NMF to restablish communication
        test.power_supply.output(True)

        #Read DTCs every 200ms for 10 times (2seconds)
        test.canoe.set_envVariable(envReadingPeriod=200)
        time.sleep(0.1)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
        time.sleep(2.2)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')

    def test_005(self, name='4 seconds delay + read DTCs 6 - Lost Comm DTC is SET'):
        test.preconditions(
            step_info=info()
        )
        time.sleep(4)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 2F'%self.DTC
            }
        )
        prompt = tools.popup.ask(title=name, description='Verify that the Lost Comm DTC sets only after 5 seconds of voltage recovery')
        test.compare(True, prompt, step='test_005')

