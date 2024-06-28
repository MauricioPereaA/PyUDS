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

    def test_001(self, name='Condition 1 not satisfied DID 5182'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'RCIP_RrClsrMtnCtlParmEnblAuth', 'RrClsrInfo_Prtctd_PDU', 1
            ]          
        )

        test.step(
            step_title='Security Level 09',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='09',
            send_key='09',
            expected={
                'response': 'Positive'
            }
        )

        input('\n**Please create conditions so DTC U040100 is set. Make sure DTC U042200 is not set. Press Enter when done...**\n')

        test.step(
            step_title=name,
            custom='2F 51 82 03 00 09 FF',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_002(self, name='Condition 2 not satisfied DID 5182'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'RCIP_RrClsrMtnCtlParmEnblAuth', 'RrClsrInfo_Prtctd_PDU', 1
            ]          
        )

        input('\n**Please create conditions so DTC U042200 is set. Make sure DTC U040100 is not set. Press Enter when done...**\n')

        test.step(
            step_title=name,
            custom='2F 51 82 03 00 09 FF',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )   