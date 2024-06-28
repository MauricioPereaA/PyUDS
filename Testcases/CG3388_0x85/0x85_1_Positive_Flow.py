'''
    TestScript intended to perform CG3388 Tab 0x85 -- 1. Positive Flow
'''
'''  CG2019
Author: Manuel Medina
Modified by : Ricardo Montes  Date: 17-Jun-20
Modified by: Mauricio Perea        Date: 30-Sep-20

This script is intended to validate Functionality of service 0x85 which main function is to stop or resume the setting of diagnostic trouble codes (DTCs) in the server(s).


'''
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
            writeTestResults=True,
            excel_tab='0x85'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_003(self, name='Transition Server to extendedSession'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
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

    def test_005(self, name='DTC Setting On extendedSession Physical Messaging'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='Transition Server to extendedSession'):
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

    def test_007(self, name='Activate TesterPresent'):
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

    def test_008(self, name='DTC Setting Off extendedSession Functional Messaging'):
        test.preconditions(
            step_info=info(),

        )
        test.step(
            step_title=name,
            custom='85 02',
            expected={
                'response': 'Positive'
            }
        )

    def test_009(self, name='DTC Setting On extendedSession Functional Messaging'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_010(self, name='DTC Setting Off extendedSession Functional Messaging'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True

        )
        test.step(
            step_title=name,
            custom='85 02',
            expected={
                'response': 'Positive'
            }
        )