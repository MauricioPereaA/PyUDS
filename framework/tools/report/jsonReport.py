"""@jsonReport.py
*********************************************************************************
@Description
PyUDS - JSON Implementation
    -- Logger
       - SubClass: jsonReport
    	   - JSON Structure (Create a template)
    	   - JSON Manipulation (Read, append)
    	   - Params: 
                Request, response, expected_response, data, dataLength, 
                trace_log, timestamp, 
                test_suite, test_case, test_step_func, test_step_title, 
                test_status(PASSED/FAILED), sw_version

*********************************************************************************
"""
import json, os

class jsonReport:

    def __init__(self, filepath=os.getcwd(), **kwargs):
        self.path = filepath + '\\results.json'
        self.test_results = {}

        if not self.startJSON(**kwargs):
            raise RuntimeError('jsonReport - Not able to create JSON file: %s'%self.path)

    def __iter__(self):
        for key, data in self.test_results.items():
            yield key, data

    def startJSON(self, **kwargs):
        try:
            self.test_results.update(**kwargs)
            return True
        except Exception as error:
            print(__name__, type(error).__name__, error.__doc__, error)
            return False

    def append_info(self, test_suite, **kwargs):
        try:
            if len(kwargs)>0:
                self.test_results.update(**kwargs)
                return True
            print(__name__, 'No key=value provided.')
        except Exception as error:
            print(__name__, type(error).__name__, error.__doc__, error)
            return False

    def append_testcase_info(self, testcase, **kwargs):
        try:
            if len(kwargs)>0:
                if not testcase in self.test_results:
                    self.test_results.update({testcase:{}})

                self.test_results[testcase].update(**kwargs)
                return True
            print(__name__, 'No key=value provided.')
        except Exception as error:
            print(__name__, type(error).__name__, error.__doc__, error)
            return False
  
    def append_step_results(self, testcase, test_func, repeated=None, **kwargs):
        try:
            if len(kwargs)>0:
                while True:
                    if not testcase in self.test_results:
                        self.test_results.update({testcase:{}})
                    if not test_func in self.test_results[testcase]:
                        self.test_results[testcase].update({test_func:{}})
                        self.test_results[testcase][test_func].update(**kwargs)
                        break
                    else:
                        if repeated is None: # First sub-step
                            repeated = True
                            test_func = test_func + '__0'
                        else:
                            _test_func, _num = test_func.split('__')
                            test_func = _test_func + '__%s'%str(int(_num)+1)

                return True
            print(__name__, 'No key=value provided.')
        except Exception as error:
            print(__name__, type(error).__name__, error.__doc__, error)
            return False
  
    def writeJSON(self):
        formatted_dict = json.dumps(
            self.test_results, indent=4
        )
        with open(self.path, 'w') as json_file:
            json_file.write(
                formatted_dict
            )

if __name__ == '__main__':

    json_file = jsonReport(
        sw_version='141R4',
        test_suite='COMMON_DIDs',
    )

    examples = [
        dict(
            testcase='COMMON_DIDs_1_18',
            test_func='test_001',

            timestamp='2019-01-23__17-48-51',
            title='Read SUM SOH Port Interface Request Exceeded',
            request='22 F0 94',
            response='0x62 0xf0 0x94 0x00 0x01 0xf4 0x00',
            expectedRsp='Positive',
            data='None',
            dataLength='4',
            test_status='PASSED',
            comments=''
        ), dict(
            testcase='COMMON_DIDs_1_18',
            test_func='test_002',

            timestamp='2019-01-23__17-48-51',
            title='Read SUM SOH Port Interface Request Exceeded',
            request='22 F0 94',
            response='0x62 0xf0 0x94 0x00 0x01 0xf4 0x00',
            expectedRsp='Positive',
            data='None',
            dataLength='4',
            test_status='PASSED',
            comments=''
        ), dict(
            testcase='COMMON_DIDs_1_18',
            test_func='test_003',

            timestamp='2019-01-23__17-48-51',
            title='Read SUM SOH Port Interface Request Exceeded',
            request='22 F0 94',
            response='0x62 0xf0 0x94 0x00 0x01 0xf4 0x00',
            expectedRsp='Positive',
            data='None',
            dataLength='4',
            test_status='PASSED',
            comments=''
        ),
    ]
    for i in examples:
        json_file.append_step_results(**i)

    json_file.append_testcase_info(
        testcase='COMMON_DIDs_1_18',
        log_path=r'C:\Users\evan.tirado\Workspace\Logs\COMMON_DIDs_1_18_2019-01-23__17-48-58\COMMON_DIDs_1_18.asc'
    )

    json_file.writeJSON()