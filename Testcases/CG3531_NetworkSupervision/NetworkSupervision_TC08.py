
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
from dcps import BK9115
from os import environ
import pyvisa
from framework.drivers.Power_Supply.power_supply import *
import unittest, time, tools


test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            step_delay=0.001,
            writeTestResults=True,
            excel_tab='Network Supervision'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001_1(self, name='wait +5 seconds and Clear DTCs'):
        test.preconditions(
            step_info=info(),
        #    power_mode='RUN'
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_001_2(self, name='read DTCs 1 - NO DTCs SET'):
        test.preconditions(
            step_info=info()
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )

    def test_002(self, name='change voltage to < 9v + read DTCs 2 + wait 5s + bus off condition + read DTCs'):
        test.preconditions(
            step_info=info()
        )
        # Power supply - Set underVoltage condition
        test.set_dtc_condition(underVoltage=True)
        test.canoe.set_envVariable(underVoltageCondition=1)
        
        print(__name__, 'Please wait for 5 seconds')
        time.sleep(6)

        # Set Bus OFF DTC
        test.canoe.set_envVariable(envBusOff=1)
        time.sleep(1)
        test.canoe.set_envVariable(envBusOff=0)
        time.sleep(1)    
        #Remove BusOff condition:
        test.canoe.set_envVariable(envVNMFStop=1)
        test.canoe.set_envVariable(envVNMFSend=0)
        time.sleep(1)
        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)
        
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )

    def test_003_1(self, name='return voltage to normal + create bus condition + read DTCs every 200 ms for 10 times'):
        test.preconditions(
            step_info=info()            
        )
        time.sleep(2)
        # Power supply - Return voltage to normal
        test.power_supply_reset_default()
        test.canoe.set_envVariable(underVoltageCondition=0)
        
        # Set Bus OFF DTC and clear within 4secs
        test.canoe.set_envVariable(envBusOff=1)
        time.sleep(0.2)
        test.canoe.set_envVariable(envBusOff=0)
        time.sleep(1)    
        
        #Remove BusOff condition: 
        test.canoe.set_envVariable(envVNMFStop=1)
        test.canoe.set_envVariable(envVNMFSend=0)
        time.sleep(0.5)
        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)
        
        #Read DTCs every 200ms for 10 times (2seconds)
        test.canoe.set_envVariable(envReadingPeriod=200)
        time.sleep(0.1)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
        time.sleep(2.2)
        test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')

    def test_003_2(self, name='read DTCs - Check is not SET YET'):
        test.preconditions(
            step_info=info()
        )
        time.sleep(4)
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )
        prompt = tools.popup.ask(title=name, description='Please check all replies to 19 02 09 are 59 02 FF (No DTCs Set)')
        test.compare(True, prompt, step='test_003_2')        