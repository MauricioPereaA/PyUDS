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
        
    def test_001(self, name='Boot Mode'):
        # Begin -- Boot Mode preconditions
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,

            expected={
                'response'   : 'Positive'
            }
        )
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            request_seed='01',
            send_key='01'
        )
        test.step(
            step_title=name,
            custom='10 02'
        )
        # End -- Boot Mode preconditions 
        test.preconditions(
            step_info=info(),
            )             
        test.step(
            step_title=name,
            custom='31 01 FF 00 01',         
            expected={
                'response': 'Positive',
            }
        )  
        
    def test_002(self, name='Request download'):
        test.preconditions(            
            step_info=info()            
        )            
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 0e 7e 00',

            expected={
                'response'   : 'Positive' #74 20
            }
        ) 
    def test_003(self, name='Continue programming event to successful completion'):
        test.preconditions(            
            step_info=info()            
        )                         
        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
                }
            )
        test.preconditions(            
            step_info=info()            
        )
        # time.sleep(20)  # add by KLQ
        test.step(
            step_title=name,
            custom='37',
            
            expected={
                'response'   : 'Positive',
            }
        )
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_030(self, name='Transition Server to the defaultSession'):

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
    