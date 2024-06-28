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

    def test_001(self, name='Request Remote Diagnostics Mode seed security access'):
        test.preconditions(
            step_info=info()          
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            request_seed='0B',
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
            send_key='0B',
            expected={
                'response': 'Positive'
            }
        )

    def test_003(self, name='All conditions satisfied DID 4314'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1,
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0 
            ]          
        )

        test.step(
            step_title='Security Level 0B',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='0B',
            send_key='0B',
            expected={
                'response': 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='2F 43 14 00',
            expected={
                'response': 'Positive'
            }
        )     
        
    def test_004(self, name='Condition 1 not satisfied DID 4314'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1,
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0 
            ]          
        )

        test.step(
            step_title=name,
            custom='2F 43 14 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_005(self, name='Condition 2 not satisfied DID 4314'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 0,
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0 
            ]          
        )

        test.step(
            step_title=name,
            custom='2F 43 14 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_006(self, name='Condition 3 not satisfied DID 4314'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1,
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 1 
            ]          
        )

        test.step(
            step_title=name,
            custom='2F 43 14 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_007(self, name='Remote Diagnostics Mode canceled and General Conditions satisfied DID 4314'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 100,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1,
                        'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title='Security Level 01',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='01',
            send_key='01',
            expected={
                'response': 'Positive'
            }
        )


        test.step(
            step_title=name,
            custom='2F 43 14 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )