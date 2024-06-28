"""@TestClass.py
*********************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential
@Description:
    PyUDS TestCase Class -  Base template for easier UDS TestScripts implementation

@TestScript body
    >> test = TestCase()
    >> test.begin(*params)
    >> test.step(*params)
    >> test.end()
    
Modified by Mauricio Perea
Date:13 July 2020
This script was fixed for recognize the RBS path and run correctly using the config_***.cfg file
Modified by Mauricio Perea
Date:03/09/2020
Add the Attribute RBS in TestCaseClass and it is implemented in the verification
Fix the sw_prog_state read the correct byte in the dataframe
Modified by Mauricio Perea
Date:04/11/2020
Added the attribute last_dtcs Storage the self.last_dtcs activated without status and self.initial_dtcs that Storage the first list of dtc's
Also added the data_dtc parameter that receive as input (string or list or string + list in a tuple) at the end merged the data structure 
Modified by Mauricio Perea
Date:10 November 2020
Addition of 2A Servicel Full Automation, code for parameters "periodics_verification"
and "periodics_num" were added
Callback if on every response for 2A service was added
SchemaError package as dependency was added
Custom rates for service 2A from INI file were added
Modified by Mauricio Perea
Date:20 September 2021
Addition of WriteWindow logfile when a test case is executed, the information displayed at CANoe Write Window is saved to a logfile with
the name: TesCaseName_WriteWindow.txt
There is a routine to erase the content from a generic buffer file when it is too large, it is because when the simulation starts
the data is saved to a generic file names: WriteWindow.txt instead the oficial logfile, we need to do this because the syncronization
of CANoe with the new logfile takes some time.
A new verification for NRC 0x78 was added it uses the System Variable Counter from the  UDS Engine to evaluate this functionality.
A Hardware Abstraction Layer for the Power Supply was added.
The logic for Service 2A with Scheduler 1 was modified to use the new Rates_2A property.
"""
from __global__ import _real_time_report, __reports__
from framework.drivers.Excel_COM.Excel import ExcelTool
from framework.shared_libs.supplier_info import SupplierInfo
from framework.shared_functions import *
from framework.tools.logs import Logger
from misc import FileExists
from __version__ import __version__
from UDS.UDS_Services import *
from __global__ import _running_cg
from schema import Schema, And, Use, Optional, SchemaError
from framework.drivers.Power_Supply.power_supply import *

import inspect, os

# ================================================
#  CG Properties: CG3388 flag & log/result columns
# ================================================
template_path = template_path if template_path != None else ''  # Added by Evan
cg3388 = lambda: 1 if '3388' in template_path else 0
is_full_path = lambda x: True if ':\\' in x else False
_result_column = 5 + cg3388()
_log_column = 6 + cg3388()


class TestCase(UDS_Services):
    def __init__(self, **kwargs):

        # ================================================
        #  Objects: CANoe Driver, Logger and Power Supply
        # ================================================

        self.canoe = CANTool()
        self.Logger = Logger()
        if power_supply_model != 'None':
            if not hasattr(power_supply, power_supply_model):
                _ERROR = 'CONFIG - Specified power supply %s is not supported.' % power_supply_model
                self.Logger.write_debug_log('ERROR', __name__, _ERROR)
                raise ValueError(_ERROR)
            # AYanez PS HAL
            PS_Model = read_cfg_file('POWER_SUPPLY', 'model', False)
            PS_HW_Interface = read_cfg_file('POWER_SUPPLY', 'HW_interface', False)
            PS_Address = read_cfg_file('POWER_SUPPLY', 'address', False)
            PS_COM_Options = read_cfg_file('POWER_SUPPLY', 'COM_options', False)
            self.power_supply = PowerSupplyFactory().get_powersupply(PS_Model, PS_HW_Interface, PS_Address, PS_COM_Options)

        else:
            self.power_supply = None

        # ================================================
        #  Init Values: 
        #   - Physical Addressed Request
        #   - Test Results on Excel
        #   - MEC in 00
        #   - SBAT in 00's
        #   - Tester Present    Enabled
        #   - Debug mode        Disabled
        # ================================================

        self.functionalAddr = None
        self.response_from_log = False
        self.writeTestResults = False  # Test Results on Excel 'ENABLED'
        self.mec_zero = False
        self.sbat = False  # True = Valid SBAT | False = 00's
        self.report_log_active = False  # False - Changes if expected param is declared at any step
        self.tester_present = True  # Enabled by Default
        self.step_delay = 0.20  # 20 ms by Default
        self.security_seed = '00' * 32  # Empty seed
        self.debug_mode = False
        self.request = ''
        self.tester_id = 'default'
        self.physical_id_rsp = '14DAF1A4x'
        self.underVoltage = under_voltage  # Imported from
        self.overVoltage = over_voltage  # shared_functions
        self.periodic_data = None  # Required flag for service 0x2A usage
        self.latest_response = None  # Stores latest response received from ECU
        self.rbs_path = None
        self.attributes = {}
        self.last_dtcs = []  # Storage the last dtcs activated without status, each dtc in a list
        self.initial_dtcs =[] # Storage the first list of dtc's
        self.rates_2A = {'01': 1.000,'02': 0.200,'03': 0.025}
        self.scheduler_2A = '1'

        global template_path
        self.template_path = template_path

        _pyuds_version = 'Running on PyUDS v%s' % __version__
        self.Logger.write_debug_log('DEBUG', __name__, _pyuds_version)

    def begin(self, suite='Examples', test_path=test_cases_path,
              test_name='Test_01_CanoeSimulation', **kwargs):
        """
        =======================================================================
        # begin() - Start RBS, Excel object, etc...
        =======================================================================
        """
        try:
            ''' Initial begin() params '''
            if 'test_info' in kwargs:
                self.test_path = os.path.dirname(
                    os.path.abspath(kwargs['test_info'][0][1])
                )
                self.suite = self.test_path.split('\\')[-1]
                self.file_name = kwargs['test_info'][0][1].replace(
                    self.test_path + '\\', ''
                ).replace('.py', '')
            else:
                self.test_path = test_path
                self.suite = suite
                self.file_name = test_name

            
            ''' Initialize Logger HTML + Clear Logs '''
            self.Logger.clear_logs(self.file_name)
            self.Logger.beginHTML()

            print(
                '\n    #' + '=' * 72 + \
                '\n    # Starting %s' % self.file_name + \
                '\n    #' + '=' * 72, end='\n\n'
            )

            ''' JSON Report append test info'''
            self.Logger.append_info(
                test_suite=self.file_name,
                suite=self.suite,
                sw_version=info['sw_version']
            )

            ''' Load RBS configuration '''
            self.rbs_path = read_cfg_file('CANOE', 'config_path')

            ''' Check if cfg path is valid '''
            if (FileExists(self.rbs_path)):
                self.canoe.open(self.rbs_path)
            else:
                tools.popup.warning(title='Invalid Configuration Path',
                                    description='The CANoe configuration filepath given at INI file is invalid, please fix it.')

                sys.exit("PyUDS cannot start due Invalid CANoe Configuration path from INI file.")

            ''' Trace Log configuration '''
            self.canoe.log_settings(path=LogsPath + '\\TraceLog.asc')

            ''' UDS Services Initialization'''
            UDS_Services.__init__(self)

            ''' DEBUG Mode on Excel Report'''
            if 'debug_mode' in kwargs:
                self.debug_mode = kwargs['debug_mode']

            ''' Test Params '''
            if 'step_delay' in kwargs:
                self.step_delay = float(kwargs['step_delay'])
            
            ''' DUT Power UP '''
            if self.power_supply != None:
                self.power_supply.output(True)

            ''' Start Simulation '''
            # - Start Measurement -
            # Clear Temporal Buffer File if is too large
            if (FileExists(LogsPath + '\\' + 'writewindow.txt')):
                if(os.path.getsize(LogsPath + '\\' + 'writewindow.txt') > 1000000):
                    open(LogsPath + '\\' + 'writewindow.txt', 'w').close()
            # AYanez Write Window Log        
            self.canoe.App.UI.Write.EnableOutputFile(LogsPath + '\\' + self.file_name + '_writewindow.txt', 0)
            self.canoe.start()
            time.sleep(0.25)
            
            # Default/Project PDID Rates, values given in Seconds
            for rate_key in self.rates_2A:
                rate_value = read_cfg_file('SID_2A', rate_key, False)
                if isinstance(rate_value, str):
                    self.rates_2A[rate_key] = float(rate_value)
            scheduler_type = read_cfg_file('SID_2A', 'scheduler', False)
            if scheduler_type == '1' or scheduler_type == '2':
                self.scheduler_2A = read_cfg_file('SID_2A', 'scheduler', False)
            self.canoe.set_system_variable('Periodic_DID', 'Rates', list(self.rates_2A.values()))
            time.sleep(1)
            
            # - Send WakeUp Frame -
            self.canoe.set_envVariable(envVNMFSend=1)
            time.sleep(2.5)

            attempts = 0
            while (self.catch_error_frames() and attempts < 5):  # Try to restablish communication
                self.restart_communication()
                attempts += 1
                time.sleep(1.5)
            if self.catch_error_frames():
                raise RuntimeError('CRITICAL - Not able to proceed, CAN bus is OFF!')

            if not self.canoe.App.Measurement.Running:
                raise RuntimeError('ERROR - Not able to start CANoe Simulation')

            ''' Excel COM '''

            if 'writeTestResults' in kwargs:
                if not isinstance(kwargs['writeTestResults'], bool):
                    raise ValueError('ERROR - -> writeTestResults <- must be a boolean.')
                self.writeTestResults = kwargs['writeTestResults']

            if self.writeTestResults and _real_time_report:
                # - Excel COM Object -
                #    * template_path & report_path variables defined in config.cfg*
                if not is_full_path(self.template_path):  # If relative path, will go through
                    self.template_path = __reports__ + '\\' + self.template_path
                self.excel = ExcelTool(self.template_path, report_path)

                # - Excel Tab -
                if not 'excel_tab' in kwargs:
                    raise RuntimeError('ERROR - Please specify -> excel_tab <- in params')

                # - Test Rows for Excel CG Report -
                json_file = self.test_path + '\\test_rows.json'
                if not os.path.isfile(json_file):
                    raise RuntimeError('test_rows.json file does not exist. It is required' \
                                       + ' to write test results on Excel')

                self.TestcaseRow = tools.readJSON(json_file)

                self.SheetName = kwargs['excel_tab']
                self.TestcaseRow = self.TestcaseRow[self.file_name]

                # - Supplier info | Only for CG3388 -
                if cg3388():
                    self.supplier_info = SupplierInfo(self.excel, self.SheetName)

        except Exception as error:
            self.Logger.write_debug_log('ERROR', __name__, error)
            print(__name__, 'begin()', type(error).__name__, error,
                  'Line %s' % (sys.exc_info()[2].tb_lineno))

    def preconditions(self, current_step='test_001', **kwargs):

        try:
            ''' Current Step '''
            if 'step_info' in kwargs:
                if isinstance(kwargs['step_info'], list):
                    self.current_step = kwargs['step_info'][0][3]
            else:
                self.current_step = current_step

            ''' Transmit In OFF '''
            if 'transmit_in_off' in kwargs:
                if kwargs['transmit_in_off']:
                    self.canoe.transmit_in_off()  # Enabled
                    self.Logger.write_on_report(
                        self.Logger.generate_row(
                            tools.timeStamp(), self.suite,
                            'precondition::transmit_in_off()',
                            'INFO', 'Enabling Transmit in OFF'
                        )
                    )

            ''' MEC Zero '''
            if 'mec_zero' in kwargs:
                mec = self.send('22 F1 A0', False, True, quiet_mode=True)
                if kwargs['mec_zero']:
                    # MEC = 00 if required
                    if not '0x00' in mec:
                        print('MEC is not 00', mec)
                        self.send('2E F1 A0 00', False, True, quiet_mode=True)
                        self.Logger.write_on_report(
                            self.Logger.generate_row(
                                tools.timeStamp(), self.suite,
                                'precondition::mec_zero()',
                                'INFO', 'Writting MEC to 00'
                            )
                        )
                else:
                    # MEC > 00 if required
                    if '0x00' in mec:
                        _error = ('\n\n\n ** MEC > 0 is required. Please reflash the ECU manually and try ' + \
                                  'again... ** \n* * * Any result you get from this will not be valid. * * *\n\n')
                        tools.popup.error(title='MEC > 0 is required!', description=_error)
                        raise Warning(_error)

            ''' SW State '''
            if 'sw_prog_state' in kwargs:

                if isinstance(kwargs['sw_prog_state'], str):

                    ECU_SW_status = {'FULL': '0x00', 'SW_MISSING': '0x01', 'CAL_MISSING': '0x02', 'NEED_PROG': '0x03',
                                     'MEM_ERR': '0x50'}
                    if kwargs['sw_prog_state'].upper() in ECU_SW_status:

                        state = self.send('31 01 FF 01', False, True, quiet_mode=True)

                        if ECU_SW_status[kwargs['sw_prog_state'].upper()] != state[4]:

                            tools.popup.warning(title='SW Validation',
                                                description='SW State currently is {} ={}, which is different to request {} ={}'.format(
                                                    list(ECU_SW_status.keys())[
                                                        list(ECU_SW_status.values()).index(state[4])], state[4],
                                                    kwargs['sw_prog_state'].upper(),
                                                    ECU_SW_status[kwargs['sw_prog_state'].upper()]))

                            print('SW State currently is {} ={}, which is different to request {} ={}'.format(
                                list(ECU_SW_status.keys())[list(ECU_SW_status.values()).index(state[4])], state[4],
                                kwargs['sw_prog_state'].upper(), ECU_SW_status[kwargs['sw_prog_state'].upper()]))

                        else:

                            print('SW Prog State is {} according to expected'.format(kwargs['sw_prog_state'].upper()))

                    else:

                        validvals = ', '.join(ECU_SW_status.keys())
                        print('Script Syntax Error. SW State parameter: "{}" is invalid, valid options are: {}'.format(
                            kwargs['sw_prog_state'], validvals))
                        tools.popup.warning(title='SW Validation',
                                            description='SW State Parameter is not valid')
                        raise ValueError('Script Syntax Error. Invalid sw_prog_state value was given')

                else:

                    raise ValueError('sw_prog_state must be string value, script passed a different datatype')

            ''' SBAT '''
            if 'sbat' in kwargs:
                def enter_security_level(level='01'):
                    # Extended Session
                    self.send('10 03', False, True, quiet_mode=True)
                    self.send('3E 80', False, True, quiet_mode=True)
                    # Service object   
                    sec_access = service.obj('request_seed')
                    # key = CMAC_AES encrypted Seed
                    seed = tools.readable_hex(self.send(
                        sec_access.request_seed(level),
                        False, True, quiet_mode=True
                    ))[2:].replace(' ', '')
                    self.send(sec_access.send_key(level, seed), False, True, quiet_mode=True)

                read_sbat = self.send('22 F0 F4', False, True, quiet_mode=True)
                if kwargs['sbat']:  # True  | Set valid SBAT
                    for i, byte in enumerate(read_sbat[3:]):
                        if not '0X' + valid_SBAT[i * 2:(i * 2) + 2] in byte.upper():
                            print('SBAT is not valid. Attempting to write new value')
                            while True:
                                try:
                                    enter_security_level()
                                except Exception:
                                    pass
                                sbat_rsp = self.send(
                                    '2E F0 F4 ' + valid_SBAT, False, True, quiet_mode=True)

                                if not sbat_rsp[-1] in ['0x31', '0x33']:
                                    break
                                enter_security_level()

                            break
                else:  # False | Clear SBAT - 00's
                    for byte in read_sbat[3:]:
                        if not '0x00' in byte:
                            print('Clearing SBAT...')
                            while True:
                                try:
                                    enter_security_level()
                                except Exception:
                                    pass
                                sbat_rsp = self.send(
                                    '2E F0 F4 ' + '00' * 822, False, True, quiet_mode=True)

                                if not sbat_rsp[-1] in ['0x31', '0x33']:
                                    break

                                enter_security_level()
                            break

            ''' Tester ID '''
            if 'tester_id' in kwargs:
                self.tester_id = kwargs['tester_id']
                if not isinstance(self.tester_id, str):
                    raise ValueError('tester_id must be string value')

            ''' Physical ID RSP '''
            if 'physical_id_rsp' in kwargs:
                self.physical_id_rsp = kwargs['physical_id_rsp']
                if not isinstance(self.physical_id_rsp, str):
                    raise ValueError('physical_id_rsp must be string value')

            ''' Request Address Type '''
            if 'functionalAddr' in kwargs:
                funcAddr = kwargs['functionalAddr']
                if not isinstance(funcAddr, bool):
                    raise ValueError('functionalAddr must be boolean')

                self.functionalAddr = funcAddr
            else:
                self.functionalAddr = False

            if 'response_from_log' in kwargs:
                response_from_log = kwargs['response_from_log']
                if not isinstance(response_from_log, bool):
                    raise ValueError('response_from_log must be boolean')
                # if self.functionalAddr:
                #    self.response_from_log = response_from_log

                self.response_from_log = response_from_log
                # else:
                #    raise AttributeError(
                #        '-response_from_log- requires -functionalAddr- flag to be set as True')

            ''' Power Mode '''
            if 'power_mode' in kwargs:
                power_mode = kwargs['power_mode'].upper()
                allowed_modes = [
                    'OFF', 'ACC', 'RUN', 'START', 'PROP'
                ]

                if not str(power_mode) in allowed_modes:
                    raise ValueError('Power mode not supported. Try using {}'.format(allowed_modes))

                self.canoe.power_panel(power_mode)
                self.Logger.write_on_report(
                    self.Logger.generate_row(
                        tools.timeStamp(), self.suite,
                        'power_mode()::%s' % power_mode.upper(),
                        'INFO', 'Setting power mode to %s' % power_mode.upper()
                    )
                )

            ''' Power Mode Ignition '''
            if 'ignition_switch' in kwargs:

                if not isinstance(kwargs['ignition_switch'], list):
                    raise ValueError('Please provide a valid list to create an ignition cycle. Example: \n' + \
                                     '   [\'OFF\', \'PROP\', \'OFF\'] -> will change from OFF to PROP and then go back to OFF.')

                if len(kwargs['ignition_switch']) == 1:
                    raise Warning('You can use -> power_mode <- instead if only one power mode is required.')

                for p_mode in kwargs['ignition_switch']:
                    print(__name__, 'Setting power mode:', p_mode.upper())
                    allowed_modes = [
                        'OFF', 'ACC', 'RUN', 'START', 'PROP'
                    ]

                    if not str(p_mode.upper()) in allowed_modes:
                        raise ValueError('Power mode not supported. Try using {}'.format(allowed_modes))

                    self.canoe.power_panel(p_mode.upper())
                    self.Logger.write_debug_log('DEBUG', __name__, 'Setting power mode to %s' % p_mode.upper())
                    self.Logger.write_on_report(
                        self.Logger.generate_row(
                            tools.timeStamp(), self.suite,
                            'ignition_switch()::%s' % p_mode.upper(),
                            'INFO', 'Setting power mode to %s' % p_mode.upper()
                        )
                    )
                    time.sleep(1)

            ''' Reset Communication - Canoe '''
            if 'reset_communication' in kwargs:
                if kwargs['reset_communication']:
                    if self.restart_communication():
                        print('Communication restablished successfully!')
                        self.Logger.write_on_report(
                            self.Logger.generate_row(
                                tools.timeStamp(), self.suite,
                                'power_supply - reset_communication()',
                                'INFO', 'Communication restablished successfully!'
                            )
                        )
                    else:
                        raise RuntimeError('Wow! There was a problem attempting to restablish your communication')

            ''' Enviroment Variable '''
            if 'envVariable' in kwargs:
                envVar = kwargs['envVariable']
                if not isinstance(envVar, dict):
                    raise ValueError(r'-> envVariable <- must be a dictionary containing \{Name:Value\}')
                # Set CANoe environment variables
                self.canoe.set_envVariable(**envVar)

                # Write on Report
                self.Logger.write_on_report(
                    self.Logger.generate_row(
                        tools.timeStamp(), self.suite,
                        ' - '.join(['{}::{}'.format(i, envVar[i]) for i in envVar.keys()]),
                        'INFO', 'Environment variable(s) {} has been modified'.format(list(envVar.keys()))
                    )
                )

            ''' Signals '''
            if 'signal' in kwargs:
                signal = kwargs['signal']
                if not isinstance(signal, list) or not len(signal) > 2:
                    raise ValueError('-> signal <- must be an array containing [Name, PDU_MSG, Value]')
                print(__name__, 'Attempting to set: ', *signal)

                if not 'power_mode' in locals() or self.canoe.power_mode() == 'OFF':
                    self.canoe.transmit_in_off()  # Required to set signals in OFF
                for i in range(0, len(signal), 3):
                    # Set Signal
                    self.canoe.set_signal(
                        signal[i], signal[i + 1], signal[i + 2])

                    # Write on Report
                    self.Logger.write_on_report(
                        self.Logger.generate_row(
                            tools.timeStamp(), self.suite,
                            '{}::{}::{}'.format(signal[i], signal[i + 1], signal[i + 2]),
                            'INFO', '{} has been set to {}'.format(signal[i], signal[i + 2])
                        )
                    )
                time.sleep(0.250)

        except Exception as error:
            self.Logger.write_debug_log('ERROR', __name__, error)
            print(__name__, 'preconditions()', type(error).__name__, error,
                  'Line %s' % (sys.exc_info()[2].tb_lineno))

    def step(self, **kwargs):

        try:
            ''' Test Parameters '''
            if not 'step_title' in kwargs:
                raise ValueError('ERROR - No argument -> step_title <- defined in step function')
            step_title = kwargs['step_title']
            if self.writeTestResults and _real_time_report:
                default = self.TestcaseRow.get('default', 1)
                self.ResultRow = self.TestcaseRow.get(
                    self.current_step,
                    default
                )

            print(
                ' *********************************************************************\
                \n {0} - {1}\
                \n *********************************************************************' \
                    .format(self.current_step, step_title)
            )
            self.canoe.App.UI.Write.Output(self.file_name + ' - ' + step_title)

            ''' Step is applicable? '''
            if self.writeTestResults and _real_time_report:
                if self.excel.read_cell_value(
                        self.SheetName, self.ResultRow, _result_column) == 'Not Applicable':
                    # Test Not Applicable
                    print(__name__, 'According to CG, step {} is not applicable.'.format(self.current_step))
                    return False

            ''' Step Timestamp '''
            print(__name__, tools.timeStamp('timeOnly'))

            ''' Execute UDS Service request '''
            actualRsp = self.uds_service(kwargs)
            self.latest_response = tools.readable_hex(actualRsp) if actualRsp else ''
            actualRsp = '   No response received!' if not actualRsp else actualRsp
            
            ''' AYanez 2A Reset DELETE since CAPL is i charge now '''
            if actualRsp[0].lower() == '0x6a': # On every 2A response

                if self.scheduler_2A == '1': # Haz prueba de regresion quiza modo 1 ya no es necesario
                    #self.canoe.set_system_variable("Periodic_DID", "Mode", "1"); # Reset Counter for All IDs
                    print('Reset by 2A Interaction')  # For DEBUG purposes dont remove

                if self.scheduler_2A == '2' and ('read_periodic_data_id' in kwargs):

                    print('Begin - Capturing DDDID Stream (2A Service) at', tools.timeStamp('timeOnly'))
                    _timeout = kwargs['read_periodic_data_id']['timeout']
                    tools.timer.input('Please wait for timeout to be reached. %ss' % str(_timeout),
                                      timeout=_timeout)
                    print('End - Capturing DDDID Stream (2A Service) at', tools.timeStamp('timeOnly'))

            ''' Validate response '''
            if 'expected' in kwargs:
                self.report_log_active = True
                data = data_2 = dataLength = partialData = unexpected_response = uudt_data = periodic_data = expected_byte = byte_index = data_dtc = NRC78_data = None  # Default values
                expected = kwargs['expected']

                if 'response' in expected:
                    if expected['response'] is not None:
                        if not expected['response'] in ['Positive', 'Negative', 'No response']:
                            raise ValueError('ERROR - Specified expected response is not supported.\n' \
                                             + ' -> Try using: Positive, Negative or No response')
                        expected_response = expected['response']
                else:
                    raise ValueError('ERROR- Please specify a response in expected, could be ' + \
                                     'Positive, Negative or No response')
                # being modified on 15/Jan/2020
                if 'partialData' in expected:
                    if expected['partialData'] is not None:
                        if not isinstance(expected['partialData'], (str, tuple, list)):
                            raise ValueError(
                                'ERROR - -> partialData <- should be string, list or a tuple. Ex. \'FF FF\', \("FF","FF")\, \["FF","FF"]\ ')
                        partialData = expected['partialData']
                # Till here
                elif 'data' in expected:
                    if expected['data'] is not None:
                        if not isinstance(expected['data'], str):
                            raise ValueError('ERROR - -> data <- should be a string value. Ex. \'FF FF\'')
                        data = tools.split_every_two(expected['data'].lower())

                if 'data_2' in expected:
                    if expected['data_2'] is not None:
                        if not isinstance(expected['data_2'], str):
                            raise ValueError('ERROR - -> data_2 <- should be a string value. Ex. \'FF FF\'')
                        data_2 = tools.split_every_two(expected['data_2'].lower())

                if 'dataLength' in expected:
                    if expected['dataLength'] is not None:  # Value must be different than None
                        dataLength = expected['dataLength']
                        if not isinstance(dataLength, list):
                            dataLength = int(dataLength)

                if 'expected_byte' in expected:
                    if expected['expected_byte'] is not None:
                        if not isinstance(expected['expected_byte'], (str, tuple, list)):
                            raise ValueError(
                                'ERROR - -> expected_byte <- should be a string, tuple or a list value. Ex. \'FF FF\', \("FF","FF")\, \["FF","FF"]\ ')
                        expected_byte = expected['expected_byte']

                if 'byte_index' in expected:
                    if expected['byte_index'] is not None:
                        if not isinstance(expected['byte_index'], (int, tuple, list)):
                            raise ValueError('ERROR - -> byte_index <- should be an integer, tuple or a list value.')
                        byte_index = expected['byte_index']
                        
                ''' AYanez NRC 78 '''
                if 'check_NRC78' in expected:
                    
                    # breakpoint()
                    if not isinstance(expected['check_NRC78'], (dict)):
                        raise ValueError('ERROR - -> check_NRC78 <- MUST be a dictionary.')
                            
                    def schema_trace_error(conf_schema, conf):
                        try:
                            conf_schema.validate(conf)
                            return ''
                        except SchemaError as e:
                            return e
                            
                    CType = {
                    'EQ': 1,
                    'NEQ': 2,
                    'GELE': 3
                    }
                    
                    result_base = {'is_error':True,'description':''}
                    NRC78_data = []
                    NRC78_data.append(result_base.copy())
                    
                    # Data Validation Schemas
                    
                    nrc78_validation_schema1 = Schema({
                        'CompType': And(str, lambda s: s in CType, error='Invalid Type, it only can be: EQ, NEQ or GELE'),
                        'HighLimit': And(int, lambda n: 1 <= n <= 9, error='High Limit range must be between 1 and 9'),
                        'LowLimit': And(int, lambda n: 1 <= n <= 9, error='Low Limit range must be between 1 and 9')
                    })
                    
                    nrc78_validation_schema2 = Schema({
                        'CompType': And(str, lambda s: s in CType, error='Invalid Type, it only can be: EQ, NEQ or GELE'),
                        'LowLimit': And(int, lambda n: 1 <= n <= 9, error='Low Limit range must be between 1 and 9')
                    })

                    # Ignore validation, it is a failure already 
                    if not nrc78_validation_schema1.is_valid(expected['check_NRC78']) and "HighLimit" in expected['check_NRC78']:

                        errorMsg = 'Data Input ERROR: ' + str(schema_trace_error(nrc78_validation_schema2, expected['check_NRC78']))
                        
                        NRC78_data[0]['description'] = errorMsg

                    elif nrc78_validation_schema1.is_valid(expected['check_NRC78']):
                    
                        if expected['check_NRC78']['LowLimit'] > expected['check_NRC78']['HighLimit']:
                    
                            errorMsg = 'Data Input ERROR: Your Low Limit is higher than your High Limit'
                            NRC78_data[0]['description'] = errorMsg
                            
                        else:
                        
                            NRC78Receptions = self.canoe.get_system_variable('Generic_Diagnostics', 'NRC78Receptions')
                            NRC78_data[0]['is_Error'] = (NRC78Receptions < expected['check_NRC78']['LowLimit'] or NRC78Receptions > expected['check_NRC78']['HighLimit'])
                            
                            if NRC78_data[0]['is_Error'] == True:
                            
                                errorMsg = 'NRC78 Receptions out of Range: The reading was ' + str(NRC78Receptions) + ' while HighLimit was ' + str(expected['check_NRC78']['HighLimit']) + ' and Low Limit was ' + str(expected['check_NRC78']['LowLimit'])
                                NRC78_data[0]['description'] = errorMsg
                        
                    elif not nrc78_validation_schema2.is_valid(expected['check_NRC78']):
                    
                        errorMsg = 'Data Input ERROR: ' + str(schema_trace_error(nrc78_validation_schema2, expected['check_NRC78']))
                        NRC78_data[0]['description'] = errorMsg
                    
                    elif nrc78_validation_schema2.is_valid(expected['check_NRC78']):
                    
                        NRC78Receptions = self.canoe.get_system_variable('Generic_Diagnostics', 'NRC78Receptions')
                        
                        if expected['check_NRC78']['CompType'] == 'EQ':
                        
                            NRC78_data[0]['is_Error'] = (NRC78Receptions != expected['check_NRC78']['LowLimit'])
                            
                            if NRC78_data[0]['is_Error'] == True:
                            
                                errorMsg = 'NRC78 Receptions out of Range: The reading was ' + str(NRC78Receptions) + ' and it is NOT Equal to ' + str(expected['check_NRC78']['LowLimit'])
                                NRC78_data[0]['description'] = errorMsg
                                    
                        elif expected['check_NRC78']['CompType'] == 'NEQ':
                        
                            NRC78_data[0]['is_Error'] = (NRC78Receptions == expected['check_NRC78']['LowLimit'])
                            
                            if NRC78_data[0]['is_Error'] == True:
                            
                                errorMsg = 'NRC78 Receptions out of Range: The reading was ' + str(NRC78Receptions) + ' and it is Equal to ' + str(expected['check_NRC78']['LowLimit'])
                                NRC78_data[0]['description'] = errorMsg
                                    

                ''' AYanez Periodic Validation '''
                if 'periodic_verifications' in expected:
                
                    if not isinstance(expected['periodic_verifications'], (dict, tuple)):
                        raise ValueError('ERROR - -> periodic_verifications <- MUST be a tuple of dictionaries or a single dictionary.')

                    result_base = {'is_error':True,'description':''}
                    periodic_data = []
                    verifications_container = None
                    
                    # Create Iterable Container
                    if isinstance(expected['periodic_verifications'], dict):
                        verifications_container = [expected['periodic_verifications']]
                    elif isinstance(expected['periodic_verifications'], tuple):
                        verifications_container = expected['periodic_verifications']
                    
                    # Create Results List - All Failures by default
                    for result in range(len(verifications_container)):
                        periodic_data.append(result_base.copy())
                        
                    i = 0 # Counter for items in periodic_verifications

                    def schema_trace_error(conf_schema, conf):
                        try:
                            conf_schema.validate(conf)
                            return ''
                        except SchemaError as e:
                            return e
                    
                    # Data Validation Schemas
                    
                    period_rate_schema = Schema({
                        'dddid': And(str, error='dddid MUST be a string'),
                        'rate': And(str, lambda s: s in self.rates_2A, error='Invalid Rate, it only can be: 01, 02 or 03'),
                        'tolerance': And(float, lambda n: 1 <= n <= 99, error='% Tolerance range for timing pattern must be between 1 and 99')
                    })

                    period_status_schema = Schema({
                        'dddid': And(str, error='dddid MUST be a string'),
                        'active': And(bool, error='Active MUST be boolean')
                    })

                    # Check all verifications
                    for item in verifications_container:

                        if not isinstance(item, dict):
                            raise ValueError('ERROR - -> Item for periodic_verifications should be a dictionary with valid format.')
                            errorMsg = 'ERROR - -> Item for periodic_verifications should be a dictionary with valid format.'
                            periodic_data[i]['description'] = errorMsg


                        # Check if Timing Patern is valid, by default ID is Active since a Rate Check was requested
                        if 'rate' in item and 'dddid' in item:
                            # Set Stream ID to inspect
                            self.canoe.set_system_variable('Periodic_DID', 'ID', item['dddid'])

                            # Ignore validation, it is a failure already 
                            if not period_rate_schema.is_valid(item):
                            
                                errorMsg = 'Data Input ERROR -> Item ' + str(i) + ' ' + str(schema_trace_error(period_rate_schema, item))
                                periodic_data[i]['description'] = errorMsg
                            
                            else:
                                if self.scheduler_2A == '1':
                                    # - Get Information for specific ID with CAPL Interaction -
                                    self.canoe.set_system_variable('Periodic_DID', 'Mode', '2')
                                    time.sleep(1)

                                    MaxTime = self.canoe.get_system_variable('Periodic_DID', 'Max_Time')
                                    MinTime = self.canoe.get_system_variable('Periodic_DID', 'Min_Time')
                                    HighLimit = self.rates_2A[item['rate']] + (self.rates_2A[item['rate']]*(item['tolerance']/100))
                                    LowLimit = self.rates_2A[item['rate']] - (self.rates_2A[item['rate']]*(item['tolerance']/100))

                                    print(f"Window verification for DDDID: {item['dddid']}. MaxTime was {MaxTime:.3f}s, MinTime was {MinTime:.3f}s. ULimit: {HighLimit:.3f}, LLimit:{LowLimit:.3f}")

                                    if (MaxTime <= HighLimit) and (MinTime >= LowLimit):
                                        periodic_data[i]['is_error'] = False

                                    if periodic_data[i]['is_error'] == True:
                                        errorMsg = 'STEP FAILURE -> Latency times for DDDID: ' + item['dddid'] + ' exceeded limits. MaxTime was ' + str(MaxTime) + ', MinTime was ' + str(MinTime) + '. ULimit: '+str(HighLimit)+ ', LLimit:' + str(LowLimit)
                                        periodic_data[i]['description'] = errorMsg

                                if self.scheduler_2A == '2':

                                    # - Get Information for specific ID with CAPL Interaction -
                                    self.canoe.set_system_variable('Periodic_DID', 'Mode', '5')
                                    time.sleep(1)
                                    GlobalRate = self.canoe.get_system_variable('Periodic_DID', 'GlobalRate')

                                    MaxTime = self.canoe.get_system_variable('Periodic_DID', 'Max_Time')
                                    MinTime = self.canoe.get_system_variable('Periodic_DID', 'Min_Time')

                                    HighLimit = GlobalRate + (GlobalRate * (item['tolerance'] / 100))
                                    LowLimit = GlobalRate - (GlobalRate * (item['tolerance'] / 100))

                                    missing_execution = self.canoe.get_system_variable('Periodic_DID', 'MissingExecution')

                                    print(
                                        f"Window verification for DDDID: {item['dddid']}. MaxTime was {MaxTime:.3f}s, MinTime was {MinTime:.3f}s. ULimit: {HighLimit:.3f}, LLimit:{LowLimit:.3f}, Missing_Execution(s):{missing_execution}")

                                    if (MaxTime <= HighLimit) and (MinTime >= LowLimit) and (missing_execution == 0):
                                        periodic_data[i]['is_error'] = False

                                    if periodic_data[i]['is_error'] == True:
                                        errorMsg = 'STEP FAILURE -> Latency times for DDDID: ' + item[
                                            'dddid'] + ' exceeded limits. MaxTime was ' + str(
                                            MaxTime) + ', MinTime was ' + str(MinTime) + '. ULimit: ' + str(
                                            HighLimit) + ', LLimit:' + str(LowLimit) + ',MissingExecution:' + str(missing_execution)
                                        periodic_data[i]['description'] = errorMsg

                        elif 'active' in item and not 'rate' in item and 'dddid' in item: # If rate and active are present then overwrite is possible it marks this case as NO valid
                            # Set Stream ID to inspect
                            self.canoe.set_system_variable('Periodic_DID', 'ID', item['dddid'])

                            # Ignore validation, it is a failure already 
                            if not period_status_schema.is_valid(item):
                          
                                errorMsg = 'Data Input ERROR -> Item ' + str(i) + ' ' + str(schema_trace_error(period_status_schema, item))
                                periodic_data[i]['description'] = errorMsg
                                
                            else:
                            
                                # Compare if Status is Inactive by reading Stream Counter
                                self.canoe.set_system_variable('Periodic_DID', 'Mode', '3')
                                time.sleep(2)
                                StreamCounter = self.canoe.get_system_variable('Periodic_DID', 'Counter')
                                
                                idstatus = {
                                'True': 'Active',
                                'False': 'Inactive'
                                }
                                
                                if item['active'] == True and StreamCounter >= 0:
                                    periodic_data[i]['is_error'] = False
                                    
                                    print('Pass Active Case for DDDID = {0} counter = {1}.'.format(item['dddid'], StreamCounter))
                                    
                                elif item['active'] == False and StreamCounter == -1:
                                    periodic_data[i]['is_error'] = False
                                    
                                    print('Pass Inactive Case for DDDID = {0} counter = {1}.'.format(item['dddid'], StreamCounter))
                                    
                                else:
                                    periodic_data[i]['is_error'] = True
                                    
                                    print('Failed Case for DDDID = {0} counter = {1}.'.format(item['dddid'], StreamCounter))
   
                                if periodic_data[i]['is_error'] == True:
                                    
                                    errorMsg = 'STEP FAILURE -> DDDID: ' + item['dddid'] + ' was expected to be ' + idstatus[str(item['active'])] + '. Counter = ' + str(StreamCounter)
                                    periodic_data[i]['description'] = errorMsg

                        else:
                        
                            errorMsg = 'ERROR - -> Service 2A verification item format is INVALID, not rate or status type.'
                            raise ValueError(errorMsg)
                            periodic_data[i]['description'] = errorMsg
                            
                        i += 1 # Index for Results List
                               
                ''' AYanez Periodic Validation '''       
                if 'periodics_num' in expected:
                
                    # The results vector is shared for this parameter and 'periodic_verifications' so if list does not exist then we create it
                    if not periodic_data:
                        periodic_data = []
                
                    if not isinstance(expected['periodics_num'], int):
                        raise ValueError('ERROR - -> periodics_num <- should be an integer.')
                                       
                    self.canoe.set_system_variable('Periodic_DID', 'Mode', '4')
                    time.sleep(1)
                    ActiveNumStreams = self.canoe.get_system_variable('Periodic_DID', 'ActiveStreams')
                    time.sleep(1)
                    ActiveIDList = self.canoe.get_system_variable('Periodic_DID', 'ActiveIDStreams')
   
                    if(ActiveIDList != 'None') :
                        #-1 to delete space at end from CANoe String
                        hexIDList = *map(hex, map(int, ActiveIDList.split(',')[:-1])),
                        ActiveIDList = ','.join([ i.replace('0x', '') for i in hexIDList ]).upper()
                    
                    if ActiveNumStreams > expected['periodics_num'] or ActiveNumStreams < expected['periodics_num']:
                        errorMsg = 'Number of Active PDIDs transmitting is ' + str(ActiveNumStreams) + ', the expected number was ' + str(expected['periodics_num']) + '. Active PDIDs are: ' + ActiveIDList
                        periodic_data.append({'is_error':True,'description':errorMsg})
                        
                    elif ActiveNumStreams == expected['periodics_num']:
                        periodic_data.append({'is_error':False,'description':''})
                
                if 'unexpected_response' in expected:
                    unexpected_response = expected['unexpected_response']
                    if not isinstance(unexpected_response, bool):
                        raise ValueError('-unexpected_response- should be a boolean.')

                if 'data_dtc' in expected:

                    if expected['data_dtc'] is None:
                        raise RuntimeError('data_dtc is {0} must be a tuple at least with one element like list or string not None'.format(type(expected['data_dtc'])))

                    if expected['data_dtc'] is not None:

                        if not (isinstance(expected['data_dtc'], tuple) or isinstance(expected['data_dtc'], list) or isinstance(expected['data_dtc'], str)):
                            raise ValueError('data_dtc is {0}- must be a tuple at least with one element like list or string'.format(type(expected['data_dtc'])))
                        data_initial = []
                        temp_dtc = []

                        if len(expected['data_dtc']) >= 1 and isinstance(expected['data_dtc'], list):
                            for i in expected['data_dtc']:
                                data_initial.append(i)

                        if len(expected['data_dtc']) == 8 and isinstance(expected['data_dtc'], str):
                            temp_dtc = expected['data_dtc'].split(" ")
                            data_initial.append(temp_dtc)

                        if len(expected['data_dtc']) == 2 and isinstance(expected['data_dtc'], tuple):

                            if isinstance(expected['data_dtc'][0], list) and isinstance(expected['data_dtc'][1], str):
                                temp_dtc = expected['data_dtc'][0].copy()
                                temp_dtc.append(expected['data_dtc'][1].split(" "))
                                data_initial = temp_dtc

                            if isinstance(expected['data_dtc'][0], str) and isinstance(expected['data_dtc'][1], list):
                                temp_dtc = expected['data_dtc'][1].copy()
                                temp_dtc.append(expected['data_dtc'][0].split(" "))
                                data_initial = temp_dtc

                        # # Create a list with the dtc sent by user and dtc current
                        data_dtc = []
                        data_dtc.append(data_initial)
                        data_dtc.append(self.last_dtcs)

                #This  variable safe information about current dtc_list
                dtc_list = self.last_dtcs

                status = validate(

                    actualRsp,
                    expected_response,
                    data,
                    data_2,
                    periodic_data,
                    partialData,
                    dataLength,
                    expected_byte,
                    byte_index,
                    unexpected_response,
                    dtc_list,
                    data_dtc,
                    NRC78_data

                )

                self.attributes.update(dict({
                    'status': status[0],
                    'failure_cause': status[1]
                }))

                ''' JSON Report append step results '''
                json_report_failure = '' if True in status else status[1]
                data = None if not isinstance(data, list) else tools.readable_hex(data)
                self.Logger.append_step_results(
                    testcase=self.file_name,
                    test_func=self.current_step,
                    timestamp=tools.timeStamp(),
                    title=step_title,
                    request=self.request,
                    response=tools.readable_hex(actualRsp),
                    expected_response=expected_response,
                    data=data,
                    dataLength=dataLength,
                    test_status=TestResult[status[0]],
                    comments=json_report_failure
                )

                ## DEBUG ## Write request / response on excel / expected
                debug_info = 'Request: {0} \nResponse: {1}\nExpected: {2}\nExpData: {3}\nExpDataLength: {4}\npartialData: {5}'.format(
                    self.request,
                    tools.readable_hex(actualRsp),
                    expected_response,
                    data,
                    dataLength,
                    partialData,
                )

                comments = debug_info if True in status else status[1] + '\n' + debug_info
                self.Logger.write_tester_report(self.file_name, TestResult[status[0]],
                                                self.current_step + ' - ' + step_title, comments)
                print(__name__, 'Test {0}'.format(TestResult[status[0]]))
                if not status[0]: print(__name__, status[1])  # Print failure
                if self.writeTestResults and _real_time_report:
                    ''' Excel Test Report Status '''
                    self.excel.write_test_result(self.SheetName, self.ResultRow, _result_column, status[0])
                    self.Logger.write_debug_log('DEBUG', __name__, 'Writing test results:' \
                                                + 'SheetName:{0}\nRow:{1}\nColumn:{2}\nStatus{3}'.format(
                        self.SheetName, self.ResultRow, _result_column, status[0]
                    ))
                    self.Logger.write_debug_log('DEBUG', __name__, 'Results successfully written!')

                    if self.debug_mode:
                        self.excel.write_cell(self.SheetName, self.ResultRow, _log_column, debug_info)
                    ## DEBUG ## Write request / response on excel / expected
                    ''' Failure Handler '''
                    if not status[0]:
                        failure_cause = '{0} :: {1}'.format(step_title, status[1])
                        comments = self.excel.read_cell_value(self.SheetName, self.ResultRow, _log_column)
                        comments = 'Failure cause:\n' if comments is None else comments
                        self.excel.write_cell(self.SheetName, self.ResultRow, _log_column,
                                              comments + '\n' + failure_cause)
                        self.excel.write_cell(self.SheetName, self.ResultRow, _log_column + 1, debug_info)

                return self.attributes
        except Exception as error:
            self.Logger.write_debug_log('ERROR', __name__, error)
            print(__name__, 'step()', type(error).__name__, error,
                  'Line %s' % (sys.exc_info()[2].tb_lineno))

    def uds_service(self, kwargs):

        try:

            services = filter(  # Find services to execute from arguments
                lambda x: not x in ['step_title', 'expected'],
                kwargs
            )

            for s in services:  # Execute services
                data = kwargs[s]

                if s in ['custom', 'custom_Functional']:
                    self.request = kwargs[s]
                    if not isinstance(self.request, str):
                        raise ValueError('-custom- does not contain valid data.')
                    if not len(self.request) > 0:
                        raise ValueError('-custom- empty custom argument. Please specify valid data.')
                    rsp = self.send(
                        self.request, self.functionalAddr,
                        response_from_log=self.response_from_log,
                        response_delay=self.step_delay,
                        tester=self.tester_id,
                        physical_id_rsp=self.physical_id_rsp
                    )

                    continue

                if s == 'multiple_tester':
                    for _ in range(5):
                        if not isinstance(data, list):
                            raise ValueError(r'-multitester- requires list value. Ex. ["10 01", "10 01"]')
                        self.request = '/'.join(data)
                        rsp = self.multiple_request(*data)
                        if not 'No response received' in rsp:
                            break

                    continue

                uds = service.obj(s)
                # Access Security Lvls
                if s == 'request_seed':
                    self.request = uds(s, data)
                    rsp = self.send(self.request, self.functionalAddr, tester=self.tester_id)
                    ff_in_seed = [i for i in rsp if i == '0xff']
                    if 'No response received' in rsp:
                        self.security_seed = None
                        continue

                    if not len(ff_in_seed) > 4:
                        # Concatenate hex message & remove 0x prefix
                        self.security_seed = tools.readable_hex(rsp)[2:].replace(' ', '')
                    # Just execute the function but do not send any message
                    continue

                if s == 'send_key':
                    if self.security_seed is None:
                        raise ValueError(
                            'Security Key cannot be generated. Seed was not obtained on previous step.')
                    self.request = uds(
                        s, data, self.security_seed, SecurityAccess.CMAC_AES.cmac_encrypt(self.security_seed)
                    )
                    if self.functionalAddr:
                        print(__name__,
                              'Functional Address req is not supported for send_key',
                              'It will be executed -Physically-')
                    rsp = self.send(self.request, tester=self.tester_id)
                    continue

                if s == 'read_periodic_data_id':
                    if not isinstance(data, dict):
                        raise ValueError('-dict- type value is required for ->read_periodic_data_id<-')

                    params = (s, *[i for i in data.values()])
                    self.periodic_data = data
                    self.request = uds(*params[:3])
                    rsp = self.send(
                        self.request, self.functionalAddr,
                        response_from_log=self.response_from_log,
                        response_delay=self.step_delay,
                        tester=self.tester_id
                    )


                    continue

                self.request = uds(s, data)

                rsp = self.send(
                    self.request, self.functionalAddr,
                    response_from_log=self.response_from_log,
                    response_delay=self.step_delay,
                    tester=self.tester_id
                )

            # Note: PyUDS does support multiple functions in 1 single step
            # but only the response from last request will be returned. Other ones are ignored, but sent.
            if rsp is None:
                raise RuntimeError('Not able to process request.')
            return rsp

        except Exception as error:
            if type(error).__name__ == 'com_error' and self.functionalAddr:
                print('\nPlease add -> %s_Functional <- to CAN Network and try again\n' % (ECU_info['name']))
            else:
                print(__name__, 'uds_service()', type(error).__name__, error,
                      'Line %s' % (sys.exc_info()[2].tb_lineno))

    def end(self, **kwargs):
        """
        =======================================================================
         end() - Stop CANoe simulation, end & place Logs in Report
        =======================================================================
        """
        try:

            # - Stop Measurement
            self.canoe.stop()
            time.sleep(2)
            if self.power_supply != None:	
                self.power_supply.output(False)
            self.canoe.App.UI.Write.EnableOutputFile(LogsPath + '\\' + 'writewindow.txt', 0)

            # - End Longs
            self.Logger.rename_log(self.file_name)
            TraceLog = LogsPath + '\\' + self.file_name + '.asc'

            # - Attach ASC Log to Excel Report
            if self.writeTestResults and _real_time_report:
                _column = 'G' if cg3388() else 'F'  # cg3388 => Only for CG3388

                ''' Excel - SW Version '''
                _column = 'G' if cg3388() else 'F'
                self.excel.write_sw_version(
                    self.TestcaseRow['sw_version'], _column, self.SheetName, info
                )

                ''' Excel - Attach ASC Log file '''
                self.excel.insert_log_file(
                    self.TestcaseRow['log'], _column, TraceLog, self.SheetName
                )

                if cg3388():  # Only for CG3388
                    _excluded_tabs = ('Multiple Tester', 'Transport Layer', 'Scanner')
                    if not self.SheetName in _excluded_tabs:
                        self.supplier_info.write_supplier_info()

                self.excel.save_report()

            # - End Logger
            self.Logger.end_logs(self.file_name, self.report_log_active)

            print(
                '\n    #' + '=' * 72 + \
                '\n    # Finishing %s' % self.file_name + \
                '\n    #' + '=' * 72, end='\n\n'
            )
        except Exception as error:
            self.Logger.write_debug_log('ERROR', __name__, error)
            print(__name__, 'end()', type(error).__name__, error,
                  'Line %s' % (sys.exc_info()[2].tb_lineno))
            sys.exit(0)

    def restart_communication(self, only_nmf=False):

        try:
            while True:
                success = True
                if not only_nmf:
                    success = self.cold_reset()
                self.canoe.set_envVariable(envVNMFSend=0)
                self.canoe.set_envVariable(envVNMFStop=1)
                print(__name__, 'Restablishing communication...')
                time.sleep(0.75)
                self.canoe.set_envVariable(envVNMFStop=0)
                self.canoe.set_envVariable(envVNMFSend=1)

                if success: break

            return True
        except Exception as error:
            print(__name__, 'End()', type(error).__name__, error)
            return False

    def cold_reset(self, timer=2.5):
        try:
            self.Logger.write_debug_log('DEBUG', __name__, 'Executing cold reset...')
            if self.power_supply != None:
                self.power_supply.output(False)
                time.sleep(timer)
                self.power_supply.output(True)
                self.power_supply_reset_default()
            else:
                tools.popup.info(title='Power supply reset',
                                 description='Please make sure to reset your Power Supply manually, then press ENTER to continue...')
            return True
        except Exception as error:
            print(__name__, 'cold_reset()', type(error).__doc__, type(error).__name__, error)
            return False

    def set_dtc_condition(self, overVoltage=False, underVoltage=False, **kwargs):
        if self.power_supply != None:
            if overVoltage + underVoltage != 1:
                raise ValueError('Please specify whether overVoltage OR underVoltage is required')

            if overVoltage:
                #self.canoe.power_panel('RUN')
                self.power_supply.settings(current=2, voltage=17) #self.overVoltage
                time.sleep(3)
                while self.catch_error_frames():
                    time.sleep(1)
            if underVoltage:
                #self.canoe.power_panel('RUN')
                self.power_supply.settings(current=2, voltage=8)
                time.sleep(3)
                while self.catch_error_frames():
                    time.sleep(1)

        else:
            condition_for = 'overVoltage' if overVoltage else 'underVoltage'
            tools.popup.info(title='%s condition' % condition_for,
                             description='Please make sure to set valid conditions for %s' % condition_for)

    def power_supply_reset_default(self):
        if self.power_supply != None:
            self.power_supply.settings(current=2, voltage=12.5)
        else:
            tools.popup.info(title='Power supply default settings',
                             description='Please make sure reset power supply settings to 12.5v')

    def read_power_supply_current(self):
        if self.power_supply != None:
            return self.power_supply.get_current()

    def read_power_supply_voltage(self):
        if self.power_supply != None:
            return self.power_supply.get_voltage()

    def compare(self, first, second, negative_test=False, step=None):
        """
        -compare- method allows user to compare val1 & val2 
            and write Test results according to this comparison.
        """
        if self.writeTestResults and _real_time_report:
            if step is None:
                raise Warning('-step- argument is required when writeTestResults are enabled!')

            if not (isinstance(step, int) or isinstance(step, str)):
                raise ValueError('Step must be either -str- or -int- type')

            default = self.TestcaseRow.get('default', 1)

            self.ResultRow = self.TestcaseRow.get(
                step, default
            )

        if step:
            print(
                ' *********************************************************************\
                \n {0} - {1}\
                \n *********************************************************************' \
                    .format(step, 'PyUDS - %s' % step)
            )

        def write_report(status, failure_cause=None):
            ''' Excel - Write results on report '''
            try:
                if self.writeTestResults and _real_time_report:
                    self.excel.write_test_result(self.SheetName, self.ResultRow, _result_column, status)
                    if failure_cause != None:  # Write Failure cause
                        comments = self.excel.read_cell_value(self.SheetName, self.ResultRow, _log_column)
                        comments = 'Failure cause:\n' if comments is None else comments
                        self.excel.write_cell(self.SheetName,
                                              self.ResultRow,
                                              _log_column,
                                              comments + '\n' + failure_cause)

                _step = step if step else 'test_compare_step'
                _failure_cause = failure_cause if failure_cause else 'This is just a comparison step'
                self.Logger.write_tester_report(self.file_name,
                                                TestResult[status],
                                                _step + ' :: test.compare()', _failure_cause)
            except Exception as error:
                self.Logger.write_debug_log('ERROR', __name__, error)
                print(__name__, 'compare().write_report()', type(error).__name__, error,
                      'Line %s' % (sys.exc_info()[2].tb_lineno))

        if first == second:
            if negative_test:
                print(__name__, 'Test FAILED, value expected is {0}, but actual is: {1}'.format(
                    first, second
                ))
                write_report(False, 'Please look at TraceLog for further information.')
                return False
            else:
                print(__name__, 'Test PASSED')
                write_report(True)
                return True
        else:
            if not negative_test:
                print(__name__, 'Test FAILED, value expected is {0}, but actual is: {1}'.format(
                    first, second
                ))
                write_report(False, 'Please look at TraceLog for further information.')
                return False
            else:
                print(__name__, 'Test PASSED')
                write_report(True)
                return True