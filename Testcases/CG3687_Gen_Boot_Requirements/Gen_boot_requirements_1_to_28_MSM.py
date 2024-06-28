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
            excel_tab='Gen Boot Requirements'
        )      
        message = 'Please ensure you have a Green ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        
        self.test_status = {}

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()



    # Verify that the ECU transitions to the Boot Mode

    def test_001(self, name='Observe normal communication message is disabled'):
        time.sleep(2)
        test.preconditions(
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_001')

    def test_002(self, name='Verify that the ECU transitions to the Boot Mode'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'   : 'Positive',
                'data'       : '01 02 02 02'
            }
        )
        breakpoint()


    def test_003(self, name='Implement Pre-Programming Sequence'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response': 'Negative',
                'data'    : '12'
            }
        )
    
    def test_004(self, name='Implement Pre-Programming Sequence'):

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

    def test_005(self, name='Request Seed'):
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
    def test_006(self, name='Transition to programmingSession, Boot Mode'):

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

    def test_008(self, name='Request Download of Valid Signed App SW file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 fe 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_009(self, name='Transfer Data of Valid Signed App SW file'):
        time.sleep(0.5)
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

    def test_010(self, name='Request Transfer Exit'):
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
    def test_011(self, name='Update PSI'):

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

    # Verify that the App SW PSI is set to "Valid Programming Present" and Calibration Data PSI is NOT set to "Valid Programming Present" 
    def test_012(self, name='Read PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'    : 'Positive',
                'partialData' : '01 00 02' 
            }
        )
    
    # Verify that the PEC is set to "$0000 = Err_NoError"                                     
    def test_013(self, name='Read PEC'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F1',

            expected={
                'response'   : 'Positive',
                'data'       : '00 00'
            }
        )

    def test_014(self, name='Observe normal communication message is disabled'):
        # Power Supply - Turn OFF
        test.power_supply.output(False)
        print(__name__, 'Waiting 60 seconds while power supply is down')
        for i in reversed(range(60)): # This is just a countdown from 59 to 0 (60s = 1 min)
            print(i, end='  ', flush=True)
            time.sleep(1)
        test.power_supply.output(True)
        test.preconditions(
            step_info=info()
        )
        test.compare(test.normal_comm(), True, step='test_014')

    def test_015(self, name='Read PSI'):

        test.preconditions(            
            step_info=info()            
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'    : 'Positive',
                'partialData' : '01 00 02'
            }

        )

    def test_016(self, name='Request SendKey'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response'   : 'Negative',
                'data'       : '12'
            }
        )

    def test_017(self, name='Implement Pre-Programming Sequence'):

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

    def test_018(self, name='Security Access - Request key'):

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
    def test_019(self, name='Transition to programming session'):

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
    
    def test_020(self, name='Erase Memory'):

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

    def test_021(self, name='Request Download of Valid Signed Calibration Data file'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 A0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_022(self, name='Transfer Data of Valid Signed Calibration Data file'):

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

 
  # defaultSession - Security Level 0D
    def test_023(self, name='Request Transfer Exit'):

        test.preconditions(            
            step_info=info()            
        )

        test.step(
            step_title=name,
            custom= '37',

            expected={
                'response'   : 'Positive',
            }
        )

    def test_024(self, name='Repeat programming for multiple Calibration Data modules to successful completion as required'):
        test.preconditions(
            step_info=info()
        )
        test.compare(self.test_status.get('status_1'), True, step='test_024')

    # This step is not applicable to ECUs that use the in-house Bootloader
    def test_025(self, name='Update PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '31 01 02 09 02',

            expected={
                'response'   : 'Positive'
            }
        )
    
    #Verify that the App SW PSI is set to "Valid Programming Present" and Calibration Data PSI is set to "Valid Programming Present"
    def test_026(self, name='Read PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom = '22 F0 F0',

            expected={
                'response'   : 'Positive',
                'data'       : '01 00 02 00'
            }
        )
    # Verify that the PEC is set to "$0000 = Err_NoError"
    def test_027(self, name='Read PEC'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom = '22 F0 F1',

            expected={
                'response'   : 'Positive',
                'data'       : '00 00'
            }
        )
 
 
    # Transition to defaultSession, Application Mode
    def test_028(self, name='defaultSession '):

        test.preconditions(            
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive'
            }

        )

    def test_029(self, name='Observe normal communication message is enabled'):
        time.sleep(2)       # This delay is used for the ECU to send the corresponding CAN messages, at this point APP SW is enabled
        test.preconditions(
            step_info=info()
        )
        test.compare(False, test.normal_comm(), step='test_029') 

    # Verify that the ECU transitions to the Application Mode
    def test_030(self, name='Request a Download'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 80 00 00 00 7E 00',

            expected={
                'response'   : 'Negative',
                'data'       : '7F'
            }
        )
 