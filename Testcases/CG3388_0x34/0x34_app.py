from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()

class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x34'
        )

        self.DUT = device_under_test

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        

    def test_001(self, name='Transition Server to the defaultSession'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        ) 
    def test_002(self, name='Service not supported for Service 34 -- NRC 0x11'):
        test.preconditions(
            step_info=info()
            )
        if device_under_test == 'ARB':
            test.step(
                step_title=name,
                custom='34 00 44 00 00 A0 00 00 0E DE 00',

                expected={
                    'response': 'Negative',
                    'data': '11'
                }
            )
        else:
            test.step(
                step_title=name,
                custom='34 00 44 00 01 00 00 00 0e 7e 00',
                expected={
                    'response': 'Negative',
                    'data': '7F'
                }
        )         
        
    