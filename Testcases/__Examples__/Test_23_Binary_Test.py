'''

    Binary Test - Example

'''
from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest
from framework.shared_functions import device_under_test
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Test_UDS(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False          # Write on CG Report
        )
        self.DUT = device_under_test
        self.test_status = {}
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Implement Pre-Programming Sequence'):

        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )

        test.step(
            step_title=name,
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_002(self, name='Request Seed'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': '00 '*30
            }
        )
 
  # Boot mode
    def test_003(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_004(self, name='Erase Memory'):

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

    def test_005(self, name='Request Download of Valid Signed App SW file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_006(self, name='Transfer Data of Valid Signed App SW file'):
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

    def test_007(self, name='Request Transfer Exit'):
        test.preconditions(            
            step_info=info()            
        )
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'   : 'Positive',
            }

        )
    # Note: This step is not applicable to ECUs that use the in-house Bootloader
    def test_008(self, name='Update PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_009(self, name='Implement Pre-Programming Sequence'):

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
                'response'   : 'Positive'
            }
        )

    def test_010(self, name='Security Access - Request key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',
            

            expected={
                'response'   : 'Positive',
                'dataLength' :  31
            }
        )
 
  # Transition to programmingSession
    def test_011(self, name='Transition to programming session'):

        test.preconditions(            
            step_info=info()            
        )

        test.step(
            step_title=name,
            programming_session_control = True,

            expected={
                'response'   : 'Positive'
            }
        )
    
    def test_012(self, name='Erase Memory'):

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

    def test_013(self, name='Request Download of Valid Signed Calibration Data file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 a0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_014(self, name='Transfer Data of Valid Signed Calibration Data file'):

        test.preconditions(
            step_info=info()
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

        if device_under_test == 'MSM':
    
            test.preconditions(
                step_info=info()
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
        self.test_status.update({'status_1': test.attributes.get('status'), 'failure_cause_1': test.attributes.get('failure_cause')})