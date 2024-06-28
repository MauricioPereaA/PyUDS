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

    def test_001(self, name='All conditions satisfied RID 0200'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0
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
            custom='31 01 02 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 55 5C 31 DE A4 7D ED 05 C3 F6 F5 CC AB 2A 29 01 A1 70 3E 01 AD A1 D2 00 7F 62 BF 29 CD 52 9B 00 E1 6E F6 96 25 F6 52 4F 9E FA 8D AC 35 72 62 AC 6D',
            expected={
                'response': 'Positive'
            }
        )     
        
    def test_002(self, name='Condition 1 not satisfied RID 0200'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 1,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 55 5C 31 DE A4 7D ED 05 C3 F6 F5 CC AB 2A 29 01 A1 70 3E 01 AD A1 D2 00 7F 62 BF 29 CD 52 9B 00 E1 6E F6 96 25 F6 52 4F 9E FA 8D AC 35 72 62 AC 6D',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_003(self, name='Condition 2 not satisfied RID 0200'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 55 5C 31 DE A4 7D ED 05 C3 F6 F5 CC AB 2A 29 01 A1 70 3E 01 AD A1 D2 00 7F 62 BF 29 CD 52 9B 00 E1 6E F6 96 25 F6 52 4F 9E FA 8D AC 35 72 62 AC 6D',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )