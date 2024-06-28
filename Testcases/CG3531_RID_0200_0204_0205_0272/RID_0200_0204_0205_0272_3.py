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
        self.RID = '02 05'
    
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
    
    # Security Level 01
    def test_007(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_008(self, name='Access Security Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_009(self, name='Start Routine Secured ECU Key Provision Data in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive',
                'dataLength' : 99
            }
        )

    def test_009_2(self, name= 'Provide the number of supported payload bytes'):
        #test.preconditions(
        #    step_info=info()
        #)

        #test.step(
        #    step_title=name,

        #   expected={
        #       'response'   : ''
        #   }
        #)
        pass

    def test_010(self, name='Transition to Default Diagnostic Session'):

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

    def test_011(self, name='Transition to Extended Diagnostic Session'):

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

    def test_012(self, name='Activate TesterPresent'):

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

    # Security Level 03
    def test_013(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='03',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_014(self, name='Access Security Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='03',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_015(self, name='Start Routine Secured ECU Key Provision Data in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive',
                'dataLength' : 99
            }
        )

    def test_015_2(self, name= 'Provide the number of supported payload bytes'):
        #test.preconditions(
        #    step_info=info()
        #)

        #test.step(
        #    step_title=name,

        #   expected={
        #       'response'   : ''
        #   }
        #)
        pass

    def test_016(self, name='Transition to Default Diagnostic Session'):

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

    def test_017(self, name='Transition to Extended Diagnostic Session'):

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

    def test_018(self, name='Activate TesterPresent'):

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

    # Security Level 11
    def test_019(self, name='Access Security Request Seed'):

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

    def test_020(self, name='Access Security Send Key'):

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

    def test_021(self, name='Start Routine Secured ECU Key Provision Data in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive',
                'dataLength' : 99
            }
        )

    def test_021_2(self, name= 'Provide the number of supported payload bytes'):
        #test.preconditions(
        #    step_info=info()
        #)

        #test.step(
        #    step_title=name,

        #   expected={
        #       'response'   : ''
        #   }
        #)
        pass

    def test_022(self, name='Transition to Default Diagnostic Session'):

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

    def test_023(self, name='Transition to Extended Diagnostic Session'):

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

    def test_024(self, name='Activate TesterPresent'):

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

    # Security Level 13
    def test_025(self, name='Access Security Request Seed'):

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

    def test_026(self, name='Access Security Send Key'):

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

    def test_027(self, name='Start Routine Secured ECU Key Provision Data in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive',
                'dataLength' : 99
            }
        )

    def test_027_2(self, name= 'Provide the number of supported payload bytes'):
        #test.preconditions(
        #    step_info=info()
        #)

        #test.step(
        #    step_title=name,

        #   expected={
        #       'response'   : ''
        #   }
        #)
        pass

    def test_028(self, name='Transition to Default Diagnostic Session'):

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

    def test_029(self, name='Transition to Extended Diagnostic Session'):

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

    def test_030(self, name='Activate TesterPresent'):

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

    def test_031(self, name='Start Routine Secured ECU Key Provision Data in Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Negative',
                'data'       : '33'
            }
        )
