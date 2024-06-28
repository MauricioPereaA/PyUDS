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
            excel_tab='0x34'
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
#======================NRC13===============================    
    def test_003(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34',
            expected={
                'response': 'Negative',
                'data': '13'
            }
        ) 
    '''    
    def test_004(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 2'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )  
    def test_005(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 3'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )   
    def test_006(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 4'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )  
    def test_007(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 5'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        ) 
    def test_008(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 6'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )   
    def test_009(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 7'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )  
    def test_010(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 8'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )  
    def test_011(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 9'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        )  
    def test_012(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 10'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 fe', 

            expected={
                'response': 'Negative',
                'data': '13'
            }
        ) 
    '''   
    def test_004(self, name='incorrectMessageLengthOrInvalidFormat - 0x13 (minimum length check) -- 11'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 fe 00 00',

            expected={
                'response': 'Negative',
                'data': '13'
            }
        ) 
#======================NRC31===============================         
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
        test.restart_communication()             
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
    def test_006(self, name='invalid dataFormatIdentifier - 0x31 (out of range) -- 1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 FF 44 00 01 00 00 00 15 fe 00',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        )       
    def test_007(self, name='invalid memory address - 0x31 (out of range) -- 2'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 FF FF FF FF 00 15 fe 00',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        ) 
    
#============invalid memory size should be tested after reflash ECU
    def test_008(self, name='invalid memory size - 0x31 (out of range) -- 3'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 FF FF FF',

            expected={
                'response': 'Negative',
                'data': '31'
            }
        ) 
#======================NRC22===============================        
    def test_009(self, name='Boot Mode'):
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
        test.restart_communication()            
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
            custom='34 00 44 00 01 00 00 00 15 fe 00',

            expected={
                'response'   : 'Positive' #74 20
            }
        )              
    def test_011(self, name='data size mismatch - 0x22 (condition not correct) -- 1'):             
        test.preconditions(
            step_info=info(),
            )          
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 fe 00',
            expected={
                'response': 'Negative',
                'data': '22'
            }
        ) 
    '''
#===========================NRC70 maybe software test==========================
    def test_021(self, name='restart boot'):
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
        test.restart_communication()             
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
            custom='31 01 FF 00 02',         
            expected={
                'response': 'Positive',
            }
        )  
    def test_023(self, name='Request download'):  
        test.step(
            step_title=name,
            custom='34 00 44 00 01 00 00 00 15 fe 00',
           expected={
                'response': 'Negative',
                'data': '70' 
            }
        )   
    '''
#======================full===============================                
    def test_012(self, name='Erase Application SW Memory'):
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
        test.restart_communication()             
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
        time.sleep(20)#add
        test.step(
            step_title=name,
            custom='37',

            expected={
                'response'   : 'Positive'
            }

        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )
        
        # CAL 1 loder
        test.step(
            step_title=name,
            custom= '31 01 FF 00 02',
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='34 00 44 00 00 A0 00 00 00 1E 00',

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
        
        # CAL2--loader
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
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 03',

            expected={
                'response'   : 'Positive'
            }
        )       
        
        # CAL3--loader
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
        
        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 04',

            expected={
                'response'   : 'Positive'
            }
        )
        
        # verfify the bootloader result

    
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
        # this step can loader all the files  