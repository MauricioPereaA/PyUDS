from framework.shared_libs.regex import Regex
import re


class TransportLayer(Regex):
    """
        *** Transport Layer - Test Cases ***
    """
    def __init__(self, trace_log=r'C:\Users\manuel.medina\Workspace\Logs\TraceLog.asc'):
        Regex.__init__(self, trace_log)

        self.uds_id_rqst =  r'[0-9A-F]{8}x[ ]+Tx[ ]+d \d+[ ]*'
        self.uds_id_rsp =   r'[0-9A-F]{8}x[ ]+Rx[ ]+d \d+[ ]*'
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

    def test_case_01(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]+', verbose=False) # Match
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 00 00', verbose=False)              # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)       # Match
        step_4 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)       # Match
        step_5 = self.find_line(self.uds_id_rqst +  r'23 [0-9A-F ]+', verbose=False)         # NO MATCHES FOUND
        step_6 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES FOUND // This is to verify that there is no any other response 

        # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False
    
    def test_case_02(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]+', verbose=False) # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 00 00', verbose=False)              # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)       # NO MATCH
        step_4 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)       # NO MATCH

                # PASSING CRITERIA
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_3, step_4, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_03(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]+', verbose=False) # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 00 00', verbose=False)              # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)       # Match
        step_4 = self.find_line(self.uds_id_rqst +  r'23 [0-9A-F ]+', verbose=False)       # Match
        step_5 = self.find_line(self.uds_id_rqst +  r'24 [0-9A-F ]+', verbose=False)       # NO MATCH
        step_6 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_04(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]{5}', verbose=False) # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 00 00', verbose=False)              # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)       # Match
        step_4 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)       # Match
        step_5 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)       # Match
        step_6 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, step_5, matches=True):
            print('Steps from 1 to 5 PASSED')
            if self.validate(step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_05(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]{5}', verbose=False) # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 00 00', verbose=False)              # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)       # Match
        step_4 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)       # NO Match
        step_5 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_06(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F1 90 [0-9A-F ]+', verbose=False) # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False) # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'30 00 00', verbose=False)              # NO Match
        step_4 = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)          # NO Match

                # PASSING CRITERIA
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_3, step_4, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_07(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)    # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False) # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'30 [0-9A-F ]+', verbose=False)             # Match
        step_4 = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)             # NO Match
        step_5 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_08(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)    # Match        
        step_2 = self.find_line(self.uds_id_rsp  +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False) # Match
        step_3 = self.find_line(self.uds_id_rqst +  r'30 [0-9A-F ]+', verbose=False)             # Match
        step_4 = self.find_line(self.uds_id_rqst +  r'30 [0-9A-F ]+', verbose=False)             # Match
        step_5 = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)             # Match
        step_6 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, step_5, matches=True):
            print('Steps from 1 to 5 PASSED')
            if self.validate(step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_09(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 [0-9A-F ]+', verbose=False)               # Match   
        step_3 = self.find_line(self.uds_id_rqst +  r'21 [0-9A-F ]+', verbose=False)    
        step_4 = self.find_line(self.uds_id_rqst +  r'22 [0-9A-F ]+', verbose=False)              # NO Match
        step_5 = self.find_line(self.uds_id_rqst +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_10(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp  +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)      # Match   
        step_3 = self.find_line(self.uds_id_rqst +  r'30 [0-9A-F ]+', verbose=False)               # Match
        step_4 = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)       # Match
        step_5 = self.find_line(self.uds_id_rsp  +  r'22 [0-9A-F ]+', verbose=False)       # Match
        step_6 = self.find_line(self.uds_id_rsp  +  r'23 [0-9A-F ]+', verbose=False)       # No Matches
        step_7 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, step_5, matches=True):
            if float(step_5[0]) - float(step_4[0]) < 0.250:        # N_Cr Timeout (250 ms)
                print('Steps from 1 to 5 PASSED')
                if self.validate(step_6, step_7, matches=False):
                    print('Whole Test PASSED')
                    return True
        else:
            return False

    def test_case_11(self, iteration):
        STmin = iteration*10
        step_1 = self.find_line(self.uds_id_rqst +   r'03 22 F1 90 [0-9A-F ]+',start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)          # Match    
        step_2 = self.find_line(self.uds_id_rsp  +   r'10 14 62 F1 90 [0-9A-F ]+', start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)      # Match

        if iteration > 0:
            step_3 = self.find_line(self.uds_id_rqst +  r'30 00 %s [0-9A-F ]+'%STmin, start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False) 
        else:
            step_3 = self.find_line(self.uds_id_rqst +  r'30 00 01 [0-9A-F ]+', start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)  

        step_4 = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+',start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)       # Match
        step_5 = self.find_line(self.uds_id_rsp  +  r'22 [0-9A-F ]+',start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)       # Match
        step_6 = self.find_line(self.uds_id_rsp  +  r'23 [0-9A-F ]+',start_flag='This was iteration %s'%iteration,end_flag='This is iteration %s'%iteration, verbose=False)       # Match

        decimal_STmin = int((step_3[1][31]+step_3[1][32]),16)*0.001   # This represents the maximum separation time between consecutive frames in ms
        difference = float(step_5[0]) - float(step_4[0])

                # PASSING CRITERIA
        if self.validate(step_1, step_2, step_3, step_4, step_5, matches=True):
            if difference < decimal_STmin:
                print('Steps from 1 to 5 PASSED')
                if self.validate(step_6, matches=False):
                    print('Whole Test PASSED')
                    return True
        else:
            return False

    def test_case_12(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'10 21 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp  +  r'30 [0-9A-F ]+', verbose=False)               # Match   
        step_3 = self.find_line(self.uds_id_rsp  +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES

        STmin = int((step_2[1][31]+step_2[1][32]))

                # PASSING CRITERIA
        if STmin >= 0 and STmin <= 127 or STmin >= 241 and STmin <= 249:            
            if self.validate(step_1, step_2, matches=True):
                print('Steps from 1 to 2 PASSED')
                if self.validate(step_3, matches=False):
                    print('Whole Test PASSED')
                    return True
        else:
            return False

    def test_case_13(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp  +  r'0\d 62 [0-9A-F ]+', verbose=False)        # Match   
        step_3 = self.find_line(self.uds_id_rqst +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_3, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_14(self):
        step_1 = self.find_line(self.uds_id_rqst +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp  +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)        # Match   
        step_3 = self.find_line(self.uds_id_rqst +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_3, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_15(self):
        step_1 = self.find_line(self.uds_id_rqst  +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp   +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)        # Match   
        step_3 = self.find_line(self.uds_id_rqst  +  r'30 [0-9A-F ]+', verbose=False)               # Match   
        step_4 = self.find_line(self.uds_id_rsp   +  r'21 [0-9A-F ]+', verbose=False)               # Match   
        step_5 = self.find_line(self.uds_id_rqst  +  r'21 [0-9A-F ]+', verbose=False)               # Match   
        step_6 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_16_interruption_correctly(self):
        consecutive_1     = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)         # Match 
        flow_control_2    = self.find_line(self.uds_id_rqst  +  r'32 00 00 [0-9A-F ]+', verbose=False)         # Match     
        consecutive_2     = self.find_line(self.uds_id_rsp  +  r'22 [0-9A-F ]+', verbose=False)         # Match   
        print(
            float(consecutive_1[0]), float(flow_control_2[0]), float(consecutive_2[0])
        )
        print(float(consecutive_1[0]) < float(flow_control_2[0]) < float(consecutive_2[0]))
        if float(consecutive_1[0]) < float(flow_control_2[0]) < float(consecutive_2[0]):
            return True
        print('flow_control_2 >> 32 00 00 .. << must be sent between consecutive frames.')
        return False   

    def test_case_16(self):
        step_1 = self.find_line(self.uds_id_rqst  +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp   +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)        # Match   
        step_3 = self.find_line(self.uds_id_rqst  +  r'30 [0-9A-F ]+', verbose=False)                  # Match
        step_4 = self.find_line(self.uds_id_rsp    +  r'21 [0-9A-F ]+', verbose=False)         # Match 
        step_5 = self.find_line(self.uds_id_rqst  +  r'32 00 00 [0-9A-F ]+', verbose=False)         # Match     
        step_6 = self.find_line(self.uds_id_rsp    +  r'22 [0-9A-F ]+', verbose=False)         # Match   
        step_7 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_17_interruption_correctly(self):
        consecutive_1  = self.find_line(self.uds_id_rsp  +  r'21 [0-9A-F ]+', verbose=False)         # Match 
        flow_control_2 = self.find_line(self.uds_id_rqst  +  r'50 00 00 [0-9A-F ]+', verbose=False)         # Match     
        consecutive_2  = self.find_line(self.uds_id_rsp  +  r'22 [0-9A-F ]+', verbose=False)         # Match   
        print(
            float(consecutive_1[0]), float(flow_control_2[0]), float(consecutive_2[0])
        )
        print(float(consecutive_1[0]) < float(flow_control_2[0]) < float(consecutive_2[0]))
        if float(consecutive_1[0]) < float(flow_control_2[0]) < float(consecutive_2[0]):
            print('ia halo reach')
            return True
        return False   

    def test_case_17(self):
        step_1 = self.find_line(self.uds_id_rqst  +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp   +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)        # Match   
        step_3 = self.find_line(self.uds_id_rqst  +  r'30 [0-9A-F ]+', verbose=False)                  # Match
        step_4 = self.find_line(self.uds_id_rsp   +  r'21 [0-9A-F ]+', verbose=False)            # Match 
        step_5 = self.find_line(self.uds_id_rqst  +  r'50 00 00 [0-9A-F ]+', verbose=False)          # Match     
        step_6 = self.find_line(self.uds_id_rsp   +  r'22 [0-9A-F ]+', verbose=False)                     # Match   
        step_7 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 00)).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_18(self):
        step_1 = self.find_line(self.uds_id_rqst  +  r'10 11 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp   +  r'30 [0-9A-F ]+', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst  +  r'03 22 F1 A0 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rsp    +  r'04 62 F1 A0 [0-9A-F ]+', verbose=False)         # Match 
        step_5 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!21 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_19(self):
        step_1 = self.find_line(self.uds_id_rqst  +  r'10 11 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp   +  r'30 [0-9A-F ]+', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst  +  r'10 11 22 F1 90 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rsp   +  r'30 [0-9A-F ]+', verbose=False)          # Match   
        step_5 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_20(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'10 11 22 [0-9A-F ]+', verbose=False)         # Match     
        step_2 = self.find_line(self.uds_id_rsp    +  r'30 [0-9A-F ]{20}', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'30 08 14 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'21 [0-9A-F ]+', verbose=False)          # Match   
        step_5 = self.find_line(self.uds_id_rqst   +  r'22 [0-9A-F ]+', verbose=False)          # Match   
        step_6 = self.find_line(self.uds_id_rsp    +  r'[0-9A-F ]{5} 62 [0-9A-F ]{5}', verbose=False)          # Match   
        step_7 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{20}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_21(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'10 11 22 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'30 [0-9A-F ]{20}', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'40 08 14 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'21 [0-9A-F ]+', verbose=False)          # Match   
        step_5 = self.find_line(self.uds_id_rqst   +  r'22 [0-9A-F ]+', verbose=False)          # Match   
        step_6 = self.find_line(self.uds_id_rsp    +  r'[0-9A-F ]{5} 62 [0-9A-F ]+', verbose=False)          # Match   
        step_7 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_22(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'32 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rsp    +  r'21 [0-9A-F ]+', verbose=False)          # No Match   
        step_5 = self.find_line(self.uds_id_rsp    +  r'22 [0-9A-F ]+', verbose=False)          # No Match   
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_23(self, blocksize):
        if not blocksize in [1, 8, 20]:
            raise Warning('Blocksize specified is not supported. Please try using: %s'%blocksize)
            
        if blocksize == 1:
            step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)         # Match
            step_2 = self.find_line(self.uds_id_rsp    +  r'[0-9A-F ]{5} 62 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)          # Match 
            step_3 = self.find_line(self.uds_id_rqst   +  r'30 0%s 00 [0-9A-F ]{14}'%blocksize, start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)                 # Match
            i = 1

            while i < 2:
                step_4 = self.find_line(self.uds_id_rsp    +  r'2%i [0-9A-F ]{20}'%i,start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)          # Match   
                if step_4[0] == False:
                    break
                i += 1

        if blocksize == 8:
            step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)         # Match
            step_2 = self.find_line(self.uds_id_rsp    +  r'[0-9A-F ]{5} 62 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)          # Match 
            step_3 = self.find_line(self.uds_id_rqst   +  r'30 0%s 00 [0-9A-F ]+'%blocksize, start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)                 # Match
            i = 1
            while i < 9:
                step_4 = self.find_line(self.uds_id_rsp    +  r'2%i [0-9A-F ]+'%i,start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)          # Match   
                if step_4[0] == False:
                    break
                i += 1

        if blocksize == 20:
            step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)         # Match
            step_2 = self.find_line(self.uds_id_rsp    +  r'[0-9A-F ]{5} 62 F0 F4 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)          # Match 
            step_3 = self.find_line(self.uds_id_rqst   +  r'30 14 00 [0-9A-F ]+', start_flag='This was the iteration for blocksize %s'%blocksize,end_flag='This is the iteration for blocksize %s'%blocksize, verbose=False)                 # Match
            i = 1
            while i < 16:
                hexnumber = hex(i).lstrip('0x')
                text = '2{} [0-9A-F ]'.format(hexnumber) + '+' # This concatenates the expresion to be searched in the asc file
                if text[1] in ['a','b','c','d','e','f']:
                    text = '2{} [0-9A-F ]'.format(hexnumber.upper()) + '+'
                step_4 = self.find_line(self.uds_id_rsp + text, 
                                            start_flag='This was the iteration for blocksize %s'%blocksize,
                                            end_flag='This is the iteration for blocksize %s'%blocksize, 
                                            multiple_matches=False, 
                                            verbose=False)          # Match   
                if step_4[0] == False:
                    break
                i += 1

            i=0
            
            # Search for the multiple matches in flow control frames as flow control passes $2F ..
            while i < 5:
                step_4 = self.find_line(self.uds_id_rsp + r'2%i [0-9A-F ]+'%i,
                                            start_flag='This was the iteration for blocksize %s'%blocksize,
                                            end_flag='This is the iteration for blocksize %s'%blocksize, 
                                            multiple_matches=True, 
                                            verbose=False)          # Match   
                if step_4[0] == False:
                    break

                i += 1

                # PASSING CRITERIA

        step_5 = self.find_line(self.uds_id_rsp   +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
        step_4 = step_4[0] if isinstance(step_4[0], tuple) else step_4
        if self.validate(step_1, step_2, step_3, step_4, matches=True):
            print('Steps from 1 to 4 PASSED')
            if self.validate(step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False


    def test_case_24(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)        # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)     # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'30 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rsp    +  r'21 [0-9A-F ]+', verbose=False)          # Match   
        step_5 = self.find_line(self.uds_id_rsp    +  r'22 [0-9A-F ]+', verbose=False)          # Match   
        step_6 = self.find_line(self.uds_id_rsp    +  r'23 [0-9A-F ]+', verbose=False)          # No Matches   
        step_7 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3,step_4,step_5, matches=True):
            print('Steps from 1 to 5 PASSED')
            if self.validate(step_6, step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_25(self, invalid_flow_status=3):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)          # Match   
        
        if invalid_flow_status > 3 and invalid_flow_status < 10 :
            step_3 = self.find_line(self.uds_id_rqst +  r'3%s 00 [0-9A-F ]+'%invalid_flow_status, start_flag='This was invalid status %s'%invalid_flow_status,end_flag='This is invalid status %s'%invalid_flow_status, verbose=False) 

        elif invalid_flow_status >= 10:
            hexnumber = hex(invalid_flow_status).lstrip('0x')
            hexnumber = hexnumber.upper()
            step_3 = self.find_line(self.uds_id_rqst +  r'3%s 00 [0-9A-F ]+'%hexnumber, start_flag='This was invalid status %s'%invalid_flow_status,end_flag='This is invalid status %s'%invalid_flow_status, verbose=False) 

        else:
            step_3 = self.find_line(self.uds_id_rqst   +  r'33 [0-9A-F ]+', start_flag='This was invalid status %s'%invalid_flow_status,end_flag='This is invalid status %s'%invalid_flow_status, verbose=False)

        step_4 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_26(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)          # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'31 [0-9A-F ]+', verbose=False)                 # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'30 [0-9A-F ]+', verbose=False)                 # Match
        step_5 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 A0 [0-9A-F ]+', verbose=False)                 # Match
        step_6 = self.find_line(self.uds_id_rsp    +  r'62 F1 A0 [0-9A-F ]+', verbose=False)                 # Match
        step_7 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_7, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_27(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)        # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)     # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'30 00', verbose=False)                         # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'04 22 [0-9A-F ]+', verbose=False)                 # Match   
        step_5 = self.find_line(self.uds_id_rsp    +  r'03 7F 22 13 [0-9A-F ]+', verbose=False)                 # Match
        step_6 = self.find_line(self.uds_id_rsp    +  r'23 [0-9A-F ]+', verbose=False)                 # Match
                # PASSING CRITERIA 
        if self.validate(step_1, step_2, step_3, step_4, step_5, step_6, matches=True):
            print('Steps from 1 to 6 PASSED')
            if self.validate(step_6, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_28(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22 F1 90 [0-9A-F ]+', verbose=False)        # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'10 14 62 F1 90 [0-9A-F ]+', verbose=False)     # Match   
        step_3 = self.find_line(self.uds_id_rqst   +  r'30 [0-9A-F ]+', verbose=False)                 # Match   
        step_4 = self.find_line(self.uds_id_rsp    +  r'21 [0-9A-F ]+', verbose=False)                 # Match
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_29(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'00 03 22 F1 90 [0-9A-F ]+', verbose=False)         # Match
        i = 8
        while i < 16:
            hexnumber= hex(i).lstrip('0x')
            text = '0{} [0-9A-F ]'.format(hexnumber) + '+' # This concatenates the expresion to be searched in the asc file
            if text[1] in ['a','b','c','d','e','f']:
                text = '0{} [0-9A-F ]'.format(hexnumber.upper()) + '+'
            step_2 = self.find_line(self.uds_id_rqst + text, verbose=False)          # Match   
            if step_2[0] == False:
                break
            i += 1
        
        step_3 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES

                # PASSING CRITERIA        
        if self.validate(step_1, step_2, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_3, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_30(self): # Pending ..
        step_1 = self.find_line(self.uds_id_rqst   +  r'03 22', start_flag = 'CAN-DLC shorter and equal to transport protocol data length test ends', end_flag = 'CAN-DLC shorter and equal to transport protocol data length test begins', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rqst   +  r'03 22', start_flag = 'CAN-DLC shorter to transport protocol data length test ends', end_flag = 'CAN-DLC shorter to transport protocol data length test begins', verbose=False)         # Match
        step_3 = self.find_line(self.uds_id_rqst   +  r'03 22 F0', start_flag = 'CAN-DLC equal to SF data length test ends', end_flag = 'CAN-DLC equal to SF data length test begins', verbose=False)         # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'[0-9A-F ]{2} 62 [0-9A-F ]+', verbose=False)         # Match
        step_5 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_31(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'10 00 22 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, matches=True):
            print('Steps from 1 to 2 PASSED')
            if self.validate(step_2, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_32(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'10 0B 22 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'30 [0-9A-F ]+', verbose=False)               # Match
        step_3 = self.find_line(self.uds_id_rqst   +  r'21 00 00 [0-9A-F ]+', verbose=False)         # Match
        step_4 = self.find_line(self.uds_id_rqst   +  r'22 00 00 [0-9A-F ]+', verbose=False)         # Match
        step_5 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, step_2, step_3, matches=True):
            print('Steps from 1 to 3 PASSED')
            if self.validate(step_4, step_5, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_33(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'08 40 08 14 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, matches=True):
            print('Step 1 PASSED')
            if self.validate(step_2, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_34(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'10 21 22 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, matches=True):
            print('Step 1 PASSED')
            if self.validate(step_2, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    '''
        Function test_case_35() commented below correspond to the older TC35 which for the CG3388 version 2019 is deleted
    '''
    # def test_case_35(self):
    #     step_1 = self.find_line(self.uds_id_rqst   +  r'10 21 22 [0-9A-F ]+', verbose=False)         # Match
    #     step_2 = self.find_line(self.uds_id_rsp    +  r'30 [0-9A-F ]+', verbose=False)               # Match
    #     step_3 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
    #             # PASSING CRITERIA        
    #     if self.validate(step_1, step_2, matches=True):
    #         print('Steps 1 to 2 PASSED')
    #         if self.validate(step_3, matches=False):
    #             print('Whole Test PASSED')
    #             return True
    #     else:
    #         return False

    def test_case_35(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'21 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'30 [0-9A-F ]+', verbose=False)         # Match
        step_3 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, matches=True):
            print('Step 1 PASSED')
            if self.validate(step_2, step_3, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False

    def test_case_36(self):
        step_1 = self.find_line(self.uds_id_rqst   +  r'30 [0-9A-F ]+', verbose=False)         # Match
        step_2 = self.find_line(self.uds_id_rsp    +  r'^.+([0-9A-F]{8}x[ ]+Rx[ ]+d 8[ ](?!30 )).*', verbose=False)  # NO MATCHES
                # PASSING CRITERIA        
        if self.validate(step_1, matches=True):
            print('Step 1 PASSED')
            if self.validate(step_2, matches=False):
                print('Whole Test PASSED')
                return True
        else:
            return False