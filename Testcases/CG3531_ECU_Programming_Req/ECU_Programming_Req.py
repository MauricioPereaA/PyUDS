'''

    ECU Programming Req
    
    GB6001 contains the requirement to support the infrastructure  4 ECU Programming Requirements. 
    The Diagnostic CTRS (odx) file provides definition for the DIDs 
    (structure and format). Other requirements documents are referenced 
    in the Description when additional information is specified therein.


'''
from framework.shared_functions import device_under_test
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()


class ECU_Proggramming_Req(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,  # Write on CG Report
            excel_tab='ECU Programming Req'  # Specify CG Excel Tab
        )

        # ''' RID to be tested '''
        # self.RID_1 = '02 09'
        # self.RID_2 = 'FF 00'
        # ''' Device Under Test '''

        self.DUT = device_under_test

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_003(self, name='Transition Server to extendedSession'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False

        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response': 'Positive',
                'dataLength': None
            }

        )

    def test_004(self, name='Activate TesterPresent'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response': 'No response'
            }

        )

    def test_005(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response': 'Positive'
            }
        )

    def test_007(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'partialData': ('00', 'FF')
            }
        )

    def test_008(self, name='Access Security Send Key'):

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

    def test_010(self, name='Transition Server to programmingSession'):

        test.preconditions(
            step_info=info(),
            power_mode='OFF'
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response': 'Positive',
                'dataLength': None
            }
        )

    def test_011(self, name='Erase Application SW Memory'):
        input(
            "WARNING! - Please make sure test has been completed correctly until now before performing Erase Application SW. Then press Enter to continue...")

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=['FF 00', '01'],
            expected={
                'response': 'Positive',
                'dataLength': None
            }

        )

    def test_012(self, name='Download Application SW'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 A0 00 00 0E DE 00',

            expected={
                'response': 'Positive'
            }
        )

    def test_013(self, name='Transfer Application SW'):
        test.preconditions(
            step_info=info()
        )
        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom=packet,

                expected={
                    'response': 'Positive'
                }
            )

    def test_014(self, name='Request Transfer Exit'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response': 'Positive',
            }

        )

    def test_015(self, name='Upload PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response': 'Positive'
            }
        )

    def test_016(self, name='Erase Calibration Data Memory'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            start_routine=['FF 00', '02'],

            expected={
                'response': 'Positive',
                'dataLength': None
            }

        )

    def test_017(self, name='Download Calibration Data'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 80 00 00 00 1E 00',

            expected={
                'response': 'Positive'
            }
        )

    def test_018(self, name='Transfer Calibration Data'):
        test.preconditions(
            step_info=info()
        )
        for packet in Binary.packets_to_send(_binary_cal1):
            test.step(
                step_title=name,
                custom=packet,

                expected={
                    'response': 'Positive'
                }
            )

    def test_019(self, name='Request Transfer Exit'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response': 'Positive',
            }

        )

    def test_020(self, name='Upload PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 02',

            expected={
                'response': 'Positive'
            }
        )

    def test_021(self, name='Transition to defaultSession, Boot Mode'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response': 'Positive',
                'dataLength': None
            }

        )
