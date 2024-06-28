'''

     Test Example - Testing All UDS Services

'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False # Write on CG Report
        )

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Testing all Services :: ' + __name__):

        test.preconditions(current_step='start_tester_present')
        test.step(
            step_title=name,
            start_tester_present=True
        )

        test.preconditions(current_step='stop_tester_present')
        test.step(
            step_title=name,
            stop_tester_present=True
        )

        test.preconditions(current_step='read_data_ID')
        test.step(
            step_title=name,
            read_data_ID='F0 F4'
        )
        
        test.preconditions(current_step='ecu_reset')
        test.step(
            step_title=name,
            ecu_reset=True
        )

        test.preconditions(current_step='start_routine')
        test.step(
            step_title=name,
            start_routine='FF 01'
        )

        test.preconditions(current_step='request_routine_result')
        test.step(
            step_title=name,
            request_routine_result='FF 01'
        )

        test.preconditions(current_step='rqst_dtc_number_status_mask')
        test.step(
            step_title=name,
            rqst_dtc_number_status_mask='09'
        )

        test.preconditions(current_step='rqst_dtc_by_status_mask')
        test.step(
            step_title=name,
            rqst_dtc_by_status_mask='09'
        )
        
        test.preconditions(current_step='rqst_dtc_read_extended_data')
        test.step(
            step_title=name,
            rqst_dtc_read_extended_data='XX XX'
        )

        test.preconditions(current_step='rqst_supported_dtcs')
        test.step(
            step_title=name,
            rqst_supported_dtcs=True
        )

        test.preconditions(current_step='rqst_supported_dtcs')
        test.step(
            step_title=name,
            rqst_supported_dtcs=True
        )

        test.preconditions(current_step='io_return_control')
        test.step(
            step_title=name,
            io_return_control='FF FF'
        )

        test.preconditions(current_step='io_reset_to_default')
        test.step(
            step_title=name,
            io_reset_to_default=['FF FF', '01']
        )

        test.preconditions(current_step='io_freeze_current_state')
        test.step(
            step_title=name,
            io_freeze_current_state=['FF FF', '01']
        )

        test.preconditions(current_step='io_short_term_adjustment')
        test.step(
            step_title=name,
            io_short_term_adjustment=['FF FF', '01']
        )

        test.preconditions(current_step='request_seed')
        test.step(
            step_title=name,
            request_seed='01'
        )

        test.preconditions(current_step='send_key')
        test.step(
            step_title=name,
            send_key='01'
        )

        test.preconditions(current_step='write_data_ID')
        test.step(
            step_title=name,
            write_data_ID=['F0 F4', '00'*822]
        )

        test.preconditions(current_step='read_periodic_data_id')
        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID='FF', rate='03')
        )

        test.preconditions(current_step='stop_periodic_data')
        test.step(
            step_title=name,
            stop_periodic_data='FF'
        )

        test.preconditions(current_step='default_session_control')
        test.step(
            step_title=name,
            default_session_control=True
        )

        test.preconditions(current_step='extended_session_control')
        test.step(
            step_title=name,
            extended_session_control=True
        )

        test.preconditions(current_step='programming_session_control')
        test.step(
            step_title=name,
            programming_session_control=True
        )

        test.preconditions(current_step='safety_session_control')
        test.step(
            step_title=name,
            safety_session_control=True
        )

        test.preconditions(current_step='dtc_settings')
        test.step(
            step_title=name,
            dtc_settings=False
        )

        test.preconditions(current_step='communication_control')
        test.step(
            step_title=name,
            communication_control=False
        )