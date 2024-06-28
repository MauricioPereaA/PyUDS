'''
Created on 12/12/2018

    * Based on Bootstrap v4.0.0 - Cascade Style Sheet *

@author: Evan Tirado

'''
import re, os

class HTMLreport:

    def __init__(self, filepath, *args, **kwargs):

        self.report_path = filepath
        self.full_report_path = os.path.join(self.report_path, 'report.html')

        self.bootstrap_path = 'https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css'

        self.html_header = '<link href="{}" rel="stylesheet">\n'.format(self.bootstrap_path)+\
        '<!-- PyUDS - Test Report -->\n'

        self.table_header = '  <table class="table">\n'+\
        '    <thead class="thead-dark">\n'+\
        '      <tr>\n'+\
        '        <th scope="col">Timestamp</th>\n'+\
        '        <th scope="col">Test case</th>\n'+\
        '        <th scope="col">Step</th>\n'+\
        '        <th scope="col">Status</th>\n'+\
        '        <th scope="col">Comments</th>\n'+\
        '      </tr>\n'+\
        '    </thead>\n'+\
        '    <tbody>\n'

        self.table_footer = '    </tbody>\n'+\
        '  </table>'

        self.row = '	  <tr>\n'+\
        '	    <td>#TS#</td>\n'+\
        '	    <td>#TC#</td>\n'+\
        '	    <td>#STEP#</td>\n'+\
        '	    <th scope="row"><button type="button" class="btn #BTN#">#STATUS#</button></th>\n'+\
		'	    <td>#COMMENTS#</td>\n'+\
        '	  </tr>\n'

        self.btn_status = {
            'PASSED':'btn-success', 'FAILED': 'btn-danger', 'Not Applicable':'btn-warning', 'INFO': 'btn-info'
        }

    def generate_row(self, timestamp, testcase, step, status, comments=''):
        try:
            if status not in self.btn_status:
                raise RuntimeError('Status reported is not supported by PyUDS HTML report generator!')
            rep = {
                '#TS#'       :   timestamp,
                '#TC#'       :   testcase,
                '#STEP#'     :   step,
                '#COMMENTS#' :   comments,
                '#BTN#'      :   self.btn_status[status],
                '#STATUS#'   :   status
            }
            rep = dict((re.escape(k), v) for k, v in rep.items())
            pattern = re.compile("|".join(rep.keys()))
            row = pattern.sub(lambda m: rep[re.escape(m.group(0))], self.row)
            return row

        except Exception as error:
            print(__name__, type(error).__doc__, error)

    def HTMLbegin(self):
        with open(self.full_report_path, 'w') as html:
            html.write(
                self.html_header + self.table_header
            )
        return True

    def write_on_report(self, row):
        with open(self.full_report_path, 'a+') as html:
            html.write(
                row
            )

    def HTMLend(self, verbose=False):
        with open(self.full_report_path, 'a+') as html:
            html.write(
                self.table_footer
            )
        if verbose: print('Finished report successfully!')

if __name__ == '__main__':

    reportHTML = HTMLreport(os.getcwd())
    reportHTML.HTMLbegin()
    reportHTML.write_on_report(reportHTML.generate_row(
        timestamp='2018-12-04__16-01-38', 
        testcase='RID_03BC', 
        step='Transition to Extended Diagnostic Session Application Mode ', 
        status='PASSED', comments=''
    ))
    reportHTML.write_on_report(reportHTML.generate_row(
        '2018-12-04__16-01-38', 
        'RID_03BC', 
        'Start Routine Ethernet Cable Diagnostic Test', 
        'FAILED', 
        'NRC 0x31 when expecting Positive response'
    ))
    reportHTML.write_on_report(reportHTML.generate_row(
        '2018-12-04__16-01-38', 
        'RID_03BC', 
        'Start Routine Ethernet Cable Diagnostic Test', 
        'INFO', 
        'NRC 0x31 when expecting Positive response' 
    ))
    reportHTML.HTMLend()

