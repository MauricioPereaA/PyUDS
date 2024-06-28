from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Infrastructure'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    
    def test_001(self, name='Transition to Extended Session'):
        test.preconditions(
            step_info=info()        
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_002(self, name='Request Manufacturing Mode seed security access'):
        test.preconditions(
            step_info=info()         
        )

        test.step(
            step_title=name,
            request_seed='03',
            expected={
                'response': 'Positive'
            }
        )
    
    def test_003(self, name='Send key'):
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

    def test_004(self, name='All conditions satisfied Service 28'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title='Security Level 01',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='01',
            send_key='01',
            expected={
                'response': 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='Stop tester present'):
        test.preconditions(
            step_info=info()       
        )

        test.canoe.set_envVariable(envVNMFStop=1)
        test.canoe.set_envVariable(envVNMFSend=0)
         
        test.step(
            step_title='Stop Tester Present',
            stop_tester_present=True
        )

        time.sleep(30)

        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)

        time.sleep(10)

        test.step(
            step_title='Start Tester Present and send 10 01',
            start_tester_present=True,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_006(self, name='Transition to Extended Session'):
        test.preconditions(
            step_info=info()        
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_007(self, name='Request Manufacturing Mode seed security access'):
        test.preconditions(
            step_info=info()         
        )

        test.step(
            step_title=name,
            request_seed='03',
            expected={
                'response': 'Positive'
            }
        )
    
    def test_008(self, name='Send key'):
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

    def test_009(self, name='Condition 1 not satisfied Service 28'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 0
            ]          
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            custom='28 00 01',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )

    def test_010(self, name='Condition 2 not satisfied Service 28'):
        test.preconditions(
            step_info=info(),
            signal = [
                        'SPMP_SysPwrModeAuth', 'SysPwrMode_Prtctd_PDU', 1
            ]          
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            custom='28 03 01',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )