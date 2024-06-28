
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
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
            excel_tab='0x2E'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='default'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='nrc 0x31 - default'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='2E E0 10 00',
            expected={
                'response': 'No response'
            }
        )

    def test_003(self, name='nrc 0x31 - default2'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='2E F0 87 00 00 00',
            expected={
                'response': 'No response'
            }
        )
    
    def test_004(self, name='nrc 0x31 - default3'):
        pass

    def test_005(self, name='extended'):
        test.preconditions(
            step_info=info()
        )
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        # 
        test.step(
            step_title=name,
            extended_session_control=True,
            custom='2E E0 10 00',
            expected={
                'response': 'No response'
            }
        )

        test.step(
            step_title=name,
            custom='2E F0 87 00 00 00',
            expected={
                'response': 'No response'
            }
        )

        # Pre-condition step
        test.preconditions('Write DID 0xF197 - Preconditions')#F190-->F197
        test.step(step_title='Write DID 0xF197 - Preconditions',#F190-->F197
                 extended_session_control=True)
        #     request_seed='01', send_key='01')     

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='2E F1 97 FF FF FF FF', #F1 99 --> F1 97
            expected={
                'response': 'No response'
            }
        )
