"""
Develop by Mauricio Perea
Test Case for testeing the function calculate_size_binary
20 October 2020
"""
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time
from framework.tools.misc import calculate_size_binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()


class Comp_Hand(unittest.TestCase):
    ''' Positive Flow Diagnostic Session Control Session and Security Tests '''

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        value=calculate_size_binary(_binary_app)
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='Comp Hand'
        )
        message = value
        print(__name__, message)


    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='defaultSession in defaultSession'):
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