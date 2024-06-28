
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
 #Modified by: Mauricio Perea        Date: 30-Sep-20
       
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x10'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_002(self, name='ServiceNotSupported - 0x11'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        test.step(
            step_title=name,
            custom='10 02'
        )
        #add
        test.preconditions(
            step_info=info(),
        )
        if device_under_test in 'ARB':
            print('%s supports Service'%device_under_test)    
            return 0            

        test.step(
            step_title=name,
            custom='10 02',
            expected={
                'response': 'Negative',
                'data'    : '11'
            }
        )

    def test_003(self, name='incorrectMessageLengthOrInvalidFormat - 0x13'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10',
            expected={
                'response': 'Negative',
                'data'    : '13'
            }
        )

    def test_004(self, name='incorrectMessageLengthOrInvalidFormat - 0x13'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 02 00',
            expected={
                'response': 'Negative',
                'data'    : '13'
            }
        )

    def test_005(self, name='subFunctionNotSupported - 0x12'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 00',
            expected={
                'response': 'Negative',
                'data'    : '12'
            }
        )
        
    def test_006(self, name='subFunctionNotSupported - 0x33'):
        test.preconditions(
            step_info=info()
        )
        
        if device_under_test in 'ARB':
            print('%s does not return NRC 0x33'%device_under_test)    
            return 0 
            
        test.step(
            step_title=name,
            custom='10 22',
            expected={
                'response': 'Negative',
                'data'    : '33'
            }
        )        

