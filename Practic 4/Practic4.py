import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Генерация случайного ключа и IV (инициализационного вектора)
def generate_key_iv():
    key = os.urandom(32)  # AES-256 ключ
    iv = os.urandom(16)  # IV для режима CBC
    return key, iv

# Шифрование данных
def encrypt(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_data

# Расшифрование данных
def decrypt(encrypted_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data

# Шифрование файла
def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = encrypt(data, key, iv)
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)  # Сохраняем IV в начале файла

# Расшифрование файла и вывод содержимого в консоль
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # IV находится в начале файла
        encrypted_data = f.read()
    decrypted_data = decrypt(encrypted_data, key, iv)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    # Вывод содержимого расшифрованного файла в консоль
    return decrypted_data

if __name__ == "__main__":
    # Генерация ключа и IV
    key, iv = generate_key_iv()

    # Пути к файлам
    input_file = 'input.txt'
    encrypted_file = 'encrypted.bin'
    decrypted_file = 'decrypted.txt'

    # Шифрование файла
    encrypt_file(input_file, encrypted_file, key, iv)
    print(f"Файл {input_file} зашифрован и сохранен как {encrypted_file}")

    # Расшифрование файла и вывод содержимого в консоль
    decrypted_data = decrypt_file(encrypted_file, decrypted_file, key)
    print(f"Файл {encrypted_file} расшифрован и сохранен как {decrypted_file}")

    # Вывод содержимого файлов
    with open(input_file, 'r') as f:
        original_data = f.read()
    print(f"\nСодержимое исходного файла ({input_file}):")
    print(original_data)

    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    print(f"\nСодержимое зашифрованного файла ({encrypted_file}):")
    print(encrypted_data)

    print(f"\nСодержимое расшифрованного файла ({decrypted_file}):")
    print(decrypted_data.decode('utf-8'))
