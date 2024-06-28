from win32com.client import makepy
import subprocess
import os

class CANoe_genpy:
    
    _path = os.environ.get('CANOE_INSTALLDIR', None)
    _64bits = True if '64' in _path else False

    @classmethod
    def run(cls):
        if cls._64bits:
            COMdev_path = cls._path.replace('64', '32') + '\\COMdev\\CANoe.tlb'
        else:
            COMdev_path = cls._path + '\\COMdev\\CANoe.tlb'

        makepy.GenerateFromTypeLibSpec(
            COMdev_path, 
            None, 
            verboseLevel=0, 
            bForDemand=0, 
            bBuildHidden=1
        )
if __name__ == "__main__":
    CANoe_genpy.run()
