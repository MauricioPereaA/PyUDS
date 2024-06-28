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
        
        self.test_status = {}
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()



    # Verify that the ECU transitions to the Boot Mode

    def test_001(self, name='Observe normal communication message is enabled'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        time.sleep(6)           # Time set for the current ASC log file to be updated and check the # of CAN messages 
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

    def test_003(self, name='Implement Pre-Programming Sequence'):

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

    def test_004(self, name='Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'unexpected_response': True,
                'partialData': '00 '*30
            }
        )

    def test_005(self, name='sendKey'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_006(self, name='Transition to programmingSession, Boot Mode'):

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

    def test_007(self, name='Observe normal communication message is disabled'):
        time.sleep(5)
        test.preconditions(
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_007')

    def test_008(self, name='Verify that the ECU transitions to the Boot Mode'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_009(self, name='Request SendKey '):

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