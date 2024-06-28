
            # This is and autogenerated test case using PyUDS Test Builder v0.3 #
#Modified by: Mauricio Perea        Date: 5-Nov-20
        
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        if device_under_test is 'MSM':
            raise Warning(device_under_test + ' does not support current test: %s'%__name__)
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x31'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        
    def test_227(self, name='<Transition to extendedSession>'):
        test.preconditions(
            step_info=info(),
            mec_zero=True, 
            sbat=False   
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_228(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_230(self, name='<Start Routine> Physical Address Req'):
        # == Create valid conditions ==
        test.preconditions(current_step='create valid conditions')
        test.step(step_title='create valid conditions', extended_session_control=True,
                    request_seed='01', send_key='01')
        # == Create valid conditions ==
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='31 01 02 1E',
            expected={
                'response': 'Positive'
            }
        )

    def test_232(self, name='perform hardReset'):
        if device_under_test is 'MSM':
            print('Test step not supported by %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='11 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_233(self, name='<Verify return to defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Negative',
                'data': '7F'
            }
        )
