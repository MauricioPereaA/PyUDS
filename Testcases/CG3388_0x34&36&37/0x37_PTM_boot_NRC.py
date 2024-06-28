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
            excel_tab='0x37'
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
    def test_002(self, name='Erase Memory'):        
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
        
 
    def test_004(self, name='service $34, RequestDownload, is not active - 0x24 (requestSequenceError) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37',
            expected={
                'response': 'Negative',
                'data': '24'
            }
        )  
        
    def test_005(self, name='Boot Mode'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control= True,
            expected={
                'response'   : 'Positive'
            }
        )          
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
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 0e 7e 00',

            expected={
                'response'   : 'Positive' #74 20
            }
        ) 
        time.sleep(0.5)

    def test_006(self, name='service $36 is not completed'):
        test.preconditions(
            step_info=info()
        )
        for packet in Binary.packets_to_send(_binary_app, percentage = 10):
            test.step(
                step_title=name,
                custom = packet,
                expected={
                    'response': 'Positive'
                }
            )  
                 
    def test_007(self, name='service $36 is not completed - 0x24 (requestSequenceError)'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response': 'Negative',
                'data': '24'
            }
        )           
    def test_008(self, name='Boot Mode'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control= True,
            expected={
                'response'   : 'Positive'
            }
        )          
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
        
    def test_009(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )         
    
    def test_010(self, name='Boot Mode'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control= True,
            expected={
                'response'   : 'Positive'
            }
        )          
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

        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 0e 7e 00',

            expected={
                'response'   : 'Positive' #74 20
            }
        ) 
        time.sleep(0.5)

#change binary after 0x810
    def test_011(self, name='an error when programming a memory location'):
        time.sleep(0.5)

        test.preconditions(
            step_info=info()
        )

        for packet in Binary.packets_to_send(_binary_cal2):
            test.step(
                step_title=name,
                custom = packet,
                
                expected={
                    'response' : 'Positive'    # Expected response
                }
            )                

    def test_012(self, name='Transfer Data of Valid Signed App SW file'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response': 'Negative',
                'data': '72'
            }
        )  
    

            
    def test_013(self, name='Erase Application SW Memory'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            default_session_control= True,
            expected={
                'response'   : 'Positive'
            }
        )         
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
            step_info=info()
        )
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
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 0e 7e 00',

            expected={
                'response'   : 'Positive' #74 20
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
                'response'   : 'Positive'
            }
        )         
        test.step(
            step_title=name,
            custom='34 00 44 00 00 80 00 00 00 7E 00', # changed by KLQ

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
        test.step(
            step_title=name,
            custom= '31 01 02 09 02',

            expected={
                'response'   : 'Positive'
            }
        )
                
    
    def test_023(self, name='Transition Server to the defaultSession'):

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