'''

    Read DID - Examples

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
            writeTestResults=False          # Write on CG Report
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Functional Req - Read Data ID using Service request - Expected response and data length'):

        test.preconditions(
            # === Pre-conditions ===
            step_info=info(),               # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            functionalAddr=True,             # Functional Addressed Request -ENABLED-
            response_from_log=True           # Alternative Method for reading out a response - Takes it out of 'traceLog.asc' file 
        )

        test.step(
            # === Name & Service Request ===
            step_title=name,                # name defined above with-in test function
            read_data_ID='F1 A0',           # Read Data ID - Service request
            # === Expected Params ===
            expected={
                'response'  : 'Positive',   # Expected response
                'data'      : '00',
                'dataLength': 1             # Byte length expected
            }
        )

    def test_002(self, name='Physical Req - Read Data ID using Custom request - Expected response and data'):

        test.preconditions(
            step_info=info(),
            functionalAddr=False,            # Functional Addressed Request -DISABLED-
            response_from_log=False
        )
        test.step(
            step_title=name,
            custom='22 F1',                 # Invalid format Request

            expected={
                'response' : 'Negative',    # Expected response
                'data'     : '13'           # Data expected from reading Data ID
            }
        )
    
    def test_003(self, name='Functional Req - Read Data ID using Service request - No expected'):

        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )

        test.step(
            step_title=name,
            read_data_ID='F0 80'            # No expected defined
        )