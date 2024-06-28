
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

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

        self.bus_off_DTC = {
            'ARB': 'C0 75 00',
            'PTM': 'C0 79 00',
            'MSM': 'C0 79 00',
            'SCL': 'C0 75 00',
            'TCP': 'C0 7B 00'
        }

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001_1(self, name='wait +5 seconds and Clear DTCs'):
        test.preconditions(
            step_info=info()
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
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'data': 'FF'
            }
        )

    def test_003(self, name='wait 5s + Read DTCS - Should be set'):
        test.canoe.set_envVariable(envBusOff=1)
        time.sleep(1)
        test.canoe.set_envVariable(envBusOff=0)
        time.sleep(1)    
        
        print(__name__, 'Now wait for 4s')
        
        test.canoe.set_envVariable(envVNMFStop=1)
        test.canoe.set_envVariable(envVNMFSend=0)
        time.sleep(1)
        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)
        time.sleep(7)
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 09',
            expected={
                'response': 'Positive',
                'partialData': '%s 2E'%self.bus_off_DTC[device_under_test]
            }
        )

    def test_004(self, name='Repeat the test for all the subnets supported by ECU'):
        pass
