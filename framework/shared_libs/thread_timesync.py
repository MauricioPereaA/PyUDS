from subprocess import Popen, CREATE_NEW_CONSOLE
import threading
import logging
import time
import os

class cmd_Thread(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        Popen(self.cmd, creationflags=CREATE_NEW_CONSOLE)

if __name__ == '__main__':
    try:
        cmd = cmd_Thread('py timesync.py -d 1000 -i 1000 -m CGM_CAN1_PDU06')
        cmd.start()
        for i in range(10):
            print('Running script')
            time.sleep(1)
        cmd.join()
    except KeyboardInterrupt:
        print(__name__, 'Terminated due to -KeyboardInterrupt-',)
