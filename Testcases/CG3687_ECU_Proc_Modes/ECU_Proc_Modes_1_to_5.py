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
        message = 'Please ensure you have APP SW Flashed on the ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Observe normal communication message is enabled'):
        test.preconditions(
            step_info=info()
        )
        test.compare(False, test.normal_comm(), step='test_001')

    def test_002(self, name='Request a Download'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 00 00 00 00 00 00',

            expected={
                'response'    : 'Negative',
                'partialData' : '11'
            }
        )