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
            excel_tab='0x10'
        )
        self.unsecured_DID = {
            'PTM': '4B 61',
            'ARB': 'F0 80',
            'MSM': 'F0 80',
            'SCL': 'F0 80',
            'TCP': 'F1 A0'
        }


    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Transition to defaultSession'):
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

    def test_003(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_004(self, name='Access security Lvl 01 - request_seed'):
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

    def test_005(self, name='transition to extendedSession'):
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

    def test_006(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_007(self, name='Access security Lvl 01 - request_seed-Repeat 5 times for a period of 2 minutes'):
        test.preconditions(
            step_info=info()
        )
        for _ in range(5):
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
            tools.timer.input('Repeating request in: ', timeout=24)

    def test_016(self, name='transition to extendedSession'):
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

    def test_017(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_018(self, name='Unlock the Server via SecurityAccess 27 01/27 02'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            send_key='01',
            expected={
                'response': 'Positive'
            }
        )

    def test_021(self, name='<Activate ReadDataByIdentifier> '): # No DID supported for this Test
        pass

    def test_022(self, name='<Activate ReadDataByIdentifier> '): # Unsecured DID
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+ self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )

    def test_035(self, name='Stop periodically transmitted TesterPresent'):
        test.preconditions(
            step_info=info(),

        )
        test.step(
            step_title=name,
            stop_tester_present= True,
            expected={
                'response' : 'Positive'
            }
        )
        tools.timer.input('Wait for S3 timeout', timeout=6)

    def test_036(self, name='Verify Server has transitioned to defaultSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Negative',
                'data' : '7F'
            }
        )

    def test_037(self, name='<Activate ReadDataByIdentifier> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '31'
            }
        )
    def test_040(self, name='<Activate ReadDataByIdentifier> '): # No DID supported for this Test
        pass

    def test_041(self, name='Activate ReadDataByIdentifier'): # Unsecured DID
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )


    def test_061(self, name='Transition to defaultSession'):
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

    def test_062(self, name='Security Enabled'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '31'
            }
        )

    def test_063(self, name='Activate ReadDataByIdentifier'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22'+self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )

    def test_068(self, name='Transition to defaultSession'):
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


    def test_070(self, name='Security Enabled'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '31'
            }
        )

    def test_071(self, name='Activate ReadDataByIdentifier'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22'+self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )


    def test_106(self, name='Transition Server to a extendedSession'):
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

    def test_107(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_108(self, name='Unlock the Server via SecurityAccess 27 01/27 02'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            send_key='01',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_111(self, name='<Activate ReadDataByIdentifier> '): # No DID supported for this Test
        pass

    def test_112(self, name='<Activate ReadDataByIdentifier> '): # Unsecured DID
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+ self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )


    def test_125(self, name='transition to extendedSession'):
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

    def test_126(self, name='<Activate TesterPresent>'):
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

    def test_127(self, name='<Security Enabled>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '33'        #31-->33
            }
        )

    def test_130(self, name='Activate ReadDataByIdentifier'): # No DID supported
        pass

    def test_131(self, name='<Activate ReadDataByIdentifier> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )


    def test_152(self, name='transition to extendedSession'):
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

    def test_153_1(self, name='<Activate TesterPresent-DefaultSession>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_153_2(self, name='<Unlock the Server via SecurityAccess 27 01/27 02'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            send_key='01',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_156(self, name='Activate ReadDataByIdentifier'): # No DID supported
        pass

    def test_157(self, name='Activate ReadDataByIdentifie'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+ self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )

    def test_170(self, name='Transition to defaultSession'):
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

    def test_171(self, name='Verify Server has transitioned to defaultSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='27 01',
            expected={
                'response': 'Negative',
                'data' : '7F'
            }
        )

    def test_172(self, name='Security Enabled'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '31'
            }
        )

    def test_175(self, name='Activate ReadDataByIdentifier'): # No DID supported
        pass

    def test_176(self, name='<Activate ReadDataByIdentifier> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 '+self.unsecured_DID[device_under_test],
            expected={
                'response': 'Positive'
            }
        )

    def test_189(self, name='Transition Server to a extendedSession'):
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

    def test_190(self, name='<Activate TesterPresent-DefaultSession>'):
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

    def test_192(self, name='Unlock the Server via SecurityAccess 27 01/27 02'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='01',
            send_key='01',
            expected={
                'response': 'Positive'
            }
        )

    def test_193(self, name='Configure ResponseOnEvent'):  # Response on Event Test
        pass



    def test_194(self, name='Clear DTCs'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='14 FF FF FF',
        )

        test.step(
            step_title=name,
            custom='85 02',
            expected={
                'response': 'Positive'
            }
        )

    def test_195(self, name='Disable Normal Comm via CommunicationControl'):
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

    def test_220(self, name='ECUReset'):
        if device_under_test is 'MSM':
            print(__name__, '::', name, 'No supported by %s'%device_under_test)
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
        tools.timer.input('Verifying successful transition to defaultSession', timeout=5)

    def test_221(self, name='Verify Server has transitioned to defaultSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='27 01',
            expected={
                'response': 'Negative',
                'data'    : '7F'
            }
        )

    def test_222(self, name='<Security Enabled>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E F1 90'+'00'*17,
            expected={
                'response': 'Negative',
                'data'    : '31'
            }
        )

    def test_223(self, name='Verify Service 86, ResponseOnEvent is stopped'): # Response on Event Test
        pass

    def test_224(self, name='Verify Service 85, ControlDTCSetting is re-enabled'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive'
            }
        )

    def test_225(self, name='Verify Service 28, CommunicationControl is re-enabled'):
        com_enabled = tools.popup.ask(
            title=name,
            description=name,
            timeout=15, default = False )
        test.compare(True, com_enabled, step ='test_225')


    def test_231(self, name='pyrotechnic ECU Test'):
        print('Pyrotechnic ECU Test not applicable for %s'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_232(self, name='pyrotechnic ECU Test'):
        print('Pyrotechnic ECU Test not applicable for %s'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_234(self, name='pyrotechnic ECU Test'):
        print('Pyrotechnic ECU Test not applicable for %s'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_235(self, name='pyrotechnic ECU Test'):
        print('Pyrotechnic ECU Test not applicable for %s'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )

    def test_236(self, name='pyrotechnic ECU Test'):
        print('Pyrotechnic ECU Test not applicable for %s'%device_under_test)
        return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='NOT APPLICABLE'
        )
