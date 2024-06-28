
'''
Author : Ricardo Montes

Modified by : Manuel Medina      Date: 17 - Jun - 20
Modified by: Mauricio Perea        Date: 30-Sep-20

This script is intended to validate positive response of service 0x19 which main function is to enable a client to read the status of the Server-Based Diagnostic Trouble Code (DTC) 
information from any server or group of servers within a vehicle. Unless otherwise noted, the server will return emission related and non emission related DTC information.

                        ************ ATTENTION !!! ************
    Script potentially must be modified according to the applicable ECU supported subfunctions of service $19
'''
from framework.shared_functions import device_under_test, tools, pn_dict, sleep_timeout
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='0x19'
        )

        self.under_voltage_DTC = 'F0 03 16'


    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def test_002(self, name='reportNumberOfDTCByStatusMask request'):
        test.preconditions(
            step_info=info(),
            power_mode='RUN',
            mec_zero = True,
            sbat = False
        )
        # Extra step to ensure that no DTCs are set ..
        test.step(
            step_title=name,
            custom='14 FF FF FF',
            expected={
                'response': 'Positive'
            }
        )
        time.sleep(2)
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': '00',
                'byte_index'   : 3			
            }
        )

    def test_003(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()

        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_004(self, name='<Activate TesterPresent>'):
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

    def test_005(self, name='reportNumberOfDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'     : 'Positive',
                'dataLength'   : 4,
                'expected_byte': '00',
                'byte_index'   : 3 
            }
        )

    def test_006(self, name='Transition to defaultSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        )

    def test_007(self, name='reportDTCByStatusMask'):#cannot get DTC with low voltage
        test.set_dtc_condition(underVoltage=True)
        test.preconditions(
            step_info=info()
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response'   : 'Positive',
                'partialData': '%s 2F'%self.under_voltage_DTC
            }
        )

    def test_008(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()

        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_009(self, name='<Activate TesterPresent>'):
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

    def test_010(self, name='reportDTCByStatusMask in extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response'   : 'Positive',
                'partialData': '%s 2F'%self.under_voltage_DTC
            }
        )

    def test_011(self, name='Transition to defaultSession'):

        test.preconditions(
            step_info=info()
        )

        test.step(
            step_title=name,
            default_session_control=True,

            expected={
                'response'   : 'Positive',
                'dataLength':  4
            }
        )

    def test_012(self, name='reportDTCSnapshotIdentification'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $03 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 01'
                }
            )

    def test_013(self, name='<Transition Server to extendedSession> '):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $03 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()

            )
            test.step(
                step_title=name,
                custom='10 03',
                expected={
                    'response': 'Positive',
                    'dataLength': '4'
                }
            )

    def test_014(self, name='<Activate TesterPresent>'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $03 not supported by %s'%device_under_test)
            return 0

        else:

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

    def test_015(self, name='reportDTCSnapshotIdentification'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $03 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 01'
                }
            )


    def test_016(self, name='Transition to defaultSession'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_017(self, name='reportDTCSnapshotRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 04 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F' + ' 01'
                }
            )

    def test_018(self, name='<Transition Server to extendedSession> '):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()

            )
            test.step(
                step_title=name,
                custom='10 03',
                expected={
                    'response': 'Positive',
                    'dataLength': '4'
                }
            )

    def test_019(self, name='<Activate TesterPresent>'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:

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

    def test_020(self, name='reportDTCSnapshotRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 04 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F' + ' 01'
                }
            )



    def test_021(self, name='Transition to defaultSession'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_022(self, name='reportDTCExtendedDataRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
            return 0
        elif device_under_test in ['ARB']:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' FF',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 14
                }
            )        
        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 12
                }
            )

    def test_023(self, name='<Transition Server to extendedSession> '):
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()

        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_024(self, name='<Activate TesterPresent>'):
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
            return 0

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

    def test_025(self, name='reportDTCExtendedDataRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
            return 0
        elif device_under_test in ['ARB']:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' FF',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 14
                }
            )
        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 12
                }
            )



    def test_026(self, name='Transition to defaultSession'):
        #if device_under_test not in ['ARB', 'PTM', 'TCP']:
        #    print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
        #    return 0

        #else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_027(self, name='reportSupportedDTC'): # Purpose of the test is to verify the positive response of subfunction $0A  along with supported DTCs but not necessary to verify the report of all of them
                test.preconditions(                                                # This verifies that at least the current DTC with failed status is being reported
                        step_info=info()
                )
                test.step(
                        step_title=name,
                        custom='19 0A',
                        expected={
                                'response'   : 'Positive',
                                'partialData': self.under_voltage_DTC + ' 2F'
                        }
                )

    def test_028(self, name='<Transition Server to extendedSession> '):
        test.preconditions(
            step_info=info()

        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_029(self, name='<Activate TesterPresent>'):
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

    def test_030(self, name='reportSupportedDTC in extendedSession'):
        test.preconditions(
            step_info=info()
        )
        test.step(
                step_title=name,
                custom='19 0A',
                expected={
                        'response'   : 'Positive',
                        'partialData': self.under_voltage_DTC + ' 2F'
                }
        )

    def test_031(self, name='Transition to defaultSession'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:

            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_032(self, name='reportEmissionsOBDDTCByStatusMask'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                    step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 13 FF',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )

    def test_033(self, name='<Transition Server to extendedSession> '):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()

            )
            test.step(
                step_title=name,
                custom='10 03',
                expected={
                    'response': 'Positive',
                    'dataLength': '4'
                }
            )

    def test_034(self, name='<Activate TesterPresent>'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:

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

    def test_035(self, name='reportEmissionsOBDDTCByStatusMask'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 13 FF',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )


    def test_036(self, name='Transition to defaultSession'):
        if device_under_test in ['ARB', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_037(self, name='reportDTCFaultDetectionCounter'):
        if device_under_test in ['ARB', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                    step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 14',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )

    def test_038(self, name='<Transition Server to extendedSession> '):
        if device_under_test in ['ARB', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()

            )
            test.step(
                step_title=name,
                custom='10 03',
                expected={
                    'response': 'Positive',
                    'dataLength': '4'
                }
            )

    def test_039(self, name='<Activate TesterPresent>'):
        if device_under_test in ['ARB', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:

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

    def test_040(self, name='reportDTCFaultDetectionCounter'):
        if device_under_test in ['ARB', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 14',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )


    def test_041(self, name='Transition to defaultSession'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_042(self, name='reportDTCWithPermanentStatus'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $15 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                    step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 15',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )

    def test_043(self, name='<Transition Server to extendedSession> '):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()

            )
            test.step(
                step_title=name,
                custom='10 03',
                expected={
                    'response': 'Positive',
                    'dataLength': '4'
                }
            )

    def test_044(self, name='<Activate TesterPresent>'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:

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

    def test_045(self, name='reportDTCWithPermanentStatus'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info()
            )
            test.step(
                    step_title=name,
                    custom='19 15',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )



    def test_046(self, name='Transition to defaultSession'):
        #if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
        #    print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
        #    return 0

        #else:
            test.preconditions(
                step_info=info()
            )

            test.step(
                step_title=name,
                default_session_control=True,

                expected={
                    'response'   : 'Positive',
                    'dataLength':  4
                }
            )

    def test_047(self, name='reportDTCWithPermanentStatus in security Level 15'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        test.step(
            step_title=name,
            custom='19 01 FF',
            expected={
                'response'  : 'Positive',
                'dataLength': 4
            }
        )

    def test_048(self, name='reportDTCByStatusMask'):
        test.preconditions(
            step_info=info(),
            functionalAddr = True
        )
        time.sleep(5)
        test.step(
            step_title=name,
            custom='19 02 FF',
            expected={
                'response'   : 'Positive',
                'partialData': '%s 2F'%self.under_voltage_DTC
            }
        )

    def test_049(self, name='reportDTCSnapshotIdentification'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $03 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
            )
            test.step(
                step_title=name,
                custom='19 03',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 01'
                }
            )

    def test_050(self, name='reportDTCSnapshotRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM']:
            print('Skipping test .. Subfunction $04 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
            )
            test.step(
                step_title=name,
                custom='19 04 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F' + ' 01'
                }
            )

    def test_051(self, name='reportDTCExtendedDataRecordByDTCNumber'):
        if device_under_test not in ['ARB', 'PTM', 'TCP']:
            print('Skipping test .. Subfunction $06 not supported by %s'%device_under_test)
            return 0
        elif device_under_test in ['ARB']:
            test.preconditions(
                step_info=info()
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' FF',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 14
                }
            )
        else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
            )
            test.step(
                step_title=name,
                custom='19 06 ' + self.under_voltage_DTC + ' 01',
                expected={
                    'response'   : 'Positive',
                    'partialData': self.under_voltage_DTC + ' 2F',
                    'dataLength' : 12
                }
            )

    def test_052(self, name='reportSupportedDTC'): # Purpose of the test is to verify the positive response of subfunction $0A  along with supported DTCs but not necessary to verify the report of all of them
        test.preconditions(                        # This verifies that at least the current DTC with failed status is being reported
            step_info=info(),
            functionalAddr = True
            )
        test.step(
                step_title=name,
                custom='19 0A',
                expected={
                        'response'   : 'Positive',
                        'partialData': self.under_voltage_DTC + ' 2F'
                }
        )

    def test_053(self, name='reportEmissionsOBDDTCByStatusMask'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $13 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
                )
            test.step(
                    step_title=name,
                    custom='19 13 FF',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )

    def test_054(self, name='reportDTCFaultDetectionCounter'):
        if device_under_test in ['ARB', 'SCL', 'TCP']:   #14 is supported
            print('Skipping test .. Subfunction $14 not supported by %s'%device_under_test)
            return 0

        #else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
                )
            test.step(
                    step_title=name,
                    custom='19 14',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
            )

    def test_055(self, name='reportDTCWithPermanentStatus'):
        if device_under_test in ['ARB', 'PTM', 'MSM', 'SCL', 'TCP']:
            print('Skipping test .. Subfunction $15 not supported by %s'%device_under_test)
            return 0

        else:
            test.preconditions(
                step_info=info(),
                functionalAddr = True
                )
            test.step(
                    step_title=name,
                    custom='19 15',
                    expected={
                            'response'   : 'Positive',
                            'partialData': 'PLACEHOLDER'
                    }
                )

    def test_056(self, name='<Transition Server to extendedSession> '):
        if device_under_test in ['PTM', 'MSM']:#add
            print('Skipping test .. Subfunction $15 not supported by %s'%device_under_test)
            return 0
        test.preconditions(
            step_info=info()

        )
        test.step(
            step_title=name,
            custom='10 03',
            expected={
                'response': 'Positive',
                'dataLength': '4'
            }
        )

    def test_057(self, name='<Activate TesterPresent>'):
        if device_under_test in ['PTM', 'MSM']:#add
            print('Skipping test .. Subfunction $15 not supported by %s'%device_under_test)
            return 0
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
        test.power_supply_reset_default()
