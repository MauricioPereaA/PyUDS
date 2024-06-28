"""@shared_functions.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    SHARED FUNCTIONS imports the whole libraries required for framework 
    usage, defines the Enviroment paths and multiple functions to perform the
    whole validation process.
    
@note ABBREVIATIONS:
        - uds: Unified Diagnostic Services
*******************************************************************************
"""
#==============================================================================
# Python Standard import packages
#==============================================================================
import inspect
import os
import sys
import time
import unittest
import shutil
import random

#==============================================================================
# Update PYTHONPATH
#==============================================================================
automation_home = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
PyUDS = os.path.dirname( automation_home )
sys.path.insert(0, PyUDS)
sys.path.insert(0, os.path.abspath(__file__) )
sys.path.insert(0, automation_home + '/UDS')
sys.path.insert(0, automation_home + '/framework')
sys.path.insert(0, automation_home + '/framework/config')
sys.path.insert(0, automation_home + '/framework/tools')
sys.path.insert(0, automation_home + '/framework/drivers/Vector_COM')
sys.path.insert(0, automation_home + '/framework/drivers/Excel_COM')
sys.path.insert(0, automation_home + '/framework/drivers/Power_Supply')

#===============================================================================
# Custom modules
#===============================================================================

#from __global__ import __supported_cgs__, __supported_ecus__, __reports__, __logs__, _running_cg
from framework.drivers.Power_Supply import *
from framework.validateClass import validate
from read_config import read_cfg_file
from logs import Logger
from CANoe import CANTool
import PyUDS
import configparser
import argparse
import misc as tools
import __global__

#===============================================================================
# Global variables
#===============================================================================

# Paths    
report_path = __global__.__reports__
default_cg = 'CG3388'
if default_cg == __global__._running_cg:
    template_path = __global__.__supported_cgs__.get(default_cg)

elif 'CG3531' == __global__._running_cg:
    template_path = __global__.__supported_cgs__.get('CG3531')

elif 'CG4577' == __global__._running_cg:
    template_path = __global__.__supported_cgs__.get('CG4577')
else:
    template_path = __global__._running_cg

LogsPath = __global__.__logs__
test_cases_path = automation_home + '\\Testcases'

# Execution info
info = {
    'sw_version'  : read_cfg_file('INFO', 'sw_version', False),
    'cadence'     : read_cfg_file('INFO', 'cadence', False)
}
ECU_info = {
    'name'   : read_cfg_file('CANOE', 'ECU', False),
    'network': read_cfg_file('CANOE', 'Network', False)
}

# CMAC AES - CyberSec
#encryption_ecu_key = read_cfg_file('CMAC_AES_Cyber_Security', 'ecu_key', False)

sleep_timeout = int(read_cfg_file('INFO', 'sleep_timeout', False))
supported_ecus = ['MSM', 'PTM', 'ARB', 'SCL','TCP']
no_io_ecus = ['SCL', 'TCP']
device_under_test = tools.device_under_test(supported_ecus, ECU_info['name'])

pn_dict = tools.readJSON(automation_home + '\\UDS\\partial_networks.json')
ARC_sys_vars = tools.readJSON(automation_home + '\\UDS\\sys_vars.json')

if device_under_test != '':
    read_supported_dids = tools.readJSON(automation_home + '\\UDS\\supported_dids.json')['read'][device_under_test]
    write_supported_dids = tools.readJSON(automation_home + '\\UDS\\supported_dids.json')['write'][device_under_test]
    supported_rids = tools.readJSON(automation_home + '\\UDS\\supported_rids.json')[device_under_test]
    supported_services = tools.readJSON(automation_home + '\\UDS\\services.json')[device_under_test]
    if device_under_test not in no_io_ecus:
        supported_io_dids = tools.readJSON(automation_home + '\\UDS\\supported_dids.json')["io"][device_under_test]
    else:
        supported_io_dids = None
else:
    read_supported_dids, write_supported_dids, supported_rids, supported_services = (None, None, None, None)
    print('Make sure {} has been defined in: {}'.format(
        ECU_info['name'], *('supported_dids.json', 'supported_dids.json', 'supported_rids.json', 'services.json')
    ))

valid_SBAT = read_cfg_file('SBAT', 'valid_key', False)
keys = tools.readJSON(automation_home + '\\UDS\\keys.json')


# Power Supply Settings #
power_supply_model = read_cfg_file('POWER_SUPPLY', 'model', False)
under_voltage = float(read_cfg_file('POWER_SUPPLY', 'under_voltage', False))
over_voltage = float(read_cfg_file('POWER_SUPPLY', 'over_voltage', False))

TestResult = {
    True: 'PASSED',
    False: 'FAILED'
}

#===============================================================================
# Global Objects
#===============================================================================

canoe = CANTool()
Logger = Logger()