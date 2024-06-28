
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 5-Nov-20
#Modified by: Mauricio Perea        Date: 18-Dec-20
from framework.shared_functions import device_under_test, tools    
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest,time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        if device_under_test is 'SCL':
            tools.popup.warning(__name__, 'SCL does not support service 0x2F')
            raise Warning('SCL does not support Service 0x2F')
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x2F'
        )

        self.io_dids = {
            'ARB': {
                'multiple_tester'       : '50 29',
                'unsupported_default'   : '43 14',
                'incorrect_length'      : '50 29',
                'out_of_range'          : '50 29',
                'conditions_not_correct_single': '4B 5C',
                'conditions_not_correct_mutiple': '4B 5C',                
                'invalid_parameter'     : 'FF',
                'con_parameter'         : '00', #not used                
                'mask'                  : '06'                
            },
            'PTM': {
                'multiple_tester'       : '50 29',
                'unsupported_default'   : '43 14',
                'incorrect_length'      : '51 82',#51 82-->50 20
                'out_of_range'          : '51 82',#51 82-->50 20
                'out_of_range_2'        : '50 20',#51 82-->50 20
                'security_access_denied': '51 82',#add
                'conditions_not_correct_mutiple': '51 82',    #49 5F --> 44 5D mutiple parameter
                'conditions_not_correct_single': '50 20',     #49 5F --> 44 5D  single parameter
                'conditions_not_correct': '4B 5C',
                'invalid_parameter'     : 'FF',
                'parameter'             : 'FF FF',                
                'less_parameter'        : 'FF', 
                'sec_parameter'         : 'FF FF', #for 5182 
                'con_parameter'         : '00 09', # 1E 05 -->00 09for 5182 condition                    
                'more_mask'             : '00 00',  
                'mask'                  : 'FF'  #00 -->FF

            },
            'MSM': {
                'multiple_tester'       : '49 5F',     
                'unsupported_default'   : '49 5F',
                'incorrect_length'      : '4B 53',#495F -->4B 53
                'out_of_range'          : '44 5D',     #49 5F --> 49 10 #This part need to check
                'out_of_range_2'        : '49 5E',               
                'conditions_not_correct_mutiple': '44 5D',     #49 5F --> 44 5D mutiple parameter
                'conditions_not_correct_single': '49 5F',     #49 5F --> 44 5D  single parameter
                'security_access_denied': '48 FB',#add
                'invalid_parameter'     : 'FF', #for 495E
                'parameter'             : 'FF FF FF FF ', #for 4B53 right parameter    
                'less_parameter'        : 'FF', #for 4B53 less parameter
                'sec_parameter'         : 'FF FF', #for 48FB    
                'con_parameter'         : '04', #for 445D condition                
                'more_mask'             : '00 00',     
                'mask'                  : '08'                         
                
            }
            
        }

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_002(self, name='Pyrotechnic'):
        # test.preconditions(
        #     step_info=info(),
            
        # )
        # test.step(
        #     step_title=name,
        #     custom=''
        # )
        pass

    def test_003(self, name='Pyrotechnic'):
        # test.preconditions(
        #     step_info=info(),
            
        # )
        # test.step(
        #     step_title=name,
        #     custom=''
        # )
        pass

    def test_004(self, name='<Transition Server to defaultSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 01',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='serviceNotSupportedInActiveSession - 0x7F_DefaultSession'):
        did = self.io_dids[device_under_test]['unsupported_default']
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F %s 00'%did,
            expected={
                'response': 'Negative',
                'data': '7F'
            }
        )

    def test_006(self, name='<Transition Server to extendedSession>'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_007(self, name='<Activate TesterPresent>'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='3E 80',
            expected={
                'response': 'No response'
            }
        )
        
    def test_008(self, name='requestOutOfRange - 0x31_1'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F FF FF 00',
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_009(self, name='requestOutOfRange - 0x31_2'):
        did = self.io_dids[device_under_test]['out_of_range']
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F %s 05'%did,
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )
    #need to confirm we cannot get NRC 31 with any did
    def test_010(self, name='requestOutOfRange - 0x31_3'):	
    
        # Pre-condition step
        if device_under_test in ['PTM']:
            # For DID '5182', Sec Lvl 09 is required
            test.preconditions(current_step='sec lvl precondition' ,
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',1])
            #test.step(step_title='sec lvl 09 precondition',
                        #request_seed='09', send_key='09')
                        
        # Pre-condition step
        did = self.io_dids[device_under_test]['out_of_range']
        para1 = self.io_dids[device_under_test].get('invalid_parameter')
        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 00 {}'.format(did, para1),  
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )
        
    def test_011(self, name='requestOutOfRange - 0x31_ControlParameter_01'):	
    
        # Pre-condition step
        if device_under_test in ['PTM']:
            # For DID '5182', Sec Lvl 09 is required
            test.preconditions(current_step='sec lvl precondition' ,
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',1])
            #test.step(step_title='sec lvl 09 precondition',
                        #request_seed='09', send_key='09')
                        
        # Pre-condition step
        did = self.io_dids[device_under_test]['out_of_range']
        para1 = self.io_dids[device_under_test].get('invalid_parameter')
        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 01 {}'.format(did, para1),  
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_012(self, name='requestOutOfRange - 0x31_ControlParameter_02'):	
    
        # Pre-condition step
        if device_under_test in ['PTM']:
            # For DID '5182', Sec Lvl 09 is required
            test.preconditions(current_step='sec lvl precondition' ,
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',1])
            #test.step(step_title='sec lvl 09 precondition',
                        #request_seed='09', send_key='09')
                        
        # Pre-condition step
        did = self.io_dids[device_under_test]['out_of_range']
        para1 = self.io_dids[device_under_test].get('invalid_parameter')
        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 02 {}'.format(did, para1),  
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )

    def test_013(self, name='requestOutOfRange - 0x31_ControlParameter_03'):	
    
        # Pre-condition step
        if device_under_test in ['PTM']:
            # For DID '5182', Sec Lvl 09 is required
            test.preconditions(current_step='sec lvl precondition' ,
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',1])
            #test.step(step_title='sec lvl 09 precondition',
                        #request_seed='09', send_key='09')
                        
        # Pre-condition step
        did = self.io_dids[device_under_test]['out_of_range']
        para1 = self.io_dids[device_under_test].get('invalid_parameter')
        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 03 {}'.format(did, para1),  
            expected={
                'response': 'Negative',
                'data': '31'
            }
        )
        
          
    def test_015(self, name='securityAccessDenied - 0x33_1'):
        if device_under_test in 'ARB':
            #Not applicable to ARB, all IO Controls executed all sec levels:
            return 0
        # Pre-condition step
        if device_under_test in ['PTM']:
            # For DID '5182', Sec Lvl 09 is required
            test.preconditions(current_step='sec lvl precondition')
            test.step(step_title='quit lvl 09 precondition',
                        extended_session_control=True)
        # Pre-condition step        
        did = self.io_dids[device_under_test]['security_access_denied']
        mask = self.io_dids[device_under_test].get('mask')           
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 00'.format(did),
            #custom='2F {} 00 {} '.format(did, mask),            
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_016(self, name='securityAccessDenied - 0x33_2'):
        if device_under_test in 'ARB':
            #Not applicable to ARB, all IO Controls executed all sec levels:
            return 0        
        did = self.io_dids[device_under_test]['security_access_denied']
        mask = self.io_dids[device_under_test].get('mask')      
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 01'.format(did),
            #custom='2F {} 01 {} '.format(did, mask),            
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )


    def test_017(self, name='securityAccessDenied - 0x33_3'):
        if device_under_test in 'ARB':
            #Not applicable to ARB, all IO Controls executed all sec levels:
            return 0
        did = self.io_dids[device_under_test]['security_access_denied']
        mask = self.io_dids[device_under_test].get('mask')      
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 02'.format(did),
            #custom='2F {} 02 {} '.format(did, mask),            
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )

    def test_018(self, name='securityAccessDenied - 0x33_4'):
        if device_under_test in 'ARB':
            #Not applicable to ARB, all IO Controls executed all sec levels:
            return 0
        did = self.io_dids[device_under_test]['security_access_denied']
        para3 = self.io_dids[device_under_test]['sec_parameter']
        mask = self.io_dids[device_under_test].get('mask')           
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='2F {} 03 {} {}'.format(did, para3, mask),
            expected={
                'response': 'Negative',
                'data': '33'
            }
        )
        
        
    def test_020(self, name='conditionsNotCorrect - 0x22_1'):
        did = self.io_dids[device_under_test]['conditions_not_correct_single'] #change
        mask = self.io_dids[device_under_test].get('mask')
        if device_under_test in ['PTM']:
            test.preconditions( step_info=info(),
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',0])
        if device_under_test in ['MSM']:
	        test.preconditions(
	            step_info=info(),
	            signal=[
	                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
	                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
	            ]
	        )
        if device_under_test in 'ARB':
            test.preconditions(
                step_info=info()
            )        
        test.step(
            step_title=name,
            custom='2F %s 00'%did, 
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )

    def test_021(self, name='conditionsNotCorrect - 0x22_2'):
        did = self.io_dids[device_under_test]['conditions_not_correct_single'] #change
        mask = self.io_dids[device_under_test].get('mask')
        if device_under_test in ['PTM']:
            test.preconditions( step_info=info(),
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',0])
        if device_under_test in ['MSM']:
	        test.preconditions(
	            step_info=info(),
	            signal=[
	                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
	                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
	            ]
	        )
        if device_under_test in 'ARB':
            test.preconditions(
                step_info=info()
            )            
        test.step(
            step_title=name,
            custom='2F %s 01'%did, 
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
        
    def test_022(self, name='conditionsNotCorrect - 0x22_3'):
        did = self.io_dids[device_under_test]['conditions_not_correct_single'] #change
        mask = self.io_dids[device_under_test].get('mask')
        if device_under_test in ['PTM']:
            test.preconditions( step_info=info(),
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',0])
        if device_under_test in ['MSM']:
	        test.preconditions(
	            step_info=info(),
	            signal=[
	                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
	                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
	            ]
	        )
        if device_under_test in 'ARB':
            test.preconditions(
                step_info=info()
            )            
        test.step(
            step_title=name,
            custom='2F %s 02'%did, 
            expected={
                'response': 'Negative',
                'data': '22'
            }
        )
        
    def test_023(self, name='conditionsNotCorrect - 0x22_4'):
        did = self.io_dids[device_under_test]['conditions_not_correct_mutiple'] #changge
        mask = self.io_dids[device_under_test].get('mask')
        para4 = self.io_dids[device_under_test]['con_parameter']
        if device_under_test in ['PTM']:
            test.preconditions( step_info=info(),
                               signal=['RCIP_RrClsrMtnCtlParmEnblAuth','SrlDat2_Prtctd_PDU',0])
            test.step(step_title='sec lvl 09 precondition',
                        request_seed='09', send_key='09')        
        if device_under_test in ['MSM']:
	        test.preconditions(
	            step_info=info(),
	            signal=[
	                'VSADP_VehSpdAvgDrvnSrcAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000,
	                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 2
	            ]
	        )
        if device_under_test in 'ARB':
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='2F {} 03 {}'.format(did, mask),
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )                
        else:
            test.step(
                step_title=name,
                custom='2F {} 03 {} {}'.format(did, para4, mask),
                expected={
                    'response': 'Negative',
                    'data': '22'
                }
            )