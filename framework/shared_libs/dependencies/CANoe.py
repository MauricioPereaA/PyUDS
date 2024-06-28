"""@CANoe.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    Use of CANalyzer/CANoe as a COM server.
    

@note ABBREVIATIONS:
        - COM: Component Object Model
*******************************************************************************
"""
# ==============================================================================
# Python import packages
# ==============================================================================
import win32com.client
import inspect
import time


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
        except Exception as error:
            print(__name__, error)
            print(__name__, "Method: ", inspect.stack()[0][0].f_code.co_name)
            print(__name__, "Class: ", self.__class__.__name__)
   
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
            # Set Initialization variable to 1
            # InitValue = self.App.Environment.GetVariable('Ev_Initialization_Value')
            # InitValue.Value = 1

            # Signal implementation
            signalObj = self.App.Bus.GetSignal( 1, message, signal)
            signalObj.RawValue = value
            
            print(__name__, signalObj.FullName, signalObj.IsOnline, signalObj.RawValue)
            return signalObj.IsOnline

        except Exception as error:
            print(__name__, error)
            print(__name__, "Method: ", inspect.stack()[0][0].f_code.co_name)
            print(__name__, "Class: ", self.__class__.__name__)
            raise RuntimeError('Not able to set signal')
