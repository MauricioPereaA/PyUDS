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
Changes for v.2021 from uif01834 (Abraham Estrada):
    *Test case naming (started from 002)
    *sbat=False
"""

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random
import misc as tools

test = TestCase()


class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F1A0 Manufactures Enable Code
    *****************************************************************************
    '''

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,  # Write on CG Report
            excel_tab=' Corp Common DIDs'
        )

        ''' DID to be tested '''
        self.DID = 'F1A0'
        DID_Length = tools.readJSON(
            os.getcwd() + r'\\Testcases\CG3531_COMMON_DIDs\\did_lengths.json'
        )
        self.max_dataLength = self.dataLength = DID_Length[__name__]

        if isinstance(DID_Length[__name__], list):
            self.max_dataLength = self.dataLength[-1]

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_002(self, name='Read Manufactures Enable Code'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False

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

    def test_003(self, name='Write Manufactures Enable Code'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, 'FE' * self.max_dataLength],

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_004(self, name='Read Manufactures Enable Code'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': 'FE' * self.max_dataLength,
                'dataLength': None
            }

        )

    def test_005(self, name='Transition to extendedSession, Application Mode'):
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

    def test_006(self, name='Activate TesterPresent'):
        test.preconditions(

            step_info=info()

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

    def test_007(self, name='Read Manufactures Enable Code'):
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

    def test_008(self, name='Write Manufactures Enable Code'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, 'FD' * self.max_dataLength],

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )


    def test_009(self, name='Verify that the new data (Write request) was correctly written (Read request)'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': 'FD' * self.max_dataLength,
                'dataLength': None
            }

        )
