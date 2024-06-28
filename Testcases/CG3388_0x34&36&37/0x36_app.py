from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout, ECU_info
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
            excel_tab='0x36'
        )
        self.tester = [ECU_info['name']+'_11_bit', ECU_info['name'], ECU_info['name']+'_2', ECU_info['name']+'_3',
                        ECU_info['name']+'_4', ECU_info['name']+'_5', ECU_info['name']+'_6', ECU_info['name']+'_Functional']
        if (device_under_test == 'MSM'):
            self.rsp = ['14DAFCA8x', '14DAF1A8x', '14DAF2A8x', '14DAF3A8x', '14DAF4A8x', '14DAF5A8x', '14DAF6A8x']
    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        

    def test_001(self, name='Transition Server to the defaultSession'):

        test.preconditions(
            step_info=info(),
            tester_id = self.tester[0]  
            
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  None
            }
        ) 
    def test_002(self, name='Service not supported for Service 36 -- 0x7F'):               
        test.preconditions(
            step_info=info(),
            tester_id = self.tester[0]  
            )                    
        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom = packet,
                expected={
                    'response': 'Negative',
                    'data': '11'
                }
        )         
            break
    