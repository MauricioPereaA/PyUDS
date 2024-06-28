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
        ''' Device Under Test - Settings '''
        self.protected_message = list(pn_dict[device_under_test]['protected_messages'].keys())[0]
        
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']
        self.dtc_status_mask = '2F' if device_under_test in ['MSM', 'PTM', 'ARB', 'TCP'] else '29'

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_005_1(self, name='%s :: stop message transmission + read DTC - DTC is not Set | '%device_under_test):
        # CAPL implementation stops message from being transmitted
        test.canoe.power_panel('RUN')
        test.set_dtc_condition(overVoltage=True)
        time.sleep(6)
        test.preconditions(
            step_info=info(),
            
        )

        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',

            expected={
                'response':     'Positive',                
                'partialData': 'F0 03 17 2F'
            }
        )

    def test_005_2(self, name='%s :: read All supported DTCs'%device_under_test):
        test.preconditions(step_info=info())
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 0A',
            expected={
                'response': 'Positive',
                'partialData': 'F0 03 17 2F'
            }
        )

    def test_006(self, name='%s :: Clear DTCs'%device_under_test):
        test.preconditions(step_info=info())
        test.power_supply_reset_default()
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )
            

    #Snapshot Record:

    if device_under_test in ['ARB', 'PTM']:


        def test_008_1(self, name='Read DTC'):
            test.set_dtc_condition(overVoltage=True)
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive',
                    'partialData': '59 03 F0 03 17 01'

                }
            )

        def test_008_2(self, name='Read DTC'):
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 04 F0 03 17 01',
                expected={
                    'response':     'Positive'
                }
            )
            
        def test_009(self, name='Remove DTC Conditions'):
            test.power_supply_reset_default()
            time.sleep(6)

        def test_010_1(self, name='Read DTC'):
            test.set_dtc_condition(underVoltage=True)
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive',
                    'partialData': '59 03 F0 03 17 01 F0 03 16 01'

                }
            )

        def test_010_2(self, name='Read DTC'):
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 04 F0 03 16 01',
                expected={
                    'response':     'Positive'
                }
            )

        def test_011(self, name='Remove Vehicle Settings B'):
            test.power_supply_reset_default()
            time.sleep(6)

        def test_012_1(self, name='Read DTC'):
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1)
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response':     'Positive',
                    'partialData': '59 03 F0 03 17 01 F0 03 16 01 D6 11 00 01'

                }
            )

        def test_012_2(self, name='Read DTC'):
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 04 D6 11 00 01',
                expected={
                    'response':     'Positive'
                }
            )



        def test_014(self, name='wait +5 seconds and Clear DTCs'):
            test.power_supply_reset_default()
            test.preconditions(
                step_info=info(),
            )
            time.sleep(5)
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                'response': 'Positive'
            }
        )

        #Extended Data Record
        def test_020(self, name='%s :: stop message transmission and NMF + read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            #Perform sleep-wakeup:
            test.canoe.power_panel('OFF')
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)
                
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(3)  
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1)
            time.sleep(10)                                              # Delay necessary to set the DTC
            
            #Step 20
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 01',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 01'
                }
            ) 
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 12 bytes')
            test.compare(True, prompt, step='test_020')

        def test_021(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 02',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 02'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 8 bytes')
            test.compare(True, prompt, step='test_021')


        def test_022(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title='{0} - {1}::{2}'.format(name, device_under_test, 'VehSpdAvgDrvnAuth_StopSend'),
                custom='19 06 D6 11 00 03',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 03'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 8')
            test.compare(True, prompt, step='test_022')

        def test_023(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 16 bytes')
            test.compare(True, prompt, step='test_023')
            

        def test_024_1(self, name='Clear DTCs'):
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0) # Set to 0 to resume the message transmission
            time.sleep(5)
            test.canoe.power_panel('RUN')
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


        def test_024_2(self, name='Read DTCs'):
            time.sleep(10)                               # This delay is to let the diagnostic test to run, and be completed
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': '59 02 FF'
                }
            ) 
            
        def test_024_3(self, name='Disable message - Read DTCs'):
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1)
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            )
        
        def test_024_4(self, name='Enable message - Read DTCs'):
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0)
            time.sleep(5)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2E'
                }
            )
            
        def test_024_5(self, name='Disable message - Read DTCs'):
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1)
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            )     
            
        def test_024_6(self, name='Power OFF - Read DTCs'):
            test.canoe.power_panel('OFF')
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'               
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp updates, Occurrence counter = 0 or 1, Aging Cycle Counter = 0')
            test.compare(True, prompt, step='test_024')            

        def test_025_1(self, name='Enable Message - sleep - wake - Read DTCs'):
            # CAPL implementation stops message from being transmitted

            test.preconditions(
                step_info=info(),
                
            )
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0) 
            time.sleep(7)
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)

            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(15)
            prompt = tools.popup.ask(title=name, description='Make D6 11 00 28 happen')

            test.canoe.power_panel('RUN')
            time.sleep(6)    
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 28'
                }
            ) 
           
        def test_025_2(self, name='Disable Message - Read DTCs'):
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1) 
            time.sleep(6)                               # This delay is to let the diagnostic test to run, and be completed

            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            )            
        def test_025_3(self, name='Power OFF - Read DTCs'):
            test.canoe.power_panel('OFF')
            time.sleep(6)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'               
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp does not update, Occurrence counter = 1 or 2, Aging Cycle Counter = 0')
            test.compare(True, prompt, step='test_025') 

        def test_026(self, name='sleep - wake - Power ON - OFF  - Read DTCs'):
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)

            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)
                
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            test.canoe.power_panel('RUN')
            time.sleep(6)                               # This delay is to let the diagnostic test to run, and be completed
            test.canoe.power_panel('OFF')
            time.sleep(3)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp does not update, Occurrence counter = 2 or 3, Aging Cycle Counter = 0')
            test.compare(True, prompt, step='test_026')
            
        def test_027_1(self, name='sleep - wake - Power ON - Read DTCs'):
            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 0)
            time.sleep(3)
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            #print('Stoping NMF for .. ')
            #for i in range(31):
            #    print(i, end='  ', flush=True)
            #    time.sleep(1)
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)            
            
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            test.canoe.power_panel('RUN')
            time.sleep(6)                               # This delay is to let the diagnostic test to run, and be completed

            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                    'partialData': 'D6 11 00 28'
                }
            )
            
        def test_027_2(self, name='Power OFF - Read DTCs'):
            test.canoe.power_panel('OFF')
            time.sleep(3)

            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp does not update, Occurrence counter = 3, Aging Cycle Counter = 1 or 0')
            test.compare(True, prompt, step='test_027')
            
        def test_028(self, name='sleep - wake - Power ON - OFF  - Read DTCs'):
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)
                
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            test.canoe.power_panel('RUN')
            time.sleep(10)                               # This delay is to let the diagnostic test to run, and be completed
            test.canoe.power_panel('OFF')
            time.sleep(3)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp does not update, Occurrence counter = 3, Aging Cycle Counter = 2 or 1')
            test.compare(True, prompt, step='test_028')
            
        def test_029_1(self, name='sleep - wake - Power ON - Disable - Read DTCs'):
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)
                
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            test.canoe.power_panel('RUN')

            test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1)
            time.sleep(6)
 
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 02 09',
                expected={
                    'response':     'Positive',
                    'partialData': 'D6 11 00 2F'
                }
            )
            
        def test_029_2(self, name='Power OFF - Read DTCs'):
            test.canoe.power_panel('OFF')
            time.sleep(3)

            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Timestamp does not update, Occurrence counter = 3 or 4, Aging Cycle Counter = 0')
            test.compare(True, prompt, step='test_029')           
            
            
            
            
    if device_under_test is 'TCP':



        def test_014(self, name='wait +5 seconds and Clear DTCs'):
            test.power_supply_reset_default()
            test.preconditions(
                step_info=info(),
            )
            time.sleep(5)
            test.step(
                step_title=name,
                custom='14 FF FF FF',
                expected={
                'response': 'Positive'
            }
        )

        def test_017(self, name='%s :: stop message transmission and NMF + read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 1) # Set to 1 - True
            time.sleep(6)                                              # Delay necessary to set the DTC
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            print('Stoping NMF for .. ')
            for i in range(30):
                print(i, end='  ', flush=True)
                time.sleep(1)
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(10)                               # This delay is to let the diagnostic test to run, and be completed
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 01',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 01'
                }
            ) 
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 12 bytes')
            test.compare(True, prompt, step='test_017')

        def test_018(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 02',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 02'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 8 bytes')
            test.compare(True, prompt, step='test_018')


        def test_019(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title='{0} - {1}::{2}'.format(name, device_under_test, 'VehSpdAvgDrvnAuth_StopSend'),
                custom='19 06 D6 11 00 03',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F 03'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 8')
            test.compare(True, prompt, step='test_019')

        def test_020(self, name='%s :: Read reportDTCExtendedDataRecordByDTCNumber | '%device_under_test):
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            )
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 16 bytes')
            test.compare(True, prompt, step='test_020')
            

        def test_021_1(self, name='%s :: stop message transmission + read DTC - DTC is not Set | '%device_under_test):
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 0) # Set to 0 to resume the message transmission
            time.sleep(1)
            test.canoe.power_panel('RUN')
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            print('Stoping NMF for .. ')
            for i in range(30):
                print(i, end='  ', flush=True)
                time.sleep(1)
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(1)
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 28'
                }
            )

        def test_021_2(self, name='%s :: stop message transmission + read DTC - DTC is not Set | '%device_under_test):
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 16 bytes and verify that the timestamp and ocurrence counter are not updated and Aging Cycle Counter are updated')
            test.compare(True, prompt, step='test_021_2')

        def test_022_1(self, name='%s :: stop message transmission + read DTC - DTC is not Set | '%device_under_test):
            # CAPL implementation stops message from being transmitted
            test.canoe.set_envVariable(VehSpdAvgDrvn_Auth_PDU_StopSend = 1) # Set to 1 - True
            time.sleep(6)                                               # Delay necessary to set the DTC
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            print('Stoping NMF for .. ')
            for i in range(30):
                print(i, end='  ', flush=True)
                time.sleep(1)
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(10)                               # This delay is to let the diagnostic test to run, and be completed
            test.preconditions(
                step_info=info(),
                
            )
            test.step(
                step_title=name,
                custom='19 06 D6 11 00 FF',
                expected={
                    'response':     'Positive',                
                    'partialData': 'D6 11 00 2F'
                }
            ) 

        def test_022_2(self, name='%s :: stop message transmission + read DTC - DTC is not Set | '%device_under_test):
            prompt = tools.popup.ask(title=name, description='Please verify that the Length of the response is 16 bytes and verify that the timestamp / ocurrence counter are not updated and DTC Aging Cycle Counter is reset to 0')
            test.compare(True, prompt, step='test_022_2')






