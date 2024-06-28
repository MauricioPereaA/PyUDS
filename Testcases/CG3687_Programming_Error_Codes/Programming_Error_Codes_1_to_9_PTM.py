"""CG3388 Ver Apr2020

Author: -
Date: -
Modified by: David Urzúa
Date: Feb 2022
    Script cloned from PTM, modified to work with MSM due amount valid partitions for test 05
    This script may no be updated to the latest CG33388 version
"""
import unittest
from inspect import stack as info

from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase

test = TestCase()


class Gen_Boot_Requirements(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Initialize test case"""
        test.begin(
            test_info=info(), writeTestResults=True, excel_tab="Programming Error Codes"
        )
        message = "Please ensure you have APP SW Flashed on the ECU."
        print(__name__, message)
        tools.popup.warning(title="Bootloader", description=message)

    @classmethod
    def tearDownClass(self):
        """End test case"""
        test.end()

    def test_001(self, name="Pre-Programming Sequence"):

        test.preconditions(step_info=info(), mec_zero=True, sbat=False)

        test.preconditions(step_info=info(), functionalAddr=True)

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            dtc_settings=False,
            communication_control=False,
            expected={"response": "Positive"},
        )

    def test_002(self, name="Request Seed"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            request_seed="01",
            expected={
                "response": "Positive",
                "dataLength": 31,
                "unexpected_response": True,
                "partialData": ("00", "FF"),
            },
        )

    def test_003(self, name="Send Key"):
        test.preconditions(step_info=info())

        test.step(step_title=name, send_key="01", expected={"response": "Positive"})

    def test_004(self, name="Transition to programmingSession"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            programming_session_control=True,
            expected={"response": "Positive"},
        )

    def test_005(
        self, name="Erase Memory with Partition ID set to a Non-Supported Value"
    ):

        test.preconditions(step_info=info())

        part = ""
        if device_under_test == "MSM":
            part = " 06"
        else:
            part = " 05"
        test.step(
            step_title=name,
            custom="31 01 FF 00" + part,  # 06 partitions for MSM
            expected={"response": "Negative", "data": "31"},
        )

    def test_006(self, name='Verify PEC is set to "$0001 =  Err_PartitionID'):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="22 F0 F1",
            expected={"response": "Positive", "data": "00 01"},
        )
