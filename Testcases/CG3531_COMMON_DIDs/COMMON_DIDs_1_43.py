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
    *Power Mode OFF for test 10
    *Access Security Request Seed 'dataLength':31 instead of None
    *MSM/PTM/ARB/TCP skip tests 7,8
    *MSM/PTM/ARB skip tests 10 through 18
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
    @test DID $F186 Active Diagnostic Session Data Identifier
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
        self.DID = 'F186'
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

    def test_002(self, name='Read Active Diagnostic Session Data Identifier'):

        test.preconditions(

            step_info=info(),
            mec_zero=True,
            sbat=False,

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

    def test_003(self, name='Transition to extendedSession, Application Mode'):

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

    def test_004(self, name='Activate TesterPresent'):

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

    def test_005(self, name='Read Active Diagnostic Session Data Identifier'):

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

    """
    STEP 6: Create valid preconditions for which the
            criteria for safetySystemDiagnosticSession are met,
            e.g. Power mode is RUN, Vehicle Speed is 0 and Engine Run is InActive
    """

    def test_007(self, name='Transition to safetySession, Application Mode'):
        if (
                device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB' or device_under_test == 'TCP'):
            raise Warning('Not a Pyrotechnic ECU. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            safety_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_008(self, name='Read Active Diagnostic Session Data Identifier'):
        if (
                device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB' or device_under_test == 'TCP'):
            raise Warning('Not a Pyrotechnic ECU. Test step will skip.')
            pass

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

    def test_009(self, name='Transition to defaultSession, Application Mode'):

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

    def test_010(self, name='Transition to extendedSession, Application Mode'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

        test.preconditions(

            step_info=info(),
            power_mode='OFF'

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

    def test_011(self, name='Activate TesterPresent'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

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

    def test_012(self, name='Disable DTCs'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

        test.preconditions(

            step_info=info(),
            functionalAddr=True,

        )

        test.step(
            step_title=name,
            dtc_settings='off',

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_013(self, name='Disable Normal Communication'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

        test.preconditions(

            step_info=info(),
            functionalAddr=True,

        )

        test.step(
            step_title=name,
            communication_control=False,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_014(self, name='Access Security Request Seed'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

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

    def test_015(self, name='Access Security Send Key'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

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

    def test_016(self, name='Transition to programmingSession, Installer'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_017(self, name='Read Active Diagnostic Session Data Identifier'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

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

    def test_018(self, name='Transition to defaultSession, Application Mode'):
        if (device_under_test == 'MSM' or device_under_test == 'PTM' or device_under_test == 'ARB'):
            raise Warning('ECU does not support GB6005. Test step will skip.')
            pass

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
