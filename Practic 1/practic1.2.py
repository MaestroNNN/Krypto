def caesar_encrypt(text, key):
    result = [] #  пустой список для хранения зашифрованного текста
    for char in text:
        if char.isalpha(): # Проверяем, является ли символ буквой
            shift = ord(char) + key # Вычисляем новый символ, сдвигая его на значение ключа

            if char.islower(): # Если символ - строчная буква
                result.append(chr((shift - ord('a')) % 26 + ord('a')))

            elif char.isupper():  # Если символ - заглавная буква
                result.append(chr((shift - ord('A')) % 26 + ord('A')))
        else:
            result.append(char) # Если символ не буква, добавляем его в исходном виде
    
    return ''.join(result) # Объединяем список символов в строку и возвращаем

def find_key(plain_text, cipher_text):
    for key in range(26):
        # Если зашифрованный текст с текущим ключом совпадает с данными зашифрованным текстом
        if caesar_encrypt(plain_text, key) == cipher_text:
            return key
    # Если не нашли соответствующий ключ, возвращаем None
    return None

# Пример использования:
import os
clear = lambda: os.system('cls')
clear()

plain_text = "Hello"  # Исходный текст
cipher_text = "Khoor"  # Зашифрованный текст
key = find_key(plain_text, cipher_text)  # Поиск ключа

print("Открытый текст:", plain_text)
print("Зашифрованный текст:", cipher_text)
if key is not None:
    print(f"найден ключ: {key}")  # Выводим ключ
else:
    print("Ключ не найден")  
