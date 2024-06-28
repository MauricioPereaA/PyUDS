from framework.shared_functions import device_under_test, tools, pn_dict
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random

test = TestCase() 
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Diagnostic Fault Detection ==# 
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='Diagnostic Fault Detection'
        )

        if device_under_test not in ['ARB', 'PTM', 'TCP'] :
            raise Warning(__name__, 'This test case is only meant to be executed for ARB/PTM/TCP')

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    
    
    def test_004(self, name='Generate Vehicle conditions to set multiple DTCs'):
    
        test.preconditions(
            step_info=info(),
            power_mode='RUN'
        )
        
        #Non-continuous DTCs are the ones triggered by event. Continous DTCs such as Loss of Comm or Invalid Data Signal DTCs cannot be used for this test.
        
        if device_under_test is 'ARB':
            #For ARB the only non-continuous DTCs suitable for this test are under and over voltage thresholds DTCs. 
            #These two are mutually exclusive so only one DTC: under-voltage is used for this test.
            test.set_dtc_condition(underVoltage=True)
            test.canoe.set_envVariable(underVoltageCondition=1)
            time.sleep(6)
        

    def test_005(self, name='%s :: stop message transmission to set 3 lost of comm DTCs + read DTC information | '%device_under_test):
    
        test.preconditions(step_info=info())
        
        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 2F'
                    }
                ) 
            
        if device_under_test is 'PTM':
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(CGM_CAN4_PDU10_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(ExtRrClsrRelReqAuth_StopSend = 1) # Set to 1 - True

            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Status byte of the DTCs C14600 / C10100 / D61100  is 2F')
            test.compare(True, prompt, step='test_005')


        if device_under_test is 'TCP':
            # CAPL implementation stops message from being transmitted
            # Only setting DTC for TCP Module, subfunctions 03 and 04 are NA
            test.canoe.set_envVariable(BkupSysPwrModeAuth_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(PDU_9080_StopSend = 1) # Set to 1 - True

            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Status byte of the DTCs C14600 / D61100 / C14000 is is 2F')
            test.compare(True, prompt, step='test_005')
            

    def test_006_1(self, name='%s :: Read reportDTCSnapshotIdentification  | '%device_under_test):
    
        if device_under_test is 'ARB':
        
            test.preconditions(
                step_info=info(),            
            )
            
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 01'
                }
            )

        if device_under_test is 'PTM':
            test.preconditions(
                step_info=info(),            
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the DTCs C14600 / D61100 / C14000 are reported with its SnapshotRecordNumber')
            test.compare(True, prompt, step='test_006')


    def test_006_2(self, name='%s :: Read reportDTCSnapshotRecordByDTCNumber  | '%device_under_test):
    
        if device_under_test is 'ARB':
        
            test.preconditions(
                step_info=info(),               
            )
            
            test.step(
                step_title=name,
                custom='19 04 F0 03 16 01',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 2F 01'
                }
            )

        if device_under_test is 'PTM':
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 04 C1 46 00 01',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the DTCs C14600 / D61100 / C14000 are reported with its SnapshotRecordNumberByDTCNumber')
            test.compare(True, prompt, step='test_006_2')
            
            
    def test_007(self, name='%s :: Read reportDTCRetractedDataRecordByDTCNumber  | '%device_under_test):
    
        if device_under_test is 'ARB':
        
            test.preconditions(
                step_info=info(),  
            )
            
            test.step(
                step_title=name,
                custom='19 06 F0 03 16 FF',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 2F'
                }
            )

        if device_under_test is 'PTM':
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 C1 46 00 01',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its RetractedDataRecordByDTCNumber')
            test.compare(True, prompt, step='test_007')

        if device_under_test is 'TCP':
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 C1 46 00 01',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its RetractedDataRecordByDTCNumber')
            test.compare(True, prompt, step='test_007')

    def test_009(self, name='%s :: Remove DTCs conditions | '%device_under_test):

        test.preconditions(
            step_info=info(),
        )
            
        if device_under_test is 'ARB':
            test.power_supply_reset_default()
            test.canoe.set_envVariable(underVoltageCondition=0)
            time.sleep(6)            
            
            
    def test_010(self, name='%s :: Clear DTCs  | '%device_under_test):
    
        if device_under_test is 'ARB':

            test.preconditions(
                step_info=info(),
                power_mode='OFF'                
            )
            
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }
            )       

        if device_under_test is 'PTM':
            test.canoe.set_envVariable(CGM_CAN4_PDU10_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(ExtRrClsrRelReqAuth_StopSend = 0) # Set to 1 - True

            time.sleep(1)
            test.preconditions(
                step_info=info(),            
            )
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }
            )

        if device_under_test is 'TCP':
            test.canoe.set_envVariable(BkupSysPwrModeAuth_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(PDU_9080_StopSend = 0) # Set to 1 - True

            time.sleep(1)
            test.preconditions(
                step_info=info(),            
            )
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }               
            )


    def test_011(self, name='%s :: Read DTC information and check status byte of the tested DTCs is $50| '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )
        test.step(
            step_title=name,
            custom='19 02 50',
            expected={
                'response':     'Positive'
            }
        )

        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 02 50',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 50'
                }
            )

        if device_under_test in ['PTM', 'TCP']:
        
            test.step(
                step_title=name,
                custom='19 02 50',
                expected={
                    'response':     'Positive'
                }
            )       
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 is 50')
            test.compare(True, prompt, step='test_011')

   
    def test_012(self, name='%s :: Read reportDTCSnapshotRecordByDTCNumber  | '%device_under_test):
        test.preconditions(
            step_info=info(),
            
        )

        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 04 F0 03 16 01',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 50'
                }
            )        

        if device_under_test is 'PTM':
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 is 50')
            test.compare(True, prompt, step='test_012')

    def test_013(self, name='%s :: Read reportDTCRetractedDataRecordByDTCNumber  | '%device_under_test):
        test.preconditions(
            step_info=info(),
            
        )

        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 06 F0 03 16 FF',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 50'
                }
            )        

        if device_under_test in ['PTM', 'TCP']:
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 is 50')
            test.compare(True, prompt, step='test_013')
            

    def test_014(self, name='Generate Vehicle conditions to set multiple DTCs'):
    
        test.preconditions(
            step_info=info(),
            power_mode='RUN'
        )
        
        #Non-continuous DTCs are the ones triggered by event. Continous DTCs such as Loss of Comm or Invalid Data Signal DTCs cannot be used for this test.
        
        if device_under_test is 'ARB':
            test.set_dtc_condition(underVoltage=True)
            test.canoe.set_envVariable(underVoltageCondition=1)
            time.sleep(6)
            
            
    def test_015(self, name='%s :: Set multiple DTCs and read supported DTCs  | '%device_under_test):
    
        if device_under_test is 'ARB':

            test.preconditions(
                step_info=info(),
                
            )
            
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 2F'
                    }
                ) 
            
        if device_under_test is 'PTM':
            test.canoe.set_envVariable(CGM_CAN4_PDU10_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(ExtRrClsrRelReqAuth_StopSend = 1) # Set to 1 - True

            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Status byte of the DTCs C14600 / D61100 / C14000 is 2F')
            test.compare(True, prompt, step='test_015')

        if device_under_test is 'TCP':
            # CAPL implementation stops message from being transmitted
            # Only setting DTC for TCP Module, subfunctions 03 and 04 are NA
            test.canoe.set_envVariable(BkupSysPwrModeAuth_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 1) # Set to 1 - True
            test.canoe.set_envVariable(PDU_9080_StopSend = 1) # Set to 1 - True

            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Status byte of the DTCs C14600/ D61100 / C14000 is 2F')
            test.compare(True, prompt, step='test_015')
            


    def test_016_1(self, name='%s :: Read reportDTCSnapshotIdentification  | '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )
        
        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive',                
                    'partialData': 'F0 03 16 01'                
                }
            )  

        if device_under_test is 'PTM':
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its SnapshotRecordNumber')
            test.compare(True, prompt, step='test_016')


    def test_016_2(self, name='%s :: Read reportDTCSnapshotRecordByDTCNumber  | '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )
        
        if device_under_test is 'ARB':  
        
            test.step(
                step_title=name,
                custom='19 04 F0 03 16 01',
                expected={
                    'response':     'Positive',                
                    'partialData': 'F0 03 16 2F 01'
                }
            )  

        if device_under_test is 'PTM':
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its SnapshotRecordNumber')
            test.compare(True, prompt, step='test_016_2')
            
            
    def test_017(self, name='%s :: Read reportDTCRetractedDataRecordByDTCNumber  | '%device_under_test):
    
        test.preconditions(
            step_info=info(),
        )
        
        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 06 F0 03 16 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'F0 03 16 2F'
                }
            )

        if device_under_test in ['PTM', 'TCP']:
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its RetractedDataRecordByDTCNumber')
            test.compare(True, prompt, step='test_017')


    def test_018(self, name='%s :: Remove DTCs conditions | '%device_under_test):

        test.preconditions(
            step_info=info(),            
        )
            
        if device_under_test is 'ARB':
            test.power_supply_reset_default()
            test.canoe.set_envVariable(underVoltageCondition=0)
            time.sleep(6)               
          
          
    def test_020(self, name='%s :: Remove Vehicle conditions and clear DTCs  | '%device_under_test):
    
        if device_under_test is 'ARB':
            test.preconditions(
                step_info=info(),
                power_mode='OFF'
            )
            
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }             
            )
            
        if device_under_test is 'PTM':
            test.canoe.set_envVariable(CGM_CAN4_PDU10_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(ExtRrClsrRelReqAuth_StopSend = 0) # Set to 1 - True

            time.sleep(1)
            test.preconditions(
                step_info=info(),            
            )
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }
            )

        if device_under_test is 'TCP':
            test.canoe.set_envVariable(BkupSysPwrModeAuth_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 0) # Set to 1 - True
            test.canoe.set_envVariable(PDU_9080_StopSend = 0) # Set to 1 - True

            time.sleep(1)
            test.preconditions(
                step_info=info(),            
            )
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                    'response':     'Positive'
                }         
            )
            
    def test_021(self, name='%s :: Read DTC information and check status byte of the tested DTCs is $50| '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )

        if device_under_test is 'ARB':
            test.step(
                step_title=name,
                custom='19 02 50',
                expected={
                    'response':     'Positive',
                    'partialData': 'F0 03 16 50'
                }
            )
        
        if device_under_test in ['PTM', 'TCP']:
            test.step(
                step_title=name,
                custom='19 02 50',
                expected={
                    'response':     'Positive',
                }
            )
            
            
    def test_022(self, name='%s :: Read reportDTCSnapshotRecordByDTCNumber  | '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )
        
        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 04 F0 03 16 01',
                expected={
                    'response':     'Positive',                
                    'partialData': 'F0 03 16 50'
                }
            ) 

        if device_under_test is 'PTM':
            prompt = tools.popup.ask(title=name, description='verify that the DTCs C1 46 00 / D6 11 00 / C1 40 00 are reported with its SnapshotRecordNumberByDTCNumber ($50)')
            test.compare(True, prompt, step='test_022')
            
            
    def test_023(self, name='%s :: Read reportDTCRetractedDataRecordByDTCNumber  | '%device_under_test):
    
        test.preconditions(
            step_info=info(),
            
        )

        if device_under_test is 'ARB':
        
            test.step(
                step_title=name,
                custom='19 06 F0 03 16 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'F0 03 16 50'
                }
            )
            
        if device_under_test in ['PTM', 'TCP']:
            prompt = tools.popup.ask(title=name, description='verify that the Status byte of the DTCs C14600/ D61100 / C14000 are reported with its RetractedDataRecordByDTCNumber')
            test.compare(True, prompt, step='test_023')
            
            