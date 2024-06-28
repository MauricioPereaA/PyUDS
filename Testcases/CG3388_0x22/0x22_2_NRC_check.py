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
            excel_tab='0x22'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='NRC_13_test by just sending service 22'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            default_session_control=True,
            custom='22',
            expected={
                'response': 'Negative',
                'data': '13'
            }
        )

    def test_002(self, name='NRC_13_test by exceeding the maximum number of valid DIDs'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80 F0 80',
            expected={
                'response': 'Negative',
                'data': '13'
            }
        )

    def test_003(self, name='send two unsupported dataIdentifiers'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F1 87 F1 88',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_004(self, name='send a unsupported dataIdentifier which is not supported in the current session'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'ARB':
            test.step(
                step_title=name,
                custom='22 4B 63',
                expected={
                    'response': 'Negative',
                    'data': '31'
                }
            )
        if device_under_test in  ['SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Negative',
                    'data': '31'
                }
            )

    def test_005(self, name='send a dynamic data identifier that has not yet been assigned'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F2 FF',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_007(self, name='request a secured  '):
        # Extended session transition
        test.preconditions('Transition to extended session')
        test.step(step_title='Transition to extended session',
                extended_session_control=True)

        test.preconditions(
            step_info=info(),
        )

        if device_under_test is 'PTM':
            test.step(
                step_title=name,
                custom='22 51 7F',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )
        if device_under_test in 'SCL':
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )
        if device_under_test is 'TCP':
            test.step(
                step_title=name,
                custom='22 F0 A7',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F0 8F',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F0 90',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F0 91',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F0 92',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 F0 94',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )


    def test_008(self, name='request two secured DIDs'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'PTM':
            test.step(
                step_title=name,
                custom='22 51 7F 51 7E ',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )
        if device_under_test in ['SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7 F0 A7',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

    def test_009(self, name='request two DIDs, one secured and the other unsecured'):
        test.preconditions(
            step_info=info()
        )
        if device_under_test is 'PTM':
            test.step(
                step_title=name,
                custom='22 51 7F F1 90',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )
        if device_under_test in ['SCL', 'TCP']:
            test.step(
                step_title=name,
                custom='22 F0 A7 F0 80',
                expected={
                    'response': 'Negative',
                    'data': '33'
                }
            )

    def test_011(self, name='conditions not correct test (NRC 22)'):
        if device_under_test is 'PTM':
            # Test Precondition
            test.preconditions('Enter security level 9 as a precondition to test NRC 22')
            test.step(step_title='Enter security level 9 as a precondition to test NRC 22',
                request_seed='09', send_key = '09')
            # Test Precondition
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='22 4B 64',
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )
        if device_under_test in ['SCL', 'TCP']:
            test.preconditions(
                step_info=info()
            )
            test.set_dtc_condition(overVoltage=True)
            test.step(
                step_title=name,
                custom='22 F0 80',
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )
            test.power_supply_reset_default()

    def test_013(self, name='create a condition which the response message will exceed the limit of underlying transport protocol'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F0 F4 F0 F4 F0 F4 F0 F4 F0 F4',
            expected={
                'response': 'Negative',
                'data': '14'
            }
        )