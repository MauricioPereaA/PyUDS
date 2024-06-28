
            # This is and autogenerated test case using PyUDS Test Builder v0.3 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        if device_under_test in ['MSM', 'SCL','PTM']:
            tools.popup.warning(
                title='Not supported',
                description='Test case '+__name__+' not applicable for %s.\n'%device_under_test+\
                    'There is no DID that can accomplish test criteria'
            )
            raise Warning(__name__, 'is not supported by %s'%device_under_test)
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


    def test_539(self, name='<Transition Server to extendedSession> -- Sec Level 05'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            request_seed='01',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_540(self, name='send key -- Security Level 05'):
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

    def test_541(self, name='<Verify Server is unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_542(self, name='request seed -- Security Level 05'):
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

    def test_543(self, name='<Verify Server is still unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_544(self, name='<Verify Server is locked for Security Level 05>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 97' + '00'*21,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_545(self, name='<Unlock the Server via security access service for Level 05>'):
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

    def test_546(self, name='<Verify Server is unlocked for Security Level 05>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 97' + '00'*21,
            expected={
                'response': 'Positive'
            }
        )

    def test_547(self, name='<Verify Server is locked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_548(self, name='<Transition Server to extendedSession> -- Sec Level 05'):
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

    def test_549(self, name='<Activate TesterPresent> -- Sec Level 05'):
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

    def test_550(self, name='request seed -- Security Level 01'):
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

    def test_551(self, name='send key -- Security Level 01'):
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

    def test_552(self, name='<Verify Server is unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_553(self, name='request seed -- Security Level 13'):
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

    def test_554(self, name='<Verify Server is still unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_555(self, name='<Verify Server is locked for Security Level 13>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 98' + '00'*30,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_556(self, name='<Unlock the Server via security access service for Level 13>'):
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

    def test_557(self, name='<Verify Server is unlocked for Security Level 13>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 98' + '00'*30,
            expected={
                'response': 'Positive'
            }
        )

    def test_558(self, name='<Verify Server is locked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_559(self, name='<Transition Server to extendedSession> -- Sec Level 05'):
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

    def test_560(self, name='<Activate TesterPresent> -- Sec Level 05'):
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

    def test_561(self, name='request seed -- Security Level 01'):
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

    def test_562(self, name='send key -- Security Level 05'):
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

    def test_563(self, name='<Verify Server is unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_564(self, name='request seed -- Security Level 15'):
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

    def test_565(self, name='<Verify Server is still unlocked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Positive'
            }
        )

    def test_566(self, name='<Verify Server is locked for Security Level 15>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 97' + '00'*21,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_567(self, name='<Unlock the Server via security access service for Level 15>'):
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

    def test_568(self, name='<Verify Server is unlocked for Security Level 15>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 4F 97' + '00'*21,
            expected={
                'response': 'Positive'
            }
        )

    def test_569(self, name='<Verify Server is locked for Security Level 01>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2E 45 DA' + '00'*14,
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

