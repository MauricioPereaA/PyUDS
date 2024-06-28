
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test, ARC_sys_vars, sleep_timeout, tools
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os, random

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=False,
            excel_tab='Network Supervision'
        )

        ''' Device Under Test - Settings '''
        self.sys_vars = tuple(ARC_sys_vars[device_under_test].keys())

        self.test_step_counter=23
        self.invalid_signal_DTCs = {
            "ARB":{
                "VehSpdAvgDrvn_Prtcd_MSG":{
                    "ID":"614","ARC":1,"PV":0,"CS":0,"RATE":100,
                    "DTC":{
                        "C4 01 00":{"x":8,"y":1000,"cal":0}
                    }
                },
                "TrnsEstGr_Prtcd_MSG":{
                    "ID":"50","ARC":1,"PV":0,"CS":0,"RATE":12.5,
                    "DTC":{
                        "C4 01 00":{"x":16,"y":720,"cal":0},
                        "C4 11 00":{"x":1,"y":1000,"cal":0},
                        "C4 02 00":{"x":1,"y":1000,"cal":1},
                    }
                },
                "SysPwrMode_Prtcd_MSG":{
                    "ID":"878","ARC":1,"PV":1,"CS":0,"RATE":250,
                    "DTC":{
                        "C4 22 00":{"x":8,"y":2500,"cal":0}
                    }
                },
                "BkupSysPwrMode_Prtctd_MSG":{
                    "ID":"880","ARC":1,"PV":1,"CS":0,"RATE":250,
                    "DTC":{
                        "C4 47 00":{"x":8,"y":2500,"cal":0}
                    }
                }
            }
        }
    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()
    
    def current_step(self):
        return 'test_' + str(self.test_step_counter).rjust(3,'0')

    def count_step(self):
        self.test_step_counter+=1

    def test_001_1(self, name='Start Test'):
        # Pre condition - Clear DTCs before starting the TC
        test.preconditions(
            current_step='Clear DTCs - Precondition',
            #power_mode='RUN',
            mec_zero=True
        )
        test.step(
            step_title='Read MEC',
            custom='22 F1 A0',
            expected={
                'response': 'Positive',
                'data': '00'
            }
        )
        time.sleep(5)

        for msg in self.invalid_signal_DTCs[device_under_test].keys():
            print(msg)
            if self.invalid_signal_DTCs[device_under_test][msg]['PV'] == 1:
                self.Msg_ID=self.invalid_signal_DTCs[device_under_test][msg]['ID']
                self.Msg_rate=self.invalid_signal_DTCs[device_under_test][msg]['RATE']
                self.Msg_DTC=list(self.invalid_signal_DTCs[device_under_test][msg]['DTC'].keys())[0]
                self.Msg_x=self.invalid_signal_DTCs[device_under_test][msg]['DTC'][self.Msg_DTC]['x']
                
                self.count_step()
                self.count_step()
                test.preconditions(
                    current_step=self.current_step() + '_2'
                )
                test.step(
                    step_title='{0} - {1}'.format('Clear DTCs - Precondition', device_under_test)+'::'+msg,
                    custom='14 FF FF FF',
                    expected={
                        'response': 'Positive'
                    }
                )
                test.preconditions(current_step=self.current_step() + '_3')
                test.step(
                    step_title='{0} - {1}'.format('Read DTCs - Not DTCs are set', device_under_test)+'::'+msg,
                    custom='19 02 09',
                    expected={
                        'response': 'Positive',
                        'data': 'FF'
                    }
                )
                                
                #Step 25 Start and continue requesting DTCs, at the recorded periodic rate, for the recorded received message that contains PV Signal
                test.canoe.set_envVariable(envReadingPeriod=self.Msg_rate)
                time.sleep(0.1)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
                
                #Step 26 Start and continue transmitting the recorded received message with an invalid PV value
                test.canoe.set_envVariable(Env_MsgID = self.Msg_ID)
                test.canoe.set_system_variable('SysVarSecMsg','SysInValidDataCount','1')
                test.canoe.set_system_variable('SysVarSecMsg','SysInvalidPV','1')
                test.canoe.set_envVariable(Env_MsgStartStop='INVALIDPV')
                time.sleep(6)
                
                #Stop requesting DTCs:
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')
                
                self.count_step()
                #Manually check in RBS trace if the DTC is not set before X count and sets after X count
                prompt = tools.popup.ask(title=name, description='Verify invalidSignal DTCs sets only after X instances for Y ms')
                test.compare(True, prompt, step=self.current_step()+' - Verify invalidSignal DTCs sets only after X instances for Y ms')     
                               
                #Start Reading DTCs again
                test.canoe.set_envVariable(envReadingPeriod=self.Msg_rate)
                time.sleep(0.1)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
                
                #Step 27 Once the InvalidSignalDataReceived DTC sets, start transmitting the supervised message with a valid PV value 
                test.canoe.set_envVariable(Env_MsgID = self.Msg_ID)
                test.canoe.set_system_variable('SysVarSecMsg','SysInValidDataCount','0')
                test.canoe.set_system_variable('SysVarSecMsg','SysInvalidPV','0')
                test.canoe.set_envVariable(Env_MsgStartStop='INVALIDPV')
                time.sleep(3)
                
                #Step 28 Stop requesting DTCs
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')
                
                self.count_step()
                #Manually check in RBS trace if the DTC testFailed bit goes to 0 after two instances of Valid PV
                prompt = tools.popup.ask(title=name, description='Verify invalidSignal DTCs status byte is 2E after two instances of Valid PV')
                test.compare(True, prompt, step=self.current_step()+' - Verify invalidSignal DTCs status byte is 2E after two instances of Valid PV')      

                self.count_step()
                self.count_step()                
                test.preconditions(
                    current_step=self.current_step()
                )
                
                #Step 29 Clear DTCs
                test.step(
                    step_title='{0} - {1}'.format('Clear DTCs - Precondition', device_under_test)+'::'+msg,
                    custom='14 FF FF FF',
                    expected={
                        'response': 'Positive'
                    }
                )
                
                #Step 30 Wait > 5 seconds
                self.count_step()
                time.sleep(5.1)
                
                #Step 31 Read DTCs
                self.count_step()
                test.preconditions(
                    current_step=self.current_step()
                )
                test.step( 
                    step_title='{0} - {1}'.format('Read DTC - DTC remains 2E', device_under_test)+'::'+msg,
                    custom='19 02 09',
                    expected={
                        'response':     'Positive',
                        'data':  'FF'
                    }
                )
                
                #Step 32 Transmit the received message with the following Invalid/Valid PV pattern:
                #less than X_Failure_Count Limit number of messages with invalid PV (Invalid):
                invalid_msgs_count=(int(self.Msg_x)-2) 
                invalid_msgs_count=(invalid_msgs_count-1)*2 #CAPL for Invalid Data Signals provided by GM seems to apply this formula for number of instances
                print(invalid_msgs_count)
                
                #followed by 2 times X_Failure_Count Limit number of messages with Valid PV (Valid) :               
                valid_msgs_count=(int(self.Msg_x)*2)
                valid_msgs_count=(valid_msgs_count+1)*2 #CAPL for Invalid Data Signals provided by GM seems to apply this formula for number of instances
                
                print(valid_msgs_count)
                print(hex(valid_msgs_count)) #Requires passing hex value
                
                #for a duration of at least 10 cycles of Invalid/Valid data:
                ms_data_cycles = 10*(invalid_msgs_count+valid_msgs_count)/2*self.Msg_rate
                print(ms_data_cycles)
                
                #If x (invalid msg count) < 1 then step 10 and 11 CAN NOT BE DONE
                if invalid_msgs_count >0:
                    test.canoe.set_envVariable(Env_MsgID = self.Msg_ID)
                    test.canoe.set_system_variable('SysVarSecMsg','SysInValidDataCount',hex(invalid_msgs_count))
                    test.canoe.set_system_variable('SysVarSecMsg','SysValidDataCount',hex(valid_msgs_count))
                    test.canoe.set_system_variable('SysVarSecMsg','SysInvalidPV','1')
                    test.canoe.set_envVariable(Env_MsgStartStop='INVALIDPV')
                    time.sleep(ms_data_cycles/1000)
                    test.canoe.set_system_variable('SysVarSecMsg','SysInValidDataCount','0')
                    test.canoe.set_system_variable('SysVarSecMsg','SysValidDataCount','0')
                    test.canoe.set_system_variable('SysVarSecMsg','SysInvalidPV','0')
                    test.canoe.set_envVariable(Env_MsgStartStop='INVALIDPV')

                    time.sleep(1)                    
                    #Manually check in RBS trace if the Messages valid/invalid cycles are correct
                    prompt = tools.popup.ask(title=name, description='Verify if the Messages invalid/valid cycles are correct')
                    
                    #Step 33 Check no DTCs set
                    self.count_step()
                    self.count_step()                    
                    test.preconditions(
                        current_step=self.current_step()
                    )
                    test.step(
                        step_title='{0} - {1}'.format('Read DTC - Must be clear after 10 cycles of "Invalid = less than x" and "Valid = x*2" PV Pattern', device_under_test)+'::'+msg,
                        custom='19 02 09',
                        expected={
                            'response': 'Positive',
                            'data': 'FF'
                        }
                    )
            self.test_step_counter = 23
