
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
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
            writeTestResults=False
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Transition to extendedSession, Application Mode'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            extended_session_control=True,
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_002(self, name='Disable Comm'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='85 02',
            expected={
                'response': 'Positive'
            }
        )

    def test_003(self, name='Disable DTCs'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='Req Seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='Send Key'):
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

    def test_006(self, name='Transition to programming'):
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
        input('Press ENTER to end the test!')

