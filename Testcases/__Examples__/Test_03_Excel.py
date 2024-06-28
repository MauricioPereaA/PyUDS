'''

     Test Example - Writing Test Results on a CG Excel Report

'''
from framework.shared_functions import tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        tools.popup.warning(__name__,
                            'This test script is just to be taken as a template.\n'+
                            'It might not work unless you provide valid test_rows.json '+
                            'containing the function steps from this script and its corresponding rows.\n'+
                            'To find a working example please refer to Test cases from CG3388, CG3531 & CG4577')
        test.begin(
            test_info=info(),                   # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            writeTestResults=True,              # Write on CG Report -ENABLED-
            excel_tab='0x10'
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='start tester present'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response' : 'Positive'         # By providing expected argument containing a 'dict'
                                                # reporting will be enabled (HTML, test_report, Excel reporting)
            }
        )

    def test_002(self, name='Test Step 2'):
        time.sleep(2.5)                         
        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )
        test.step(
            step_title=name,
            read_data_ID='F0 81'                # This test step does not have expected argument
        )                                       # Hence, it will not write any report, just will perform the instruction

    def test_003(self, name='Stop tester present'):
        time.sleep(2.5)
        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )
        test.step(
            step_title=name,
            stop_tester_present=True,

            expected={
                'response' : 'No response'      # Expecting a No response
                                                # This step will be written in HTML, test_report & Excel
            }
        )
    
    def test_004(self, name='Test Step 4'):
        time.sleep(2.5)
        test.preconditions(
            step_info=info(),
            sbat=False,
            functionalAddr=False
        )
        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'  : 'Positive',       # Criteria is taken to validate response received
                'dataLength': 4
            }
        )
