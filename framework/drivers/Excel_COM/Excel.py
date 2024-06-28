"""@Excel.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    Use of Excel application as a COM server.
    

@note ABBREVIATIONS:
        - COM: Component Object Model
Modified by Mauricio Perea
Date:13 July 2020
This script was modified for not kill excel process because it caused that excel files are lost

*******************************************************************************
"""

from __global__ import __supported_cgs__, _no_excel_prompt
from framework.shared_functions import tools
from framework.tools.logs import Logger
import win32com.client
import misc as tools
import os
import shutil
import psutil
import subprocess

Logger = Logger()
class ExcelTool(object):
    def __init__(self, TemplateFullPath, ReportPath=None):
        # Check if CG mentioned is supported
        self.CGReport = [CG for CG in __supported_cgs__.keys() if CG in TemplateFullPath]
        if not any( self.CGReport ):
            raise RuntimeError('{0} is not supported. \
                PyUDS only supports {1}.'.format(TemplateFullPath, ', '.join(__supported_cgs__.keys())))
        
        # Search for existing CG in path mentioned
        _cg_path = '\\'.join(TemplateFullPath.split('\\')[:-1])
        _cg_filename = TemplateFullPath.split('\\')[-1]
        if not _cg_filename in os.listdir(_cg_path):
            raise RuntimeError(
                _cg_filename + ' not found. Make sure path %s is correct'%_cg_path)

        if ReportPath is None:
            ReportPath = '\\'.join(TemplateFullPath.split('\\')[:-1])

        tools.isFolder(ReportPath)
        self.ReportFullPath = os.path.join(
            ReportPath, self.CGReport[0] + '_Report' + '.xlsx'
        )
        
        print("++++++++ pyUDS Excel Cleanup Procedure +++++++++\n")

        try:
            #AYanez: Kill Excel foreground and background processes in case these are running
            
            # Scan all Excel Foreground Instances
            for task in (line.split() for line in subprocess.check_output("tasklist").splitlines()[3:]):
            
                if "excel" in task[0].decode('utf-8').lower():
                
                    # Save and close the opened documents
                    Excelapp= win32com.client.GetActiveObject('Excel.Application')
                    for wb in Excelapp.Application.Workbooks:
                        #print(wb.Name)
                        wb.Save()
                        Excelapp.Application.Quit()
            
            my_pid = os.getpid()

            # Scan all Excel Background Instances
            for proc in psutil.process_iter():
            
                try:
                    # Get process name & pid from process object.
                    processName = proc.name()
                    processID = proc.pid
                    
                    #print(processName)

                    if proc.pid == my_pid:
                        # Skip process belongs to itself
                        continue

                    if processName.lower().startswith("excel"):
                        print(f"pyUDS removed {processName}[{processID}] : {''.join(proc.cmdline())})")
                        proc.kill()
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                    print(e)
                    
        except Exception as error:
            Logger.write_debug_log('ERROR', __name__, 'Failed attempt to close Excel process!')
            print(__name__, error)
            
        #breakpoint()

        # Creates a new Excel file (Copy from Template) if it does not exist
        if not os.path.isfile(self.ReportFullPath):
            Logger.write_debug_log('DEBUG', __name__, 'CREATING NEW WORKBOOK!')

            self.create_new_workbook(TemplateFullPath)

        try:
            Logger.write_debug_log('DEBUG', __name__, 'Initializing Excel COM...')

            self.Excel = win32com.client.Dispatch('Excel.Application')      # COM object
            Logger.write_debug_log('DEBUG', __name__, 'Opening Existing Workbook: ' + self.ReportFullPath)
            self.CGReport_Workbook = self.Excel.Workbooks.Open(self.ReportFullPath, UpdateLinks = 0)

        except Exception as error:
            Logger.write_debug_log('ERROR', __name__, 'Not able to initialize Excel COM: {}'.format(error))
            print(__name__, 'Not able to initialize Excel COM. :(')
            print(__name__, error)
                
    def write_test_result(self, SheetName, ResultRow, ResultColumn, result):
        try:
            if self.CGReport[0] == 'CG4577':
                TestResult = {
                    True  : 'Tested and passed',
                    False : 'Tested but failed'
                } 
            else:
                TestResult = {
                    True  : 'Tested and Passed',
                    False : 'Tested and Failed'
                }
            Logger.write_debug_log(
                'DEBUG', __name__, 
                'Writing test result... {}'.format(
                    TestResult[result]
                )
            )
            if self.read_cell_value(SheetName, ResultRow, ResultColumn) != TestResult[False]:
                self.write_cell(
                    SheetName, ResultRow, ResultColumn, TestResult[result]
                )
            
        except Exception as Error:
            Logger.write_debug_log('ERROR', __name__, Error)
            print(__name__, Error)
    
    def write_cell(self, SheetName, Row, Column, Value):

        try:
            Logger.write_debug_log('DEBUG', __name__, 'Attempting to write on cell {0}::{1}: {2}'.format(Row, Column, Value))
            if not Row>0:
                raise ValueError('Row must be higher than 0') 
            self.CGReport_Workbook.Worksheets(SheetName).Cells(Row,Column).Value = Value
               
        except Exception as Error:
            print(__name__, 'Not able to Write on cell')
            Logger.write_debug_log('ERROR', __name__, 'Not able to Write on cell {0}{1}: {2}'.format(Row, Column, Error))
            print(__name__, Error)
    
    def read_cell_value(self, SheetName, Row, Column):
        try:
            if not Row>0:
                raise ValueError('Row must be higher than 0') 
            Logger.write_debug_log('DEBUG', __name__, 'Attempting to read cell value {0}{1}'.format(Row, Column))
            cellVal = self.CGReport_Workbook.Worksheets(SheetName).Cells(Row,Column).Value
            Logger.write_debug_log('DEBUG', __name__, 
                    '{} :: Current value: {}'.format('read_cell_value()', cellVal))
            return cellVal
               
        except Exception as Error:
            print(__name__, 'Not able to read cell value.')
            Logger.write_debug_log('ERROR', __name__, 'Not able to read cell {0}{1}: {2}'.format(Row, Column, Error))
            print(__name__, Error)

    def insert_log_file(self, row=None, column='G', log_path=None, sheetname=None): 
        try:
            Logger.write_debug_log('DEBUG', __name__, 'Attempting to insert: ' + log_path)

            if not row > 0:
                raise ValueError('Row must be higher than 0')
            _worksheet = self.CGReport_Workbook.Worksheets(sheetname)

            # -- Positioning for log attach --3
            for _ in range(5):
                if self.set_current_position(row, column, sheetname):
                    break

            _dest_cell = _worksheet.Range(str(column) + str(row))
            _obj = _worksheet.OLEObjects()

            _obj.Add(
                ClassType=None, 
                Filename=log_path, 
                Link=False, 
                DisplayAsIcon=True,
                Left=_dest_cell.Left, 
                Top=_dest_cell.Top, 
                Width=30,
                Height=25
            )
        except Exception as Error:
            Logger.write_debug_log('ERROR', __name__, Error)
            print(__name__, 'Not able to insert Object' + log_path)
            print(__name__, Error)

    def set_current_position(self, row, column, sheetname):
        try:
            _col = ord(column.lower())-96 if isinstance(column, str) else column
            _cell = self.read_cell_value(sheetname, row, _col)

            if _cell != None: # Clear non-empty cell 
                self.write_cell(sheetname, row, column, '')

            self.CGReport_Workbook.Worksheets(sheetname).Activate()
            self.CGReport_Workbook.Worksheets(
                sheetname).Range(str(column) + str(row)).Select()

            if _cell != None: # Fill back cell
                self.write_cell(sheetname, row, column, _cell)
            
            return True
        except Exception as select_range_error:
            Logger.write_debug_log('ERROR', __name__, 
                '{}'.format((
                    'Col:' +str(column) + ' Row:' + str(row),
                    type(select_range_error).__name__,
                    type(select_range_error).__doc__,
                    type(select_range_error).__class__,
                    select_range_error)))
            return False

    def write_sw_version(self, Row=None, Column=6, SheetName=None, info=None): # For CG3388 it is 6 and for CG3531 is 5
        try:
            Logger.write_debug_log('DEBUG', __name__, 'Attempting to write SW Version')
            self.write_cell(
                SheetName, Row, Column, 
                'Tested with cadence {0}: \n {1}'.format(
                    info['cadence'], 
                    info['sw_version']
                    )
                )
        except Exception as error:
            Logger.write_debug_log('ERROR', __name__, error)
            print(__name__, error)

    def save_report(self):
        try:
            if not os.path.isfile(self.ReportFullPath):
                self.CGReport_Workbook.SaveAs(self.ReportFullPath)
                Logger.write_debug_log('DEBUG', __name__, 'Successfully saved new workbook!')
            else:
                Logger.write_debug_log('DEBUG', __name__, 'Attempting to save workbook!')
                
                self.CGReport_Workbook.Save()
                self.Excel.Application.Quit()

                if tools.process_running('excel.exe'):
                    os.system('taskkill /F /IM excel.exe>>excel_taskkill.log')
                Logger.write_debug_log('DEBUG', __name__, 'Successfully saved workbook!')
            
            
        except Exception as Error:
            Logger.write_debug_log('ERROR', __name__, Error)
            print(__name__, 'Not able to save Workbook: ')
            print(__name__, Error)
   
    def create_new_workbook(self, TemplateFullPath):
        try:
            shutil.copy(
                TemplateFullPath, self.ReportFullPath
            )
            Logger.write_debug_log('DEBUG', __name__, 'Successfully created ' + self.ReportFullPath)

        except Exception as error:
            print(__name__, 'Not able to create Workbook :(', TemplateFullPath)
            Logger.write_debug_log('ERROR', __name__, 'Not able to create Workbook {}'.format(error))
            print(__name__, error)
    