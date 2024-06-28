'''

    RID 0200_0204_0205_0272
    
    Corporate Common RIDs are defined and maintained by General Motors. 
    GB6001 contains the requirement to support the infrastructure RIDs. 
    The Diagnostic CTRS (odx) file provides definition for the RIDs 
    (structure and format). Other requirements documents are referenced 
    in the Description when additional information is specified therein.


'''
from framework.shared_functions import device_under_test, keys
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
        
        ''' Device Under Test '''
        #self.supported_ecus = ['MSM', 'PTM', 'ARB']
        #self.DUT = ''.join([i for i in self.supported_ecus if i in ECU_info['name']])
        self.DUT = device_under_test
        self.unlock_key = keys[self.DUT]['unlock_key'][0]
        
        

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
            step_info=info()
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
            step_title='Start Routine for Unlock Key',
            start_routine=['02 72', self.unlock_key],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_011(self, name='Transition to Default Diagnostic Session'):
        prompt = input('Require restart? [y,n]')
        if prompt.lower() == 'y':
            test.restart_communication()

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )

    def test_015(self, name='Transition to Extended Diagnostic Session'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )

    def test_016(self, name='Activate TesterPresent'):

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

    def test_017(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_018(self, name='Start Routine Provision Security Peripheral All Keys in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[
                self.RID, 
                '01000000000000000000000000000000441BAFA3B95A64DF9B40B8FD17A47433E1300E1706220E7B5CDC2F405CC16733335A64164E981A4D32A1349F845795E0BB'
            ],

            expected={
                'response'   : 'Negative',
                'data'       : '33'
            }
        )

    def test_019(self, name='Transition to Default Diagnostic Session'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )
