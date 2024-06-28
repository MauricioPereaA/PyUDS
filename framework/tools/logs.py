'''
Created on 08/08/2018

@author: Evan Tirado

'''
from __global__ import __workspace__, __logs__
from framework.tools.report.htmlReport import HTMLreport
from framework.tools.report.jsonReport import jsonReport
import misc as tools
import os, shutil

class Logger(HTMLreport, jsonReport):
    
    def __init__(self, *args, **kwargs):

        ''' ENVIROMENT FOLDERS '''

        self.WORKSPACE_PATH = os.path.join(
            os.environ['userprofile'],
            'Workspace'
        )

        self.LOGS_PATH = __logs__
        self.HTML_PATH = __logs__

        tools.isFolder(self.WORKSPACE_PATH)
        tools.isFolder(self.LOGS_PATH)
        tools.isFolder(self.HTML_PATH)
        ''' LOG FIELD LENGTHS '''

        self.module_name_length = 20
        self.test_status_length = 8
        self.debug_level_length = 8

        HTMLreport.__init__(self, filepath=self.HTML_PATH)
        jsonReport.__init__(self, filepath=self.LOGS_PATH)
        
    def write_tester_report(self, module_name, status, message_log, comments=''):
        _report_path = os.path.join(
            self.LOGS_PATH,
            'test_report.log'
        )
        if comments != '':
            comments = comments.replace('\n', '<br>') # \n -> to HTML

        try:
            reportLog = open(_report_path, 'a+')
            self.write_on_report(
                self.generate_row(
                    tools.timeStamp(), module_name, message_log, status, comments
                )
            )
            reportLog.write(
                '{0} {1} {2} {3} \n'.format(
                    tools.timeStamp(),
                    module_name.ljust(self.module_name_length, ' '),
                    status.ljust(self.test_status_length, ' '),
                    message_log
                )
            )
        except Exception as error:
            print(__name__, module_name, error)
            reportLog.close()
        reportLog.close()
    
    def write_debug_log(self, debug_level, module_name, debug_message):
        _debug_log_path = os.path.join(
            self.LOGS_PATH,
            'debug.log'
        )
        try:
            debug_log = open(_debug_log_path, 'a+')

            debug_log.writelines(
                '{0} {1} {2} {3} \n'.format(
                    tools.timeStamp(),
                    debug_level.ljust(self.debug_level_length, ' '), 
                    module_name.ljust(self.module_name_length, ' '),
                    debug_message
                )
            )
            
        except Exception as error:
            print(__name__, error)
            debug_log.close()
        debug_log.close()

    def rename_log(self, test_case):
        try:
            shutil.copy(
                self.LOGS_PATH + '\\TraceLog.asc',
                self.LOGS_PATH + '\\' + test_case + '.asc'
            )
            os.remove(self.LOGS_PATH + '\\TraceLog.asc')
        except OSError:
            print(__name__, 'TraceLog.asc is already in use. If required make sure to delete it from Logs folder.')

    def end_logs(self, test_case, tester_report_active=False):
        log_type = ('test_report.log', 'debug.log', test_case + '.asc', 'report.html', 'results.json', test_case + '_writewindow.txt')
        logs_folder = os.path.join(
            self.LOGS_PATH, '{0}_{1}'.format(
            test_case, tools.timeStamp())
        )
        tools.isFolder(logs_folder)
        self.HTMLend()
        
        ''' Ending JSON Report file '''
        self.append_info(
            test_case,
            log_path=os.path.join(logs_folder, test_case+'.asc')
        )

        self.writeJSON()

        for log in log_type:
            if not tester_report_active:
                if log in 'test_report.log': continue
            try:
                shutil.copy(
                    os.path.join( self.LOGS_PATH, log ),
                    os.path.join( self.LOGS_PATH, logs_folder, log )
                )
                os.remove( os.path.join(self.LOGS_PATH, log) )                
            except Exception as error:
                print(__name__, error)

    def beginHTML(self):
        return self.HTMLbegin()

    def clear_logs(self, test_case):
        logs = ('test_report.log', 'debug.log', test_case + '_writewindow.txt')

        for log in logs:
            log_files = ( next(i for i in os.walk(self.LOGS_PATH))[2] )
            if log in log_files:
                print('Deleting %s from logs...'%log)
                os.remove(
                    os.path.join(self.LOGS_PATH, log)
                )
