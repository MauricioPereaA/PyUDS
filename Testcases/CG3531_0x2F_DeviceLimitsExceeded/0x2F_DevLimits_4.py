
            # This is and autogenerated test case using PyUDS Test Builder v0.2 #

from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        testcase_not_supported_ecus = [
            'PTM', 'SCL', '..'
        ]

        if device_under_test in testcase_not_supported_ecus:
            raise Warning(__name__, 'is not supported by %s'%device_under_test)

        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x2F Device Limits Exceeded'
        )
        self.DIDs = {
            'ARB' : {
                'DID1' : '4B 5C',
                'mask1': '02',
                'code1': '0A 6D',

                'DID2' : '4B 5D',
                'mask2': '02',
                'code2': '0A 6D',
                
                'DID3' : '43 14',
                'mask3': '02',
                'code3': '09 03'
            },

            'MSM' : {
                'DID1' : '44 5D',
                'mask1': '00 00',
                'code1': '0A 13', # PrplSysActive code
                'data1': '0A',

                'DID2' : '44 5E',
                'mask2': '00 00',
                'code2': '0A 13',
                'data2': '0A',

                'DID3' : '4B 53',
                'mask3': '01 01 01 01 F0',
                'code3': '0A 13',
                'data3': '00 00 00 00'
            }
        }
        
        self.dut_dids = self.DIDs[device_under_test]

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='Transition to Default Diagnostic Session Application Mode'):
        test.preconditions(
            step_info=info()
        )
        test.restart_communication()
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_002(self, name='Transition to Extended Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_003(self, name='Activate TesterPresent'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_004(self, name='Read DID 0xXXX4'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID1'],
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='Valid controlState parameter(s) - Request I/O Control Short Term Adjustment DID 0xXXX4'):
        if device_under_test is 'ARB':
            test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
                ]
            )
        if device_under_test is 'MSM':
           test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0
                ]
            ) 
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID1'], self.dut_dids['mask1']
            ),
            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='Read DID 0xXXX4 - Verify I/O Control DID 0xXXX4 has successfully started or has reached its desired state'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'ARB':
            expected_data = self.dut_dids['mask1']
        elif device_under_test is 'MSM':
            expected_data = self.dut_dids['data1']
        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID1'],
            expected={
                'response': 'Positive',
                'data': expected_data
            }
        )

    def test_007(self, name='Create invalid conditions - Read Device Limits Exceeded for I/O Controls'):
        if device_under_test is 'ARB':
            test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
                ]
            )
        if device_under_test is 'MSM':
           test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 1
                ]
            )
        time.sleep(1)
        test.step(
            step_title='2F Request', 
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID1'], self.dut_dids['mask1'],),

            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data'    : '{0} {1}'.format(
                    self.dut_dids['DID1'], self.dut_dids['code1']
                )
            }
        )

    def test_008(self, name='Transition to Default Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_009(self, name='Verify contents of DID 0xF245 shall be retained across all diagnostic session transitions'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '{0} {1}'.format(
                    self.dut_dids['DID1'], self.dut_dids['code1']
                )
            }
        )

    def test_010(self, name='Transition to Extended Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_011(self, name='Transition to Safety Diagnostic Session (If Supported)'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 04',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_012(self, name='Transition to Default Diagnostic Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_013(self, name='Verify contents of DID 0xF245 shall be retained across all diagnostic session transitions'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '{0} {1}'.format(
                    self.dut_dids['DID1'], self.dut_dids['code1']
                )
            }
        )

    def test_014(self, name='Transition to Programming Diagnostic Session Boot Mode'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='test_010_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        # End -- Boot Mode preconditions

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,

            custom='10 02',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_015(self, name='Transition to Default Diagnostic Session Application Mode'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

        if test.catch_error_frames():
            test.restart_communication()

    def test_016(self, name='Verify contents of DID 0xF245 shall be retained across diagnostic session transition'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '{0} {1}'.format(
                    self.dut_dids['DID1'], self.dut_dids['code1']
                )
            }
        )

    def test_017(self, name='Transition to extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_018(self, name='TesterPresent'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_019(self, name='Hard Reset'):
        if device_under_test is not 'MSM':
            test.preconditions(
                step_info=info(),
                power_mode='OFF'
            )
            test.step(
                step_title=name,
                custom='11 01',
                expected={
                    'response': 'Positive'
                }
            )
        else:
            print('Test step not supported by %s'%device_under_test)
            return 0

    def test_020(self, name='Verify contents of DID 0xF245 are reset to 0x00000000'):
        if device_under_test is not 'MSM':
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F2 45',
                expected={
                    'response': 'Positive',
                    'data': '00 00 00 00'
                }
            )
        else:
            print(__name__, 'MSM does not support Service 0x11')

    def test_021(self, name='Transition to Extended Session'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_022(self, name='TesterPresent'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_023(self, name='Read DID 0xXXX5'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID2'],
            expected={
                'response': 'Positive'
            }
        )

    def test_024(self, name='Valid controlState parameter(s) - Request I/O Control Short Term Adjustment DID 0xXXX5'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
            ]
        )
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID2'], self.dut_dids['mask2']
            ),
            expected={
                'response': 'Positive'
            }
        )
    def test_025(self, name='Read DID 0xXXX5'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID2'],
            expected={
                'response': 'Positive'
            }
        )

    def test_026(self, name='Verify the Short Term Adjustment DID 0xXXX5'):
        test.preconditions(
            step_info=info()
        )

        if device_under_test is 'ARB':
            expected_data = self.dut_dids['mask2']
        elif device_under_test is 'MSM':
            expected_data = self.dut_dids['data2']

        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID2'],
            expected={
                'response': 'Positive',
                'data': expected_data
            }
        )

    def test_027(self, name='Create invalid conditions - Verify contents of DID 0xF245 '):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
            ]
        )
        test.step(
            step_title='2F Request', 
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID2'], self.dut_dids['mask2']),
            expected={
                'response': 'Negative',
                'data'    : '22'
            }    
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '{0} {1}'.format(
                    self.dut_dids['DID2'], self.dut_dids['code2']
                )
            }
        )

    def test_028(self, name='Valid controlState parameter(s) - Request I/O Control Short Term Adjustment DID 0xXXX5 again'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
            ]
        )
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID2'], self.dut_dids['mask2']
            ),
            expected={
                'response': 'Positive'
            }
        )

    def test_029(self, name='Verify contents of DID 0xF245 are reset to 0x00000000 again'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '00 00 00 00'
            }
        )

    def test_030(self, name='Create invalid conditions - Verify contents of DID 0xF245 - 0xXX6'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
            ]
        )
        test.step(
            step_title='2F Request', 
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID3'], self.dut_dids['mask3']
            )    
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '{0} {1}'.format(
                    self.dut_dids['DID3'], self.dut_dids['code3']
                )
            }
        )

    def test_031(self, name='Create valid conditions - Request I/O Control Short Term Adjustiment DID XXX6'):
        if device_under_test is 'ARB':
            test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
                ]
            )
        if device_under_test is 'MSM':
            test.preconditions(
                step_info=info(),
                signal=[
                    'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0
                ]
            )
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(
                self.dut_dids['DID3'], self.dut_dids['mask3']
            ),
            expected={
                'response': 'Positive'
            }
        )

    def test_032(self, name='Verify contents of DID 0xF245 are reset to 0x00000000'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 45',
            expected={
                'response': 'Positive',
                'data': '00 00 00 00'
            }
        )

    def test_033(self, name='Request I/O Control Return Control To ECU'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F %s 00'%self.dut_dids['DID1'],
            expected={
                'response': 'Positive'
            }
        )