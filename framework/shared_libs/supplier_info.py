"""@supplier_info.py
*******************************************************************************
@copyright    Copyright 2018 . All rights reserved.
@attention    Confidential

@par DESCRIPTION:
    Intended to fill Supplier info for all CG3388 Tabs
*******************************************************************************
"""
from framework.drivers.Excel_COM.Excel import ExcelTool
from framework.config.read_config import read_cfg_file
from framework.shared_functions import tools

class SupplierInfo:
    def __init__(self, excel_obj, sheetname, info_column=4):
        """
        Initialization parameters 
        """
        self.excel = excel_obj
        self.sheetname = sheetname 
        self.info_column = info_column  # Column D = 5

        self.supplier_info = {          # [ row, value ]
            'ECU':                      [ 2, None],
            'Supplier':                 [ 3, None],
            'TestEngineer':             [ 4, None],
            'Phone':                    [ 5, None],
            'Email':                    [ 6, None],
            'HWIdentifier':             [ 8, None],
            'sw_version':               [ 9, None],
            'DiagnosticSpecification':  [10, None],
            'DataDictionaryVersion':    [11, None]
        }

    def get_supplier_info_from_cfg(self):
        '''
        Read config.cfg to get supplier information + 
            get timeStamp
        '''
        for field in self.supplier_info.keys():

        # Condition to take ECU from the canoe config instead of INFO
            if field == 'ECU':
                self.supplier_info[field][1] = read_cfg_file('CANOE', field, False)
            else:
                self.supplier_info[field][1] = read_cfg_file('INFO', field, False)

        self.supplier_info.update(
            dict(Date=[7, tools.timeStamp()]))
    
    def write_supplier_info(self, ecu=None, supplier=None, engineer=None,
                                    phone=None, email=None, hw_id=None, sw_id=None,
                                    data_specification=None, data_dictionary=None):
        """
        Write down supplier info
        """    
        if None in self.write_supplier_info.__defaults__:
            self.get_supplier_info_from_cfg()
        
        for data in self.supplier_info.values():
            self.excel.write_cell(self.sheetname,         # Sheetname
                                data[0],            # Row
                                self.info_column,   # Column
                                data[1])            # Value

