'''
Modified by Mauricio Perea
Date: 13 July 2020
This script was added new feature in the precondition sw_prog_state it verify the sw status 

'''        
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from framework.shared_functions import device_under_test, tools
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='RID 0209_FF00'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    #TestCase 1 is only a precondition at CG so it is included
    #in Test Case 2 hence you will no see TC 1 file

    def test_004(self, name='Transition to extendedSession, Application Mode'):
        test.preconditions(
            step_info=info(),
            mec_zero=False,
            sw_prog_state='Full',
            sbat=False
        )
        test.step(
            step_title=name,
            extended_session_control=True,
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_005(self, name='Activate TesterPresent'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_006(self, name='Start Routine Update PSI'):
        test.preconditions(
            step_info=info(),
            functionalAddr=False
        )
        test.step(
            step_title=name,
            custom='31 01 02 09',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_007(self, name='Start Routine Update PSI'):
        test.preconditions(
            current_step='test_007_bootMode_Precondition'
        )

        test.step(
            step_title='bootMode Precondition',
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,
            request_seed='01',
            send_key='01',   

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom= '10 02',

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
        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='34 00 44 00 00 80 00 00 00 1E 00', #Calibration file address / size ARB r162.1

                expected={
                    'response'   : 'Positive'
                }
            )
        
        else: #substitute condition here for corresponding ECU
        
            test.step(
                step_title=name,
                custom='34 00 44 00 01 00 00 00 0e 7e 00',

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


    def test_008(self, name='Start Routine Update PSI Application SW Partition ID'):
        test.preconditions(
            step_info=info(),
        )
        test.step(
            step_title=name,
            custom='31 01 02 09 01',
            expected={
                'response'   : 'Negative',
                'data'       : '22'
            }
        )
        
        prompt = tools.popup.ask(title=name, description='Please use DPS to program calibrations and execute RID_0209_FF00_2_2')