'''

    RID 0200_0204_0205_0272
    
    Corporate Common RIDs are defined and maintained by General Motors. 
    GB6001 contains the requirement to support the infrastructure RIDs. 
    The Diagnostic CTRS (odx) file provides definition for the RIDs 
    (structure and format). Other requirements documents are referenced 
    in the Description when additional information is specified therein.


'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()

class RID_0200_0204_0205_0272(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='RID 0200_0204_0205_0272'   # Specify CG Excel Tab
        )      

        ''' RID to be tested '''
        self.RID = '02 72'
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_005(self, name='Transition to extendedSession, Application Mode'):
        ''' 
        Define request conditions 
         - Step info *Dynamically changes*
         - Request address type
         - Power mode
         - Environment Variables
         - Signals
        '''

        test.preconditions(
            
            step_info=info(),
            transmit_in_off=True,
            signal=[
                'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'PSP_PrplSysActvAuth', 'PrplStat_Prtctd_PDU', 0
            ],
            power_mode='off'
            
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )

    def test_006(self, name='Activate TesterPresent'):

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

    def test_007(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_008(self, name='Access Security Request Seed'):

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

    def test_009(self, name='Access Security Send Key'):

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

    def test_010(self, name='Start Routine Provision Security Peripheral All Keys in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID, '02' + '00'*64],

            expected={
                'response'   : 'Negative',
                'data'       : '22'
            }
        )
