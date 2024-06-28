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

    def test_001(self, name="Implement Pre-Programming Sequence"):

        test.preconditions(step_info=info(), functionalAddr=False)

        test.step(
            step_title=name,
            start_tester_present=True,
            extended_session_control=True,
            communication_control=False,
            dtc_settings=False,
            expected={"response": "Positive"},
        )

    def test_002(self, name="Req Seed"):
        test.preconditions(step_info=info())
        test.step(step_title=name, request_seed="01", expected={"response": "Positive"})

    def test_003(self, name="Send Key"):
        test.preconditions(step_info=info())
        test.step(step_title=name, send_key="01", expected={"response": "Positive"})

    # Boot mode
    def test_004(self, name="Transition to programmingSession, Boot Mode"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            programming_session_control=True,
            expected={"response": "Positive"},
        )

    def test_005(self, name="Erase Memory"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name, custom="31 01 FF 00 01", expected={"response": "Positive"}
        )

    def test_006(self, name="Request Download"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="34 00 44 00 01 00 00 00 15 fe 00",
            expected={"response": "Positive"},
        )

    def test_007(self, name="Transfer Data with an invalid message length 2"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="36",
            expected={"response": "Negative", "data": "13"},
        )

    def test_008(self, name="Transfer Data with an invalid message length 2"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="36 00",
            expected={"response": "Negative", "data": "13"},
        )


    def test_009(
        self, name="Transfer Data of Valid Signed App SW file, ReqDown not active"
    ):
        time.sleep(0.5)
        test.preconditions(step_info=info())
        for index, packet in enumerate(Binary.packets_to_send(_binary_app)):
            if index == 0:
                test.step(
                    step_title=name,
                    custom=packet,
                    expected={"response": "Negative", "data": "24"},
                )

    def test_010(self, name="Request Download with an invalid message length 1"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="34 00 44 00 01 00 00 00 00 01 00",
            expected={"response": "Positive"},
        )

    def test_011(self, name="Transfer Data of Valid Signed App SW file"):
        time.sleep(0.5)
        test.preconditions(step_info=info())
        for index, packet in enumerate(Binary.packets_to_send(_binary_app)):
            if index <= 10:
                test.step(
                    step_title=name,
                    custom=packet,
                    expected={"response": "Negative", "data": "24"},
                )

    def test_012(
        self, name="Transfer Data with a blockrSequenceCounter non consecutive"
    ):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="36 02",
            expected={"response": "Negative", "data": "73"},
        )

    def test_013(self, name="<Activate default>"):
        test.preconditions(
            step_info=info(),
        )
        test.step(
            step_title=name,
            default_session_control=True,
            expected={"response": "Positive"},
        )

    def test_014(self, name="<Activate hardReset>"):
        test.preconditions(step_info=info(), power_mode="OFF")
        test.step(step_title=name, custom="11 01", expected={"response": "Positive"})

    def test_015(self, name="Implement Pre-Programming Sequence"):

        test.preconditions(step_info=info(), functionalAddr=False)

        test.step(
            step_title=name,
            start_tester_present=True,
            extended_session_control=True,
            communication_control=False,
            dtc_settings=False,
            expected={"response": "Positive"},
        )

    def test_016(self, name="Req Seed"):
        test.preconditions(step_info=info())
        test.step(step_title=name, request_seed="01", expected={"response": "Positive"})

    def test_017(self, name="Send Key"):
        test.preconditions(step_info=info())
        test.step(step_title=name, send_key="01", expected={"response": "Positive"})

    # Boot mode
    def test_018(self, name="Transition to programmingSession, Boot Mode"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            programming_session_control=True,
            expected={"response": "Positive"},
        )

    def test_019(self, name="Erase Memory"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name, custom="31 01 FF 00 01", expected={"response": "Positive"}
        )

    def test_020(self, name="Request Download"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="34 00 44 00 01 00 00 00 15 fe 00",
            expected={"response": "Positive"},
        )

    def test_021(self, name="Transfer Data of Invalid Signed App SW file"):
        time.sleep(0.5)
        test.preconditions(step_info=info())
        for index, packet in enumerate(Binary.packets_to_send(_binary_app)):
            if index == 0:
                test.step(
                    step_title=name,
                    custom=packet,
                    expected={"response": "Negative", "data": "72"},
                )

    def test_022(self, name="<Activate default>"):
        test.preconditions(
            step_info=info(),
        )
        test.step(
            step_title=name,
            default_session_control=True,
            expected={"response": "Positive"},
        )

    def test_023(self, name="<Activate hardReset>"):
        test.preconditions(step_info=info(), power_mode="OFF")
        test.step(step_title=name, custom="11 01", expected={"response": "Positive"})

    def test_024(self, name="Implement Pre-Programming Sequence"):

        test.preconditions(step_info=info(), functionalAddr=False)

        test.step(
            step_title=name,
            start_tester_present=True,
            extended_session_control=True,
            communication_control=False,
            dtc_settings=False,
            expected={"response": "Positive"},
        )

    def test_025(self, name="Req Seed"):
        test.preconditions(step_info=info())
        test.step(step_title=name, request_seed="01", expected={"response": "Positive"})

    def test_026(self, name="Send Key"):
        test.preconditions(step_info=info())
        test.step(step_title=name, send_key="01", expected={"response": "Positive"})

    # Boot mode
    def test_027(self, name="Transition to programmingSession, Boot Mode"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            programming_session_control=True,
            expected={"response": "Positive"},
        )

    def test_028(self, name="Erase Memory"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name, custom="31 01 FF 00 01", expected={"response": "Positive"}
        )

    def test_029(self, name="Request Download"):

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="34 00 44 00 01 00 00 00 15 fe 00",
            expected={"response": "Positive"},
        )

    def test_030(self, name="Transfer Data of valid Signed App SW file"):
        time.sleep(0.5)
        test.preconditions(step_info=info())
        for packet in Binary.packets_to_send(_binary_app):
            test.step(step_title=name, custom=packet, expected={"response": "Positive"})

    def test_031(self, name="Request Transfer Exit"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="37",
            expected={
                "response": "Positive",
            },
        )