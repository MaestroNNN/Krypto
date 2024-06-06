import os
import random
import string

from practic_21_22 import calculate_frequencies, calculate_entropy

def generate_files():
    """Создание нескольких различных файлов с символами"""
    with open('file_same_chars.txt', 'w') as f:
        f.write('a' * 1000)

    with open('file_random_01.txt', 'w') as f:
        f.write(''.join(random.choice('01') for _ in range(1000)))

    with open('file_random_chars.txt', 'w') as f:
        f.write(''.join(random.choice(string.ascii_letters) for _ in range(1000)))

# Генерация файлов
generate_files()

# Анализ энтропии файлов
for file_name in ['file_same_chars.txt', 'file_random_01.txt', 'file_random_chars.txt']:
    frequencies = calculate_frequencies(file_name)
    entropy = calculate_entropy(frequencies)
    print(f"Файл: {file_name}")
    if file_name=='file_same_chars.txt':
        print("Файл с одним символом")
    if file_name=='file_random_01.txt':
        print("Файл с 0 и 1")
    if file_name=='file_random_chars.txt':
        print("Файл со случайными символами")
    print(f"Энтропия: {entropy:.4f}\n")