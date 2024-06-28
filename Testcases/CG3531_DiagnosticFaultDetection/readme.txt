Diagnostic Fault Detection - TC03:
  Service 0x19 Subfunctions supported differs for each project. Find inside this folder the respective scripts for each ECU (ARB, MSM, ESCL & PTM)


Diagnostic Fault Detection - TC09:
  This test case is only applicable for MSM. Only Not applicable Steps are:
  - Step 9-2 : 'Generate conditions to set the permanently latched DTC (DTC3)' is already achieved by flashing MSM using -Default Calibrations-
  - Step 9-3 : 'Remove vehicle conditions that set DTC3' is only achieved by reflashing MSM and modifying/removing default calibrations.
 		Purpose of the test cannot be acheived if a reflash is performed during this test case execution, hence, test step is Not applicable.


Diagnostic Fault Detection - TC10:
  In order to properly execute this test case, it should be performed on the first time Power Up. (After a reflash)

Diagnostic Fault Detection - TC11:
  Steps 11-5 to 11-7 requires DPS Flash. Perform and provide the log manually to complete the report as it requires.
  Steps 11-8 to 11-21, Timing between triggered message (DTC_Info) and activation of DTCs cannot be achieved under black box testing.