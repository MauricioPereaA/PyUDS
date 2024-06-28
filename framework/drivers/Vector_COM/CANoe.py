"""@CANoe.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    Use of CANalyzer/CANoe as a COM server.
    

@note ABBREVIATIONS:
        - COM: Component Object Model
Modified by Mauricio Perea
Date: 7 Oct 2020		
Modify the open method
Change the message in the exception

Modified by Mauricio Perea
Date: 10 November 2020
"set_system_variable" is near to be generic now, it accepts more datatypes besides boolean
Modified by Mauricio Perea
Date: 5 October 2020
"set_system_variable" was modified due bugs with the input data manipulation for several datatypes
*******************************************************************************
"""
# ==============================================================================
# Python import packages
# ==============================================================================
from framework.tools.logs import Logger
from framework.drivers.Vector_COM.genpy import CANoe_genpy
import win32com.client
import inspect
import time
import sys

Logger = Logger()

class CANTool(object):
    """
    CANalyzer/CANoe as a COM server
    """
    def __init__(self):
        """
        Create the instance through which the COM server's  
        Application object will be accessed
        """
        try:
            self.App = win32com.client.Dispatch('CANoe.Application')
            Logger.write_debug_log('DEBUG', __name__, 'CANoe Application succesfully Dispatched.')
        except Exception as error:
            print(__name__, 'Failed to Dispatch CANoe COM', error)
            Logger.write_debug_log('ERROR', __name__, 'CANoe failed attempting to dispatch COM.')
   
    def open(self, path, *options):
        """open(config As String, 
                    Optional autoSave As Boolean, 
                    Optional promptUser As Boolean)
        """
        _options = options if options else (True, False)
        try:
            self.App.Open(path, *_options)
            Logger.write_debug_log('DEBUG', __name__, 
                'CANoe.open.path -> %s'%path)
        except Exception as error:
            print(__name__, 'is open the -> %s is running actually'%path)
            Logger.write_debug_log('DEBUG', __name__, 
                'CANoe.open() failed: {}'.format(error))
            
    def start(self):
        """
        start() method retries CANoe.Measurement start
        """
        try:
            if self.App.Measurement.Running:
                self.stop()
            while not self.App.Measurement.Running:
                time.sleep(0.25)
                self.App.Measurement.Start()

            
            Logger.write_debug_log('DEBUG', __name__, 
                'Simulation started: -> %s'%self.App.Measurement.Running)
                        
        except Exception as error:
            Logger.write_debug_log('ERROR', __name__, 
                'CANoe.start() failed: {}'.format(error))
            
    def stop(self):
        """
        stop() method stops CANoe.Measurement simulation
        """
        try:
            while self.App.Measurement.Running:
                #===============================================================
                # Wakeup Settings:  Stop NMF
                #===============================================================
                EnvVarObj = self.App.Environment.GetVariable('envVNMFSend')
                EnvVarObj.Value = 0
                #==============================================================
                # Stop Communication
                #==============================================================
                self.App.Measurement.Stop()
                
        except Exception as error:
            Logger.write_debug_log('ERROR', __name__, error)

    def log_settings(self, **kwargs):
        """
        log_settings() handles log path configuration
        """
        try:
            if not 'path' in kwargs:
                raise RuntimeError('path parameter is required for log_settings()')
            
            logFullPath = kwargs['path']

            self.LogsObj = self.App.Configuration.OfflineSetup.LoggingCollection(1)
            if not self.LogsObj.FullName == logFullPath:

            # Disable all LoggingFileNameOptions
                self.LogsObj.FileNameOptions.IncrementAtMeasurementStart = False
                self.LogsObj.FileNameOptions.IncrementAfterDuration = False
                self.LogsObj.FileNameOptions.IncrementAfterTrigger = False
                self.LogsObj.FileNameOptions.IncrementAfterGrowth = False
                self.LogsObj.FileNameOptions.NumberOfLeadingZeros = False
                self.LogsObj.FileNameOptions.IncrementationSize = False

                print(__name__, 'Current Log full path: {}'.format(self.LogsObj.FullName))
                
                self.LogsObj.FullName = logFullPath
                print(__name__, 'New Log full path: {}'.format(self.LogsObj.FullName))
            return self.LogsObj.FullName

        except Exception as error:
            print(__name__, error)
            print(__name__, "Method: ", inspect.stack()[0][0].f_code.co_name)
            print(__name__, "Class: ", self.__class__.__name__)
            raise RuntimeError('Not able to change log settings.')

    def power_mode(self):
        """    
        power_mode() Returns current power mode | -str- type obj
        """
        power_mode = ['OFF', 'ACC', 'RUN', 'START', 'PROP']
        return power_mode[self.App.Environment.GetVariable('IgnitionSwitch').Value]

    def power_panel(self, value, current=False):
        """
        power_panel() sets power mode
        """
        power_mode = {
            'OFF'   : 0,
            'ACC'   : 1,
            'RUN'   : 2,
            'START' : 3,
            'PROP'  : 4
        }
        try:
            IgnitionSwitchPanel = self.App.Environment.GetVariable('IgnitionSwitch')
            IgnitionSwitchPanel.Value = power_mode[value]
            Logger.write_debug_log('DEBUG', __name__, 'Attempting to set power mode: %s'%value)
            Logger.write_debug_log('DEBUG', __name__, 'Current value is: %s'%IgnitionSwitchPanel.Value)

            return True
        except Exception as error:
            print(__name__, error)
            print(__name__, "Method: ", inspect.stack()[0][0].f_code.co_name)
            print(__name__, "Class: ", self.__class__.__name__)
            print(__name__, 'Not able to change Power Panel')

    def set_envVariable(self, **kwargs):
        """
        Sets environment variable
        """
        try:
            for envVariable in kwargs:
                self.App.Environment.GetVariable(envVariable).Value = kwargs[envVariable]
                
                Logger.write_debug_log('DEBUG', __name__,
                    'envVariable: {} has been set to {}'.format(envVariable, kwargs[envVariable]))
            return True
        except Exception as error:
            print(__name__, 'Not able to set Enviroment Variable', error)
            Logger.write_debug_log('ERROR', __name__,
                    'Not able to set envVariable {} to {} :: {}'.format(envVariable, 
                                                                        kwargs[envVariable], 
                                                                        error))
    
    def read_envVariable(self, *envVars):
        """
        Returns environment variable value | -int- type obj
        """
        try:
            for envVariable in envVars:
                print(__name__, envVariable, self.App.Environment.GetVariable(envVariable).Value)
            return self.App.Environment.GetVariable(envVariable).Value
        except Exception as error:
            print(__name__, 'Not able to read Enviroment Variable', error)
            Logger.write_debug_log('ERROR', __name__,
                    'Not able to read envVariable(s) {} :: {}'.format(envVars, error))
        
    def get_signal(self, signal='PSP_PrplSysActvAuth', PDU='CGM_CAN4_PDU11'):
        """
        Returns signal value | -int- type obj
        """
        try:
            # Signal implementation
            signalObj = self.App.Bus.GetSignal( 1, PDU, signal)
            print(__name__, signalObj.FullName, signalObj.IsOnline, signalObj.RawValue, signalObj.State)
            return signalObj.RawValue
        except Exception as error:
            print(__name__, 'Not able to read signal value', error)
            Logger.write_debug_log('ERROR', __name__,
                    'Not able to read signal value {} from {} :: {}'.format(signal, PDU, error))
    
    def set_signal(self,  signal='PSP_PrplSysActvAuth', message='CGM_CAN4_PDU11', value=0):
        # =====  Function Parameters Description  =====
        # Param    | Type      |  Description
        # -------------------------------------------------------------
        # value    | Integer   | Value to be set to signal
        # signal   | String    | Signal name
        # message  | String    | message that contains signal
        # -------------------------------------------------------------
        # NOTE: If TransmitInOFFInfinite is not set, Power Mode MUST be different than OFF
        # -------------------------- Example --------------------------
        # set_signal( 'PSP_PrplSysActvAuth', 'CGM_CAN4_PDU11', 1 )
        # --------------------------------------------------------------

        try:
            # Signal implementation
            signalObj = self.App.Bus.GetSignal( 1, message, signal)
            signalObj.RawValue = value
            print(__name__, signalObj.FullName, signalObj.IsOnline, signalObj.RawValue)

            Logger.write_debug_log('DEBUG', __name__,
                'Signal: {}::{} has been set to {}'.format(message, signal, value))

            return signalObj.IsOnline
        except Exception as error:
            print(__name__, 'Not able to set signal', signal, message, error)
            Logger.write_debug_log('ERROR', __name__,
                    'Not able to set signal value {} from {} :: {}'.format(signal, message, error))

    def transmit_in_off(self):
        """
        Activates transmit in off checkbox
        """
        try:
            self.power_panel('RUN')
            self.set_envVariable(TransmitInOFFInfinite=1)
            self.power_panel('OFF')
            Logger.write_debug_log('DEBUG', __name__, 'CANoe.Transmit_in_off() - Enabled')
            return True
        except Exception as error:
            print(__name__, 'Not able to set -transmit in off-', error)
            Logger.write_debug_log('ERROR', __name__, 
                'Failed to stablish transmit in off :: {}'.format(error))
            return False

    def set_system_variable(self, namespace, variable, value):
       
        try:
            _root = self.App.Application.System.Namespaces
            _namespace = namespace.split('::') if '::' in namespace else namespace

            is_nested = lambda obj: obj.Namespaces.Count > 0

            def get_namespace_id(root_obj, namespace):
                for i in range(1, root_obj.Count+1):
                    if root_obj.Item(i).Name.lower() == namespace.lower():
                        return i
                else:
                    raise ValueError('%s not found!'%namespace)

            def get_nested_namespace_obj(root_obj, namespaces):
                _active_object = root_obj
                for ns in namespaces:
                    _ns_id = get_namespace_id(_active_object, ns)
                    if is_nested(_active_object.Item(_ns_id)):    
                        _active_object = _active_object.Item(_ns_id).Namespaces
                    else:
                       return (_ns_id, _active_object)
                       
            def is_hex(string):
                try:
                    int(string, 16)
                    return True
                except ValueError:
                    return False

            def get_variable_id(namespace_obj, variable):
                if not hasattr(namespace_obj, 'Variables'):
                    if not '::' in namespace:
                        raise ValueError('Nested namespaces requires to provide nested '+\
                            'namespaces separated by :: like following: namespace_1::namespace_2')
                var_obj = namespace_obj.Variables
                for i in range(1, var_obj.Count+1):
                    if var_obj.Item(i).Name.lower() == variable.lower():
                        return i
                else:
                    raise ValueError('%s not found in system variables!'%variable)

            _namespace_obj = None
            if isinstance(_namespace, str):      #    Single namespace
                _namespace_obj = _root
                _namespace_id = get_namespace_id(_root, _namespace)
            elif isinstance(_namespace, list):   #    Multiple namespaces
                _namespace_id, _namespace_obj = get_nested_namespace_obj(_root, _namespace)

            _variable_id = get_variable_id(_namespace_obj.Item(_namespace_id), variable)

            sys_var_obj = _namespace_obj.Item(_namespace_id).Variables.Item(_variable_id)
            
            """
            0: Integer 
            1: Float 
            2: String 
            4: Float Array 
            5: Integer Array 
            6: LongLong 
            7: Byte Array 
            98: Generic Array is not implemented
            99: Struct  is not implemented
            65535: Invalid 
            """
            
            if sys_var_obj.type in [98,99,65535]:
            
                raise Exception('Invalid datatype: Generic Array, Struct or Invalid are not supported')
            
            # For array the entire array should be written, for specific element you can use on variable argument: ArrayName[Index] and datatype is scalar
            elif sys_var_obj.type in [4,5,7]:
                
                arrayValue = [0] * sys_var_obj.ElementCount
                
                i = 0
            
                for item in value:
                
                    if sys_var_obj.type == 4:
                    
                        if isinstance(item, float):
                
                            arrayValue[i] = item
                        
                    elif sys_var_obj.type == 5:
                    
                        if isinstance(item, int):
                
                            arrayValue[i] = item
                        
                    elif sys_var_obj.type == 7:
                    
                        if isinstance(item, int):
                
                            arrayValue[i] = item
                        
                    i += 1
                        
                sys_var_obj.Value = arrayValue
            
            else:
            
                if sys_var_obj.type == 0:
                
                    if value is True:
                        value ='TRUE'
                    elif value is False:
                        value = 'FALSE'
                
                    if isinstance(value, str):
                        
                        if value.upper() in ['TRUE', 'FALSE']:
                    
                            sys_var_obj.Value = int(value == 'TRUE')
                        
                        elif is_hex(value.replace('0x', '')):
                        
                            sys_var_obj.Value = int(value.replace('0x', ''), 16)    
                        
                    elif isinstance(value, int):
                        
                        sys_var_obj.Value = value
                        
                elif sys_var_obj.type == 1:
                
                    if isinstance(value, float):

                        sys_var_obj.Value = value

                elif sys_var_obj.type == 2:
                
                    if isinstance(value, str):

                        sys_var_obj.Value = value

                elif sys_var_obj.type == 6:
                
                    if isinstance(value, int):

                        sys_var_obj.Value = value

                Logger.write_debug_log('DEBUG', __name__, '{0}::{1}::{2}'.format(_namespace, variable, value))
                
            time.sleep(0.1) # Small delay for update action at CANoe SysVars

            return sys_var_obj.Value

        except Exception as error:
            _error = 'Not able to set System Variable {}::{}::{} - {}'.format(
                        _namespace, variable, value, error)
            print(__name__, _error)
            Logger.write_debug_log('ERROR', __name__, _error)

            print(__name__, type(error).__name__, error,                                       
                    'Line %s' % (sys.exc_info()[2].tb_lineno))
    

    def get_system_variable(self, namespace, variable):
        """
        Get System Variable
        """
        try:
            _root = self.App.Application.System.Namespaces
            _namespace = namespace.split('::') if '::' in namespace else namespace

            is_nested = lambda obj: obj.Namespaces.Count > 0

            def get_namespace_id(root_obj, namespace):
                for i in range(1, root_obj.Count+1):
                    if root_obj.Item(i).Name.lower() == namespace.lower():
                        return i
                else:
                    raise ValueError('%s not found!'%namespace)

            def get_nested_namespace_obj(root_obj, namespaces):
                _active_object = root_obj
                for ns in namespaces:
                    _ns_id = get_namespace_id(_active_object, ns)
                    if is_nested(_active_object.Item(_ns_id)):    
                        _active_object = _active_object.Item(_ns_id).Namespaces
                    else:
                       return (_ns_id, _active_object)

            def get_variable_id(namespace_obj, variable):
                if not hasattr(namespace_obj, 'Variables'):
                    if not '::' in namespace:
                        raise ValueError('Nested namespaces requires to provide nested '+\
                            'namespaces separated by :: like following: namespace_1::namespace_2')
                var_obj = namespace_obj.Variables
                for i in range(1, var_obj.Count+1):
                    if var_obj.Item(i).Name.lower() == variable.lower():
                        return i
                else:
                    raise ValueError('%s not found in system variables!'%variable)

            _namespace_obj = None
            if isinstance(_namespace, str):      #    Single namespace
                _namespace_obj = _root
                _namespace_id = get_namespace_id(_root, _namespace)
            elif isinstance(_namespace, list):   #    Multiple namespaces
                _namespace_id, _namespace_obj = get_nested_namespace_obj(_root, _namespace)

            _variable_id = get_variable_id(_namespace_obj.Item(_namespace_id), variable)

            sys_var_obj = _namespace_obj.Item(_namespace_id).Variables.Item(_variable_id)

            Logger.write_debug_log('DEBUG', __name__, '{0}::{1}'.format(_namespace, variable))

            return sys_var_obj.Value
        except Exception as error:
            _error = 'Not able to set System Variable {}::{} - {}'.format(
                        _namespace, variable, error)
            print(__name__, _error)
            Logger.write_debug_log('ERROR', __name__, _error)

            print(__name__, type(error).__name__, error,                                       
                    'Line %s' % (sys.exc_info()[2].tb_lineno))

    def write(self, message):
        """
        Write output on CANoe Panel
        """
        try:
            self.App.UI.Write.Output(str(message))              
        except Exception as error:
            _error = 'Not able to write message {0} on CANoe'.format(message)
            Logger.write_debug_log('ERROR', __name__, _error + ','.join(error))

    def close(self):
        """
        The COM server functionality to quit the CANoe application:
        """
        try:
            self.App.Quit()
            Logger.write_debug_log('DEBUG', __name__, 'CANoe.quit()')
        except Exception as error:
            _error = 'Not able to close CANoe COM'
            Logger.write_debug_log('ERROR', __name__, _error + ','.join(error))