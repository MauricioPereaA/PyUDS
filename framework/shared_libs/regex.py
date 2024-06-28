import re

class Regex(object):
    """
    RegEx: 
        - Find string match in TraceLog
    """
    def __init__(self, trace_log):
        self.trace_log = trace_log
    
    def find_line(self, pattern, start_flag="Passed: Test module 'TransportLayer' finished.",
                            end_flag="Test module 'TransportLayer' started.", multiple_matches=False, verbose=False):
        r""" find_line -method-
            @Description:
                - find pattern in TraceLog. 
                    Returns *timestamp* & *matched pattern*

            @Usage:
                >>obj = Regex(trace_log='C:\\TraceLog.asc')
                >>obj.find_line(pattern=r'\d+')
                    Will return first pattern match -> \d+ <-
                    & its corresponding timestamp as a tuple: (timestamp, match)
                >>(0.0, 1)
                
        """
        if multiple_matches:
            matches = []

        with open(self.trace_log, 'r') as trace:
            for num, line in enumerate(reversed(trace.readlines())):
                if start_flag in line:
                    if verbose: print('__started__')
                    end_timestamp = re.search(r'\d+\.[0-9]{6}', line).group(0)
                
                if end_flag in line:
                    if verbose: print('__finished__')
                    if not 'found_pattern' in locals():
                        return (False, 'No matches found')
                    elif multiple_matches:
                        return matches

                if 'end_timestamp' in locals():
                    if hasattr(re.search(pattern, line), 'group'):
                        found_pattern = re.search(pattern, line).group(0)
                        found_timestamp = re.search(r'\d+\.[0-9]{6}', line).group(0)
                        if verbose:
                            print('__found_line__')
                            print(found_timestamp, found_pattern)

                        if multiple_matches:
                            matches.append((found_timestamp, found_pattern))
                        else:
                            return (found_timestamp, found_pattern)
            if verbose: print('End of for loop')