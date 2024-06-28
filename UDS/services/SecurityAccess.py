from UDS.security.CMAC_AES import Generate_Security_Key

class SecurityAccess:
    def __new__(self, function, *args, **kwargs):
        if not hasattr(self, function):
            raise AttributeError('function %s not supported.'%function)
        req = getattr(self, function)
        return req(*args)

    CMAC_AES = Generate_Security_Key()

    security_level = {
            '01':('01', '02'),
            '03':('03', '04'),
            '05':('05', '06'),
            '09':('09', '0A'),
            '0B':('0B', '0C'),
            '0D':('0D', '0E'),
            '11':('11', '12'),
            '13':('13', '14'),
            '15':('15', '16')
        }
    seed = ''  
    @classmethod
    def request_seed(cls, level):
        if not level in cls.security_level.keys():
            raise ValueError('Level %s not supported'%level)
            
        request = '27 {}'.format(
            cls.security_level[level][0]
        )
        return request

    @classmethod
    def send_key(cls, level, seed='00'*32, encrypt_key=''):
        if not level in cls.security_level.keys():
            raise ValueError('Level %s not supported'%level)
        # If a seed contains FFs, then the provided one is previous used (TestClass module). 
        # Refer CG3531 - Tab RID 021E for more information.
        if encrypt_key != '': 
            security_key = cls.CMAC_AES.get_security_key( seed, encrypt_key )
        else:
            security_key = cls.CMAC_AES.get_security_key( seed )

        request = '27 {0}{1}'.format(
            cls.security_level[level][1], security_key
        )
        
        return request
