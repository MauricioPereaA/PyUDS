
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import supported_rids, supported_io_dids, device_under_test, no_io_ecus
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
            excel_tab='Scanner',
            step_delay=0.025
        )
        self.supported_rids = supported_rids
        self.supported_io_dids = supported_io_dids

        self.rids_deviate_from_ODX = (
            'THIS IS A PLACEHOLDER',
            'THIS IS A PLACEHOLDER',
            'THIS IS A PLACEHOLDER'
        )
        self.io_rids_deviate_from_ODX = (
            'THIS IS A PLACEHOLDER',
            'THIS IS A PLACEHOLDER',
            'THIS IS A PLACEHOLDER'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def format_hex(self, decimal):
        return hex(decimal).replace('0x','').upper().rjust(4,'0')

    def test_001(self, name='All RIDs'):
        test.preconditions(step_info=info())
        for i in range(65536):
            if not i in self.supported_rids:
                test.step(
                    step_title='RID ' + self.format_hex(i),
                    custom='31 01 ' + self.format_hex(i),
                    expected={
                        'response': 'Negative',
                        'data': '31'
                    }
                )

    def test_002(self, name='rids which deviate from GB6000'):
        if not len(self.rids_deviate_from_ODX) > \
            self.rids_deviate_from_ODX.count('THIS IS A PLACEHOLDER'):
            print('Theres no rids that deviates from GB6000\n',
                    'if any, please specify from %s test script.'%__name__)
            return 0
        for rids in self.rids_deviate_from_ODX:
                test.preconditions(
                    step_info=info()
                )
                test.step(
                    step_title=rids,
                    custom='31 01 '+ rids,
                    expected={
                        'response': 'Negative',
                        'unexpected_response': True,
                        'data': '31'
                    }
                )

    def test_003(self, name='All IO DIDs'):
        if device_under_test in no_io_ecus:
            raise Warning(device_under_test, 'does not support service 0x2F')

        test.preconditions(step_info=info())
        test.step(step_title='extendedSession',
                    extended_session_control=True)
        for i in range(65536):
            if not i in self.supported_io_dids:
                test.step(
                    step_title='DID ' + self.format_hex(i),
                    custom='2F ' + self.format_hex(i) + '03 00',
                    expected={
                        'response': 'Negative',
                        'data': '31'
                    }
                )

    def test_004(self, name='io rids which deviate from GB6000'):
        if not len(self.io_rids_deviate_from_ODX) > \
            self.io_rids_deviate_from_ODX.count('THIS IS A PLACEHOLDER'):
            print('Theres no io rids that deviates from GB6000\n',
                    'if any, please specify from %s test script.'%__name__)
            return 0
        for io_rids in self.io_rids_deviate_from_ODX:
                test.preconditions(
                    step_info=info()
                )
                test.step(
                    step_title=rids,
                    custom='31 01 '+ rids,
                    expected={
                        'response': 'Negative',
                        'unexpected_response': True,
                        'data': '31'
                    }
                )

