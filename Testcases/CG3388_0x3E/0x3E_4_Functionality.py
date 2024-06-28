            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20

from framework.shared_functions import tools, device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

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
        message = 'This test requires user input to confirm behaviors.'+\
            '\nPlease standby and wait for prompts to popup.'
        print(__name__, message)
        tools.popup.warning(title='User input required',
                                description=message)
        self.s3_timeout = 5 + 0.1 # S3 Time out + 1Ms

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='transition to defaultSession'):
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

    def test_002(self, name='transition to extendedSession'):
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

    def test_004(self, name='<Service supported in the extendedSession but not the defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_006(self, name='<Service supported in the extendedSession but not the defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_007(self, name='<Transmit request 5 times for a period of 2 minutes>'):
        test.preconditions(
            step_info=info()
        )
        for _ in range(5):
            test.step(
                step_title=name,
                custom='28 03 01',
                expected={
                'response': 'Positive'
            }
            )
            tools.timer.input('Wait for', timeout=24)



    def test_008(self, name='Continue requesting the diagnostic service'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_009(self, name='<Stop TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            stop_tester_present=True,
            expected={
                                'response' : 'Positive'
                        }
        )

    def test_010(self, name='<Service supported in the extendedSession but not the defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        #time delay
        tools.timer.input('Wait for', timeout=5)
        #test presenter cannot change in a short time
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Negative',
                'data'       : '7F'
            }
        )

    def test_019(self, name='transition to defaultSession'):
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

    def test_020(self, name='transition to extendedSession'):
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

    def test_022(self, name='<Wait 4 seconds and while the Server is in extendedSession>'):
        #tools.timer.input('Wait for', timeout=4) CG step 22 doesnt make sense if wait 4 seconds then we are out of extended Session
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_023(self, name='<Verify that normal communication message remains disabled for the duration the diagnostic session is kept active>'):
        test.preconditions(
            step_info=info()
        )
        #this step doest make sense since we will timeout from exteded session moving to default and enabling normal communication 
        prompt = tools.popup.ask(title=name, description=name)
        test.compare(True, prompt, step='test_023')

    def test_024(self, name='<Activate TesterPresent>'):
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

    def test_025(self, name='<Service supported in the extendedSession but not the defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_026(self, name='<Verify that normal communication message remains disabled for the duration the diagnostic session is kept active>'):
        test.preconditions(
            step_info=info()
        )
        prompt = tools.popup.ask(title=name, description=name)
        test.compare(True, prompt, step='test_026')

    def test_028(self, name='<hardreset -extendedSession>Preconditionns'):
        if device_under_test is 'MSM':
            print('Test step not supported by %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='11 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_029(self, name='<Verify that normal communication message remains disabled for the duration the diagnostic session is kept active>'):
        test.preconditions(
            step_info=info()
        )
        prompt = tools.popup.ask(title=name, description=name)
        test.compare(True, prompt, step='test_029')