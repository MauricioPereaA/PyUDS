
            # This is and autogenerated test case using PyUDS Test Builder v0.2 #
        
from framework.shared_functions import ECU_info, keys, supported_ecus
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        input('Please reflash your unit. Then disconnect the programming tool and press Enter when done...')
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Application '
        )

        self.DIDs= [
            ('44 5D', '03 03 03'),
            ('44 5E', '03 03 03'),
            ('44 5F', '03 03 03'),
            ('44 60', '03 03 03'),
            ('44 62', '03 03 03'),
            ('44 63', '03 03 03'),
            ('44 64', '03 03 03'),
            ('44 65', '03 03 03'),
            ('44 66', '03 03 03'),
            ('44 67', '03 03 03'),
            ('44 68', '03 03 03'),
            ('44 69', '03 03 03'),
            ('44 6A', '03 03 03'),
            ('44 6B', '03 03 03'),
            ('44 6C', '03 03 03'),
            ('44 6E', '03 03'),
            ('44 6F', '03 03 03'),
            ('49 5F', '03 03')
        ]

        #Device Under Test
        self.supported_ecus = supported_ecus
        self.DUT = ''.join([i for i in self.supported_ecus if i in ECU_info['name']])
    
        self.keys = keys[self.DUT]['provision_key']

        self.keys_0272 = keys[self.DUT]['unlock_key'] + keys[self.DUT]['master_key'] 

    @classmethod
    def tearDownClass(self):
        #Delete SBAT & set MEC = 0
        test.preconditions(      
            step_info=info(),
			mec_zero=True
        )

        #== End Test Case ==#
        test.end()

    def test_001(self, name='Preconditions'):
        test.preconditions(
            step_info=info(),
            mec_zero=False
        )

        #ProvisionKeys - RID 0200
        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='01',
            send_key='01'
        )
		
        for key in self.keys:
            test.step(
                step_title='Send keys',
                start_routine=['02 00', key],

                expected={
                    'response':'Positive'
                }
            )
        
        #Master Key & Unlock Key
        test.step(
            step_title='Sec Lvl 0D',
            extended_session_control=True,
			start_tester_present=True,
            request_seed='0D',
            send_key='0D'
        )
		
        for key in self.keys_0272:
            test.step(
                step_title='Send keys',
                start_routine=['02 72', key],

                expected={
                    'response': 'Positive'
                }
			)

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
        )
    
    def test_002(self, name='Condition 1 not satisfied DID '):        
        test.preconditions(
            step_info=info(),
            signal = [
                    'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 0,
                    'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 100,
                    'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
            ]          
        )

        for DID in self.DIDs:
            test.step(
                step_title=name + DID[0],
                custom='2F ' + DID[0] + ' ' + DID[1],
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )