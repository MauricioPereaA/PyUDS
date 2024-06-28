"""@power_supply.py
*******************************************************************************
@copyright    Copyright 2019 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    Power supply HAL. 
@author: Andres Yañez (Andres.Yanez@-corporation.com)
Date:31 Agosto 2021
    
*******************************************************************************
"""
from pkg_resources import require
from pyvisa import constants
import datetime
import time

#####################################################################################################################################################

# IMPORTANT: This code will not be necessary if we move pyUDS to Python 3.9 or greather because it is native in those versions

# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Abstract Base Classes (ABCs) according to PEP 3119."""


def abstractmethod(funcobj):
    """A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj


class abstractclassmethod(classmethod):
    """A decorator indicating abstract classmethods.

    Deprecated, use 'classmethod' with 'abstractmethod' instead:

        class C(ABC):
            @classmethod
            @abstractmethod
            def my_abstract_classmethod(cls, ...):
                ...

    """

    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)


class abstractstaticmethod(staticmethod):
    """A decorator indicating abstract staticmethods.

    Deprecated, use 'staticmethod' with 'abstractmethod' instead:

        class C(ABC):
            @staticmethod
            @abstractmethod
            def my_abstract_staticmethod(...):
                ...

    """

    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)


class abstractproperty(property):
    """A decorator indicating abstract properties.

    Deprecated, use 'property' with 'abstractmethod' instead:

        class C(ABC):
            @property
            @abstractmethod
            def my_abstract_property(self):
                ...

    """

    __isabstractmethod__ = True


try:
    from _abc import (get_cache_token, _abc_init, _abc_register,
                      _abc_instancecheck, _abc_subclasscheck, _get_dump,
                      _reset_registry, _reset_caches)
except ImportError:
    from _py_abc import ABCMeta, get_cache_token
    ABCMeta.__module__ = 'abc'
else:
    class ABCMeta(type):
        """Metaclass for defining Abstract Base Classes (ABCs).

        Use this metaclass to create an ABC.  An ABC can be subclassed
        directly, and then acts as a mix-in class.  You can also register
        unrelated concrete classes (even built-in classes) and unrelated
        ABCs as 'virtual subclasses' -- these and their descendants will
        be considered subclasses of the registering ABC by the built-in
        issubclass() function, but the registering ABC won't show up in
        their MRO (Method Resolution Order) nor will method
        implementations defined by the registering ABC be callable (not
        even via super()).
        """
        def __new__(mcls, name, bases, namespace, **kwargs):
            cls = super().__new__(mcls, name, bases, namespace, **kwargs)
            _abc_init(cls)
            return cls

        def register(cls, subclass):
            """Register a virtual subclass of an ABC.

            Returns the subclass, to allow usage as a class decorator.
            """
            return _abc_register(cls, subclass)

        def __instancecheck__(cls, instance):
            """Override for isinstance(instance, cls)."""
            return _abc_instancecheck(cls, instance)

        def __subclasscheck__(cls, subclass):
            """Override for issubclass(subclass, cls)."""
            return _abc_subclasscheck(cls, subclass)

        def _dump_registry(cls, file=None):
            """Debug helper to print the ABC registry."""
            print(f"Class: {cls.__module__}.{cls.__qualname__}", file=file)
            print(f"Inv. counter: {get_cache_token()}", file=file)
            (_abc_registry, _abc_cache, _abc_negative_cache,
             _abc_negative_cache_version) = _get_dump(cls)
            print(f"_abc_registry: {_abc_registry!r}", file=file)
            print(f"_abc_cache: {_abc_cache!r}", file=file)
            print(f"_abc_negative_cache: {_abc_negative_cache!r}", file=file)
            print(f"_abc_negative_cache_version: {_abc_negative_cache_version!r}",
                  file=file)

        def _abc_registry_clear(cls):
            """Clear the registry (for debugging or testing)."""
            _reset_registry(cls)

        def _abc_caches_clear(cls):
            """Clear the caches (for debugging or testing)."""
            _reset_caches(cls)


class ABC(metaclass=ABCMeta):
    """Helper class that provides a standard way to create an ABC using
    inheritance.
    """
    __slots__ = ()
    
#####################################################################################################################################################

class ICOM_Creator:

    @staticmethod
    def create_object(interface, device_name, options):
        if interface == 'USB':
            return USB(device_name, options)
        if interface == 'Serial':
            return Serial(device_name, options)
        if interface == 'GPIB':
            return GPIB(device_name, options)
        return None

class ICOM(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)
                
    def __init__(self, device_name, options):
        self._protected_options = self.map_options(options)
                
    @abstractmethod
    def read(self, command):
        raise NotImplementedError

    @abstractmethod
    def write(self, command):
        # This method is intended to read the current from the power supply
        raise NotImplementedError

    def map_options(self, options):
        # This method is to map a string with delimiter to the Options Dictionary
        if options != '' and options != 'None':
            self._protected_options = dict(item.split("=") for item in options.split(";"))
        
    def get_option_byname(self, name, default):
        # Check if Dict is empty
        if bool(self._protected_options):
            # This method is to retrive a stored option
            if name in self._protected_options:
                return self._protected_options[name]
            else:
                return default
        else:
            return default

class USB(ICOM):

    def __init__(self, device_name, options):
        super().__init__(device_name, options)
        try:
            require("pyvisa-py")
            import visa
            self.__rm__ = visa.ResourceManager()
            self.__device__ = self.__rm__.open_resource(device_name)
            if self.__device__ is None:
                raise RuntimeError('Device was not detected.')
        except Exception as error:
            print(__name__, type(error).__doc__, type(error).__name__, error)
                
    def read(self, command):
        return self.__device__.query(command)

    def write(self, command):
        return self.__device__.write(command)
        
    def __del__(self):
        try:
            self.__device__.close()
        except Exception as error:
            pass
        
class GPIB(ICOM):

    def __init__(self, device_name, options):
        super().__init__(device_name, options)
        try:
            require("pyvisa-py")
            import visa
            self.__rm__ = visa.ResourceManager()
            self.__device__ = self.__rm__.open_resource(device_name)
            if self.__device__ is None:
                raise RuntimeError('Device was not detected.')
        except Exception as error:
            print(__name__, type(error).__doc__, type(error).__name__, error)
                
    def read(self, command):
        return self.__device__.query(command)

    def write(self, command):
        return self.__device__.write(command)
        
    def __del__(self):
        try:
            self.__device__.close()
        except Exception as error:
            pass

class Serial(ICOM):

    def __init__(self, device_name, options):
        super().__init__(device_name, options)
        try:
            require("pyvisa-py")
            import visa
            br_value = self.get_option_byname('Baudrate', 9600)
            self.__rm__ = visa.ResourceManager()
            self.__device__ = self.__rm__.open_resource(device_name,baud_rate=br_value)
            if self.__device__ is None:
                raise RuntimeError('Device was not detected.')
        except Exception as error:
            print(__name__, type(error).__doc__, type(error).__name__, error)
                
    def read(self, command):
        return self.__device__.query(command)

    def write(self, command):
        return self.__device__.write(command)
        
    def __del__(self):
        try:
            self.__device__.close()
        except Exception as error:
            pass


#####################################################################################################################################################

class IPowerSupply(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    def __init__(self, interface, device_name, options):
        self._protected_Device = ICOM_Creator().create_object(interface, device_name, options)
        self._protected_default_settings = {
                'voltage': '12.5',
                'current': '1.0'
        }

    @abstractmethod
    def get_current(self):
        # This method is intended to read the current from the power supply
        raise NotImplementedError
    
    @abstractmethod
    def reset(self):
        # This method is intended to reset the power supply
        raise NotImplementedError
     
    @abstractmethod
    def clear_alarms(self):
        # This method is intended to clear the alarms at power supply
        raise NotImplementedError
     
    #@abstractmethod    
    def set_limits(self, data):
        # This method is intended to write limit values as OVP, OVC, etc. at power supply
        raise NotImplementedError

    @abstractmethod
    def get_voltage(self):
        # This method is intended to read the voltage from the power supply
        raise NotImplementedError
        
    @abstractmethod
    def get_output(self):
        # This method is intended to read the output state from the power supply
        raise NotImplementedError
    
    #@abstractmethod
    def get_alarms(self):
        # This method is intended to read the active alarms from the power supply
        raise NotImplementedError

    @abstractmethod
    def settings(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def output(self, state):
        raise NotImplementedError

class SCPI_PS_Base(IPowerSupply):

    def get_current(self):
        # This method is intended to read the current from the power supply
        return float(self._protected_Device.read(':MEASure:CURRent?').split('\n')[0])

    def get_voltage(self):
        # This method is intended to read the voltage from the power supply
        return float(self._protected_Device.read(':MEASure:VOLTage?').split('\n')[0])
        
    def get_output(self):
        # This method is intended to read the output state from the power supply
        return int(self._protected_Device.read(':OUTPut:STATe?').split('\n')[0])
        
    def clear_alarms(self):
        # This method is intended to clear the alarms at power supply
        try:
            self._protected_Device.write('OUTPut:PROTection:CLEar')
        except Exception as error:
            pass

    def reset(self):
        # This method is intended to reset the power supply
        try:
            self._protected_Device.write('RST')
        except Exception as error:
            pass
        
    def settings(self, *args, **kwargs):
        # /============ Set Current ============/
        if 'current' in kwargs:
            try:
                current = kwargs['current']
                print(__name__, 'Setting current to:', current)
                self._protected_Device.write('CURRent:TRIGgered {};:INITiate;*TRG'.format(current))
            except Exception as error:
                pass
        # /============ Set Voltage ============/
        if 'voltage' in kwargs:
            try:
                volts = kwargs['voltage']
                print(__name__, 'Setting voltage to:', volts)
                s_volt = str(volts)
                self._protected_Device.write('VOLTage:LEVel '+s_volt)#'VOLTage:TRIGgered {};:INITiate;*TRG'.format(volts)
            except Exception as error:
                pass
        
        if 'default' in args:
            print(__name__, 'Restoring settings to default')
            try:
                self._protected_Device.write('CURRent:TRIGgered {};:INITiate;*TRG'.format(
                    self._protected_default_settings['current']
                ))
                self._protected_Device.write('VOLTage:TRIGgered {};:INITiate;*TRG'.format(
                    self._protected_default_settings['voltage']
                ))
            except Exception as error:
                pass
    
    def output(self, state):
        if not isinstance(state, bool):
            raise RuntimeError('Output must be a boolean value.')
        
        if state:
        # /============ Turn ON ============/
            try:
                print(__name__, 'Turning ON')
                self._protected_Device.write('OUTPut ON')
            except Exception as error:
                pass
        else:
        # /============ Turn OFF ============/
            try:
                print(__name__, 'Turning OFF')
                self._protected_Device.write('OUTPut OFF')
            except Exception as error:
                pass
                
class KeySight_N57XX(SCPI_PS_Base):

    #PENDING CONCATENA MULTIPLE     
    def get_alarms(self):
        # This method is intended to read the active alarms from the power supply
        alarms = int(self._protected_Device.read(':STAT:QUES?').split('\n')[0])
        if alarms == 1:
            alarm_msg = "OVP Tripped"
        elif alarms == 2:
            alarm_msg = "OCP Tripped"
        elif alarms == 3:
            alarm_msg = "OTP Tripped"
        else:
            alarm_msg = "Unknown Alarm"
        return alarm_msg
            
    def set_limits(self, *args, **kwargs):
        # /============ Set Low Voltage Limit ============/
        if 'VLow' in kwargs:
            try:
                low_voltage = kwargs['VLow']
                print(__name__, 'Set Low Voltage Limit to:', low_voltage)
                self._protected_Device.write('VOLTage:LIMit:LOW '.format(low_voltage))
            except Exception as error:
                pass
        # /============ Set Over Voltage ============/
        if 'OVV' in kwargs:
            try:
                over_voltage = kwargs['OVV']
                print(__name__, 'Setting over voltage limit to:', over_voltage)
                self._protected_Device.write('VOLTage:PROTection:LEVel '.format(over_voltage))
            except Exception as error:
                pass
                
class KeySight_N87XX(KeySight_N57XX):
    # ALL methods are inherited, only we create this to instanciate the object with this model
    def get_power(self):
        return 1

class Tektronix_BK911X(SCPI_PS_Base):

    def get_power(self):
        # This method is intended to read the power from the power supply
        return float(self._protected_Device.read(':MEASure:POWer?').split('\n')[0])
        
    def set_limits(self, *args, **kwargs):
        # /============ Set Low Voltage Limit ============/
        if 'SWVProt' in kwargs:
            try:
                SW_voltage = kwargs['SWVProt']
                print(__name__, 'Set SW Protection Level:', SW_voltage)
                self._protected_Device.write('VOLTage:PROTection:LEVel '.format(SW_voltage))
            except Exception as error:
                pass
        # /============ Set Under Voltage ============/
        if 'UVC' in kwargs:
            try:
                under_voltage = kwargs['UVC']
                print(__name__, 'Setting under voltage limit to:', under_voltage)
                self._protected_Device.write('VOLTage:LIMit:LEVel '.format(under_voltage))
            except Exception as error:
                pass
        # /============ Set Over Voltage ============/
        if 'OVV' in kwargs:
            try:
                over_voltage = kwargs['OVC']
                print(__name__, 'Setting over voltage limit to:', over_voltage)
                self._protected_Device.write('VOLTage:RANGe '.format(over_voltage))
            except Exception as error:
                pass
        
    def save_sequence(self):
        # This method is intended to save the active sequence
        self._protected_Device.write(':SEQuence:SAVe')
        
    def edit_sequence(self, seq_index):
        # This method is intended to set the sequence to edit
        self._protected_Device.write('SEQuence:EDIT '.format(seq_index))
        
    def edit_step(self, step_index, voltage, current, duration, slope):
        # This method is intended to configure a step of the sequence
        self._protected_Device.write(':SEQuence:VOLTage {0},{1};:SEQuence:CURRent {0},{2};:SEQuence:WIDTh {0},{3};:SEQuence:SLOPe {0},{4}'.format(step_index, voltage, current, duration, slope))

class Keithley_2260B(SCPI_PS_Base):

    def get_power(self):
        # This method is intended to read the power from the power supply
        return float(self._protected_Device.read(':MEASure:POWer?').split('\n')[0])
        
    def set_limits(self, *args, **kwargs):
        # /============ Set Low Voltage Limit ============/
        if 'VLow' in kwargs:
            try:
                low_voltage = kwargs['VLow']
                print(__name__, 'Set Low Voltage Limit to:', low_voltage)
                self._protected_Device.write('VOLTage:LIMit:LOW '.format(low_voltage))
            except Exception as error:
                pass
        # /============ Set Over Voltage ============/
        if 'OVV' in kwargs:
            try:
                over_voltage = kwargs['OVV']
                print(__name__, 'Setting over voltage limit to:', over_voltage)
                self._protected_Device.write('VOLTage:PROTection:LEVel '.format(over_voltage))
            except Exception as error:
                pass
        # /============ Set Over Current ============/
        if 'OVC' in kwargs:
            try:
                over_current = kwargs['OVC']
                print(__name__, 'Setting over current limit to:', over_current)
                self._protected_Device.write('CURRent:PROTection:LEVel '.format(current))
            except Exception as error:
                pass
              
class PowerSupplyFactory:

    def __init__(self):
        # Default Power Supplies in this package
        self._PSModels = {'Generic':SCPI_PS_Base,'KeySight_N57XX':KeySight_N57XX, 'Keithley_2260B': Keithley_2260B}

    def register_model(self, model, creator):
        self._PSModels[model] = creator

    def get_powersupply(self, model, interface, device_name, options):
        creator = self._PSModels.get(model)
        if not creator:
            raise ValueError(model)
        return creator(interface, device_name, options)

#####################################################################################################################################################

# Unit Test Code

if __name__ == '__main__':
    print('-power_supply- object was created.\n')
    #power_supply = KeySight_N57XX('USB', 'USB0::0x0957::0x9507::US15M3879P::INSTR', '')
    #power_supply = PowerSupplyFactory().get_powersupply('KeySight_N57XX', 'USB', 'USB0::0x0957::0x9507::US15M3879P::INSTR', '')
    #power_supply = PowerSupplyFactory().get_powersupply('Keithley_2260B', 'Serial', 'COM4', '')
    power_supply = PowerSupplyFactory().get_powersupply('Tektronix_BK911X', 'USB', 'USB0::0xFFF::0x9115::800422020757320031::INSTR', '')
    
    print('Power supply settings reseting to default values\n')
    power_supply.settings( 'default' )

    print('Output turn ON\n')
    power_supply.output( True )
    
    time.sleep(3)
    
    #breakpoint()
    
    ecurr = power_supply.get_current()
    volt = power_supply.get_voltage()
    message = 'Power Supply Current is: ' + str(ecurr) + ' and voltage is: ' + str(volt)
    print(message)

    