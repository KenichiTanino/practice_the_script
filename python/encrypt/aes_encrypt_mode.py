from Cryptodome.Cipher import AES
from hashlib import sha256
import random


import time

def start_time():
    return time.time()


def end_time(start_time, message):
    end_time = time.time()
     
    # 経過時間を表示
    elapsed_time = end_time - start_time
    print("{} 経過時間(s)：{}".format(message, elapsed_time))


def generate_random_secret_key(algorithm_func=sha256):
    return algorithm_func(str(random.random).encode('utf-8')).digest()


# CTR
def ctr_encrypt(secret_key, raw_data):
    crypto = AES.new(secret_key, AES.MODE_CTR)
    return dict(content=crypto.encrypt(raw_data),
                nonce=crypto.nonce)


def ctr_decrypt(secret_key, encrypted_data):
    """ encrypted_data = dict(content, nonce) """
    crypto = AES.new(secret_key, AES.MODE_CTR, nonce=encrypted_data['nonce'])
    return crypto.decrypt(encrypted_data['content'])


def ctr_encrypt_and_decrypt(secret_key, raw_data):
    encrypted_data = ctr_encrypt(secret_key, raw_data.encode())
    return ctr_decrypt(secret_key, encrypted_data)


# GCM
def gcm_encrypt(secret_key, raw_data):
    crypto = AES.new(secret_key, AES.MODE_GCM)
    content, tag = crypto.encrypt_and_digest(raw_data)
    return dict(content=content, nonce=crypto.nonce, tag=tag)


def gcm_decrypt(secret_key, encrypted_data):
    crypto = AES.new(secret_key, AES.MODE_GCM, nonce=encrypted_data['nonce'])
    return crypto.decrypt_and_verify(encrypted_data['content'], encrypted_data['tag'])


def gcm_encrypt_and_decrypt(secret_key, raw_data):
    encrypted_data = gcm_encrypt(secret_key, raw_data.encode())
    return gcm_decrypt(secret_key, encrypted_data)


# OCB
def ocb_encrypt(key, raw_data):
    crypto = AES.new(secret_key, AES.MODE_OCB)
    content, tag = crypto.encrypt_and_digest(raw_data)
    return dict(content=content, nonce=crypto.nonce, tag=tag)


def ocb_decrypt(key, encrypted_data):
    crypto = AES.new(secret_key, AES.MODE_OCB, nonce=encrypted_data['nonce'])
    return crypto.decrypt_and_verify(encrypted_data['content'], encrypted_data['tag'])


def ocb_encrypt_and_decrypt(secret_key, raw_data):
    encrypted_data = ocb_encrypt(secret_key, raw_data.encode())
    return ocb_decrypt(secret_key, encrypted_data)


if __name__ == "__main__":
    key = generate_random_secret_key()

    raw_data = 'raw_test_data'
    t = start_time()
    for i in range(100000):
        decrypted_data = ctr_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_CTR')
    print(decrypted_data)

    t = start_time()
    for i in range(100000):
        decrypted_data = gcm_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_GCM')
    print(decrypted_data)

    t = start_time()
    for i in range(100000):
        decrypted_data = gcm_encrypt_and_decrypt(key, raw_data)
    end_time(t, 'MODE_OCB')
    print(decrypted_data)
