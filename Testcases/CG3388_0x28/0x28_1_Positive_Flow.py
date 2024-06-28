'''
    TestScript intended to perform CG3388 Tab 0x28 -- 1. Positive Flow
'''
'''
Author: Ricardo Montes

Modified by: Manuel Medina     Date: 17-Jun-20
Modified by: Mauricio Perea        Date: 30-Sep-20
Modified by: Mauricio Perea        Date: 13-Jan-20
This script is intended to validate positive response of service 0x28 which main function is to switch on/off the transmission and/or the reception of certain messages of (a) server(s) (e.g. application communication messages)..



'''

            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
from framework.shared_functions import tools           
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
            writeTestResults=True,
            excel_tab='0x28'
        )

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_003(self, name='Transition Server to extendedSession'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='Activate TesterPresent'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={
                'response': 'No response'
            }
        )

    def test_005(self, name='disable Rx And Tx extendedSession Physical Messaging'):
        test.canoe.set_envVariable(TransmitInOFFInfinite=1)
        time.sleep(2)#set for reminding OFF mode
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )

    
    def test_006(self, name='disable Rx And Tx extendedSession Physical Messaging'):
        
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 03 F1',
            expected={
                'response': 'Positive'
            }
        )
        
     #add by zqt 28 00 F1    
        
        
    '''    
    def test_007(self, name='disable Rx And Tx extended Session'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )
    '''
    def test_008(self, name='Transition Server to extendedSession'):
        test.preconditions(
            step_info=info(),
            sbat=False, # Clear SBAT
            mec_zero=True
        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive'
            }
        )
    def test_009(self, name='disable Rx And Tx extendedSession Physical Messaging'):
        test.canoe.set_envVariable(TransmitInOFFInfinite=1)
        time.sleep(2)#set for reminding OFF mode
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='28 03 01',
            expected={
                'response': 'Positive'
            }
        )  
    def test_010(self, name='enable Rx And Tx extendedSession Physical Messaging'):
        
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 00 01',
            expected={
                'response': 'Positive'
            }
        ) 
    def test_011(self, name='enable Rx And Tx extendedSession Physical Messaging'):
        
        test.preconditions(
            step_info=info(),
            functionalAddr=True
        )
        test.step(
            step_title=name,
            custom='28 00 F1',
            expected={
                'response': 'Positive'
            }
        )
        
        
        
        