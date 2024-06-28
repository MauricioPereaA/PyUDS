'''
    Test Example - CANoe Start / Stop simulation
'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()
class Test_UDS(unittest.TestCase):

# === Run 1ST ===
    @classmethod
    def setUpClass(self):
        ''' Runs at the beggining of the test '''
        test.begin(                         # TestCase() Class - Test Begin Method:
                                            #   ** Opens .cfg, Starts CANoe simulation, sends envVNMFSend
            test_info=info(),               # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            writeTestResults=False          # Write on CG Report -ENABLED-

        )

# === Run 3RD ===
    @classmethod
    def tearDownClass(self):
        ''' Runs at the end of the test '''
        test.end()                          # TestCase() Class - Test End Method:
                                            #   ** Stops CANoe simulation, finished logs and copies them to a '<Test name>_<timestamp>' folder
# === Run 2ND ===
    
    def test_001(self, name='CANoe Simulation Test - Multiple tester test'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['10 03', '10 03'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )