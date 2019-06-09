from OpenSSL.crypto import load_pkcs12, FILETYPE_PEM
import OpenSSL
import os


class PKCS12:
    # input
    PKCS12_FILENAME = 'server.p12'

    # output
    PUBLIC_KEY_FILENAME = 'pubkey.pem'
    PRIVATE_KEY_FILENAME = 'privkey.pem'

    def __init__(self):
        pass

    def output(self):
        with open(self.PKCS12_FILENAME, 'rb') as f:
            c = f.read()
        
        p = None
        ### PKCS#12ファイルを読み込む
        try: 
            p = load_pkcs12(c, os.environ['P12_PASSWORD'])
        except OpenSSL.crypto.Error as e:
            print(e)
            return
         
        certificate = p.get_certificate()
        public_key = certificate.get_pubkey()
        private_key = p.get_privatekey()
          
        type_ = FILETYPE_PEM

        with open(self.PRIVATE_KEY_FILENAME, 'wb') as f:
            f.write(OpenSSL.crypto.dump_privatekey(type_, private_key))

        with open(self.PUBLIC_KEY_FILENAME, 'wb') as f:
            f.write(OpenSSL.crypto.dump_publickey(type_, public_key))


if __name__ == "__main__":
   p = PKCS12().output()
