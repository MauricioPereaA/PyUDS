from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x34'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        

    def test_001(self, name='Transition Server to the defaultSession'):

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
    def test_002(self, name='Service not supported for Service 34 -- 0x7F'):               
        test.preconditions(
            step_info=info(),
            )          
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 0e 7e 00',
            expected={
                'response': 'Negative',
                'data': '7F'
            }
        )         
        
    