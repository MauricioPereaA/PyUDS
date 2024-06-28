from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Application '
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='All conditions satisfied RID 0204'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0
            ]          
        )

        test.step(
            step_title='Security Level 03',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='03',
            send_key='03',
            expected={
                'response': 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='31 01 02 04',
            expected={
                'response': 'Positive'
            }
        )     
        
    def test_002(self, name='Condition 1 not satisfied RID 0204'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 1
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 04',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )