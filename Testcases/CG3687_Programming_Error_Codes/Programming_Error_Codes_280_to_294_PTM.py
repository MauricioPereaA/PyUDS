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
            excel_tab='Programming Error Codes'
        )
        message = 'Please ensure you have APP SW Flashed on the ECU.'+\
                  '\nThis test is intented to Err_MsgOutOfSequence when programming App SW with invalid App SW service request sequence'
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
            mec_zero=True,
            sbat=False
        )

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

    def test_003(self, name='Send key for security level 01'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            send_key = '01',
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_004(self, name='Transition to programmingSession'):

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

    def test_005(self, name='Erase Memory'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            custom = '31 01 FF 00 01',
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_006(self, name='Request Download modified App SW file'):

        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_007(self, name='Request Download Calibration Data file'):

        test.preconditions(
            step_info=info(),
        )

        for packet in (Binary.packets_to_send(_binary_cal1)):
            test.step(
            step_title=name,
            custom = packet,

            expected={
                'response'     : 'Positive'
            }
        )

    def test_008(self, name='Request Transfer Exit'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'    : 'Positive' 
            }
        )

    def test_009(self, name='Request Download modified Calibration file'):

        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Negative',
                'partialData': '7F 34'
            }
        )

    def test_010(self, name='Verify PEC'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F1',

            expected={
                'response'    : 'Positive',
                'data'        : '00 1D' 
            }
        )

    def test_011(self, name='Observe normal communication message is disabled'):
        time.sleep(2)
        test.preconditions(
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_011')