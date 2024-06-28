from Testcases.TestClass import TestCase
from framework.shared_functions import tools, ECU_info
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Gen_Boot_Requirements(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Proc Modes Details'
        )
        message = 'Please ensure you have APP SW Flashed on the ECU.'
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)
        self.s3_timeout = 5 + 0.1 # S3 timeout + 100 msec
        self.sbat_signer_info_invalid = '0301005B50544D000000000043414E4F452044495641204543554944FF6F647900000000000000000000000007000000000000000000B4169DAEEC3646EC594A288E37B6FAEF88AE90169904D909D3EF61FBD51A9B6B537FA47B74FD782799B14F8F19353A98B46E77F84848C9CDD7794CC58A4481248BAB1EFD8BD117A082B8DD3506824CF632918FECE932488D28355E4B758F915AB410C1A21CFC2B6F70FB8365620F6A05B31912435F3F7B03ECEA59E4460AB867E730888953301E5FD2274B6CF56ABE7FDA90B33A555099995B7F1855DDC5006B57B2C692772F01BDA270ACB2454EEE4B9E9AC92F53DA2C23D6F92DFE2A43A069BDEEE952E2CA743959ACAC9B84A6B0322A80D5FF16853526A1F358C0262338D198D3873CCCA6C04BA79AA29AA1C81F0243DAF7DD2B5EFF6671D130044AA1D58728BB947F42C357F36ED69BF7355AFDCB8109F8E69E6C2C63E5C4E7E56A44A822E3AE4ECE7DB318D5684A2B6AFBB3406C86A78CA0377230DA2C53520AD92BBD7F4AE62B26FA2FD84C22881BD9CCF7C3229ECE6C67B953EFC412078A88B4009B5B10A1E65470BFE092B341AE5F63C2F61495EB038E064F3071B14AEFB5DFFCEEF573A365AC8EBD0FAF2CD10CE6BE25F9EC93F3A040A5C23C5F1066CA59DDA681DEAE1A675007A3687FA082F5E39B8E481EA04C1BAAEB509C7DC2F0BD388D1E45CB6A4254029B356CA40CDDC0D7EB34AB19E8AC1310C9EEC9C9D840C7556490AFBC926927C071A158E2B209F1899C438A6CE68A335C1AB40AADC7438158731329C4AE7E696F43A7C7578E2B684819F2E9F558D14914E8BC75B8AF33EFB06FAE465C2D49D6E6C8A82C9391F69859950F156241761FC19493D53CDFCA49897CB0BCFB7C73D3F81110806CA196FAE719750551AAB1ED6938CB06C9D8E211190A479CE9633DBEE945C24EFB68C700CD8865430A90FFB7D82E6C845FB7CC33779FB21F9B9151EEB1FB488BDDA43A937814C1CAC471DC5486A74972140AFD4E0E2CF31515C366477C4C44BEE8816DF8E9228EA0C069C360D58FA6B1C4931F6D09F2FA1EFBF0DE03E42FFEEE4E50D24D54611718FBA1D1263DADF8ED2E5E00A93F74D235399E98BBF09EC016E00DCF3E8E17A7A64F7D8B0FC0B3693C3F50D6E9D069F30DE3'
        
    
    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Implement Pre-Programming Sequence'):

        test.preconditions(
            step_info=info(),
        )

        test.step(
            step_title=name,
            extended_session_control= True,
            request_seed='01',
            send_key = '01',
            custom = '2E F0 F4' + self.sbat_signer_info_invalid,
            default_session_control = True,

            expected={
                'response': 'Positive'
            }
        )

        # The test starts here, the step before is a precondition to modify the SBAT
        test.preconditions(
            step_info=info(),
            mec_zero=True,
            functionalAddr=True
        )
        test.step(
            step_title=name,
            extended_session_control= True,
            start_tester_present= True,
            dtc_settings = False,
            communication_control= False,

            expected={
                'response'   : 'Positive'
            }
        )

    def test_002(self, name='Request Seed'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            request_seed='01',

            expected={
                'response'   : 'Positive',
                'dataLength':  31,
                'partialData': ('00', 'FF')
            }
        )



    def test_003(self, name='Request SendKey'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            send_key='01',

            expected={
                'response': 'Positive'
            }
        )

    def test_004(self, name='Transition to programmingSession, Boot Mode'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            programming_session_control = True,

            expected={
                'response'            : 'Positive'
            }
        )


    def test_005(self, name='Read BIS'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom='22 F0 F2',

            expected={
                'response'    : 'Positive',
                'partialData' : '62 F0 F2 00 08' 
            }
        )
    

    def test_006(self, name='defaultSession '):

        test.preconditions(            
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive'
            }

        )


    def test_007(self, name='Request a Download'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            custom= '34 00 44 00 00 A0 00 00 00 1E 00',

            expected={
                'response'   : 'Negative',
                'data'       : '11'
            }
        )