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
''' Chagnges realized by Mauricio Perea
High Level CG 3531 2019 Complete all test steps
18 February 2020 '''
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random
import misc as tools

test = TestCase()


class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F190 Vehicle Identification Number
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
        self.DID = 'F190'
        DID_Length = tools.readJSON(
            os.getcwd() + r'\\Testcases\CG3531_COMMON_DIDs\\did_lengths.json'
        )
        self.max_dataLength = self.max_dataLength = self.dataLength = DID_Length[__name__]

        if isinstance(DID_Length[__name__], list):
            self.max_dataLength = self.dataLength[-1]
        if isinstance(DID_Length[__name__], list):
            self.max_dataLength = self.dataLength[-1]

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    # def tes_001 is a Precondition

    def test_002(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info(),
            mec_zero=True

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

    def test_003(self, name='Write Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, '00' * self.max_dataLength],

            expected={
                'response': 'Negative',
                'data': '31',
                'dataLength': None
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
            functionalAddr=True

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

    def test_006(self, name='Read Vehicle Identification Number'):

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

    def test_007(self, name='Write Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            write_data_ID=[self.DID, '00' * self.max_dataLength],

            expected={
                'response': 'Negative',
                'data': '33',
                'dataLength': None
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
            send_key='01',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_010(self, name='Read Vehicle Identification Number'):

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

    def test_011(self, name='Write Vehicle Identification Number'):

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

    def test_012(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '00' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )

    def test_013(self, name='Transition to extendedSession, Application Mode'):

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

    def test_014(self, name='Access Security Request Seed'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='03',

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
            send_key='03',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_016(self, name='Read Vehicle Identification Number'):

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

    def test_017(self, name='Write Vehicle Identification Number'):

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

    def test_018(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '01' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )

    def test_019(self, name='Transition to extendedSession, Application Mode'):

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

    def test_020(self, name='Access Security Request Seed'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='05',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_021(self, name='Access Security Send Key'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key='05',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_022(self, name='Read Vehicle Identification Number'):

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

    def test_023(self, name='Write Vehicle Identification Number'):

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

    def test_024(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '00' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )

    def test_025(self, name='Transition to extendedSession, Application Mode'):

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

    def test_026(self, name='Access Security Request Seed'):

        test.preconditions(

            step_info=info(),
            power_mode='OFF'

        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_027(self, name='Access Security Send Key'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key='11',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_028(self, name='Read Vehicle Identification Number'):

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

    def test_029(self, name='Write Vehicle Identification Number'):

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

    def test_030(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '01' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )

    def test_031(self, name='Transition to extendedSession, Application Mode'):

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

    def test_032(self, name='Access Security Request Seed'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_033(self, name='Access Security Send Key'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key='13',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_034(self, name='Read Vehicle Identification Number'):

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

    def test_035(self, name='Write Vehicle Identification Number'):

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

    def test_036(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '00' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )

    def test_037(self, name='Transition to extendedSession, Application Mode'):

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

    def test_038(self, name='Access Security Request Seed'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_039(self, name='Access Security Send Key'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key='15',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_040(self, name='Read Vehicle Identification Number'):

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

    def test_041(self, name='Write Vehicle Identification Number'):

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

    def test_042(self, name='Read Vehicle Identification Number'):

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=self.DID,

            expected={
                'response': 'Positive',
                'data': '01' * self.max_dataLength,
                'dataLength': self.dataLength
            }

        )
