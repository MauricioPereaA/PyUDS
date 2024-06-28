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

    def test_001(self, name='All conditions satisfied DID 5029'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1
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
            custom='2F 50 29 00',
            expected={
                'response': 'Positive'
            }
        )     
        
    def test_002(self, name='Condition 1 not satisfied DID 5029'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1
            ]          
        )

        test.step(
            step_title=name,
            custom='2F 50 29 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_003(self, name='Condition 2 not satisfied DID 5029'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            custom='2F 50 29 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_004(self, name='Condition 3 not satisfied DID 5029'):
        
        test.canoe.set_system_variable(
        namespace='ARC_Functions',
        variable='VSADP_ARC_sts',
        status=False
        )

        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1
            ]          
        )
        time.sleep(1)

        test.step(
            step_title=name,
            custom='2F 50 29 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
    
    def test_005(self, name='Condition 4 not satisfied DID 5029'):
        
        test.canoe.set_system_variable(
        namespace='ARC_Functions',
        variable='VSADP_ARC_sts',
        status=True
        )
        
        test.canoe.set_system_variable(
        namespace='ARC_Functions',
        variable='TEGP_ARC_sts',
        status=False
        )
        test.preconditions(
            step_info=info(),
            signal = [
                        'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                        'TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1
            ]          
        )
        time.sleep(1)

        test.step(
            step_title=name,
            custom='2F 50 29 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )