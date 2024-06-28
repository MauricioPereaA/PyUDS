
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
#Modified by: Mauricio Perea        Date: 30-Sep-20
        
from framework.shared_functions import read_supported_dids    
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest,time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x22'
        )
        self.DIDs = filter(
            lambda k: 'PROGRAMMING' in read_supported_dids[k], 
            read_supported_dids.keys()
        )
        self.DID2s = filter(
            lambda k: 'PROGRAMMING' in read_supported_dids[k], 
            read_supported_dids.keys()
        )
        

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()


    def test_001(self, name='Read supported DID in BootMode'):
        # Begin -- Boot Mode preconditions
        test.preconditions(current_step='BootMode_Precondition')
        test.step(
            step_title='BootMode Precondition',
            extended_session_control=True,
            dtc_settings=False,
            communication_control=False,
            request_seed='01',
            send_key='01'
        )
        test.step(
            step_title = 'Boot_Mode',
            programming_session_control = True
        )
        # End -- Boot Mode preconditions

        test.preconditions(
            step_info=info(),            
        )
        time.sleep(1)
        test.step(
            step_title=name,
            custom='22 F1 80',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_001_2(self, name='Read supported DIDs in BootMode'):
        test.preconditions(
                    step_info=info(),
                    functionalAddr=True               
                    )

        for DID in self.DIDs:
            test.step(
                step_title=name,
                custom='22 ' + DID,

                expected={
                    'response'   : 'Positive'
                }
            )
            #time.sleep(0.5)

    def test_002(self, name='Read supported DID in BootMode with functional address'):
        test.preconditions(
            step_info=info(),         
            functionalAddr=True   
        )
        test.step(
            step_title=name,
            custom='22 F1 80',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_002_2(self, name='Read supported DIDs in BootMode with functional address'):
        test.preconditions(
                    step_info=info(),
                    functionalAddr=True               
                    )
        for DID2 in self.DID2s:     #for DID in self.DIDs --> for DID2 in self.DID2s:


            test.step(
                step_title=name,
                custom='22 ' + DID2,

                expected={
                    'response'   : 'Positive'
                }
            )
    
            #time.sleep(0.5)

    def test_003(self, name='Read two supported DIDs in BootMode'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='22 F1 80 F1 81',

            expected={
                'response'   : 'Positive'
            }
        )

    def test_004(self, name='Read two supported DIDs in BootMode with functional address'):
        test.preconditions(
            step_info=info(),
            functionalAddr=True   
        )
        test.step(
            step_title=name,
            custom='22 F1 80 F1 81',

            expected={
                'response'   : 'Positive'
            }
        )

