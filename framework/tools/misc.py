'''@misc.py
*******************************************************************************

@par DESCRIPTION:

    Miscelanious functions lib to be used accross the whole framework

@ - Evan Tirado -
Created on 08/08/2018
Modified by Mauricio Perea
Date:13 July 2020
This script was added the FileExist Function for validate the path

Developed by Mauricio Perea
[function calculate_size_binary]
It permits to calculate the size of the binary file in hexadecimal format
October 15 2020

*******************************************************************************
'''

from tkinter import messagebox, Tk, Toplevel

_supress_prompts = None
if not __name__ == '__main__':
    from __global__ import _supress_prompts

import sys
import datetime
import time
import json
import os
import select
import threading
import msvcrt
import subprocess

def isFolder(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        return True
    except Exception as error:
        print(__name__, error)
        return False
        
def FileExists(path):
    try:
        if os.path.isfile(path):
            return True
    except Exception as error:
            print(__name__, error)
            return False

def timeStamp(format='default'):
    tsFormat = {
        'default' : '%Y-%m-%d__%H-%M-%S',
        'dateOnly': '%Y-%m-%d',
        'timeOnly': '%H-%M-%S.%f'
    }
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime(tsFormat[format]).__str__()

def readJSON(jsonPath):
    try:
        with open(jsonPath) as f:
            data = json.load(f)
        
        return data
    except Exception as error:
        print(__name__, type(error).__name__, error.__doc__, error)
        raise RuntimeError('Not able to read JSON file: {}'.format(jsonPath))
        
def readFileLine(filePath):
    with open(filePath) as file:  
        data = file.read().split('\n')
    return data

def split_every_two(data):
    try:
        data = data.replace(' ', '') # Values should NOT have spaces
        
        if not len(data)%2==0:
            raise RuntimeError('-> data <- byte values are not correct.')

        return [
            '0x{0}{1}'.format(data[i-1], x) for i, x in enumerate(data) if (i+1)%2==0
        ]
    
    except Exception as error:
        print(__name__, error)
        raise RuntimeWarning(__name__ + 'Not able to split data')

def hex_op(*strings):
    """
        Returns hex (string formatted) operation
            -- Initial hex strings  ->  '27', '40', ...
            -- Returned string      ->  '67'  
    """
    if not len(strings) > 1:
        raise RuntimeError('Function requires 2 arguments or more.')
    result = 0
    for data in strings:
        result += int(data, 16)

    return hex(result).replace('0x', '')

def readable_hex(hex_list):
    """
        Returns readable formatted hex 'string' type
            -- Initial hex_list    -> ['0xFF', '0xFF', '0xFF', ... ]
            -- Returned string     -> 'FF FF FF ...'
    """
    if not (isinstance(hex_list, list) or isinstance(hex_list, str)):
        raise ValueError('Expecting a -List- type argument, but provided %s instead.'%type(hex_list))
    
    if 'No response' in hex_list:
        return 'No response'

    return ' '.join(
        [ i.replace('0x', '') for i in hex_list ]
    ).upper()

def device_under_test(supported_ecus, ecu_node):
    for ecu in supported_ecus:
        if ecu in ecu_node: return ecu
    return None

def process_running(process='notepad.exe'):
    for task in (line.split() for line in subprocess.check_output("tasklist").splitlines()[3:]):
        if process.lower() == task[0].decode('utf-8').lower(): return True
    return False


def calculate_size_binary(path):
    """
    Function that calculate the size of binary file in string format
    Input Type: String
    path is absolute, contains the file.bin
    Output Type: String contains 8 values in hexadecimal value from 0 to F
    hexadecimal value in string format
    Example:path='AC.bin'
    data_value=calculate_size_binary(path)
    After Execution
    data_value='FF FF FF FF'
    If the path is not validate function return NoneType Class
    """
    SIZE_OF_CHARACTERS = 10  # Number of total characters including prefix 0x

    try:
        os.path.isfile(path)
        sizeable = os.stat(path).st_size
        print(f"Size File:{sizeable}bytes")
        hex_value = "{0:#0{1}x}".format(sizeable, SIZE_OF_CHARACTERS)
        data_hex_value = ' '.join([hex_value.replace('0x', '')])
        data_hex_value_with_spaces = ' '.join(data_hex_value[i:i+2] for i in range(0, len(data_hex_value), 2))

        print(f"Hex Value:{hex_value}")
        print(f"Data Hex Value:{data_hex_value_with_spaces}")
        return data_hex_value_with_spaces
    except OSError as err:
        print("OS error: {0}".format(err))



class timer:
    """
    @ Class Description
    - timer.input works exactly like input Python built-in
          function, but if a timeout is reached, it takes default
          parameter
    @ Usage:
    - timer.input(
            str PROMPT, int SECONDS, bool DEFAULT_VAL
        )
    """
    ceil = lambda num: round(num)+bool(num%2>1)
    @classmethod
    def input(cls, prompt, timeout=10, default=False):
        print(__name__, prompt)
        for i in reversed(range(1,cls.ceil(timeout)+1)):
            print(i, end=' ', flush=True)
            time.sleep(1)
            if msvcrt.kbhit():
                msvcrt.getch()
                print('\n')
                return True
        print('\n')
        return default

class test_rows:
    """
    @ Class Description
    - 'generate_json' method creates a json based on Test Modules provided in path
    in order to let the user fill it with its corresponding row in CG Report
    """

    @classmethod
    def python_files(cls, test_suite_path):
        for root, _, files in os.walk(test_suite_path):
            for f in files:
                if f.endswith('.py'):
                    with open(os.path.join(root, f)) as module:
                        yield {
                        'file_name': f,
                        'full_path': os.path.join(root, f),
                        'content'  : module.readlines()
                        }
            break

    @classmethod
    def generate_json(cls, *, test_suite_path):
        step_format = lambda step: 'test_{}'.format(str(step).rjust(3, '0'))
        output_file = {}
        for module in cls.python_files(test_suite_path):
            step_count = 0
            for line in module['content']:
                if 'def test_' in line: 
                    step_count+=1
            output_file.update(dict({
                    module['file_name'].replace('.py', ''):dict({
                        "log" : 0,
                        "sw_version" : 0,
                        **dict({
                            step_format(key):value for key, value in zip(range(1, step_count+1), [0]*step_count)
                        })
                    })
                }))
        with open(os.path.join(test_suite_path, 'test_rows.json'), 'a+') as f:
            f.write(json.dumps(output_file, indent=4))            
        print(__name__, 'Empty test_rows.json generated for', test_suite_path)

class popup:
    _prefix = 'PyUDS - '
    _awaiting_message = '\n * awaiting response from prompt window * \n'
    root = Tk(screenName=_prefix + 'Popup handler')

    @classmethod
    def set_window_config(cls, **options):
        if 'title' in options:
            cls.root.title(options['title'])
        if 'resizable' in options:
            _op = {True: options['resizable'], False: (0,0)}
            cls.root.resizable(
                *_op.get(bool(options['resizable']), (0,0)))
            if not bool(options['resizable']):
                cls.root.geometry('0x0')
        cls.root.withdraw()
        cls.root.iconify()
        
    @classmethod
    def error(cls, title, description, timeout=None, **kwargs):
        if timeout != None: timer.input('Wait for %s'%timeout, timeout=int(timeout))
        if _supress_prompts: return True
        _error = 'ERROR - '
        cls.set_window_config(title=title, resizable=False)
        print(cls._awaiting_message)
        prompt = messagebox.showerror(title=cls._prefix + _error + title,
                                        message=description)
        cls.root.withdraw()
        return prompt
                         
    @classmethod
    def warning(cls, title, description, timeout=None, **kwargs):
        if timeout != None: timer.input('Wait for %s'%timeout, timeout=int(timeout))
        if _supress_prompts: return True
        _warning = 'WARNING - '
        cls.set_window_config(title=title, resizable=False)
        print(cls._awaiting_message)
        prompt = messagebox.showwarning(title=cls._prefix + _warning + title,
                                        message=description)
        cls.root.withdraw()                                       
        return prompt
    
    @classmethod
    def info(cls, title, description, timeout=None, **kwargs):
        if timeout != None: timer.input('Wait for %s'%timeout, timeout=int(timeout))
        if _supress_prompts: return True
        _info = 'INFO - '
        cls.set_window_config(title=title, resizable=False)
        print(cls._awaiting_message)
        prompt = messagebox.showinfo(title=cls._prefix + _info + title,
                                        message=description, icon='info')
        cls.root.withdraw()                            
        return prompt
        
    @classmethod
    def ask(cls, title, description, timeout=None, **kwargs):
        if timeout != None: timer.input('Wait for %s'%timeout, timeout=int(timeout))
        if _supress_prompts: return True
        _options = {'yes' : True, 'no': False}
        cls.set_window_config(title=title, resizable=False)
        print(cls._awaiting_message)
        prompt = messagebox.askquestion(cls._prefix + title,
                                description, icon='warning')
        cls.root.withdraw()                       
        return _options[prompt]

if __name__ == '__main__':
    _popup = ('warning', 'error', 'info', 'ask')
    for p_type in _popup:
        getattr(popup, p_type)(
            title='Test Window',
            description='PyUDS %s | Pop-ups feature '%p_type.upper()
        )