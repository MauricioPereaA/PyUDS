'''
@par DESCRIPTION:

    binary file handler lib, to be used to analyze binaries files intended for tests on CG3687

'''
import binascii
import math
from framework.tools.logs import Logger


Logger = Logger()
class Binary:

    '''
    This method (binary_packet_percentage) is not used in the tests of CG3687 ..
    '''

    @classmethod
    def binary_packet_percentage(cls, filename, percentage):
        with open(filename,'rb') as f:
            bin_length = len(str(binascii.hexlify(f.read())))
        iterations = (percentage * .01 * bin_length) / 0xA00    # 0xA00 represents the maximum number of bytes to send for each request of $36
        return iterations

    @classmethod
    def packets_to_send(cls, filename, bloc = '01', percentage = 100):
        transfer_packet_size  = 0xA00
        transfer_packet_size += transfer_packet_size
        
        with open(filename,'rb') as f:  # rb -> read binary file mode
            bin_content = str(binascii.hexlify(f.read()))
            bin_length  = len(bin_content)
            bin_content = bin_content[2:bin_length-1]
        read_length = 0

        if percentage < 100:            # This means that a specific % of the binary data has been specified
            bin_length = math.ceil(bin_length * percentage * 0.01)

        try:
            while( read_length < bin_length ):
                if (read_length + transfer_packet_size <= bin_length):
                    if bloc == '100':
                        bloc = '00'
                    packet_to_transfer = '36' + bloc + str(bin_content[read_length:(read_length+transfer_packet_size)])
                    read_length = read_length + transfer_packet_size
                    bloc = '{:02x}'.format(int(bloc, 16) + 1)
                else:
                    if bloc == '100':
                        bloc = '00'
                    packet_to_transfer = '36' + bloc + bin_content[read_length:(read_length + int(bin_length-read_length+1))]
                    read_length += bin_length - read_length + 1
                    bloc = '{:02x}'.format(int(bloc, 16) + 1)
                yield packet_to_transfer

        #'''
        #            - NOT IMPLEMENTED - 
        #        Method to be used to modify binary files to make invalid parameters
        #'''

        #def binary_modified(filename):
        #    pass


        except Exception as error:
            Logger.write_debug_log(
                'CRITICAL', __name__, 'Binary Packet Error')
            print(__name__, 'Something went wrong when attempting to send the binary packet data ..')

