
            # This is and autogenerated test case using PyUDS Test Builder v0.3 #
#Modified by: Mauricio Perea        Date: 30-Sep-20

from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x27'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='<Transition Server to extendedSession> -- Sec Lvl 01 TC'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_002(self, name='<Activate TesterPresent> -- Sec Lvl 01 TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_004(self, name='request Seed - Sec Lvl 01'):
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

    def test_005(self, name='send Key - Sec Lvl 01'):
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

    def test_006(self, name='<Verify Server is unlocked for Security Level 01>'):
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

    def test_007(self, name='<Transition Server to extendedSession> -- Sec Lvl 03 TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_008(self, name='<Activate TesterPresent> -- Sec Lvl 03 TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_010(self, name='request Seed - Sec Lvl 03'):
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

    def test_011(self, name='send Key - Sec Lvl 03'):
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

    def test_012(self, name='<Verify Server is unlocked for Security Level 03>'):
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

    def test_013(self, name='<Transition Server to extendedSession> -- Sec Lvl 09 TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_014(self, name='<Activate TesterPresent> -- Sec Lvl 09 TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_016(self, name='request Seed - Sec Lvl 09'):
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

    def test_017(self, name='send Key - Sec Lvl 09'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='09',
            expected={
                'response': 'Positive'
            }
        )

    def test_018(self, name='<Verify Server is unlocked for Security Level 09>'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'MSM':
            test.step(
                step_title=name,
                custom='31 01 02 3A',
                expected={
                    'response': 'Positive'
                }
            )
        if device_under_test in ['ARB', 'PTM', 'SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Positive'
                }
            )

    def test_019(self, name='<Transition Server to extendedSession> -- Sec Lvl 0B TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_020(self, name='<Activate TesterPresent> -- Sec Lvl 0B TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_022(self, name='request Seed - Sec Lvl 0B'):
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

    def test_023(self, name='send Key - Sec Lvl 0B'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='0B',
            expected={
                'response': 'Positive'
            }
        )

    def test_024(self, name='<Verify Server is unlocked for Security Level 0B>'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'MSM':
            test.step(
                step_title=name,
                custom='31 01 02 3A',
                expected={
                    'response': 'Positive'
                }
            )
        if device_under_test in ['ARB', 'PTM', 'SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Positive'
                }
            )

    def test_025(self, name='<Transition Server to extendedSession> -- Sec Lvl 0D TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_026(self, name='<Activate TesterPresent> -- Sec Lvl 0D TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_028(self, name='request Seed - Sec Lvl 0D'):
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

    def test_029(self, name='send Key - Sec Lvl 0D'):
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

    def test_030(self, name='<Verify Server is unlocked for Security Level 0D>'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'MSM':
            test.step(
                step_title=name,
                custom='31 01 02 3A',
                expected={
                    'response': 'Positive'
                }
            )
        if device_under_test in ['ARB', 'PTM', 'SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Positive'
                }
            )

    def test_031(self, name='<Transition Server to extendedSession> -- Sec Lvl 11 TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_032(self, name='<Activate TesterPresent> -- Sec Lvl 11 TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_034(self, name='request Seed - Sec Lvl 11'):
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

    def test_035(self, name='send Key - Sec Lvl 11'):
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

    def test_036(self, name='<Verify Server is unlocked for Security Level 11>'):
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

    def test_037(self, name='pyrotechnic ECU Test'):
        print('%s is not a Pyrotechnic ECU'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_038(self, name='pyrotechnic ECU Test'):
        print('%s is not a Pyrotechnic ECU'%device_under_test)
        return 0
        ## THIS IS A PLACE HOLDER TEST STEP ##
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_040(self, name='pyrotechnic ECU Test'):
        print('%s is not a Pyrotechnic ECU'%device_under_test)
        return 0
        ## THIS IS A PLACE HOLDER TEST STEP ##

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_041(self, name='pyrotechnic ECU Test'):
        print('%s is not a Pyrotechnic ECU'%device_under_test)
        return 0
        ## THIS IS A PLACE HOLDER TEST STEP ##
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_042(self, name='pyrotechnic ECU Test'):
        print('%s is not a Pyrotechnic ECU'%device_under_test)
        return 0
        ## THIS IS A PLACE HOLDER TEST STEP ##
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_043(self, name='<Transition Server to extendedSession> -- Sec Lvl 11 TC'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_044(self, name='<Activate TesterPresent> -- Sec Lvl 11 TC'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )