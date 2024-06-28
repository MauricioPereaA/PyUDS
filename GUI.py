"""
Modified by Mauricio Perea
Date: 03/09/2020
Modify def stop_test(self) method
Add the pop-up message for PYUDS Process & RBS Simulation
"""
from tkinter import *  
from tkinter.ttk import Label, Combobox, Button, Scrollbar, Notebook
from subprocess import Popen, CREATE_NEW_CONSOLE
from __version__ import __version__
#from __global__ import __config__, __reports__, __supported_ecus__, __supported_cgs__, \
#                        __logs__, _supress_prompts, _no_excel_prompt, _running_cg
from framework.tools.report.resultAnalyzer import ResultAnalyzer, _TIMESTAMP, _TITLE, _REQUEST, _RESPONSE, _EXPECTED, \
                                                    _DATA, _DATA_LENGTH, _STATUS, _COMMENTS, _FAILED, _PASSED

from functools import partial
import tkinter.filedialog
import webbrowser
import subprocess
import shutil
import time
import sys
import os
import __global__



'''
                - UNDER DEVELOPMENT -
log_write and log is the decorador used to log the methods in this module
'''

def log_write(*data):
    try:
        with open('gui.log', 'a+') as log:
            data = [str(i).ljust(42, ' ') for i in data]
            log.write(' '.join(data) + '\n')
    except Exception as error:
        print(*data)
        
def log(func, *args):
    def inner(*args, **kwargs):
        _func_name = func.__qualname__
        _args = tuple([i for i in args if type(i) in (str, int, float, bool)])
        log_write(_func_name,                    
                f' -- Begin --                            | {_args}')
        try:
            response = func(*args, **kwargs)
            log_write(_func_name,                    
                    f' -- Function executed successfully  --  | {response}')
        except:
            response = f'Error while executing {_func_name}'

        return response
    return inner

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        """Display text in tooltip window"""
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()



class GUI:
    def __init__(self):
        
        # ================================================
        #  - PyUDS GUI - Based on Tkiter lib
        # ================================================

        ''' PyUDS GUI - Window '''
        self.window = Tk()
        self.window.title('PyUDS v'+__version__)
        w, h = 500, 600
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x, y = (ws/2) - (w/2), (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ''' PyUDS GUI - LOGO '''
        path = os.path.join(os.getcwd(), 'framework', 'logo.png')
        logo = PhotoImage(file=path)
        background_label = Label(self.window, image=logo)
        background_label.pack(ipadx=10,pady=10)

        ''' PyUDS GUI - Tabs '''
        self.tabControl = Notebook(self.window)
        self.mainTab = Frame(self.tabControl)
        self.configTab = Frame(self.tabControl)
        self.reportsTab = Frame(self.tabControl)
        self.binariesTab = Frame(self.tabControl)
        self.tabControl.add(self.mainTab, text='Main')
        self.tabControl.add(self.configTab, text='Config')
        self.tabControl.add(self.reportsTab, text='Reports')
        self.tabControl.add(self.binariesTab, text='Binaries')
        self.tabControl.pack(expand=1, fill="both")

        ''' PyUDS GUI - Main - CGs checkboxes '''
        self.check_boxes = Frame(self.mainTab)
        self.cg_checkbox = dict()
        self.supported = dict()
        self.cgs_filter = list()
        lbl_filter_cg = Label(self.check_boxes, text='Filter by CG:')
        self.show_tooltip(lbl_filter_cg, 'Filter will be reflected in Test cases list below.')
        lbl_filter_cg.pack(side=LEFT)
        for cg in __global__.__supported_cgs__.keys():
            self.supported.update(dict({cg:BooleanVar()}))
            self.cg_checkbox.update(dict({cg:Checkbutton(self.check_boxes, text=cg,
                            variable=self.supported[cg], onvalue=True, offvalue=False,
                            command=self.checkbox_toggle).pack(side=LEFT)}))
        self.check_boxes.pack()

        ''' PyUDS GUI - Main - Test Suites :: ComboBox '''
        self.test_suites = Combobox(self.mainTab, width=35)
        self.test_suites['values'] = (self.get_test_suites())
        self.test_suites.bind("<<ComboboxSelected>>", self.update_test_cases)
        self.test_suites.current(len(self.test_suites['values'])-2) # __Examples__
        self.test_suites.pack(pady=5)

        ''' PyUDS GUI - Main - Run Selected Button / Stop current test'''
        buttons_frame = Frame(self.mainTab)
        run_btn = Button(buttons_frame, text="Run selected", command=self.run_selection)
        run_btn.pack(ipadx=10,pady=5, side=LEFT)
        stop_btn = Button(buttons_frame, text="Stop current test", command=self.stop_test)
        stop_btn.pack(ipadx=10,pady=5, side=RIGHT)
        buttons_frame.pack()

        ''' PyUDS GUI - Main - Create batch script '''
        buttons_frame_2 = Frame(self.mainTab)
        batch = Button(buttons_frame_2, text="Create QuickLaunch Batch", command=self.create_script)
        batch.pack(ipadx=10,pady=5)
        buttons_frame_2.pack()

        ''' PyUDS GUI - Main - Scrollbar '''
        scrollbar = Scrollbar(self.mainTab, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=Y)

        ''' PyUDS GUI - Main - Test cases :: ListBox '''
        self.listbox = Listbox(self.mainTab, selectmode=EXTENDED, width=30, height=50, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=BOTH, side=BOTTOM)
        scrollbar.config(command=self.listbox.yview)

        ''' PyUDS GUI - Config Tab - Options '''
        self.options = {'Unnatended mode'   :   '--unnatended',
                        'No Excel prompt'   :   '--no_excel_prompt',
                        'Disable real-time CG report' : '--no_real_time_report'}

        self.config_options_formatted = ''
        self.config_check_boxes = Frame(self.configTab)
        self.op_selection = dict()

        Label(self.config_check_boxes, text='Options:').pack(side=LEFT)
        for op in self.options.keys():
            self.op_selection.update(dict({op:BooleanVar()}))
            Checkbutton(self.config_check_boxes, text=op,
                variable=self.op_selection[op], onvalue=True, offvalue=False,
                command=self.update_options).pack(side=LEFT)
        self.config_check_boxes.pack()

        ''' PyUDS GUI - Config Tab - Select ECU '''
        select_cfg_lbl = Label(self.configTab, text="Select ECU:")
        select_cfg_lbl.pack(ipadx=10)
        selected_ecu_frame = Frame(self.configTab)
        self._ecu_config = os.path.join(os.path.dirname(os.path.abspath((__file__))),'framework','config', __global__.__config__)
        self.selected_ecu = Combobox(selected_ecu_frame, width=30)
        self.selected_ecu['values']=['default', *__global__.__supported_ecus__]
        update_default_btn = Button(selected_ecu_frame, text='Set as default cfg', command=self.set_default)
        update_default_btn.pack(padx=8, side=RIGHT)
        selected_ecu_frame.pack()
        
        self.selected_ecu.bind("<<ComboboxSelected>>", self.update_config_window)
        self.selected_ecu.current(0)
        self.selected_ecu.pack(ipadx=10)

        ''' PyUDS GUI - Config Tab - Config.cfg edit panel '''
        self.config_box = Text(self.configTab, width=60, height=20)
        scrollbarYConfigBox = Scrollbar(self.configTab, orient="vertical", command=self.config_box.yview)
        scrollbarXConfigBox = Scrollbar(self.configTab, orient="horizontal", command=self.config_box.xview)     
        scrollbarYConfigBox.pack(side=RIGHT, fill=Y)
        scrollbarXConfigBox.pack(side=BOTTOM, fill=X)
        self.config_box.pack(pady=10)
        self.config_box.config(yscrollcommand=scrollbarYConfigBox.set, xscrollcommand=scrollbarXConfigBox.set)

        cfg_btn = Button(self.configTab, text="Update config.cfg file", command=self.update_config_file)
        cfg_btn.pack(ipadx=10,pady=5)
    
        ''' PyUDS GUI - Reports Tab - CGs '''
        report_selection = LabelFrame(self.reportsTab,
                                        text='CG Report settings:',
                                        highlightbackground="grey",
                                        highlightcolor="grey",
                                        bd=2)

        self.radio_buttons_formatted = lambda: '--cg "{}"'.format( self.cg_entries_val.get(self.selected_cg_report.get()).get() )
        self.saved__supported_cgs__ = __global__.__supported_cgs__
        self.saved_running_cg = {'CG3388': 'CG3388Jun2018_Template.xlsx'}
        self.selected_cg_report = StringVar()
        self.selected_cg_report.set('CG3388')   # Sets the checkbox for the given cg string

        cg_frames = dict()
        cg_entries = dict()
        self.cg_entries_val = dict()
        browse_dir_btns = dict()

        for cg in __global__.__supported_cgs__.keys():
            cg_frames.update(dict({cg:Frame(report_selection)}))
            Radiobutton(cg_frames[cg], text=cg, variable=self.selected_cg_report,
                        command=self.radio_buttons_formatted, value=cg).pack(side=LEFT)
            self.cg_entries_val.update(dict(
                {cg:StringVar()}))
            cg_entries.update(dict(
                {cg:Entry(cg_frames[cg], textvariable=self.cg_entries_val[cg], width=45)} ))     
            self.cg_entries_val[cg].set(__global__.__supported_cgs__.get(cg))
            cg_entries[cg].pack(side=LEFT)
            browse_dir_btns.update(dict(
                {cg:Button(cg_frames[cg], text='...', width=3,
                            command=partial(self.browse_cg_file, cg)
                    ).pack(side=RIGHT, padx=3)} ))
            cg_frames[cg].pack(pady=5)

        report_selection.pack(pady=15)
        ''' PyUDS GUI - Reports Tab - JSON Result Analyzer '''
        result_analysis_frame = LabelFrame(self.reportsTab, 
                                        text='Overall results report',
                                        highlightbackground="grey", 
                                        highlightcolor="grey",
                                        bd=2)
        
         # Input - Entry & button
        input_settings_frame = Frame(result_analysis_frame)
        self.log_path_formatted = lambda: '--lg "{}"'.format(self.report_path_container.get())
        self.report_path_container = StringVar()
        self.report_path_container.set(__global__.__logs__)
        lbl_input = Label(input_settings_frame, text='Reports directory:')
        self.show_tooltip(lbl_input, 'Directory containing report folders to be analyzed')
        lbl_input.pack(side=LEFT)
        
        Entry(input_settings_frame, 
                textvariable=self.report_path_container, width=45).pack(side=LEFT)             
        Button(input_settings_frame, text='...', width=3, 
                command=partial(
                    self.browse_reports_folder, self.report_path_container,
                    'Select input folder to analyze Logs...',
                    )
                ).pack(side=RIGHT, padx=3)
        input_settings_frame.pack(pady=10)

        #result_analysis_frame.pack(pady=3)
        '''  HTML  '''
        # Output - Entry & button
        lbl_html = Label(result_analysis_frame, text="HTML filtered results output directory:").place(y = 45)
        output_settings_frame = Frame(result_analysis_frame)
        # test from here
        #self.log_dir_path_formatted = lambda: '--lgd "{}"'.format(self.output_report_path_container.get())
        # to here
        self.output_report_path_container = StringVar()
        self.output_report_path_container.set(__global__.__logs__)
        lbl_output = Label(output_settings_frame, text='Output directory:')
        self.show_tooltip(lbl_output, 'Generated HTML report is going to be saved to this directory')
        lbl_output.pack(side=LEFT)
        Entry(output_settings_frame,
                textvariable=self.output_report_path_container, width=45).pack(side=LEFT)
        Button(output_settings_frame, text='...', width=3,
                command=partial(
                    self.browse_reports_folder, 
                    self.output_report_path_container,
                    'Select output folder to save HTML report...'
                    )                                  
                ).pack(side=RIGHT, padx=3)
        output_settings_frame.pack(pady=23)
        
         # Parameters - check boxes
        result_parameters = (_REQUEST, _RESPONSE, _EXPECTED, _DATA, _DATA_LENGTH)
        #Label(result_analysis_frame, text='Parameters:').pack(side=TOP)
        Label(result_analysis_frame, text='Parameters:').place(x=180,y=95)
            #      Radio buttons
        radio_param_buttons_frame = Frame(result_analysis_frame)
        self.test_status_param = StringVar()
        self.test_status_param.set(_FAILED)

        Radiobutton(radio_param_buttons_frame, 
                        text=_PASSED, variable=self.test_status_param,
                        command=partial(self.test_status_param.set, _PASSED), 
                        value=_PASSED).pack(side=LEFT)

        Radiobutton(radio_param_buttons_frame, 
                        text=_FAILED, variable=self.test_status_param,
                        command=partial(self.test_status_param.set, _FAILED), 
                        value=_FAILED).pack(side=RIGHT)

        
        radio_param_buttons_frame.pack()

            #      Check-boxes
        check_boxes_parameters_selected = dict()
        self.html_parameters_params = lambda: (
            op for op in check_boxes_parameters_selected
                if check_boxes_parameters_selected[op].get() )

        results_filter_check_boxes = Frame(result_analysis_frame)

        check_boxes_sub_frames = list()
        check_boxes_sub_frames.append(Frame(results_filter_check_boxes))
        for count, op in enumerate(result_parameters):
            if count % 5 == 0:
                check_boxes_sub_frames.append(Frame(results_filter_check_boxes))
            _current_frame = check_boxes_sub_frames[-1]

            _formatted_text = list(op.replace('_', ' '))
            _formatted_text.pop(0) and _formatted_text.insert(0, op[0].upper())
            _formatted_text = ''.join(_formatted_text)

            check_boxes_parameters_selected.update(dict({op:BooleanVar()}))
            Checkbutton(_current_frame, text=_formatted_text,
                variable=check_boxes_parameters_selected[op], onvalue=True, offvalue=False
            ).pack(side=LEFT)
            _current_frame.pack()
        results_filter_check_boxes.pack()

         # Create HTML report
        Button(result_analysis_frame, text='Generate HTML report', command=self.create_html_report).pack(pady=10)
        result_analysis_frame.pack(pady=10)

        ''' PyUDS GUI - Binary files settings '''

        binary_selection = LabelFrame(self.binariesTab,
                                        text='Binary files settings:',
                                        highlightbackground="grey",
                                        highlightcolor="grey",
                                        bd=2)


        self.saved__supported_binaries__ = __global__.__default_binaries__
        self.saved_binary_file = {'Application':  'MSM-Onlyapplication'}
        self.App_command = lambda: '--binApp "{}"'.format(self.binary_entries_val.get(self.selected_binary_app_file.get()).get()) 
        self.Cal_1_command = lambda: '--binCal1 "{}"'.format(self.binary_entries_val.get(self.selected_binary_cal_1_file.get()).get()) 
        self.Cal_2_command = lambda: '--binCal2 "{}"'.format(self.binary_entries_val.get(self.selected_binary_cal_2_file.get()).get()) 
        self.Cal_3_command = lambda: '--binCal3 "{}"'.format(self.binary_entries_val.get(self.selected_binary_cal_3_file.get()).get()) 
        self.selected_binary_app_file = StringVar()
        self.selected_binary_cal_1_file = StringVar()
        self.selected_binary_cal_2_file = StringVar()
        self.selected_binary_cal_3_file = StringVar()
        self.selected_binary_app_file.set('Application') 
        self.selected_binary_cal_1_file.set('Calibration_1')
        self.selected_binary_cal_2_file.set('Calibration_2') 
        self.selected_binary_cal_3_file.set('Calibration_3') 

        binary_frames = dict()
        binary_entries = dict()
        self.binary_entries_val = dict()
        browse_dir_btns = dict()

        for binary in __global__.__default_binaries__.keys():
            binary_frames.update(dict({binary:Frame(binary_selection)}))
            #Radiobutton(binary_frames[binary], text=binary, variable=self.selected_binary_file,
            #            command=self.radio_buttons_formatted, value=binary).pack(side=LEFT)
            bin_input = Label(binary_frames[binary], text=binary+ ' ')
            self.show_tooltip(bin_input, 'Directory containing binary files')
            bin_input.pack(side=LEFT)
            self.binary_entries_val.update(dict(
                {binary:StringVar()}))
            binary_entries.update(dict(
                {binary:Entry(binary_frames[binary], textvariable=self.binary_entries_val[binary], width=45)} ))     
            self.binary_entries_val[binary].set(__global__.__default_binaries__.get(binary))
            binary_entries[binary].pack(side=LEFT)
            browse_dir_btns.update(dict(
                {binary:Button(binary_frames[binary], text='...', width=3,
                            command=partial(self.browse_binary_file, binary)
                    ).pack(side=RIGHT, padx=3)} ))
            binary_frames[binary].pack(pady=5)
        binary_selection.pack(pady=15)
        self.update_test_cases()
        self.update_config_window()
        '''
        Variables for gui logger (Not used)
        '''
        self.WORKSPACE_PATH = os.path.join(
            os.environ['userprofile'],
            'Workspace'
        )
        self.LOGS_PATH = os.path.join(
            self.WORKSPACE_PATH,
            'Logs'
        )
        self.window.mainloop()
        


    @log
    def get_test_suites(self):
        ''' 
        Return test suites found.
        '''
        test_suites = (
            next(i for _, i, _ in os.walk(os.getcwd()+'\\Testcases'))
        )
        if any(self.cgs_filter):
            return list(filter(
                lambda x: any([ True for cg in self.cgs_filter if cg in x ]), test_suites))               
                
        return test_suites

    @log
    def checkbox_toggle(self):
        ''' 
        Main tab :: Filters test cases by CGs according to checked checkboxes.
        '''
        self.cgs_filter = [cg for cg in __global__.__supported_cgs__.keys() if self.supported[cg].get()]
        self.test_suites['values']= (self.get_test_suites())
        self.test_suites.set(self.test_suites['values'][0])
        self.update_test_cases()

    @log
    def update_options(self, *args):
        '''
        Config Tab :: Options assembles --command according to checked options
        '''
        if any(self.op_selection):
            self.config_options_formatted = ' '.join(map(
                self.options.get, ( i for i in self.op_selection.keys() 
                                    if self.op_selection[i].get() )))
    @log
    def update_test_cases(self, *event):
        '''
        Main :: Inserts test cases found in test suite folders.
        '''
        self.listbox.delete(0, END)
        for _file in self.get_files():
            if '.py' in _file:
                self.listbox.insert(END, _file.replace('.py', ''))

    @log
    def get_files(self):
        ''' 
        Return test script files found
        '''
        return [
            i for _,_,i in os.walk(os.getcwd()+"\\Testcases\\"+self.test_suites.get())
        ][0]

    @log
    def update_config_window(self, *event):
        '''
        Config Tab :: Shows selected ECU config file in text panel. 
        '''
        self._ecu_config = os.path.join(os.path.dirname(
                                os.path.abspath((__file__))), 'framework', 'config',                                
                                __global__.__supported_ecus__.get(self.selected_ecu.get(),'config.cfg'))
                                    
        with open(self._ecu_config, 'r') as config_file:
            config_read = config_file.read()
            self.config_box.delete(1.0, END) 
            self.config_box.insert(END, config_read)
    @log
    def update_config_file(self): 
        '''
        Config Tab :: Saves modifications performed in config.cfg file. 
        '''
        with open(self._ecu_config, 'w') as config_file:
            config_file.write(self.config_box.get(1.0, END))

    @log
    def set_default(self):
        '''
        Config Tab :: Set selected ECU config as default config. 
        '''
        current_ecu = self.selected_ecu.get()
        if current_ecu != 'default':
            configs_path = os.getcwd() + '\\framework\\config\\'
            try:
                os.remove(configs_path + '\\config.cfg')
                shutil.copy(
                    src=configs_path + __global__.__supported_ecus__.get(current_ecu),
                    dst=configs_path + '\\config.cfg'
                )
                self.selected_ecu.set('default')
            except OSError:
                print('Please make sure -config.cfg- file is not already opened.')

            finally:
                print('SUCCESS!', current_ecu, 'has been set as default config.cfg.')

    @log
    def run_selection(self):
        '''
        Main Tab :: Launch PyUDS subprocess with selected parameters. 
        '''
        if len(self.listbox.curselection()) == 0:
            print('You have not selected any test case !\nPlease select a test case ()')
        else:
            try:
                test_suite = self.test_suites.get()
                #if test_suite in self.listbox.selection_get():
                #    print(' -- Please select test case (s) to run. -- ')
                test_cases = self.listbox.selection_get().split()
                self.pyuds_process = subprocess.Popen('py PyUDS.py -r {0} -t {1} -e {2} {3} {4} {5} {6} {7} {8} {9} '.format(
                    test_suite, ','.join(test_cases), self.selected_ecu.get(),
                    self.radio_buttons_formatted(), self.config_options_formatted,
                    self.App_command(), self.Cal_1_command(), self.Cal_2_command(), self.Cal_3_command(), self.log_path_formatted()
                ))
                # The command of logs is under test
                
            except KeyboardInterrupt:
                os.system('cls')
                print('WARNING - Previous test was interrupted!')
        
    @log
    def stop_test(self):
        '''
        Main Tab :: Kill PyUDS subprocess. 
        '''
        from framework.tools.misc import popup
        if hasattr(self, 'pyuds_process'):
            try:
                self.pyuds_process.kill()
                print('PyUDS Prcoess - Test stopped!')
                popup.info(title='Stop Test', description='Test Stopped\n Please [Stop] the RBS \n Simulation Manually')
            except Exception as error:
                print('PyUDS - Couldnt stop current running test!')
                print(type(error).__name__, type(error).__doc__, error)
        else:
            print('PyUDS - No test is being executed !!')

    def create_script(self, filename='PyUDS_QuickLaunch.bat'):
        '''
        Main Tab :: Create PyUDS runnable batch script with selected parameters. 
        '''
        try:
            test_suite = self.test_suites.get()
            if test_suite in self.listbox.selection_get():
                print(' -- Please select test case (s) to add to Batch. -- ')
            test_cases = self.listbox.selection_get().split()
            
            if not filename in os.listdir(os.getcwd()):
                _header = True

            with open(filename, 'a+') as script:
                if '_header' in locals(): script.write('@echo off\n')
                script.write('py PyUDS.py -r {0} -t {1} -e {2} {3} {4}\n'.format(
                    test_suite, ','.join(test_cases), self.selected_ecu.get(),
                    self.radio_buttons_formatted(), self.config_options_formatted
                )) 
                print('Added {} to batch script.'.format(test_cases))
        except Exception as error:
            print(type(error).__name__, type(error).__doc__, error)

    @log
    def browse_cg_file(self, cg, *args):
        '''
        Reports tab :: Browse for *.xlsx CG report template file. 
        '''
        browser_window = Tk()
        browser_window.withdraw()
        path = tkinter.filedialog.askopenfilename(
                initialdir = __global__.__reports__,
                title='Choose *.xlsx template file...').replace('/', '\\')
        if any(path): self.cg_entries_val[cg].set(path)
        return path          
        
    @log
    def browse_binary_file(self, binary, *args):

        browser_window = Tk()
        browser_window.withdraw()
        path = tkinter.filedialog.askopenfilename(
                initialdir = __global__.__binaries__,
                title='Choose *.bin binary file...').replace('/', '\\')

        if any(path): self.binary_entries_val[binary].set(path)
        return path 

    @log
    def browse_reports_folder(self, entry_obj, window_title):
        '''
        Reports tab :: Browse for folder to recursively search for JSON reports.
        '''
        browser_window = Tk()
        browser_window.withdraw()
        path = tkinter.filedialog.askdirectory(
                initialdir=__global__.__logs__,
                title=window_title).replace('/', '\\')
        if any(path): entry_obj.set(path)
        # Is this correct?
        return path

    @log
    def create_html_report(self):
        '''
        Reports tab :: Creates HTML report filtering PASSED/FAILED results from provided path.
        '''
        generate_html = ResultAnalyzer(
            self.report_path_container.get(),
            self.test_status_param.get(), *self.html_parameters_params())            
        generate_html.create_html_report(
            output_path=self.output_report_path_container.get())
        
        webbrowser.open('{}\\report.html'.format(
            self.output_report_path_container.get()))

    @log
    def show_tooltip(self, widget, text):
        '''
        Shows tooltip box on mouse over
        '''
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

launch = GUI()