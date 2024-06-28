
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random
from framework.drivers.Power_Supply.power_supply import *

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='Network Supervision'
        )

        ''' Device Under Test - Settings '''
        self.protected_message = list(pn_dict[device_under_test]['protected_messages'].keys())[0]
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    
    def test_001_1(self, name='%s :: 5s delay + Clear DTCs'%device_under_test):
        test.preconditions(
            step_info=info(),
 #           power_mode='RUN'
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_001_2(self, name='%s :: read DTCs - No DTCs set'%device_under_test):
        test.preconditions(step_info=info())
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        
        )

    def test_003(self, name='%s :: stop message transmission + 5s delay + read DTC - DTC is Set | '%device_under_test):
        # CAPL implementation stops message from being transmitted
        #Step 2
        test.canoe.set_envVariable(**dict({self.protected_message:1})) # Set to 1 - True
        
        time.sleep(6)
        test.preconditions(
            step_info=info()
        )
        #Step 3
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response':     'Positive',                
                'partialData':  '%s 2F'%self.DTC
            }
        )  
        
        # CAPL implementation stops message from being transmitted
        test.canoe.set_envVariable(**dict({self.protected_message:0})) # Set to 0 - False

    def test_005_1(self, name='%s :: DTC 5 seconds delay test '%device_under_test):
        time.sleep(6)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 2E'%self.DTC
            }
        )
    def test_005_2(self, name='%s :: 5s delay + Clear DTCs'%device_under_test):
        test.preconditions(
            step_info=info(),
 #           power_mode='RUN'
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_005_3(self, name='%s :: read DTCs - No DTCs set'%device_under_test):
        test.preconditions(step_info=info())
        time.sleep(5)
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        
        )

    def test_005_4(self, name='%s :: stop message transmission + 5s delay + read DTC - DTC is Set | '%device_under_test):
        # CAPL implementation stops message from being transmitted
        #Step 2
        test.canoe.set_envVariable(**dict({self.protected_message:1})) # Set to 1 - True
        
        time.sleep(6)
        test.preconditions(
            step_info=info()
        )
        #Step 3
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 09',
            expected={
                'response':     'Positive',                
                'partialData':  '%s 2F'%self.DTC
            }
        )  
        
        # CAPL implementation stops message from being transmitted
        test.canoe.set_envVariable(**dict({self.protected_message:0})) # Set to 0 - False

    def test_006(self, name='%s :: DTC 5 seconds delay test '%device_under_test):
        time.sleep(6)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 2E'%self.DTC
            }
        )
    def test_007(self, name='%s :: 1 Operation Cycle '%device_under_test):
        test.preconditions(
            step_info=info()
        )
        if not device_under_test in ['ARB', 'PTM']:
            test.canoe.power_panel('OFF')
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=0
            ) 
                        
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

        if not device_under_test in ['ARB', 'PTM']:
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=2
            ) # power mode = RUN
            test.canoe.power_panel('RUN')
        #time.sleep(15)              
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 28'%self.DTC
            }
        )

    def test_008(self, name='%s :: 39 Operation cycles '%device_under_test):
        for i in range(65):
            test.preconditions(current_step='Ignition %s'%str(i+1),)

            if not device_under_test in ['ARB', 'PTM']:
                test.canoe.power_panel('OFF')
                test.canoe.set_signal(
                    signal='SPMP_SysPwrModeAuth',
                    message='SysPwrMode_Prtctd_PDU',
                    value=0
                ) # power mode = OFF
                
            
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            
            #Wait until sleep current is reached.
            s_current=test.read_power_supply_current()
            i_current=float(s_current)
            while i_current > 0.02:         
                time.sleep(2)
                i_current=float(test.read_power_supply_current())
                print(i_current)
            time.sleep(3)    
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
#            while test.catch_error_frames(): # Re attempt to restart communication if required
#                test.canoe.set_envVariable(envVNMFStop=1)
#                test.canoe.set_envVariable(envVNMFSend=0)
#                time.sleep(1)
#                test.canoe.set_envVariable(envVNMFStop=0)
#                test.canoe.set_envVariable(envVNMFSend=1)
            if not device_under_test in ['ARB', 'PTM']:
                test.canoe.set_signal(
                    signal='SPMP_SysPwrModeAuth',
                    message='SysPwrMode_Prtctd_PDU',
                    value=2
                ) # power mode = RUN
                test.canoe.power_panel('RUN')
            
            time.sleep(15)
            test.step(
                step_title=name+str(i),
                custom='19 06 D6 11 00 FF',
                expected={
                    'response': 'Positive',
                }
            )

    def test_010(self, name='%s :: read DTCs - No DTCs set'%device_under_test):
        test.preconditions(
            step_info=info()
            )
        if not device_under_test in ['ARB', 'PTM']:
            test.canoe.power_panel('OFF')
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=0
            ) # power mode = OFF
            
        test.canoe.set_envVariable(envVNMFSend=0)
        test.canoe.set_envVariable(envVNMFStop=1)
        
        #Wait until sleep current is reached.
        s_current=test.read_power_supply_current()
        i_current=float(s_current)
        while i_current > 0.02:         
            time.sleep(2)
            i_current=float(test.read_power_supply_current())
            #print(i_current)
        time.sleep(3)    
        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)
#        while test.catch_error_frames(): # Re attempt to restart communication if required
#            test.canoe.set_envVariable(envVNMFStop=1)
#            test.canoe.set_envVariable(envVNMFSend=0)
#            time.sleep(1)
#            test.canoe.set_envVariable(envVNMFStop=0)
#            test.canoe.set_envVariable(envVNMFSend=1)
        time.sleep(15)            
        if not device_under_test in ['ARB', 'PTM']:
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=2
            ) # power mode = RUN
            test.canoe.power_panel('RUN')
        
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )
  

