'''

     ** Test Template Example ** 

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

    @classmethod
    def tearDownClass(self):
        test.end()

 # Assuming MEC > 0
    def test_001(self, name='Pre-Requisites - SBAT'):
        valid_key = '0301005B4D534D000000000043414E4F452044495641204543554944426F647900000000000000000000000007000000000000000000B4169DAEEC3646EC594A288E37B6FAEF88AE90169904D909D3EF61FBD51A9B6B537FA47B74FD782799B14F8F19353A98B46E77F84848C9CDD7794CC58A4481248BAB1EFD8BD117A082B8DD3506824CF632918FECE932488D28355E4B758F915AB410C1A21CFC2B6F70FB8365620F6A05B31912435F3F7B03ECEA59E4460AB867E730888953301E5FD2274B6CF56ABE7FDA90B33A555099995B7F1855DDC5006B57B2C692772F01BDA270ACB2454EEE4B9E9AC92F53DA2C23D6F92DFE2A43A069BDEEE952E2CA743959ACAC9B84A6B0322A80D5FF16853526A1F358C0262338D198D3873CCCA6C04BA79AA29AA1C81F0243DAF7DD2B5EFF6671D130044AA1D58728BB947F42C357F36ED69BF7355AFDCB8109F8E69E6C2C63E5C4E7E56A44A822E3AE4ECE7DB318D5684A2B6AFBB3406C86A78CA0377230DA2C53520AD92BBD7F4AE62B26FA2FD84C22881BD9CCF7C3229ECE6C67B953EFC412078A88B4009B5B10A1E65470BFE092B341AE5F63C2F61495EB038E064F3071B14AEFB5DFFCEEF573A365AC8EBD0FAF2CD10CE6BE25F9EC93F3A040A5C23C5F1066CA59DDA681DEAE1A675007A3687FA082F5E39B8E481EA04C1BAAEB509C7DC2F0BD388D1E45CB6A4254029B356CA40CDDC0D7EB34AB19E8AC1310C9EEC9C9D840C7556490AFBC926927C071A158E2B209F1899C438A6CE68A335C1AB40AADC7438158731329C46B37BE1C76EF649918FA67E816D724A494DC5C8D20084C059DC3F085D0262D08A7CBBAF5E80DC0DF01281348FEC5F26AB35299DD406B4B0E44386AD4D6789F9EE47B7D764F2EB47F5DF8B8FFE66168FCE331215AC4EE4A1E0B7951377B54BA0E990A946EBEC246EA767DCA8B7AAB7730E96CF872478003706BE157BC547025D68EF312D59F5CE800871723128C47BFBD7D260ABD8EBB3D1A58071235D88352739D2949AB6D7326ADC8AB3E634CF369D15BA1E01A1200E98B473E86C2654B50F4158317A594F67BD93A9EE4AEEEEFF4AEC60DEE9C5F39168A3B88D52C5B61B7E838662D4294497B8628A019C3EFDEC1F4BE5C1B1B1E93DBE35FD16512046E7459'
        
        test.preconditions(      
            step_info=info()
        )
        
        test.step(
            step_title='Transition to Extended Session',
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )

        test.step(
            step_title='Sec Lvl 01 - Request Seed',
            request_seed='01'
        )

        test.step(
            step_title='Sec Lvl 01',
            send_key='01'
        )

        test.step(
            step_title='Read SBAT',
            read_data_ID='F0 F4'
        )

        test.step(
            step_title='Write SBAT',
            write_data_ID=['F0 F4', valid_key]
        )

    def test_002(self, name='Pre-Requisites - Unlock key'):
        unlock_key = '01000000000000000000000000000000441BAFA3B95A64DF9B40B8FD17A47433E1300E1706220E7B5CDC2F405CC16733335A64164E981A4D32A1349F845795E0BB'

        test.preconditions(      
            step_info=info()
        )
        
        test.step(
            step_title='Transition to Extended Session',
            extended_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength' : 4
            }
        )

        test.step(
            step_title='Sec Lvl 0D - Request Seed',
            request_seed='0D'
        )

        test.step(
            step_title='Sec Lvl 0D',
            send_key='0D'
        )

        test.step(
            step_title='Start Routine for Unlock Key',
            start_routine=['02 72', unlock_key]
        )


    def test_003(self, name='Check for successful programming'):
        input('Wait until DPS has finished and ECU is already up to continue... Reset if necessary and Press Enter')

        test.preconditions(      
            step_info=info(),
            reset_communication=True
        )
        
        test.step(
            step_title='Start routine to verify successful programming',
            start_routine=['FF 01', ' '],

            expected={
                'response'   : 'Positive'
            }
        )