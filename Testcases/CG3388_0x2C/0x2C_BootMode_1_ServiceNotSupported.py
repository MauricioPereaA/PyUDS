'''
    TestScript intended to perform CG3388 Tab 0x2C -- NRC 0x11
    Modified by: Mauricio Perea        Date: 30-Sep-20

'''
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):

    @classmethod
    def format_hex(cls, decimal):
        return hex(decimal).replace('0x','').upper().rjust(2,'0')

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''

        if device_under_test is 'SCL':
            raise Warning('SCL does not support service 0x2C')

        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='0x2C'
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='0x2C - Boot Mode - NRC 0x11'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
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
            custom='2C 01 F2 FF F0 80 01 01',

            expected={
                'response': 'Negative',
                'data'    : '11',
                'data_2'    : '7F' #add             

            }
        )

