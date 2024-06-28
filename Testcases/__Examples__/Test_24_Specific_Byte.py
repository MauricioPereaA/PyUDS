'''
Author: Mauricio Perea
Date: 13 Jul 2020
This script was developed for testing the robustness of feature expected byte_index & expected_byte
'''
from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='0x19'
        )

        self.under_voltage_DTC = 'F0 03 16'


    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        
    def test_001(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('59', '01', '00', '4D'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
        
    def test_002(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('59', '01', '01', '4F'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )


    def test_003(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('59', '01', '79'),
				'byte_index'   : None			# tuple of multiple index
            }
        )
        
        
    def test_004(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('50-55', '01', '00-04', '4F'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
        
     

    def test_005(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': '00',
				'byte_index'   : 3			# Counting from 0, so this is the fourth byte
            }
        )

    def test_006(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': '01',
				'byte_index'   : 3			# Counting from 0, so this is the fourth byte
            }
        )
        
    def test_007(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': '55-60',
				'byte_index'   : 0			# Counting from 0, so this is the fourth byte
            }
        )
        
    def test_008(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('50-59', '01', '00-04', '50-4F'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
        
    def test_009(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('50-59', '01', '00-04', '53-4F'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
        
    def test_010(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('50-59', '01', '00-04', '4F-53'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
    
    def test_011(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': ('50-59', '01', '00-04', '4F-50'),
				'byte_index'   : (0, 1, 3, 5)
            }
        )
    