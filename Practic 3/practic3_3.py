
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

def encrypt(plaintext, key):
    nonce = os.urandom(16)  # Генерация случайного значения nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return nonce + ciphertext

def decrypt(ciphertext, key):
    nonce = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

# Генерация случайного ключа
key = os.urandom(32)

# Шифрование данных
plaintext = b"Hello, world!"
encrypted_data = encrypt(plaintext, key)
print("Исходный текст",plaintext)
print("Зашифрованные данные:", encrypted_data)

# Дешифрование данных
decrypted_data = decrypt(encrypted_data, key)
print("Дешифрованные данные:", decrypted_data)
