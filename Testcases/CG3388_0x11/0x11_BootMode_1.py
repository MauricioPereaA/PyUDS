
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        if device_under_test is 'MSM':
            tools.popup.warning(
                title=__name__,
                description='MSM does not support Service 0x11'
            )
            raise Warning(__name__, 'MSM does not support Service 0x11')
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x11'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_002(self, name='1 (Service Not Supported in Boot) - physicalAddress'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='BootMode_Precondition')
        test.step(
            step_title='BootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        
        test.step(
            step_title = 'Boot_Mode',
            custom = '10 02'
        )
        # End -- Boot Mode preconditions
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='11 01',
            expected={
                'response': 'Negative',
                'data'    : '11'
            }
        )

