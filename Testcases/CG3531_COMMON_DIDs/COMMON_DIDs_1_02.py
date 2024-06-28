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
    *Deleted redundant Read steps before Verify steps
    *functionalAddr=True for test 6
    *sbat=False
    
Changes for v. 2022 from uif01834 (Abraham Estrada):
    * Test steps starting from 004
    * Write ECU Key receives negative response
"""
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random, time
import misc as tools

test = TestCase()

class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F080 ECU Key Provision State Flag
    *****************************************************************************
    '''
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,          # Write on CG Report
            excel_tab=' Corp Common DIDs',
            step_delay=2.5
        )

        ''' DID to be tested '''
        self.DID = 'F080'
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
    
    def test_004(self, name='Read ECU Key Provision State Flag'):

        test.preconditions(
            
            step_info=info(),
            mec_zero=True, 
            sbat=False,         # SBAT in 00s
                        
        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            
            expected={
                'response'   : 'Positive',
                'data'       :  None,
                'dataLength' :  self.dataLength
            }
    
        )

        
    def test_005(self, name='Write ECU Key Provision State Flag'):

        test.preconditions(
            step_info=info()
        )
        time.sleep(2.5)
        test.step(
            step_title=name,
            write_data_ID=[self.DID, '00' * self.max_dataLength],

            
            expected={
                'response'   : 'Negative',
                'data'       :  '31',
                'dataLength':  None
            }
    
        )
    