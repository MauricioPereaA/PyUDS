"""@__global__.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    __global__ module contains variables to be used around the whole framework
        variables specified are open to be modified as per required.
    
@note SPECIFICATIONS:

        __config__           ==> Contains default cfg file. Intented to be modified
                                by GUI.py as per selected from <<combobox>>.

        __workspace__        ==> Absolute path of PyUDS Workspace. This will contain
                                folders such as: Report, Logs, Binaries & PyUDS itself.

        __reports__          ==> Absolute path for Report folder. Container of CGs
                                template reports to be written.

        __logs__             ==> Absolute path for Logs folder. Contains all generated
                                logs by PyUDS Framework.

        __binaries__         ==> Absolute path for binaries folder. Contains the binaries
                                files to use for CG3687.

        __supported_ecus__   ==> All ECUs supported and its corrisponding cfg file.
                                Note: files specified should be placed in path.
                                framework/config otherwise it will not work.

        __supported_cgs__    ==> All CGs supported and its corrisponding filename.
                                Note: files specified should be placed in path
                                specified in __reports__ var.
    
        __default_binaries__ ==> Default binaries files intended to use on CG3687.
                                Note: files specified should be placed in path
                                specified in __binaries__ var.
        
        _no_excel_prompt     ==> Flag that supress Excel prompt that notifies when
                                Excel process is going to be killed.
        
        _running_cg          ==> Variable containing CG that is working on.
                                Intended to dynamically change from one CG
                                to another by PyUDS.
        
        _supress_prompts     ==>    - ENABLES NO USER INTERACTION MODE -
                                allows PyUDS to supress popup prompts, they will 
                                always return 'True' by default
                                * Requires tester debug after it finishes *

        _real_time_report    ==> Results are written while test is running. Each
                                step executed will automatically write results
                                on its conrrisponding CG.

        _binary_app          ==> Variable containing the APP SW currently working on.
                                Intended to dynamically change from one APP SW
                                to another by PyUDS.

        _binary_cal1         ==> Variable containing one of the three calibrations data.
                                Intended to dynamically change from one calibration
                                to another by PyUDS.

        _binary_cal2         ==> Variable containing one of the three calibrations data.
                                Intended to dynamically change from one calibration
                                to another by PyUDS.

        _binary_cal3         ==> Variable containing one of the three calibrations data.
                                Intended to dynamically change from one calibration
                                to another by PyUDS.

*******************************************************************************
"""

import os

__config__ = 'config.cfg'
__workspace__ = os.environ['userprofile'] + '\\Workspace'
__reports__  = __workspace__ + '\\Report'
__binaries__ = __workspace__ + '\\Binary_Files_CG3687'
__logs__     = __workspace__ + '\\Logs'
__canoe_process__ = 'CANoe64.exe'

__supported_ecus__ = {
    'MSM':  'config_MSM.cfg',
    'ARB':  'config_ARB.cfg',
    'PTM':  'config_PTM.cfg',
    'SCL':  'config_SCL.cfg',
    'TCP':  'config_TCP.cfg'
}

__supported_cgs__ = {
    'CG3388': 'CG3388Jun2018_Template.xlsx',
    'CG3531': 'CG3531Aug2018_Template.xlsx',
    'CG4577': 'CG4577 - ARB Blank.xlsx',
    'CG3687': 'CG3687Dec2017.xlsx'
}

__default_binaries__ = {
    'Application':  __binaries__ + '\\app_uncompressed_13533842AA_sif.bin.uc',
    'Calibration_1':__binaries__ + '\\cal_1_13533845AA_sif.bin.uc',
    'Calibration_2':__binaries__ + '\\cal_2_13533844AA_sif.bin.uc',
    'Calibration_3':__binaries__ + '\\cal_3_13533846AA_sif.bin.uc'
}

_running_cg   = None
_no_excel_prompt = False
_supress_prompts = False
_real_time_report = True
_binary_app = None
_binary_cal1 = None
_binary_cal2 = None
_binary_cal3 = None
