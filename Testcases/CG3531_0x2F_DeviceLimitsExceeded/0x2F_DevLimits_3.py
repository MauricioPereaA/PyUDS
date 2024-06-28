
            # This is and autogenerated test case using PyUDS Test Builder v0.2 #

from framework.shared_functions import device_under_test        
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        testcase_not_supported_ecus = [
            'PTM', 'SCL', '..'
        ]

        if device_under_test in testcase_not_supported_ecus:
            raise Warning(__name__, 'is not supported by %s'%device_under_test)

        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x2F Device Limits Exceeded'
        )
    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Power-up Initialization - Transition to Default Diagnostic Session'):
        test.preconditions(
            step_info=info(),
            reset_communication=True
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_002(self, name='Verify DID 0xF245 is supported in defaultSession and initialized to 0x00000000 at power-up'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '00 00 00 00'
            }
        )

    def test_003(self, name='Power down & up - Transition to Extended Diagnostic Session'):
        test.preconditions(
            step_info=info(),
            reset_communication=True
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_004(self, name='Activate TesterPresent'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_005(self, name='Verify DID 0xF245 is supported in extendedSession and initialized to 0x00000000 at power-up'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '00 00 00 00'
            }
        )

    def test_006(self, name='Transition to Safety Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 04',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_007(self, name='Activate TesterPresent  - safety Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_008(self, name='Verify DID 0xF245 is not supported in safetySession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_009(self, name='Transition to Default Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,

            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_010(self, name='Transition to Programming Diagnostic Session'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='test_010_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        # End -- Boot Mode preconditions

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,

            custom='10 02',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_011(self, name='Verify DID 0xF245 is not supported in programmingSession Boot Mode'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

