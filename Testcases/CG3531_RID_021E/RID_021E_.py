'''

     ** Test Template ** 

'''
''' Changes realized by Mauricio Perea
High Level CG 3531 2019 Complete all test steps
19 February 2020 '''
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest,time

test = TestCase()

class RID_021E(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='RID 021E',   # Specify CG Excel Tab
            step_delay=1
        )      

        ''' RID to be tested '''
        self.RID = '02 1E'
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_004(self, name='Transition to extendedSession, Application Mode'):
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
            functionalAddr=False,
            mec_zero=True, 
            sbat=False,         # SBAT in 00s
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

    def test_005(self, name='Activate TesterPresent'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response'   : 'No response'
            }

        )

    def test_006(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_007(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
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
            request_seed='01',

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
            send_key='01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_010(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_011(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )


    def test_012(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )
    def test_013(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )

    def test_014(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response'   : 'No response'
            }

        )

    def test_015(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response'   : 'Positive',
                # Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_016(self, name='Access Security Send Key'):
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

    def test_017(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )
        
    def test_019(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            power_mode='off'
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_020(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_021(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_022(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_023(self, name='Access Security Request Seed'):

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

    def test_024(self, name='Access Security Send Key'):

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

    def test_025(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_026(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_027(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_028(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_029(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_030(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response'   : 'Positive',
                #Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_031(self, name='Access Security Send Key'):

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

    def test_032(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )
        
    def test_034(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            power_mode='off',
            functionalAddr=False,
            signal=[
                'BSPMP_RmtProgmActvAuth', 'BkupSysPwrMode_Prtctd_PDU', 1
            ]
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_035(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_036(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_037(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_038(self, name='Access Security Request Seed'):

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

    def test_039(self, name='Access Security Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='05',

            expected={
                'response'   : 'Positive'
            }
        )
        time.sleep(2.5)
    def test_040(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_041(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_042(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' :  4
            }

        )

    def test_043(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_044(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_045(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response'   : 'Positive',
                # Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_046(self, name='Access Security Send Key'):

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

    def test_047(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            signal=['BSPMP_RmtProgmActvAuth', 'BkupSysPwrMode_Prtctd_PDU', 0]
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )
    
    def test_050(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            power_mode='RUN'
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            },

        )

    def test_051(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_052(self, name='Access Security Request Seed'):

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

    def test_053(self, name='Access Security Send Key'):

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

    def test_054(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Negative',
                'data'       : '22'
            }
        )
        
        
    def test_056(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            mec_zero=True, 
            sbat=False,         # SBAT in 00s
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

    def test_057(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_058(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_059(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_060(self, name='Access Security Request Seed'):

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

    def test_061(self, name='Access Security Send Key'):

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

    def test_062(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_063(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_064(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_065(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_066(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_067(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response'   : 'Positive',
                # Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_068(self, name='Access Security Send Key - 12 byte ANY Key'):

        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )

        test.step(
            step_title=name,
            custom='27 12'+'FF'*12,

            expected={
                'response'   : 'Negative',
                'data'       : '35'
            }
        )
    
    def test_070(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
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

    def test_071(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_072(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_073(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_074(self, name='Access Security Request Seed'):

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

    def test_075(self, name='Access Security Send Key'):

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

    def test_076(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_077(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_078(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_079(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_080(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_081(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response'   : 'Positive',
                # Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_082(self, name='Access Security Send Key - 12 byte ANY Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='27 14'+'FF'*12,

            expected={
                'response'   : 'Negative',
                'data'       : '35'
            }
        )

    def test_083(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            signal=[
                'BSPMP_RmtProgmActvAuth', 'BkupSysPwrMode_Prtctd_PDU', 1
            ]
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )
        
    def test_085(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info(),
            power_mode='off',
            signal=[
                'BSPMP_RmtProgmActvAuth', 'BkupSysPwrMode_Prtctd_PDU', 1
            ]
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_086(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_087(self, name='Disable DTCs'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_088(self, name='Disable Normal Communication'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_089(self, name='Access Security Request Seed'):

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

    def test_090(self, name='Access Security Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='05',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_091(self, name='Start Routine Diagnostic Initiate Extended Reflash'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            start_routine=[self.RID],

            expected={
                'response'   : 'Positive'
            }
        )

    def test_092(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_093(self, name='Transition to defaultSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_094(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_095(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True
            
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            
            expected={
                'response'   : 'No response'
            }


        )

    def test_096(self, name='Access Security Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response'   : 'Positive',
                # Expected to find 15 bytes of FFs
                'partialData': 'FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF',
                'dataLength' : 31
            }
        )

    def test_097(self, name='Access Security Send Key - 12 byte ANY Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='27 16 ' + 'FF'*12,

            expected={
                'response'   : 'Negative',
                'data'       : '35'
            }
        )



if __name__ == '__main__':
    unittest.main()