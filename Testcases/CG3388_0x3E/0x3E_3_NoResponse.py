            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x3E'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='transition to defaultSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_003(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_004(self, name='transition to extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='<Activate TesterPresent-ExtendedSession>'):
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

    def test_006(self, name='transition to extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_007(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_009(self, name='Pyrotechnic ECU Test'):
        pass

    def test_010(self, name='Pyrotechnic ECU Test'):
        pass

    def test_013(self, name='Pyrotechnic ECU Test'):
        pass

    def test_014(self, name='Pyrotechnic ECU Test'):
        pass
    '''
    def test_016(self, name='Service not supported Test'):
        pass

    def test_017(self, name='Service not supported Test'):
        pass

    def test_018(self, name='subFunctionNotSupported - No Response'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            custom='3E 01',
            expected={
                'response': 'No response'
            }
        )

    def test_019(self, name='subFunctionNotSupported - No Response'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control=True,
            custom='3E 02',
            expected={
                'response': 'No response'
            }
        )

    def test_020(self, name='Pyrotechnic ECU Test'):
        pass

    def test_021(self, name='subFunctionNotSupported - No Response'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            custom='3E FF',
            expected={
                'response': 'No response'
            }
        )

    def test_022(self, name='subFunctionNotSupported - No Response'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control=True,
            custom='3E FF',
            expected={
                'response': 'No response'
            }
        )
    

    def test_023(self, name='Pyrotechnic ECU Test'):
        pass
    '''