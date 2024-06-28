from Testcases.TestClass import TestCase
from framework.shared_functions import tools, ECU_info
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Gen_Boot_Requirements(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Proc Modes Details'
        )
        message = 'Please ensure you have a Green ECU and set "0" in error_frames in the config file'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Observe normal communication message is disabled'):
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )
        test.compare(True, test.normal_comm(), step='test_001')

    def test_002(self, name='Read PSI'):
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F0',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_003(self, name='Request Send Key'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response': 'Negative',
                'data'    : '12',
                'data_2'  : '7F'
            }
        )

    def test_004(self, name='Send any CAN Message '):
        # This is only to verify that ECU is Awake
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_004')

    def test_005(self, name='Send any CAN Message '):
        # This is only to verify that ECU is Awake
        time.sleep(5)
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_005')

    def test_006(self, name='Send any CAN Message '):
        # This is only to verify that ECU is Awake
        time.sleep(5)
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_006')

    def test_007(self, name='Send any CAN Message '):
        # This is only to verify that ECU is Awake
        time.sleep(5)
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_007')

    def test_008(self, name='Send any CAN Message '):
        # This is to verify that the ECU has transitioned to sleep mode
        time.sleep(10)
        test.preconditions(            
            step_info=info()
        )
        time.sleep(11)   # Time for the ASC log file be updated
        test.compare(True, test.catch_error_frames(), step='test_008')

    def test_009(self, name='Send any CAN Message '):
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_009')

    def test_010(self, name='Send any CAN Message '):
        time.sleep(15)
        test.preconditions(            
            step_info=info()
        )
        test.compare(True, test.normal_comm(), step='test_010')

    def test_011(self, name='Read BIS'):
        test.preconditions(            
            step_info=info()
        )

        test.step(
            step_title=name,
            custom = '22 F0 F2',
            expected={
                'response'   : 'Positive' 
            }

        )

    def test_012(self, name='Send any CAN Message '):
        time.sleep(5)
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

    def test_013(self, name='Send any CAN Message '):
        time.sleep(5)
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

    def test_014(self, name='Execute Successful Programming Event (only calibration partition)'):

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
                'response': 'Positive'
            }
        )

        test.step(
            step_title=name,
            request_seed='01',


            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            programming_session_control=True,

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

        for packet in Binary.packets_to_send(_binary_cal1):
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
                'response'   : 'Positive'
            }

        )
