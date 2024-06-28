"""@validate.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    ValidateClass processes response data to compare with a provided expected
    to determine whether a Test PASSES or FAILS

    -- This library is under development and has not been used yet.

Modified by Mauricio Perea
Date:13 July 2020
This script was modified for extended the robustness of feature expected byte_index & expected_byte

Modified by Mauricio Perea
Date:7 October 2020
Import object shared
Modified the expected byte parameter, change the name variable range by interval
Modified the periodic data , adjust the seed value for MSM and the others has the default value

Modified by Mauricio Perea
Date:13 October 2020
In the previous version the information from speed was in inversed order, it was fixed.

Modified by Mauricio Perea
Date:14 October 2020
Fixed the reported information in the data parameter. Before the actualRsp took the index position 3, but it does not contemplate other cases
so the index position now is star_byte covering all the cases.These changes applied also for partialData and dataLength
Date:15 October 2020
Fix Add the start_byte  in the line 222 as part of peer review

Modified by Mauricio Perea
Date:10 November 2020
"periodic_data" verification routine was modified to accept a results as tuple of dictionaries

Modified by Mauricio Perea
Date:04/11/2020
Added in the function validate the positive response for request 19 02 that generate the dtc_list and compare the initial_dtcs vs current_dtcs

*******************************************************************************
"""
import framework.shared_functions as shared
from logs import Logger
import misc as tools

# NRC dictionary
dictNRC = tools.readJSON(
    shared.automation_home + '\\UDS\\response_codes.json'
)

Logger = Logger()


class ValidateClass:
    """
    Under implementation. validate() function still working on PyUDS v2.2.4.3
    """

    def __init__(self, actualRsp, expectedRsp=None,
                 data=None, partialData=None, dataLength=None):
        raise NotImplementedError('Under implementation -  Use validate() function.')

        self.actual_response = self.format_hex(*actualRsp)
        self.expected_response = expectedRsp.upper()
        self.data = data.upper()
        self.partial_data = data.upper()
        self.data_length = dataLength

        # == Test Status variables ==
        self.test_status = None
        self.failure_cause = None

    def format_hex(self, *data_response):
        # data_response should be processed to return a readable hex list - ['FF', 'FF'.., 'FF']
        return data_response

    def test_result(self):
        # 1. Function meant to compare expected and actual data
        # 2. Set failure description into variable failure_cause 
        # 3. Return True (PASSED), False (FAILED)
        if self.expected_response == 'POSITIVE':
            """
                Go through all expected possible escenarios
                If no Failure found, test PASSES
            """
            if None in self.actual_response:
                self.failure_cause = 'No response when expecting %s' % self.expected_response
                return None

            if self.actual_response[0] == '7F':
                negative_response_code = self.actual_response[2]
                self.failure_cause = 'NRC {0}: {1} when expecting a Positive response'.format(
                    negative_response_code, '[PLACEHOLDER] - pending to add JSON dict for NRCs'
                )
                return False

            if self.data_length:
                start_byte = 3 if self.actual_response[0] in ['62', '6E'] else (
                    4 if self.actual_response[0] in ['71'] else 2)
                if not isinstance(self.data_length, list):
                    # Data length unique value
                    if not len(self.actual_response[start_byte:]) == self.data_length:
                        self.failure_cause = 'Data Length is {0}, while expected is {1}'.format(
                            len(self.actual_response[3:]), self.data_length)
                        return False
                else:
                    # Data length range
                    dataRangeLength = range(self.data_length[0], self.data_length[1] + 1)
                    if not len(self.actual_response[3:]) in dataRangeLength:
                        self.failure_cause = 'Data Length is {0} out of range {1}'.format(
                            len(self.actual_response[3:]), self.data_length)
                        return False

            if self.data:

                start_byte = 3 if self.actual_response[0] in ['62', '6E'] else (
                    4 if self.actual_response[0] in ['71'] else 2)
                if not self.data == self.actual_response[start_byte:]:
                    self.failure_cause = 'Data is {0}, while expected is {1}'.format(
                        self.actual_response[3:], self.data
                    )
                    return False
            if self.partial_data:
                string_complete_response = ' '.join(self.actual_response)
                if not self.partial_data in string_complete_response:
                    self.failure_cause = 'partialData {0} is not in {1}'.format(
                        self.partial_data, string_complete_response)
                    return False

            if self.failure_cause: self.failure_cause = None
            return True
        elif self.expected_response == 'NEGATIVE':
            if None in self.actual_response:
                self.failure_cause = 'No response when expecting %s' % self.expected_response
                return False

            if not self.actual_response[0] == '7F':
                self.failure_cause = 'Negative response is expected. Actual response: {0}'.format(
                    ' '.join(self.actual_response))
                return False

            negative_response_code = self.actual_response[2]
            if self.data:
                if not self.data[0] == negative_response_code:
                    self.failure_cause = 'NRC {0}:{1} when expecting {2}'.format(
                        negative_response_code, '[PLACEHOLDER] - NRC JSON dict pending to implement', self.data[0])
                    return False
            else:
                self.failure_cause = 'No NRC specified for Negative test'
                return False
            return True
        pass


def validate(actualRsp, expected_response='No response', data=None, data_2=None, periodic_data=None,
             partialData=None, dataLength=None, expected_byte=None, byte_index=None, unexpected_response=False,
             dtc_list=[], data_dtc=None, NRC78_data=None):
    ######  Function Parameters Description  ######
    # Param         | Type     |  Description
    # -------------------------------------------------------------
    # actualRsp     | Array     | Response from Canoe_Diagnostics
    # expected_response   | String    | Negative, Positive OR No response
    # data          | Array     | Only mandatory for Negative & Positive if data comparison, else None
    # dataLength    | Integer   | Expected data length.
    # dtc_list      | List      | Save information about current dtc_list
    # data_dtc      | Tuple     | Deliver information about dtc_initial or dtc_initial  + protected message dtc
    # -------------------------------------------------------------
    # NOTE: If "dataLength" is required but not "data" parameter, please just put None as function param
    # -------------------------- Example --------------------------
    # validate( ['0x00', '0x01', '0x02'], 'Positive', None, 3 )
    # --------------------------------------------------------------
    try:
        if expected_response == 'Positive':

            if 'No response received' in actualRsp:
                return False, actualRsp

            if actualRsp[0] == '0x7f':
                NRC = actualRsp[2]
                Logger.write_debug_log('FAIL', __name__, '{0} - {1}'.format(actualRsp, dictNRC[NRC]))
                failure_cause = 'NRC {0}: {1} when expecting a Positive response'.format(NRC, dictNRC[NRC])
                return False, failure_cause

            # Verify if the request of 19 02 09 is positive
            # len(actualRsp[2]) means that this code check the 3rd byte of the response this byte is different for each project
            # for this reason only ask about if there is a byte present.
            # the propouse is that in the next version is implement this 3rd byte customizable for each project in the GUI

            if actualRsp[0] == '0x59' and actualRsp[1] == '0x02' and len(actualRsp[2]) == 4:

                # Verify if the response has more than one dtc and if the dtc are in blocks of 4 bytes

                if len(actualRsp[3:]) != 0 and len(actualRsp[3:]) % 4 == 0:
                    temp_all_dtc = actualRsp[3:]
                    temp_all_dtc = [i.replace('0x', '').upper() for i in temp_all_dtc]
                    temp_sublist_dtc = []
                    # It is important to clear the dtc_list otherwise storage the previous dtc
                    dtc_list.clear()
                    for i in range(len(temp_all_dtc)):
                        # This conditional skip the four byte of dtc that is status
                        if (i + 1) % 4 == 0:
                            dtc_list.append(temp_sublist_dtc.copy())
                            temp_sublist_dtc.clear()
                            continue
                        temp_sublist_dtc.append(temp_all_dtc[i])

            if dataLength:
                start_byte = 3 if actualRsp[0] in ['0x62', '0x6e', '0x6f'] else (4 if actualRsp[0] in ['0x71'] else 2)
                if not isinstance(dataLength, list):
                    Logger.write_debug_log('DEBUG', __name__,
                                           'Expecting data lengh: {} | Start Byte: {} | Response: {}'.format(
                                               dataLength, start_byte, tools.readable_hex(actualRsp[start_byte:])
                                           ))
                    # Data length unique value
                    if not len(actualRsp[start_byte:]) == dataLength:
                        if not unexpected_response:
                            failure_cause = 'Data Length is {0}, while expected is {1}'.format(
                                len(actualRsp[start_byte:]), dataLength)
                            Logger.write_debug_log('FAIL', __name__, failure_cause)
                            return False, failure_cause
                else:
                    # Data length range
                    dataRangeLength = range(dataLength[0], dataLength[1] + 1)
                    if not len(actualRsp[3:]) in dataRangeLength:
                        Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                        failure_cause = 'Data Length is {0} out of range {1}'.format(len(actualRsp[3:]), dataLength)
                        return False, failure_cause
            if data:
                start_byte = 3 if actualRsp[0] in ['0x62', '0x6e'] else (4 if actualRsp[0] in ['0x71'] else 2)
                if not data == actualRsp[start_byte:] and not unexpected_response:
                    Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[start_byte:]))
                    failure_cause = 'Data is {0}, while expected is {1}'.format(
                        tools.readable_hex(actualRsp[start_byte:]), tools.readable_hex(data)
                    )
                    return False, failure_cause
                if data == actualRsp[start_byte:] and unexpected_response:
                    Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[start_byte:]))
                    failure_cause = 'Data {0}, should be different to {1} received.'.format(
                        tools.readable_hex(actualRsp[start_byte:]), tools.readable_hex(data)
                    )
                    return False, failure_cause

            if partialData:
                fullRsp = tools.readable_hex(actualRsp)
                start_byte = 3 if actualRsp[0] in ['0x62', '0x6e', '0x6f'] else (4 if actualRsp[0] in ['0x71'] else 2)
                if isinstance(partialData, str):
                    if not partialData in fullRsp and not unexpected_response:
                        Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[start_byte:]))
                        failure_cause = 'partialData {0} is not in {1}'.format(partialData, fullRsp)
                        return False, failure_cause

                    if partialData in fullRsp and unexpected_response:
                        Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[start_byte:]))
                        failure_cause = 'partialData {0} should not be in {1}'.format(partialData, fullRsp)
                        return False, failure_cause

                if isinstance(partialData, (tuple, list)) and unexpected_response:
                    for i, unexpected_byte in enumerate(partialData):
                        if unexpected_byte in fullRsp:
                            if fullRsp.count(unexpected_byte) == len(actualRsp[
                                                                     start_byte:]):  # Evaluates if the unexpected byte is equal to number of times which is unexpected for example, a '00 bytes' found 31 times
                                Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[start_byte:]))
                                failure_cause = 'partialData {0} bytes of {1} value should not be in {2}'.format(
                                    str(len(actualRsp[start_byte:])), partialData[i], fullRsp)
                                return False, failure_cause

            if expected_byte:

                if byte_index == None:
                    raise ValueError('ERROR: You must specify a byte_index !!')

                if isinstance(expected_byte, str) and isinstance(byte_index, int):  # Verify Single Byte

                    actual_byte_index_value = actualRsp[byte_index].replace('0x',
                                                                            '').upper()  # Variable containing the actual byte value to be validated
                    interval = expected_byte.split('-')

                    if len(interval) == 2:  # Range Comparison (Min, Max)
                        if int(interval[0], 16) >= int(interval[1], 16):
                            Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                            failure_cause = 'Error in the Range defined by User. Min: {0} must be less than Max: {1}'.format(
                                interval[0], interval[1])
                            return False, failure_cause


                        elif not int(interval[0], 16) <= int(actual_byte_index_value, 16) <= int(interval[1],
                                                                                                 16):  # Verify the expected byte is inside a range
                            Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                            failure_cause = 'Expecting byte {0} at position {1} is outside of range (Min: {2}, Max {3})'.format(
                                expected_byte, byte_index, interval[0], interval[2])
                            return False, failure_cause

                    elif len(interval) == 1:  # Single Value Comparison

                        if expected_byte != actual_byte_index_value:  # Comparing the expected byte with the actual
                            Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                            failure_cause = 'Expecting byte {0} at position {1} -- Actual byte is: {2}'.format(
                                expected_byte, byte_index, actual_byte_index_value)
                            return False, failure_cause

                    else:  # Invalid Format

                        Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                        failure_cause = 'Invalid format for "expected_byte" parameter it can be a single string or a pair Max-Min'
                        return False, failure_cause

                if isinstance(expected_byte, (tuple, list)) and isinstance(byte_index, (
                tuple, list)):  # Verify Multiple bytes at different positions

                    if len(expected_byte) != len(byte_index):
                        raise ValueError('ERROR: expected_byte and byte_index number of elements must be the same !')

                    for i, value in enumerate(byte_index):

                        interval = expected_byte[i].split('-')

                        if len(interval) == 2:  # Range Comparison (Min, Max)

                            if int(interval[0], 16) >= int(interval[1], 16):
                                Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                                failure_cause = 'Error in the Range defined by User. Min: {0} must be less than Max: {1}'.format(
                                    interval[0], interval[1])
                                return False, failure_cause


                            elif not int(interval[0], 16) <= int(actualRsp[value].replace('0x', ''), 16) <= int(
                                    interval[1], 16):  # Verify the expected byte is inside a range

                                Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                                failure_cause = 'Response byte {0} at position {1} is outside of range (Min: {2}, Max {3})'.format(
                                    actualRsp[value].replace('0x', ''), byte_index[i], interval[0], interval[1])
                                return False, failure_cause

                        elif len(interval) == 1:  # Single Value Comparison

                            if expected_byte[i] != actualRsp[value].replace('0x',
                                                                            '').upper():  # Comparing the expected byte with the actual
                                Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                                failure_cause = 'Expecting byte {0} at position {1} -- Actual byte is: {2}'.format(
                                    expected_byte[i], value, actualRsp[value].replace('0x', ''))
                                return False, failure_cause

                        else:  # Invalid Format

                            Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                            failure_cause = 'Invalid format for "expected_byte" parameter it can be a single string or a pair Max-Min'
                            return False, failure_cause

            if data_dtc:
                # data_dtc[0] = initial_dtcs / initial_dtcs + protected_message_dtcs
                # data_dtc[1] = current _dtcs
                    if len(data_dtc[0]) != len(data_dtc[1]):
                        Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                        failure_cause = 'Number of Initial DTC\'s [{0}] - values {1}, Number of Current DTC\'s [{2}] - values {3}, the Numbers of DTC\'s are different'.format(
                            len(data_dtc[0]), data_dtc[0], len(data_dtc[1]), data_dtc[1])
                        return False, failure_cause

                    if len(data_dtc[0]) == len(data_dtc[1]):
                        for dtc in data_dtc[0]:
                            if not (dtc in data_dtc[1]):
                                failure_cause = 'Initial DTC\'s {0} and Current DTC\'s {1} are not equal in the content'.format(
                                    data_dtc[0], data_dtc[1])
                                return False, failure_cause

            if periodic_data:
                failure_cause = ''
                
            # Here we have max 2 items per test 1 for the timing pattern and another for number of active streams
                for result in periodic_data:
                
                    if result['is_error'] == True:
                        failure_cause = failure_cause + result['description'] + '. '
                
                # XOR logic to define pass fail criteria based on Timing Pattern and Active Streams
                if len(failure_cause) > 0:
                    Logger.write_debug_log('FAIL', __name__, '{}'.format(failure_cause))
                    return False, failure_cause

            # return True, None
            
            if NRC78_data:
                failure_cause = ''
                
            # Here we have max 2 items per test 1 for the timing pattern and another for number of active streams
                for result in NRC78_data:
                
                    if result['is_error'] == True:
                        failure_cause = failure_cause + result['description'] + '. '
                
                # XOR logic to define pass fail criteria based on Timing Pattern and Active Streams
                if len(failure_cause) > 0:
                    Logger.write_debug_log('FAIL', __name__, '{}'.format(failure_cause))
                    return False, failure_cause

            return True, None


        elif expected_response == 'Negative':

            if 'No response received' in actualRsp:
                return False, actualRsp

            if not actualRsp[0] == '0x7f' and not unexpected_response:
                return False, 'Negative {} response is expected. Actual response: {}'.format(
                    data[0], tools.readable_hex(actualRsp)
                )

            NRC = actualRsp[2]
            Logger.write_debug_log('DEBUG', __name__, 'NRC Specified: {0}'.format(NRC))

            if actualRsp[0] == '0x7f' and unexpected_response:
                if data[0] == NRC:
                    failure_cause = 'NRC {0}:{1} when expecting a different one than {0}.'.format(
                        NRC, dictNRC[NRC])
                    return False, failure_cause
            if data and not data_2:
                if not data[0] == NRC:
                    failure_cause = 'NRC {0}:{1} when expecting {2}'.format(
                        NRC, dictNRC[NRC], data[0]
                    )
                    return False, failure_cause
            # Potentially can be changed data_2 for a tuple / list in data to check multiple responses
            # New addition Jan/11/2020:
            elif data and data_2:
                if not data[0] == NRC and not data_2[
                                                  0] == NRC:  # This means that if data and data_2 are not equal to the actual NRC, test fails
                    failure_cause = 'NRC {0}:{1} when expecting {2} or {3}'.format(
                        NRC, dictNRC[NRC], data[0], data_2[0]
                    )
                    return False, failure_cause

            elif partialData:
                fullRsp = tools.readable_hex(actualRsp)
                if not partialData in fullRsp:
                    Logger.write_debug_log('FAIL', __name__, '{}'.format(actualRsp[3:]))
                    failure_cause = 'partialData {0} is not in {1}'.format(partialData, fullRsp)
                    return False, failure_cause
            # Till here ..
            else:
                print(__name__, 'Mandatory NRC code as argument')
                Logger.write_debug_log('ERROR', __name__, 'Mandatory NRC code as argument')
                return False, 'Mandatory NRC code as argument'
            return True, None


        elif expected_response == 'No response':
            if 'No response received' in actualRsp:
                return True, None
            else:
                return False, 'No response is expected, but received %s instead.' % tools.readable_hex(actualRsp)
    except Exception as error:
        print(__name__, type(error).__name__, type(error).__doc__, error)
