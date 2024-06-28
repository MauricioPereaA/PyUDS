'''

     ** Test Template ** 

'''
print('-- PyUDS --')
print('This security access method got Deprecated. Please run Test_8 for new method')
#from Testcases.TestClass import TestCase
#from inspect import stack as info
#import time
#import unittest
#
#test = TestCase()
#
#class Test_PyUDS_SecurityLevels(unittest.TestCase):
#    
#    @classmethod
#    def setUpClass(self):
#        ''' Initialize test case '''
#        test.begin(
#            test_info=info(),
#            writeTestResults=False # Write on CG Report
#        )
#
#        self.supported_lvls = {
#            '01', '03', '09', '0B', '0D', '11', '05', '13', '15'
#        }
#
#    @classmethod
#    def tearDownClass(self):
#        ''' End test case'''
#        test.end()
#
#    def test_001(self, name='Test All Security Levels'):
#    
#        for lvl in self.supported_lvls:
#
#            test.preconditions(
#                step_info=info(),
#                functionalAddr=False
#            )
#
#            test.step(
#                step_title='{0} - Security Level {1}'.format(name, lvl),
#                send_key=lvl
#            )