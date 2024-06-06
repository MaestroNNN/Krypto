import random

def generate_random_file(file_name, num_chars):
    """Генерирует файл из случайных символов."""
    with open(file_name, 'w') as f:
        for _ in range(num_chars):
            random_char = chr(random.randint(10, 100))
            f.write(random_char)

def vernam_cipher(input_file, key_file, output_file):
    """Реализует шифр Вернама для зашифрования/расшифрования файла."""
    with open(input_file, 'rb') as f:
        input_data = f.read()

    with open(key_file, 'rb') as f:
        key_data = f.read()

    # Применяем операцию XOR к соответствующим байтам входного файла и ключа
    encrypted_data = bytes(a ^ b for a, b in zip(input_data, key_data))

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)


# Генерируем файл ключа для шифра Вернама
generate_random_file('key_file.txt', 100)

# Зашифровываем файл с помощью шифра Вернама
vernam_cipher('input.txt', 'key_file.txt', 'encrypted.txt')

# Расшифровываем файл с помощью шифра Вернама
vernam_cipher('encrypted.txt', 'key_file.txt', 'decrypted.txt')
