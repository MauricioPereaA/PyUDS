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

from framework.shared_functions import device_under_test, tools
from Testcases.TestClass import TestCase

test = TestCase()


class PyUDS_TestCase(unittest.TestCase):

    # == Positive Flow Diagnostic Session Control Session and Security Tests ==#
    @classmethod
    def setUpClass(self):
        # == Initialize test case ==#
        if device_under_test == "SCL":
            tools.popup.warning(
                title="Service 0x2A not supported",
                description="SCL does not support service 0x2A",
            )
            raise Warning("SCL does not support service 0x2A")
        test.begin(test_info=info(), writeTestResults=True, excel_tab="0x2A")

        self.s3_timeout = 0.1  # time:01 1000ms   02 200ms 03 25ms

    @classmethod
    def tearDownClass(self):
        # == End Test Case ==#
        test.end()

    def test_001(self, name="Transition Server to ExtendedSession"):
        test.preconditions(step_info=info(), sbat=False, mec_zero=True)  # Clear SBAT
        test.step(step_title=name, custom="10 03", expected={"response": "Positive"})

    def test_002(self, name="Activate tester present"):
        test.preconditions(step_info=info(), functionalAddr=True)
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={"response": "No response"},
        )

    def test_003(self, name="DynamicallyDefineDataIdentifier  2C - F0-FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 FF F0 80 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FE F0 81 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FD F0 84 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FC F0 89 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FB F0 8D 01 01",  # change The 2C 01 F2 FB F0 8E 01 01 ->2C 01 F2 FB F0 8D 01 01
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 FA F0 8F 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 F9 F0 90 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 F8 F0 91 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F7 F0 92 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F6 F0 94 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F5 F0 95 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F4 F0 A7 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F3 F0 84 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F2 F0 AB 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F1 F0 B3 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F0 F0 B4 01 01",
            expected={"response": "Positive"},
        )

    # Here we must validate that only the DDDI "FF" is transmitted
    def test_004(self, name="read PDID mode 01 - ADD DELAY 10s"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID="FF DF", rate="01", timeout=10
            ),  # DDDID='FF FA'-->DDDID='FF' re-try it
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_005(self, name="stop transmission of PDID FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": False}),
                "periodics_num": 0,
            },
        )

    # Here we must validate the timing of each transmission of the PDID
    def test_006(
        self,
        name="While Server is in extended Session, Send a valid 29 bit Normal fixed addressing, N_TAtype=physical addres request, ADD DELAY 10s",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_007(self, name="Verify response"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "01", "tolerance": 10.0}
                ),
                "periodics_num": 0,
            },
        )

    def test_008(self, name="stop transmission of PDID FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2A 04",  # delete
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": False}),
                "periodics_num": 0,
            },
        )

    # Here we must validate the timing of each transmission of the PDID
    def test_009(self, name="read PDID mode 02 - ADD DELAY 10s"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="02", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_010(self, name="Verify response and stop transmission of PDID FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "02", "tolerance": 10.0}
                ),
                "periodics_num": 0,
            },
        )

    # Here we must validate the timing of each transmission of the PDID
    def test_012(self, name="read PDID mode 03 - ADD DELAY 10s"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="03", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    # Test 13 is combined with test 14 for the porpose of verify and stop transmision in one step
    def test_014(
        self, name="Verify response and stop transmission of PDID FF"
    ):  # change
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "03", "tolerance": 10.0}
                ),
                "periodics_num": 0,
            },
        )

    def test_015(self, name="read PDID mode 01 - ADD DELAY 10s"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_rate": "01",
                "periodics_num": 1,
            },
        )

    def test_016(self, name="Stop tester present"):
        test.preconditions(step_info=info(), stop_tester_present=True)
        print("Waiting for 5s + S3 timeout to be reached...")
        time.sleep(5 + self.s3_timeout)
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={"response": "Positive", "periodics_num": 0},
        )

    def test_017(self, name="Transition Server to extendedSession"):
        test.preconditions(step_info=info())
        test.step(step_title=name, custom="10 03", expected={"response": "Positive"})

    def test_018(self, name="Start tester present"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            start_tester_present=True,
            expected={"response": "No response"},
        )

    # Validate transmission timing ~25ms
    def test_019(
        self,
        name="While Server is in ExtendedSession, Send a valid 29 bitNormal fixed addressing, N_TAtype=physical address request with maximum number of valid periodicDataIdentifieres allowed in a single request- ADD DELAY 120s",
    ):
        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2A 03 F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF",
            expected={"response": "Positive"},
        )

    def test_020(self, name="Keep periodic scheduler active for 2 minutes"):
        test.preconditions(step_info=info())
        tools.timer.input(
            "<Keep periodic scheduler active for 120 seconds>", timeout=120
        )

        test.step(
            step_title=name,
            read_periodic_data_id=dict(
                DDDID="F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF",
                rate="03",
                timeout=10,
            ),
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {
                        "dddid": "F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF",
                        "active": True,
                    },
                    {"dddid": "F0", "active": True},
                    {"dddid": "F1", "active": True},
                    {"dddid": "F2", "active": True},
                    {"dddid": "F3", "active": True},
                    {"dddid": "F4", "active": True},
                    {"dddid": "F5", "active": True},
                    {"dddid": "F6", "active": True},
                    {"dddid": "F7", "active": True},
                    {"dddid": "F8", "active": True},
                    {"dddid": "F9", "active": True},
                    {"dddid": "FA", "active": True},
                    {"dddid": "FB", "active": True},
                    {"dddid": "FC", "active": True},
                    {"dddid": "FE", "active": True},
                    {"dddid": "FF", "active": True},
                ),
                "periodics_num": 16,
            },
        )

    def test_021(self, name="Stop Transmission of Periodic Data Identifier"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2A 04",
            expected={"response": "Positive", "periodics_num": 0},
        )

    # Validate transmission timing of each mode Fast / medium / slow rate
    def test_022(
        self,
        name="While Server is in extendedSession, Send a valid 29 bit Normal fixed addressing, N_TAtype=physical address request",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_023(
        self,
        name="While Server is in extendedSession Send a valid 29 bit Normal fixed addresing,N_TAtype=physical address request-FE",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FE", rate="02", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FE", "active": True}),
                "periodics_num": 2,
            },
        )

    def test_024(
        self,
        name="While Server is in extendedSession Send a valid 29 bit Normal fixed addresing,N_TAtype=physical address request-FD",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FD", rate="03", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FD", "active": True}),
                "periodics_num": 3,
            },
        )

    def test_025(self, name="Keep periodic scheduler active for 30 seconds"):
        test.preconditions(step_info=info())
        tools.timer.input("<Keep periodic scheduler active for 30 seconds>", timeout=30)
        test.step(
            step_title=name,
            stop_periodic_data="FD",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FD", "rate": "03", "tolerance": 10.0}
                ),
                "periodics_num": 2,
            },
        )

    def test_026(self, name="Stop Transmission of Periodic Data Identifier"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2A 04",
            expected={"response": "Positive", "periodics_num": 0},
        )

    def test_027(self, name="read PDID mode 01"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_028(self, name="read PDID mode 02"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="02", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    def test_030(
        self,
        name="While Server is in extendedSession Send a valid29 bit Normal fixed addressing, N_TAtype=physical address request with the periodicDataIdentifier previously requested with the transmissionMode=02 - ADD DELAY 120s",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="03", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": ({"dddid": "FF", "active": True}),
                "periodics_num": 1,
            },
        )

    # Purpose of the following tests is the use of subfunction 04 of service 2A
    def test_032(self, name="Stop Transmission of Periodic Data Identifier"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2A 04",
            expected={"response": "Positive", "periodics_num": 0},
        )

    def test_033(
        self,
        name="While Server is in extendedSession and multiple DDIDS are defined Send a valid 29 bit Normal fixed addressing, N_TAtype=physical address request with two valid periodicDataIdentifiers",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF FE", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "active": True},
                    {"dddid": "FE", "active": True},
                ),
                "periodics_num": 2,
            },
        )

    def test_034(self, name="stop transmission of PDID FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FF",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "01", "tolerance": 10.0}
                ),
                "periodics_num": 1,
            },
        )

    def test_036(self, name="stop transmission of PDID FE"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            stop_periodic_data="FE",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FE", "rate": "01", "tolerance": 10.0}
                ),
                "periodics_num": 0,
            },
        )

    def test_038(self, name="read PDID mode 01"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            custom="10 03",
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "01", "tolerance": 10.0}
                ),
                "periodics_num": 1,
            },
        )

    def test_040(self, name="Transition to extended Session"):
        test.preconditions(step_info=info())
        test.step(step_title=name, custom="10 03", expected={"response": "Positive"})
        test.step(
            step_title="Verify periodicDataID sent",
            read_periodic_data_id=dict(DDDID="FF", rate="01", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "01", "tolerance": 10.0}
                ),
                "periodics_num": 1,
            },
        )

    def test_042(self, name="DynamicallyDefineDataIdentifier  2C - F0-FF"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 FF F0 80 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FE F0 81 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FD F0 84 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FC F0 89 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 FB F0 8B 01 01",  # F0 8E is not in odx  -->F0 8B
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 FA F0 8F 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 F9 F0 90 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2C 01 F2 F8 F0 91 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F7 F0 92 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F6 F0 94 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F5 F0 95 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F4 F0 A7 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F3 F0 84 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F2 F0 AB 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F1 F0 B3 01 01",
            expected={"response": "Positive"},
        )

        test.preconditions(step_info=info())

        test.step(
            step_title=name,
            custom="2C 01 F2 F0 F0 B4 01 01",
            expected={"response": "Positive"},
        )

    def test_043(self, name="read PDID mode 03 - ADD DELAY 10s"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FF", rate="03", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FF", "rate": "03", "tolerance": 10.0}
                ),
                "periodics_num": 1,
            },
        )

    def test_044(
        self,
        name="While Server is in extendedSession Send a valid 29 bit Normal fixed addresing,N_TAtype=physical address request-FE",
    ):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            read_periodic_data_id=dict(DDDID="FE", rate="02", timeout=10),
            expected={
                "response": "Positive",
                "periodic_verifications": (
                    {"dddid": "FE", "rate": "02", "tolerance": 10.0}
                ),
                "periodics_num": 2,
            },
        )

    def test_046(self, name="<hardreset -extendedSession Physical Messaging>"):
        test.preconditions(step_info=info(), power_mode="OFF")
        # There is no need to re set ignition switch envVariable, that is static so it remains with the same value which was set
        test.step(step_title=name, custom="11 01", expected={"response": "Positive"})

    def test_047(self, name="<Verify all scheduled PIDs are stoped>"):
        test.preconditions(step_info=info())
        test.step(
            step_title=name,
            custom="2A 04",
            expected={"response": "Positive", "periodics_num": 0},
        )
