'''

     ** Provision Keys ** 

'''
from framework.shared_functions import ECU_info, keys, supported_ecus
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False,  # Write on CG Report - Enable / Disable
            debug=False              # Write Actual response and expected in Report for Debug
        )
		
        ''' Device Under Test '''
        self.supported_ecus = supported_ecus
        self.DUT = ''.join([i for i in self.supported_ecus if i in ECU_info['name']])
    
        self.keys = keys[self.DUT]['provision_key']

        self.keys_0272 = keys[self.DUT]['unlock_key'] + keys[self.DUT]['master_key'] 

    @classmethod
    def tearDownClass(self):
        test.end()

    def test_001(self, name='ProvisionKeys - RID 0200'):
        test.preconditions(      
            step_info=info()


        )

        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
            start_tester_present=True,
            communication_control=False,
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
			
    def test_002(self, name='Master Key & Unlock Key'):
        test.preconditions(      
            step_info=info()
        )

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


'''    def test_003(self, name='Delete SBAT & set MEC = 0'):
        
        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
			start_tester_present=True,
            request_seed='01',
            send_key='01'
        )
        test.preconditions(      
            step_info=info()
        )
        
        test.step(
            step_title='Transition to Extended Session',
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )'''