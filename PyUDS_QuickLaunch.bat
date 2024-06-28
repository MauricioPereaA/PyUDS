@echo off
py PyUDS.py -r __Examples__ -t Test_01_CanoeSimulation -e default --cg "CG3388Jun2018_Template.xlsx" 
py PyUDS.py -r __Examples__ -t Test_00_1_Basic_Test_Begin,Test_00_Basic_PyUDS_TestScript,Test_01_CanoeSimulation,Test_02_Read_Data_ID,Test_03_Excel,Test_04_AllServices,Test_05_SecurityLevels,Test_06_Signals_EnvVariables,Test_07_Step_delay,Test_08_SecurityLevels_CMAC_AES_Encryption,-,Copy,Test_09_Ignition_switch,Test_10_Signals+Custom_UDS -e default --cg "CG3388Jun2018_Template.xlsx" 
