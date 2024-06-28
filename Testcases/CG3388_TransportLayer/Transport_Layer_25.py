
            # This is and autogenerated test case using PyUDS Test Builder v0.3 #

'''  CG2020

Modified by: Mauricio Perea        Date: 30-Sep-20

'''              
from framework.shared_libs.transport_layer import TransportLayer
from framework.shared_functions import tools, LogsPath
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
            excel_tab='Transport Layer'
        )
        self.TransportLayer = TransportLayer(LogsPath+'\\TraceLog.asc')
        
    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='Transport Layer 25'):

        # *CHECKED* - Check-box
        test.canoe.set_envVariable(TransportLayer25=1)

        # *PUSH* - Run selected test cases
        test.canoe.set_envVariable(RunTransportLayerTC=1)
        time.sleep(0.75)
        test.canoe.set_envVariable(RunTransportLayerTC=0)
        test.canoe.set_envVariable(TransportLayer25=0)

        # Wait for Transport Layer Test Case to be finished
        print('Please wait until TC is completed...')
        time.sleep(18) #15-->18 need time dealy to compare all content
        test.canoe.stop()
        test.compare(self.TransportLayer.test_case_25(), True, 
                        step='test_001') 

    def test_002(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 4), True, 
                        step='test_002') 
    def test_003(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 5), True, 
                        step='test_003') 
    def test_004(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 6), True, 
                        step='test_004') 
    def test_005(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 7), True, 
                        step='test_005') 
    def test_006(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 8), True, 
                        step='test_006') 
    def test_007(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 9), True, 
                        step='test_007') 
    def test_008(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 10), True, 
                        step='test_008') 
    def test_009(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 11), True, 
                        step='test_009') 
    def test_010(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 12), True, 
                        step='test_010') 
    def test_011(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 13), True, 
                        step='test_011') 
    def test_012(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 14), True, 
                        step='test_012') 
    def test_013(self, name='Transport Layer 25'):
        test.compare(self.TransportLayer.test_case_25(invalid_flow_status = 15), True, 
                        step='test_013') 