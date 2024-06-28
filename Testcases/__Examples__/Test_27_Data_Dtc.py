'''
Developed by Mauricio Perea
04 / 11  / 2020
     Test Example - Testing Data_DTC
'''
from framework.shared_functions import device_under_test, tools, pn_dict
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, random

test = TestCase()


class Test_UDS(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False,  # Write on CG Report
            step_delay=0.002
        )
        self.protected_message = random.choice(  # Pick random message to be tested
            list(pn_dict[device_under_test]['protected_messages'].keys())
        )
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Clear DTCs after 5 seconds'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN'
        )
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='read DTCs 1'):
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
        test.initial_dtcs = test.last_dtcs.copy()
        print(f'Actual DTC {test.initial_dtcs}')

    def test_003_1(self, name='Test data_dtc - Negative'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'Type:None is not valid'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': None
            }
        )

    def test_003_2(self, name='Test data_dtc - Negative'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'One element Type:Set '),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': {self.DTC}
            }
        )

    def test_004_1(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'One element Type: list'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (test.initial_dtcs)
            }
        )

    def test_004_2(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'One element Type: str'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (self.DTC)
            }
        )

    def test_004_3(self, name='Test data_dtc - Generate New DTC\'\s'):
        time.sleep(5)
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0}'.format(name),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )
        test.initial_dtcs = test.last_dtcs.copy()
        print(f'Actual DTC {test.initial_dtcs}')

    def test_004_4(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'One element Type: list'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (test.initial_dtcs)
            }
        )

    def test_004_5(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title='{0} - {1}'.format(name, 'One element Type: str'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (self.DTC)
            }
        )

    def test_004_6(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )
        print(f'Actual DTC {test.initial_dtcs}')
        print(f'Self DTC {self.DTC}')

        test.step(
            step_title='{0} - {1}'.format(name, 'Two elements Type: list & str'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (test.initial_dtcs, self.DTC)
            }
        )

    def test_004_7(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )
        print(f'Actual DTC {test.initial_dtcs}')
        print(f'Self DTC {self.DTC}')

        test.step(
            step_title='{0} - {1}'.format(name, 'Two elements Type: str & list'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': (self.DTC, test.initial_dtcs)
            }
        )

    def test_004_7(self, name='Test data_dtc - Positive'):
        # Stop RBS
        test.canoe.set_envVariable(**dict({self.protected_message: 1}))

        test.preconditions(
            step_info=info()
        )
        print(f'Actual DTC {test.initial_dtcs}')
        print(f'Self DTC {self.DTC}')

        test.step(
            step_title='{0} - {1}'.format(name, 'Testing with empty dtc'),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data_dtc': ([])
            }
        )