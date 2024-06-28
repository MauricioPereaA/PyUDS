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
            excel_tab='Robustness'
        )      
        message = 'This test requires user input to confirm behaviors.'+\
            '\nPlease standby and wait for prompts to popup.'
        print(__name__, message) 
        tools.popup.warning(title='User input required',
                                description=message)
        self.no_power = False
        self.power = True
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()
  
    def test_001(self, name='Implement Pre-Programming Sequence and request seed'):

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
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': '00 '*30
            }
        )

    def test_002(self, name='Send Key'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response': 'Positive'

            }
       )

    def test_003(self, name='Transition to programmingSession'):

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

    def test_005(self, name='Request Download of App SW'):

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
        test.power_supply.output(False)
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'No response'
            }
        )
        # Re-connect ECU power

    def test_006(self, name='Re-connect ECU Power'):
        test.power_supply.output(True)

        test.preconditions(
            step_info=info()
        )
        if test.read_power_supply_voltage() >= 9 and test.read_power_supply_voltage() < 16:
            test.compare(True, self.power, step='test_006')
        else:
            test.compare(True, self.no_power, step='test_006')

    #Verify PSI"    PENDING   xx is not equal to 0
    def test_007(self, name='Read PSI'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom = '22 F0 F0',

            expected={
                'response'   : 'Positive',
                'unexpected_response' : True,
                'partialData'       : '62 F0 F0 01 00' 
                                                       
            }
        )

    def test_008(self, name='Re-start the programming process'):

        test.preconditions(
            step_info=info()
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

    def test_009(self, name='Request Seed'):

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

    def test_010(self, name='Transition to programmingSession'):

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

    def test_011(self, name='Erase Memory'):

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

    def test_012(self, name='Request Download of App SW'):

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

    def test_013(self, name='Transfer Data of Valid Signed App SW file'):
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

    def test_014(self, name='Request Transfer Exit'):
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
    def test_015(self, name='Update PSI'):

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

    def test_016(self, name='Implement Pre-Programming Sequence'):

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

    def test_017(self, name='Request Seed'):

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

    def test_018(self, name='Transition to programmingSession, Boot Mode'):

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

    def test_019(self, name='Erase Memory'):

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

    def test_020(self, name='Request Download of Valid Signed App SW file'):

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
        message = 'Please disconnect the communication connector, then continue with the test.'
        tools.popup.warning(title='Bootloader', description=message)
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'No response'
            }
        )

    def test_021(self, name='Re-connect communication connector'):
        message = 'Please connect the communication connector, then continue with the test.'
        tools.popup.warning(title='Bootloader', description=message)
        test.preconditions(
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_021')        

     # Verify that the App SW PSI is set to "Valid Programming Present" and Calibration Data PSI is NOT set to "Valid Programming Present" 
    def test_022(self, name='Read PSI'): #PENDING

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'   : 'Positive',
                'unexpected_response' : True,
                'partialData'       : '62 F0 F0 01 00 02 00' 
                                                       
            }
        )

    def test_023(self, name='Implement Pre-Programming Sequence'):

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

    def test_024(self, name='Request Seed'):

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

    def test_025(self, name='Transition to programmingSession, Boot Mode'):

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

    def test_026(self, name='Erase Memory'):

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

    def test_027(self, name='Request Download of Calibration Data'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 a0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_028(self, name='Transfer Data of Calibration Data'):

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

    def test_029(self, name='Request Transfer Exit'):

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

   # This step is not applicable to ECUs that use the in-house Bootloader
    def test_030(self, name='Update PSI'):

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

    # Verify that the App SW PSI is set to "Valid Programming Present" and Calibration Data PSI is NOT set to "Valid Programming Present" 
    def test_031(self, name='Read PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'    : 'Positive',
                'partialData' : '62 F0 F0 01 00 02 00' 
            }
        )
    
    # Verify that the PEC is set to "$0000 = Err_NoError"                                     
    def test_032(self, name='Read PEC'):

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

    # Transition to defaultSession
    def test_033(self, name='defaultSession '):

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






 



    

            