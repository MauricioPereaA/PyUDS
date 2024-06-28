#2 Syntax NRC Check. Rows from 9 - 11

from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()


class Request_Download(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,  # Write on CG Report
            excel_tab='0x36'  # Specify CG Excel Tab
        )

        self.DUT = device_under_test

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_003(self, name='Transition Server to extendedSession'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=True

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

    def test_009(self, name='Transition Server to programmingSession'):

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

    def test_010(self, name='Erase Application'):
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

    def test_011(self, name='Request Download'):

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


    def test_012(self, name="Wrong Block Sequence Counter"):
        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="36 02",
            expected={"response": "Negative", "data": "73"})