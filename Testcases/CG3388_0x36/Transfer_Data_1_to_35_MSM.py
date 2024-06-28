"""CG3388 Ver Apr2020

Author: David Urzua
Date: Jan 2020
Modified by:
Date:

    This script may no be updated to the latest CG33388 version
"""

import time
import unittest
from inspect import stack as info

from __global__ import _binary_app
from framework.shared_libs.binary_file_handler import Binary
from Testcases.TestClass import TestCase

test = TestCase()


class Request_Download(unittest.TestCase):

    """Request Download service is used by the client to initiate a data transfer from the client to the server"""

    @classmethod
    def setUpClass(self):
        """Initialize test case"""
        test.begin(test_info=info(), writeTestResults=True, excel_tab="0x36")

        self.test_status = {}

    @classmethod
    def tearDownClass(self):
        """End test case"""
        test.end()

    def test_001(self, name="Service Not Supported in Application"):
        test.preconditions(
            step_info=info(),
            sbat=False,  # Clear SBAT
            mec_zero=True,
            # functionalAddr=True
        )
        test.step(
            step_title=name,
            custom="36 01 00 00 00 00 00",
            expected={"response": "Negative", "data": "11"},
        )

    def test_002(self, name="Implement Pre-Programming Sequence"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            send_key="01",
            expected={"response": "Negative", "data": "12"},
        )

    def test_003(self, name="Implement Pre-Programming Sequence"):

        test.preconditions(step_info=info(), functionalAddr=False)

        test.step(
            step_title=name,
            extended_session_control=True,
            start_tester_present=True,
            dtc_settings=False,
            communication_control=False,
            expected={"response": "Positive"},
        )

    def test_004(self, name="Request Seed"):
        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            request_seed="01",
            expected={
                "response": "Positive",
                "dataLength": 31,
                "partialData": "00 " * 30,
            },
        )

    # Boot mode
    def test_005(self, name="Transition to programmingSession, Boot Mode"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            programming_session_control=True,
            expected={"response": "Positive"},
        )

    def test_006(self, name="Erase Memory"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name, custom="31 01 FF 00 01", expected={"response": "Positive"}
        )

    def test_007(self, name="Request Download of Valid Signed App SW file"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="34 00 44 00 01 00 00 00 15 fe 00",
            expected={"response": "Positive"},
        )

    def test_008(self, name="Transfer Data of Valid Signed App SW file"):
        time.sleep(0.5)
        test.preconditions(step_info=info())
        for packet in Binary.packets_to_send(_binary_app):
            test.step(step_title=name, custom=packet, expected={"response": "Positive"})

    def test_009(self, name="Request Transfer Exit"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="37",
            expected={
                "response": "Positive",
            },
        )
