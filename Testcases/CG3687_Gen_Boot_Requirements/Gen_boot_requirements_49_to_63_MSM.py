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
        test.compare(False, test.normal_comm(), step='test_001')

    def test_002(self, name='Verify Application Mode'):
        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

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
                'response': 'Positive',
                'unexpected_response' : True,
                'data': '00'*31
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
            custom= '31 01 FF 00 01',
            expected={
                'response'   : 'Positive'
            }
        )

    #Verify that the App SW PSI is set to "Programming is Invalid" and Calibration Data PSI is NOT set to "Valid Programming Present"
    def test_008(self, name='Read PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '22 F0 F0',
            expected={
                'response'   : 'Positive',
                'partialData' : '01 02 02' 
            }
        )

    def test_009(self, name='Request Download of Valid Signed Calibration Data file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Negative',
                'data'       : '70'
            }
        )

    # Program Signed Application SW and Signed Calibration Data to successful completion
    def test_010(self, name='Program Signed Application SW and Signed Calibration Data to successful completion'):

        test.preconditions(
            step_info=info()
        )

        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
                }
            )

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'   : 'Positive',
            }
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 02',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 a0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_cal1):
            test.step(
                step_title=name,
                custom = packet,
                
                expected={
                    'response' : 'Positive'    # Expected response
                }
            )

        test.step(
            step_title=name,
            custom= '37',

            expected={
                'response'   : 'Positive',
            }
        )

    
        test.step(
            step_title=name,
            custom= '31 01 FF 00 03',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 c0 00 00 00 3E 00',

            expected={
                'response'   : 'Positive'
            }
        )

        for packet in  Binary.packets_to_send(_binary_cal2):
            test.step(
                step_title=name,
                custom = packet,
                
                expected={
                    'response' : 'Positive'    # Expected response
                }
            )

        test.step(
            step_title=name,
            custom= '37',

            expected={
                'response'   : 'Positive',
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 04',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 60 00 00 00 3E 00',

            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_cal3):
            test.step(
                step_title=name,
                custom = packet,
                
                expected={
                    'response' : 'Positive'    # Expected response
                }
            )

        test.step(
            step_title=name,
            custom= '37',

            expected={
                'response'   : 'Positive',
            }

        )

    # This step is not applicable to ECUs that use the in-house Bootloader
    def test_011(self, name='Update PSI'):

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
    def test_012(self, name='defaultSession '):

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
