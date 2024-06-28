from framework.shared_functions import ECU_info, keys, supported_ecus
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        input('Please reflash your unit. Then disconnect the programming tool and press Enter when done...')
        
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Application '
        )

        #Device Under Test
        self.supported_ecus = supported_ecus
        self.DUT = ''.join([i for i in self.supported_ecus if i in ECU_info['name']])
    
        self.keys = keys[self.DUT]['provision_key']

        self.keys_0272 = keys[self.DUT]['unlock_key'] + keys[self.DUT]['master_key'] 

    @classmethod
    def tearDownClass(self):
        test.preconditions(      
            step_info=info(),
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

    def test_002(self, name='Condition 1 satisfied DID F1 A0'):        
        test.preconditions(
            step_info=info(),       
        )

        test.step(
            step_title=name,
            custom='2E F1 A0 50',
            expected={
               'response': 'Positive'
            }
        )
    
    def test_003(self, name='Condition 1 not satisfied DID F1 A0'):        
        test.preconditions(
            step_info=info(),
            mec_zero=True         
        )

        test.step(
            step_title=name,
            custom='2E F1 A0 FF',
            expected={
               'response': 'Negative',
               'data': '22'
            }
        )