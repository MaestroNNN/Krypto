from collections import Counter
import math

def calculate_frequencies(file_path):
    """Подсчет частоты появления символов в файле"""
    with open(file_path, 'r') as file:
        text = file.read()
    frequencies = Counter(text)
    total_characters = sum(frequencies.values())
    
    # Преобразование частот в доли от общего количества символов
    frequencies = {char: count / total_characters for char, count in frequencies.items()}
    
    return frequencies

def calculate_entropy(frequencies):
    """Вычисление энтропии по частотам"""
    entropy = -sum(freq * math.log2(freq) for freq in frequencies.values() if freq > 0)
    return entropy

# Пример использования:
file_path = '2.1-2.2.txt'

with open('2.1-2.2.txt', 'r') as f:
    words = f.read() 
print(f"Содержимое файла: {words}")

# Подсчет частот
frequencies = calculate_frequencies(file_path)
print("Частоты символов:")
for char, freq in frequencies.items():
    print(f"'{char}': {freq:.4f}")

# Вычисление энтропии
entropy = calculate_entropy(frequencies)
print(f"\nЭнтропия файла: {entropy:.4f}")
