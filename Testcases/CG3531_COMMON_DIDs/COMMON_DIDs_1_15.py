
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
    *sbat=False
    *functionalAddr=True for Activate TesterPresent
    
Changes for v.2021 from uif01834 (Abraham Estrada):
    *Adding TC considered for ARB MY24
    *Length bytes was modified for DID F091
"""
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random
import misc as tools

test = TestCase()


class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F091 SOH Platform Status Operation
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
        self.DID = 'F091'
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

    def test_003(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info(),
            mec_zero=True,
            sbat=False,

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Negative',
                'data': '31'
            }

        )
    
    def test_004(self, name='Transition to extendedSession, Application Mode'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_005(self, name='Activate TesterPresent'):
        test.preconditions(

            step_info=info(),
            functionalAddr=True,

        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response': 'No response',
                'data': None,
                'dataLength': None
            }

        )

    def test_007(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Negative',
                'data': '33'
            }

        )

    def test_008(self, name='Access Security Request Seed'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed= '03',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_009(self, name='Access Security Send Key'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key= '03',

            expected={
                'response': 'Positive'
            }
        )

    def test_010(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.dataLength
            }

        )

    def test_011(self, name='Access Security Request Seed'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='09',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_012(self, name='Access Security Send Key'):
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

    def test_013(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.dataLength
            }

        )

    def test_014(self, name='Access Security Request Seed'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='0B',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_015(self, name='Access Security Send Key'):
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

    def test_016(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.dataLength
            }

        )

    def test_017(self, name='Access Security Request Seed'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='0D',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_018(self, name='Access Security Send Key'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key='0D',

            expected={
                'response': 'Positive'
            }
        )

    def test_019(self, name='Read SUM_SOH Platform Reliability Monitor'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.dataLength
            }

        )

    def test_020(self, name='Transition to defaultSession, Application Mode'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    