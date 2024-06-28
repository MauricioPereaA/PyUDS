#1 Service not supported in application

from framework.shared_functions import device_under_test
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()


class Request_Download(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,  # Write on CG Report
            excel_tab='0x36'  # Specify CG Excel Tab
        )

        self.DUT = device_under_test

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_002(self, name='serviceNotSupported 0x11'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.step(
            step_title=name,
            custom='36 01 44 00 00 c0 00',

            expected={
                'response': 'Negative',
                'data': '11'
            }
        )
