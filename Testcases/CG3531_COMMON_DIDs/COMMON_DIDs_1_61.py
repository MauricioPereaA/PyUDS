
'''
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    "Corporate Common DIDs
    Corporate Common DIDs are defined and maintained by General Motors. 
    GB6001 contains the requirement to support the infrastructure DIDs. 
    The Diagnostic CTRS (odx) file provides definition for the DIDs (structure 
    and format). Other requirements documents are referenced in the Description 
    when additional information is specified therein.
    "

@note ABBREVIATIONS:
        - uds: Unified Diagnostic Services
*******************************************************************************'''

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random
import misc as tools

test = TestCase()


class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F1E6 Ethernet Bridge Part Number Check
    *****************************************************************************
    '''
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,          # Write on CG Report
            excel_tab=' Corp Common DIDs'
        )      

        ''' DID to be tested '''
        self.DID = 'F1E6'
        DID_Length = tools.readJSON(
            os.getcwd() + r'\\Testcases\CG3531_COMMON_DIDs\\did_lengths.json'
        )
        self.max_dataLength = self.dataLength = DID_Length[__name__]

        if isinstance( DID_Length[__name__], list ):
            self.max_dataLength = self.dataLength[-1]

        
        
           
            
            
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()
    
    def test_001(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info(),
			mec_zero=True                
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
            }
    
        )

        
    def test_002(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_003(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            start_tester_present=True,

            
            expected={
                'response'   : 'No response',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_004(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
            }
    
        )

        
    def test_005(self, name='Disable DTCs'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            dtc_settings='off',

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_006(self, name='Disable Normal Communication'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            communication_control=False,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_007(self, name='Access Security Request Seed'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            request_seed='01',

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
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
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_009(self, name='Transition to programmingSession, Installer'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_010(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
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
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_012(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
            }
    
        )

        
    def test_013(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_014(self, name='Erase Application SW'):
        input("WARNING! - Please make sure test has been completed correctly until now before performing Erase Application SW. Then press Enter to continue...")

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            start_routine=['FF 00', '01'],

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_015(self, name='Transition to defaultSession, Boot Mode'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            default_session_control=True,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_016(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info(),
            reset_communication=True
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
            }
    
        )

        
    def test_017(self, name='Transition to extendedSession, Boot Mode'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  None
            }
    
        )

        
    def test_018(self, name='Read Ethernet Bridge Part Number Check'):

        test.preconditions(
            
            step_info=info()            
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength':  self.dataLength
            }
    
        )

        
    def test_019(self, name='Program Application SW and Calibration Data to successful completion'):

        input("Please reflash your unit and press Enter to finish the test...")

    