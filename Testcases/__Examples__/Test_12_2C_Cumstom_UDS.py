'''
    This is a Test Example for PyUDS
'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()

class Test_UDS_Example(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False
        )      

        self.srcDIDs = (
            '55CE', #F0
            '4457', #F1
            '4471', #F2
            '445B', #F3
            '445A', #F4
            '495E', #F5
            '445C', #F6
            '4471', #F7
            '4455', #F8
            '4467', #F9
            '446B', #FA
            '495F', #FB
            '4960', #FC
            '472F', #FD
            '47A8', #FE
            '446A'  #FF
        )
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def format_hex(self, decimal):
        return hex(decimal).replace('0x','').upper()

    def test_001(self, name='Step 1_Transition to extendedSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        )

    def test_002(self, name='Step 2_Activate TesterPresent'):

        test.preconditions(
            step_info=info()            
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response'   : 'No response'
            }
        )

    def test_003(self, name='Step 3_DynamicallyDefineDataIdentifier, defineByIdentifier F2 C0 - F2 FF'):

        test.preconditions(
            step_info=info()
        )

        for byte in range(192, 256):
            test.step(
                step_title=name,
                custom='2C 01 F2 {} 44 55 01 01'.format(self.format_hex(byte)), 
                expected={
                    'response'   : 'Positive'
                }
            )
