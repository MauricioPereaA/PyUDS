'''
*******************************************************************************
@copyright    Copyright 2022 . All rights reserved.
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

@Author: uif01834 Abraham Estrada
*******************************************************************************'''

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os, random
import misc as tools

test = TestCase()


# Ask for the partition calibration ID

class Test_CorpCommon_DIDs(unittest.TestCase):
    '''
    *****************************************************************************
    @test DID $F246 Device Limits Exceeded For Routine Identifiers
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

        DID_Length = tools.readJSON(
            os.getcwd() + r'\\Testcases\CG3531_COMMON_DIDs\\did_lengths.json'
        )

        self.DIDs_length = DID_Length[__name__]

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_002(self, name='Transition to extendedSession, Application Mode'):
        test.preconditions(

            step_info=info(),
            mec_zero=True,
            sbat=False

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

    def test_003(self, name='Activate TesterPresent'):
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

    def test_004(self, name='Disable DTCs'):
        test.preconditions(

            step_info=info(),
            functionalAddr=True

        )

        test.step(
            step_title=name,
            dtc_settings=False,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_005(self, name='Disable Normal Communication'):
        test.preconditions(

            step_info=info(),
            functionalAddr=True

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

    def test_006(self, name='Access Security Request Seed'):
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

    def test_007(self, name='Access Security Send Key'):
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

    def test_008(self, name='Transition to programmingSession, Boot Mode'):
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

    def test_009(self, name='Erase one Calibration Partition ID'):
        input(
            "WARNING! - Please make sure test has been completed correctly until now before performing Erase one Calibration ID. Then press Enter to continue...")

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            start_routine=['FF 00', '02'],  # Main Processor 1st Calibration Partition

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_010(self, name='Transition to the defaultSession, Boot Mode'):
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

    def test_011(self, name='Read Programmed State Indicator'):
        did = 'F0F0'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'partialData': '01 00',
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_012(self, name='Read Programming Error Code'):
        did = 'F0F1'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_013(self, name='Read Boot Initialization Status'):
        did = 'F0F2'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_014(self, name='Read ECU ID in defaultSession'):
        did = 'F0F3'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_015(self, name='Read Signature Bypass Authorization Ticket'):
        did = 'F0F4'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_016(self, name='Read Boot Info Block Subject Name and ECU Name'):
        did = 'F0F6'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_017(self, name='Read Boot Software Identification Data Identifier'):
        did = 'F180'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_019(self, name='Read Application Software Identification Data Identifier'):
        did = 'F181'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_020(self, name='Read Application Data Identification Data Identifier'):
        did = 'F182'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_021(self, name='Read Diagnostic Address'):
        did = 'F1B0'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_022(self, name='Read GM End Model Part Number'):
        did = 'F1CB'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_023(self, name='Read GM Base Model Part Number'):
        did = 'F1CC'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_024(self, name='Read GM End Model Part Number Alpha Code'):
        did = 'F1DB'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_025(self, name='Read GM Base Model Part Number Alpha Code'):
        did = 'F1DC'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    # Test Steps from test_026 to test_033 are not applicable to ARB project

    def test_34(self, name='Transition Server to the extendedSession, Boot Mode'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            extendeded_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_035(self, name='Read Programmed State Indicator'):
        did = 'F0F0'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'partialData': '01 00',
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_036(self, name='Read Programming Error Code'):
        did = 'F0F1'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_037(self, name='Read Boot Initialization Status'):
        did = 'F0F2'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_038(self, name='Read ECU ID in defaultSession'):
        did = 'F0F3'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_039(self, name='Read Signature Bypass Authorization Ticket'):
        did = 'F0F4'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_040(self, name='Read Boot Info Block Subject Name and ECU Name'):
        did = 'F0F6'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_041(self, name='Read Boot Software Identification Data Identifier'):
        did = 'F180'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_043(self, name='Read Application Software Identification Data Identifier'):
        did = 'F181'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_044(self, name='Read Application Data Identification Data Identifier'):
        did = 'F182'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_045(self, name='Read Diagnostic Address'):
        did = 'F1B0'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_046(self, name='Read GM End Model Part Number'):
        did = 'F1CB'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_047(self, name='Read GM Base Model Part Number'):
        did = 'F1CC'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_048(self, name='Read GM End Model Part Number Alpha Code'):
        did = 'F1DB'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    def test_049(self, name='Read GM Base Model Part Number Alpha Code'):
        did = 'F1DC'

        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            read_data_ID=did,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': self.DIDs_length[did]
            }

        )

    # Following the CG Test Steps, TC from test_050 to test_057 are not applicable to ARB project
