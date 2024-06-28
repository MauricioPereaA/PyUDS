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
        message = 'Please ensure you have a APP SW Flashed on the ECU.'+\
                  '\nThis test is intented to Err_ModuleID when programming APP SW or calibration data with invalid Module ID'

        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Execute Successful Programming Event'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
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
                'response': 'Positive',
                'dataLength':  31,
                'unexpected_response' : True,
                'partialDdata': ('00', 'FF' )
            }
        )

        test.step(
            step_title=name,
            send_key='01',

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

        for packet in Binary.packets_to_send(_binary_app):
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

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_002(self, name='Erase Memory'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 02',
            expected={
                'response'   : 'Positive'
            }
        )

    def test_003(self, name='Request Download Modified Calibration Data file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 A0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_004(self, name='Request Download Modified Calibration Data file'):

        test.preconditions(
            step_info=info(),
        )

        for packet in (Binary.packets_to_send(_binary_cal1)):
            packet_list = list(packet)
            packet_list[84:148] = 'f'*64
            packet = ''.join(packet_list)

            test.step(
            step_title=name,
            custom = packet,

            expected={
                'response'     : 'Positive'
            }
        )
            break

    def test_005(self, name='Request Transfer Exit'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'    : 'Negative',
                'partialData' : '7F 37' 
            }
        )

    def test_006(self, name='Verify PEC'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F1',

            expected={
                'response'    : 'Positive',
                'data'        : '00 1B' 
            }
        )

