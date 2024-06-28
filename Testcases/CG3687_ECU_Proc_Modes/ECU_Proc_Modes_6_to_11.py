from Testcases.TestClass import TestCase
from framework.shared_functions import tools  
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Gen_Boot_Requirements(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='ECU Proc Modes'
        )
        message = 'Please ensure you have a Green ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()



    # Verify that the ECU transitions to the Boot Mode

    def test_001(self, name='Observe normal communication message is disabled'):
        time.sleep(2)
        test.preconditions(
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_001')

    def test_002(self, name='Request a Download'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'    : 'Positive'
            }
        )

    def test_003(self, name='Request SendKey'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response'   : 'Negative',
                'data'       :  '12',
                'data_2'     :  '7F'
            }
        )