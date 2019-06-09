
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

from pkcs12 import PKCS12

from aes import generate_random_secret_key


class RSACipher:

    def __init__(self):
        self._pubKey = None
        self._privKey = None

    def import_pubkey(self, public_key):
        """ public_key: PEM 
            暗号用
        """
        self._pubKey = RSA.importKey(public_key)

    def import_privkey(self, private_key):
        """ private_key: PEM 
            復号用
        """
        self._privKey = RSA.importKey(private_key)

    def encrypt(self, byte_data):
        if not self._pubKey:
            print("pubKey is not loaded")
            return
        pkcs1Cipher=PKCS1_OAEP.new(self._pubKey)
        encryptedString=pkcs1Cipher.encrypt(byte_data)
        return encryptedString

    def decrypt(self, encryptedString):
        if not self._privKey:
            print("privKey is not loaded")
            return
        pkcs1Cipher=PKCS1_OAEP.new(self._privKey)
        decryptedString=pkcs1Cipher.decrypt(encryptedString)
        return decryptedString


if __name__ == "__main__":
    # 簡易テスト
    rsa=RSACipher()
    with open(PKCS12.PUBLIC_KEY_FILENAME) as f:
        rsa.import_pubkey(f.read())

    with open(PKCS12.PRIVATE_KEY_FILENAME) as f:
        rsa.import_privkey(f.read())

    # 公開鍵で暗号化
    key =  generate_random_secret_key()
    print("encrypted key: {}".format(key))
    encryptedString = rsa.encrypt(key)
    # 秘密鍵で復号
    decryptedString = rsa.decrypt(encryptedString)
    print("decrypted key: {}".format(decryptedString))
