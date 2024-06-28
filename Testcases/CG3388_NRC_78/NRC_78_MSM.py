"""CG3388 Ver Apr2020

Author: David Urzua
Date: Jan 2020
Modified by:
Date:

    This script may no be updated to the latest CG33388 version
"""
import unittest
from inspect import stack as info

from __global__ import _binary_app
from framework.shared_functions import device_under_test
from framework.shared_libs.binary_file_handler import Binary
from Testcases.TestClass import TestCase

test = TestCase()


class PyUDS_TestCase(unittest.TestCase):

    """Positive Flow Diagnostic Session Control Session and Security Tests"""

    @classmethod
    def setUpClass(self):
        """Initialize test case"""
        test.begin(
            test_info=info(), writeTestResults=True, excel_tab="NRC 78 & P2 Timing"
        )

    @classmethod
    def tearDownClass(self):
        """End test case"""
        test.end()

    if device_under_test == "TCP":

        def test_001(self, name="NRC 78"):

            test.preconditions(step_info=info())

            test.step(
                step_title=name,
                extended_session_control=True,
                request_seed="01",
                send_key="01",
                custom="2E " + "F0 F8 " + "00" * 1173,
                expected={
                    "response": "Positive",
                    "check_NRC78": {"CompType": "GELE", "HighLimit": 8, "LowLimit": 5},
                },
            )

    else:

        def test_001(self, name="NRC 78"):

            test.preconditions(step_info=info())

            test.step(
                step_title=name,
                extended_session_control=True,
                start_tester_present=True,
                dtc_settings=False,
                communication_control=False,
                request_seed="01",
                send_key="01",
                programming_session_control=True,
                custom="31 01 FF 00 01",  # Erase Memory
                expected={
                    "response": "Positive",
                    "check_NRC78": {"CompType": "GELE", "HighLimit": 8, "LowLimit": 5},
                },
            )

        def test_002(self, name="Request Download of Valid Signed App SW file"):

            test.preconditions(step_info=info())

            test.step(
                step_title=name,
                custom="34 00 44 00 01 00 00 00 15 FE 00",
                expected={"response": "Positive"},
            )

        def test_003(self, name="Transfer Data of Valid Signed App SW file"):
            test.preconditions(step_info=info())
            for packet in Binary.packets_to_send(_binary_app):
                test.step(
                    step_title=name, custom=packet, expected={"response": "Positive"}
                )

        def test_004(self, name="Request Transfer Exit"):
            test.preconditions(step_info=info())
            test.step(
                step_title=name,
                custom="37",
                expected={
                    "response": "Positive",
                },
            )

        # Note: This step is not applicable to ECUs that use the in-house Bootloader
        def test_005(self, name="Update PSI"):

            test.preconditions(step_info=info())

            test.step(
                step_title=name,
                custom="31 01 02 09 01",
                expected={"response": "Positive"},
            )

    # Purpose of test 005 only to fill CG report
    def test_006(self, name="Attach log "):
        test.preconditions(step_info=info())
        test.compare(True, True, step="test_005")
