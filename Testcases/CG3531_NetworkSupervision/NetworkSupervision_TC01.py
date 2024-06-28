
            # This is and autogenerated test case using PyUDS Test Builder v0.1 #
        
from framework.shared_functions import device_under_test, tools, pn_dict
from Testcases.TestClass import TestCase
from inspect import stack as info
import unittest, time, os

test = TestCase()
class PyUDS_TestCase(unittest.TestCase):

    #== CG3531 - Network Supervision ==#
    @classmethod
    def setUpClass(self):
        #== Initialize test case ==#
        test.begin(
            test_info=info(),
            writeTestResults=True,
            excel_tab='Network Supervision'
        )

        ''' Device Under Test - Settings '''
        self.DUT = device_under_test
        # Keys from Dictionary file -> 'protected_messages' correspond to already implemented CAPL
        self.partial_networks = pn_dict[self.DUT]

        self.test_step_counter=2

    @classmethod
    def tearDownClass(self):
        #== End Test Case ==#
        test.end()

    def current_step(self):
        return str(self.test_step_counter).rjust(3,'0')

    def count_step(self):
        self.test_step_counter+=1
    
    def test_001(self, name='PN + Lost Comm'):
        for msg in self.partial_networks['protected_messages'].keys():
            print(__name__, 'Testing: %s'%msg)
            for PN in self.partial_networks['protected_messages'][msg]['PartialNetwork']:
                print(__name__, 'Under PN: %s'%PN)
                for p in self.partial_networks['supported_PNs']:
                    # Disable all PNs
                    print(__name__, dict({p:0}))
                    test.canoe.set_envVariable(**dict({p:0}))
                # Enable Tested PN
                print(__name__, dict({PN:1}))
                test.canoe.set_envVariable(**dict({PN:1}))
                lcTimer=self.partial_networks['protected_messages'][msg]['MatureTime']                
                msgSupTimeout=self.partial_networks['protected_messages'][msg]['SupervisionTimeout']
                print(str(msgSupTimeout))
                
                # Re-send configured PNs
                test.canoe.set_envVariable(envVNMFStop=1)
                test.canoe.set_envVariable(envVNMFSend=0)
                time.sleep(1)
                test.canoe.set_envVariable(envVNMFStop=0)
                test.canoe.set_envVariable(envVNMFSend=1)

                test.preconditions(
                    current_step='test_001_1',
#                    power_mode='RUN'
                )
                
                #Step 1-1
                time.sleep(5)
                test.step(
                    step_title='{0} :: Clear DTCs {1}:{2}'.format(self.DUT, PN, msg),
                    custom='14 FF FF FF',
                    expected={
                        'response': 'Positive'
                    }
                )

                test.preconditions(
                    current_step='test_001_2',
 #                   power_mode='RUN'
                )
                time.sleep(5)
                test.step(
                    step_title='{0} :: Read DTCs {1}:{2}'.format(self.DUT, PN, msg),
                    custom='19 02 09',
                    expected={
                        'response': 'Positive',
                        'data': 'FF'
                    }
                )
                
                self.count_step()
                #Step 1-2
                test.preconditions(
                    current_step='test_%s'%self.current_step()
                )
                
                #Stop Sending Current Supervised Message:
                test.canoe.set_envVariable(**dict({msg:1}))
                
                #Step 1-3 Read DTC multiple times before signal supervision time out expires
                periodDTCReads = int(msgSupTimeout/3)
                #Read DTCs every msgTimeout/3 for MsgTimeout
                test.canoe.set_envVariable(envReadingPeriod=periodDTCReads)
                time.sleep(0.1)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
                time.sleep(msgSupTimeout/1000)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')

                #Step 1-4 Read DTCs beyond LC_Timer expires, this is understood as DTC Mature Time
                periodDTCReads=int(lcTimer/5)
                test.canoe.set_envVariable(envReadingPeriod=periodDTCReads)
                time.sleep(0.1)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','1')
                time.sleep(lcTimer/1000+3)
                test.canoe.set_system_variable('Generic_Functional','TriggerDTCRead','0')
                
                #Enable Sending Current Supervised Message:
                test.canoe.set_envVariable(**dict({msg:0}))
                
                prompt = tools.popup.ask(title=name, description='Verify that the Lost Comm DTC sets after Signal Supervision Timeout + LC_Timer time have all expired')
                test.compare(True, prompt, step='test_002_2')