'''
Author: Mauricio Perea

Modified by Mauricio Perea      Date: 17-Jun-20

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
            writeTestResults=False,
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
            transmit_in_off=False,
            sbat=True, # Clear SBAT
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
