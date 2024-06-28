'''

     ** Provision Keys ** 

'''

from Testcases.TestClass import TestCase
from inspect import stack as info
import time
import unittest

test = TestCase()

class Test_UDS(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=False,  # Write on CG Report - Enable / Disable
            debug=False              # Write Actual response and expected in Report for Debug
        )
		
        self.keys = [
            '02000000000000000000000000000000551BAFA3B95A64DF9B40B8FD17A47433E1C944E918F22054B9E6B065A83E73283EC4F4B2F370F74352FFBDB683BE82DB49',  
            '0300000000000000000000000000000066E9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BD5A121354B550577B26426A09DB73288F', 
            '0400000000000000000000000000000077E9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BD381A0D2EDF21E9BC82BAC028FD7FE8C9',
            '0500000000000000000000000000000088E9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BD4089925F4A0EEC46EB61FD064287825B', 
            '0600000000000000000000000000000099E9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BDFD74EB85023814322B32779A9D18A301',  
            '07000000000000000000000000000000AAE9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BD34F0BA495E58ECBEB0A05BCB063588FF',  
            '08000000000000000000000000000000BBE9714CB7A2D72EB9ECFE4753E095E54F4FA23D8872112486117871ADF45A44BD33DC7469BB9AC1927469AC907A6B0997',  
            '09000000000000000000000000000000CC858967FDF0F59179026B1891F94FD37B42115446E29DC13729C574B63461CD7491E98658FE5F34FAA03463A7666171BF'
		]
    @classmethod
    def tearDownClass(self):
        test.end()

    def test_001(self, name='ProvisionKeys - RID 0200'):
        test.preconditions(      
            step_info=info()
        )

        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
            start_tester_present=True,
            request_seed='01',
            send_key='01'
        )
		
        for key in self.keys:
            test.step(
                step_title='Send keys',
                start_routine=['02 00', key],

                expected={
                    'response':'Positive'
                }
            )


    def test_002(self, name='Delete SBAT & set MEC = 0'):
        
        test.step(
            step_title='Sec Lvl 01',
            extended_session_control=True,
			start_tester_present=True,
            request_seed='01',
            send_key='01'
        )
        test.preconditions(      
            step_info=info()
            #sbat=False,
            #mec_zero=True
        )
        
        test.step(
            step_title='Transition to Extended Session',
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )