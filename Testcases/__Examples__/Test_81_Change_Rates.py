'''
    TestScript intended to perform Unit Testing for pyUDS 0x2A Service
'''
'''
Author: Mauricio Perea

This script is intended to validate Functionality of service 0x2A which main function is to request the periodic transmission of data record values from the server by one or more periodicDataIdentifiers (PDID).


'''
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #

from framework.shared_functions import tools, device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        if device_under_test is 'SCL':
            tools.popup.warning(
                title='Service 0x2A not supported',
                description='SCL does not support service 0x2A'
            )
            raise Warning('SCL does not support service 0x2A')
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='0x2A'
        )

        self.s3_timeout = 0.1

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Transition Server to ExtendedSession'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='Activate tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_003(self, name='DynamicallyDefineDataIdentifier  2C - F0-FF'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FF F0 80 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 FE F0 81 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 FD F0 84 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 FC F0 89 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 FB F0 89 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FA F0 8F 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F9 F0 90 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F8 F0 91 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F7 F0 92 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F6 F0 94 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F5 F0 95 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F4 F0 A7 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F3 F0 84 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F2 F0 AB 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F1 F0 B3 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='2C 01 F2 F0 F0 B4 01 01',
            expected={
                'response': 'Positive'
            }
        )


    # Test failure is expected, it is just to check verification functionality
    def test_004(self, name='Start DDDIDs Mode 02 -Expected Passed'):
        test.preconditions(
            step_info=info()
        )
       

        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID='F4 FF FD F0 F1', rate='02', timeout=3),

            expected={
                'response': 'Positive',
                'periodic_verifications': (
                {'dddid': 'F4', 'rate': '02', 'tolerance': 10.0}, {'dddid': 'FF', 'rate': '02', 'tolerance': 10.0},
                {'dddid': 'FD', 'rate': '02', 'tolerance': 10.0}, {'dddid': 'F0', 'rate': '02', 'tolerance': 10.0},
                {'dddid': 'F1', 'rate': '02', 'tolerance': 10.0})
            }
        )
        
        
        test.step(
            step_title=name,
            stop_periodic_data='F2 FB',

            expected={
                'response': 'Positive',
            }
        )

        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID='FC FE', rate='01', timeout=6),
            expected={
                'response': 'Positive',
                'periodic_verifications': ({'dddid': 'F1', 'rate': '01', 'tolerance': 10.0}, {'dddid': 'F2', 'rate': '01', 'tolerance': 10.0}),
            }
        )

        test.step(
            step_title=name,
            stop_periodic_data='',

            expected={
                'response': 'Positive',
            }
        )
