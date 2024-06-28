""""
*******************************************************************************
@copyright    Copyright 2022 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    "WakeUp Description
    Wakeups are physical events that cause an ECU to leave a low power state. There are two types of wakeups,
    Active and Passive. An Active wakeup is an internal wakeup caused by the ECU itself. As an example of an Active
    wakeup, ECUs support internal software alarms to wake an ECU from a sleep mode to perform a required task. A
    Passive wakeup is an external wakeup cause by another ECU along a serial bus or a directly connected I/O. A CAN
    wakeup frame is an example of a passive wakeup.
    "

@note ABBREVIATIONS:
        - uds: Unified Diagnostic Services

Author: Abraham Estrada (uif01834)
*******************************************************************************"""

from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, os
import misc as tools

test = TestCase()


class Test_WakeUpDescription(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        ''' Initialize test case '''
        test.begin(
            test_info=info(),
            writeTestResults=True, # Write on CG Report
            excel_tab='WakeUp Description'  # Specify CG Excel Tab
        )

    @classmethod
    def tearDownClass(self):
        # == End Test Case ==#
        test.end()

    def test_004(self, name='Clear Wakeup records'):

        test.preconditions(
            step_info=info(),
            # power_mode='RUN'# 11/26/2021 check power mode is run or off?
        )
        time.sleep(5)
        if device_under_test is 'PTM':
            # print(test.canoe.get_signal(signal='PwrRrClsrMtnSts', PDU='PDU_4037'))
            if test.canoe.get_signal(signal='PwrRrClsrMtnSts', PDU='PDU_4037') == 1:
                print('Gate is closed')

            else:
                prompt = tools.popup.ask(title=name, description='Gate is not closed')

        test.step(
            step_title=name,
            custom='31 01 04 1A',
            expected={
                'response': 'Positive'
            }
        )
        test.canoe.set_envVariable(envVNMFStop=1)
        test.canoe.set_envVariable(envVNMFSend=0)
        time.sleep(60)

    # def test_001_7(self, name='Select and Record a supported Wakeup source'):
    #     test.preconditions(
    #         step_info=info()
    #     )
    #     test.canoe.set_envVariable(envVNMFStop=0)
    #     test.canoe.set_envVariable(envVNMFSend=1)
    #     time.sleep(5)
    #     prompt = tools.popup.ask(title=name, description='check the ECU is wakeup')
    #     test.compare(True, prompt, step='test_001_7')
    #
    # def test_001_8(self, name='Read Wakeup Records'):
    #     test.preconditions(
    #         step_info=info()
    #     )
    #     test.step(
    #         step_title=name,
    #         custom='22 F0 9E',
    #         expected={
    #             'response': 'Positive',
    #             'expected_byte': ('01', '20', '02', '01'),
    #             'byte_index': (3, 4, 13, 14)
    #
    #         }
    #
    #     )
    #
    # def test_001_12(self, name='Read Wakeup Records after reconnecting power'):
    #     test.power_supply.output(False)
    #     time.sleep(10)
    #     test.power_supply.output(True)
    #     test.preconditions(
    #         step_info=info()
    #     )
    #     test.step(
    #         step_title=name,
    #         custom='22 F0 9E',
    #         expected={
    #             'response': 'Positive',
    #             'expected_byte': ('01', '01', '02', '20', '03', '01'),
    #             'byte_index': (3, 4, 13, 14, 23, 24)  # response 62 is byte 0
    #
    #         }
    #
    #     )