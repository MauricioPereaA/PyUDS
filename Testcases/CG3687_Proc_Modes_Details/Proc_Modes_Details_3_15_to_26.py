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
        message = 'Please ensure you have a Green ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        self.s3_timeout = 5 + 0.1 # S3 timeout + 100 msec
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Observe normal communication message is disabled'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.compare(True, test.normal_comm(), step='test_001')

    def test_002(self, name='Verify that the ECU transitions to the Boot Mode'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'   : 'Positive',
                'partialData'       : '62 F0 F0'
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
                'response': 'Negative',
                'data'    : '12',
                'data_2'  : '7F'
            }
        )

    def test_004(self, name='Transition to extendedSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='10 03',

            expected={
                'response'            : 'Positive'
            }
        )


    def test_005(self, name='Request Seed key'):

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

    def test_006(self, name='Request Seed key'):

        time.sleep(self.s3_timeout)

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'            : 'Negative',
                'data'                : '7E'
            }
        )


    def test_007(self, name='Execute Successful Programming Event (only calibration partition)'):

        test.preconditions(
            step_info=info()
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

        test.step(
            step_title=name,
            request_seed='01',


            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 01',
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_cal1):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
                }
            )

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'   : 'Positive'
            }

        )

