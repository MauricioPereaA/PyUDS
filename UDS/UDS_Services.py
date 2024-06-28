"""@UDS_Services.py
*********************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    UDS_Services.py
    - Services message concatenation

*********************************************************************************
"""

# ==============================================================================
#  UDS - Unified Diagnostic Services 
# ==============================================================================

from UDS.services.DynamicallyDefineData import ReadDataByPeriodicIdentifier
from UDS.services.DiagnosticTroubleCode import DiagnosticTroubleCode
from UDS.services.CommunicationControl import CommunicationControl
from UDS.services.ControlDTCSettings import ControlDTCSettings
from UDS.services.DiagnosticSession import DiagnosticSession
from UDS.services.RoutineControl import RoutineControl
from UDS.services.SecurityAccess import SecurityAccess
from UDS.services.TesterPresent import TesterPresent
from UDS.services.WriteDataID import WriteDataID
from UDS.services.ReadDataID import ReadDataID
from UDS.services.IOControl import IOControl
from UDS.services.ECUReset import ECUReset

from UDS.diagnostics import Canoe_Diagnostics

class UDS_Services(Canoe_Diagnostics):

    def __init__(self, functionalAddr=None, *args, **kwargs):

        # False is default value
        self.functionalAddr = False if not functionalAddr else functionalAddr
        Canoe_Diagnostics.__init__(self)

class service(object):
    def __new__(self, *args, **kwargs):
        return globals().keys()

    @staticmethod
    def obj(function):            
        for obj in globals().values():
            if hasattr(obj, function):
                return obj
        raise RuntimeError('No service -> %s <- found'%function)         

if __name__ == '__main__':

    req = 'send_key'
    data = [
        '01',
        '03',
        '05',
        '09',
        '0B',
        '0D',
        '11',
        '13',
        '15'
    ]
    uds = service.obj(req)

    for lvl in data:
        print( uds(req, lvl) )