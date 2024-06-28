#===============================================================================
# Python Standard import packages
#===============================================================================
import configparser
import argparse
import unittest
import importlib
import os
import sys

#===============================================================================
# Python Library Dependencies
#===============================================================================
from pkg_resources import require
require("pywin32>=223")
require("pycryptodome>=3.7.2")

import __global__
from __version__ import __version__

loader = unittest.TestLoader()
tsuite = unittest.TestSuite()
parser = argparse.ArgumentParser(description='PyUDS Framework v%s - Test Automation Tool'%__version__)

class PyUDS:
    def __init__(self):
        parser.add_argument(
            '-r', '--run', type=str, metavar='TEST_SUITE(s)',
            help='Test suite name(s) to run. Separated by comma -> , <-'
        )
        parser.add_argument(
            '-t', '--testcase', type=str, metavar='TEST_CASE(s)',
            help='Specific test case name(s) to run. Separated by comma -> , <-'
        )
        parser.add_argument(
            '-e', '--ecu', type=str, default='config.cfg',
            help='Specific ECU under test (default: the one specified in config.cfg)'
        )

        _default_cg = tuple(__global__.__supported_cgs__.keys())[0]
        parser.add_argument(
            '-c', '--cg', type=str, default=_default_cg,
            help='Specific CG (default: will be %s)'%_default_cg
        )

        _default_binary = tuple(__global__.__default_binaries__.keys())
        parser.add_argument(
            '-b', '--binApp', type=str, default=_default_binary[0],
            help='Specific binary (default: will be application)'
        )
        parser.add_argument(
            '-bc1', '--binCal1', type=str, default=_default_binary[1],
            help='Specific binary (default: will be calibration number 1)'
        )
        parser.add_argument(
            '-bc2', '--binCal2', type=str, default=_default_binary[2],
            help='Specific binary (default: will be calibration number 2)'
        )
        parser.add_argument(
            '-bc3', '--binCal3', type=str, default=_default_binary[3],
            help='Specific binary (default: will be calibration number 3)'
        )
        # Test from here
        parser.add_argument(
            '-l', '--lg', type=str, default=__global__.__logs__,
            help='Specific log location (default: will be workspace\\logs )'
        )
        # to here

        #group = parser.add_mutually_exclusive_group()
        parser.add_argument('-a', '--all', action='store_true', help='Run all test cases')
        parser.add_argument('-z', '--debug', action='store_true', help='Enable debug mode')
        parser.add_argument('-u', '--unnatended', action='store_true', help='Unnatended mode')
        parser.add_argument('-n', '--no_excel_prompt', action='store_true', help='Disable Excel prompts')
        parser.add_argument('-d', '--no_real_time_report', action='store_true', help='Disable real-time reporting')
        parser.add_argument('-x', '--no_exclutions', action='store_true', help='Disable exclutions')

        self._args = parser.parse_args()
        self._cfg = configparser.ConfigParser()
        self.test_cases_path = os.getcwd() + '\\Testcases'
        self.__exclutions__(not self._args.no_exclutions) 

        if self._args.debug:
            breakpoint()

        if self._args.run:
            self.run_test_suites = self.__format_arg__(self._args.run)

        if self._args.testcase:
            if not hasattr(self, 'run_test_suites'):
                raise RuntimeError('--run/-r argument is required.')
            self.run_test_case = self.__format_arg__(self._args.testcase)

        #if self._args.cg.upper() in __global__.__supported_cgs__.keys():
            #__global__._running_cg = self._args.cg.upper()

        # Global Variables changed via GUI
        __global__.__config__ = __global__.__supported_ecus__.get(self._args.ecu, 'config.cfg')
        __global__._no_excel_prompt = bool(self._args.no_excel_prompt)
        __global__._supress_prompts = bool(self._args.unnatended)
        __global__._real_time_report = not bool(self._args.no_real_time_report)
        __global__._running_cg = self._args.cg 
        __global__._binary_app = self._args.binApp
        __global__._binary_cal1 = self._args.binCal1
        __global__._binary_cal2 = self._args.binCal2
        __global__._binary_cal3 = self._args.binCal3
        __global__.__logs__     = self._args.lg

    def begin(self):
        if self._args.run[0:6] in self._args.cg or self._args.run == '__Examples__' or self._args.run  == 'DPS':
            try:
                if not self._args.all:

                    if not self._args.run and not self._args.testcase:
                        parser.print_help()
                        
                        print('\n\n  - Available test suites: \n\n {}'.format(
                            '\n '.join(self.get_test_suites())))
                                
                    else:
                        found_test_suites = [
                            ts for ts in self.get_test_suites() for rts in self.run_test_suites if rts in ts
                        ]

                        if not len(found_test_suites)>0:
                            raise Warning(
                                'There were no test suites found with: {!r}'.format(self.run_test_case)
                            )
                        
                        self.__run__(
                            found_test_suites
                        )
                else:
                    print('Running all test cases...')
                    self.__run__(
                        self.get_test_suites()
                    )

            except Exception as exp:
                print(type(exp).__name__, exp)
        else:
            print('The selected test does not correspond to the CG Report Folder !')

    def __run__(self, test_suites):
        # Import Test Suites & Test cases
        for ts in test_suites:
            test_suite_path = self.test_cases_path + '\\' + ts
            test_modules = filter(
                lambda x: '.py' in x, 
                next(i[2] for i in os.walk(test_suite_path))
            )
            sys.path.insert( 0, test_suite_path )
            
            self._cfg.read(test_suite_path + '\\config.ini')
            excluded = self._cfg.get('EXCLUDED', 'test_cases').split('\n')

            if self._args.testcase:
                test_modules = [
                    tm for tm in test_modules for rtc in self.run_test_case if rtc in tm
                ]

            for module in test_modules:
                if module not in excluded:
                    path = test_suite_path + '\\' + module
                    name = module.replace('.py', '')
                    
                    tsuite.addTest(
                        loader.loadTestsFromModule(
                            importlib.import_module(name, path)
                        )
                    )
                else:
                    name = module.replace('.py', '')
                    print(name + ' excluded.')

        # Start PyUnit
        unittest.TextTestRunner().run(
            tsuite
        )
    
    def get_test_suites(self):
        try:
            return filter(
                lambda x: not '__pycache__' in x,
                next(i[1] for i in os.walk(self.test_cases_path))
            )
        except Exception as exp:
            print(type(exp).__name__, exp)
            return None

    def __exclutions__(self, *args):
        if True in args:
            test_suites = filter(
                lambda x: not '__pycache__' in x,
                next(i[1] for i in os.walk(self.test_cases_path))
            )
            for suite in test_suites:
                path = self.test_cases_path + '\\' + suite
                if not 'config.ini' in next(i[2] for i in os.walk(path)):
                    print('config.ini not found in', suite)
                    self.__ini_file__(
                        suite_path=path
                    )

    def __ini_file__(self, **kwargs):
        if 'suite_path' in kwargs:
            ini_file = kwargs['suite_path'] + '\\config.ini'
            test_cases = filter(
                lambda x: '.py' in x,
                next(i[2] for i in os.walk(kwargs['suite_path']))
            )

            with open(ini_file, 'w+') as ini:
                ini.write('[EXCLUDED]\ntest_cases=\n')
                for tc in test_cases:
                    ini.write(' #' + tc + '\n')

    def __format_arg__(self, string):
        return string.replace(' ', '').split(',')

if __name__ == '__main__':

    pyuds = PyUDS()
    pyuds.begin()

