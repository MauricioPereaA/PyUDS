'''
Developed by Mauricio Perea
04 / 11  / 2020
Network Supervision CG3531 TC 04
'''

from framework.shared_functions import device_under_test, tools, pn_dict
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, random

test = TestCase()


class PyUDS_TestCase(unittest.TestCase):

    # == Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        # == Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Network Supervision (MY20-MY22)',
            step_delay=0.001  # 200 ms
        )

        # == Device Under Test - Settings ==#
        self.protected_message = list(pn_dict[device_under_test]['protected_messages'].keys())[0]
        
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']
        self.msgSupTimeout=pn_dict[device_under_test]['protected_messages'][self.protected_message]['SupervisionTimeout']

    @classmethod
    def tearDownClass(self):
        # == End Test Case ==#
        test.end()

    def test_001_1(self, name='Clear DTCs after 5 seconds'):
        test.preconditions(
            step_info=info(),
            #power_mode='RUN'
        )
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_001_2(self, name='read DTCs 1'):
        test.preconditions(
            step_info=info()
        )
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )
        test.initial_dtcs = test.last_dtcs.copy()
        print(f'Actual DTC {test.initial_dtcs}')

    def test_002_1(self, name='Stop msg - read DTC less than supervision timeout'):
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
        

    def test_002_2(self, name='wait > 5 seconds + read DTC 3 - LostComm DTC should be activated'):
        time.sleep(7)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (test.initial_dtcs, self.DTC)
            }
        )
        print(__name__, '== LostComm DTC should be active! ==')

    def test_003_1(self, name='Clear DTCs after 5 seconds - 2'):
        test.canoe.set_envVariable(**dict({self.protected_message: 0}))
        time.sleep(6)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_003_2(self, name='read DTCs 1'):
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

    def test_004(self, name='overVoltage Conditions + create conditions for Lost Comm + 15 seconds delay'):
        test.set_dtc_condition(overVoltage=True)
        test.canoe.set_envVariable(overVoltageCondition=1)
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))
        time.sleep(15)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )
        print(__name__, 'No additional DTCs, other than those reported in Step 1, shall be set')

    #
    def test_005(self, name='normalVoltage Conditions + 4 seconds delay'):
        test.power_supply_reset_default()
        test.canoe.set_envVariable(overVoltageCondition=0)
        test.preconditions(
            step_info=info()
        )
        time.sleep(4)
        
        #Read DTCs every 200ms for 10 times (2seconds)
        test.canoe.set_envVariable(envReadingPeriod=200)
        time.sleep(0.1)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
        time.sleep(2.2)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')
        
        print(__name__, 'Verify No Lost Comm DTCs set')

    def test_006(self, name='delay 4 seconds + read DTCs - DTC should be set'):
        time.sleep(5)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (test.initial_dtcs, self.DTC)
            }
        )
        print(__name__, 'DTC should be set')
        prompt = tools.popup.ask(title=name, description='Verify that the Lost Comm DTC sets only after 5 seconds of voltage recovery')
        test.compare(True, prompt, step='test_006')        

