"""@configuration.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    "A configuration file consists of sections, lead by a "[section]" header,
    and followed by "name: value" entries.
    "

@note ABBREVIATIONS:
        - N/A
*******************************************************************************
"""
from __global__ import __config__, __workspace__
from configparser import ConfigParser
from framework.tools.logs import Logger
import misc as tools
import os

cfg_file = os.path.dirname(os.path.abspath((__file__))) + os.sep + __config__
_workspace = __workspace__
Logger = Logger()
def get_test_filename(file_path):
    """
    *******************************************************************
    FUNCTION:  get_test_filename

    PURPOSE:
        Returns the path of the file that for test logging..

    PARAMETERS:
        file_path - contains the entire path of the module under test.

    RETURN:
        test_filename - Name of test file for logging messages.
    *******************************************************************
    """
    test_filename = os.path.basename(os.path.dirname(
                                     os.path.dirname(
                                     os.path.dirname(
                                     os.path.abspath(file_path)))))
    return test_filename

def read_cfg_file(section, option, includeRoot=True):
    """
    *******************************************************************
    FUNCTION:  read_cfg_file

    PURPOSE:
        To read parameters (option) stored in a configuration file

    PARAMETERS:
        test_path - Project file path (configuration file is located
                    in a relative path from the project path)
        section - Name of the group of parameters
        option - Name of the parameter to read

    RETURN:
            value - int or str value
    *******************************************************************
    """
    try:
        tools.isFolder(_workspace)

        parser = ConfigParser()
        parser.read(cfg_file)
        if includeRoot:
            cfg_value = os.path.join(
                _workspace, 
                parser.get(section, option)
            )
        else:
            cfg_value = parser.get(section, option)
        
        return cfg_value
    except Exception as error:
        Logger.write_debug_log('ERROR', __name__, error)
        print(__name__, error)