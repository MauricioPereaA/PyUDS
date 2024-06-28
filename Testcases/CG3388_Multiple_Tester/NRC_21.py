            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
'''
    TestScript intended to perform CG3388 Tab MultiTester
'''
'''  CG2020
Author: Mauricio Perea
Modified by: Mauricio Perea        Date: 30-Sep-20

'''      
from framework.shared_functions import ECU_info, tools, device_under_test
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
            excel_tab='Multiple Tester & NRC 21'
        )
        self.srcDID = {
            'ARB': '50 03',
            'PTM': '50 03',
            'MSM': '44 6A',
            'TCP': '43 AE'
        }
        self.tester = [ECU_info['name'], ECU_info['name']+'_2']
        tools.popup.warning(
            title='Multiple Tester',
            description='Please make sure you have created 6 testers from Diagnostic/ISO TP:\n\
                Tester 1: {0}\n\
                Tester 2: {0}_2\n\
                Tester 3: {0}_3\n\
                Tester 4: {0}_4\n\
                Tester 5: {0}_5\n\
                Tester 6: {0}_6\n\
            Otherwise, you will not be able to perform this test.'.format(ECU_info['name'])
        )
            
        #For each tester combination below, repeat Multiple Tester Test Steps 
        #    • Tester 1 = F1, Tester 2 = F2 -
        #    • Tester 1 = F1, Tester 2 = F3 -
        #    • Tester 1 = F1, Tester 2 = F4 -
        #    • Tester 1 = F1, Tester 2 = F5 -
        #    • Tester 1 = F1, Tester 2 = F6 -
        #    • Tester 1 = F2, Tester 2 = F1 -
        #    • Tester 1 = F3, Tester 2 = F1 -
        #    • Tester 1 = F4, Tester 2 = F1
        #    • Tester 1 = F5, Tester 2 = F1
        #    • Tester 1 = F6, Tester 2 = F1        

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='<Transition Server to defaultSession> '):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            default_session_control=True,
            multiple_tester=['10 01', '10 01'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_003(self, name='T1: transition to extendedSession'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='T1: start tester present'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_005(self, name='busyRepeatRequest -  0x21_TwoTesters'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            multiple_tester=['11 01', '11 01'],

            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_006(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_007(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_008(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_009(self, name='busyRepeatRequest - 0x21'):          
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['27 01', '27 01'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_010(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_011(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_012(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_013(self, name='NRC 21 test'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            multiple_tester=['28 00 01', '28 00 01'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_014(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_015(self, name='CANoe Simulation Test - Multiple tester test'):
        test.preconditions(
             step_info=info()
        )

        test.step(
             step_title=name,
             multiple_tester=['3E 00', '3E 00'],
             expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_016(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_017(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_018(self, name='busyRepeatRequest - 0x21'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['85 01', '85 01'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_019(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
#Service 86
    def test_020(self, name='busyRepeatRequest - 0x21'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            multiple_tester=['86 00 02', '86 00 02'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_021(self, name='NRC_21_test'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            default_session_control=True,
            multiple_tester = ['22 F0 F4', '22 F0 F4'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_022(self, name='T1: transition to extendedSession'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_023(self, name='T1: start tester present'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_024(self, name='Security Level 09 - Req Seed'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            request_seed='09',
            expected={
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_025(self, name='<Unlock the Server via security access service> - Security Level 09'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            send_key='09',
            expected={
                'response'  : 'Positive'
            }
        )
#Service 23
    def test_026(self, name='NRC_21_test'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            multiple_tester = ['23 xx xx', '23 xx xx'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_027(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

#not sure
    def test_028(self, name='Dynamically Define Data Identifier, definebyIdentifier'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FF '+self.srcDID[device_under_test]+' 01 01',
            expected={
                'response': 'Positive'
            }
        )
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FE F0 80 01 01',
            expected={
                'response': 'Positive'
            }
        )
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FD F0 81 01 06',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FC F1 A0 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FB '+self.srcDID[device_under_test]+' 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 FA F0 80 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F9 F0 81 01 06',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F8 F1 A0 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F7 '+self.srcDID[device_under_test]+' 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F6 F0 80 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F5 F0 81 01 06',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F4 F1 A0 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F3 '+self.srcDID[device_under_test]+' 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F2 F0 80 01 01',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F1 F0 81 01 06',
            expected={
                'response': 'Positive'
            }
        )

        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2C 01 F2 F0 F1 A0 01 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_029(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_030(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_031(self, name='busyRepeatRequest - 0x21'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['2A 01 FF', '2A 01 FF'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_032(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
#Service 2C
    def test_033(self, name='serviceNotSupported - 0x11'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['2C 01 F2 FF F0 80 01 01', '2C 01 F2 FF F0 80 01 01'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_034(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
#Change it to another did        
    def test_035(self, name='busyRepeatRequest - 0x21 Multiple Testers'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            request_seed='01',
            send_key='01',
            multiple_tester=['2E F1 99 00 00 00 00', '2E F1 99 00 00 00 00'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )

    def test_036(self, name='First and Second tester physical Req'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['14 FF FF FF', '14 FF FF FF'],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_037(self, name='busyRepeatRequest - 0x21'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['19 01 FF', '19 01 FF'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_038(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_039(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_040(self, name='busyRepeatRequest - 0x21'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=[
                '2F 49 5F 00', 
                '2F 49 5F 00'
            ],
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_041(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_042(self, name='busyRepeatRequest - 0x21'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['31 01 FF 01', '31 01 FF 01'],

            expected={
                'response': 'Negative',
                'data': '21'
            }
        )
    def test_043(self, name='T1: transition to extendedSession'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_044(self, name='T1: start tester present'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
#Service 38
    def test_045(self, name='busyRepeatRequest - 0x21'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            multiple_tester=['38 XX', '38 XX'],
            expected={
                'response': 'Negative',
                'data': '21'
            }
        )

    def test_046(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )
    def test_047(self, name='T1: transition to extendedSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_048(self, name='T1: start tester present'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True,
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )
    def test_049(self, name='<hardreset -extendedSession>Preconditions Security Level 01>'):
        if device_under_test in ['MSM']:
            print('Test not applicable for %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1],
            power_mode='OFF',
            functionalAddr=True
            
        )
        test.step(
            step_title=name,
            custom='11 01',
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_050(self, name='Security Level 01 - Req Seed'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]            
        )
        test.step(
            step_title=name,
            request_seed='01',
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
#the precondition
    def test_051(self, name='disable Rx And Tx extendedSession Physical Messaging'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]  
        )
        test.step(
            step_title=name,
            custom='28 00 01',
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_052(self, name='CANoe Simulation Test - Multiple tester test'):
        test.preconditions(
             step_info=info(),
            tester_id=self.tester[1]  
        )

        test.step(
            step_title=name,
            extended_session_control=True,
            custom='3E 00',
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_053(self, name='DTC Setting On extendedSession Physical Messaging'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[1]  
        )
        test.step(
            step_title=name,
            custom='85 01',
            expected={
                'response': 'Negative',
                'data'    : '21'
            }
        )
    def test_054(self, name='T1: transition to defaultSession'):
        test.preconditions(
            step_info=info(),
            tester_id=self.tester[0]
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )