from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1

test = TestCase()

class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # == Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x34'
        )

    @classmethod
    def tearDownClass(self):
        # == End Test Case ==#
        test.end()

    def test_001(self, name='Transition Server to extendedSession'):

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

    def test_002(self, name='Activate TesterPresent'):

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

    def test_003(self, name='Disable DTCs'):

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

    def test_004(self, name='Disable Normal Communication'):

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

    def test_005(self, name='Access Security Request Seed'):

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

    def test_006(self, name='Access Security Send Key'):

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

    def test_007(self, name='Transition Server to programmingSession'):

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

    # ======================Syntax NRC Check===============================

    def test_008(self, name='Erase Memory'):
        input(
            "WARNING! - Please make sure test has been completed correctly until now before performing Erase Application SW. Then press Enter to continue...")

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=['FF 00', '02'], #Erasing calibration partition
            expected={
                'response': 'Positive',
                'dataLength': None
            }

        )

    # ======================NRC13===============================
    def test_009(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34',
            expected={
                'response': 'Negative',
                'data': '13'
            }
        )

    def test_010(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 11'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 00 80 00 00 00 1E 00 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )

    #     # ======================NRC31===============================
    def test_011(self, name='invalid dataFormatIdentifier - 0x31 (out of range) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 FF 44 00 00 80 00 00 00 1E 00',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_012(self, name='invalid memory address - 0x31 (out of range) -- 2'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 FF FF FF FF 00 00 1E 00',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_013(self, name='invalid memory address - 0x31 (out of range) -- 3'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 FF FF FF FF FF FF FF FF',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    ###########################  Valid Calibration  #####################################
    def test_014(self, name='Download Calibration Data'):

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

    def test_015(self, name='Download Calibration Data, NRC 0x22'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 80 00 00 00 00 00',

            expected={
                'response': 'Negative',
                'data': '22'
            }
        )

    def test_016(self, name='Transfer Calibration Data'):
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

    def test_017(self, name='Request Transfer Exit'):
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

    def test_018(self, name='Upload PSI'):

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


    def test_019(self, name="<Activate default>"):
        test.preconditions(
            step_info=info(),
        )
        test.step(
            step_title=name,
            default_session_control=True,
            expected={"response": "Positive"},
        )

    def test_020(self, name="<Activate hardReset>"):
        test.preconditions(step_info=info(), power_mode="OFF")
        test.step(step_title=name, custom="11 01", expected={"response": "Positive"})