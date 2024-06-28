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
            excel_tab='0x3E'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_003(self, name='testerPresent defaultSession Physical Messaging'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_005(self, name='testerPresent defaultSession Physical Messaging'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='Access security Lvl 01 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_007(self, name='Access security Lvl 01 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='01',
            expected={
                'response': 'Positive'
            }
        )

    def test_008(self, name='testerPresent extendedSession Security Level 01'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_009(self, name='Access security Lvl 03 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='03',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_010(self, name='Access security Lvl 03 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='03',
            expected={
                'response': 'Positive'
            }
        )

    def test_011(self, name='testerPresent extendedSession Security Level 03'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_012(self, name='Access security Lvl 05 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='05',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_013(self, name='Access security Lvl 05 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='05',
            expected={
                'response': 'Positive'
            }
        )

    def test_014(self, name='testerPresent extendedSession Security Level 05'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_015(self, name='Access security Lvl 09 - request_seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='09',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_016(self, name='Security Access - Send key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='09',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_017(self, name='testerPresent extendedSession Security Level 09'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )


    def test_018(self, name='Access security Lvl 0B - request_seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='0B',

            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_019(self, name='Access security Lvl 0B - send_key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='0B',

            expected={
                'response'   : 'Positive'
            }
        )


    def test_020(self, name='testerPresent extendedSession Security Level 0B'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_021(self, name='Access security Lvl 0D - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='0D',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_022(self, name='Access security Lvl 0D - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='0D',
            expected={
                'response': 'Positive'
            }
        )

    def test_023(self, name='testerPresent extendedSession Security Level 0D'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_024(self, name='Access security Lvl 11 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='11',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_025(self, name='Access security Lvl 11 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='11',
            expected={
                'response': 'Positive'
            }
        )

    def test_026(self, name='testerPresent extendedSession Security Level 11'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_027(self, name='Access security Lvl 13 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='13',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_028(self, name='Access security Lvl 13 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='13',
            expected={
                'response': 'Positive'
            }
        )

    def test_029(self, name='testerPresent extendedSession Security Level 13'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_030(self, name='Access security Lvl 15 - request_seed'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='15',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_031(self, name='Access security Lvl 15 - send_key'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='15',
            expected={
                'response': 'Positive'
            }
        )

    def test_032(self, name='testerPresent extendedSession Security Level 15'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )

    def test_034(self, name='Pyrotechnic ECU Test'):
        pass

    def test_035(self, name='Pyrotechnic ECU Test'):
        pass

    def test_036(self, name='Pyrotechnic ECU Test'):
        pass

    def test_037(self, name='Pyrotechnic ECU Test'):
        pass

    def test_038(self, name='Pyrotechnic ECU Test'):
        pass

    def test_039(self, name='<Transition Server to defaultSession> '):
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

    def test_040(self, name='testerPresent defaultSession Functional Messaging'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='3E 00',
            expected={
                'response': 'Positive'
            }
        )
