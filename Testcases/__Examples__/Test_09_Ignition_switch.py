'''

     ** Test Template ** 

'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_PyUDS_SecurityLevels(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False # Write on CG Report
        )

        self.supported_lvls = {
            '01', '03', '09', '0B', '0D', '11', '05', '13', '15'
        }

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()
    
    def test_001(self, name='Ignition switch'):
        test.preconditions(
            step_info=info(),
            ignition_switch=['OFF', 'PROP','OFF']
        )
        test.step(
            step_title=name,
            read_data_ID='F1 A0',
            expected={
                'response': 'Positive'
            }
        )