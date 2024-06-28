"""@jsonHandler.py
*********************************************************************************
@Description
PyUDS - JSON Implementation

       - Class:	JSON to CG Report
       	   - test_rows.json -> for each test suite (containing test_num, tests_row, log_row, sw_version_row, cg)
       	   - JSONreport already formatted. Translate params to specifically
*********************************************************************************
"""
from glob import glob
import json
import sys
import os

class jsonHandler:

    def __init__(self, logs_path):
        self.logs_path = logs_path

    def json_reports(self):
        try:
            _found_json_on_main_path = [ _file for _file in os.listdir(self.logs_path)
                                                            if _file.endswith('.json') ]

            if any(_found_json_on_main_path):
                for f in _found_json_on_main_path:
                    with open(os.path.join(self.logs_path, f)) as json_file:
                            yield json.load(json_file)

            for root, _, files in os.walk(self.logs_path):
                for f in files: # Recursive search
                    if f.endswith('.json'):
                        with open(os.path.join(root, f)) as json_file:
                            yield json.load(json_file)
        except Exception as error:
            print(__name__, type(error).__name__, error,                                       
                        'Line %s' % (sys.exc_info()[2].tb_lineno))
    
    def filter_results(self, *args, **kwargs):
        try:
            if not len(kwargs)>0:
                raise ValueError('Please provide filter arguments. Ex. test_status=\'PASSED\'')
            # Search in json reports
            reports = '' if not 'reports' in kwargs else kwargs['reports']
            reports_to_search = reports if not isinstance(reports, str) else self.json_reports()
            for report in reports_to_search:
                # Find test_case key
                for test_case in report:
                    if isinstance(report[test_case], dict):
                        # Now into test_case dictionary
                        for step in report[test_case]:
                            # Find specified 'kwargs' params
                            #   Example: test_result='PASSED'
                            #   - This one will find all PASSED test cases 
                            for k, v in kwargs.items():
                                if not k in report[test_case][step]: continue
                                if report[test_case][step][k] == v:
                                    yield (
                                        test_case, 
                                        step,
                                        report[test_case][step][k],
                                        report[test_case][step]['title'],
                                        report[test_case][step]['comments'],
                                        report[test_case][step]['timestamp'],
                                        *['{}::{}'.format(
                                            a, report[test_case][step][a]
                                        ) for a in args]
                                    )
        except Exception as error:
            print(__name__, type(error).__name__, error,                                       
                        'Line %s' % (sys.exc_info()[2].tb_lineno))
            return False

    def filter_tests_suites(self, *suites):
        try:
            if not len(suites)>0:
                raise ValueError('Please provide suites to filter Ex. \'CG3531_COMMON_DIDs\'')
            
            for report in self.json_reports():
                # Find key(s)
                for v in report.values():
                    if v in suites:
                        # yield report dictionaries
                        yield report
        except Exception as error:
            print(__name__, type(error).__name__, error,                                       
                        'Line %s' % (sys.exc_info()[2].tb_lineno))
            
if __name__ == '__main__':
    jsonReports = jsonHandler(logs_path=r'C:\Users\manuel.medina\Workspace\Logs\Results_8-Jul_PTM')
    for i,j in enumerate(jsonReports.filter_results(
        'timestamp', 'comments', 'request', # Parameter to be added
        test_status='FAILED')):
        print('#', i, j)

