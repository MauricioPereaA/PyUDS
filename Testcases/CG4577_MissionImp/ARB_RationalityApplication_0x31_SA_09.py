'''
/*****************************************************************************/
    CG4577 - ARB Rationality Application 0x31 Tab
        * Based on GM PTM Script by @Zhang Jirao

    Test details:
        - Security Level: 09/0A
        - RIDs Tested + Signals required to be satisfied:
            * 033E *
                'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
                
            * 033F *
                'VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0,
                'TEGP_TrnsShftLvrPstnAuth', 'TrnsEstGr_Prtctd_PDU', 1
                
/==============================================================================/
    Created by @Evan Tirado | 05/08/2021
/******************************************************************************/
'''

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Rationality-Application $31'
        )

        # Signal Conditions - To be used with test.preconditions()
        veh_speed_condition     = ('VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 0)
        veh_speed_inv_condition = ('VSADP_VehSpdAvgDrvnAuth_Inv', 'VehSpdAvgDrvn_Prtctd_PDU', 0)
        shift_lever_condition   = ('TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1)
        shift_lever_inv_condition   = ('TEGP_TrnsShftLvrPstnAuth_Inv',  'TrnsEstGr_Prtctd_PDU', 0)
        
        veh_speed_condition_false     = ('VSADP_VehSpdAvgDrvnAuth', 'VehSpdAvgDrvn_Prtctd_PDU', 1000)
        veh_speed_inv_condition_false = ('VSADP_VehSpdAvgDrvnAuth_Inv', 'VehSpdAvgDrvn_Prtctd_PDU', 1)
        shift_lever_condition_false   = ('TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 0)
        shift_lever_inv_condition_false   = ('TEGP_TrnsShftLvrPstnAuth_Inv',  'TrnsEstGr_Prtctd_PDU', 1)
       
        self.rids_info = [
            {   # Group 1 - Same SF & DataRecord + Same Conditions
                'rids': ('033E', '033F'), 
                'data': '00 00', #DataRecord
                'conditions_true':  [veh_speed_condition, veh_speed_inv_condition, shift_lever_condition, shift_lever_inv_condition],
                'conditions_false': [veh_speed_condition_false, veh_speed_inv_condition_false, shift_lever_condition_false, shift_lever_inv_condition_false]
            }
        ]

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_001(self, name='Transition to extendedSession, Application Mode'):
        test.preconditions(

            step_info=info(),
            signal = ['TEGP_TrnsShftLvrPstnAuth',  'TrnsEstGr_Prtctd_PDU', 1]

        )

        test.step(
            step_title=name,
            extended_session_control=True,

            expected={
                'response': 'Positive',
                'data': None,
                'dataLength': None
            }

        )

    def test_002(self, name='Activate TesterPresent'):
        test.preconditions(

            step_info=info(),
            functionalAddr=True,

        )

        test.step(
            step_title=name,
            start_tester_present=True,

            expected={
                'response': 'No response',
                'data': None,
                'dataLength': None
            }

        )

    def test_003(self, name='Access Security Lvl 9'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            request_seed= '09',

            expected={
                'response': 'Positive',
                'dataLength': 31,
                'unexpected_response': True,
                'partialData': ('00', 'FF')
            }

        )

    def test_004(self, name='Access Security Send Key'):
        test.preconditions(

            step_info=info()

        )

        test.step(
            step_title=name,
            send_key= '09',

            expected={
                'response': 'Positive'
            }
        )

    def test_005(self, name='ALL Condition satisfied '):
        for rid_info in self.rids_info:
            for supported_rid in rid_info['rids']:
                # Unify all conditions into a single List - To be used by test.preconditions()

                ''' Condition 1 - Satisfied '''
                all_signal_conditions = rid_info['conditions_true'][0]

                ''' Condition 2 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][1]

                ''' Condition 3 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][2]

                ''' Condition 4 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][3]

                test.preconditions(
                    step_info=info(),
                    signal = [
                        *all_signal_conditions # Unpack all signal conditions
                    ]
                )

                test.step(
                    step_title=name + supported_rid,
                    custom='31 01' + supported_rid + rid_info['data'],
                    expected={
                        'response': 'Positive',
                    }
                )
    
    def test_006(self, name='Condition 1 not satisfied '):
        for rid_info in self.rids_info:
            for supported_rid in rid_info['rids']:
                # Unify all conditions into a single List - To be used by test.preconditions()

                ''' Condition 1 - Unsatisfied '''
                all_signal_conditions = rid_info['conditions_false'][0]

                ''' Condition 2 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][1]

                ''' Condition 3 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][2]

                ''' Condition 4 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][3]

                test.preconditions(
                    step_info=info(),
                    signal = [
                        *all_signal_conditions # Unpack all signal conditions
                    ]
                )
                
                test.step(
                    step_title=name + supported_rid,
                    custom='31 01' + supported_rid + rid_info['data'],
                    expected={
                        'response': 'Negative',
                        'data': '22'
                    }
                )
    
    def test_007(self, name='Condition 2 not satisfied '):
        for rid_info in self.rids_info:
            for supported_rid in rid_info['rids']:
                # Unify all conditions into a single List - To be used by test.preconditions()

                ''' Condition 1 - Satisfied '''
                all_signal_conditions = rid_info['conditions_true'][0]

                ''' Condition 2 - Unsatisfied '''
                all_signal_conditions += rid_info['conditions_false'][1]

                ''' Condition 3 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][2]

                ''' Condition 4 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][3]

                test.preconditions(
                    step_info=info(),
                    signal = [
                        *all_signal_conditions # Unpack all signal conditions
                    ]
                )
                
                test.step(
                    step_title=name + supported_rid,
                    custom='31 01' + supported_rid + rid_info['data'],
                    expected={
                        'response': 'Negative',
                        'data': '22'
                    }
                )
    
    def test_008(self, name='Condition 3 not satisfied '):
        for rid_info in self.rids_info:
            for supported_rid in rid_info['rids']:
                # Unify all conditions into a single List - To be used by test.preconditions()

                ''' Condition 1 - Satisfied '''
                all_signal_conditions = rid_info['conditions_true'][0]

                ''' Condition 2 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][1]
                
                ''' Condition 3 - Unsatisfied '''
                all_signal_conditions += rid_info['conditions_false'][2]

                ''' Condition 4 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][3]

                test.preconditions(
                    step_info=info(),
                    signal = [
                        *all_signal_conditions # Unpack all signal conditions
                    ]
                )
                
                test.step(
                    step_title=name + supported_rid,
                    custom='31 01' + supported_rid + rid_info['data'],
                    expected={
                        'response': 'Negative',
                        'data': '22'
                    }
                )

    def test_009(self, name='Condition 4 not satisfied '):
        for rid_info in self.rids_info:
            for supported_rid in rid_info['rids']:
                # Unify all conditions into a single List - To be used by test.preconditions()

                ''' Condition 1 - Satisfied '''
                all_signal_conditions = rid_info['conditions_true'][0]

                ''' Condition 2 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][1]
                
                ''' Condition 3 - Satisfied '''
                all_signal_conditions += rid_info['conditions_true'][2]

                ''' Condition 4 - Unsatisfied '''
                all_signal_conditions += rid_info['conditions_false'][3]

                test.preconditions(
                    step_info=info(),
                    signal = [
                        *all_signal_conditions # Unpack all signal conditions
                    ]
                )
                
                test.step(
                    step_title=name + supported_rid,
                    custom='31 01' + supported_rid + rid_info['data'],
                    expected={
                        'response': 'Negative',
                        'data': '22'
                    }
                )
