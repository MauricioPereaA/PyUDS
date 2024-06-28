'''

     ** Provision Keys ** 

'''

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
    @classmethod
    def tearDownClass(self):
        test.end()

    def test_001(self, name='Delete SBAT & set MEC = 0'):
        test.preconditions(      
            step_info=info(),
			mec_zero=True,
			sbat=False
        )
        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
			start_tester_present=True,
            request_seed='01',
            send_key='01'
        )
        
        test.step(
            step_title='Transition to Extended Session',
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )