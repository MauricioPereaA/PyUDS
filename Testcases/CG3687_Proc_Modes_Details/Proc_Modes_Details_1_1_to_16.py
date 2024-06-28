from Testcases.TestClass import TestCase
from framework.shared_functions import tools, ECU_info
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
            excel_tab='Proc Modes Details'
        )
        self.tester = [ECU_info['name'], ECU_info['name']+'_2', ECU_info['name']+'_3', ECU_info['name']+'_4', ECU_info['name']+'_5', ECU_info['name']+'_6']
        message = 'Please ensure you have APP SW Flashed on the ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Pre-Programming Sequence'):
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

    def test_002(self, name='Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_003(self, name='Send Key'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response': 'Positive'

            }
       )

    def test_004(self, name='Transition to programmingSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_005(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF1'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'Positive',
                'data'       : '00 00'
            }
        )

    def test_006(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF2'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[1]
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'No response'
            }
        )

    def test_007(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF3'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[2]
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'No response'
            }
        )

    def test_008(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF4'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[3]
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'No response'
            }
        )

    def test_009(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF5'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[4]
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'No response'
            }
        )

    def test_010(self, name='Send 29 bit Normal fixed addressing Physical request from source address 0xF6'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[5]
        )

        test.step(
            step_title = name,
            custom = '22 F1 F0',
            
            expected={
                'response'   : 'No response'
            }
        )