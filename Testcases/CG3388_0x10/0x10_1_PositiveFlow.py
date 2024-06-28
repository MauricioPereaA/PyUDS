'''
Author: Ricardo Montes

Modified by: Ricardo Montes       Date: 17-Jun-20
Modified by: Mauricio Perea        Date: 30-Sep-20
This script is intended to validate positive response of service 0x10 which main function is enable different diagnostic sessions in the server for the ECU 

The DiagnosticSessionControl service is used to enable different diagnostic sessions
in the server(s).

The test procedures described in this worksheet have been written against the requirements
defined in GB6000 Unified Diagnostic Services Specification as well as ISO 14229-1 and is
written for component level testing. All test procedures require the Server to have a valid
Application SW and Calibrations to run the Server's sessions in Application Mode
and Boot Mode.

With every executed test run the following information needs to be provided (for every ECU
within the tested network topology) besides the actual test results.

'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()

class Service_0x10(unittest.TestCase):

    ''' Positive Flow Diagnostic Session Control Session and Security Tests '''
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x10'
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()


# Physical Messaging

 # 0x10 - default Session
    def test_003(self, name='defaultSession in defaultSession'):
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
            sbat=False, # Clear SBAT
            mec_zero=True
        )

        test.step(
            step_title=name,
            default_session_control=True, # Servicio 10

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }

        )

    def test_004(self, name='extendedSession in defaultSession'):

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

    def test_005(self, name='defaultSession in extendedSession'):

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

  # defaultSession - Security Level 01
    def test_006(self, name='extendedSession in defaultSession'):

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

    def test_007(self, name='Activate TesterPresent'):

        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )

        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response'   : 'No response'
            }
        )

    def test_008(self, name='Security Access - Request seed'):

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

    def test_009(self, name='Security Access - Send key'):

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

    def test_010(self, name='defaultSession - Security Level 01'):

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

    def test_011(self, name='Transition to extendedSession'):

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

    def test_012(self, name='Security Access - Request seed'):

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

    def test_013(self, name='Security Access - Send key'):

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

    def test_014(self, name='defaultSession - Security Level 03'):

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

    def test_015(self, name='Transition to extendedSession'):

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

    def test_016(self, name='Security Access - Request seed'):

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

    def test_017(self, name='Security Access - Send key'):

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

  # defaultSession - Security Level 0B
    def test_018(self, name='defaultSession - Security Level 05'):

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

    def test_019(self, name='Transition to extendedSession'):

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

    def test_020(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='09',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_021(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='09',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_022(self, name='defaultSession - Security Level 09'):

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

    def test_023(self, name='Transition to extendedSession'):

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

    def test_024(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0B',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_025(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0B',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_026(self, name='defaultSession - Security Level 0B'):

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

    def test_027(self, name='Transition to extendedSession'):

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

    def test_028(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0D',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_029(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0D',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_030(self, name='defaultSession - Security Level 0D'):

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

    def test_031(self, name='Transition to extendedSession'):

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

    def test_032(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_033(self, name='Security Access - Send key'):

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

    def test_034(self, name='defaultSession - Security Level 11'):

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

    def test_035(self, name='Transition to extendedSession'):

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

    def test_036(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_037(self, name='Security Access - Send key'):

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

    def test_038(self, name='defaultSession - Security Level 13'):

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

    def test_039(self, name='Transition to extendedSession'):

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

    def test_040(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_041(self, name='Security Access - Send key'):

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

    def test_042(self, name='defaultSession Security Level 15'):

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

    def test_043(self, name='Transition to extendedSession'):

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

    def test_044(self, name='extendedSession in extendedSession'):

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

    def test_045(self, name='Security Access - Request seed'):

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

    def test_046(self, name='Security Access - Send key'):

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

    def test_047(self, name='extendedSession - Security Level 01'):

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

  # Security Level 03
    def test_048(self, name='Security Access - Request seed'):

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

    def test_049(self, name='Security Access - Send key'):

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

    def test_050(self, name='ExtendedSession - Security Level 03'):

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


  # Security Level 05
    def test_051(self, name='Security Access - Request seed'):

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

    def test_052(self, name='Security Access - Send key'):

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

    def test_053(self, name='extendedSession - Security Level 05'):

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

  # Security Level 09
    def test_054(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='09',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_055(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='09',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_056(self, name='extendedSession - Security Level 09'):

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


  # Security Level 0B
    def test_057(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0B',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_058(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0B',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_059(self, name='extendedSession - Security Level 0B'):

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


  # Security Level 0D
    def test_060(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0D',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_061(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0D',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_062(self, name='extendedSession - Security Level 0D'):

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

  # Security Level 11
    def test_063(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='11',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_064(self, name='Security Access - Send key'):

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

    def test_065(self, name='extendedSession - Security Level 11'):

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

  # Security Level 13
    def test_066(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='13',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_067(self, name='Security Access - Send key'):

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

    def test_068(self, name='extendedSession - Security Level 13'):

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

  # Security Level 15
    def test_069(self, name='Security Access - Request seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='15',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_070(self, name='Security Access - Send key'):

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

    def test_071(self, name='extendedSession'):

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

    def test_072(self, name='defaultSession in extendedSession '):

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


  # NOT APPLICABLE - PENDING TO CREATE STEPS FOR OTHER ECUs

    # SKIP 73 to 81

# Functional Messaging


    def test_082(self, name='defaultSession in defaultSession'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        )

    def test_083(self, name='extendedSession in defaultSession '):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        )

