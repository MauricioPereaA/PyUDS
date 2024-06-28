from framework.shared_functions import device_under_test  
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, random

test = TestCase()

class PyUDS_TestCase(unittest.TestCase):

    ''' Positive Flow Diagnostic Session Control Session and Security Tests '''
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='NRC 78 & P2 Timing'
        )      
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='NRC 78 in boot mode'):
#    Edit by YCC
#         test.preconditions(
#             step_info=info()
#         )
# 
#         test.step(
#             step_title=name,
#             extended_session_control= True,
#             start_tester_present= True,
#             dtc_settings = False,
#             custom = '28 03 F1',
#             request_seed = '01',
#             send_key = '01',
#             programming_session_control = True,
# 
#             expected={
#                 'response'   : 'Positive'
#             }
#         )

        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            extended_session_control=True,
            start_tester_present= True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01',
            programming_session_control = True
        )
        # End -- Boot Mode preconditions

        test.step(
            step_title=name,
            custom = '22 F0 F8',
            expected={
                'response': 'Negative',
                'data': '78'
            }
        )
    # Purpose of test 002 only to fill CG report
    def test_002(self, name='Attach log '):
        test.preconditions(            
            step_info=info()            
        )
        test.compare(True, True, step='test_002')
        test.restart_communication()