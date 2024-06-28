
# Calibrations automation pending ..
        
from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
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
            writeTestResults=True,
            excel_tab='Diagnostic Fault Detection'
            step_delay = 0.01
        )

        if device_under_test != 'MSM':
            raise Warning(__name__, 'This test case is only meant to be executed for MSM')

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    

    def test_004(self, name='%s :: No DTCs Set | '%device_under_test):
        input('Please make sure default calibrations are set in MSM Module')
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response':     'Positive'
            }
        )

    def test_005(self, name='%s :: Permanently DTC Set | '%device_under_test):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response':     'Positive',
                'partialData':  'F0 00 54 2F'
            }
        )

    def test_008(self, name='%s :: Permanently DTC Set | '%device_under_test):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response':     'Positive',
                'partialData':  'F0 00 54 2F'
            }
        )



    # Complete one (1) operation cycle
    def test_009(self, name='%s :: Read DTCs| '%device_under_test):
        test.canoe.set_envVariable(VehSpdAvgDrvnAuth_StopSend = 1) # Set to 1 - True
        time.sleep(6)                                              # Delay necessary to set the DTC
        test.canoe.set_envVariable(envVNMFSend=0)
        test.canoe.set_envVariable(envVNMFStop=1)
        print('Stoping NMF for .. ')
        for i in range(60):
            print(i, end='  ', flush=True)
            time.sleep(1)
        test.canoe.set_envVariable(envVNMFStop=0)
        test.canoe.set_envVariable(envVNMFSend=1)
        time.sleep(10) 
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response':     'Positive',
                'partialData':  'F0 00 54 2F'
            }
        )

    def test_010(self, name='%s :: 40 operation cycles permanently DTC test '%device_under_test):
        for i in range(39):
            print(__name__, 'Iteration %s'%str(i))
            test.step(
                step_title=name+str(i),
                custom='19 02 FF',
                expected={
                    'response': 'Positive',
                    'partialData': 'F0 00 54 FF'
                }
            )
            test.canoe.power_panel('OFF')
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=0
            ) # power mode = OFF
            test.canoe.set_envVariable(envVNMFSend=0)
            test.canoe.set_envVariable(envVNMFStop=1)
            for s in reversed(range(sleep_timeout)):
                # Wait for 'n' seconds until the module goes to sleep
                #  - Where 'n' = sleep_timeout integer value specified in config file
                print(s, end='  ', flush=True)
                time.sleep(1)
            test.canoe.set_envVariable(envVNMFStop=0)
            test.canoe.set_envVariable(envVNMFSend=1)
            while test.catch_error_frames(): # Re attempt to restart communication if required
                test.canoe.set_envVariable(envVNMFStop=1)
                test.canoe.set_envVariable(envVNMFSend=0)
                time.sleep(1)
                test.canoe.set_envVariable(envVNMFStop=0)
                test.canoe.set_envVariable(envVNMFSend=1)
            test.canoe.set_signal(
                signal='SPMP_SysPwrModeAuth',
                message='SysPwrMode_Prtctd_PDU',
                value=2
            ) # power mode = RUN
            test.canoe.power_panel('RUN')

    def test_011(self, name='%s :: Permanently DTC can not be cleared | '%device_under_test):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response':     'Negative',
                'data':         '22'
            }
        )