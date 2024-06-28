
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
"""
Changes for v.2019 from uic13313 (Gad, Yasmin):
    *Test case naming +1 (started from 001)
    *Import for device_under_test
    *sbat=False
    *functionalAddr=True for Activate TesterPresent, Disable DTCs, Disable Normal Communication
    *CG has different DID. Original: F1DF. Current: F1E4.
    *MSM skips entire test case.
    *Power Mode OFF for test 3
    *Additional tests 6 through 12 to match CG.
    *Access Security Request Seed 'dataLength':31 instead of None
    *MSM/PTM/ARB skip tests 6 through 12 (Edit: MSM/PTM/ARB skip entire test.)
"""
from Testcases.TestClass import TestCase
from inspect import stack as info
from framework.shared_functions import device_under_test
import unittest, os, random
import misc as tools

test = TestCase()


class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F1E4 Remote Reflash Programming Status
    *****************************************************************************
    '''
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            pass
            
        test.begin(
            test_info=info(),
            writeTestResults=True,          # Write on CG Report
            excel_tab=' Corp Common DIDs'
        )      

        ''' DID to be tested '''
        self.DID = 'F1E4'
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
    
    def test_002(self, name='Read Remote Reflash Programming Status'):

        test.preconditions(
            
            step_info=info(),
			mec_zero=True,
            sbat=False,
                        
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

        
    def test_003(self, name='Transition to extendedSession, Application Mode'):

        test.preconditions(
            
            step_info=info(),
            power_mode='OFF'            
                        
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

        
    def test_004(self, name='Activate TesterPresent'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True,            
                        
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

        
    def test_005(self, name='Read Remote Reflash Programming Status'):

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

    def test_006(self, name='Disable DTCs'):
            
        test.preconditions(
            
            step_info=info(),
            functionalAddr=True,             
                        
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

        
    def test_007(self, name='Disable Normal Communication'):

        test.preconditions(
            
            step_info=info(),
            functionalAddr=True,            
                        
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

        
    def test_009(self, name='Security Access Send Key'):
            
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

        
    def test_010(self, name='Transition to programmingSession, Installer'):
            
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
        
    def test_011(self, name='Read Remote Reflash Programming Status'):
          
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

    def test_012(self, name='Transition to defaultSession, Application Mode'):
    
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