
'''
    TestScript intended to perform CG3388 Tab 0x2A -- 1. Positive Flow
'''
''' High Level Script CG2019
Author: Manuel Medina
Modified by : Mauricio Perea
Modified by : Ricardo Montes  Date: 17-Jun-20
Modified by: Mauricio Perea        Date: 30-Sep-20

This script is intended to validate Positive response of service 0x2A which main function is to request the periodic transmission of data record values from the server by one or more periodicDataIdentifiers (PDID).


'''
from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):

    @classmethod
    def format_hex(cls, decimal):
        return hex(decimal).replace('0x','').upper()

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        
        if device_under_test == 'SCL':
            tools.popup.warning(
                title='Service 0x2A not supported',
                description='SCL does not support service 0x2A'
            )
            raise Warning('SCL does not support service 0x2A')

        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='0x2A',
            step_delay=0.25
        )     
        self.DID =  'F0 80'

        self.sec_levels = [
            '01', '03', '05', '09', '0B', '0D', '11', '13', '15'
        ]

        self.supported_range = {
            'MSM' : (240, 256), #192,
            'ARB' : (240, 256),
            'PTM' : (240, 256),
            'TCP':  (240, 256)
        }
        self.supported_DDDDI = [
            'F2 %s'%n for n in map(self.format_hex, range(
                self.supported_range[device_under_test][0],
                self.supported_range[device_under_test][1]
            )) # F2 XX -> F2 FF  ['F2 F0', 'F2 F1', 'F2 F2', 'F2 F3', 'F2 F4', 'F2 F5', 'F2 F6', 'F2 F7', 'F2 F8', 'F2 F9', 'F2 FA', 'F2 FB', 'F2 FC', 'F2 FD', 'F2 FE', 'F2 FF'] are 16 combinations                                                       
        ]

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()
    
    # Steps from 3 to 44 will be covered within 'test_001'
    def test_001(self, name='Positive Flow Define Single DDID By Identifier Session and Security Tests'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        self.step_counter = 2

        def step_preconditions(functional=False):
            #self.step_counter += 1
            test.preconditions(
                current_step='test_%s'%str(self.step_counter).rjust(3, '0'),
                functionalAddr=functional
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

                expected={
                    'response' : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
                }
            )
            self.step_counter += 1
            step_preconditions()
            test.step(
                step_title='Security Level %s - Send Key'%level,
                send_key=level,

                expected={
                    'response' : 'Positive'
                }
            )
        #                 F2 F0, F0 80
        def define_DDDDI(DDDDI, srcDataID):
            step_preconditions()
            test.step(
                step_title='Define DDDDI {0} by srcIdentifier {1}'.format(DDDDI, srcDataID),
                custom='2C 01 {0} {1} 01 01'.format(DDDDI, srcDataID),
                expected = {
                    'response': 'Positive'
                }
            )

        def read_PDID(PDID, speed, functional=False):
            step_preconditions(functional)
            test.step(
                step_title='Start PDID {0} at {1} rate'.format(PDID, speed),
                read_periodic_data_id=dict(
                    DDDID=PDID, rate=speed, timeout=10),

                expected={
                    'response': 'Positive',
                    'periodic_rate' : speed,
                    'periodic_data' : PDID
                }
            )

        def stop_PDID(PDID):
            step_preconditions()
            test.step(
                step_title='Stop PDID {}'.format(PDID),
                custom='2A 04 {}'.format(PDID),
                expected = {
                    'response': 'Positive'
                }
            )

        def tester_present():
            step_preconditions(functional=True)
            test.step(
                step_title='Start Tester Present',
                start_tester_present=True,

                expected={
                    'response': 'No response'
                }
            )

        self.step_counter = 3
        extended_session()              # 10 03

        self.step_counter = 4
        tester_present()                # 3E 80

        # Define all Periodic Identifiers   
        for DDDDI in self.supported_DDDDI:
            self.step_counter = 5             
            define_DDDDI( DDDDI, self.DID )   # 2C 01 F2 XX YY YY 01 01

        for DDDDI in self.supported_DDDDI:

            PDID = DDDDI[-2:]
            self.step_counter = 6
            read_PDID( PDID, speed='03')  # 2A 03 XX
            time.sleep(2.5)

            self.step_counter = 7
            stop_PDID(PDID)           # 2A 04 XX
            for lvl in self.sec_levels:
                self.step_counter += 1
                enter_security_level( lvl )

                self.step_counter += 1
                read_PDID( PDID, speed='03' )  # 2A 03 XX
                time.sleep(2.5)

                self.step_counter += 1
                stop_PDID( PDID )           # 2A 04 XX

            self.step_counter += 1
            extended_session()
        
    # FF FE FD are valid  FA is not valid
    def test_008(self, name='Read Data by PID - Send at fast rate - Multiple PDIDs'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID='FF FE', rate='03', timeout=10),

            expected={
                'response': 'Positive',
                'periodic_rate' : '03',
                'periodic_data' : 'FF FE'
            }
        )
    
    def test_009(self, name='Stop transmission of periodic data identifier'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2A 04',
            expected = {
                'response': 'Positive'
            }
        )

    def test_010(self, name='Read Data By PID - Send At Fast Rate - Functional Messaging'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID='FF', rate='03', timeout=10),

            expected={
                'response': 'Positive',
                'periodic_rate' : '03',
                'periodic_data' : 'FF'
            }
        )
    
    def test_011(self, name='Read Data By PID - Stop Sending - Functional Messaging'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='2A 04',
            expected = {
                'response': 'Positive'
            }
        )

