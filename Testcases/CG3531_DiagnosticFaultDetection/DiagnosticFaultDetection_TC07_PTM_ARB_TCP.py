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
            writeTestResults=True,
            excel_tab='Diagnostic Fault Detection'
        )

        
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            raise Warning(__name__, 'This test case is only meant to be executed for PTM/ARB')

        ''' Device Under Test - Settings '''
        self.protected_message = random.choice(     # Pick random message to be tested
            list(pn_dict[device_under_test]['protected_messages'].keys())
        )
        self.DTC = pn_dict[device_under_test]['protected_messages'][self.protected_message]['DTC']

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    
    def test_004(self, name='%s :: Clear DTCs'%device_under_test):
        test.canoe.power_panel('RUN')
        time.sleep(5)
        test.preconditions(step_info=info())
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='%s :: stop message transmission + read DTC | '%device_under_test):
        # CAPL implementation stops message from being transmitted
        test.canoe.set_envVariable(**dict({self.protected_message:1}))
        time.sleep(6)
        test.preconditions(
            step_info=info(),
            
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 FF',
            expected={
                'response':     'Positive',                
                'partialData': '%s 2F'%self.DTC
            }
        )  

    def test_006(self, name='%s :: resumes message transmission + read DTC | '%device_under_test):
        # CAPL implementation stops message from being transmitted
        test.canoe.set_envVariable(**dict({self.protected_message:0}))
        time.sleep(2)
        test.preconditions(
            step_info=info(),            
        )
        test.step(
            step_title='{0} - {1}::{2}'.format(name, device_under_test, self.protected_message),
            custom='19 02 FF',
            expected={
                'response':     'Positive',                
                'partialData': '%s 26'%self.DTC
            }
        )  
