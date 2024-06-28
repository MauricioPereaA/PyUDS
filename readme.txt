
/====== PyUDS - Python Unified Diagnostic Services ======/
PYUDS Version 4.2.1
----------------------------------------------------------------
Run GUI mode:
    - Simply double click on GUI.py

	PyUDS - GUI Tabs:
	  - Main:
	    * <CheckBoxes> to filter Test cases by CG.
	    * <ComboBox> to select Test Suite. After selection is made,
		Test cases will get updated.
	    * <Button> Run selected. Run all selected test cases from <ListBox>.
	    * <Button> Stop current test. Stops all running test cases.
	    * <Button> Creates/Appends selected test cases to batch file.
		>>PyUDS_QuickLaunch.bat<< launches Queues of test cases if executed.
	    * <ListBox> Lists all test cases from selected Test Suite in <ComboBox>.

	  - Config:
	    * <CheckBoxes> to select enable/disable features:
		unnatended mode, no excel prompts, no real-time reporting
	    * <ComboBox> to select ECU under test. Supported: MSM, PTM, ARB & ESCL.
	    * <Button> to set selected ECU from <ComboBox> as default.cfg.
	    * <TextArea> containing modifiable real-time selected config from <ComboBox>.
	    * <Button> Saves config.cfg with modifications done in <TextArea>

	  - Reports:
	    * <Radio buttons> Listed CGs to select the one to be written
	    * <Entries> Modifiable paths of CG Reports.
	    * <Buttons> '...' buttons allows user to select Excel file. Path will be 
		reflected on <Entries> once you select an specific file.
	    * <Button> Save changes button allows user to keep settings as selected
		during the current PyUDS session.

----------------------------------------------------------------
Type in a cmd prompt:

    - Help (Simply run PyUDS.py for usage information):

	py PyUDS.py

----------------------------------------------------------------
    - Run All Test Suites

	py PyUDS.py --all

	 OR

	py PyUDS.py -a

----------------------------------------------------------------

   - Running multiple test suites:

	py PyUDS.py --run "<Test 1>,<Test 2>"

	 OR

	py PyUDS.py -r "<Test 1>,<Test 2>"

----------------------------------------------------------------

   - Running specific test case(s) from a test suite:

	py PyUDS.py --run "<Test 1>" --testcase "<Specific Test 1>, <Specific Test 2>"

	 OR

	py PyUDS.py -r "<Test 1>" -t "<Specific Test 1>"

----------------------------------------------------------------
    
    NOTE: It is not required to use the whole filename, just what identifies it.
    Example:  py PyUDS.py -r "COMMON_DIDs"


Changes:
  ====== PyUDS v2.0 ====== 
 - TestClass is now implemented. New layer design for easier interpretation and creation of test cases.
 - Jobs/Runner files are now in one simplier main file called PyUDS. All UnitTest modules are imported dinamically from 'Testcases' folder.
 - Testcases do not require SETUP, CLEANUP and SHARED_FUNCTIONS modules. Everything is now executed from the TestClass. Find it inside 'Testcases' folder.
 - 'config.ini' file inside each test suite folder implemented to specify excluded test cases from the suite.
 - 'UDS_Services' class contains all objects and methods declared inside a dictionary to be called from TestClass.

  ====== PyUDS v2.1 ====== 
 - 'UDS_Services' optimized. Only one object is created at the beggining of the test, and the same is used until the end of it.
 - 'Canoe_Diagnostics':
	* Functional request read-out response works more efficiently.
	* Tester Present stopping fixed.
 - 'Excel_COM' automatically determines if running CG3388 or CG3531 (These are the only ones supported)
 - 'TestClass':
	* 'mec_zero' & 'sbat' preconditions are now implemented. See documentation, preconditions section for usage details.
	* 'envVariable' precondition implemented, also for multiple variables. See documentation, preconditions section for usage details.
 - Logger: removed error when no tester_report is present.
 - 'config.cfg' more data required for PyUDS usage. Added [SBAT] block & valid_key, Network & physical/functional IDs. + open_cfg_each_test added
	* open_cfg_each_test parameter to Enable if you want to re-open CANoe cfg every test case PyUDS launches.
	NOTE: If you set this parameter to Enable/True, please make sure proper cfg is already open.
 - 'Examples' added. Recommended to run each one of them if is the first time you use PyUDS.

  ====== PyUDS v2.1.1 ====== 
 - Added HTML report based on a -Bootstrap- CSS for easier visualization.
 - Added conditionals specifically used for DOORs generated test cases.
 - Added fixes for UDS Services. More efficient UDS message concatenation.
 - Security Access implementation
	* 'CMAC_AES' class implemented for service 0x27. Generates an encrypted key to access all Security Levels.
 - Power Supply Keysight N5744 supported
	* 'KeySight_N5744' class for power supply manipulation through PyUDS
 - 'TestClass':
	* 'ignition_switch', able to change from one power mode to another as precondition. -Required to run CG3531 - Security Access-
	* Supports Key encryption for CG3531 - 021E
	* 'KeySight_N5744' implemented for 'reset_communication' method.
 - 'config.cfg' contains power_supplies field for 'reset_communication'.
	* If model is set as None, TestClass will let you do 'reset_communication' manually by turning OFF & ON your power supply.
 - 'shared_functions' new name for previously named GLOBAL_SHARED_FUNCTIONS.
 - Added debug data to HTMLReport & debug.log.
 - Logger now clears logs if previous run was not completed successfully.
 - SBAT & MEC_ZERO preconditions now are working properly with CMAC_AES encryption (Required to enter Sec Level 01).
 - Service Class 0x31 - 'Routine_Control' Added.
 - Method catch_error_frames() added to diagnostics. In order to wake up the BUS if it gets down during test initialization.

  ====== PyUDS v2.2 ====== 
 - Added 'multiple_request' for NRC 0x21 tests
 - Added 'set_dtc_condition' for simple Under voltage & Over voltage automation. Power supply is required. Otherwise it will prompt manual action
 - Fixed 'functional' for custom UDS requests
 - Added 'partialData' as expected for validation.
 - Added new test cases for CG3388 and fixed some others for CG3531.
 - JSON reports implemented.
 - JSON data analysis partially implemented. To be finished on next version.
 - Added few Examples Testscripts for new implementations.
 - Added BETA 'GUI.py' based on tkinter lib for easier test case selection.

  ====== PyUDS v2.2.1 ====== 

 - Added under/over voltage values on config.cfg
 - Deleted 'update test cases' button from GUI. 
 	* Functionality changed for dynamic refreshing list.
 - Added 'ECU_Reset' as service class.

  ====== PyUDS v2.2.2 ====== 

 - Added Diagnostic Fault Detection capabilities
 	* 'cmd_Thread' able to launch second thread to increment TimeSync signal in parallel
 - Added Network Supervision write on CG report capability
 - Added complete failures description for Excel CG report writing
 - Implemented 'timer.input' feature to wait for user prompt for certain period of time, if no reponse received and timeout is reached, a default response is received + Test case continues its execution
 - Added 'test_rows.generate_json' for easier test_rows generation. - Required to know where to write on CG -
 - PyUDS Launcher supports -config.cfg change-.
 - PyUDS GUI -config tab- added for easier -config.cfg change- usage. Supported ECU listed in __global__
 - Added __global__ lib. Includes required global variables used accross the whole framework.
 - Added 'Network supervision TC12' Clear DTCs preconditions.


  ====== PyUDS v2.2.3.4 ====== 
 - Added 'Network supervision TC12' Clear DTCs preconditions.
 - Added 'Diagnostic Fault Detection' TC04 for ARB/PTM & fixed TC03
 - Network Supervision TC02 - Operation cycle for ARB/PTM without ignition OFF-RUN-OFF.
 - Added 'supported_dids' JSON dictionary containing all DIDs supported for ARB, PTM, MSM & SCL


  ====== PyUDS v2.2.4.4 ====== 
 - Added popup windows and prompts when user interaction is required
 - Excel COM alerts when excel process is running and is going to be killed
 - HTML report contains INFO regarding Signal changes
 - Improved 'multiple_tester' method to provide NRC 0x21 from any of both testers
 - Fixed Excel 'select range' error from Excel COM lib

  ====== PyUDS v2.2.4.5 ====== 
 - Added flags and description in __global__ file.
 - Fixed Excel log insert method.
 - Added supress prompts for unnatended mode.
 - Added GUI Button to create Batch script to run PyUDS test script queue.
 - Added options in GUI Config tab. *TEMPORARY DISABLED* This is just a place-holder.
 - Added IO DIDs and Services supported to JSON dictionaries.

  ====== PyUDS v2.2.4.6 ====== 
 - Enabled options from Config tab. 
	* Unnatended mode, No Excel prompts, Disable real-time CG report
 - Added Reports tab on GUI for Reporting settings, like Excel file path.
 - Supported Nested Namespace for System variables. CANoe Driver adapted.
 - Added new Reports tab. For CG Excel file selection.
 - Report analyzer added from GUI. Found in Reports tab.
 - Removed settings from config.cfg and placed at __global__.py settings.
 - CANOE block from config.cfg file now contains all settings regarding COM Server interaction.
 - INFO block from config.cfg file contains suplier information to fill CG3388 report.
 - Added Overall results report (html) to provide JSON result analysis and generate HTML report out of results obtained.
 - JSON Handler adapted to recursively search into Log folders to find JSON results.
 - test.compare() method adds rows to HTML report.
 - Fixed global variable 'template_path' for TestClass.
 - Logger methods changed to PEP8.
 - diagnostics Error logging improved to know whether you are using an incorrect config file.
 
  ====== PyUDS v2.2.4.7 ====== 
- Fixed Issue where PyUDS did not write on the CG3531 Excel Report
- Added correct CG report to fill according to the selected CG report
	* Warns the user if the selected CG report does not match with the test script to be executed

  ====== PyUDS v2.2.5.1 BETA ====== 
- Added feature were the user can select any CG to take into account for the tool to write into the report
- Modified __global__.py to include variables containing the path and control for binary files
- Added library "binary_file_handler.py" to handle all the binaries files specified by the user intended to
  use for the tests on CG3687
- Modified GUI for the user be able to specify the binary files to be used on CG3687
	*Note_1: Binaries folder containing binary files should be placed in the PyUDS workspace
		 (the same one where the reports / logs are)
	*Note_2: The test scripts for CG3687 may not be entirely correct and at the current moment.
	         the test results are not being written on the excel file.

  ====== PyUDS v2.2.5.2 ====== 
- Added normal_comm method on diagnostic.py to verify normal communication
- Added test_rows.json file for the tool be able to write on the corresponding CG3687 tests of tab 
	Gen_boot_requirements
- Modified TestClass module to use specific tests of CG3687 
- Updated the default binaries path on __global__.py module
- Scripts for CG3687 Tab Gen_Boot_requirements updated to follow the CG3687
- Note:
	Pending to full implement the method for the power supply in order to measure the output current.

  ====== PyUDS v2.2.5.3 ======
- Fixed power supply settings, the setting of undervoltage and over voltage was swapped
- Updated normal_comm method on diagnostyic.py to dynamically check the current ASC log file
- Updated packets_to_send method on binary_file_handler to be used on Robustness tab of CG3687
- Added methods get_current and get_voltage on power_supply.py to read the output voltage and current
- Added scripts for Robustness tab of CG3687
- Added test_rows.json file for Robustness tab of CG3687
- Added decorador @log to log the methods inside the GUI

  ====== PyUDS v2.2.5.4 ======
- Updated diagnostic.py module in order to verify the response from the log
- Updated test class module for tests that correspond to test that require changing the testers ID response 
- Updated GUI.py module to warn the user if no test script is selected and the button "Run selected" is clicked
- Added new library diagnostic_address_support to test specific test cases of diagnostic address tab of CG3687
	using the newly implemented CAPLs
- Added scripts for Diagnostic Address Support tab of CG3687 (PTM)
- Added test_rows.json file for Diagnostic Address Support tab of CG3687

  ====== PyUDS v2.2.5.5 ======
- Updated validateClass.py module to validate multiple expected NRC codes as well as
	validate multiple bytes in a response (for EX. to check that are no '00' and 'FF' in a response)
- Updated testClass.py module, now partialData can be either a tuple or a string in order to verify multiple responses
- Updated diagnostic.py module - normal_comm method, the number of CAN_ID messages was modified from 5 to 4
- Updated diagnostic.py module - get_response_from_log / catch_error_frames, the number of lines to read from log was increased from 50 to 100
	and 20 to 35 respectively. Also, the physical IDs now can be changed properly (get_response_from_log method)
- Scripts of __Examples__ folder updated to fulfill the purpose of the test (test_02, test_21)
- Scripts of Gen Boot Requirements tab were updated for the PTM Module
- Scripts for the ECU_Proc_Modes tab of CG3687 are added in this version
- Scripts for the Proc_Modes_Details tab of CG3687 are added in this version

  ====== PyUDS v2.2.5.6 ======
- GUI updated to be clearer about the overall report, specifically the HTML report
- Issue Item CFTNA-5078 fixed, now the Report directory path can be changed via GUI
- TCP module added to the GUI
- TC-GUI.xlsx file updated, now there are more test cases to test the GUI
- Updated diagnostic.py - get_response_from_log method, now takes into account the functional request to look
	into the working trace_log as well as the lines to analyze incremented
- Scripts of the programming error code tab of CG3687 added (still work to do on this)

  ====== PyUDS v2.2.5.7 ======
- Modified supplier_info.py to take ECU from the CANOE config instead of INFO
- Pending to add method for binary_file_handler.py to modify binaries specific parameters
- Scripts of the programming error code tab of CG3687 added
- Advance of comp_hand tab of CG3687 scripts added

  ====== PyUDS v2.2.5.8 ======
- TCP config file updated
- Shared functions library modified to include TCP ECU
- partial_networks, supported_dids, supported_rids UDS .json files updated to include TCP ECU
- Prog_Sess_Det tab of CG3687 test scripts added (still work to do on this one)
- Comp_hand tab of CG3687 test scripts added
- Prog_Data_Files tab of CG3687 test scripts added

  ====== PyUDS v2.2.6.1 ======
- TestClass.py updated. Added parameters expected_byte and byte_index to validate an specific byte in the response.
	Also, modified uds_service method to send functional request of Security Level seeds
- validateClass.py updated. added the logic to validate the specified expected byte.
- Supported dids.json updated. Added session precondition and rationality check
- CG3531 test scripts updated

  ====== PyUDS v3.0.0 ======
  30/Nov/2020
  PyUDS Core
- __version__.py Updated the Version of PYUDS because it has information about CG 2020
- Deleted Files. Documentation Folder, the content was updated and moved to next link 
- libs_64bits.7z and PyUDS 2.2.6.1.zip has redundant information
- install.py Updated the Install.py, now is not neccesary to decompress the PYUDS_XXX.zip for installation, it only install the offline libraries, added libraries contextlib2==0.6.0.post1 and schema==0.7.2 that given support to service 2A
- libs_64bit and libs_32bit folders was updated the information
- validateClass.py Added in the function validate the positive response for request 19 02 that generate the dtc_list and compare the initial_dtcs vs current_dtcs
        periodic_data verification routine was modified to accept a results as tuple of dictionaries
- TestClass.py Added the attribute last_dtcs Storage the self.last_dtcs activated without status and self.initial_dtcs that Storage the first list of dtc's
	Also added the data_dtc parameter that receive as input (string or list or string + list in a tuple) at the end merged the data structure
        Logic to verificate 2A Service was replaced, the new approach is a mixed implementation
        based on CAPL and Python
- Canoe.py set_system_variable was enhanced to support more datatypes, before only boolean was supported and now
        most of the variable types are accepted like Integer ,Float, String, Float Array, Integer Array, LongLong and Byte Array
        PyUDS Scripts
- Test_27_Data_Dtc.py Validated the data_dtc parameter it was included in the examples folder
- Test_29_Digital_IO.pu Validated the digital IO it was included in the example folder
- NetworkSupervision_TC03.py Implemented the data_dtc_parameter in the CG35331_NetworkSupervision Folder
- test_rows.json Updated this file for writing correctly the NetworkSupervision_TC03
- Test_28_2A_Service.py Validated the 2AService it was included in the examples folder
