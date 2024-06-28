'''
    TestScript intended to perform CG3388 Tab 0x2C -- 1. Positive Flow
'''
''' High Level Script CG2019
Author: Manuel Medina

Modified by : Mauricio Perea

Modified by : Ricardo Montes   Date: 17-Jun-20
Modified by: Mauricio Perea        Date: 30-Sep-20

This script is intended to validate positive response of service 0x2C which main function is o dynamically define in a server a data identifier that can be read via ReadDataByIdentifier or ReadDataByPeriodicIdentifier service.


'''
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):

    @classmethod
    def format_hex(cls, decimal):
        return hex(decimal).replace('0x','').upper().rjust(2,'0')

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''

        if device_under_test is 'SCL':
            raise Warning('SCL does not support service 0x2C')

        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='0x2C'
        )     
        self.DID =  'F0 80'

        self.sec_levels = [
            '01', '03', '05', '09', '0B', '0D', '11', '13', '15'
        ]

        self.sec_levels_partial = [
            '09', '0B']

        self.supported_range = {
            'MSM' : (240, 256),
            'ARB' : (240, 256),
            'PTM' : (240, 256),
            'TCP' : (240, 256)
        }
        self.supported_DDDDI = [
            'F2 %s'%n for n in map(self.format_hex, range(
                self.supported_range[device_under_test][0],
                self.supported_range[device_under_test][1]
            )) # F2 XX -> F2 FF ['F2 F0', 'F2 F1', 'F2 F2', 'F2 F3', 'F2 F4', 'F2 F5', 'F2 F6', 'F2 F7', 'F2 F8', 'F2 F9', 'F2 FA', 'F2 FB', 'F2 FC', 'F2 FD', 'F2 FE', 'F2 FF'] are 16 combinations                                                       
        ]

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Positive Flow Define Single DDID By Identifier Session and Security Tests'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        self.step_counter = 2
	
        def step_preconditions():
            self.step_counter += 1
            test.preconditions(
                current_step='test_%s'%str(self.step_counter).rjust(3, '0')
            )

        def step_preconditions_functional():

            self.step_counter += 1
            test.preconditions(
                current_step='test_%s'%str(self.step_counter).rjust(3, '0'),
                functionalAddr=True	
            )			

      
        def extended_session():
            step_preconditions()
            test.step(
                step_title='Transition to Extended Session ',
                custom='10 03',
                expected = {
                    'response': 'Positive',
                    'dataLength': 4
                }
            )
	
        def enter_security_level(level):
            step_preconditions()
            test.step(
                step_title='Security Level %s - Req Seed'%level,
                request_seed=level,
                expected = {
                'response'            : 'Positive', 
                'dataLength'          : 31,
                'unexpected_response' : True, # Make sure 'data' is not in Response received
                'partialData'         : ('00', 'FF')
                }
            )

            step_preconditions()
            test.step(
                step_title='Security Level %s - Send Key'%level,
                send_key=level,
                expected = {
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
                }
            )
		#                'F2 F0','F0 80'
        def define_DDDDI(DDDDI, srcDataID):
            step_preconditions()
            test.step(
                step_title='Define DDDDI {0} by srcIdentifier {1}'.format(DDDDI, srcDataID),
                custom='2C 01 {0} {1} 01 01'.format(DDDDI, srcDataID),
                expected = {
                    'response': 'Positive'
                }
            )
	
        def clear_DDDDI(DDDDI):
            step_preconditions()
            test.step(
                step_title='Clear DDDDI {}'.format(DDDDI),
                custom='2C 03 {}'.format(DDDDI),
                expected = {
                    'response': 'Positive'
                }
            )
	
        def tester_present():
            step_preconditions_functional()
            test.step(
                step_title='Start Tester Present',
                start_tester_present=True,
                expected={                      #change
                    'response': 'No response'
                }
            )

        for DDDDI in self.supported_DDDDI:
	
            # Step 3 - Default Session - define PID
			#            'F2 F0','F0 80'
            define_DDDDI(DDDDI, self.DID)
	
            # Step 4 - Default Session - clear PID
            clear_DDDDI(DDDDI)
	
            # Step 5
            extended_session()
	
            # Step 6
            tester_present()
	
            # Step 7 - Extended Session - define PID
            define_DDDDI(DDDDI, self.DID)
	
            # Step 8 - Extended Session - clear PID
            clear_DDDDI(DDDDI)
	
            self.step_counter = 2
	

    def test_009(self, name='Positive Flow Define Single DDID By Identifier Session and Security Tests'):
        
        self.step_counter = 9

        def step_preconditions():
            self.step_counter += 1
            test.preconditions(
                current_step='test_%s'%str(self.step_counter).rjust(3, '0')
            )

        def enter_security_level(level):
            step_preconditions()
            test.step(
                step_title='Security Level %s - Req Seed'%level,
                request_seed=level,
                expected = {
                    'response': 'Positive'
                }
            )

            step_preconditions()
            test.step(
                step_title='Security Level %s - Send Key'%level,
                send_key=level,
                expected = {
                    'response': 'Positive'
                }
            )
        
        def define_DDDDI(DDDDI, srcDataID):
            step_preconditions()
            test.step(
                step_title='Define DDDDI {0} by srcIdentifier {1}'.format(DDDDI, srcDataID),
                custom='2C 02 {0} {1} 01 01'.format(DDDDI, srcDataID),
                expected = {
                    'response': 'Positive'
                }
            )
        
        def clear_DDDDI(DDDDI):
            step_preconditions()
            test.step(
                step_title='Clear DDDDI {}'.format(DDDDI),
                custom='2C 03 {}'.format(DDDDI),
                expected = {
                    'response': 'Positive'
                }
            )
        
        def tester_present():
            step_preconditions()
            test.step(
                step_title='Start Tester Present',
                start_tester_present=True
            )

        for DDDDI in self.supported_DDDDI:
            for lvl in self.sec_levels_partial:
                # Now on each Sec Level

                # Step 10 and 11
                enter_security_level(lvl)

                # Step 12
                define_DDDDI(DDDDI, self.DID)

                # Step 13
                clear_DDDDI(DDDDI)
        
            self.step_counter = 9

    def test_018(self, name='<Transition Server to the extendedSession>'):
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
