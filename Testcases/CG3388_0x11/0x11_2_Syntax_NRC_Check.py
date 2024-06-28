
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        if device_under_test is 'MSM':
            tools.popup.warning(
                title=__name__,
                description='MSM does not support Service 0x11'
            )
            raise Warning(__name__, 'MSM does not support Service 0x11')

        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x11'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='<Transition Server to extendedSession> '):
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

    def test_002(self, name='<Activate TesterPresent>'):
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
        
    def test_004(self, name='conditionsNotCorrect - 0x22'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN'
        )
        time.sleep(1)
        test.step(
            step_title=name,
            custom='11 01',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
        
        
    def test_005(self, name='conditionsNotCorrect - 0x22'):
        test.preconditions(
            step_info=info()
        )
        
        test.step(
            step_title='Preconditions',
            extended_session_control=True,            
            start_tester_present=True
        )
        
        test.preconditions(
        step_info=info()
        )
        
        test.step(
            step_title=name,
            custom='11 81',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )



