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

    def test_001(self, name='Request Manufacturing Mode seed security access'):
        test.preconditions(
            step_info=info()         
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            request_seed='03',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='Send key'):
        test.preconditions(
            step_info=info()         
        )

        test.step(
            step_title=name,
            send_key='03',
            expected={
                'response': 'Positive'
            }
        )

    def test_003(self, name='All conditions satisfied RID 0205'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'PSP_EngRnngAuth', 'PrplStat_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 05',
            expected={
                'response': 'Positive'
            }
        )     
        
    def test_004(self, name='Condition 1 not satisfied RID 0205'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 1,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'PSP_EngRnngAuth', 'PrplStat_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 05',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_005(self, name='Condition 2 not satisfied RID 0205'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000,
                        'PSP_EngRnngAuth', 'PrplStat_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 05',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_006(self, name='Condition 3 not satisfied RID 0205'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0,
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'PSP_EngRnngAuth', 'PrplStat_Prtctd_PDU', 1
            ]          
        )

        test.step(
            step_title=name,
            custom='31 01 02 05',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )