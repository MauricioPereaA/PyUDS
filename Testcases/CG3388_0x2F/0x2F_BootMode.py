'''
    TestScript intended to perform CG3388 Tab 0x2F -- NRC 0x11 
Modified by: Mauricio Perea        Date: 7-Jan-20
'''
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='0x2F'   #THIS STEP IS MISSED
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='0x2F - Boot Mode - NRC 0x11'):
        # Begin -- Boot Mode preconditions
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,

            expected={
                'response'   : 'Positive'
            }
        )
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            request_seed='01',
            send_key='01'
        )
        test.step(
            step_title=name,
            custom='10 02'
        )
        # End -- Boot Mode preconditions
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F 4B 5C 00',

            expected={
                'response': 'Negative',
                'data'    : '11',
                'data_2'  : '7F' #add
            }
        )