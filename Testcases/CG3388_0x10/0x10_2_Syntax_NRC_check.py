          # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x10'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        
    def test_004(self, name='<Transition Server to defaultSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present='true',

            expected={
                'response': 'No response'
            }
        )
        
    def test_025(self, name='conditionsNotCorrect enabled Comm - 0x22 (programmingSession)'):
        test.preconditions(
            current_step='preconditions',
            functionalAddr=True
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            dtc_settings=False,
            communication_control=True,
            request_seed='01',
            send_key='01'
        )
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
 
    def test_026(self, name='suppressPosRspMsgIndicationBit '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 82',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )

    def test_035(self, name='conditionsNotCorrect enabled DTCs - 0x22 (programmingSession)'):
        test.preconditions(
            current_step='preconditions',
            functionalAddr=True
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            dtc_settings=True,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )

    def test_036(self, name='suppressPosRspMsgIndicationBit'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 82',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_040(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_041(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present='true',

            expected={
                'response': 'No response'
            }
        )

    def test_042(self, name='<Disable DTCs>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='85 01',

            expected={
                'response': 'Positive'
            }
        )   

    def test_043(self, name='<Disable Normal Communication>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 03 01',

            expected={
                'response': 'Positive'
            }
        )
        
    def test_044(self, name='Send a physically addressed request'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='05',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )
        
    def test_045(self, name='<Unlock the Server via security access service>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='05',

            expected={
                'response': 'Positive'
            }
        ) 

    def test_046(self, name='Send a physically addressed request'):        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )    

    def test_047(self, name='<Transition Server to defaultSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
        
    def test_048(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )

    def test_049(self, name='suppressPosRspMsgIndicationBit'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 82',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
    def test_055(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_056(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present='true',

            expected={
                'response': 'No response'
            }
        )

    def test_057(self, name='<Disable DTCs>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='85 01',

            expected={
                'response': 'Positive'
            }
        )   

    def test_059(self, name='<Disable Normal Communication>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 03 01',

            expected={
                'response': 'Positive'
            }
        )    
        
    def test_060(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_061(self, name='Send a physically addressed request'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='09',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )
        
    def test_062(self, name='<Unlock the Server via security access service>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='09',

            expected={
                'response': 'Positive'
            }
        ) 
        
    def test_063(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_064(self, name='Send a physically addressed request'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='0B',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )
        
    def test_065(self, name='<Unlock the Server via security access service>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='0B',

            expected={
                'response': 'Positive'
            }
        )

    def test_066(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_067(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0D',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_068(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0D',

            expected={
                'response'   : 'Positive'
            }
        )
        
    def test_069(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_070(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_071(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='11',

            expected={
                'response'   : 'Positive'
            }
        )
        
    def test_072(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_073(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_074(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='13',

            expected={
                'response'   : 'Positive'
            }
        )
        
    def test_075(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )

    def test_076(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_077(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='15',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_078(self, name='<Transition Server to programmingSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '22'
            }
        )
        
    def test_079(self, name='<Transition Server to defaultSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )