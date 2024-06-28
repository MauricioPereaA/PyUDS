from framework.shared_functions import device_under_test   
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, random

test = TestCase()

class PyUDS_TestCase(unittest.TestCase):

    ''' Positive Flow Diagnostic Session Control Session and Security Tests '''
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='NRC 78 & P2 Timing'
        )      
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()
    if device_under_test is 'TCP':
        def test_001(self, name='NRC 78'):

            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                extended_session_control= True,
                request_seed = '01',
                send_key = '01',
                custom = '2E ' + 'F0 F8 ' + '00'*1173,

                expected={
                    'response'   : 'Positive'
                }
            )
    else:
        def test_001(self, name='NRC 78'):

            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                extended_session_control= True,
                request_seed = '01',
                send_key = '01',
                custom = '2E ' + 'F0 F4 ' + '00'*2456,

                expected={
                    'response'   : 'Positive',
                    'check_NRC78' : {'CompType' : 'EQ', 'LowLimit' : 5}
                }
            )