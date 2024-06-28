
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
from framework.shared_functions import ECU_info
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
            excel_tab='Multiple Tester & NRC 21'
        )
        self.tester = [ECU_info['name']+'_2', ECU_info['name']]
            
        #For each tester combination below, repeat Multiple Tester Test Steps 
        #    • Tester 1 = F1, Tester 2 = F2 -
        #    • Tester 1 = F1, Tester 2 = F3 -
        #    • Tester 1 = F1, Tester 2 = F4 -
        #    • Tester 1 = F1, Tester 2 = F5 -
        #    • Tester 1 = F1, Tester 2 = F6 -
        #    • Tester 1 = F2, Tester 2 = F1 -
        #    • Tester 1 = F3, Tester 2 = F1 -
        #    • Tester 1 = F4, Tester 2 = F1
        #    • Tester 1 = F5, Tester 2 = F1
        #    • Tester 1 = F6, Tester 2 = F1

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_003(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_005(self, name='T2: enable DTCs'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )

    def test_006(self, name='T1: enable DTCs'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_007(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
'''
    def test_008(self, name='T2: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_009(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_010(self, name='T2: enable DTCs'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Positive'
            }
        )
'''
