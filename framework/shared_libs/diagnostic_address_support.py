from framework.shared_libs.regex import Regex
import os
import re

class DiagAddrResp(Regex):
    """
                --- UNDER DEVELOPMENT ---
        *** Diagnostic Address Support - Test Cases ***
    """

    #def __init__(self, trace_log=r'C:\Users\manuel.medina\Workspace\Logs\TraceLog.asc'):
    def __init__(self, trace_log=r'C:\Users\manuel.medina\Workspace\Logs\TraceLog.asc'):
        Regex.__init__(self, trace_log)
        self.uds_id_rqst =  r'6A4[ ]+Tx[ ]+d \d+[ ]*'
        self.uds_id_rsp =   r'[0-9A-F]{8}x[ ]+Rx[ ]+d \d+[ ]*'
        self.uds_id_rsp_tx =   r'[0-9A-F]{8}x[ ]+Tx[ ]+d \d+[ ]*'
        self.test_failed = 'Test Failed !!!'

    def validate(self, *args, matches=True):
        """
        Validates response returned from above Class
         - Possible responses:
            (bool, str) => For NO matches
            (str, str)  => For match founds

         - Usage:
            >>validate(Regex.find_line('PATTERN'), matches=True)
                if PATTERN is found using 'find_line' method,
                it will return: True
        """
        expected = str if matches else bool
        for i in args:
            if not isinstance(i, tuple):
                return False
            if not isinstance(i[0], expected):
                return False
        return True

    def test_case_flow_control_1(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F0 F4 [0-9A-F ]+', start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_2 = self.find_line(self.uds_id_rsp +  r'13 39 62 F0 F4+',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_3 = self.find_line(self.uds_id_rsp_tx +  r'30 00 00 00 00 00 00 00',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_4 = self.find_line(self.uds_id_rsp +  r'21 [0-9A-F ]+ ',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_5 = self.find_line(self.uds_id_rsp +  r'22 [0-9A-F ]+ ',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_6 = self.find_line(self.uds_id_rsp +  r'23 [0-9A-F ]+ ',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_7 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match

        # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 and 2 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False
    def test_case_flow_control_2(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 09 22 F1 B0 [0-9A-F ]+', start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_2 = self.find_line(self.uds_id_rsp +  r'30 00 00 00 00 00 00 00',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        step_3 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*',start_flag = "Passed: Test module 'Diagnostic Address Support' finished.", end_flag="Test module 'Diagnostic Address Support' started.", verbose=False) # Match
        # PASSING CRITERIA
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 and 2 PASSED')
            if self.validate(step_3, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False