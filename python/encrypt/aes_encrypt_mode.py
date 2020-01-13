from Cryptodome.Cipher import AES
from hashlib import sha256
import secrets


import time

def start_time():
    return time.time()


def end_time(start_time, message):
    end_time = time.time()
     
    # 経過時間を表示
    elapsed_time = end_time - start_time
    print("{} 経過時間(s)：{}".format(message, elapsed_time))


def generate_random_secret_key(algorithm_func=sha256):
    return secrets.token_bytes(32)


# CTR
def ctr_encrypt(secret_key, raw_data, f=True):
    crypto = AES.new(secret_key, AES.MODE_CTR)
    if f:
        return dict(content=crypto.encrypt(raw_data),
                    nonce=crypto.nonce)
    else:
        return dict(content=raw_data,
                    nonce=crypto.nonce)


def ctr_decrypt(secret_key, encrypted_data, f=True):
    """ encrypted_data = dict(content, nonce) """
    crypto = AES.new(secret_key, AES.MODE_CTR, nonce=encrypted_data['nonce'])
    if f:
        return crypto.decrypt(encrypted_data['content'])
    else:
        return encrypted_data['content']


def ctr_encrypt_and_decrypt(secret_key, raw_data, f=True):
    encrypted_data = ctr_encrypt(secret_key, raw_data.encode(), f)
    return ctr_decrypt(secret_key, encrypted_data, f)


# GCM
def gcm_encrypt(secret_key, raw_data, f=True):
    crypto = AES.new(secret_key, AES.MODE_GCM)
    if f:
        content, tag = crypto.encrypt_and_digest(raw_data)
    else:
        content, tag = raw_data, None
    return dict(content=content, nonce=crypto.nonce, tag=tag)


def gcm_decrypt(secret_key, encrypted_data, f=True):
    crypto = AES.new(secret_key, AES.MODE_GCM, nonce=encrypted_data['nonce'])
    if f:
        return crypto.decrypt_and_verify(encrypted_data['content'], encrypted_data['tag'])
    else:
        return encrypted_data['content']


def gcm_encrypt_and_decrypt(secret_key, raw_data, f=True):
    encrypted_data = gcm_encrypt(secret_key, raw_data.encode(), f)
    return gcm_decrypt(secret_key, encrypted_data, f)


# OCB
def ocb_encrypt(secret_key, raw_data, f):
    crypto = AES.new(secret_key, AES.MODE_OCB)
    if f:
        content, tag = crypto.encrypt_and_digest(raw_data)
    else:
        content, tag = raw_data, None
    return dict(content=content, nonce=crypto.nonce, tag=tag)


def ocb_decrypt(secret_key, encrypted_data, f=True):
    crypto = AES.new(secret_key, AES.MODE_OCB, nonce=encrypted_data['nonce'])
    if f:
        return crypto.decrypt_and_verify(encrypted_data['content'], encrypted_data['tag'])
    else:
        return encrypted_data['content']


def ocb_encrypt_and_decrypt(secret_key, raw_data, f=True):
    encrypted_data = ocb_encrypt(secret_key, raw_data.encode(), f)
    return ocb_decrypt(secret_key, encrypted_data, f)


def encrypto_and_decrypto(key, raw_data):
    # 暗号/復号
    t = start_time()
    for i in range(100000):
        decrypted_data = ctr_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_CTR')
    print('{:.20}'.format(decrypted_data.decode()))

    t = start_time()
    for i in range(100000):
        decrypted_data = gcm_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_GCM')
    print('{:.20}'.format(decrypted_data.decode()))

    t = start_time()
    for i in range(100000):
        decrypted_data = ocb_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_OCB')
    print('{:.20}'.format(decrypted_data.decode()))

    # 非暗号/復号
    t = start_time()
    for i in range(100000):
        decrypted_data = ctr_encrypt_and_decrypt(key, raw_data, False)
    end_time(t, 'MODE_CTR (非暗号)')
    print('{:.20}'.format(decrypted_data.decode()))

    t = start_time()
    for i in range(100000):
        decrypted_data = gcm_encrypt_and_decrypt(key, raw_data, False)
    end_time(t, 'MODE_GCM (非暗号)')
    print('{:.20}'.format(decrypted_data.decode()))

    t = start_time()
    for i in range(100000):
        decrypted_data = ocb_encrypt_and_decrypt(key, raw_data, False)
    end_time(t, 'MODE_OCB (非暗号)')
    print('{:.20}'.format(decrypted_data.decode()))


if __name__ == "__main__":
    key = generate_random_secret_key()

    raw_data = 'raw_test_data'
    encrypto_and_decrypto(key, raw_data)

    raw_data = secrets.token_hex(65536)
    encrypto_and_decrypto(key, raw_data)
