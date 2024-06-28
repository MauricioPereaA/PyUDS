
            # This is and autogenerated test case using PyUDS Test Builder v0.3 #
'''
    TestScript intended to perform CG3388 Tab MultiTester
'''
'''  CG2020
Author: Mauricio Perea
Modified by: Mauricio Perea        Date: 30-Sep-20

'''              
from framework.shared_libs.Multiple_Tester import MultiTester
from framework.shared_functions import tools, LogsPath, ECU_info, tools, device_under_test
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== PyUDS - Autogenerated Test Case Template ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Multiple Tester & NRC 21'
        )
        self.MultiTester = MultiTester(LogsPath+'\\TraceLog.asc')
        
    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
     
    def test_033(self, name='NRC21 3'):

        # *CHECKED* - Check-box
        test.canoe.set_envVariable(MultiTester10=1)

        # *PUSH* - Run selected test cases
        test.canoe.set_envVariable(MultiTester=1)
        time.sleep(0.75)
        test.canoe.set_envVariable(MultiTester=0)
        test.canoe.set_envVariable(MultiTester10=0)

        # Wait for Transport Layer Test Case to be finished
        print('Please wait until TC is completed...')
        time.sleep(5)
        test.canoe.stop()
        test.compare(self.MultiTester.test_case_009(), True, 
                        step='test_033')