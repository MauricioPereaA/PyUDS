
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
            excel_tab='0x31'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='<Transition to extendedSession>'):
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

    def test_002(self, name='<Activate TesterPresent>'):
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

    def test_004(self, name='validConditions -- <Start Routine> Physical Address Req'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='31 01 FF 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='<Stop Routine>'):
        if device_under_test in ['SCL', 'MSM', 'ARB', 'TCP']:
            print(name, 'Test not applicable for %s'%device_under_test)
            return 0

        test.preconditions(
            step_info=info(),
        )
        test.step(
            step_title=name,
            custom='31 02 03 41',
            expected={
                'response': 'Positive',
            }
        )

    def test_006(self, name='<Request  Routine Results>'):
        if device_under_test is not 'SCL':
            print(name, 'Test not applicable for %s'%device_under_test)
            return 0
        # Start - RID 03 11 - Preconditions 
        test.preconditions('RID 03 11 - Preconditions')
        test.step(step_title='RID 03 11 - Preconditions',
                    extended_session_control=True,
                    start_tester_present=True,
                    request_seed='01', send_key='01')
        # End   - RID 03 11 - Preconditions 
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='31 03 03 11',

            expected={
                'response': 'Positive'
            }
        )
        # tearDown step
        test.preconditions('teardown - transition to defaultSession')
        test.step(step_title='teardown - defaultSession',
                    default_session_control=True)
        # tearDown step

    def test_007(self, name='Repeat the Diagnostic Functionality Physical Addressing test procedures in defaultSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            default_session_control=True,
            custom='31 01 FF 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_008(self, name='Repeat the Diagnostic Functionality Physical Addressing test procedures in safetySystemDiagnosticSession'):
        pass

    def test_010(self, name='validConditions -- <Start Routine> Functional Address Req'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='31 01 FF 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_011(self, name='<Stop Routine>'):
        if device_under_test in ['SCL', 'MSM', 'ARB', 'TCP']:
            print(name, 'Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            functionalAddr=True              
        )
        test.step(
            step_title=name,
            custom='31 02 03 41',
            expected={
                'response': 'Positive',
            }
        )  

    def test_012(self, name='<Request  Routine Results>'):
        if device_under_test is not 'SCL':
            print(name, 'Test not applicable for %s'%device_under_test)
            return 0
        # Start - RID 03 11 - Preconditions 
        test.preconditions('RID 03 11 - Preconditions')
        test.step(step_title='RID 03 11 - Preconditions',
                    extended_session_control=True,
                    start_tester_present=True,
                    request_seed='01', send_key='01')
        # End   - RID 03 11 - Preconditions 
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='31 03 03 11',

            expected={
                'response': 'Positive'
            }
        )
        # tearDown step
        test.preconditions('teardown - transition to defaultSession')
        test.step(step_title='teardown - defaultSession',
                    default_session_control=True)
        # tearDown step

    def test_013(self, name='Repeat the Diagnostic Functionality Functional Addressing test procedures in defaultSession'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control=True, #no suitable RID for subfuction 0x02
            custom='31 01 FF 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_014(self, name='Repeat the Diagnostic Functionality Physical Addressing test procedures in safetySystemDiagnosticSession'):
        pass
