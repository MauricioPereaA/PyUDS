
            # This is and autogenerated test case using PyUDS Test Builder v0.2 #
        
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Application '
        )

        self.DIDs= [
            ('49 07', '00'*4),
            ('49 08', '00'),
            ('48 F9', '00'*8),
            ('4B 50', '00'*29),
            ('4B 51', '00'*10)
        ]

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='Enter security level 9'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            request_seed='09',
            send_key='09',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='All conditions satisfied DID '):
        test.preconditions(
            step_info=info(),
            signal = [
                    'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 2,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                    'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 2
            ]          
        )
        for DID in self.DIDs:
            test.step(
                step_title=name + DID[0],
                custom='2E ' + DID[0] + ' ' + DID[1],
                expected={
                    'response': 'Positive'
                }
            )
    
    def test_003(self, name='Condition 1 not satisfied DID '):
        test.preconditions(
            step_info=info(),
            signal = [
                    'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 3,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                    'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 2
            ]          
        )
        for DID in self.DIDs:
            test.step(
                step_title=name + DID[0],
                custom='2E ' + DID[0] + ' ' + DID[1],
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )
    
    def test_004(self, name='Condition 2 not satisfied DID '):
        test.preconditions(
            step_info=info(),
            signal = [
                    'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 2,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 1,
                    'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 2
            ]          
        )
        for DID in self.DIDs:
            test.step(
                step_title=name + DID[0],
                custom='2E ' + DID[0] + ' ' + DID[1],
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )

    def test_005(self, name='Condition 3 not satisfied DID '):
        test.preconditions(
            step_info=info(),
            signal = [
                    'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 2,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                    'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000
            ]          
        )
        for DID in self.DIDs:
            test.step(
                step_title=name + DID[0],
                custom='2E ' + DID[0] + ' ' + DID[1],
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )