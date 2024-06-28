from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x36'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
        
    def test_001(self, name='Boot Mode'):
        # Begin -- Boot Mode preconditions
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
        test.preconditions(current_step='test_bootMode_Precondition')
        test.step(
            step_title='bootMode Precondition',
            request_seed='01',
            send_key='01'
        )
        test.step(
            step_title=name,
            custom='10 02'
        )
        # End -- Boot Mode preconditions 
        test.preconditions(
            step_info=info(),
            )             
        test.step(
            step_title=name,
            custom='31 01 FF 00 01',         
            expected={
                'response': 'Positive',
            }
        )  
        
    def test_002(self, name='Request download'):
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
    def test_003(self, name='Tranfer'): 
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
                    
    def test_004(self, name='Continue programming event to successful completion'):
        test.preconditions(            
            step_info=info()            
        )
        # time.sleep(20)  # add by KLQ
        test.step(
            step_title=name,
            custom='37',
            
            expected={
                'response'   : 'Positive',
            }
        )
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
        
        test.step(
            step_title=name,
            custom= '31 01 FF 00 02',
            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 FF 00'
            }
        )
        test.step(
            step_title=name,
            #Ex:   "34 00 44 00 00 c0 00 00" is the request to download.
            #                              "00 3E 00" is the current length of the motor cals file for MSM. -YG
            custom='34 00 44 00 00 a0 00 00 00 1E 00',

            expected={
                'response'   : 'Positive'
            }
        )
        time.sleep(0.5)
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
                'response'   : 'Positive',
            }

        )
        test.step(
            step_title=name,
            custom='31 01 02 09 02',

            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 02 09'
            }
        )
        
        test.step(
            step_title=name,
            custom= '31 01 FF 00 03',
            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 FF 00'
            }
        )
        test.step(
            step_title=name,
            #Ex:   "34 00 44 00 00 c0 00 00" is the request to download.
            #                              "00 3E 00" is the current length of the motor cals file for MSM. -YG
            custom='34 00 44 00 00 c0 00 00 00 3E 00',

            expected={
                'response'   : 'Positive'
            }
        )
        time.sleep(0.5)
        for packet in Binary.packets_to_send(_binary_cal2):
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
            custom='31 01 02 09 03',

            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 02 09'
            }
        )
   
        test.step(
            step_title=name,
            custom= '31 01 FF 00 04',
            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 FF 00'
            }
        )
        test.step(
            step_title=name,
            #Ex:   "34 00 44 00 00 60 00 00" is the request to download.
            #                              "00 3E 00" is the current length of the vehicle cals file for MSM. -YG
            custom='34 00 44 00 00 60 00 00 00 3E 00',

            expected={
                'response'   : 'Positive'
            }
        )
        time.sleep(0.5)
        for packet in Binary.packets_to_send(_binary_cal3):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
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
            custom='31 01 02 09 04',

            expected={
                'response'   : 'Positive',
                'partialData' : '71 01 02 09'
            }
        )

    def test_030(self, name='Transition Server to the defaultSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        ) 
        
        test.restart_communication()
    