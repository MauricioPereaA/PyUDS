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
    *Step numbering +1 (started at 001).
    *Step 2: Checks 'data' is same as write data
    *Removed Read steps before Verify steps (redundant)
    *sbat=False
    *functionalAddr=True for Activate TesterPresent
    *Warning for MSM (3,4,8,9), added import for device_under_test
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
    @test DID $F09A Diagnostic DataIdentifier
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
        self.DID = 'F09A'
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

    def test_002(self, name='Read Diagnostic DataIdentifier'):

        test.preconditions(

            step_info=info(),
            mec_zero=True,
            sbat=False,
        )

        test.step(

            step_title=name,
            write_data_ID=[self.DID, '01' * self.max_dataLength],  # Initial value 01
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '01' * self.max_dataLength,  # To-Do: Have a way to check the read data currently on the ECU
                'dataLength': self.dataLength
            }

        )

    def test_003(self, name='Write Diagnostic DataIdentifier'):
        if (device_under_test == 'MSM'):
            raise Warning('Does not apply for ECU. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, '00' * self.max_dataLength],

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_004(self, name='Verify that the new data (Write request) was correctly written (Read request)'):
        if (device_under_test == 'MSM'):
            raise Warning('Does not apply for ECU. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '00' * self.max_dataLength,
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

    def test_007(self, name='Read Diagnostic DataIdentifier'):

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

    def test_008(self, name='Write Diagnostic DataIdentifier'):
        if (device_under_test == 'MSM'):
            raise Warning('Does not apply for ECU. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, '01' * self.max_dataLength],

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_009(self, name='Verify that the new data (Write request) was correctly written (Read request)'):
        if (device_under_test == 'MSM'):
            raise Warning('Does not apply for ECU. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '01' * self.max_dataLength,
                'dataLength': None
            }

        )
