from Testcases.TestClass import TestCase
from framework.shared_functions import tools, ECU_info
from inspect import stack as info
import unittest, time
from framework.shared_libs.binary_file_handler import Binary
from __global__ import _binary_app, _binary_cal1, _binary_cal2, _binary_cal3

test = TestCase()

class Prog_Sess_Det(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Prog_Sess_Det'
        )
        message = 'Please ensure you have a Green ECU and ensure that you specify an LZMA compressed binary app with Signature = Invalid '
        print(__name__, message)
        tools.popup.warning(title='Bootloader',
                                description=message)

    @classmethod
    def tearDownClass(self):
        ''' End test case'''
        test.end()

    def test_001(self, name='Pre-Programming Sequence'):

        test.preconditions(
            step_info=info(),
            mec_zero=True,
            sbat=False
        )

        test.preconditions(
            step_info=info(),
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
                'response'            : 'Positive',
                'dataLength'          : 31,
                'unexpected_response' : True,
                'partialData'         : ('00', 'FF')
            }
        )

    def test_003(self, name='Send Key'):
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

    def test_004(self, name='Transition to programmingSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            programming_session_control = True,
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_005(self, name='Erase App SW Partition ID'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            custom = '31 01 FF 00 01',
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_006(self, name='Request Download App SW File'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            custom = '34 00 44 00 01 00 00 00 0E 7E 00',
            
            expected={
                'response'   : 'Positive'
            }
        )

    def test_007(self, name='Bootloader evaluates Data Type in 2nd received envelope'):
        test.preconditions(
            step_info=info()
        )

        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Negative',
                    'data'       : '72'
                }
            )
            break

    def test_008(self, name='Program ECU'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title = name,
            custom = '34 00 44 00 01 00 00 00 0E 7E 00',
            
            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_app):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
                }
            )

        test.step(
            step_title = name,
            custom = '37',
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 01',

            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title = name,
            custom = '31 01 FF 00 02',
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title = name,
            custom = '34 00 44 00 01 00 00 00 00 7E 00',
            
            expected={
                'response'   : 'Positive'
            }
        )

        for packet in Binary.packets_to_send(_binary_cal1):
            test.step(
                step_title=name,
                custom = packet,

                expected={
                    'response'   : 'Positive'
                }
            )

        test.step(
            step_title = name,
            custom = '37',
            
            expected={
                'response'   : 'Positive'
            }
        )

        test.step(
            step_title=name,
            custom='31 01 02 09 02',

            expected={
                'response'   : 'Positive'
            }
        )
