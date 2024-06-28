from tkinter.filedialog import askdirectory
from tkinter import Tk

if __name__ == '__main__':
    import htmlReport
    import jsonHandler
else:
    import framework.tools.report.htmlReport as htmlReport
    import framework.tools.report.jsonHandler as jsonHandler

''' PARAMETERS LIST '''
_TIMESTAMP   = 'timestamp'
_TITLE       = 'title'
_REQUEST     = 'request'
_RESPONSE    = 'response'
_EXPECTED    = 'expected_response'
_DATA        = 'data'
_DATA_LENGTH = 'dataLength'
_STATUS      = 'test_status'
_COMMENTS    = 'comments'

_FAILED      = 'FAILED'
_PASSED      = 'PASSED'  

class ResultAnalyzer(htmlReport.HTMLreport, jsonHandler.jsonHandler):

    def __init__(self, path=None, test_status=_FAILED, *params):
        if test_status not in (_FAILED, _PASSED):
            raise ValueError('Status must be either {} or {}'.format(_FAILED, _PASSED))
        self.looking_for = test_status

        if path is None:
            root = Tk()
            root.withdraw()
            path = askdirectory( initialdir=r'C:\Users\evan.tirado\Workspace\Logs',
                                 title = "Choose a folder." )
        self.path = path
        jsonHandler.jsonHandler.__init__(self, logs_path=self.path)

        self.params = params if any(params) else (
                                _REQUEST, _RESPONSE, _EXPECTED)
    
    def get_results(self, *params):
        _params = params if any(params) else self.params
        for result in self.filter_results(*_params, test_status=self.looking_for):
            yield result
    
    def create_html_report(self, output_path=None):
        _path = self.path if output_path is None else output_path
        htmlReport.HTMLreport.__init__(self, filepath=_path)
        self.HTMLbegin()
        
        for row in self.get_results():
            extra_params = list()
            (   _testcase, _step_num, 
                _test_status, _step_title,
                _failure, _execution_time ) = row[:6]
            if len(row)>6: extra_params = row[6:]
            _step_title = _step_title.replace('<', '-').replace('>', '-') 
            print(row)
            self.write_on_report(self.generate_row(
                timestamp=_execution_time, 
                testcase=_testcase,
                step=_step_num + ' :: ' + _step_title, 
                status=_test_status, comments='{}<br>\n{}'.format(
                    _failure, '<br>\n'.join(extra_params))
            ))

        self.HTMLend()

if __name__ == '__main__':
    result_analysis = ResultAnalyzer(None, _FAILED, _COMMENTS, _DATA, _DATA_LENGTH, _REQUEST)
    result_analysis.create_html_report()