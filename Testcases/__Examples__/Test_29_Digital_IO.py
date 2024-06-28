
''' Developer : Mauricio Perea
    10 December 2020
    Digital IO
'''        
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            step_delay=0.005
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Enable CAN Communication'):

        test.canoe.set_system_variable( 
            namespace = 'IO::VN1600_1',
            variable = 'DOUT',
            value = 0
        )

    def test_002(self, name='Functional Req - Read Data ID using Service request - Expected response and data length'):

        test.preconditions(
            # === Pre-conditions ===
            step_info=info(),               # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            functionalAddr=True,             # Functional Addressed Request -ENABLED-
            response_from_log=True           # Alternative Method for reading out a response - Takes it out of 'traceLog.asc' file 
        )

        test.step(
            # === Name & Service Request ===
            step_title=name,                # name defined above with-in test function
            custom='22 F1 A0', 
           
            # === Expected Params ===
            expected={
                'response'  : 'Positive'   # Expected response
             
            }
        )
    
       
    def test_003(self, name='Disable CAN Communication'):
        test.preconditions(
            # === Pre-conditions ===
            step_info=info()              # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
          )

        test.canoe.set_system_variable( 
            namespace = 'IO::VN1600_1',
            variable = 'DOUT',
            value = 1
        )
        
    time.sleep(10)
        
    def test_004(self, name='Functional Req - Read Data ID using Service request - Expected response and data length'):

        test.preconditions(
            # === Pre-conditions ===
            step_info=info(),               # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
            functionalAddr=True,             # Functional Addressed Request -ENABLED-
            response_from_log=True           # Alternative Method for reading out a response - Takes it out of 'traceLog.asc' file 
        )

        test.step(
            # === Name & Service Request ===
            step_title=name,                # name defined above with-in test function
            custom='22 F1 A0',
            #read_data_ID='F1 A0',           # Read Data ID - Service request
            # === Expected Params ===
            expected={
                'response'  : 'Positive'   # Expected response
               
            }
        )
    
    def test_005(self, name='Enable CAN Communication'):
        test.preconditions(
            # === Pre-conditions ===
            step_info=info()              # info() -> inspect.stack() -> Return a list of frame records for the caller’s stack.
        )

    # Example 1 - Provide namespace as per found in Signal Panel - Enable
        test.canoe.set_system_variable( 
            namespace = 'IO::VN1600_1',
            variable = 'DOUT',
            value = 0
        )
        
    time.sleep(10)

    
    def test_006(self, name='Functional Req - Read Data ID using Service request - Expected response and data length'):

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
                'response'  : 'Positive'   # Expected response
               
            }
        )
        
   