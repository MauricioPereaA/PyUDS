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
        message = 'Please ensure you have APP SW Flashed on the ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        self.s3_timeout = 5 + 0.1 # S3 timeout + 100 msec
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Observe normal communication message is enabled'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.compare(False, test.normal_comm(), step='test_001')

    def test_002(self, name='Verify Application Mode'):
        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 C0 00 00 00 3E 00',
            expected={
                'response'   : 'Negative',
                'data'       :  '11'
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
                'response': 'Positive'
            }
        )

    def test_004(self, name='Request Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'            : 'Positive',
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_005(self, name='Send key '):
        # This is only to verify that ECU is Awake
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

    def test_006(self, name='Transition to programmingSession'):
        # This is only to verify that ECU is Awake
        time.sleep(5)
        test.preconditions(            
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive'
            }
        )


    def test_007(self, name='Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'            : 'Positive',
                'partialData'         : '00 '*30
            }
        )

    def test_008(self, name='Observe normal communication message is enabled'):

        time.sleep(self.s3_timeout)

        test.preconditions(
            step_info=info()
        )
        time.sleep(5)
        test.compare(False, test.normal_comm(), step='test_008')


    def test_009(self, name='Verify that the ECU transitions to the Application Mode'):
        test.preconditions(            
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 a0 00 00 00 1E 00',
            expected={
                'response'   : 'Negative',
                'data'       : '11' 
            }

        )
