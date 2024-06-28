
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest

test = TestCase()

class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x37'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        

    def test_001(self, name='Transition Server to the defaultSession'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        ) 
    def test_002(self, name='Service not supported in App -- NRC 0x11'):
        test.preconditions(
            step_info=info()
            )

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response': 'Negative',
                'data': '11'
            }
        )
        
    