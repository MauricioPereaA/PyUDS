
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test        
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest
import time


test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test case template ==#
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
                'mask1': '06',

                'DID2' : '4B 5D',
                'mask2': '02',

                'DID3' : '4B 5D',
                'mask3': 'FF'
            },

            'MSM' : {
                'DID1' : '44 5D',
                'mask1': '00 00',
                'data1': '0A',

                'DID2' : '44 5E',
                'mask2': '00 00',
                'data2': '0A',

                'DID3' : '44 5F',
                'mask3': '0C FF'
            }
        }

        self.dut_dids = self.DIDs[device_under_test]

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Transition to Extended Diagnostic Session'):
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

    def test_002(self, name='Activate TesterPresent'):
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

    def test_003(self, name='Read XX X1'):
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

    def test_004(self, name='Correct conditions for XXX1 + Request I/O Control Short Term Adjustment DID 0xXXX1'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
            ]
        ) # This works only for MSM (DID 44 5D) & ARB (DID 4B 5C)
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(self.dut_dids['DID1'], self.dut_dids['mask1']),
            
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='Read DID 0xXXX1 - Verify Short Term Adjustment has successfully started'):
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

    def test_006(self, name='Read DID 0xXXX2'):
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

    def test_007(self, name='Incorrect conditions for DID XX X2 + Request I/O Control Short Term Adjustment DID 0xXXX2'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
            ]
        )
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(self.dut_dids['DID2'], self.dut_dids['mask2']),
            
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
    def test_008(self, name='Read DID 0xXXX1'):
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

    def test_009(self, name='Read DID 0xXXX3'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 %s'%self.dut_dids['DID3'],
            expected={
                'response': 'Positive'
            }
        )

    def test_010(self, name='Correct conditions for XXX3 + Request I/O Control Short Term Adjustment DID 0xXXX3 with control value out of range'):
        test.preconditions(
            step_info=info(),
            signal=[
                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
            ]
        )
        test.step(
            step_title=name,
            custom='2F {0} 03 {1}'.format(self.dut_dids['DID3'], self.dut_dids['mask3']),
            
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_011(self, name='Verify rejecting the request on previous step did not affect XX X1'):
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

