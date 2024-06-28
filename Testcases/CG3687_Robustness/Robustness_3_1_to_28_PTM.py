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
            '\nPlease standby and wait for prompts to popup\nand make sure you have a product intent SW.'
        print(__name__, message)
        tools.popup.warning(title='User input required',
                                description=message)
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()


    def test_001(self, name='Verify that the ECU transitions to the Boot Mode'):
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

    def test_003(self, name='Send Key'):

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

    def test_004(self, name='Transition to programmingSession'):

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

    def test_005(self, name='Erase Memory'):

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

        message = 'please disconnect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                            description=message)
        
        test.step(
            step_title=name,
            custom= '31 01 FF 00 01',
            expected={
                'response'   : 'No response'
            }
        )

    def test_006 (self, name= 'Re-connect ECU Ground'):
        message = 'please connect the ECU Ground and then press enter..'
        tools.popup.warning(title='Bootloader',
                                description=message)
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


    def test_007(self, name='Read PSI'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'    : 'Positive',
                'unexpected_response' : True,
                'partialData'       : '62 F0 F0 01 00 02 00' 
            }
        )  

    # Verify Application SW partition PSI value is set to "Valid Programming Present" and Calibration Data partition ID 02 PSI value is NOT set to  "Valid Programming Present" 

    def test_008(self, name='Implement Pre-Programming Sequence'):

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

    def test_009(self, name='Security Access - Request key'):

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

    def test_016(self, name='Read PSI'): 

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom = '22 F0 F0',

            expected={
                'response'   : 'Positive',
                'partialData'       : '62 F0 F0 01 00'
            }
        )
        # Verify Application SW partition PSI values are set to "Valid Programming Present"

    # Verify that the PEC is set to "$0000 = Err_NoError"
    def test_017(self, name='Read PEC'):

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

    def test_018(self, name='defaultSession '):

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

    def test_019(self, name= 'Interrupt ECU Ground (Disconnect the ECU Ground connector)'):
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

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': '00 '*30
            }
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 01',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
        )

        message = 'please disconnect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                                description=message)

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'No response'
            }
        )

    def test_020(self, name= 'Interrupt ECU Ground (Disconnect the ECU Ground connector)'):

        message = 'please connect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                                    description=message)
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

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': '00 '*30
            }
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 01',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_app, percentage = 50):
            test.step(
                step_title=name,
                custom = packet,
                expected={
                    'response'   : 'Positive'
                }
            )

        message = 'please disconnect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                                    description=message)

        for packet in Binary.packets_to_send(_binary_app, percentage = 50):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'No response'
                }
            )
            break

    def test_021(self, name= 'Interrupt ECU Ground (Disconnect the ECU Ground connector)'):
        message = 'please connect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                                    description=message)
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

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': '00 '*30
            }
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '31 01 FF 00 01',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 FE 00',

            expected={
                'response'   : 'Positive'
            }
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

        message = 'please disconnect the ECU Ground connector and then press enter..'
        tools.popup.warning(title='Bootloader',
                                    description=message)

        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'   : 'No response',
            }

        )
            