'''
        ** Warning !! **
    This script may no be updated to the latest CG3687 version
'''

from Testcases.TestClass import TestCase
from framework.shared_functions import tools  
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Gen_Boot_Requirements(unittest.TestCase):

    ''' Positive Flow Diagnostic Session Control Session and Security Tests '''
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Gen_Boot_Requirements'
        )      
        message = 'Please ensure you have APP SW flashed in your ECU'+\
                  '\nand make sure you have sent the provision keys'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        self.test_status = {}
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    # Verify that the ECU transitions to the Application Mode
    def test_001(self, name='Observe normal communication message is enabled'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.compare(test.normal_comm(), True, step='test_001')


    def test_002(self, name='Verify Application Mode'):
        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 A0 00 00 00 1E 00',

            expected={
                'response'   : 'Negative',
                'data'       :  '7F'
            }

        )

    def test_003(self, name='Implement Pre-Programming Sequence'):

        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,

            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',


            expected={
                'response'   : 'Positive',
                'dataLength':  31
            }
        )

    def test_005(self, name='Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_006(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control=True,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_007(self, name='Erase Memory'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 02',
            expected={
                'response'   : 'Positive'
            }
        )

    def test_008(self, name='Request Download of Valid Signed Calibration Data file Partition ID = 03'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 C0 00 00 00 3E 00',

            expected={
                'response'   : 'Negative',
                'data'       : '70'
            }
        )

    def test_009(self, name='Program Signed Calibration Data file, Partition ID = 02  to successful completion'):

        test.preconditions(
            step_info=info()
        )

        for i, packet in enumerate(Binary.packets_to_send(_binary_cal3)):

            if i == 0:
                packet_list = list(packet)
                packet_list[10:12] = '03'
                packet = ''.join(packet_list)
                test.step(
                    step_title=name,
                    custom = packet,
                    expected={
                        'response' : 'Positive'    
                    }
                )
            else:
                test.step(
                    step_title=name,
                    custom = packet,
                    expected={
                        'response' : 'Positive'   
                    }
                )


    # This step is not applicable to ECUs that use the in-house Bootloader
    def test_010(self, name='Update PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 02',

            expected={
                'response'   : 'Positive'
            }
        )

    # Transition to defaultSession, Application Mode
    def test_011(self, name='defaultSession '):

        test.preconditions(            
            step_info=info(),
            functionalAddr=True
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive'
            }

        )
