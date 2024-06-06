def caesar_decrypt(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                result.append(chr((shift - ord('a')) % 26 + ord('a')))
            elif char.isupper():
                result.append(chr((shift - ord('A')) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def brute_force_decrypt(cipher_text): #Словарь для хранения возможных расшифрованных текстов
    possible_texts = {}
    for key in range(26):
        possible_texts[key] = caesar_decrypt(cipher_text, key)
    return possible_texts

def is_english_word(word, dictionary): #Находится ли слово в словаре
    return word.lower() in dictionary

def load_dictionary(file_path): #Загрузка словаря из файла
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file) #возврат множествва слов

def find_valid_decryption(cipher_text, dictionary): #Получение всех возможных расшифровок текста
    possible_texts = brute_force_decrypt(cipher_text)
    for key, text in possible_texts.items():
        words = text.split()
        if all(is_english_word(word, dictionary) for word in words):
            return key, text
    return None, None

# Пример использования:
import os
clear = lambda: os.system('cls')
clear()
dictionary = load_dictionary('dictionary.txt')
cipher_text = "Khoor"
key, text = find_valid_decryption(cipher_text, dictionary)

with open('dictionary.txt', 'r') as f:
    words = f.read().splitlines()  
words_in_line = ' '.join(words)
print(f"Содержимое словаря: {words_in_line}")
print("--------------------------------------------------")
print("Зашифрованный текст:", cipher_text)
if key is not None:
    print(f"Расшифрованный ключ: {key}")
    print(f"Расшифрованный текст из словаря: {text}")
else:
    print("Нет подходящего описания")