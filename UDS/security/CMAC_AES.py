from Crypto.Cipher import AES
from Crypto.Hash import CMAC
import sys

class Generate_Security_Key:
    def __init__(self):
        self.ecu_key = '43414E4469566120554E4C4B204B4559'
        self.FFs = 'FF'*16
        self.FEs = 'FE'*16
        self.current_encrypt_key = ''
    
    def get_security_key(self, seed='1543414E4F452044495641204543554944FA91755AE9A91B830590C696114BEC', custom_encrypt_key=''):
        try:
            if custom_encrypt_key != self.current_encrypt_key or custom_encrypt_key == '':
                encrypt_ecu_key = self.cmac_encrypt( seed )
                bytes_to_encrypt = self.FFs
                self.current_encrypt_key = custom_encrypt_key

            else:
                if len(custom_encrypt_key)!=32:
                    raise ValueError(
                        ' CMAC-AES Error - Encryption Key length must be 16.'\
                        +' Please provide a valid one. %s'%custom_encrypt_key)

                encrypt_ecu_key = custom_encrypt_key
                bytes_to_encrypt = self.FEs

            encrypted_seed = self.cmac_encrypt( bytes_to_encrypt, encrypt_ecu_key )
            return encrypted_seed[:24]

        except Exception as error:
            print(__name__, type(error).__name__, error)

    def cmac_encrypt(self, data, key='43414E4469566120554E4C4B204B4559'):
        encrypt = CMAC.new(bytes.fromhex(key), ciphermod=AES)
        encrypt.update(bytes.fromhex(data))
        return encrypt.hexdigest()


if __name__ == '__main__':

    gen = Generate_Security_Key()
    seed = input('Please enter your seed:\n')
    print(gen.get_security_key(seed))
