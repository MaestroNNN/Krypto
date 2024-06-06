
def caesar_encrypt(text, key):
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            # Определяем смещение и диапазон в зависимости от регистра буквы
            offset = ord('A') if char.isupper() else ord('a')
            # Смещение символа и добавление к зашифрованному тексту
            encrypted_text.append(chr((ord(char) - offset + key) % 26 + offset))
        else:
            # Добавляем символ без изменений, если это не буква
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def caesar_decrypt(text, key):
    decrypted_text = []
    
    for char in text:
        if char.isalpha():
            # Определяем смещение и диапазон в зависимости от регистра буквы
            offset = ord('A') if char.isupper() else ord('a')
            # Обратное смещение символа и добавление к расшифрованному тексту
            decrypted_text.append(chr((ord(char) - offset - key) % 26 + offset))
        else:
            # Добавляем символ без изменений, если это не буква
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

# Пример использования:
import os
clear = lambda: os.system('cls')
clear()

plain_text = input("Введите текст ")
key = int(input("Введите ключ "))

encrypted_text = caesar_encrypt(plain_text, key)
print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, key)
print(f"Расшифрованный текст: {decrypted_text}")
