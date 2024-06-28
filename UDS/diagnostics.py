"""@diagnostics.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    "Here are located functions to send/receive requests/responses.
    ...
    "
Modified by: Mauricio Perea
Date:13 July 2020
This script was added the new feature reset_delay is the time that PYUDs is waiting the module is recovered.

Modified by Mauricio Perea
Date:03/09/2020
Fix the reset_delay parameter, the problem was it was received an None as string so I change the logic

Modified by Andres Yañez
Date:07/09/2021
Refactoring of methods:
* get_diagnostic_device
* send
* get_response_from_canoe

To achieve compatilibity with the  UDS Engine

Creation of method: get_ActiveX_response_from_canoe

Modified by Andres Yañez
Date:11/11/2021

Fix for send method, when you send functional request the framework did not catch the response, the problem was an error
when I refactored the code since in the previous versios we had and conditional if with a duplicate code hence
in the v4.0 I joined this in a single code block but I missed to remove the if and decrease the indentation for this code block.

Modified by Andres Yañez
Date:30/11/2021

Fix to avoid the tester_present_active attribute not exists, it was previously faced but the last fix was incomplete since the name
was only updated in some parts of the class now it was reviewed and the variables is the same throught the whole code.

*******************************************************************************
"""
from __global__ import __logs__
from read_config import read_cfg_file
from misc import timeStamp, hex_op, readable_hex
from CANoe import CANTool
from framework.tools.logs import Logger

import inspect
import time, re, sys, os
from framework.drivers.Power_Supply import * # Not sure still if this will be here

Logger = Logger()
class Canoe_Diagnostics(object):


    def __init__(self, *args, **kwargs):
        # Default is set for Physical Requests
        self.canoe = CANTool()
        self.logs_path = __logs__ + '\\TraceLog.asc'
        self.physical_id = read_cfg_file('CANOE', 'physical_ID', False)
        self.functional_id = read_cfg_file('CANOE', 'functional_ID', False)
        self.uudt_id = read_cfg_file('CANOE', 'UUDT_ID', False)
        self.functional_req_found_ts = []
        self.tester_present = False
        
        self.reset_delay = read_cfg_file('CANOE', 'reset_delay', False)

        self.error_frames_cal = int(read_cfg_file('POWER_SUPPLY', 'error_frames', False))

    def get_diagnostic_device(self, **kwargs):
        """
            Select which dignostic console is going to be interacting
        """
        try:

            if 'tester_id' in kwargs:
            
                self.device_selected = kwargs['tester_id']
                
            else:
            
                self.device_selected = read_cfg_file('CANOE', 'ECU', False)
                
            self.canoe.set_system_variable("Generic_Diagnostics","ConsoleName",self.device_selected)
            time.sleep(0.1)

            Logger.write_debug_log(
                'DEBUG', __name__, 'Active console: ' + self.device_selected)

            return True
            
        except Exception as error:
            _error = 'Not able to reach diagnostic console {}'.format(
                        self.device_selected)
            Logger.write_debug_log('ERROR', __name__, _error)

            print(__name__, type(error).__name__, _error,                                       
                    'Line %s' % (sys.exc_info()[2].tb_lineno))
            return None

    def send(self, request, functionalAddr=False, return_response=True, response_from_log=False,
                    quiet_mode=False, response_delay=1, tester='default', physical_id_rsp = '14DAF1A4x', *args, **kwargs):
        """ 
            Send requests to CANoe
        """
        #=======================================================================
        # Initial params
        #=======================================================================
        if request in ['3E 80']:
            self.tester_present = True
        if request in ['3E 00']:
            self.tester_present = False
        if tester != 'default':
            self.diagnostic_device = self.get_diagnostic_device(tester_id=tester)
            if functionalAddr:  # Tal vez remover con el nuevo Engine ya es posible
                print(
                    __name__, 
                    'Multiple tester is not able to achieve functional requests.'+\
                    ' Not yet implemented') #Esto creo que NO aplica ya pero debo entender que significaba
        
        else:
            self.diagnostic_device = self.get_diagnostic_device() # Set Default Console
            if self.diagnostic_device is None:
                raise RuntimeError(
                        'Make sure you have selected correct settings for your device under test.')

        if return_response and not quiet_mode:
            print(__name__, 'TESTER: ', self.device_selected)
            print(__name__, request)

        if self.tester_present:
            # Start Periodic Tester Present with SB
            self.canoe.set_system_variable("Generic_Diagnostics", "TP_Mode", 4)
        else:
            # Stop Periodic Tester Present
            self.canoe.set_system_variable("Generic_Diagnostics","TP_Mode",0)
         
        # Temporal fix due SID 0x36 overrun messages
        UseActiveX = request.startswith('36')

        #=======================================================================
        # Send Request
        #=======================================================================
        try:
            Logger.write_debug_log('DEBUG', __name__, 'Request: %s'%request)
            
            if UseActiveX:
            
                #breakpoint()
                tester_name = read_cfg_file('CANOE', 'ECU', False)
                network = read_cfg_file('CANOE', 'Network', False)
                diagnostic_tester = self.canoe.App.Networks(network).Devices(tester_name).Diagnostic
                diagReq = diagnostic_tester.CreateRequestFromStream(bytearray.fromhex(request))
                diagReq.Send()
                
            else:
            
                requestframe = bytearray.fromhex(request)
     
                self.canoe.set_system_variable("Generic_Diagnostics","RawData",list(requestframe))
                self.canoe.set_system_variable("Generic_Diagnostics","DiagRqstSize",len(list(requestframe)))
                self.canoe.set_system_variable("Generic_Diagnostics","DiagRqst",int(functionalAddr == True)+1)
            
        except Exception as error:
            Logger.write_debug_log(
                'CRITICAL', __name__, 'Request Error: {0}::{1}'.format(request, error)
            )
            print( '{0} - Not able to send {1}'.format(type(error).__name__, request) )
            
        #=======================================================================
        # Delay after ECU Reset
        #=======================================================================
          
        if request.startswith('11'):
        
            ''' Default delay is 5 second and warning to the user '''
        
            if self.reset_delay == 'None' or not self.reset_delay or self.reset_delay == '0':
                self.reset_delay = 5
                print("ECU Reset delay was taken from default value")
            
            print('Delay of {0} seconds after ECU Reset'.format(self.reset_delay))
            time.sleep(int(self.reset_delay))
            
        #=======================================================================
        # Read out the response
        #=======================================================================
        
        if not return_response:
            Logger.write_debug_log('DEBUG', __name__, 'No response expected!')
            return 'No response expected'
        try:
        
            if UseActiveX:
            
                while diagReq.Pending:
                    time.sleep(0.25)
            
            else:
        
                while self.canoe.get_system_variable("Generic_Diagnostics","DiagRqst") != 3:
                    time.sleep(0.05)

            if response_from_log:

                return self.get_response_from_log(
                    request=request, quiet_mode=quiet_mode, physical_id_rsp = physical_id_rsp, functionalAddr = functionalAddr
                )

            if UseActiveX:
            
                return self.get_ActiveX_response_from_canoe(
                diagnostic_request_object=diagReq,
                quiet_mode=quiet_mode,
                response_delay=response_delay
                )
                
            else:

                return self.get_response_from_canoe(
                    quiet_mode=quiet_mode,
                    response_delay=response_delay
                )

        except Exception as error:
            print(__name__, 'Problem while Reading out the response')
            print(type(error).__name__, error)

    def multiple_request(self, *requests):
        """ 
            Send multiple requests from multiple testers
        """
        delay_on_message = 0.050
        tester = [
            read_cfg_file('CANOE', 'ECU', False),
            read_cfg_file('CANOE', 'ECU_2', False)
        ]
        network = read_cfg_file('CANOE', 'Network', False)

        if tester[1] == 'None':
            raise AttributeError(
                'Not able to execute multiple tester function. Please provide a valid Tester in \'config.cfg.\'')            
        if len(requests) != 2:
            raise ValueError(
                'You need to provide 2 requests as argument. Ex. multiple_tester(\'10 01\', \'10 03\')')            
        # Send requests
        print(__name__, 'Attempting to send:')
        for i in range(2):
            print(__name__, tester[i], requests[i])            
        
        diagnostic_device_1 = self.canoe.App.Networks(network).Devices(tester[0]).Diagnostic
        diagReq_1 = diagnostic_device_1.CreateRequestFromStream(
            bytearray.fromhex(requests[0]))
        diagnostic_device_2 = self.canoe.App.Networks(network).Devices(tester[1]).Diagnostic
        diagReq_2 = diagnostic_device_2.CreateRequestFromStream(
            bytearray.fromhex(requests[1]))
        # Begin count
        start = float(timeStamp('timeOnly')[6:])
        diagReq_1.Send()
        time.sleep(delay_on_message)
        diagReq_2.Send()
        end = float(timeStamp('timeOnly')[6:])
        print(__name__, 'Multiple tester. Executed in %s seconds'%str(end-start))
        
        responses = [
            self.get_ActiveX_response_from_canoe(            
                diagnostic_request_object=diagReq_1,
                quiet_mode=False
            ), 
            self.get_ActiveX_response_from_canoe(            
                diagnostic_request_object=diagReq_2,
                quiet_mode=False
            )
        ]
        if 'No response' in responses[1]:
            return responses[0]

        return responses[1]
    
    def get_ActiveX_response_from_canoe(self, diagnostic_request_object, quiet_mode=False, response_delay=1):
        if diagnostic_request_object.Responses.Count > 0:
            diagResp = diagnostic_request_object.Responses(1)
            rsp_type = { True:'Positive', False:'Negative' }
                                
            result = [format(e, '#04x') for e in diagnostic_request_object.Responses(1).Stream] 
            # debugLog -> Write Response
            Logger.write_debug_log(
                'DEBUG', __name__, 'Response: %s'%readable_hex(result)
            )
            # debugLog -> Write response type & device involved
            Logger.write_debug_log(
                'DEBUG', __name__, '{0} | {1}'.format(
                    rsp_type[diagResp.Positive],  diagResp.Sender
            ))

            if not quiet_mode: 
                print(__name__, readable_hex(result))

            time.sleep(response_delay)
            
            return result
        else:
            Logger.write_debug_log('DEBUG', __name__, 'ATENTION::No response received!')
            return '   No response received!'


    def get_response_from_canoe(self, quiet_mode=False, response_delay=1):
    
        RspSize = self.canoe.get_system_variable("Generic_Diagnostics","DiagRspSize")
        
        self.canoe.set_system_variable("Generic_Diagnostics","DiagRqst",'0') # Finish Request Reply Process
        
        while self.canoe.get_system_variable("Generic_Diagnostics","DiagRqst") != 0:
                time.sleep(0.02)
        
        if RspSize > 0:
        
            DataBytes = self.canoe.get_system_variable("Generic_Diagnostics","RspRawData")
            result = [format(e, '#04x') for e in DataBytes[0:RspSize]]
            rsp_type = { True:'Positive', False:'Negative' }
            # debugLog -> Write Response
            Logger.write_debug_log(
                'DEBUG', __name__, 'Response: %s'%readable_hex(result)
            )
            # debugLog -> Write response type & device involved
            Logger.write_debug_log(
                'DEBUG', __name__, '{0} | {1}'.format(
                    rsp_type[RspSize != 0],  self.device_selected
            ))

            if not quiet_mode: 
                print(__name__, readable_hex(result))

            time.sleep(response_delay)
            
            return result
        else:
            Logger.write_debug_log('DEBUG', __name__, 'ATENTION::No response received!')
            return '   No response received!'
            
    
    def get_response_from_log(self, quiet_mode=False, *args, **kwargs):
        """
            Determinate response from log file - Functional and physical requests 
        """
        if not 'request' in kwargs:
            raise RuntimeError('-> request <- param required to get response')

        request = kwargs['request']
        physical_id_rsp = kwargs['physical_id_rsp']
        functionalAddr = kwargs['functionalAddr']

        if not functionalAddr:
            if self.physical_id[4:6] != physical_id_rsp[4:6]:
                self.physical_id = physical_id_rsp
        else:
            if self.functional_id[6:8] != self.physical_id[4:6]:
                self.physical_id = self.physical_id.replace(self.physical_id[4:6], self.functional_id[6:8])

        # -- Request Length --
        length = len( request.split(' ') )
        if not length>1:
            request = re.findall('..', request)
            length = len(
                request
            )
            request = ' '.join(request)

        # -- Positive Response --
        data = '' if '14' in request[:2] else ' '+request[3:5]
        positive_rsp = ('{0}{1}'.format(
            hex_op('40', request[:2]),data)).upper()
        positive_pattern = '[0-9A-F]{2} ' + positive_rsp + (' ..' * (7-length))

        # -- Negative Response --
        negative_rsp = ('7F {0}'.format(request[:2])).upper()
        negative_pattern = '[0-9A-F]{2} 7F .. ..'

        reached_request = False
        response_found = False
        found_rsp = []

        # default Allowed timeout to find response: 
        #   -- 20 attempts*0.25s = 4s
        attempts = 0
        attempts_permitted = 20
        delay_per_attempt = 0.25 # Seconds


        # Reading TraceLog to find latests response
        time.sleep(12)  # Time necessary for the log to be updated
        while not reached_request or not response_found:
            count_line = 0
            lines_to_read = 200
            Logger.write_debug_log('DEBUG', __name__, 'Attempt: %s'%str(attempts))

            for line in reversed(open(self.logs_path, 'r').readlines()):
                if self.functional_id in line:
                    if request in line:
                        reached_request = True
                        Logger.write_debug_log('DEBUG', __name__, 
                            'Request reached in TraceLog: %s'%line)
                        break # if no response found after request, stop searching. 
                # Physical ID Found
                if self.physical_id in line:
                    search_rsp = re.search(positive_pattern, line)
                    rsp = None if not search_rsp else search_rsp.group(0)

                    # regex - Find Negative pattern
                    if not rsp: 
                        search_rsp = re.search(negative_pattern, line)
                        rsp = None if not search_rsp else search_rsp.group(0)

                    # if -response- was found above
                    if rsp:
                        Logger.write_debug_log('DEBUG', __name__, 
                            'Found response from server: %s'%line)
                        # Get timestamp from line
                        find_timestamp = re.search(r'[ 0-9][0-9]\.[0-9]{6}', line)
                        line_ts = find_timestamp.group(0)

                        # timestamp is already in previous found responses?
                        if not line_ts in self.functional_req_found_ts:
                            self.functional_req_found_ts.append(line_ts)
                            Logger.write_debug_log('DEBUG', __name__,
                                'Previous found responses: %s'%''.join(
                                    self.functional_req_found_ts
                                ))
                            if positive_rsp.upper() in rsp.upper():
                                found_rsp.append(rsp.lower())                            
                            elif negative_rsp in rsp:
                                found_rsp.append(rsp.lower())

                            if any(found_rsp): 
                                response_found = True
                                break
                        
                count_line+=1
                if count_line > lines_to_read:
                    Logger.write_debug_log('FAIL', __name__,
                        'Reached %s lines read and response was not found. Reattemting...'%lines_to_read)
                    break

            if attempts > attempts_permitted: break

            attempts += 1
            time.sleep(delay_per_attempt)

        if not len(found_rsp) > 0:
            Logger.write_debug_log('DEBUG', __name__, 'No response received!')
            return '   No response received!'
            
        frame = found_rsp[-1]
        length = int( frame[:2] )

        if length > 7:
            Logger.write_debug_log('ERROR', __name__, 
                'PyUDS still does not support multiframe reading responses')
            raise RuntimeError('PyUDS still does not support multiframe reading responses')

        # Format response => [0xXX, 0xYY, 0xZZ, ..]
        response = ['0x'+x for x in frame.split(' ')][1:length+1]
        Logger.write_debug_log('DEBUG', __name__, 'Response found: %s'%readable_hex(response))    
        if not quiet_mode: print(__name__, readable_hex(response))
                       
        return response 

    def catch_error_frames(self):
        """
            Determines whether the bus if OFF considering error frames catched.
        """
        error_frame_pattern = r'\d+.\d+ \d  ErrorFrame	Flags = \dx[a-f0-9]+	CodeExt = \dx[a-f0-9]+'
        
        total_found = 0                              # Found error frames
        required_to_be_off = self.error_frames_cal   # After X frames, CAN bus is considered to be OFF
        read_until_line = 35

        with open(self.logs_path, 'r', errors='ignore') as trace_log:
            for count, line in enumerate( reversed(trace_log.readlines()) ):
                search = re.search(error_frame_pattern, line)
                found = 0 if not search else 1

                total_found += found
                if count == read_until_line: break  
        return total_found > required_to_be_off

    def normal_comm(self):
        can_id_set = set()
        def _get_can_id(frame):
            patterns = {
                'can_id':       '  [0-9A-F]+x|  [0-9A-F]{3}'    
            }
            # Looking for CAN ID - Verify this is a CAN Frame
            find_pattern = lambda pattern: re.findall(pattern=patterns.get(pattern, []), string=line)
            found_can_id = find_pattern('can_id')
            if any(found_can_id):
                return found_can_id[-1][2:]
            return False
        try:
            with open(self.logs_path, 'r') as ASC:
                for line_number, line in enumerate(reversed(ASC.readlines())):
                    if _get_can_id(line) == False:
                        pass
                    else:
                        can_id_set.add(_get_can_id(line))
                    if line_number == 20:                  # Arbitrary number to check a bunch of CAN messages and not all of them
                        break

                if len(can_id_set) > 0 and len(can_id_set) <= 4: # This is for a Green ECU as this can include a max of four matches if the normal comm is disabled,
                                                                 # which are two testers (physical and functional), the response for the ECU and one CAN message which the ECU is sending periodically.
                    return True                                  
                else:
                    return False                                 # --> More than 4 matches means that normal communication is enabled 

        except Exception as error:
            Logger.write_debug_log(
                'DEBUG', __name__, 'Log file - pattern to search error')
            print(__name__, 'Something went wrong when attempting to find the pattern in the trace log')
        

