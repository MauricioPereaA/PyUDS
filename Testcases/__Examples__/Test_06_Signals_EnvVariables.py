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
            writeTestResults=False # Write on CG Report
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Functional Req - Read Data ID using Service request - Expected response and data length'):

        test.preconditions(
            # === Pre-conditions ===
            step_info=info(),               # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            functionalAddr=False,           # Functional Addressed Request -ENABLED-
            signal=[
                'BSPMP_RmtProgmActvAuth', 'BkupSysPwrMode_Prtctd_PDU', 1
            ]
        )

        test.step(
            # === Name & Service Request ===
            step_title=name,                # name defined above with-in test function
            read_data_ID='F0 80',           # Read Data ID - Service request
        )
        time.sleep(2.5)